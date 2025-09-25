"""
PII redaction for safe snippet transmission.
Deterministically removes sensitive information while preserving attribution signals.
"""

import re
import hashlib
from typing import Union, Optional
from urllib.parse import urlparse, urlunparse
import logging

logger = logging.getLogger(__name__)


class Redactor:
    """Redact PII and sensitive information from text snippets."""
    
    def __init__(self):
        """Initialize redactor with patterns."""
        # Email pattern
        self.email_pattern = re.compile(
            r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        )
        
        # Phone patterns (various formats)
        self.phone_patterns = [
            re.compile(r'\b\d{3}[-.\s]?\d{3}[-.\s]?\d{4}\b'),  # US format
            re.compile(r'\b\+?\d{1,3}[-.\s]?\(?\d{1,4}\)?[-.\s]?\d{1,4}[-.\s]?\d{1,9}\b'),  # International
            re.compile(r'\b\(\d{3}\)\s?\d{3}-\d{4}\b'),  # (xxx) xxx-xxxx
        ]
        
        # API key patterns
        self.api_key_patterns = [
            re.compile(r'\b(sk|pk|api[_-]?key|token|secret)[_-]?[A-Za-z0-9]{20,}\b', re.IGNORECASE),
            re.compile(r'\b[A-Za-z0-9]{32,}\b'),  # Long hex strings (potential keys)
            re.compile(r'Bearer\s+[A-Za-z0-9\-._~+/]+=*', re.IGNORECASE),  # Bearer tokens
        ]
        
        # File path patterns
        self.filepath_patterns = [
            re.compile(r'[/\\](?:Users|home|var|etc|opt|usr|tmp)[/\\][^\s]+'),  # Unix paths
            re.compile(r'[A-Z]:\\[^\s]+'),  # Windows paths
            re.compile(r'\\\\[^\s]+'),  # UNC paths
        ]
        
        # Credit card pattern (basic)
        self.credit_card_pattern = re.compile(
            r'\b(?:\d{4}[-\s]?){3}\d{4}\b'
        )
        
        # SSN pattern
        self.ssn_pattern = re.compile(
            r'\b\d{3}-\d{2}-\d{4}\b'
        )
        
        # IP address patterns
        self.ip_patterns = [
            re.compile(r'\b(?:\d{1,3}\.){3}\d{1,3}\b'),  # IPv4
            re.compile(r'\b(?:[A-Fa-f0-9]{1,4}:){7}[A-Fa-f0-9]{1,4}\b'),  # IPv6
        ]
    
    def redact_urls(self, text: str) -> str:
        """
        Strip query parameters and fragments from URLs.
        
        Args:
            text: Text containing URLs
            
        Returns:
            Text with cleaned URLs
        """
        # Pattern to match URLs
        url_pattern = re.compile(
            r'https?://[^\s<>"{}|\\^`\[\]]+',
            re.IGNORECASE
        )
        
        def clean_url(match):
            url = match.group(0)
            try:
                parsed = urlparse(url)
                # Keep only scheme, netloc, and path
                cleaned = urlunparse((
                    parsed.scheme,
                    parsed.netloc,
                    parsed.path,
                    '',  # params
                    '',  # query
                    ''   # fragment
                ))
                return cleaned.rstrip('/')
            except Exception:
                # If parsing fails, return domain only
                return re.sub(r'(https?://[^/]+).*', r'\1', url)
        
        return url_pattern.sub(clean_url, text)
    
    def redact_snippet(self, text: Union[str, bytes]) -> str:
        """
        Redact PII and sensitive information from text.
        
        Args:
            text: Text to redact (str or bytes)
            
        Returns:
            Redacted text (≤1024 bytes UTF-8)
        """
        # Convert bytes to string if needed
        if isinstance(text, bytes):
            try:
                text = text.decode('utf-8', errors='ignore')
            except Exception:
                # Fallback to latin-1
                text = text.decode('latin-1', errors='ignore')
        
        # Log SHA256 of original (never log the content itself)
        original_hash = hashlib.sha256(text.encode('utf-8', errors='ignore')).hexdigest()
        logger.debug(f"Redacting snippet with SHA256: {original_hash}")
        
        # Apply redactions in order of priority
        
        # 1. Redact emails
        text = self.email_pattern.sub('[EMAIL]', text)
        
        # 2. Redact phone numbers
        for pattern in self.phone_patterns:
            text = pattern.sub('[PHONE]', text)
        
        # 3. Redact API keys and tokens
        for pattern in self.api_key_patterns:
            text = pattern.sub('[KEY]', text)
        
        # 4. Redact file paths
        for pattern in self.filepath_patterns:
            text = pattern.sub('[PATH]', text)
        
        # 5. Redact credit cards
        text = self.credit_card_pattern.sub('[CC]', text)
        
        # 6. Redact SSNs
        text = self.ssn_pattern.sub('[SSN]', text)
        
        # 7. Redact IP addresses
        for pattern in self.ip_patterns:
            text = pattern.sub('[IP]', text)
        
        # 8. Clean URLs (remove query params)
        text = self.redact_urls(text)
        
        # 9. Normalize whitespace
        text = ' '.join(text.split())
        
        # 10. Ensure ≤1024 bytes
        text = self.budgeted(text, 1024)
        
        return text
    
    def budgeted(self, text: str, limit: int = 1024) -> str:
        """
        Truncate text to fit within byte limit.
        
        Args:
            text: Text to truncate
            limit: Maximum bytes (default 1024)
            
        Returns:
            Truncated text that fits in limit
        """
        # Quick check
        if len(text.encode('utf-8')) <= limit:
            return text
        
        # Binary search for the right truncation point
        left, right = 0, len(text)
        result = ""
        
        while left <= right:
            mid = (left + right) // 2
            truncated = text[:mid]
            
            # Check byte length
            if len(truncated.encode('utf-8')) <= limit:
                result = truncated
                left = mid + 1
            else:
                right = mid - 1
        
        # Try to truncate at a word boundary
        if result and len(result) > 50:
            # Look for last space in final 20 chars
            last_space = result.rfind(' ', len(result) - 20)
            if last_space > len(result) - 50:
                result = result[:last_space]
        
        # Add ellipsis if truncated
        if len(result) < len(text):
            # Make sure ellipsis fits
            while len((result + '...').encode('utf-8')) > limit and result:
                result = result[:-1]
            result += '...'
        
        return result
    
    def extract_safe_metadata(self, text: str) -> dict:
        """
        Extract safe metadata without including PII.
        
        Args:
            text: Original text
            
        Returns:
            Safe metadata dict
        """
        # Only return hashes and counts, never content
        return {
            'sha256': hashlib.sha256(text.encode('utf-8', errors='ignore')).hexdigest(),
            'original_bytes': len(text.encode('utf-8', errors='ignore')),
            'has_urls': bool(re.search(r'https?://', text, re.IGNORECASE)),
            'has_email_pattern': bool(self.email_pattern.search(text)),
            'has_phone_pattern': any(p.search(text) for p in self.phone_patterns),
            'language_hint': self._detect_language_hint(text)
        }
    
    def _detect_language_hint(self, text: str) -> Optional[str]:
        """
        Detect language hint from text patterns.
        
        Args:
            text: Text to analyze
            
        Returns:
            Language code or None
        """
        # Simple heuristic based on character ranges
        # This is a very basic implementation
        
        # Check for CJK characters
        if re.search(r'[\u4e00-\u9fff]', text):
            return 'zh'  # Chinese
        if re.search(r'[\u3040-\u309f\u30a0-\u30ff]', text):
            return 'ja'  # Japanese
        if re.search(r'[\uac00-\ud7af]', text):
            return 'ko'  # Korean
        
        # Check for Arabic
        if re.search(r'[\u0600-\u06ff]', text):
            return 'ar'
        
        # Check for Cyrillic
        if re.search(r'[\u0400-\u04ff]', text):
            return 'ru'  # Could be other Cyrillic languages
        
        # Default to English for Latin script
        if re.search(r'[a-zA-Z]', text):
            return 'en'
        
        return None


# Convenience functions
_redactor = None

def get_redactor() -> Redactor:
    """Get or create global redactor instance."""
    global _redactor
    if _redactor is None:
        _redactor = Redactor()
    return _redactor


def redact_snippet(text: Union[str, bytes]) -> str:
    """
    Convenience function to redact a snippet.
    
    Args:
        text: Text to redact
        
    Returns:
        Redacted text (≤1024 bytes)
    """
    return get_redactor().redact_snippet(text)


def budgeted(text: str, limit: int = 1024) -> str:
    """
    Convenience function to truncate text to byte limit.
    
    Args:
        text: Text to truncate
        limit: Byte limit
        
    Returns:
        Truncated text
    """
    return get_redactor().budgeted(text, limit)