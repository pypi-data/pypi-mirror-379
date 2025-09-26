"""
Content fingerprinting with SHA256, MinHash, and perceptual hashing.
Extracts clean snippets for analysis.
"""

import hashlib
import logging
import re
import struct
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

logger = logging.getLogger(__name__)

# Optional imports with graceful fallback
try:
    import imagehash
    from PIL import Image

    HAS_IMAGE_SUPPORT = True
except ImportError:
    HAS_IMAGE_SUPPORT = False
    logger.debug("Image hashing not available (install pillow and imagehash)")


class MinHash:
    """Simple MinHash implementation for text similarity."""

    def __init__(self, num_perm: int = 128, seed: int = 42):
        """
        Initialize MinHash.

        Args:
            num_perm: Number of permutations (hash functions)
            seed: Random seed for reproducibility
        """
        self.num_perm = num_perm
        self.seed = seed
        self.hashvalues = [float("inf")] * num_perm

        # Generate permutation parameters
        self.a = []
        self.b = []
        self.c = 4294967311  # Large prime

        # Use deterministic random for reproducibility
        import random

        rng = random.Random(seed)
        for _ in range(num_perm):
            self.a.append(rng.randint(1, self.c - 1))
            self.b.append(rng.randint(0, self.c - 1))

    def update(self, token: str):
        """Update MinHash with a token."""
        token_hash = struct.unpack("<I", hashlib.sha256(token.encode()).digest()[:4])[0]

        for i in range(self.num_perm):
            # Hash function: (a * x + b) % c
            hash_val = (self.a[i] * token_hash + self.b[i]) % self.c
            if hash_val < self.hashvalues[i]:
                self.hashvalues[i] = hash_val

    def digest(self) -> bytes:
        """Get MinHash signature as bytes."""
        # Pack hash values as bytes for compact representation
        return struct.pack(f"{self.num_perm}I", *self.hashvalues)

    def jaccard(self, other: "MinHash") -> float:
        """Estimate Jaccard similarity with another MinHash."""
        if self.num_perm != other.num_perm:
            raise ValueError("MinHash objects must have same num_perm")

        matches = sum(
            1 for i in range(self.num_perm) if self.hashvalues[i] == other.hashvalues[i]
        )
        return matches / self.num_perm


