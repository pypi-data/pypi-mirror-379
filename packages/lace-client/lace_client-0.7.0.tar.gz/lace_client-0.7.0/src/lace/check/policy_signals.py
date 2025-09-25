"""
Policy signals fetcher for robots.txt and header-based opt-out detection.
Fetches and caches robots.txt, ai-robots.txt, and X-Robots-Tag headers.
"""

import json
import hashlib
import re
from pathlib import Path
from typing import Dict, Any, Optional, List, Tuple, Union
from datetime import datetime, timedelta
from urllib.parse import urlparse, urljoin
import logging
import asyncio
from concurrent.futures import ThreadPoolExecutor
import time

try:
    import httpx
    import idna
except ImportError:
    raise ImportError("Please install httpx and idna: pip install httpx idna")

logger = logging.getLogger(__name__)


def _as_int(value: Union[str, int, float, None], default: Optional[int] = None) -> Optional[int]:
    """
    Safely convert value to integer.
    
    Args:
        value: Value to convert (str, int, float, or None)
        default: Default value if conversion fails
        
    Returns:
        Integer value or default
    """
    if value is None:
        return default
    try:
        return int(value)
    except (TypeError, ValueError):
        return default


class PolicySignalsFetcher:
    """Fetch and cache policy signals from robots.txt and headers."""
    
    def __init__(
        self,
        cache_dir: Optional[Path] = None,
        cache_ttl_days: int = 7,
        timeout: float = 10.0,
        max_domain_concurrency: int = 2,
        max_global_concurrency: int = 16
    ):
        """
        Initialize policy signals fetcher.
        
        Args:
            cache_dir: Cache directory (default ~/.lace/cache/policy/)
            cache_ttl_days: Cache TTL in days
            timeout: Request timeout in seconds
            max_domain_concurrency: Max concurrent requests per domain
            max_global_concurrency: Max total concurrent requests
        """
        self.cache_dir = cache_dir or Path.home() / '.lace' / 'cache' / 'policy'
        self.cache_dir.mkdir(parents=True, exist_ok=True)
        
        self.cache_ttl = timedelta(days=cache_ttl_days)
        self.timeout = timeout
        self.max_domain_concurrency = max_domain_concurrency
        self.max_global_concurrency = max_global_concurrency
        
        # Concurrency control
        self.domain_semaphores = {}
        self.global_semaphore = asyncio.Semaphore(max_global_concurrency)
        
        # Known opt-out patterns
        self.optout_patterns = [
            r'\bnoai\b',
            r'\bai:\s*disallow\b',
            r'\bNoAI\b',
            r'\bno-ai\b',
            r'\btext\s+and\s+data\s+mining.*prohibited\b',
            r'\bTDM.*opt.?out\b',
            r'\bDSM.*Article\s+4\b',
            r'\bnoimageai\b',
            r'\bNoIndex:\s*ai\b',
        ]
        
        # User-agent matching patterns
        self.bot_patterns = [
            r'^Lace',
            r'^GPT',
            r'^ChatGPT',
            r'^Claude',
            r'AI.*Bot',
            r'.*[Tt]raining.*[Bb]ot',
        ]
    
    def canonicalize_domain(self, domain: str) -> str:
        """
        Canonicalize domain name.
        
        Args:
            domain: Domain to canonicalize
            
        Returns:
            Canonicalized domain
        """
        # Remove protocol if present
        if '://' in domain:
            domain = urlparse(domain).netloc
        
        # Strip common subdomain prefixes (expanded list)
        for prefix in ['www.', 'm.', 'amp.', 'mobile.', 'wap.']:
            if domain.startswith(prefix):
                domain = domain[len(prefix):]
                break
        
        # Lowercase
        domain = domain.lower()
        
        # Handle IDN/punycode
        try:
            # Convert to ASCII if needed
            domain = idna.encode(domain).decode('ascii')
        except (idna.IDNAError, UnicodeError):
            # Keep as-is if conversion fails
            pass
        
        return domain
    
    def get_cache_path(self, domain: str) -> Path:
        """Get cache file path for domain."""
        canonical = self.canonicalize_domain(domain)
        # Use hash for filename to avoid filesystem issues
        domain_hash = hashlib.sha256(canonical.encode()).hexdigest()[:16]
        return self.cache_dir / f"{domain_hash}_{canonical.replace('/', '_')}.json"
    
    def load_from_cache(self, domain: str) -> Optional[Dict[str, Any]]:
        """
        Load policy signals from cache if valid.
        
        Args:
            domain: Domain to check
            
        Returns:
            Cached signals or None if expired/missing
        """
        cache_path = self.get_cache_path(domain)
        
        if not cache_path.exists():
            return None
        
        try:
            with open(cache_path, 'r') as f:
                cached = json.load(f)
            
            # Check TTL
            checked_at = datetime.fromisoformat(cached['checked_at']) if cached.get('checked_at') else None
            if checked_at:
                age = datetime.utcnow() - checked_at
            else:
                age = self.cache_ttl + timedelta(days=1)  # Force refresh if no timestamp
            
            # Return cache for HTTP freshness checks even if expired
            # The fetch methods will use If-None-Match/If-Modified-Since
            if age <= self.cache_ttl:
                logger.debug(f"Using fresh cache for {domain} (age: {age})")
                return cached
            else:
                logger.debug(f"Cache stale for {domain} (age: {age}), will check freshness")
                # Return stale cache so we can use ETag/Last-Modified
                return cached
        
        except Exception as e:
            logger.warning(f"Failed to load cache for {domain}: {e}")
            return None
    
    def save_to_cache(self, domain: str, signals: Dict[str, Any]):
        """Save policy signals to cache."""
        cache_path = self.get_cache_path(domain)
        
        try:
            with open(cache_path, 'w') as f:
                json.dump(signals, f, indent=2, default=str)
            logger.debug(f"Cached policy for {domain}")
        except Exception as e:
            logger.warning(f"Failed to cache policy for {domain}: {e}")
    
    async def fetch_robots_txt(
        self,
        domain: str,
        path: str = '/robots.txt',
        etag: Optional[str] = None,
        last_modified: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Fetch and parse robots.txt file with HTTP freshness.
        
        Args:
            domain: Domain to fetch from
            path: Path to robots file
            etag: Previous ETag for conditional request
            last_modified: Previous Last-Modified for conditional request
            
        Returns:
            Parsed robots signals
        """
        url = f"https://{domain}{path}"
        headers = {}
        if etag:
            headers['If-None-Match'] = etag
        if last_modified:
            headers['If-Modified-Since'] = last_modified
        
        result = {
            'has_file': False,
            'has_noai': False,
            'disallow': [],
            'allow': [],
            'crawl_delay': None,
            'evidence': [],
            'etag': None,
            'last_modified': None
        }
        
        try:
            async with httpx.AsyncClient(timeout=self.timeout) as client:
                response = await client.get(url, headers=headers, follow_redirects=True)
                
                if response.status_code == 304:
                    # Not modified - cache is still valid
                    result['not_modified'] = True
                    result['has_file'] = True  # We know file exists from cache
                    return result
                
                if response.status_code in [404, 406, 415]:
                    # Treat as "no file" without warning
                    return result
                
                if response.status_code != 200:
                    return result
                
                result['has_file'] = True
                result['etag'] = response.headers.get('etag')
                result['last_modified'] = response.headers.get('last-modified')
                
                content = response.text
                
                # Check for opt-out patterns
                for pattern in self.optout_patterns:
                    if re.search(pattern, content, re.IGNORECASE):
                        result['has_noai'] = True
                        result['evidence'].append(f"{path}: {pattern}")
                        break
                
                # Parse robots directives with regex for better handling
                current_agent = None
                applies_to_us = False
                
                # Regex patterns for robust parsing
                user_agent_pattern = re.compile(r'^\s*user-agent\s*:\s*(.+)$', re.IGNORECASE)
                disallow_pattern = re.compile(r'^\s*disallow\s*:\s*(.*)$', re.IGNORECASE)
                allow_pattern = re.compile(r'^\s*allow\s*:\s*(.*)$', re.IGNORECASE)
                crawl_delay_pattern = re.compile(r'^\s*crawl-delay\s*:\s*(.+)$', re.IGNORECASE)
                
                for line in content.split('\n'):
                    # Keep original line for processing, don't strip yet
                    # This handles lines with tabs and multiple spaces better
                    
                    # Skip comments and empty lines
                    if not line.strip() or line.strip().startswith('#'):
                        continue
                    
                    # User-agent line
                    ua_match = user_agent_pattern.match(line)
                    if ua_match:
                        agent = ua_match.group(1).strip()
                        current_agent = agent
                        
                        # Check if this section applies to us
                        if agent == '*':
                            applies_to_us = True
                        else:
                            for pattern in self.bot_patterns:
                                if re.match(pattern, agent, re.IGNORECASE):
                                    applies_to_us = True
                                    break
                            else:
                                applies_to_us = False  # Reset if not matching
                    
                    # Only parse directives that apply to us
                    elif applies_to_us:
                        disallow_match = disallow_pattern.match(line)
                        allow_match = allow_pattern.match(line)
                        crawl_match = crawl_delay_pattern.match(line)
                        
                        if disallow_match:
                            path = disallow_match.group(1).strip()
                            if path:
                                result['disallow'].append(path)
                                if path == '/':
                                    result['evidence'].append(f"{path}: Disallow all")
                        
                        elif allow_match:
                            path = allow_match.group(1).strip()
                            if path:
                                result['allow'].append(path)
                        
                        elif crawl_match:
                            try:
                                delay = float(crawl_match.group(1).strip())
                                result['crawl_delay'] = delay
                                if delay > 10:
                                    result['evidence'].append(f"High crawl-delay: {delay}s")
                            except ValueError:
                                pass
        
        except httpx.TimeoutException:
            result['timeout'] = True
            logger.debug(f"Timeout fetching {url}")
        except Exception as e:
            result['error'] = str(e)
            logger.debug(f"Error fetching {url}: {e}")
        
        return result
    
    async def fetch_headers(self, domain: str) -> Dict[str, Any]:
        """
        Fetch X-Robots-Tag and other headers.
        
        Args:
            domain: Domain to check
            
        Returns:
            Header signals
        """
        result = {
            'x_robots': {'all': []},
            'evidence': []
        }
        
        # Try multiple paths to get representative headers
        paths = ['/', '/ai.txt', '/robots.txt']
        
        for path in paths:
            url = f"https://{domain}{path}"
            
            try:
                async with httpx.AsyncClient(timeout=self.timeout) as client:
                    response = await client.head(url, follow_redirects=True)
                    
                    # Record canonical domain if redirected
                    if response.history:
                        final_url = str(response.url)
                        final_domain = urlparse(final_url).netloc
                        if final_domain != domain:
                            result['canonical_domain'] = self.canonicalize_domain(final_domain)
                    
                    # Check X-Robots-Tag
                    x_robots = response.headers.get('X-Robots-Tag', '')
                    if x_robots:
                        tags = [t.strip() for t in x_robots.split(',')]
                        result['x_robots']['all'].extend(tags)
                        
                        # Check for opt-out signals
                        for tag in tags:
                            if any(pattern in tag.lower() for pattern in ['noai', 'noindex']):
                                result['evidence'].append(f"X-Robots-Tag: {tag}")
                    
                    # Only need one successful response
                    if response.status_code < 400:
                        break
            
            except Exception as e:
                logger.debug(f"Failed to fetch headers from {url}: {e}")
                continue
        
        # Deduplicate
        result['x_robots']['all'] = list(set(result['x_robots']['all']))
        
        return result
    
    async def fetch_domain_policy(self, domain: str) -> Dict[str, Any]:
        """
        Fetch all policy signals for a domain with HTTP freshness checks.
        
        Args:
            domain: Domain to check
            
        Returns:
            Combined policy signals
        """
        canonical = self.canonicalize_domain(domain)
        
        # Check cache first
        cached = self.load_from_cache(canonical)
        
        # If cache is fresh and not unreachable, use it
        if cached and not cached.get('unreachable'):
            checked_at = datetime.fromisoformat(cached['checked_at']) if cached.get('checked_at') else None
            if checked_at:
                age = datetime.utcnow() - checked_at
                if age <= self.cache_ttl:
                    return cached
        
        # Get previous ETag and Last-Modified for freshness checks
        prev_etag = cached.get('etag') if cached else None
        prev_last_modified = cached.get('last_modified') if cached else None
        
        # Ensure domain semaphore exists
        if canonical not in self.domain_semaphores:
            self.domain_semaphores[canonical] = asyncio.Semaphore(self.max_domain_concurrency)
        
        # Fetch with rate limiting
        async with self.global_semaphore:
            async with self.domain_semaphores[canonical]:
                # Fetch robots.txt with freshness headers
                robots = await self.fetch_robots_txt(
                    canonical, '/robots.txt', 
                    prev_etag, prev_last_modified
                )
                
                # If not modified and we have valid cache, update timestamp and return
                if robots.get('not_modified') and cached:
                    # Update cache timestamp to extend TTL
                    cached['checked_at'] = datetime.utcnow().isoformat()
                    self.save_to_cache(canonical, cached)
                    return cached
                
                # Fetch ai-robots.txt (no conditional request as less common)
                ai_robots = await self.fetch_robots_txt(canonical, '/ai-robots.txt')
                
                # Fetch headers
                headers = await self.fetch_headers(canonical)
        
        # Combine signals
        result = {
            'domain': canonical,
            'checked_at': datetime.utcnow().isoformat(),
            'etag': robots.get('etag'),
            'last_modified': robots.get('last_modified'),
            'x_robots': headers.get('x_robots', {}),
            'robots_txt': {
                'has_noai': robots.get('has_noai', False),
                'disallow': robots.get('disallow', []),
                'crawl_delay': robots.get('crawl_delay')
            },
            'ai_robots_txt': {
                'has_noai': ai_robots.get('has_noai', False)
            },
            'optout_strength': 0.0,
            'evidence': []
        }
        
        # Collect all evidence
        result['evidence'].extend(robots.get('evidence', []))
        result['evidence'].extend(ai_robots.get('evidence', []))
        result['evidence'].extend(headers.get('evidence', []))
        
        # Calculate opt-out strength
        strength = 0.0
        
        if robots.get('has_noai') or ai_robots.get('has_noai'):
            strength = max(strength, 0.9)
        
        if any('noai' in tag.lower() for tag in result['x_robots'].get('all', [])):
            strength = max(strength, 0.85)
        
        if '/' in robots.get('disallow', []):
            strength = max(strength, 0.8)
        
        crawl_delay = _as_int(robots.get('crawl_delay'), 0)
        if crawl_delay and crawl_delay > 10:
            strength = max(strength, 0.6)
        
        result['optout_strength'] = strength
        
        # Mark as unreachable if we couldn't fetch anything
        if not robots.get('has_file') and not headers.get('x_robots', {}).get('all'):
            result['unreachable'] = True
            result['optout_strength'] = 0.0
        
        # Save to cache
        self.save_to_cache(canonical, result)
        
        return result
    
    def fetch_batch(
        self,
        domains: List[str],
        progress_callback: Optional[callable] = None
    ) -> Dict[str, Dict[str, Any]]:
        """
        Fetch policy signals for multiple domains.
        
        Args:
            domains: List of domains to check
            progress_callback: Optional callback for progress updates
            
        Returns:
            Dict mapping domain to policy signals
        """
        # Deduplicate and canonicalize
        unique_domains = list(set(self.canonicalize_domain(d) for d in domains))
        
        async def fetch_all():
            results = {}
            tasks = []
            
            for i, domain in enumerate(unique_domains):
                task = self.fetch_domain_policy(domain)
                tasks.append(task)
                
                if progress_callback and i % 10 == 0:
                    progress_callback(i, len(unique_domains))
            
            # Gather results
            responses = await asyncio.gather(*tasks, return_exceptions=True)
            
            for domain, response in zip(unique_domains, responses):
                if isinstance(response, Exception):
                    logger.warning(f"Failed to fetch policy for {domain}: {response}")
                    results[domain] = {
                        'domain': domain,
                        'unreachable': True,
                        'optout_strength': 0.0,
                        'evidence': [],
                        'error': str(response)
                    }
                else:
                    results[domain] = response
            
            return results
        
        # Run async fetch
        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
        
        return loop.run_until_complete(fetch_all())