"""
Local suggestors for Q&A pre-fill.
These compute hints locally to reduce questions but are NOT uploaded by default.
Only included in payload with --profile enhanced.
"""

import re
import json
import logging
from pathlib import Path
from typing import Dict, List, Any, Optional
from collections import Counter
from urllib.parse import urlparse

logger = logging.getLogger(__name__)

# Language detection patterns (lightweight, heuristic)
LANGUAGE_PATTERNS = {
    'en': {
        'stop_words': ['the', 'and', 'is', 'to', 'of', 'in', 'that', 'it', 'for', 'with'],
        'unicode_range': (0x0000, 0x007F)
    },
    'de': {
        'stop_words': ['der', 'die', 'das', 'und', 'ist', 'ein', 'eine', 'zu', 'den', 'mit'],
        'unicode_range': (0x0000, 0x007F)
    },
    'fr': {
        'stop_words': ['le', 'de', 'et', 'la', 'les', 'des', 'un', 'une', 'dans', 'pour'],
        'unicode_range': (0x0000, 0x007F)
    },
    'es': {
        'stop_words': ['el', 'la', 'de', 'y', 'los', 'las', 'un', 'una', 'en', 'por'],
        'unicode_range': (0x0000, 0x007F)
    },
    'zh': {
        'stop_words': [],
        'unicode_range': (0x4E00, 0x9FFF)  # CJK Unified Ideographs
    },
    'ja': {
        'stop_words': [],
        'unicode_range': (0x3040, 0x309F)  # Hiragana
    },
    'ko': {
        'stop_words': [],
        'unicode_range': (0xAC00, 0xD7AF)  # Hangul Syllables
    },
    'ar': {
        'stop_words': [],
        'unicode_range': (0x0600, 0x06FF)  # Arabic
    },
    'ru': {
        'stop_words': [],
        'unicode_range': (0x0400, 0x04FF)  # Cyrillic
    }
}

# Valid TLDs for domain extraction
VALID_TLDS = {
    'com', 'org', 'net', 'edu', 'gov', 'io', 'ai', 'dev', 'app',
    'co', 'uk', 'de', 'fr', 'es', 'it', 'nl', 'se', 'no', 'ch',
    'ca', 'au', 'nz', 'in', 'jp', 'kr', 'cn', 'co.uk', 'ac.uk',
    'eu', 'me', 'info', 'biz', 'tv', 'cc', 'ws', 'xyz', 'tech'
}

# License patterns
LICENSE_PATTERNS = {
    'MIT': ['MIT License', 'MIT ', 'Permission is hereby granted, free of charge'],
    'Apache-2.0': ['Apache License', 'Version 2.0', 'Apache-2.0', 'Licensed under the Apache'],
    'GPL-3.0': ['GNU General Public License', 'GPL-3.0', 'GPLv3', 'GNU GPL version 3'],
    'BSD-3-Clause': ['BSD 3-Clause', 'BSD License', 'Redistribution and use in source'],
    'CC-BY-4.0': ['Creative Commons Attribution', 'CC BY 4.0', 'CC-BY-4.0'],
    'CC0-1.0': ['CC0', 'Public Domain', 'No Rights Reserved'],
    'ISC': ['ISC License', 'ISC '],
    'MPL-2.0': ['Mozilla Public License', 'MPL-2.0', 'MPL 2.0']
}

