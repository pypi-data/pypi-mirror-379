"""
Utility functions for Lace client.
"""

import re
from typing import Any
from urllib.parse import urlparse


def redact_sensitive(text: str) -> str:
    """
    Redact sensitive information from text.
    
    Redacts:
    - UUID-like tokens
    - Query strings in URLs
    - AWS signatures (Signature=, X-Amz-)
    - Stripe keys (sk_)
    - Session tokens
    - Presigned URLs
    """
    if not text:
        return text
    
    # Redact UUIDs and similar tokens (36 chars with dashes)
    text = re.sub(
        r'\b[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\b',
        '<REDACTED-UUID>',
        text,
        flags=re.IGNORECASE
    )
    
    # Redact long tokens (24+ alphanumeric/underscore/dash)
    text = re.sub(
        r'\b[a-zA-Z0-9_-]{24,}\b',
        '<REDACTED-TOKEN>',
        text
    )
    
    # Redact AWS signatures
    text = re.sub(
        r'Signature=[^&\s]+',
        'Signature=<REDACTED>',
        text
    )
    text = re.sub(
        r'X-Amz-[^:=\s]+=?[^&\s]*',
        'X-Amz-<REDACTED>',
        text
    )
    
    # Redact Stripe keys
    text = re.sub(
        r'sk_[a-zA-Z0-9_]+',
        'sk_<REDACTED>',
        text
    )
    
    # Redact PyPI tokens
    text = re.sub(
        r'pypi-[a-zA-Z0-9_-]+',
        'pypi-<REDACTED>',
        text
    )
    
    # Redact query strings in URLs (keep domain)
    def redact_url(match):
        url = match.group(0)
        parsed = urlparse(url)
        if parsed.query:
            return f"{parsed.scheme}://{parsed.netloc}{parsed.path}?<REDACTED>"
        return url
    
    text = re.sub(
        r'https?://[^\s]+\?[^\s]+',
        redact_url,
        text
    )
    
    # Redact session IDs
    text = re.sub(
        r'session[_-]?id["\']?\s*[:=]\s*["\']?([^"\'\s,}]+)',
        'session_id=<REDACTED>',
        text,
        flags=re.IGNORECASE
    )
    
    # Redact API keys
    text = re.sub(
        r'(api[_-]?key|x-api-key)["\']?\s*[:=]\s*["\']?([^"\'\s,}]+)',
        r'\1=<REDACTED>',
        text,
        flags=re.IGNORECASE
    )
    
    return text


def extract_domain(url: str) -> str:
    """Extract domain from URL for safe display."""
    try:
        parsed = urlparse(url)
        return parsed.netloc or "unknown"
    except Exception:
        return "unknown"