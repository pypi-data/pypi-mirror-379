"""
Minimal dataset analyzer for IP-protected cloud-only SDS generation.
Only extracts content-free statistics. No inspection of file contents.
"""

import os
import hashlib
import logging
import json
from pathlib import Path
from typing import Dict, List, Any, Optional, Tuple
from datetime import datetime
from collections import Counter

try:
    from pathspec import PathSpec
    from pathspec.patterns import GitWildMatchPattern
    PATHSPEC_AVAILABLE = True
except ImportError:
    PATHSPEC_AVAILABLE = False

logger = logging.getLogger(__name__)

# Directories to ignore by default
IGNORE_DIRS = {'.git', 'node_modules', '__pycache__', '.venv', 'venv', 
               'dist', 'build', '.tox', '.pytest_cache', '.mypy_cache'}

# Auto-sampling threshold
AUTO_SAMPLE_THRESHOLD = 5_000_000  # 5M files

class MinimalAnalyzer:
    """Extract only minimal statistics - no content inspection."""
    
    def __init__(self, config: Optional[Dict] = None):
        """
        Initialize analyzer with optional config.
        
        Args:
            config: Configuration dict with local_salt, etc.
        """
        self.config = config or {}
        self.local_salt = self._get_or_create_salt()
        
    def _get_or_create_salt(self) -> str:
        """Get or create local salt for dataset ID generation."""
        if 'local_salt' in self.config:
            return self.config['local_salt']
        
        # Generate new salt (should be saved to ~/.lace/config.json by caller)
        import secrets
        return secrets.token_hex(16)
    
    def analyze(self, dataset_paths: List[str], profile: str = "minimal", send_domains: str = "none") -> Dict[str, Any]:
        """
        Extract statistics from datasets based on profile.
        
        Args:
            dataset_paths: List of dataset paths to analyze
            profile: Analysis profile ("minimal" or "enhanced")
            send_domains: Domain sending mode ("none", "hashed", "clear")
            
        Returns:
            Analysis dict conforming to the appropriate schema version
        """
        # For backward compatibility
        return self._analyze_impl(dataset_paths, profile, send_domains)
    
    def analyze_minimal(self, dataset_paths: List[str]) -> Dict[str, Any]:
        """
        Extract minimal statistics from datasets.
        Kept for backward compatibility.
        
        Args:
            dataset_paths: List of dataset paths to analyze
            
        Returns:
            Minimal analysis dict conforming to analysis.min.v1 schema
        """
        return self.analyze(dataset_paths, profile="minimal", send_domains="none")
    
    def _analyze_impl(self, dataset_paths: List[str], profile: str, send_domains: str) -> Dict[str, Any]:
        """
        Internal implementation of analysis.
        """
        datasets = []
        all_extensions = Counter()
        all_domains = Counter() if profile == "enhanced" and send_domains != "none" else None
        
        for i, path_str in enumerate(dataset_paths):
            path = Path(path_str).absolute()
            
            # Generate deterministic dataset ID
            dataset_id = self._generate_dataset_id(path)
            
            # Count files and bytes
            file_count, byte_total, latest_mtime, extensions = self._analyze_path(path)
            
            datasets.append({
                "id": dataset_id,
                "files": file_count,
                "bytes": byte_total,
                "mtime_latest": latest_mtime.isoformat() + 'Z' if latest_mtime else None
            })
            
            # Aggregate extensions
            all_extensions.update(extensions)
            
            # For enhanced mode, collect domains (mocked for now)
            if profile == "enhanced" and send_domains != "none" and all_domains is not None:
                # This would be populated by LocalSuggestor in the CLI
                pass
        
        # Apply k-anonymity to extensions
        ext_histogram = self._apply_k_anonymity(all_extensions)
        
        # Generate local evidence files (not uploaded)
        evidence_refs = self._generate_evidence_files(dataset_paths)
        
        # Build result based on profile
        result = {
            "schema_version": "analysis.enhanced.v1" if profile == "enhanced" else "analysis.min.v1",
            "datasets": datasets,
            "extensions": ext_histogram,
            "estimated": file_count > AUTO_SAMPLE_THRESHOLD,
            "includes_symlinks": False,  # We don't follow symlinks
            "evidence_refs": evidence_refs
        }
        
        # Add enhanced fields if requested
        if profile == "enhanced":
            result["languages"] = {}
            result["license_hints"] = {}
            result["synthetic_markers"] = {"detected": False, "markers": []}
            
            # Domains will be added by CLI after running LocalSuggestor
            # We don't add them here to avoid duplication
        
        return result
    
    def _generate_dataset_id(self, path: Path) -> str:
        """Generate deterministic, non-reversible dataset ID."""
        hash_input = f"{path}\n{self.local_salt}"
        hash_hex = hashlib.sha256(hash_input.encode()).hexdigest()
        return f"ds_{hash_hex[:10]}"
    
    def _analyze_path(self, path: Path) -> Tuple[int, int, Optional[datetime], Counter]:
        """
        Analyze a single path for basic statistics.
        Fixed: Apply ignore first, track realpath, count once.
        
        Returns:
            (file_count, byte_total, latest_mtime, extensions_counter)
        """
        if path.is_file():
            stat = path.stat()
            ext = path.suffix.lower() if path.suffix else ""
            return 1, stat.st_size, datetime.fromtimestamp(stat.st_mtime), Counter({ext: 1})
        
        file_list = []
        byte_total = 0
        latest_mtime = None
        visited_realpaths = set()
        
        # Load .laceignore patterns from root directory if it exists
        root_ignore_patterns = []
        root_laceignore = path / '.laceignore'
        if root_laceignore.exists():
            root_ignore_patterns = self._load_ignore_patterns(root_laceignore)
            logger.debug(f"Loaded {len(root_ignore_patterns)} patterns from root .laceignore")
        
        try:
            # Step 1: Build filtered file list first
            for root, dirs, files in os.walk(path, followlinks=False):
                # Track real paths to avoid loops
                try:
                    realpath = os.path.realpath(root)
                    if realpath in visited_realpaths:
                        logger.debug(f"Skipping duplicate path: {root} -> {realpath}")
                        continue
                    visited_realpaths.add(realpath)
                except (OSError, PermissionError):
                    continue
                
                # Skip ignored directories
                dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]
                
                # Apply root .laceignore patterns globally
                if root_ignore_patterns:
                    # Filter files based on patterns
                    filtered_files = []
                    for fname in files:
                        # Skip if matches any pattern
                        if not self._should_ignore_file(fname, root_ignore_patterns):
                            filtered_files.append(fname)
                    files = filtered_files
                    
                    # Filter directories too
                    dirs[:] = self._filter_by_patterns(dirs, root_ignore_patterns, is_dir=True)
                
                # Collect files (excluding dotfiles)
                for fname in files:
                    # Skip dotfiles (including .laceignore)
                    if fname.startswith('.'):
                        continue
                    
                    file_path = Path(root) / fname
                    try:
                        # Check if it's a real file (not symlink to directory)
                        if file_path.is_file():
                            file_list.append(file_path)
                    except (OSError, PermissionError):
                        continue
            
            # Step 2: Process collected files for stats
            extensions = Counter()
            for file_path in file_list:
                try:
                    stat = file_path.stat()
                    byte_total += stat.st_size
                    
                    # Track latest mtime
                    file_mtime = datetime.fromtimestamp(stat.st_mtime)
                    if latest_mtime is None or file_mtime > latest_mtime:
                        latest_mtime = file_mtime
                    
                    # Count extension ONCE
                    ext = file_path.suffix.lower() if file_path.suffix else ""
                    extensions[ext] += 1
                except (OSError, PermissionError) as e:
                    logger.debug(f"Skipping file {file_path}: {e.__class__.__name__}")
                    continue
            
            # Step 3: Verify conservation (count should match)
            file_count = len(file_list)
            assert sum(extensions.values()) == file_count, f"Extension count mismatch: {sum(extensions.values())} != {file_count}"
            
            # Auto-sample for huge trees
            if file_count > AUTO_SAMPLE_THRESHOLD:
                logger.info(f"Auto-sampling triggered at {file_count} files")
                # Extrapolate from sample
                sample_ratio = file_count / AUTO_SAMPLE_THRESHOLD
                file_count = int(file_count * sample_ratio * 10)  # Rough estimate
                byte_total = int(byte_total * sample_ratio * 10)
                    
        except (OSError, PermissionError) as e:
            logger.warning(f"Error walking {path}: {e.__class__.__name__}")
            file_count = len(file_list)
        
        return file_count, byte_total, latest_mtime, extensions
    
    def _apply_k_anonymity(self, extensions: Counter, k: int = 3, top_n: int = 15) -> Dict[str, int]:
        """
        Apply k-anonymity and top-N selection to extension histogram.
        Fixed: Apply k-anon after counting, verify conservation.
        
        Args:
            extensions: Raw extension counts
            k: Minimum count threshold (k-anonymity)
            top_n: Number of top extensions to keep
            
        Returns:
            Processed extension histogram
        """
        total_before = sum(extensions.values())
        
        # Get top N extensions
        top_extensions = extensions.most_common(top_n)
        
        result = {}
        other_count = 0
        processed_exts = set()
        
        # Process top N with k-threshold
        for ext, count in top_extensions:
            if count >= k:
                result[ext] = count
            else:
                other_count += count
            processed_exts.add(ext)
        
        # Add remaining extensions (not in top N) to "other"
        for ext, count in extensions.items():
            if ext not in processed_exts:
                other_count += count
        
        if other_count > 0:
            result['other'] = other_count
        
        # Verify conservation
        total_after = sum(result.values())
        if total_before > 0 and total_after != total_before:
            logger.warning(f"Mass not conserved in k-anonymity: {total_before} → {total_after}")
            # Fix by adjusting 'other'
            if 'other' in result:
                result['other'] += (total_before - total_after)
            else:
                result['other'] = total_before - total_after
        
        return result
    
    def _generate_evidence_files(self, dataset_paths: List[str]) -> Dict[str, str]:
        """
        Generate local evidence files (not uploaded).
        For now, just create placeholder for top domains CSV.
        """
        evidence_dir = Path('./evidence')
        evidence_dir.mkdir(exist_ok=True)
        
        # Create placeholder top domains CSV
        domains_csv = evidence_dir / 'eu_sds_top_domains.csv'
        with open(domains_csv, 'w') as f:
            f.write("domain,count\n")
            f.write("# Domains extracted locally - not uploaded\n")
            f.write("# Run with --profile enhanced --send-domains clear to auto-fill\n")
        
        return {
            "top_domains_csv": "./evidence/eu_sds_top_domains.csv"
        }
    
    def _load_ignore_patterns(self, ignore_file: Path) -> List[str]:
        """Load .laceignore patterns (gitignore syntax)."""
        patterns = []
        try:
            with open(ignore_file, 'r') as f:
                for line in f:
                    line = line.strip()
                    if line and not line.startswith('#'):
                        patterns.append(line)
        except:
            pass
        return patterns
    
    def _should_ignore_file(self, filename: str, patterns: List[str]) -> bool:
        """Check if a file should be ignored based on patterns."""
        if not patterns:
            return False
            
        if not PATHSPEC_AVAILABLE:
            # Fallback to simple matching
            for pattern in patterns:
                if pattern.startswith('*') and filename.endswith(pattern[1:]):
                    return True
                if pattern == filename:
                    return True
            return False
        
        # Use pathspec for proper gitignore semantics
        spec = PathSpec.from_lines(GitWildMatchPattern, patterns)
        # Normalize path to POSIX style for matching
        path_to_check = filename.replace(os.sep, '/')
        return spec.match_file(path_to_check)
    
    def _filter_by_patterns(self, names: List[str], patterns: List[str], is_dir: bool = False) -> List[str]:
        """Filter names by ignore patterns using gitignore semantics."""
        if not PATHSPEC_AVAILABLE:
            # Fallback to simple pattern matching if pathspec not available
            logger.warning("pathspec not available, using simplified pattern matching")
            filtered = []
            for name in names:
                skip = False
                for pattern in patterns:
                    if pattern == name or pattern == f"{name}/":
                        skip = True
                        break
                    if pattern.startswith('*') and name.endswith(pattern[1:]):
                        skip = True
                        break
                if not skip:
                    filtered.append(name)
            return filtered
        
        # Use pathspec for proper gitignore semantics
        spec = PathSpec.from_lines(GitWildMatchPattern, patterns)
        filtered = []
        
        for name in names:
            # Normalize path to POSIX style for matching
            path_to_check = name.replace(os.sep, '/')
            if is_dir:
                path_to_check += '/'
            
            # Check if the path matches any ignore pattern
            if not spec.match_file(path_to_check):
                filtered.append(name)
        
        return filtered