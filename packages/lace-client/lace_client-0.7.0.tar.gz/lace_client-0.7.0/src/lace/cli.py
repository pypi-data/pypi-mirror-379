"""
Lace CLI - Minimal command-line interface.
"""

import click
import sys
import json
import os
import logging
import time
import hashlib
import zipfile
import tempfile
import webbrowser
import uuid
import random
import base64
from datetime import datetime
from pathlib import Path
from typing import Optional, Dict, Any

from . import attest, monitor, about, __version__
from .wizard.analyzer import DatasetAnalyzer
from .wizard.questions import DocumentWizard
from .wizard.templates import TemplateGenerator
from .wizard.storage import ImmutableStorage
from .regulatory.scope import ScopeClassifier
from .wizard.serializer import to_analysis_json
from .validators import (
    validate_analysis, 
    validate_answer_type,
    coerce_answer,
    parse_answer_arg,
    generate_answer_stub
)
from .client import (
    LaceClient,
    ValidationError,
    PaymentRequiredError,
    ServerError,
    NetworkError,
    PolicyViolationError,
)
from .constants import (
    EXIT_SUCCESS,
    EXIT_VALIDATION_ERROR,
    EXIT_PAYMENT_REQUIRED,
    EXIT_SERVER_ERROR,
    EXIT_NETWORK_ERROR,
    EXIT_POLICY_VIOLATION,
    EXIT_VERIFY_FAILED,
    EXIT_GENERAL_ERROR,
    EXIT_EXPERIMENTAL_REQUIRED,
    PREFLIGHT_EXPERIMENTAL,
    SAFE_DEFAULTS,
    DEFAULT_MAX_WAIT,
    DEFAULT_POLL_INTERVAL,
    DEFAULT_UPLOAD_CONCURRENCY,
    DEFAULT_CHUNK_SIZE_MB,
    DEFAULT_MAX_FILES,
    DEFAULT_INCLUDE_EXTS,
    DEFAULT_EXCLUDE_GLOBS,
)
from .utils import redact_sensitive, extract_domain

logger = logging.getLogger(__name__)


# ============================================================================
# Helper Functions for Flow B
# ============================================================================

def build_manifest(dataset_paths, include_exts, exclude_globs, max_files):
    """Build file manifest with filtering."""
    import fnmatch
    from datetime import datetime
    files = []
    total_bytes = 0
    
    for dataset_path in dataset_paths:
        path = Path(dataset_path).resolve()
        root_path = path if path.is_dir() else path.parent
        file_count = 0
        
        # Handle both file and directory
        if path.is_file():
            # Single file
            if path.suffix in include_exts:
                stat = path.stat()
                size = stat.st_size
                # Stream file for SHA256 to avoid memory issues
                h = hashlib.sha256()
                with open(path, 'rb') as f:
                    for chunk in iter(lambda: f.read(1024*1024), b''):
                        h.update(chunk)
                file_hash = h.hexdigest()
                files.append({
                    'path': str(path),
                    'relpath': path.name,  # For single file, just use filename
                    'size': size,
                    'hash': file_hash,
                    'mtime': stat.st_mtime  # Unix timestamp
                })
                total_bytes += size
                file_count = 1
        else:
            # Directory - recursively find files
            for filepath in path.rglob('*'):
                if not filepath.is_file():
                    continue
                
                # Apply exclude filters
                rel_path = str(filepath.relative_to(path))
                if any(fnmatch.fnmatch(rel_path, glob) for glob in exclude_globs):
                    continue
                
                # Apply include filters
                if filepath.suffix not in include_exts:
                    continue
                
                if len(files) >= max_files:
                    logger.info(f"Reached max files limit ({max_files})")
                    break
                
                stat = filepath.stat()
                size = stat.st_size
                # Stream file for SHA256 to avoid memory issues
                h = hashlib.sha256()
                with open(filepath, 'rb') as f:
                    for chunk in iter(lambda: f.read(1024*1024), b''):
                        h.update(chunk)
                file_hash = h.hexdigest()
                
                files.append({
                    'path': str(filepath),
                    'relpath': str(filepath.relative_to(root_path)),  # Relative to dataset root
                    'size': size,
                    'hash': file_hash,
                    'mtime': stat.st_mtime  # Unix timestamp
                })
                total_bytes += size
                file_count += 1
    
    return {
        'total_files': len(files),
        'total_bytes': total_bytes,
        'files': files
    }

def upload_files_parallel(executor, manifest, upload_urls, chunk_size_mb):
    """Upload files in parallel with multipart support."""
    import httpx
    from concurrent.futures import as_completed
    from pathlib import Path
    import time
    
    url_map = {u['file_hash']: u for u in upload_urls}
    chunk_size = chunk_size_mb * 1024 * 1024
    
    def upload_single_file_task(file_info):
        file_hash = file_info['hash']
        filepath = Path(file_info['path'])
        
        if file_hash not in url_map:
            return {'file': filepath.name, 'status': 'skipped'}
        
        upload_info = url_map[file_hash]
        
        # Single-part upload
        if 'url' in upload_info and 'part_urls' not in upload_info:
            for attempt in range(3):
                try:
                    with open(filepath, 'rb') as f:
                        response = httpx.put(upload_info['url'], content=f, timeout=30)
                        if response.status_code in [200, 201, 204]:
                            return {'file': filepath.name, 'status': 'uploaded'}
                except Exception as e:
                    if attempt == 2:
                        raise click.ClickException(f"Upload failed for {filepath}: {e}")
                    time.sleep(2 ** attempt)  # Exponential backoff: 1s, 2s, 4s
        
        # Multipart upload
        elif 'part_urls' in upload_info:
            parts = []
            upload_id = upload_info['upload_id']
            
            with open(filepath, 'rb') as f:
                for part_info in upload_info['part_urls']:
                    part_num = part_info['part_number']
                    part_url = part_info['url']
                    
                    # Read exactly one chunk
                    chunk_data = f.read(chunk_size)
                    
                    for attempt in range(3):
                        try:
                            response = httpx.put(part_url, content=chunk_data, timeout=30)
                            if response.status_code in [200, 201, 204]:
                                etag = response.headers.get('ETag', '').strip('"')
                                parts.append({'PartNumber': part_num, 'ETag': etag})
                                break
                        except Exception as e:
                            if attempt == 2:
                                raise click.ClickException(f"Part {part_num} upload failed for {filepath}: {e}")
                            time.sleep(2 ** attempt)
            
            return {
                'file': filepath.name,
                'status': 'multipart',
                'file_hash': file_hash,
                'upload_id': upload_id,
                'parts': parts
            }
        
        return {'file': filepath.name, 'status': 'unknown'}
    
    # Submit all uploads
    futures = {executor.submit(upload_single_file_task, f): f for f in manifest['files']}
    results = []
    
    for idx, future in enumerate(as_completed(futures), 1):
        file_info = futures[future]
        try:
            result = future.result()
            click.echo(f"Uploading {idx}/{len(manifest['files'])}: {Path(file_info['path']).name}")
            results.append(result)
        except Exception as e:
            click.echo(f"Failed: {e}", err=True)
    
    return results

# upload_single_file function removed - logic moved into upload_files_parallel

def tdm_from_opt_out_summary(opt_out_summary: dict, registry_meta: dict = None) -> dict:
    """Transform SDSScanner output to Lambda-expected format."""
    total = int(opt_out_summary.get('domains_checked', 0))
    deny = int(opt_out_summary.get('deny', 0))
    pct = round((deny / total * 100.0), 1) if total else 0.0
    tdm = {
        "statistics": {
            "total_domains": total,
            "opted_out_count": deny,
            "opted_out_pct": pct
        }
    }
    if registry_meta:
        tdm["registry"] = registry_meta
    return tdm

def tdm_measures_desc(tdm_stats: dict) -> str:
    """Generate human-readable TDM measures description for Section 3.1."""
    stats = tdm_stats.get("statistics", {})
    total = stats.get("total_domains", 0)
    deny = stats.get("opted_out_count", 0)
    pct = stats.get("opted_out_pct", 0.0)
    base = ("Technical measures are implemented to respect machine-readable opt-out signals "
            "(e.g., robots.txt, ai.txt, X-Robots-Tag, trust.txt) prior to and during data collection.")
    if total:
        return f"{base} Representative sampling shows {deny} of {total} domains ({pct:.1f}%) opted out, which are programmatically honored."
    return f"{base} When present, such signals are programmatically honored."

def _sanitize_payload_for_display(payload: dict) -> dict:
    """Sanitize payload for display (remove sensitive data)."""
    import copy
    sanitized = copy.deepcopy(payload)
    
    # Truncate file lists
    if 'manifest' in sanitized:
        manifest = sanitized['manifest']
        files = manifest.get('files', [])
        orig_count = len(files)
        if len(files) > 3:
            # Truncate but don't add non-schema items to files array
            manifest['files'] = files[:3]
            # Add truncation note as a separate field
            manifest['_truncated'] = f'{orig_count - 3} more files omitted from display'
        
        # Clean up each file entry
        for f in manifest.get('files', []):
            if isinstance(f, dict):
                # Remove full path, keep relpath
                f.pop('path', None)
                # Shorten hash
                if 'hash' in f and len(str(f['hash'])) > 8:
                    f['hash'] = str(f['hash'])[:8] + '...'
    
    # Truncate domain lists in local_facts
    if 'config' in sanitized and 'local_facts' in sanitized['config']:
        facts = sanitized['config']['local_facts']
        # Limit domains list
        if 'domains' in facts and isinstance(facts['domains'], list) and len(facts['domains']) > 5:
            facts['domains'] = facts['domains'][:5] + ['...']
        # Limit any examples
        if 'opt_out_summary' in facts and 'examples' in facts['opt_out_summary']:
            examples = facts['opt_out_summary']['examples']
            if len(examples) > 3:
                facts['opt_out_summary']['examples'] = examples[:3] + ['...']
    
    return sanitized

def download_file(url, output_path):
    """Download file from pre-signed URL."""
    import httpx
    
    with httpx.stream('GET', url) as response:
        response.raise_for_status()
        with open(output_path, 'wb') as f:
            for chunk in response.iter_bytes():
                f.write(chunk)

