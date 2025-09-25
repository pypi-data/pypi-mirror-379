"""
Registry management for opt-out domains and rules.
"""

import json
import sqlite3
import hashlib
import struct
import tarfile
import tempfile
import shutil
from pathlib import Path
from typing import Dict, Any, List, Optional, Set, Tuple
from datetime import datetime
import base64

import httpx

from ..utils import redact_sensitive

import logging
logger = logging.getLogger(__name__)


class BloomFilter:
    """Simple Bloom filter for domain membership testing."""
    
    def __init__(self, m: int = 1048576, k: int = 7):
        """
        Initialize Bloom filter.
        
        Args:
            m: Number of bits (default 1MB = 8M bits)
            k: Number of hash functions (default 7 for ~1% FPR with 1M items)
        """
        self.m = m
        self.k = k
        self.bits = bytearray(m)
        
    def _hash(self, item: str, seed: int) -> int:
        """Generate hash for item with seed."""
        h = hashlib.sha256(f"{seed}:{item}".encode()).digest()
        return struct.unpack('>I', h[:4])[0] % (self.m * 8)
    
    def add(self, item: str):
        """Add item to filter."""
        for i in range(self.k):
            bit_pos = self._hash(item, i)
            byte_pos = bit_pos // 8
            bit_offset = bit_pos % 8
            self.bits[byte_pos] |= (1 << bit_offset)
    
    def contains(self, item: str) -> bool:
        """Check if item might be in filter (can have false positives)."""
        for i in range(self.k):
            bit_pos = self._hash(item, i)
            byte_pos = bit_pos // 8
            bit_offset = bit_pos % 8
            if not (self.bits[byte_pos] & (1 << bit_offset)):
                return False
        return True
    
    def save(self, path: Path):
        """Save filter to file."""
        with open(path, 'wb') as f:
            # Write header: version, m, k
            f.write(struct.pack('>III', 1, self.m, self.k))
            f.write(self.bits)
    
    @classmethod
    def load(cls, path: Path) -> 'BloomFilter':
        """Load filter from file."""
        with open(path, 'rb') as f:
            version, m, k = struct.unpack('>III', f.read(12))
            if version != 1:
                raise ValueError(f"Unsupported Bloom filter version: {version}")
            bf = cls(m, k)
            bf.bits = bytearray(f.read())
            return bf


class Registry:
    """Opt-out registry with Bloom filter + SQLite evidence."""
    
    def __init__(self, path: Optional[Path] = None):
        """Initialize registry."""
        self.path = path or Path.home() / '.lace' / 'registry'
        self.path.mkdir(parents=True, exist_ok=True)
        
        self.bloom: Optional[BloomFilter] = None
        self.conn: Optional[sqlite3.Connection] = None
        self.manifest: Dict[str, Any] = {}
        self._loaded = False
        
    def load(self) -> bool:
        """Load registry from disk."""
        manifest_path = self.path / 'manifest.json'
        bloom_path = self.path / 'optout.bloom'
        db_path = self.path / 'optout.sqlite'
        
        if not manifest_path.exists():
            logger.debug("No registry manifest found")
            return False
        
        try:
            # Load manifest
            with open(manifest_path, 'r') as f:
                self.manifest = json.load(f)
            
            # Load Bloom filter
            if bloom_path.exists():
                self.bloom = BloomFilter.load(bloom_path)
            
            # Load SQLite database
            if db_path.exists():
                self.conn = sqlite3.connect(str(db_path))
                self.conn.row_factory = sqlite3.Row
            
            self._loaded = True
            logger.info(f"Loaded registry v{self.manifest.get('version', 'unknown')}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to load registry: {e}")
            return False
    
    def verify_signature(self) -> bool:
        """Verify registry signature if present."""
        if 'signature' not in self.manifest:
            if self.manifest.get('dev_unsigned'):
                logger.warning("🚨 USING UNSIGNED DEV REGISTRY - NOT FOR PRODUCTION 🚨")
                return False
            logger.warning("Registry has no signature")
            return False
        
        # TODO: Implement KMS verification
        # For now, trust if signature field exists
        return True
    
    def check_domain(self, domain: str) -> Optional[Dict[str, Any]]:
        """
        Check if domain is in opt-out registry.
        
        Returns:
            None if not found, dict with evidence if found
        """
        if not self._loaded:
            return None
        
        # Normalize domain to eTLD+1
        domain = self._normalize_domain(domain)
        
        # Quick Bloom filter check
        if self.bloom and not self.bloom.contains(domain):
            return None  # Definitely not in registry
        
        # SQLite lookup for evidence
        if self.conn:
            cursor = self.conn.execute(
                "SELECT * FROM domains WHERE domain = ? AND ttl > ?",
                (domain, datetime.now().timestamp())
            )
            row = cursor.fetchone()
            if row:
                return dict(row)
        
        return None
    
    def _normalize_domain(self, domain: str) -> str:
        """Normalize domain to eTLD+1."""
        # Simple normalization - in production use publicsuffix2
        domain = domain.lower().strip()
        
        # Remove protocol if present
        for proto in ('https://', 'http://', 'ftp://'):
            if domain.startswith(proto):
                domain = domain[len(proto):]
        
        # Remove path
        domain = domain.split('/')[0]
        
        # Remove port
        domain = domain.split(':')[0]
        
        # TODO: Proper eTLD+1 extraction with publicsuffix2
        # For now, just return cleaned domain
        return domain
    
    def add_domain(self, domain: str, source: str, rule: str, evidence_url: str):
        """Add domain to registry (dev mode only)."""
        if not self.manifest.get('dev_unsigned'):
            raise RuntimeError("Cannot modify signed registry")
        
        domain = self._normalize_domain(domain)
        
        # Add to Bloom filter
        if not self.bloom:
            self.bloom = BloomFilter()
        self.bloom.add(domain)
        
        # Add to SQLite
        if not self.conn:
            db_path = self.path / 'optout.sqlite'
            self.conn = sqlite3.connect(str(db_path))
            self._create_tables()
        
        self.conn.execute("""
            INSERT OR REPLACE INTO domains 
            (domain, source, rule, evidence_url, last_seen, ttl)
            VALUES (?, ?, ?, ?, ?, ?)
        """, (
            domain,
            source,
            rule,
            evidence_url,
            datetime.now().timestamp(),
            datetime.now().timestamp() + 86400 * 30  # 30 day TTL
        ))
        self.conn.commit()
    
    def _create_tables(self):
        """Create SQLite tables."""
        self.conn.execute("""
            CREATE TABLE IF NOT EXISTS domains (
                domain TEXT PRIMARY KEY,
                source TEXT,
                rule TEXT,
                evidence_url TEXT,
                last_seen REAL,
                ttl REAL,
                confidence REAL DEFAULT 0.9
            )
        """)
        self.conn.execute("CREATE INDEX IF NOT EXISTS idx_ttl ON domains(ttl)")
        self.conn.commit()
    
    def save(self):
        """Save registry to disk."""
        # Update manifest
        self.manifest['version'] = datetime.now().strftime('%Y%m%d.%H%M')
        self.manifest['created_at'] = datetime.now().isoformat()
        self.manifest['sources'] = ['robots', 'ai.txt', 'dev_manual']
        self.manifest['dev_unsigned'] = True  # Mark as dev
        
        if self.bloom:
            self.manifest['bloom_m'] = self.bloom.m
            self.manifest['bloom_k'] = self.bloom.k
        
        # Save files
        manifest_path = self.path / 'manifest.json'
        with open(manifest_path, 'w') as f:
            json.dump(self.manifest, f, indent=2)
        
        if self.bloom:
            self.bloom.save(self.path / 'optout.bloom')
        
        if self.conn:
            self.conn.commit()


