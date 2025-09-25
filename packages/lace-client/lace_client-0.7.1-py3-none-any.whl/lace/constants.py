"""
Lace constants and configuration.
"""

import uuid
from typing import Final

# API Version
X_LACE_API_VERSION: Final[str] = "v2025-08-21"

# Client identification
CLIENT_RUN_ID: Final[str] = str(uuid.uuid4())

# Timeouts (seconds)
CONNECT_TIMEOUT: Final[int] = 15
READ_TIMEOUT: Final[int] = 60
WRITE_TIMEOUT: Final[int] = 30
POOL_TIMEOUT: Final[int] = 10

# Retry configuration
MAX_RETRIES: Final[int] = 2
RETRY_BACKOFF_BASE: Final[float] = 2.0
RETRY_BACKOFF_JITTER: Final[tuple[float, float]] = (2.3, 3.1)

# Polling defaults
DEFAULT_MAX_WAIT: Final[int] = 300  # 5 minutes
DEFAULT_POLL_INTERVAL: Final[float] = 2.7

# Exit codes
EXIT_SUCCESS: Final[int] = 0
EXIT_VALIDATION_ERROR: Final[int] = 2
EXIT_PAYMENT_REQUIRED: Final[int] = 3
EXIT_SERVER_ERROR: Final[int] = 4
EXIT_NETWORK_ERROR: Final[int] = 5
EXIT_POLICY_VIOLATION: Final[int] = 6
EXIT_VERIFY_FAILED: Final[int] = 7
EXIT_GENERAL_ERROR: Final[int] = 1
EXIT_EXPERIMENTAL_REQUIRED: Final[int] = 2  # Same as validation error

# Feature flags
PREFLIGHT_EXPERIMENTAL: Final[bool] = True

# Upload performance settings
DEFAULT_UPLOAD_CONCURRENCY: Final[int] = 16
DEFAULT_CHUNK_SIZE_MB: Final[int] = 32
DEFAULT_MAX_FILES: Final[int] = 10000

# File filtering defaults
DEFAULT_INCLUDE_EXTS: Final[list] = ['.parquet', '.jsonl', '.json', '.csv', '.txt', '.md', '.pdf']
DEFAULT_EXCLUDE_GLOBS: Final[list] = ['.git/**', '__pycache__/**', 'node_modules/**', '.DS_Store', '*.pyc']

# Default answers for --defaults flag
SAFE_DEFAULTS: Final[dict] = {
    "provider_status": "provider",
    "offered_in_eu_market": False,
    "confirm_license": True,
    "open_source_release": False,
    "fine_tuning": False,
    "synthetic_data": False,
}