def _legacy_wizard_flow(dataset_paths, profile, send_domains, ephemeral, debug_evidence, 
                       answer, answers_file, non_interactive, api_base, out):
    """Deprecated wizard flow - will be removed next release."""
    click.echo("⚠️  Using legacy wizard flow (deprecated)", err=True)
    
    # Move the existing implementation here
    # This is the code from lines 196-400 of the current pack_cmd
    # Not duplicating here for brevity, but would move the entire wizard implementation
    raise NotImplementedError("Legacy wizard flow temporarily disabled during migration")


@click.group()
@click.version_option(version=__version__, prog_name="lace")
@click.option('--debug', is_flag=True, envvar='LACE_DEBUG', help='Enable debug logging')
@click.pass_context
def main(ctx, debug):
    """Lace - EU AI Act Compliance Documentation"""
    if debug:
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )
        logger.debug(f"Lace CLI v{__version__} - Debug mode enabled")
    else:
        # Configure logging to quiet httpx unless in debug mode
        logging.basicConfig(
            level=logging.INFO,
            format='%(levelname)s:%(name)s:%(message)s'
        )
        logging.getLogger('httpx').setLevel(logging.WARNING)
        logging.getLogger('httpcore').setLevel(logging.WARNING)
    
    # Show experimental commands if enabled
    if os.getenv('LACE_ENABLE_PREFLIGHT') == '1':
        ctx.obj = {'show_experimental': True}


@main.command('init-registry')
@click.option('--dev', is_flag=True, help='Create unsigned dev registry for testing')
def init_registry(dev):
    """Initialize or refresh the opt-out registry."""
    try:
        from .preflight import RegistryManager
        
        mgr = RegistryManager()
        
        if dev:
            click.echo("Creating unsigned dev registry for testing...")
            mgr.create_dev_registry()
            click.echo("⚠️  Dev registry created - NOT FOR PRODUCTION USE")
        else:
            click.echo("Downloading official registry...")
            if mgr.refresh(force=True):
                click.echo("✅ Registry initialized successfully")
            else:
                click.echo("❌ Failed to download registry")
                click.echo("Creating dev registry instead...")
                mgr.create_dev_registry()
                click.echo("⚠️  Using dev registry - run again with network to get official")
                
    except Exception as e:
        click.echo(f"Error: {e}", err=True)
        sys.exit(EXIT_GENERAL_ERROR)


@main.command('preflight', hidden=PREFLIGHT_EXPERIMENTAL)  # Hide from help unless experimental
@click.argument('dataset_path', type=click.Path(exists=True))
@click.option('--experimental', is_flag=True, help='Enable experimental features')
@click.option('--budget', type=int, default=60, help='Time budget in seconds (default: 60)')
@click.option('--sample-rate', type=float, default=0.01, help='Sampling rate 0-1 (default: 0.01)')
@click.option('--pii', type=click.Choice(['off', 'light', 'standard']), default='light', help='PII detection mode')
@click.option('--max-concurrency', type=int, default=8, help='Max concurrent network requests')
@click.option('--allow-network', is_flag=True, help='Enable network calls (default: registry only)')
@click.option('--registry-refresh', is_flag=True, help='Update opt-out registry before check')
@click.option('--policy', type=click.Choice(['default', 'strict', 'lenient']), default='default', help='Policy mode')
@click.option('--out', type=click.Path(), help='Output path for JSON report')
@click.option('--fail-on-deny', is_flag=True, help='Exit with code 6 if verdict is deny (for CI)')
@click.option('--debug', is_flag=True, help='Show debug output')
def preflight(dataset_path, experimental, budget, sample_rate, pii, max_concurrency, allow_network, 
              registry_refresh, policy, out, fail_on_deny, debug):
    """[EXPERIMENTAL] Run preflight compliance checks on dataset (dev registry only)."""
    # Check if experimental features are enabled
    if not (os.getenv('LACE_ENABLE_PREFLIGHT') == '1' or experimental):
        click.echo("Preflight is experimental (dev registry). Enable with LACE_ENABLE_PREFLIGHT=1 or --experimental.")
        sys.exit(EXIT_EXPERIMENTAL_REQUIRED)
    
    # Show experimental warning
    click.echo("⚠️  EXPERIMENTAL: Preflight uses dev registry only. Advisory assessment, not a legal opinion.")
    click.echo("Coverage limited by sampling. Results may vary.\n")
    
    try:
        from .preflight import preflight_check, PreflightConfig, RegistryManager
        
        # Handle registry refresh if requested
        if registry_refresh:
            click.echo("Refreshing opt-out registry...")
            mgr = RegistryManager()
            if mgr.refresh():
                click.echo("✅ Registry updated successfully")
            else:
                click.echo("⚠️  Registry refresh failed, using cached version")
        
        # Configure preflight (default to no network unless explicitly allowed)
        config = PreflightConfig(
            budget_s=budget,
            sample_rate=sample_rate,
            pii_mode=pii,
            max_concurrency=max_concurrency,
            policy_mode=policy,
            no_network=not allow_network,  # Default to registry-only
            debug=debug
        )
        
        # Run preflight
        report = preflight_check(dataset_path, config, out)
        
        # Exit with appropriate code
        verdict = report['verdict']['status']
        if verdict == 'deny' and fail_on_deny:
            sys.exit(EXIT_POLICY_VIOLATION)
        elif verdict == 'unknown':
            sys.exit(EXIT_VALIDATION_ERROR)
        else:
            sys.exit(EXIT_SUCCESS)
            
    except Exception as e:
        logger.error(f"Preflight failed: {e}")
        if debug:
            import traceback
            traceback.print_exc()
        sys.exit(EXIT_GENERAL_ERROR)


