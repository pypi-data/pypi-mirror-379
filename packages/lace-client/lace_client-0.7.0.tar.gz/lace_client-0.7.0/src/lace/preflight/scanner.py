"""
Dataset scanner with deterministic sampling and signal extraction.
"""

import re
import hashlib
import json
import time
import concurrent.futures
from pathlib import Path
from typing import Dict, Any, List, Optional, Set, Tuple
from urllib.parse import urlparse
import logging

import httpx

from .registry import Registry
from .pii_detector import PIIDetector
from .license_detector import LicenseDetector
from .pdf_analyzer import PDFAnalyzer

logger = logging.getLogger(__name__)


class DatasetScanner:
    """Scans datasets for opt-out, license, and PII signals."""
    
    def __init__(self, config):
        """Initialize scanner with config."""
        self.config = config
        self.pii_detector = PIIDetector(config.pii_mode)
        self.license_detector = LicenseDetector()
        self.pdf_analyzer = PDFAnalyzer()
        
        # Deterministic sampling seed
        self.sampling_seed = "preflight.v0.1"
        
    def scan(
        self,
        dataset_path: Path,
        registry: Registry,
        budget_seconds: float,
        network_tracker: Dict[str, Any],
        no_network: bool = False
    ) -> Dict[str, Any]:
        """
        Scan dataset within budget.
        
        Returns:
            Signals dict with opt_out, license, pii, pdf findings
        """
        start_time = time.time()
        
        # Collect files
        files = self._collect_files(dataset_path)
        total_files = len(files)
        total_bytes = sum(f.stat().st_size for f in files if f.exists())
        
        # Deterministic sampling
        sampled_files = self._sample_files(files, self.config.sample_rate)
        
        logger.info(f"Scanning {len(sampled_files)}/{total_files} files "
                   f"(sample_rate={self.config.sample_rate})")
        
        # Initialize signal collectors
        signals = {
            'file_count': total_files,
            'byte_count': total_bytes,
            'opt_out': {
                'deny_domains': [],
                'suspect_domains': [],
                'summary': {'deny': 0, 'suspect': 0}
            },
            'license': {
                'summary': {'spdx': {}, 'noassertion': 0},
                'flags': []
            },
            'pii': {
                'coverage': {
                    'sample_rate': self.config.sample_rate,
                    'files_scanned': len(sampled_files)
                },
                'findings': {},
                'severity': 'none'
            },
            'pdf': {
                'with_origin': 0,
                'examples': []
            }
        }
        
        # Extract domains from dataset
        domains = self._extract_domains(sampled_files, budget_seconds, start_time)
        
        # Check domains against registry
        with concurrent.futures.ThreadPoolExecutor(max_workers=self.config.max_concurrency) as executor:
            futures = []
            
            for domain in domains:
                # Check time budget
                if time.time() - start_time > budget_seconds * 0.8:
                    logger.debug("Approaching budget limit, stopping domain checks")
                    break
                
                future = executor.submit(self._check_domain, domain, registry, no_network, network_tracker)
                futures.append((domain, future))
            
            # Collect results
            for domain, future in futures:
                try:
                    result = future.result(timeout=2)
                    if result:
                        if result['verdict'] == 'deny':
                            signals['opt_out']['deny_domains'].append(result)
                            signals['opt_out']['summary']['deny'] += 1
                        elif result['verdict'] == 'suspect':
                            signals['opt_out']['suspect_domains'].append(result)
                            signals['opt_out']['summary']['suspect'] += 1
                except Exception as e:
                    logger.debug(f"Domain check failed for {domain}: {e}")
        
        # License detection
        for f in sampled_files[:100]:  # Limit license checks
            if time.time() - start_time > budget_seconds * 0.9:
                break
            
            license_info = self.license_detector.detect(f)
            if license_info:
                if license_info['type'] == 'spdx':
                    spdx = license_info['identifier']
                    signals['license']['summary']['spdx'][spdx] = \
                        signals['license']['summary']['spdx'].get(spdx, 0) + 1
                elif license_info['type'] == 'flag':
                    signals['license']['flags'].append(license_info)
                else:
                    signals['license']['summary']['noassertion'] += 1
        
        # PII detection (if enabled)
        if self.config.pii_mode != 'off':
            pii_findings = self.pii_detector.scan_files(sampled_files, budget_seconds * 0.1)
            signals['pii']['findings'] = pii_findings['counts']
            signals['pii']['severity'] = pii_findings['severity']
        
        # PDF analysis
        pdf_files = [f for f in sampled_files if f.suffix.lower() == '.pdf']
        for pdf in pdf_files[:20]:  # Limit PDF checks
            if time.time() - start_time > budget_seconds * 0.95:
                break
            
            origin = self.pdf_analyzer.extract_origin(pdf)
            if origin:
                signals['pdf']['with_origin'] += 1
                if len(signals['pdf']['examples']) < 5:
                    signals['pdf']['examples'].append({
                        'file': str(pdf.relative_to(dataset_path)),
                        'origin': origin
                    })
        
        return signals
    
    def _collect_files(self, dataset_path: Path) -> List[Path]:
        """Collect all files in dataset."""
        if dataset_path.is_file():
            return [dataset_path]
        
        files = []
        for pattern in ['**/*.txt', '**/*.json', '**/*.jsonl', '**/*.csv', 
                       '**/*.md', '**/*.pdf', '**/*.py', '**/*.js']:
            files.extend(dataset_path.glob(pattern))
        
        return sorted(set(files))  # Sort for determinism
    
    def _sample_files(self, files: List[Path], sample_rate: float) -> List[Path]:
        """
        Deterministically sample files based on path hash.
        
        This ensures the same files are always sampled for a given dataset.
        """
        sampled = []
        
        for f in files:
            # Hash file path with seed for deterministic sampling
            path_hash = hashlib.sha256(f"{self.sampling_seed}:{f}".encode()).hexdigest()
            # Convert first 8 hex chars to float in [0, 1)
            sample_value = int(path_hash[:8], 16) / (16 ** 8)
            
            if sample_value < sample_rate:
                sampled.append(f)
        
        return sampled
    
    def _extract_domains(self, files: List[Path], budget: float, start_time: float) -> Set[str]:
        """Extract unique domains from files."""
        domains = set()
        url_pattern = re.compile(r'https?://([a-zA-Z0-9.-]+\.[a-zA-Z]{2,})')
        
        for f in files:
            # Check budget
            if time.time() - start_time > budget * 0.5:
                break
            
            try:
                # Read first 100KB of file
                with open(f, 'r', encoding='utf-8', errors='ignore') as fh:
                    content = fh.read(102400)
                
                # Extract URLs
                matches = url_pattern.findall(content)
                domains.update(matches)
                
                # Also check for explicit domain references
                if 'dataset_card' in f.name.lower() or 'readme' in f.name.lower():
                    # Look for source references
                    for line in content.split('\n'):
                        if 'source' in line.lower() or 'url' in line.lower():
                            matches = url_pattern.findall(line)
                            domains.update(matches)
                
            except Exception as e:
                logger.debug(f"Failed to extract domains from {f}: {e}")
        
        return domains
    
    def _check_domain(
        self,
        domain: str,
        registry: Registry,
        no_network: bool,
        network_tracker: Dict[str, Any]
    ) -> Optional[Dict[str, Any]]:
        """
        Check domain against registry and optionally fetch robots.txt.
        
        Returns:
            None or dict with verdict and evidence
        """
        # First check registry
        registry_hit = registry.check_domain(domain)
        if registry_hit:
            return {
                'domain': domain,
                'verdict': 'deny',
                'source': registry_hit.get('source', 'registry'),
                'evidence': registry_hit.get('evidence_url', ''),
                'rule': registry_hit.get('rule', ''),
                'confidence': registry_hit.get('confidence', 0.9)
            }
        
        # If no network, we're done
        if no_network:
            return None
        
        # Try to fetch robots.txt (within time/network budget)
        if network_tracker['used_ms'] > 10000:  # 10s network budget
            return None
        
        try:
            start = time.time()
            robots_url = f"https://{domain}/robots.txt"
            
            with httpx.Client(timeout=httpx.Timeout(connect=2, read=3)) as client:
                resp = client.get(robots_url, follow_redirects=True)
                
            network_tracker['used_ms'] += int((time.time() - start) * 1000)
            network_tracker['calls'] += 1
            
            if resp.status_code == 200:
                content = resp.text.lower()
                
                # Check for AI bot exclusions
                ai_bots = ['gptbot', 'chatgpt', 'claudebot', 'anthropic', 'ccbot', 
                          'google-extended', 'omgilibot', 'facebookbot']
                
                for bot in ai_bots:
                    if f"user-agent: {bot}" in content:
                        # Check if disallowed
                        lines = content.split('\n')
                        for i, line in enumerate(lines):
                            if f"user-agent: {bot}" in line:
                                # Check next few lines for disallow
                                for j in range(i+1, min(i+5, len(lines))):
                                    if 'disallow: /' in lines[j]:
                                        return {
                                            'domain': domain,
                                            'verdict': 'deny',
                                            'source': 'robots.txt',
                                            'evidence': robots_url,
                                            'rule': f"Disallow for {bot}",
                                            'confidence': 0.95
                                        }
        
        except Exception as e:
            logger.debug(f"Failed to fetch robots.txt for {domain}: {e}")
        
        # Try ai.txt if we have budget
        if network_tracker['used_ms'] < 15000:
            try:
                start = time.time()
                ai_url = f"https://{domain}/ai.txt"
                
                with httpx.Client(timeout=httpx.Timeout(connect=2, read=3)) as client:
                    resp = client.get(ai_url, follow_redirects=True)
                
                network_tracker['used_ms'] += int((time.time() - start) * 1000)
                network_tracker['calls'] += 1
                
                if resp.status_code == 200:
                    content = resp.text.lower()
                    if 'ai-training: no' in content or 'crawl: no' in content:
                        return {
                            'domain': domain,
                            'verdict': 'deny',
                            'source': 'ai.txt',
                            'evidence': ai_url,
                            'rule': 'ai-training: no',
                            'confidence': 0.95
                        }
            
            except Exception:
                pass
        
        return None