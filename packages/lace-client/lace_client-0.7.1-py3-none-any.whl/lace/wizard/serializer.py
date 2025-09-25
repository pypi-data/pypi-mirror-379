"""
Serializer for converting analyzer output to sanitized analysis.json format.
Maps ONLY existing fields - no fabrication of data.
"""

from datetime import datetime
import logging

logger = logging.getLogger(__name__)

def to_analysis_json(results: dict) -> dict:
    """
    Map analyzer output to analysis.json format.
    Supports both v1 and v1.1 schemas based on available fields.
    """
    
    import os
    if os.environ.get('LACE_DEBUG') == '1':
        logger.info(f"Analyzer results type: {type(results)}")
        logger.info(f"Analyzer results keys: {sorted(results.keys())}")
    
    serializer_notes = []
    
    # Determine schema version based on MVEA fields presence
    has_mvea_fields = any(k in results for k in [
        'dataset_origin', 'dataset_locator', 'license', 'languages_detail',
        'content_types', 'temporal_coverage', 'synthetic_data_presence',
        'dataset_card', 'line_token_estimates', 'provenance_summary'
    ])
    
    schema_version = 'analysis.v1.1' if has_mvea_fields else 'analysis.v1'
    
    # Safely extract volume metrics with validation
    volume = results.get('volume', {})
    total_files = max(int(volume.get('files', 0)), 0) if 'volume' in results else 0
    total_bytes = max(int(volume.get('bytes', 0)), 0) if 'volume' in results else 0
    
    if 'volume' not in results:
        serializer_notes.append('volume field missing - using zeros')
    
    avg_file_size = (total_bytes / total_files) if total_files > 0 else 0.0
    
    # Extract domains safely (don't synthesize)
    domains = []
    if 'domains' in results:
        raw_domains = results['domains']
        if isinstance(raw_domains, dict):
            # Check if it's the new format with 'values' key
            if 'values' in raw_domains:
                domains = raw_domains.get('values', [])
                if isinstance(domains, dict):
                    # Convert dict of domain->stats to list
                    domains = [
                        {
                            'domain': d, 
                            'bytes': max(int(v.get('bytes', 0)), 0), 
                            'count': max(int(v.get('count', 0)), 0)
                        }
                        for d, v in domains.items()
                    ]
            else:
                # Old format: dict of domain->stats
                domains = [
                    {
                        'domain': d, 
                        'bytes': max(int(v.get('bytes', 0)), 0), 
                        'count': max(int(v.get('count', 0)), 0)
                    }
                    for d, v in raw_domains.items()
                ]
        elif isinstance(raw_domains, list):
            domains = raw_domains
    else:
        serializer_notes.append('domains field missing - using empty array')
    
    # Handle modalities robustly (analyzer versions vary)
    mods = results.get('modalities', [])
    if isinstance(mods, dict):
        # New format with 'values' key
        mods = mods.get('values', [])
    
    # Extract top domains if present (don't synthesize)
    top_domains = results.get('top_10_percent_domains', [])
    if 'top_10_percent_domains' not in results:
        serializer_notes.append('top_10_percent_domains missing')
    
    coverage_pct = float(results.get('top_domains_coverage', 0))
    measurement_method = results.get('measurement_method', 'bytes')
    
    # Extract confidence scores if present
    confidence_scores = results.get('confidence_scores', {})
    if not confidence_scores:
        serializer_notes.append('confidence_scores missing - using empty dict')
    
    # Extract fingerprint sample rate if available
    sample_rate = 0.01
    if 'fingerprint' in results:
        sample_rate = results['fingerprint'].get('sample_rate', 0.01)
    
    # Build base structure - v1.1 uses domain_analysis only, no raw domains
    output = {
        'schema_version': schema_version,
        'summary': {
            'files_processed': total_files,
            'bytes_total': total_bytes,
            'modalities': mods,
        },
        # REMOVED 'domains' field for v1.1 - only use domain_analysis
        'domain_analysis': {
            'top_domains': top_domains if top_domains else (
                # If no top_domains but we have legacy domains, extract just domain names
                [d['domain'] if isinstance(d, dict) else d for d in domains[:20]]
                if domains else []
            ),
            'measurement_method': measurement_method,
            'coverage_percentage': coverage_pct,
            'total_domains': len(top_domains) if top_domains else len(domains),
        },
        'size_metrics': {
            'total_files': total_files,
            'total_bytes': total_bytes,
            'avg_file_size': avg_file_size,
        },
        'confidence_scores': confidence_scores,
        'metadata': {
            'analyzed_at': datetime.utcnow().isoformat(),
            'analyzer_version': '1.1.0' if has_mvea_fields else '1.0.0',
            'sample_rate': sample_rate,
            'privacy_notice': 'No raw text or file paths included',
            'serializer_notes': serializer_notes  # Track what was missing
        },
    }
    
    # Add MVEA fields for v1.1
    if has_mvea_fields:
        # Add new fields directly to the analysis object
        if 'dataset_origin' in results:
            output['dataset_origin'] = results['dataset_origin']
        
        if 'dataset_locator' in results:
            output['dataset_locator'] = results['dataset_locator']
        
        if 'license' in results:
            license_val = results['license']
            # Ensure license is a string
            if isinstance(license_val, dict):
                output['license'] = license_val.get('value', 'unknown')
            else:
                output['license'] = str(license_val) if license_val else 'unknown'
        
        if 'languages_detail' in results:
            output['languages'] = results['languages_detail']
        elif 'languages' in results:
            # Fallback to simple languages if detail not available
            lang_values = results['languages'].get('values', []) if isinstance(results['languages'], dict) else results['languages']
            if lang_values and isinstance(lang_values[0], str):
                # Convert simple list to detailed format
                output['languages'] = [{'code': lang, 'pct': 1.0 / len(lang_values)} for lang in lang_values]
        
        if 'content_types' in results:
            output['content_types'] = results['content_types']
        
        if 'temporal_coverage' in results:
            output['temporal_coverage'] = results['temporal_coverage']
        
        if 'pii_signals' in results:
            output['pii_signals'] = results['pii_signals']
        
        if 'synthetic_data_presence' in results:
            synth_val = results['synthetic_data_presence']
            # Ensure synthetic_data_presence is an object
            if isinstance(synth_val, str):
                output['synthetic_data_presence'] = {
                    'detected': synth_val.lower() in ['yes', 'true', 'detected'],
                    'evidence': synth_val
                }
            elif isinstance(synth_val, dict):
                output['synthetic_data_presence'] = synth_val
            else:
                output['synthetic_data_presence'] = {'detected': False}
        
        if 'dataset_card' in results:
            output['dataset_card'] = results['dataset_card']
        
        if 'line_token_estimates' in results:
            output['line_token_estimates'] = results['line_token_estimates']
        
        if 'provenance_summary' in results:
            prov_val = results['provenance_summary']
            # Ensure provenance_summary is a string
            if isinstance(prov_val, dict):
                output['provenance_summary'] = str(prov_val.get('description', prov_val))
            else:
                output['provenance_summary'] = str(prov_val) if prov_val else ''
    
    return output