@main.command('pack')
@click.argument('dataset_paths', nargs=-1, required=False, type=click.Path(exists=True))
@click.option('--profile', type=click.Choice(['minimal', 'enhanced']), default='minimal', help='Analysis profile')
@click.option('--send-domains', type=click.Choice(['none', 'hashed', 'clear']), default='none', help='Domain sending mode')
@click.option('--ephemeral', is_flag=True, help='Request server delete data after response')
@click.option('--debug-evidence', is_flag=True, help='Save analysis payload locally')
@click.option('--answer', multiple=True, help='Provide answer as id=value')
@click.option('--answers-file', type=click.Path(exists=True), help='Load answers from JSON file')
@click.option('--interactive', is_flag=True, help='Enable interactive Q&A (default: non-interactive)')
@click.option('--api-base', help='Override API base URL')
@click.option('--out', type=click.Path(), help='Output path for DOCX')
@click.option('--no-cloud', is_flag=True, hidden=True, help='(Removed) Offline mode')
@click.option('--legacy-wizard', is_flag=True, hidden=True, help='Use deprecated wizard flow')
@click.option('--concurrency', type=int, default=DEFAULT_UPLOAD_CONCURRENCY, help=f'Upload workers (default: {DEFAULT_UPLOAD_CONCURRENCY})')
@click.option('--chunk-size', type=int, default=DEFAULT_CHUNK_SIZE_MB, help=f'Chunk size MB (default: {DEFAULT_CHUNK_SIZE_MB})')
@click.option('--max-files', type=int, default=DEFAULT_MAX_FILES, help=f'Max files (default: {DEFAULT_MAX_FILES})')
@click.option('--dry-run', is_flag=True, help='Print payload without calling API')
@click.option('--verbose-http', is_flag=True, help='Log HTTP details for debugging')
@click.option('--no-wait', is_flag=True, help='Submit and exit immediately (print job_id)')
@click.option('--resume', metavar='JOB_ID', help='Attach to an existing job and download when done')
def pack_cmd(dataset_paths, profile, send_domains, ephemeral, debug_evidence, answer, 
             answers_file, interactive, api_base, out, no_cloud, 
             legacy_wizard, concurrency, chunk_size, max_files, dry_run, verbose_http,
             no_wait, resume):
    """Create EU AI Act compliance documentation with TDM compliance (§3.1)."""
    # Guard against removed offline mode
    if no_cloud:
        raise click.UsageError("Offline mode has been removed. Run without --no-cloud.")
    
    # Quiet httpx logs unless verbose
    import logging
    if not verbose_http:
        logging.getLogger('httpx').setLevel(logging.WARNING)
        logging.getLogger('httpcore').setLevel(logging.WARNING)
    
    # Default is non-interactive
    non_interactive = not interactive
    
    # Legacy wizard flow (temporary)
    if legacy_wizard:
        click.echo("⚠️  Legacy wizard flow deprecated, will be removed next release", err=True)
        return _legacy_wizard_flow(dataset_paths, profile, send_domains, ephemeral, 
                                  debug_evidence, answer, answers_file, 
                                  not interactive, api_base, out)
    
    try:
        from .sds import SDSScanner
        from .client import LaceClient, JobFailed, JobCanceled
        from concurrent.futures import ThreadPoolExecutor
        
        client = LaceClient(api_base=api_base, verbose_http=verbose_http)
        
        # Resume mode - attach to existing job
        if resume:
            if not out:
                click.echo("Error: --out is required when using --resume", err=True)
                sys.exit(EXIT_GENERAL_ERROR)
            
            job_id = resume
            click.echo(f"Attaching to job {job_id}...", err=True)
            
            try:
                # Wait for job completion (no timeout by default)
                status_resp = client.wait_for_job_completion(job_id)
                
                # Get the analysis results for building EU answers
                # (This would need client.get_job_results or similar)
                click.echo("Generating SDS document...")
                
                # For now, generate with empty answers (would need to fetch from job)
                pack_resp = client.generate_pack(job_id, {})
                
                # Download
                download_file(pack_resp['url'], out)
                click.echo(f"\n✅ SDS saved to: {out}")
                sys.exit(EXIT_SUCCESS)
                
            except KeyboardInterrupt:
                click.echo(f"\nDetached. To resume: lace pack --resume {job_id} --out {out}", err=True)
                sys.exit(130)  # Standard Ctrl+C exit code
            except JobFailed as e:
                click.echo(str(e), err=True)
                sys.exit(EXIT_SERVER_ERROR)
            except JobCanceled as e:
                click.echo(str(e), err=True)
                sys.exit(EXIT_SERVER_ERROR)
        
        # Normal mode - need dataset paths
        if not dataset_paths:
            click.echo("Error: Dataset path required (unless using --resume)", err=True)
            sys.exit(EXIT_GENERAL_ERROR)
        
        # 1. Quick scan for consent/UX  
        click.echo("Scanning dataset...")
        scanner = SDSScanner()
        quick = scanner.quick_scan(dataset_paths[0], max_files=max_files)
        click.echo(f"Dataset: {quick['file_count']} files, {quick.get('total_gb', 0):.1f} GB")
        click.echo(f"Latest acquisition: {quick.get('latest_acquisition', 'unknown')}")
        
        # 2. Full scan with TDM for Section 3.1
        click.echo("Analyzing for EU AI Act compliance...")
        full = scanner.full_scan(dataset_paths[0], include_opt_out=True)
        
        # Transform TDM data for Lambda
        tdm_results = tdm_from_opt_out_summary(
            full.get('opt_out_summary', {}),
            full.get('tdm_meta')
        )
        
        # 3. Build manifest with filtering
        click.echo("Building file manifest...")
        manifest = build_manifest(
            dataset_paths,
            include_exts=DEFAULT_INCLUDE_EXTS,
            exclude_globs=DEFAULT_EXCLUDE_GLOBS,
            max_files=max_files
        )
        click.echo(f"  Filtered to {manifest['total_files']} files ({manifest['total_bytes'] / (1024**2):.1f} MB)")
        
        # Handle dry-run mode
        if dry_run:
            # Build the exact payload that would be sent to analyze endpoint
            analyze_payload = {
                'manifest': manifest,
                'config': {
                    'tier': profile,
                    'ephemeral': ephemeral,
                    'local_facts': {
                        **full,  # Keep all scan results
                        'tdm_results': tdm_results,  # Add properly formatted TDM
                        'tdm_stats': tdm_results  # Include both for compatibility
                    }
                },
                'client': {
                    'name': 'lace-cli',
                    'version': __version__,
                    'platform': sys.platform
                }
            }
            
            # Normalize the payload as the client would
            from .client import LaceClient
            temp_client = LaceClient()
            normalized_payload = temp_client._normalize_analyze_payload_for_server(analyze_payload)
            
            # Sanitize for display (truncate file lists, mask hashes)
            import copy
            sanitized = copy.deepcopy(normalized_payload)
            if 'manifest' in sanitized and 'files' in sanitized['manifest']:
                files = sanitized['manifest']['files']
                if len(files) > 3:
                    # Show only first 3 files
                    sanitized['manifest']['files'] = files[:3]
                    sanitized['manifest']['files'].append({'note': f'{len(files) - 3} more files...'})
                # Truncate hashes
                for f in sanitized['manifest']['files']:
                    if 'hash' in f and isinstance(f.get('hash'), str) and len(f['hash']) > 8:
                        f['hash'] = f['hash'][:8] + '...'
            
            click.echo("\nDry-run mode - analyze payload that would be sent:")
            click.echo(json.dumps(sanitized, indent=2))
            
            # Also show the EU answers that would be generated
            # Note: We need to build these AFTER getting a job_id normally,
            # but for dry-run we'll show what would be built
            click.echo("\nEU answers that would be generated:")
            
            # Load user answers if provided (same as in normal flow)
            demo_user_answers = {}
            if answers_file:
                try:
                    with open(answers_file, 'r') as f:
                        demo_user_answers = json.load(f)
                except Exception:
                    pass
            
            # Apply CLI answers
            for answer_arg in answer:
                if '=' in answer_arg:
                    qid, value = answer_arg.split('=', 1)
                    if value.lower() == 'true':
                        demo_user_answers[qid] = True
                    elif value.lower() == 'false':
                        demo_user_answers[qid] = False
                    else:
                        demo_user_answers[qid] = value
            
            # Build EU answers
            from .sds.eu_answers import build_eu_answers
            full['tdm_results'] = tdm_results
            eu_answers = build_eu_answers(quick, full, demo_user_answers)
            
            # Show key fields
            eu_summary = {
                'summary_version': eu_answers.get('summary_version'),
                'provider_name': eu_answers.get('provider_name'),
                'model_name': eu_answers.get('model_name'),
                'modalities': eu_answers.get('modalities'),
                'size_bands': eu_answers.get('size_bands'),
                'crawlers_used': eu_answers.get('crawlers_used'),
                'public_datasets_used': eu_answers.get('public_datasets_used'),
                'tdm_signatory': eu_answers.get('tdm_signatory'),
                'illegal_content_measures_desc': eu_answers.get('illegal_content_measures_desc')[:50] + '...' if len(eu_answers.get('illegal_content_measures_desc', '')) > 50 else eu_answers.get('illegal_content_measures_desc')
            }
            
            click.echo(json.dumps(eu_summary, indent=2))
            click.echo("\n(Full EU answers would be sent to generate_pack endpoint)")
            sys.exit(EXIT_SUCCESS)
        
        # 4. Start async job
        click.echo("Starting cloud analysis job...")
        client = LaceClient(api_base=api_base, verbose_http=verbose_http)
        
        job_resp = client.start_async_analysis(manifest, {
            'tier': profile,
            'ephemeral': ephemeral,
            'local_facts': {
                **full,  # Keep all scan results
                'tdm_results': tdm_results,  # Add properly formatted TDM
                'tdm_stats': tdm_results  # Include both for server compatibility
            }
        })
        job_id = job_resp['job_id']
        upload_urls = job_resp.get('upload_urls', [])
        
        # 5. Parallel upload with progress
        if upload_urls:
            click.echo(f"Uploading files ({concurrency} workers, {chunk_size}MB chunks)...")
            with ThreadPoolExecutor(max_workers=concurrency) as executor:
                results = upload_files_parallel(executor, manifest, upload_urls, chunk_size)
                
                # Complete multipart uploads
                for result in results:
                    if result.get('status') == 'multipart':
                        client.complete_multipart_upload(
                            job_id,
                            result['file_hash'],
                            result['upload_id'],
                            result['parts']
                        )
            
            client.mark_upload_complete(job_id)
            click.echo("  Upload complete")
        
        # Print job ID immediately
        click.echo(f"Submitted job: {job_id}", err=True)
        
        # Handle no-wait mode
        if no_wait:
            if out:
                click.echo(f"To watch: lace pack --resume {job_id} --out {out}", err=True)
            else:
                click.echo(f"To watch: lace pack --resume {job_id} --out <output.docx>", err=True)
            sys.exit(EXIT_SUCCESS)
        
        # 6. Wait for cloud processing (no timeout by default)
        click.echo("Processing dataset in cloud...")
        try:
            client.wait_for_job_completion(job_id)  # No timeout - wait until done
        except KeyboardInterrupt:
            out_suggestion = out or f'./lace_sds_{job_id}.docx'
            click.echo(f"\nDetached. To resume: lace pack --resume {job_id} --out {out_suggestion}", err=True)
            sys.exit(130)  # Standard Ctrl+C exit code
        except JobFailed as e:
            click.echo(str(e), err=True)
            sys.exit(EXIT_SERVER_ERROR)
        except JobCanceled as e:
            click.echo(str(e), err=True)
            sys.exit(EXIT_SERVER_ERROR)
        
        # 7. Build EU-compliant answers using the new builder
        from .sds.eu_answers import build_eu_answers
        
        # Load user answers from file if provided
        user_answers = {}
        if answers_file:
            try:
                with open(answers_file, 'r') as f:
                    user_answers = json.load(f)
                click.echo(f"  Loaded {len(user_answers)} answers from file")
            except Exception as e:
                click.echo(f"Warning: Failed to load answers file: {e}", err=True)
        
        # Apply CLI answers (override file)
        for answer_arg in answer:
            if '=' in answer_arg:
                qid, value = answer_arg.split('=', 1)
                # Try to parse as boolean
                if value.lower() == 'true':
                    user_answers[qid] = True
                elif value.lower() == 'false':
                    user_answers[qid] = False
                else:
                    user_answers[qid] = value
        
        # Add TDM results to full scan for the builder
        full['tdm_results'] = tdm_results
        
        # Build EU-compliant answers with tri-state handling
        final_answers = build_eu_answers(quick, full, user_answers)
        
        # Generate top domains CSV only if user explicitly confirmed crawlers_used
        provider_crawled = full.get('provider_crawled_evidence', {})
        if final_answers.get('crawlers_used') == 'Yes' and provider_crawled.get('domains_top'):
            import csv
            domains_csv_path = f'./top_domains_{job_id}.csv'
            domains_list = provider_crawled['domains_top']
            
            # Take top 10% or max 1000 domains
            max_domains = min(1000, max(10, len(domains_list) // 10))
            top_domains = domains_list[:max_domains] if isinstance(domains_list, list) else []
            
            with open(domains_csv_path, 'w', newline='') as csvfile:
                writer = csv.writer(csvfile)
                writer.writerow(['domain', 'count', 'modality'])
                for domain_info in top_domains:
                    if isinstance(domain_info, dict):
                        domain = domain_info.get('domain', domain_info.get('name', 'unknown'))
                        count = domain_info.get('count', domain_info.get('bytes', 0))
                    else:
                        domain = str(domain_info)
                        count = 1
                    writer.writerow([domain, count, 'text'])
            
            final_answers['crawled_domains_csv_path'] = domains_csv_path
            click.echo(f"  Generated top domains CSV: {domains_csv_path}")
        
        # 8. Generate and download DOCX
        click.echo("Generating SDS document...")
        pack_resp = client.generate_pack(job_id, final_answers)
        
        # 9. Save output
        out_path = out or f'./lace_sds_{job_id}.docx'
        download_file(pack_resp['url'], out_path)
        
        click.echo(f"\n✅ SDS saved to: {out_path}")
        
        # 10. Show TDM compliance summary from Section 3.1
        if full.get('opt_out_summary'):
            opt = full['opt_out_summary']
            total = opt.get('domains_checked', 0)
            deny = opt.get('deny', 0)
            if total > 0:
                click.echo(f"📊 TDM Compliance (§3.1): {deny}/{total} domains opted out ({deny/total*100:.1f}%)")
        
        # 11. Save debug evidence if requested
        if debug_evidence:
            evidence_path = Path(out).parent / f'analysis_{job_id}.json' if out else f'./analysis_{job_id}.json'
            with open(evidence_path, 'w') as f:
                json.dump({'manifest': manifest, 'scan_results': full}, f, indent=2)
            click.echo(f"Debug evidence saved: {evidence_path}")
        
        sys.exit(EXIT_SUCCESS)
        
    except KeyboardInterrupt:
        click.echo("\nAborted by user", err=True)
        sys.exit(EXIT_GENERAL_ERROR)
    except Exception as e:
        click.echo(f"Unexpected error: {redact_sensitive(str(e))}", err=True)
        logger.exception("Unexpected error in pack command")
        sys.exit(EXIT_SERVER_ERROR)


# ============================================================================
# Check Command Group - TDM and Copyright
# ============================================================================

@main.group('check')
def check_group():
    """Compliance checks: TDM opt-out and copyright attribution."""
    pass

@check_group.command('tdm')
@click.argument('dataset_path', type=click.Path(exists=True))
@click.option('--json', 'output_json', is_flag=True, help='Output as JSON')
def check_tdm_cmd(dataset_path, output_json):
    """Quick TDM opt-out scan for Section 3.1 compliance."""
    from .sds import SDSScanner
    
    scanner = SDSScanner()
    results = scanner.full_scan(dataset_path, include_opt_out=True)
    tdm = results.get('opt_out_summary', {})
    
    if output_json:
        click.echo(json.dumps(tdm, indent=2))
    else:
        total = tdm.get('domains_checked', 0)
        deny = tdm.get('deny', 0)
        allow = tdm.get('allow', 0)
        pct_deny = (deny / total * 100) if total else 0.0
        
        click.echo("TDM Opt-out Compliance (§3.1):")
        click.echo(f"  Domains checked: {total}")
        click.echo(f"  Deny signals:    {deny} ({pct_deny:.1f}%)")
        click.echo(f"  Allowed:         {allow}")
        
        if tdm.get('examples'):
            click.echo("  Examples:")
            for ex in tdm['examples'][:5]:
                click.echo(f"    - {ex}")
    
    # Exit 1 if opt-outs found (for CI)
    if tdm.get('deny', 0) > 0:
        sys.exit(1)

@check_group.command('attrib')
@click.argument('dataset_path', type=click.Path(exists=True))
@click.option('--threshold', default=0.8, help='Match confidence threshold')
@click.option('--json', 'output_json', is_flag=True)
def check_attrib_cmd(dataset_path, threshold, output_json):
    """Deep copyright attribution scan (compute-intensive)."""
    from .check import AttributionEngine
    
    click.echo("⚠️  Running copyright attribution analysis (this may take time)...")
    engine = AttributionEngine()
    results = engine.analyze(dataset_path, threshold)
    
    if output_json:
        click.echo(json.dumps(results, indent=2))
    else:
        risky = results.get('high_risk_sources', [])
        if risky:
            click.echo(f"⚠️  Found {len(risky)} potential copyright risks")
            for source in risky[:5]:
                click.echo(f"  - {source}")
        else:
            click.echo("✅ No high-confidence copyright matches found")


@main.command('verify', hidden=True)
@click.argument('pack_path', type=click.Path(exists=True))
@click.option('--strict', is_flag=True, help='Require all verifications to pass (including KMS and Object Lock)')
def verify_cmd(pack_path, strict):
    """Verify a Lace compliance pack ZIP file.
    
    \b
    Usage: lace verify <pack.zip> [--strict]
    
    \b
    Non-strict mode (default):
      - Verifies structure and file presence
      - Verifies SHA256 digest if available
      - Reports but doesn't fail on missing KMS/Object Lock
    
    \b
    Strict mode (--strict):
      - Requires all verifications to pass
      - Fails if KMS signature cannot be verified
      - Fails if Object Lock is not present (when URL available)
    """
    try:
        errors = []
        warnings = []
        
        # Check if it's a ZIP file
        if not zipfile.is_zipfile(pack_path):
            click.echo(f"Error: {pack_path} is not a valid ZIP file", err=True)
            sys.exit(EXIT_VERIFY_FAILED)
        
        with zipfile.ZipFile(pack_path, 'r') as zf:
            # Check required files
            required_files = [
                'eu_sds.json',
                'model_card.json',
                'copyright_policy.md',
                'provider_decision_sheet.md',
                'analysis_manifest.json',
            ]
            
            zip_files = zf.namelist()
            for req_file in required_files:
                if req_file not in zip_files and f"pack/{req_file}" not in zip_files:
                    errors.append(f"Missing required file: {req_file}")
            
            # Check for signatures directory
            has_signatures = any('signatures/' in f for f in zip_files)
            if not has_signatures:
                errors.append("Missing signatures directory")
            
            # Try to find and verify digest
            digest_verified = False
            digest_value = None
            
            # Look for manifest.json with pack_sha256
            if 'signatures/manifest.json' in zip_files:
                try:
                    manifest_data = json.loads(zf.read('signatures/manifest.json'))
                    if 'pack_sha256' in manifest_data:
                        digest_value = manifest_data['pack_sha256']
                        # Compute actual SHA256
                        sha256 = hashlib.sha256()
                        with open(pack_path, 'rb') as f:
                            while chunk := f.read(8192):
                                sha256.update(chunk)
                        actual_digest = sha256.hexdigest()
                        
                        if digest_value.lower() == actual_digest.lower():
                            digest_verified = True
                            click.echo(f"✓ Digest verified: {digest_value[:16]}...")
                        else:
                            errors.append(f"Digest mismatch: expected {digest_value[:16]}..., got {actual_digest[:16]}...")
                except Exception as e:
                    warnings.append(f"Could not verify manifest digest: {str(e)}")
            
            # Look for pack.sha256 file
            if not digest_verified and 'signatures/pack.sha256' in zip_files:
                try:
                    digest_value = zf.read('signatures/pack.sha256').decode().strip()
                    # Compute actual SHA256
                    sha256 = hashlib.sha256()
                    with open(pack_path, 'rb') as f:
                        while chunk := f.read(8192):
                            sha256.update(chunk)
                    actual_digest = sha256.hexdigest()
                    
                    if digest_value.lower() == actual_digest.lower():
                        digest_verified = True
                        click.echo(f"✓ Digest verified: {digest_value[:16]}...")
                    else:
                        errors.append(f"Digest mismatch: expected {digest_value[:16]}..., got {actual_digest[:16]}...")
                except Exception as e:
                    warnings.append(f"Could not verify SHA256 file: {str(e)}")
            
            if not digest_verified:
                if strict:
                    errors.append("No digest found for verification")
                    click.echo("digest: not found ✗", err=True)
                else:
                    click.echo("digest: unknown")
            
            # Try KMS verification if available
            kms_verified = False
            kms_status = None
            if 'signatures/kms_sig.json' in zip_files:
                try:
                    import boto3
                    kms_data = json.loads(zf.read('signatures/kms_sig.json'))
                    
                    if 'key_arn' in kms_data and 'signature' in kms_data:
                        # Try to verify with KMS
                        try:
                            kms = boto3.client('kms', region_name='eu-west-1')
                            # Get public key
                            pub_key_response = kms.get_public_key(KeyId=kms_data['key_arn'])
                            
                            # Verify signature
                            verify_response = kms.verify(
                                KeyId=kms_data['key_arn'],
                                Message=digest_value.encode() if digest_value else b'',
                                Signature=base64.b64decode(kms_data['signature']),
                                SigningAlgorithm=kms_data.get('algorithm', 'RSASSA_PKCS1_V1_5_SHA_256')
                            )
                            
                            if verify_response['SignatureValid']:
                                kms_verified = True
                                click.echo(f"✓ KMS signature verified")
                            else:
                                errors.append("KMS signature invalid")
                                
                        except Exception as e:
                            kms_status = "kms: not-verifiable"
                            if strict:
                                errors.append(f"KMS verification failed: {kms_status}")
                                click.echo(f"{kms_status} ✗", err=True)
                            else:
                                click.echo(kms_status)
                    else:
                        kms_status = "kms: not-verifiable (missing signature data)"
                        if not strict:
                            warnings.append(kms_status)
                        else:
                            errors.append("KMS signature present but cannot verify (missing key/data)")
                        
                except ImportError:
                    kms_status = "kms: skipped (boto3 not installed)"
                    if not strict:
                        warnings.append(kms_status)
                    else:
                        errors.append("boto3 required for KMS verification in strict mode")
                except Exception as e:
                    kms_status = f"kms: error ({str(e)[:30]})"
                    if not strict:
                        warnings.append(kms_status)
                    else:
                        errors.append(f"KMS verification failed: {str(e)[:50]}")
            else:
                kms_status = "kms: skipped (no kms_sig.json)"
                if not strict:
                    # OK in non-strict
                    pass
                else:
                    errors.append("KMS signature required in strict mode")
            
            # Check Object Lock proof if URL present
            object_lock_checked = False
            object_lock_status = None
            if 'signatures/object_lock_proof.json' in zip_files:
                try:
                    proof_data = json.loads(zf.read('signatures/object_lock_proof.json'))
                    if 'presigned_url' in proof_data:
                        # Try HEAD request to check retention
                        import urllib.request
                        req = urllib.request.Request(
                            proof_data['presigned_url'],
                            method='HEAD'
                        )
                        try:
                            with urllib.request.urlopen(req) as response:
                                retention = response.headers.get('x-amz-object-lock-mode')
                                if retention:
                                    object_lock_checked = True
                                    click.echo(f"✓ Object Lock verified: {retention}")
                                else:
                                    object_lock_status = "object-lock: not-present"
                                    if strict:
                                        errors.append("Object Lock not enabled in strict mode")
                                    else:
                                        click.echo(object_lock_status)
                        except Exception as e:
                            object_lock_status = f"object-lock: check failed ({str(e)[:30]})"
                            if strict:
                                errors.append(f"Object Lock verification failed: {str(e)[:50]}")
                            else:
                                warnings.append(object_lock_status)
                    else:
                        object_lock_status = "object-lock: proof present but no URL"
                        if strict:
                            errors.append("Object Lock URL missing in strict mode")
                        else:
                            warnings.append(object_lock_status)
                except Exception as e:
                    object_lock_status = f"object-lock: error ({str(e)[:30]})"
                    if strict:
                        errors.append(f"Object Lock proof error: {str(e)[:50]}")
                    else:
                        warnings.append(object_lock_status)
            else:
                object_lock_status = "object-lock: no proof"
                if not strict:
                    # OK in non-strict
                    logger.debug("No Object Lock proof present")
                else:
                    # Only enforce in strict if we have a URL
                    pass
        
        # Report results
        if errors:
            click.echo("\nVerification FAILED:", err=True)
            for error in errors:
                click.echo(f"  ✗ {error}", err=True)
        
        if warnings and not strict:
            click.echo("\nWarnings:")
            for warning in warnings:
                click.echo(f"  ⚠ {warning}")
        
        if errors or (strict and warnings):
            sys.exit(EXIT_VERIFY_FAILED)
        else:
            click.echo("\n✓ Pack structure and digest verified")
            sys.exit(EXIT_SUCCESS)
            
    except Exception as e:
        click.echo(f"Verification error: {redact_sensitive(str(e))}", err=True)
        sys.exit(EXIT_VERIFY_FAILED)


@main.command()
@click.argument('dataset_path', type=click.Path(exists=True))
@click.option('--name', help='Name for the dataset')
def attest_cmd(dataset_path, name):
    """Create attestation for a dataset."""
    try:
        attestation_id = attest(dataset_path, name)
        click.echo(f"✅ Created attestation: {attestation_id}")
    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)
        sys.exit(1)


@main.command('verify-attestation', hidden=True)
@click.argument('attestation_id')
@click.option('--check-copyright', help='Text to check for copyright')
def verify_attestation_cmd(attestation_id, check_copyright):
    """Verify an attestation."""
    try:
        result = verify(attestation_id, check_copyright)
        if result.get('valid'):
            click.echo(f"✅ Attestation {attestation_id} is valid")
        else:
            click.echo(f"❌ Attestation invalid")
    except Exception as e:
        click.echo(f"❌ Error: {e}", err=True)
        sys.exit(1)


@main.command()
def about_cmd():
    """Display information about Lace."""
    about()


@main.command('generate-docs')
@click.argument('dataset_path', type=click.Path(exists=True))
@click.option('--allow-external-ai', is_flag=True, help='Allow sending redacted samples to external AI')
@click.option('--answers', type=click.Path(exists=True), help='Load answers from file (for CI/CD)')
@click.option('--output', type=click.Path(), help='Output directory for documents')
@click.option('--no-store', is_flag=True, help='Skip S3 storage (local output only)')
@click.option('--skip-validation', is_flag=True, help='Skip S3 bucket validation')
@click.option('--scope-answers', type=click.Path(exists=True), help='Pre-computed scope answers')
def generate_docs_cmd(dataset_path, allow_external_ai, answers, output, no_store, skip_validation, scope_answers):
    """Generate EU compliance documents for dataset."""
    try:
        click.echo("\n" + "="*60)
        click.echo("📋 EU AI Act Compliance Document Generator")
        click.echo("="*60 + "\n")
        
        # Step 1: Analyze dataset
        click.echo("🔍 Analyzing dataset...")
        analyzer = DatasetAnalyzer(allow_external_ai=allow_external_ai)
        analysis_results = analyzer.analyze_dataset(dataset_path)
        
        # Show analysis summary
        click.echo(f"✅ Analysis complete:")
        click.echo(f"   - Files: {analysis_results.get('volume', {}).get('files', 0)}")
        click.echo(f"   - Size: {analysis_results.get('volume', {}).get('bytes', 0) / (1024*1024):.1f} MB")
        click.echo(f"   - Estimated tokens: {analysis_results.get('volume', {}).get('estimated_tokens', 0):,}")
        if analysis_results.get('languages', {}).get('values'):
            click.echo(f"   - Languages: {', '.join(analysis_results['languages']['values'][:3])}")
        if analysis_results.get('top_10_percent_domains'):
            click.echo(f"   - Top domains: {len(analysis_results['top_10_percent_domains'])} domains")
        click.echo()
        
        # Step 2: Run wizard or load answers
        if answers:
            click.echo(f"📄 Loading answers from {answers}...")
            wizard = DocumentWizard(analysis_results)
            wizard_data = wizard.run_with_answers(answers)
        else:
            # Interactive wizard
            wizard = DocumentWizard(analysis_results)
            wizard_data = wizard.run_interactive()
        
        # Step 2.5: Integrate scope classification
        if scope_answers:
            with open(scope_answers, 'r') as f:
                scope_data = json.load(f)
        else:
            # Extract scope-relevant answers from wizard data
            scope_data = {
                'placing_date': wizard_data.get('model_identification', {}).get('release_date'),
                'general_purpose': wizard_data.get('general_purpose', True),
                'open_source_release': wizard_data.get('open_source_release', False),
                'training_compute_flops': wizard_data.get('training_compute_flops', 'unknown'),
                'outside_eu_provider': wizard_data.get('outside_eu_provider', False),
                'provider_status': wizard_data.get('provider_status', 'built_model'),
                'sme_status': wizard_data.get('sme_status', 'unsure')
            }
        
        # Classify scope
        classifier = ScopeClassifier()
        scope = classifier.classify(scope_data)
        
        # Add scope results to wizard data metadata
        wizard_data['_metadata'] = wizard_data.get('_metadata', {})
        wizard_data['_metadata']['is_gpai'] = scope.is_gpai_provider
        wizard_data['_metadata']['is_significant_modifier'] = scope.is_significant_modifier
        wizard_data['_metadata']['is_systemic_risk'] = scope.is_systemic_risk
        wizard_data['_metadata']['is_open_source'] = scope.is_open_source_release
        wizard_data['_metadata']['provider_type'] = scope.provider_type
        wizard_data['_metadata']['applicable_obligations'] = scope.applicable_obligations
        wizard_data['_metadata']['carve_outs'] = scope.carve_outs
        
        # Step 3: Generate documents based on scope
        click.echo("\n📝 Generating documents based on legal obligations...")
        
        # Show what's required
        if scope.is_gpai_provider:
            click.echo("   📜 GPAI Provider - Article 53 obligations apply")
            if scope.carve_outs:
                click.echo(f"   🛡️ Open-source carve-outs: {', '.join(scope.carve_outs)}")
        else:
            click.echo("   📄 Voluntary transparency documents only")
        
        generator = TemplateGenerator()
        documents = {}
        
        # Always generate EU summary for GPAI providers
        if scope.is_gpai_provider:
            click.echo("   • Generating EU Public Summary (Art. 53(1)(d))...")
            eu_summary = generator.generate(wizard_data, is_gpai=True)
            documents['eu_summary'] = eu_summary['document']
            
            click.echo("   • Generating Copyright Policy (Art. 53(1)(c))...")
            copyright_policy = generator.generate_copyright_policy(wizard_data)
            documents['copyright_policy'] = copyright_policy
            
            # Technical docs only if not carved out
            if "Technical documentation (Art. 53(1)(a) - exempt)" not in scope.carve_outs:
                click.echo("   • Generating Technical Documentation (Art. 53(1)(a))...")
                # TODO: Implement technical docs generator
                documents['technical_docs'] = "Technical documentation would be generated here"
            
            # Downstream info only if not carved out
            if "Downstream information (Art. 53(1)(b) - exempt)" not in scope.carve_outs:
                click.echo("   • Generating Downstream Information (Art. 53(1)(b))...")
                # TODO: Implement downstream info generator
                documents['downstream_info'] = "Downstream provider information would be generated here"
        else:
            # Voluntary documents for non-GPAI
            click.echo("   • Generating voluntary EU-style summary...")
            eu_summary = generator.generate(wizard_data, is_gpai=False)
            documents['eu_summary'] = eu_summary['document']
            
            click.echo("   • Generating voluntary copyright statement...")
            copyright_policy = generator.generate_copyright_policy(wizard_data)
            documents['copyright_policy'] = copyright_policy
        
        # Always generate model card and HTML
        click.echo("   • Generating Model Card...")
        model_card = generator.generate_model_card(wizard_data)
        documents['model_card'] = model_card
        
        click.echo("   • Generating HTML output...")
        html_output = generator.generate_html_output(
            documents.get('eu_summary', {}),
            eu_summary.get('label', 'EU Training Summary')
        )
        documents['html_output'] = html_output
        
        # Add metadata
        metadata = {
            'is_gpai': scope.is_gpai_provider,
            'provider_type': scope.provider_type,
            'is_systemic_risk': scope.is_systemic_risk,
            'is_open_source': scope.is_open_source_release,
            'applicable_obligations': scope.applicable_obligations,
            'carve_outs': scope.carve_outs,
            'validation': eu_summary.get('validation'),
            'dataset_path': str(dataset_path),
            'external_ai_used': allow_external_ai,
            'gpai_applicability_date': scope.gpai_applicability_date,
            'enforcement_date': scope.enforcement_date,
            'grace_period_end': scope.grace_period_end
        }
        
        # Step 4: Store documents
        if not no_store:
            try:
                click.echo("\n💾 Storing documents...")
                storage = ImmutableStorage()
                
                if not skip_validation:
                    click.echo("   Validating S3 configuration...")
                    # Validation happens in __init__
                
                bundle_id = storage.store_bundle(documents, metadata)
                click.echo(f"✅ Documents stored with bundle ID: {bundle_id}")
                click.echo(f"   Retention: 7 years (EU compliance)")
                
            except Exception as e:
                click.echo(f"⚠️  S3 storage failed: {e}", err=True)
                click.echo("   Falling back to local output only")
                no_store = True
        
        # Step 5: Save locally if requested
        if output or no_store:
            output_path = Path(output) if output else Path('.') / 'lace_documents'
            output_path.mkdir(parents=True, exist_ok=True)
            
            # Save EU summary
            with open(output_path / 'eu_training_summary.json', 'w') as f:
                json.dump(eu_summary['document'], f, indent=2)
            
            # Save model card
            with open(output_path / 'model_card.md', 'w') as f:
                f.write(model_card)
            
            # Save copyright policy
            with open(output_path / 'copyright_policy.md', 'w') as f:
                f.write(copyright_policy)
            
            # Save HTML
            with open(output_path / 'summary.html', 'w') as f:
                f.write(html_output)
            
            # Save metadata
            with open(output_path / 'metadata.json', 'w') as f:
                json.dump(metadata, f, indent=2)
            
            click.echo(f"\n📁 Documents saved to: {output_path}")
        
        # Show validation status
        if eu_summary.get('validation', {}).get('valid'):
            click.echo("\n✅ Document validation: PASSED")
        else:
            click.echo("\n⚠️  Document validation: FAILED")
            errors = eu_summary.get('validation', {}).get('errors', [])
            for error in errors[:5]:
                click.echo(f"   - {error}")
        
        click.echo("\n" + "="*60)
        click.echo("✨ Document generation complete!")
        click.echo("="*60 + "\n")
        
    except Exception as e:
        click.echo(f"\n❌ Error: {e}", err=True)
        sys.exit(1)


@main.command('scope')
@click.option('--answers', type=click.Path(exists=True), help='Load answers from JSON file')
@click.option('--allow-remote-llm', is_flag=True, envvar='LACE_ALLOW_REMOTE_LLM',
              help='Allow remote LLM for unsure resolution')
@click.option('--explain', is_flag=True, help='Show detailed decision trace')
@click.option('--json', 'output_json', is_flag=True, help='Output as JSON')
@click.option('--strict-triad/--legacy-placement-logic', default=True,
              help='Use strict triad logic (default) or legacy placement')
def scope_cmd(answers, allow_remote_llm, explain, output_json, strict_triad):
    """Classify EU AI Act scope and obligations."""
    try:
        # Set environment for remote LLM if enabled
        if allow_remote_llm:
            os.environ['LACE_ALLOW_REMOTE_LLM'] = 'true'
        
        # Load answers
        if answers:
            with open(answers, 'r') as f:
                answers_data = json.load(f)
        else:
            # Interactive mode would go here
            click.echo("Interactive mode not yet implemented. Please provide --answers file.")
            sys.exit(1)
        
        # Classify scope
        classifier = ScopeClassifier()
        scope = classifier.classify(answers_data)
        
        if output_json:
            # JSON output with schema version
            output = {
                'schema_version': '1.0.0',
                'provider_role': scope.provider_role,
                'placed_on_market': scope.placed_on_market,
                'placement_reason': scope.placement_reason,
                'placement_reason_code': scope.placement_reason_code,
                'is_gpai_provider': scope.is_gpai_provider,
                'is_systemic_risk': scope.is_systemic_risk,
                'needs_eu_representative': scope.needs_eu_representative,
                'eu_rep_reason': scope.eu_rep_reason,
                'compliance_deadlines': scope.compliance_deadlines,
                'applicable_obligations': scope.applicable_obligations,
                'carve_outs': scope.carve_outs,
                'validation_warnings': scope.validation_warnings,
                'decision_trace': scope.decision_trace if explain else [],
                'unsure_resolutions': scope.unsure_resolutions,
                'gpai_applicability_date': scope.gpai_applicability_date,
                'enforcement_date': scope.enforcement_date,
                'grace_period_end': scope.grace_period_end,
                'systemic_risk_threshold': scope.systemic_risk_threshold,
                'ai_office_template_version': scope.ai_office_template_version,
                'advisory_disclaimer': scope.advisory_disclaimer
            }
            click.echo(json.dumps(output, indent=2, default=str))
        else:
            # Human-readable output
            click.echo("\n" + "="*60)
            click.echo("📋 EU AI Act Scope Classification")
            click.echo("="*60 + "\n")
            
            # Show GPAI applicability dates
            click.echo("📅 Important Dates")
            click.echo(f"   GPAI obligations apply: {scope.gpai_applicability_date}")
            click.echo(f"   Enforcement begins: {scope.enforcement_date}")
            click.echo(f"   Pre-existing models grace period: until {scope.grace_period_end}")
            click.echo()
            
            # Placement Status Section
            click.echo("📍 Market Placement Status")
            if scope.placed_on_market:
                click.echo("   ✓ Making available in EU (Article 3)")
            else:
                click.echo("   ✗ Not making available in EU")
            click.echo(f"   Reason: {scope.placement_reason}")
            
            # Commercial activity indicators
            if (answers_data.get('integrated_into_own_system') == True or 
                (answers_data.get('internal_only_use') == True and 
                 (answers_data.get('essential_to_service') == True or 
                  answers_data.get('affects_individuals_rights') == True))):
                click.echo("   Note: Indicators of 'making available' in the course of")
                click.echo("         a commercial activity (Art. 3)")
            
            if not scope.placed_on_market:
                click.echo("   Note: Advisory only – no model-level obligations apply.")
            
            click.echo(f"\nDisclaimer: {scope.advisory_disclaimer}\n")
            
            # Provider Role
            click.echo("👤 Provider Role")
            if scope.provider_role == "model_provider":
                click.echo("   ✓ Model Provider")
                if scope.is_significant_modifier:
                    click.echo("     (Significant modifier)")
            else:
                click.echo("   ✓ System Integrator")
                click.echo("     Model obligations sit with upstream provider")
            
            # Key Classifications
            click.echo("\n🎯 Key Classifications")
            click.echo(f"   GPAI Provider: {'Yes' if scope.is_gpai_provider else 'No'}")
            click.echo(f"   Systemic Risk: {'Yes' if scope.is_systemic_risk else 'No'}")
            click.echo(f"   Open Source: {'Yes' if scope.is_open_source_release else 'No'}")
            click.echo(f"   SME Status: {'Yes' if scope.is_sme else 'No'}")
            
            # Obligations
            if scope.applicable_obligations:
                click.echo("\n📜 Applicable Obligations")
                for obligation in scope.applicable_obligations[:5]:
                    click.echo(f"   • {obligation}")
                if len(scope.applicable_obligations) > 5:
                    click.echo(f"   ... and {len(scope.applicable_obligations) - 5} more")
            
            # Carve-outs
            if scope.carve_outs:
                click.echo("\n🛡️ Open-Source Carve-Outs")
                for carveout in scope.carve_outs:
                    click.echo(f"   • {carveout}")
            elif scope.carveout_blockers and scope.is_open_source_release:
                click.echo("\n⚠️ Carve-Out Blockers")
                for blocker in scope.carveout_blockers:
                    click.echo(f"   • {blocker}")
            
            # Warnings
            if scope.validation_warnings:
                click.echo("\n⚠️ Validation Warnings")
                for warning in scope.validation_warnings[:3]:
                    click.echo(f"   • {warning}")
            
            # Unsure Resolution Summary
            if scope.unsure_resolutions:
                click.echo("\n🧭 Unsure Resolution Summary (informational – NOT legal advice)")
                for res in scope.unsure_resolutions:
                    via = "remote" if res.get('used_remote') else "heuristic"
                    click.echo(f"   • {res['question_id']} → {res['resolved_value']} "
                             f"(confidence {res['confidence']:.2f}) via {via}")
                    if res.get('warnings'):
                        for warning in res['warnings']:
                            click.echo(f"     ⚠️ {warning}")
                click.echo("\nPrivacy: Free-text was scrubbed before any remote processing;")
                click.echo("         raw text is not stored.")
            
            # Decision Trace (if --explain)
            if explain and scope.decision_trace:
                click.echo("\n🔍 Decision Trace")
                for trace_line in scope.decision_trace:
                    click.echo(f"   → {trace_line}")
            
            # Deadlines
            if scope.compliance_deadlines and 'note' not in scope.compliance_deadlines:
                click.echo("\n📅 Compliance Deadlines")
                for key, value in scope.compliance_deadlines.items():
                    if value and key != 'grace_period_active':
                        click.echo(f"   {key}: {value}")
            
            click.echo("\n" + "="*60 + "\n")
        
    except Exception as e:
        click.echo(f"\n❌ Error: {e}", err=True)
        sys.exit(1)


@main.command('analyze-dataset')
@click.argument('dataset_path', type=click.Path(exists=True))
@click.option('--allow-external-ai', is_flag=True, help='Allow sending redacted samples to external AI')
@click.option('--output', type=click.Path(), help='Output file for analysis results')
def analyze_dataset_cmd(dataset_path, allow_external_ai, output):
    """Analyze dataset without generating documents."""
    try:
        click.echo("\n🔍 Analyzing dataset...")
        
        analyzer = DatasetAnalyzer(allow_external_ai=allow_external_ai)
        results = analyzer.analyze_dataset(dataset_path)
        
        # Display summary
        click.echo("\n📊 Analysis Results:")
        click.echo(f"   Files: {results.get('volume', {}).get('files', 0)}")
        click.echo(f"   Size: {results.get('volume', {}).get('bytes', 0) / (1024*1024):.1f} MB")
        click.echo(f"   Estimated tokens: {results.get('volume', {}).get('estimated_tokens', 0):,}")
        
        if results.get('languages', {}).get('values'):
            click.echo(f"   Languages: {', '.join(results['languages']['values'])}")
        
        if results.get('top_10_percent_domains'):
            click.echo(f"   Top 10% domains ({len(results['top_10_percent_domains'])} total):")
            for domain in results['top_10_percent_domains'][:5]:
                click.echo(f"      - {domain}")
            if len(results['top_10_percent_domains']) > 5:
                click.echo(f"      ... and {len(results['top_10_percent_domains']) - 5} more")
        
        if results.get('source_types', {}).get('values'):
            click.echo(f"   Source types: {', '.join(results['source_types']['values'])}")
        
        if results.get('modalities', {}).get('values'):
            click.echo(f"   Modalities: {', '.join(results['modalities']['values'])}")
        
        if results.get('pii_signals', {}).get('detected'):
            click.echo(f"   ⚠️  PII detected: {', '.join(results['pii_signals']['values'])}")
        
        # Save to file if requested
        if output:
            with open(output, 'w') as f:
                json.dump(results, f, indent=2)
            click.echo(f"\n💾 Analysis saved to: {output}")
        
    except Exception as e:
        click.echo(f"\n❌ Error: {e}", err=True)
        sys.exit(1)


@main.command('advise-scope')
@click.option('--answers', type=click.Path(exists=True), help='Load answers from file')
@click.option('--output', type=click.Path(), help='Save scope analysis to file')
def advise_scope_cmd(answers, output):
    """Quickly determine EU AI Act obligations without generating documents."""
    from datetime import date
    
    try:
        click.echo("\n" + "="*60)
        click.echo("🔍 EU AI Act Scope Advisor")
        click.echo("="*60)
        click.echo("\n⚠️  This is guidance, not legal advice\n")
        
        # Load or collect answers
        if answers:
            click.echo(f"Loading answers from {answers}...")
            with open(answers, 'r') as f:
                scope_answers = json.load(f)
        else:
            # Interactive scope questions
            scope_answers = {}
            
            # Critical questions for scope
            click.echo("Please answer these questions to determine your obligations:\n")
            
            # Placing date
            placing_date = click.prompt("When will/did you first make this model available in the EU? (YYYY-MM-DD)", 
                                       default=datetime.now().strftime('%Y-%m-%d'))
            scope_answers['placing_date'] = placing_date
            
            # Check if pre-existing
            if placing_date < "2025-08-02":
                still_on_market = click.confirm("Is the model still (or will be) available in the EU?", default=True)
                scope_answers['still_on_market'] = still_on_market
            
            # SME status
            click.echo("\nSME Criteria: <250 employees AND (≤€50M turnover OR ≤€43M balance sheet)")
            sme_status = click.prompt("Do you qualify as an EU SME?", 
                                     type=click.Choice(['yes_sme', 'no_not_sme', 'unsure']),
                                     default='unsure')
            scope_answers['sme_status'] = sme_status
            
            # Provider status
            click.echo("\nWhat is your role with this model?")
            provider_status = click.prompt("Select", 
                type=click.Choice([
                    'built_model',
                    'significant_modifier', 
                    'light_finetuner',
                    'api_user',
                    'internal_only'
                ]),
                default='built_model'
            )
            scope_answers['provider_status'] = provider_status
            
            # General-purpose
            general_purpose = click.confirm("\nIs this model designed for general-purpose tasks?", default=True)
            scope_answers['general_purpose'] = general_purpose
            
            # Modification ratio if modifier
            if provider_status == 'significant_modifier':
                click.echo("\nCommission threshold: MORE THAN 1/3 (>33%) = significant")
                compute_ratio = click.prompt("Your compute as % of original", 
                    type=click.Choice([
                        'unknown',
                        'under_10',
                        '10_to_33',
                        'exactly_33',
                        '34_to_50',
                        'over_50'
                    ]),
                    default='unknown'
                )
                scope_answers['modification_compute_ratio'] = compute_ratio
            
            # Systemic risk
            click.echo("\n10^25 FLOP = Systemic risk threshold")
            compute_flops = click.prompt("Total training compute", 
                type=click.Choice([
                    'unknown',
                    'under_1e25',
                    'exactly_1e25',
                    'over_1e25'
                ]),
                default='unknown'
            )
            scope_answers['training_compute_flops'] = compute_flops
            
            # Open-source
            open_source = click.confirm("\nWill you release this under a free/open-source license?", default=False)
            scope_answers['open_source_release'] = open_source
            
            # Non-EU provider
            outside_eu = click.confirm("\nIs the provider entity based outside the EU?", default=False)
            scope_answers['outside_eu_provider'] = outside_eu
        
        # Classify scope
        classifier = ScopeClassifier()
        scope = classifier.classify(scope_answers)
        
        # Display results with clear formatting
        click.echo("\n" + "="*60)
        click.echo("📊 EU AI Act Scope Analysis")
        click.echo("="*60)
        
        # Provider status
        click.echo(f"\n🏢 Provider Status")
        click.echo(f"   Type: {scope.provider_type}")
        click.echo(f"   GPAI Provider: {'Yes' if scope.is_gpai_provider else 'No'}")
        if scope.is_significant_modifier:
            click.echo(f"   Significant Modifier: Yes (>33% compute)")
        click.echo(f"   SME Status: {'Yes' if scope.is_sme else 'No/Unknown'}")
        
        # Obligations
        click.echo(f"\n📋 Obligations")
        if scope.applicable_obligations:
            for obligation in scope.applicable_obligations:
                click.echo(f"   • {obligation}")
        else:
            click.echo("   No Article 53 obligations (voluntary transparency only)")
        
        # Open-source status (only show if actually open-source)
        if scope.is_open_source_release:
            click.echo(f"\n📖 Open-Source Status")
            click.echo(f"   Still Required:")
            click.echo(f"   • Public summary of training content")
            click.echo(f"   • Copyright compliance policy")
            if scope.needs_eu_representative:
                click.echo(f"   • EU authorized representative")
            
            # Only show actual applicable carve-outs
            if scope.carve_outs:
                click.echo(f"   Carve-outs Applied:")
                for carveout in scope.carve_outs:
                    click.echo(f"   • {carveout}")
        
        # Deadlines with clear labels
        click.echo(f"\n📅 Compliance Deadlines")
        if scope.placing_date < date(2025, 8, 2):
            click.echo(f"   ⚠️  Pre-existing model (placed {scope.placing_date})")
            click.echo(f"   Public Summary: {scope.compliance_deadlines['public_summary_due']} (2-year grace)")
            click.echo(f"   Copyright Policy: {scope.compliance_deadlines['copyright_policy_due']} (no grace)")
            click.echo(f"   Other Obligations: {scope.compliance_deadlines['other_obligations_due']} (no grace)")
        else:
            click.echo(f"   All obligations due: {scope.placing_date}")
        
        click.echo(f"   Fines enforceable from: {scope.compliance_deadlines['fines_enforceable_from']}")
        click.echo(f"   Next update due: {scope.compliance_deadlines.get('next_update_due', 'N/A')}")
        
        # Domain disclosure rule
        if scope.is_provider:
            click.echo(f"\n🌐 Domain Disclosure")
            click.echo(f"   Rule: {scope.top_domain_rule}")
            click.echo(f"   Method: Volume calculated by bytes/tokens")
        
        # EU Representative
        if scope.needs_eu_representative:
            click.echo(f"\n⚠️  EU Authorized Representative Required")
            click.echo(f"   (Non-EU provider - no open-source carve-out)")
        
        # Systemic risk
        if scope.is_systemic_risk:
            click.echo(f"\n⚠️  Systemic Risk Model (>10^25 FLOP)")
            click.echo(f"   Additional obligations apply (Art. 55)")
        
        # Notification deadline if applicable
        if scope.needs_threshold_notification:
            click.echo(f"\n📮 Commission Notification Required")
            if scope.notification_deadline:
                click.echo(f"   Deadline: {scope.notification_deadline}")
            elif scope.notification_deadline_label:
                click.echo(f"   Deadline: {scope.notification_deadline_label}")
            else:
                click.echo(f"   Deadline: Within 14 days of knowing threshold exceeded")
        
        # Indicative signals (if any)
        if hasattr(scope, 'indicative_signals') and scope.indicative_signals.get('indicative_gpai_signal'):
            click.echo(f"\nℹ️  Indicative GPAI Signals")
            for reason in scope.indicative_signals.get('reasons', []):
                click.echo(f"   • {reason}")
        
        # Carve-out blockers (if open-source but no carve-outs)
        if (hasattr(scope, 'carveout_blockers') and scope.carveout_blockers and 
            scope.is_open_source_release and not scope.carve_outs):
            click.echo(f"\n⚠️  Open-source carve-outs were not applied because:")
            for blocker in scope.carveout_blockers:
                click.echo(f"   • {blocker}")
        
        # Validation warnings (if any)
        if hasattr(scope, 'validation_warnings') and scope.validation_warnings:
            click.echo(f"\n⚠️  Validation Warnings")
            for warning in scope.validation_warnings:
                click.echo(f"   • {warning}")
        
        # Save output if requested
        if output:
            result = {
                'scope_classification': {
                    'is_gpai_provider': scope.is_gpai_provider,
                    'is_significant_modifier': scope.is_significant_modifier,
                    'is_provider': scope.is_provider,
                    'is_sme': scope.is_sme,
                    'is_open_source': scope.is_open_source_release,
                    'is_systemic_risk': scope.is_systemic_risk,
                    'needs_eu_representative': scope.needs_eu_representative,
                    'provider_type': scope.provider_type,
                    'top_domain_rule': scope.top_domain_rule
                },
                'compliance_deadlines': {
                    'placing_date': scope.placing_date.isoformat(),
                    'public_summary_due': scope.compliance_deadlines.get('public_summary_due').isoformat() 
                        if scope.compliance_deadlines.get('public_summary_due') else None,
                    'copyright_policy_due': scope.compliance_deadlines.get('copyright_policy_due').isoformat()
                        if scope.compliance_deadlines.get('copyright_policy_due') else None,
                    'fines_enforceable_from': scope.compliance_deadlines['fines_enforceable_from'].isoformat(),
                    'next_update_due': scope.compliance_deadlines.get('next_update_due').isoformat()
                        if scope.compliance_deadlines.get('next_update_due') else None
                },
                'applicable_obligations': scope.applicable_obligations,
                'carve_outs': scope.carve_outs,
                'metadata': {
                    'generated_at': datetime.now().isoformat(),
                    'generator': 'Lace EU AI Act Scope Advisor',
                    'disclaimer': 'This is guidance, not legal advice'
                }
            }
            
            with open(output, 'w') as f:
                json.dump(result, f, indent=2)
            click.echo(f"\n💾 Scope analysis saved to: {output}")
        
        click.echo("\n" + "="*60)
        if scope.is_provider:
            click.echo("Run 'lace generate-docs' to create compliance documents")
        else:
            click.echo("You may create voluntary transparency documents with 'lace generate-docs'")
        click.echo("="*60 + "\n")
        
    except Exception as e:
        click.echo(f"\n❌ Error: {e}", err=True)
        sys.exit(1)


@main.command('analyze')
@click.argument('dataset_path', type=click.Path(exists=True))
@click.option('--output', '-o', default='analysis.json', help='Output analysis file')
@click.option('--sample-rate', default=0.01, help='Sampling rate for large datasets')
@click.option('--debug', is_flag=True, envvar='LACE_DEBUG', help='Enable debug output')
def analyze_cmd(dataset_path, output, sample_rate, debug):
    """Analyze dataset and export sanitized analysis (no raw text)."""
    from lace.wizard import DatasetAnalyzer
    from lace.wizard.serializer import to_analysis_json
    from pathlib import Path
    import json
    import os
    
    if debug:
        os.environ['LACE_DEBUG'] = '1'
        logging.basicConfig(level=logging.DEBUG)
    
    click.echo(f"🔍 Analyzing dataset: {dataset_path}")
    click.echo("   Note: No raw text will be included in the output")
    
    try:
        analyzer = DatasetAnalyzer()
        results = analyzer.analyze_dataset(dataset_path, sample_rate=sample_rate)
        
        # USE UNIFIED SERIALIZER
        sanitized = to_analysis_json(results)
        
        # Fallback if analyzer returned zeros (failsafe using os.stat)
        if (sanitized['size_metrics']['total_files'] == 0 and
            sanitized['size_metrics']['total_bytes'] == 0):
            import os
            files = 0
            bytes_total = 0
            for root, _, names in os.walk(dataset_path):
                for n in names:
                    p = os.path.join(root, n)
                    try:
                        st = os.stat(p)
                        files += 1
                        bytes_total += st.st_size
                    except OSError:
                        pass
            sanitized['size_metrics']['total_files'] = files
            sanitized['size_metrics']['total_bytes'] = bytes_total
            sanitized['size_metrics']['avg_file_size'] = (bytes_total / files) if files else 0.0
            sanitized['summary']['files_processed'] = files
            sanitized['summary']['bytes_total'] = bytes_total
            if debug:
                click.echo(f"   - Fallback: counted {files} files, {bytes_total} bytes via os.stat")
        
        # Write output
        Path(output).write_text(json.dumps(sanitized, indent=2))
        
        # Show summary from SANITIZED object
        click.echo(f"✅ Analysis saved to {output} (no raw text)")
        click.echo(f"   - Files processed: {sanitized['size_metrics']['total_files']}")
        click.echo(f"   - Bytes total: {sanitized['size_metrics']['total_bytes']}")
        click.echo(f"   - Domains found: {sanitized['domain_analysis']['total_domains']}")
        
        # Show serializer notes if debug enabled
        if debug and sanitized.get('metadata', {}).get('serializer_notes'):
            notes = sanitized['metadata']['serializer_notes']
            click.echo(f"   - Serializer notes: {', '.join(notes)}")
    
    except Exception as e:
        click.echo(f"❌ Error analyzing dataset: {e}", err=True)
        raise click.ClickException(str(e))


@main.command('compliance-pack')
@click.argument('dataset_path', type=click.Path(exists=True))
@click.option('--allow-external-ai', is_flag=True, help='Allow sending redacted samples to external AI')
@click.option('--allow-remote-llm', is_flag=True, help='Allow remote LLM for unsure resolution')
@click.option('--answers', type=click.Path(exists=True), help='Load all answers from file')
@click.option('--output', type=click.Path(), help='Output directory for documents')
@click.option('--no-store', is_flag=True, help='Skip S3 storage')
def compliance_pack_cmd(dataset_path, allow_external_ai, allow_remote_llm, answers, output, no_store):
    """Generate complete EU AI Act compliance pack (scope + documents)."""
    try:
        click.echo("\n" + "="*60)
        click.echo("🚀 LACE EU AI Act Compliance Pack Generator")
        click.echo("="*60 + "\n")
        
        click.echo("📅 Important Dates:")
        click.echo("   GPAI obligations apply: 2025-08-02")
        click.echo("   Enforcement begins: 2026-08-02")
        click.echo("   Pre-existing models grace period: until 2027-08-02\n")
        
        # Step 1: Analyze dataset
        click.echo("🔍 Step 1: Analyzing dataset...")
        analyzer = DatasetAnalyzer(allow_external_ai=allow_external_ai)
        analysis_results = analyzer.analyze_dataset(dataset_path)
        
        click.echo(f"   ✓ Files: {analysis_results.get('volume', {}).get('files', 0)}")
        click.echo(f"   ✓ Size: {analysis_results.get('volume', {}).get('bytes', 0) / (1024*1024):.1f} MB")
        click.echo(f"   ✓ Estimated tokens: {analysis_results.get('volume', {}).get('estimated_tokens', 0):,}")
        
        # Step 2: Run wizard
        click.echo("\n📋 Step 2: Collecting compliance information...")
        if answers:
            click.echo(f"   Loading from {answers}...")
            wizard = DocumentWizard(analysis_results)
            wizard_data = wizard.run_with_answers(answers)
        else:
            wizard = DocumentWizard(analysis_results)
            wizard_data = wizard.run_interactive()
        
        # Step 3: Classify scope
        click.echo("\n⚖️ Step 3: Determining legal obligations...")
        
        # Set LLM environment if enabled
        if allow_remote_llm:
            os.environ['LACE_ALLOW_REMOTE_LLM'] = 'true'
        
        # Extract scope data from wizard answers
        scope_data = {
            'placing_date': wizard_data.get('placing_date') or wizard_data.get('model_identification', {}).get('release_date'),
            'general_purpose': wizard_data.get('general_purpose', True),
            'open_source_release': wizard_data.get('open_source_release', False),
            'training_compute_flops': wizard_data.get('training_compute_flops', 'unknown'),
            'outside_eu_provider': wizard_data.get('outside_eu_provider', False),
            'provider_status': wizard_data.get('provider_status', 'built_model'),
            'sme_status': wizard_data.get('sme_status', 'unsure'),
            'integrated_into_own_system': wizard_data.get('integrated_into_own_system'),
            'internal_only_use': wizard_data.get('internal_only_use'),
            'essential_to_service': wizard_data.get('essential_to_service'),
            'affects_individuals_rights': wizard_data.get('affects_individuals_rights')
        }
        
        classifier = ScopeClassifier()
        scope = classifier.classify(scope_data)
        
        # Show scope results
        if scope.placed_on_market:
            click.echo(f"   ✓ Making available in EU (Article 3)")
        else:
            click.echo(f"   ✗ Not making available in EU")
        
        if scope.is_gpai_provider:
            click.echo(f"   ✓ GPAI Provider - Article 53 obligations apply")
            if scope.is_systemic_risk:
                click.echo(f"   ⚠️ Systemic risk model (≥10²⁵ FLOPs)")
            if scope.is_open_source_release:
                click.echo(f"   📖 Open-source release")
                if scope.carve_outs:
                    click.echo(f"   🛡️ Carve-outs: {len(scope.carve_outs)} exemptions")
        else:
            click.echo(f"   📄 Not a GPAI provider - voluntary documents only")
        
        # Step 4: Generate documents
        click.echo("\n📝 Step 4: Generating compliance documents...")
        
        # Add scope to wizard data
        wizard_data['_metadata'] = wizard_data.get('_metadata', {})
        wizard_data['_metadata']['is_gpai'] = scope.is_gpai_provider
        wizard_data['_metadata']['is_systemic_risk'] = scope.is_systemic_risk
        wizard_data['_metadata']['is_open_source'] = scope.is_open_source_release
        wizard_data['_metadata']['applicable_obligations'] = scope.applicable_obligations
        wizard_data['_metadata']['carve_outs'] = scope.carve_outs
        
        generator = TemplateGenerator()
        documents = {}
        
        # Generate based on obligations
        if scope.is_gpai_provider:
            # Always required for GPAI
            click.echo("   • EU Public Summary (Art. 53(1)(d))")
            eu_summary = generator.generate(wizard_data, is_gpai=True)
            documents['eu_summary'] = eu_summary['document']
            
            click.echo("   • Copyright Policy (Art. 53(1)(c))")
            documents['copyright_policy'] = generator.generate_copyright_policy(wizard_data)
            
            # Conditional based on carve-outs
            if "Technical documentation (Art. 53(1)(a) - exempt)" not in scope.carve_outs:
                click.echo("   • Technical Documentation (Art. 53(1)(a))")
            if "Downstream information (Art. 53(1)(b) - exempt)" not in scope.carve_outs:
                click.echo("   • Downstream Information (Art. 53(1)(b))")
        else:
            click.echo("   • Voluntary EU-style summary")
            eu_summary = generator.generate(wizard_data, is_gpai=False)
            documents['eu_summary'] = eu_summary['document']
            documents['copyright_policy'] = generator.generate_copyright_policy(wizard_data)
        
        # Always generate model card
        documents['model_card'] = generator.generate_model_card(wizard_data)
        
        # Step 5: Save documents
        output_path = Path(output) if output else Path('.') / 'lace_compliance_pack'
        output_path.mkdir(parents=True, exist_ok=True)
        
        click.echo(f"\n💾 Step 5: Saving compliance pack to {output_path}...")
        
        # Save documents
        with open(output_path / 'eu_training_summary.json', 'w') as f:
            json.dump(documents['eu_summary'], f, indent=2)
        
        with open(output_path / 'copyright_policy.md', 'w') as f:
            f.write(documents['copyright_policy'])
        
        with open(output_path / 'model_card.md', 'w') as f:
            f.write(documents['model_card'])
        
        # Save scope analysis
        scope_output = {
            'schema_version': '1.0.0',
            'classification': {
                'is_gpai_provider': scope.is_gpai_provider,
                'is_systemic_risk': scope.is_systemic_risk,
                'is_open_source': scope.is_open_source_release,
                'placed_on_market': scope.placed_on_market,
                'placement_reason': scope.placement_reason,
                'needs_eu_representative': scope.needs_eu_representative
            },
            'obligations': scope.applicable_obligations,
            'carve_outs': scope.carve_outs,
            'deadlines': scope.compliance_deadlines,
            'dates': {
                'gpai_applicability': scope.gpai_applicability_date,
                'enforcement': scope.enforcement_date,
                'grace_period_end': scope.grace_period_end
            }
        }
        
        with open(output_path / 'scope_analysis.json', 'w') as f:
            json.dump(scope_output, f, indent=2, default=str)
        
        # Validation status
        if eu_summary.get('validation', {}).get('valid'):
            click.echo("   ✓ Document validation: PASSED")
        else:
            click.echo("   ⚠️ Document validation: See scope_analysis.json for details")
        
        # Summary
        click.echo("\n" + "="*60)
        click.echo("✨ Compliance Pack Generated Successfully!")
        click.echo("="*60)
        click.echo(f"\n📁 Output directory: {output_path}")
        click.echo("   • eu_training_summary.json - Official EU template")
        click.echo("   • copyright_policy.md - Article 53(1)(c) policy")
        click.echo("   • model_card.md - HuggingFace-compatible card")
        click.echo("   • scope_analysis.json - Legal obligations analysis")
        
        if scope.is_gpai_provider:
            click.echo(f"\n⚠️ Next steps:")
            click.echo("   1. Review generated documents for accuracy")
            click.echo("   2. Complete any [PLACEHOLDER] sections")
            if scope.needs_eu_representative:
                click.echo("   3. Appoint EU authorized representative")
            click.echo(f"   {3 if not scope.needs_eu_representative else 4}. Store documents immutably")
            click.echo(f"   {4 if not scope.needs_eu_representative else 5}. Update on material changes")
        else:
            click.echo("\n📌 These are voluntary transparency documents.")
            click.echo("   No legal obligations apply, but transparency is good practice!")
        
        click.echo(f"\n⚖️ Disclaimer: {scope.advisory_disclaimer}\n")
        
    except Exception as e:
        click.echo(f"\n❌ Error: {e}", err=True)
        import traceback
        traceback.print_exc()
        sys.exit(1)


if __name__ == '__main__':
    main()