class RegistryManager:
    """Manages registry loading and updates."""
    
    def __init__(self, registry_path: Optional[Path] = None):
        """Initialize registry manager."""
        self.registry_path = registry_path or Path.home() / '.lace' / 'registry'
        self.registry = Registry(self.registry_path)
        self.registry_base = "https://registry.withlace.ai"  # TODO: Move to config
        
    def load(self) -> Dict[str, Any]:
        """Load registry and return info."""
        loaded = self.registry.load()
        verified = False
        
        if loaded:
            verified = self.registry.verify_signature()
        
        return {
            'loaded': loaded,
            'verified': verified,
            'version': self.registry.manifest.get('version', 'unknown'),
            'sources': self.registry.manifest.get('sources', []),
            'dev_unsigned': self.registry.manifest.get('dev_unsigned', False)
        }
    
    def refresh(self, force: bool = False) -> bool:
        """
        Download and install latest registry.
        
        Args:
            force: Force refresh even if current version is recent
            
        Returns:
            True if updated successfully
        """
        try:
            # Check current version
            current_version = self.registry.manifest.get('version', '0')
            
            # Download manifest
            with httpx.Client(timeout=10) as client:
                resp = client.get(f"{self.registry_base}/manifest.json")
                resp.raise_for_status()
                remote_manifest = resp.json()
            
            remote_version = remote_manifest.get('version', '0')
            
            if not force and remote_version <= current_version:
                logger.info(f"Registry up to date (v{current_version})")
                return True
            
            # Download registry bundle
            logger.info(f"Downloading registry v{remote_version}...")
            with httpx.Client(timeout=30) as client:
                resp = client.get(f"{self.registry_base}/registry_{remote_version}.tar.gz")
                resp.raise_for_status()
                bundle_data = resp.content
            
            # Verify signature
            # TODO: Implement KMS verification of bundle
            
            # Extract to temp directory
            with tempfile.TemporaryDirectory() as tmpdir:
                bundle_path = Path(tmpdir) / 'registry.tar.gz'
                bundle_path.write_bytes(bundle_data)
                
                # Extract
                with tarfile.open(bundle_path, 'r:gz') as tar:
                    tar.extractall(tmpdir)
                
                # Atomic swap
                backup_path = self.registry_path.with_suffix('.backup')
                if self.registry_path.exists():
                    shutil.move(str(self.registry_path), str(backup_path))
                
                shutil.move(str(Path(tmpdir) / 'registry'), str(self.registry_path))
                
                # Clean up backup
                if backup_path.exists():
                    shutil.rmtree(backup_path)
            
            logger.info(f"Registry updated to v{remote_version}")
            return True
            
        except Exception as e:
            logger.error(f"Failed to refresh registry: {e}")
            return False
    
    def create_dev_registry(self):
        """Create a development registry for testing."""
        logger.warning("Creating unsigned dev registry...")
        
        # Initialize manifest for dev registry
        self.registry.manifest = {
            'version': 'dev-1.0',
            'dev_unsigned': True,
            'source': 'dev',
            'count': 3,
            'created': datetime.now().isoformat()
        }
        
        # Add some test domains
        test_domains = [
            ('no-ai-training.com', 'robots.txt', 'User-agent: GPTBot\nDisallow: /', 
             'https://no-ai-training.com/robots.txt'),
            ('protect-content.org', 'ai.txt', 'ai-training: no', 
             'https://protect-content.org/ai.txt'),
            ('opt-out-example.com', 'manual', 'Site owner request', 
             'https://opt-out-example.com/legal'),
        ]
        
        for domain, source, rule, evidence in test_domains:
            self.registry.add_domain(domain, source, rule, evidence)
        
        self.registry.save()
        logger.info("Dev registry created")