class LocalSuggestor:
    """Compute local suggestions for Q&A pre-fill."""
    
    def __init__(self):
        """Initialize suggestor."""
        self.max_files_to_sample = 100
        self.max_bytes_per_file = 10000
    
    def suggest_all(self, dataset_paths: List[str]) -> Dict[str, Any]:
        """
        Compute all suggestions locally.
        
        Args:
            dataset_paths: List of dataset paths
            
        Returns:
            Dict with languages, domains, licenses, synthetic markers
        """
        return {
            "languages": self.suggest_languages(dataset_paths),
            "domains": self.suggest_domains(dataset_paths),
            "licenses": self.suggest_licenses(dataset_paths),
            "synthetic": self.suggest_synthetic(dataset_paths)
        }
    
    def suggest_languages(self, dataset_paths: List[str]) -> Dict[str, float]:
        """
        Detect language distribution from small samples.
        
        Returns:
            Language histogram like {"en": 0.72, "de": 0.18, "fr": 0.10}
        """
        language_scores = Counter()
        total_samples = 0
        
        for path_str in dataset_paths:
            path = Path(path_str)
            files_sampled = 0
            
            # Sample text files
            for file_path in self._iter_text_files(path):
                if files_sampled >= self.max_files_to_sample:
                    break
                
                try:
                    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                        content = f.read(self.max_bytes_per_file)
                        
                    # Score each language
                    for lang, patterns in LANGUAGE_PATTERNS.items():
                        score = self._score_language(content, patterns)
                        if score > 0:
                            language_scores[lang] += score
                            total_samples += 1
                    
                    files_sampled += 1
                    
                except Exception as e:
                    logger.debug(f"Skip file for language detection: {e.__class__.__name__}")
                    continue
        
        # Normalize to percentages
        result = {}
        if total_samples > 0:
            total_score = sum(language_scores.values())
            for lang, score in language_scores.most_common(5):
                pct = round(score / total_score, 2)
                if pct >= 0.05:  # Only include if >5%
                    result[lang] = pct
        
        # Default to English if nothing detected
        if not result:
            result = {"en": 1.0}
        
        return result
    
    def suggest_domains(self, dataset_paths: List[str]) -> Dict[str, int]:
        """
        Extract domain names from URL fields in JSON/CSV files.
        
        Returns:
            Domain counts like {"github.com": 1000, "wikipedia.org": 500}
        """
        domains = Counter()
        
        for path_str in dataset_paths:
            path = Path(path_str)
            
            # Look for JSON/CSV files that might contain URLs
            for file_path in self._iter_data_files(path):
                try:
                    if file_path.suffix.lower() == '.json':
                        domains.update(self._extract_domains_from_json(file_path))
                    elif file_path.suffix.lower() in ['.csv', '.tsv']:
                        domains.update(self._extract_domains_from_csv(file_path))
                    elif file_path.suffix.lower() in ['.txt', '.md']:
                        domains.update(self._extract_domains_from_text(file_path))
                except Exception as e:
                    logger.debug(f"Skip file for domain extraction: {e.__class__.__name__}")
                    continue
        
        # Return top domains
        return dict(domains.most_common(100))
    
    def suggest_licenses(self, dataset_paths: List[str]) -> Dict[str, int]:
        """
        Detect licenses from LICENSE files and SPDX identifiers.
        
        Returns:
            License counts like {"MIT": 5, "Apache-2.0": 2}
        """
        licenses = Counter()
        
        for path_str in dataset_paths:
            path = Path(path_str)
            
            # Check for LICENSE files
            for pattern in ['LICENSE', 'LICENSE.*', 'LICENCE', 'LICENCE.*', 
                          'COPYING', 'NOTICE', 'COPYRIGHT']:
                for license_file in path.rglob(pattern):
                    if license_file.is_file():
                        try:
                            with open(license_file, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read(5000)
                            
                            # Check for known license patterns
                            for spdx_id, patterns in LICENSE_PATTERNS.items():
                                for pattern in patterns:
                                    if pattern.lower() in content.lower():
                                        licenses[spdx_id] += 1
                                        break
                        except:
                            continue
            
            # Also check README files for license mentions
            for readme in path.rglob('README*'):
                if readme.is_file():
                    try:
                        with open(readme, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read(5000)
                        
                        # Look for SPDX identifiers
                        spdx_match = re.search(r'SPDX-License-Identifier:\s*(\S+)', content)
                        if spdx_match:
                            licenses[spdx_match.group(1)] += 1
                    except:
                        continue
        
        return dict(licenses)
    
    def suggest_synthetic(self, dataset_paths: List[str]) -> Dict[str, Any]:
        """
        Detect synthetic data markers.
        
        Returns:
            Synthetic indicators like {"detected": true, "markers": ["generated", "synthetic"]}
        """
        synthetic_keywords = [
            'synthetic', 'generated', 'artificial', 'augmented',
            'simulated', 'fake', 'pseudo', 'manufactured'
        ]
        
        markers_found = set()
        
        for path_str in dataset_paths:
            path = Path(path_str)
            path_lower = str(path).lower()
            
            # Check path name
            for keyword in synthetic_keywords:
                if keyword in path_lower:
                    markers_found.add(keyword)
            
            # Check README and dataset cards
            for doc_name in ['README.md', 'README.txt', 'dataset_card.md', 
                           'DATASET_CARD.md', 'metadata.json']:
                for doc_file in path.rglob(doc_name):
                    if doc_file.is_file():
                        try:
                            with open(doc_file, 'r', encoding='utf-8', errors='ignore') as f:
                                content = f.read(5000).lower()
                            
                            for keyword in synthetic_keywords:
                                if keyword in content:
                                    markers_found.add(keyword)
                        except:
                            continue
        
        return {
            "detected": len(markers_found) > 0,
            "markers": list(markers_found)
        }
    
    # Helper methods
    
    def _iter_text_files(self, path: Path, max_files: int = 100):
        """Iterate over text files for sampling."""
        count = 0
        patterns = ['*.txt', '*.md', '*.json', '*.jsonl', '*.csv', '*.tsv']
        
        if path.is_file():
            yield path
            return
        
        for pattern in patterns:
            for file_path in path.rglob(pattern):
                if count >= max_files:
                    return
                if file_path.is_file():
                    yield file_path
                    count += 1
    
    def _iter_data_files(self, path: Path, max_files: int = 50):
        """Iterate over data files that might contain URLs."""
        count = 0
        patterns = ['*.json', '*.jsonl', '*.csv', '*.tsv', '*.txt', '*.md']
        
        if path.is_file():
            yield path
            return
        
        for pattern in patterns:
            for file_path in path.rglob(pattern):
                if count >= max_files:
                    return
                if file_path.is_file():
                    yield file_path
                    count += 1
    
    def _score_language(self, content: str, patterns: Dict) -> float:
        """Score content for a specific language."""
        score = 0.0
        
        # Check stop words (for Latin-based languages)
        if patterns['stop_words']:
            words = content.lower().split()[:500]
            for word in patterns['stop_words']:
                score += words.count(word)
        
        # Check Unicode ranges (for non-Latin scripts)
        if patterns['unicode_range'] != (0x0000, 0x007F):
            start, end = patterns['unicode_range']
            char_count = sum(1 for c in content[:1000] if start <= ord(c) <= end)
            if char_count > 10:
                score += char_count / 10
        
        return score
    
    def _extract_domains_from_json(self, file_path: Path) -> Counter:
        """Extract domains from JSON files."""
        domains = Counter()
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                # Read in chunks for large files
                content = f.read(100000)  # 100KB sample
                
            # Try to parse as JSON or JSONL
            try:
                data = json.loads(content)
                urls = self._extract_urls_from_obj(data)
            except:
                # Try JSONL
                urls = []
                for line in content.split('\n')[:100]:
                    try:
                        obj = json.loads(line)
                        urls.extend(self._extract_urls_from_obj(obj))
                    except:
                        continue
            
            # Extract domains from URLs
            for url in urls:
                domain = self._extract_domain(url)
                if domain:
                    domains[domain] += 1
                    
        except:
            pass
        
        return domains
    
    def _extract_domains_from_csv(self, file_path: Path) -> Counter:
        """Extract domains from CSV files."""
        domains = Counter()
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                # Sample first 1000 lines
                for i, line in enumerate(f):
                    if i >= 1000:
                        break
                    
                    # Look for URLs in the line
                    urls = re.findall(r'https?://[^\s,;"\']+', line)
                    for url in urls:
                        domain = self._extract_domain(url)
                        if domain:
                            domains[domain] += 1
        except:
            pass
        
        return domains
    
    def _extract_domains_from_text(self, file_path: Path) -> Counter:
        """Extract domains from text files."""
        domains = Counter()
        
        try:
            with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read(50000)  # 50KB sample
            
            # Find URLs
            urls = re.findall(r'https?://[^\s<>"{}|\\^`\[\]]+', content)
            for url in urls:
                domain = self._extract_domain(url)
                if domain:
                    domains[domain] += 1
                    
        except:
            pass
        
        return domains
    
    def _extract_urls_from_obj(self, obj: Any, urls: Optional[List] = None) -> List[str]:
        """Recursively extract URLs from JSON object."""
        if urls is None:
            urls = []
        
        if isinstance(obj, str):
            if obj.startswith(('http://', 'https://')):
                urls.append(obj)
        elif isinstance(obj, dict):
            for value in obj.values():
                self._extract_urls_from_obj(value, urls)
        elif isinstance(obj, list):
            for item in obj[:100]:  # Limit recursion
                self._extract_urls_from_obj(item, urls)
        
        return urls
    
    def _extract_domain(self, url: str) -> Optional[str]:
        """Extract and validate domain from URL."""
        try:
            parsed = urlparse(url)
            if parsed.netloc:
                domain = parsed.netloc.lower()
                # Remove port if present
                domain = domain.split(':')[0]
                # Remove www prefix
                if domain.startswith('www.'):
                    domain = domain[4:]
                
                # Validate TLD
                if self._is_valid_domain(domain):
                    return domain
        except:
            pass
        
        return None
    
    def _is_valid_domain(self, domain: str) -> bool:
        """Check if domain has valid TLD."""
        if '.' not in domain:
            return False
        
        parts = domain.split('.')
        if len(parts) >= 2:
            # Check composite TLDs like co.uk
            if len(parts) >= 3 and f"{parts[-2]}.{parts[-1]}" in VALID_TLDS:
                return True
            # Check simple TLD
            return parts[-1] in VALID_TLDS
        
        return False