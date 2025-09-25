"""
Data sampler with stratified MIME-based sampling.
Deterministic sampling for reproducibility.
"""

import hashlib
import mimetypes
import random
from pathlib import Path
from typing import List, Dict, Any, Optional, Set
import logging

logger = logging.getLogger(__name__)


class DataSampler:
    """Stratified sampling of datasets by MIME type."""
    
    def __init__(self, seed: str = "lace.check.v0.1"):
        """
        Initialize sampler with deterministic seed.
        
        Args:
            seed: Seed for reproducible sampling
        """
        self.seed = seed
        mimetypes.init()
        
        # Common MIME type groups for stratification
        self.mime_groups = {
            'text': ['text/plain', 'text/html', 'text/markdown', 'text/csv'],
            'code': ['text/x-python', 'text/x-c', 'application/javascript', 'text/x-java'],
            'data': ['application/json', 'application/xml', 'application/x-yaml'],
            'document': ['application/pdf', 'application/msword', 'application/vnd.openxmlformats-officedocument'],
            'image': ['image/jpeg', 'image/png', 'image/gif', 'image/svg+xml'],
            'audio': ['audio/mpeg', 'audio/wav', 'audio/ogg'],
            'video': ['video/mp4', 'video/mpeg', 'video/quicktime'],
            'archive': ['application/zip', 'application/x-tar', 'application/gzip'],
        }
        
        # Extensions to skip
        self.skip_extensions = {
            '.pyc', '.pyo', '.so', '.dylib', '.dll', '.o', '.a',
            '.git', '.svn', '.hg', '.bzr', '.DS_Store', '.egg-info',
            '__pycache__', '.pytest_cache', '.tox', '.coverage'
        }
        
        # Specific files to skip (manifest/control files)
        self.skip_files = {
            'manifest.jsonl', 'dataset_provenance.json', 
            'metadata.json', 'dataset_info.json',
            'README', 'README.md', 'README.txt', 'LICENSE',
            'CHANGELOG', 'CHANGELOG.md', 'TODO', 'TODO.md'
        }
        
        # Control file patterns to exclude - STRICT exclusions
        self.exclude_patterns = {
            '*.json', '*.jsonl', '*.csv', 'manifest.*', 'dataset_provenance.*',
            'README*', 'LICENSE*', 'CHANGELOG*', 'TODO*', '*.lock', '*.sum',
            '.*'  # All dotfiles
        }
        
        # Content file extensions allowlist - ONLY core content files
        # To process HTML, use --include-html flag (not implemented here)
        self.content_extensions = {
            '.txt', '.md'  # Core content only
            # HTML often brings noise, exclude by default:
            # '.html', '.htm' - enable via flag if needed
        }
        
        # Note: Strict exclusion of JSON/CSV metadata and non-text files
    
    def sample(
        self,
        paths: List[Path],
        sample_size: Optional[int] = None,
        sample_rate: Optional[float] = None,
        max_files: int = 5000
    ) -> List[Dict[str, Any]]:
        """
        Sample files from given paths using stratified sampling.
        
        Args:
            paths: List of paths to sample from
            sample_size: Exact number of files to sample
            sample_rate: Percentage of files to sample (0.0-1.0)
            max_files: Maximum files to sample (cap)
            
        Returns:
            List of sampled file info dicts
        """
        # Collect all files
        all_files = []
        for path in paths:
            if path.is_file():
                all_files.append(path)
            elif path.is_dir():
                all_files.extend(self._collect_files(path))
        
        # Filter out skipped extensions
        all_files = [f for f in all_files if not self._should_skip(f)]
        
        if not all_files:
            logger.warning("No files found to sample")
            return []
        
        # Determine sample size
        total_files = len(all_files)
        if sample_size:
            n_samples = min(sample_size, total_files)
        elif sample_rate:
            n_samples = int(total_files * sample_rate)
        else:
            # Default: max(1% of files, 100 files)
            n_samples = max(int(total_files * 0.01), 100)
        
        # Apply cap
        n_samples = min(n_samples, max_files, total_files)
        
        logger.info(f"Sampling {n_samples}/{total_files} files")
        
        # Group files by MIME type
        mime_groups = self._group_by_mime(all_files)
        
        # Stratified sampling
        sampled = self._stratified_sample(mime_groups, n_samples)
        
        return sampled
    
    def _collect_files(self, directory: Path) -> List[Path]:
        """Recursively collect files from directory."""
        files = []
        try:
            for item in directory.rglob('*'):
                if item.is_file() and not self._should_skip(item):
                    files.append(item)
        except (PermissionError, OSError) as e:
            logger.warning(f"Error accessing {directory}: {e}")
        return files
    
    def _should_skip(self, path: Path) -> bool:
        """Check if file should be skipped."""
        import fnmatch
        
        # Skip hidden files and directories
        for part in path.parts:
            if part.startswith('.') and part not in {'.', '..'}:
                if logger.isEnabledFor(logging.DEBUG):
                    logger.debug(f"Skipping hidden: {path}")
                return True
        
        # Skip specific manifest files
        if path.name in self.skip_files:
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(f"Skipping manifest file: {path}")
            return True
        
        # Skip by exclude patterns - STRICT (*.json, *.csv, dotfiles, etc.)
        for pattern in self.exclude_patterns:
            if fnmatch.fnmatch(path.name, pattern):
                if logger.isEnabledFor(logging.DEBUG):
                    logger.debug(f"Skipping by pattern {pattern}: {path}")
                return True
        
        # Skip by extension blacklist
        if path.suffix.lower() in self.skip_extensions:
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(f"Skipping by extension blacklist: {path}")
            return True
        
        # Skip by name patterns
        if path.name in self.skip_extensions:
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(f"Skipping by name blacklist: {path}")
            return True
        
        # Use STRICT allowlist: only .txt and .md by default
        # If no extension, skip it
        if not path.suffix:
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(f"Skipping no extension: {path}")
            return True
            
        # Only process files with content extensions (.txt, .md)
        if path.suffix.lower() not in self.content_extensions:
            if logger.isEnabledFor(logging.DEBUG):
                logger.debug(f"Skipping non-content extension {path.suffix}: {path}")
            return True
            
        return False
    
    def _get_mime_type(self, path: Path) -> str:
        """Get MIME type for file."""
        # First try by extension
        mime_type, _ = mimetypes.guess_type(str(path))
        
        if mime_type:
            return mime_type
        
        # Fallback based on extension patterns
        ext = path.suffix.lower()
        ext_to_mime = {
            '.py': 'text/x-python',
            '.js': 'application/javascript',
            '.ts': 'application/typescript',
            '.jsx': 'application/javascript',
            '.tsx': 'application/typescript',
            '.c': 'text/x-c',
            '.cpp': 'text/x-c++',
            '.h': 'text/x-c',
            '.java': 'text/x-java',
            '.go': 'text/x-go',
            '.rs': 'text/x-rust',
            '.rb': 'text/x-ruby',
            '.php': 'text/x-php',
            '.swift': 'text/x-swift',
            '.kt': 'text/x-kotlin',
            '.yaml': 'application/x-yaml',
            '.yml': 'application/x-yaml',
            '.toml': 'application/toml',
            '.md': 'text/markdown',
            '.rst': 'text/x-rst',
            '.ipynb': 'application/x-ipynb+json',
        }
        
        return ext_to_mime.get(ext, 'application/octet-stream')
    
    def _group_by_mime(self, files: List[Path]) -> Dict[str, List[Path]]:
        """Group files by MIME type."""
        groups = {}
        for file in files:
            mime_type = self._get_mime_type(file)
            if mime_type not in groups:
                groups[mime_type] = []
            groups[mime_type].append(file)
        return groups
    
    def _stratified_sample(
        self,
        mime_groups: Dict[str, List[Path]],
        n_samples: int
    ) -> List[Dict[str, Any]]:
        """
        Perform stratified sampling across MIME groups.
        
        Args:
            mime_groups: Files grouped by MIME type
            n_samples: Total number of samples needed
            
        Returns:
            List of sampled file info
        """
        # Calculate samples per group (proportional)
        total_files = sum(len(files) for files in mime_groups.values())
        samples_per_group = {}
        
        for mime_type, files in mime_groups.items():
            proportion = len(files) / total_files
            n_group_samples = max(1, int(n_samples * proportion))
            samples_per_group[mime_type] = min(n_group_samples, len(files))
        
        # Adjust if we're under/over target
        current_total = sum(samples_per_group.values())
        if current_total < n_samples:
            # Add more samples to larger groups
            remaining = n_samples - current_total
            for mime_type in sorted(mime_groups.keys(), 
                                   key=lambda x: len(mime_groups[x]), 
                                   reverse=True):
                available = len(mime_groups[mime_type]) - samples_per_group[mime_type]
                if available > 0:
                    add = min(available, remaining)
                    samples_per_group[mime_type] += add
                    remaining -= add
                    if remaining == 0:
                        break
        
        # Sample from each group deterministically
        sampled = []
        for mime_type, files in mime_groups.items():
            n_group = samples_per_group.get(mime_type, 0)
            if n_group > 0:
                # Deterministic sampling using hash-based selection
                group_samples = self._deterministic_sample(files, n_group)
                for file in group_samples:
                    sampled.append({
                        'path': file,
                        'mime_type': mime_type,
                        'size': file.stat().st_size if file.exists() else 0,
                    })
        
        return sampled
    
    def _deterministic_sample(self, items: List[Path], n: int) -> List[Path]:
        """
        Deterministically sample n items from list.
        Uses hash-based selection for reproducibility.
        """
        if n >= len(items):
            return items
        
        # Create deterministic scores for each item
        scored_items = []
        for item in items:
            # Hash combines seed + file path for deterministic score
            hash_input = f"{self.seed}:{item}".encode('utf-8')
            score = int(hashlib.sha256(hash_input).hexdigest(), 16)
            scored_items.append((score, item))
        
        # Sort by score and take top n
        scored_items.sort(key=lambda x: x[0])
        return [item for _, item in scored_items[:n]]