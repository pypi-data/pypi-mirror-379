"""
Cloud API module for IP-protected SDS generation.
All intelligence stays server-side. No raw content leaves the user's environment.
"""

from .api import (
    AuthError,
    LaceCloudAPI,
    LaceCloudError,
    NetworkError,
    NoAPIKeyError,
    PaymentRequiredError,
    RateLimitError,
    ServerError,
    ValidationError,
)

__all__ = [
    "LaceCloudAPI",
    "LaceCloudError",
    "NoAPIKeyError",
    "NetworkError",
    "AuthError",
    "ValidationError",
    "ServerError",
    "PaymentRequiredError",
    "RateLimitError",
]