class Fingerprinter:
    """Generate fingerprints for files: SHA256, MinHash, perceptual hash."""

    def __init__(self, snippet_size: int = 1024):
        """
        Initialize fingerprinter.

        Args:
            snippet_size: Max size of snippet to extract (bytes)
        """
        self.snippet_size = snippet_size

        # Text file extensions
        self.text_extensions = {
            ".txt",
            ".md",
            ".rst",
            ".tex",
            ".log",
            ".py",
            ".js",
            ".ts",
            ".jsx",
            ".tsx",
            ".java",
            ".c",
            ".cpp",
            ".h",
            ".go",
            ".rs",
            ".rb",
            ".php",
            ".swift",
            ".kt",
            ".scala",
            ".html",
            ".xml",
            ".json",
            ".yaml",
            ".yml",
            ".toml",
            ".ini",
            ".cfg",
            ".csv",
            ".tsv",
            ".sql",
            ".sh",
            ".bash",
            ".zsh",
            ".fish",
            ".r",
            ".m",
            ".jl",
            ".lua",
            ".pl",
            ".pm",
        }

        # Image extensions
        self.image_extensions = {
            ".jpg",
            ".jpeg",
            ".png",
            ".gif",
            ".bmp",
            ".webp",
            ".ico",
        }

    def fingerprint(self, file_path: Path) -> Dict[str, Any]:
        """
        Generate fingerprints for a file.

        Args:
            file_path: Path to file

        Returns:
            Dict with sha256, minhash, phash, snippet
        """
        result = {
            "path": str(file_path),
            "size": 0,
            "sha256": None,
            "minhash": None,
            "phash": None,
            "snippet": None,
            "error": None,
        }

        try:
            if not file_path.exists():
                result["error"] = "File not found"
                return result

            result["size"] = file_path.stat().st_size

            # SHA256 hash
            result["sha256"] = self._compute_sha256(file_path)

            # Check file type
            ext = file_path.suffix.lower()

            if ext in self.text_extensions or self._is_text_file(file_path):
                # Text file: compute MinHash and extract snippet
                content = self._read_text_file(file_path)
                if content:
                    result["minhash"] = self._compute_minhash(content)
                    result["snippet"] = self._extract_snippet(content)

            elif ext in self.image_extensions and HAS_IMAGE_SUPPORT:
                # Image file: compute perceptual hash
                result["phash"] = self._compute_phash(file_path)
                result["snippet"] = f"[Image: {ext} format, {result['size']} bytes]"

            else:
                # Binary or unknown: just SHA256
                result["snippet"] = (
                    f"[Binary: {ext or 'unknown'} format, {result['size']} bytes]"
                )

        except Exception as e:
            logger.warning(f"Error fingerprinting {file_path}: {e}")
            result["error"] = str(e)

        return result

    def _compute_sha256(self, file_path: Path) -> str:
        """Compute SHA256 hash of file."""
        sha256 = hashlib.sha256()
        try:
            with open(file_path, "rb") as f:
                # Read in chunks for large files
                for chunk in iter(lambda: f.read(8192), b""):
                    sha256.update(chunk)
            return sha256.hexdigest()
        except Exception as e:
            logger.error(f"Error computing SHA256 for {file_path}: {e}")
            return None

    def _is_text_file(self, file_path: Path, sample_size: int = 8192) -> bool:
        """
        Heuristic check if file is text.
        Checks for null bytes and high proportion of printable chars.
        """
        try:
            with open(file_path, "rb") as f:
                sample = f.read(sample_size)

            # Check for null bytes (binary indicator)
            if b"\x00" in sample:
                return False

            # Check proportion of printable ASCII
            try:
                text = sample.decode("utf-8", errors="ignore")
                printable = sum(1 for c in text if c.isprintable() or c.isspace())
                return (printable / len(text)) > 0.85 if text else False
            except:
                return False

        except Exception:
            return False

    def _read_text_file(
        self, file_path: Path, max_size: int = 1048576
    ) -> Optional[str]:
        """
        Read text file content (up to max_size).

        Args:
            file_path: Path to text file
            max_size: Maximum bytes to read (1MB default)

        Returns:
            File content as string or None
        """
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read(max_size)
            return content
        except Exception as e:
            logger.debug(f"Error reading text file {file_path}: {e}")
            return None

    def _compute_minhash(self, text: str) -> str:
        """
        Compute MinHash for text using 5-gram shingles.

        Args:
            text: Text content

        Returns:
            Hex string of MinHash signature
        """
        # Generate 5-gram shingles
        shingles = self._generate_shingles(text, n=5)

        if not shingles:
            return None

        # Compute MinHash
        mh = MinHash(num_perm=128)
        for shingle in shingles:
            mh.update(shingle)

        # Return as hex string
        return mh.digest().hex()

    def _generate_shingles(self, text: str, n: int = 5) -> Set[str]:
        """
        Generate n-gram shingles from text.

        Args:
            text: Input text
            n: Size of n-grams

        Returns:
            Set of shingles
        """
        # Normalize: lowercase, remove extra whitespace
        text = re.sub(r"\s+", " ", text.lower().strip())

        if len(text) < n:
            return {text} if text else set()

        shingles = set()
        for i in range(len(text) - n + 1):
            shingle = text[i : i + n]
            shingles.add(shingle)

        return shingles

    def _compute_phash(self, file_path: Path) -> Optional[str]:
        """
        Compute perceptual hash for image.

        Args:
            file_path: Path to image file

        Returns:
            Hex string of perceptual hash or None
        """
        if not HAS_IMAGE_SUPPORT:
            return None

        try:
            img = Image.open(file_path)
            # Convert to RGB if necessary
            if img.mode not in ("RGB", "L"):
                img = img.convert("RGB")

            # Compute perceptual hash
            phash = imagehash.phash(img)
            return str(phash)

        except Exception as e:
            logger.debug(f"Error computing phash for {file_path}: {e}")
            return None

    def _extract_snippet(self, text: str) -> str:
        """
        Extract clean ASCII snippet from text.

        Args:
            text: Full text content

        Returns:
            Clean snippet (≤1KB)
        """
        if not text:
            return "[Empty file]"

        # Take first snippet_size characters
        snippet = text[: self.snippet_size]

        # Clean up: remove non-ASCII, normalize whitespace
        snippet = re.sub(r"[^\x20-\x7E\n\r\t]", " ", snippet)
        snippet = re.sub(r"[ \t]+", " ", snippet)
        snippet = re.sub(r"\n{3,}", "\n\n", snippet)

        # Trim to last complete line if truncated
        if len(text) > self.snippet_size and "\n" in snippet:
            last_newline = snippet.rfind("\n")
            if last_newline > self.snippet_size * 0.8:  # Keep at least 80%
                snippet = snippet[:last_newline]

        # Add truncation marker if needed
        if len(text) > self.snippet_size:
            snippet += "\n[... truncated]"

        return snippet.strip() or "[Empty content]"
