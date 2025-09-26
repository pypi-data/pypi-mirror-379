"""
Lace Preflight - Pre-training gate for AI compliance.
Fast opt-out/license/PII checks before you waste compute.
"""

from .orchestrator import PreflightConfig, preflight_check
from .registry import Registry, RegistryManager
from .scanner import DatasetScanner
from .verdict import PreflightVerdict, VerdictEngine

__all__ = [
    "preflight_check",
    "PreflightConfig",
    "Registry",
    "RegistryManager",
    "DatasetScanner",
    "VerdictEngine",
    "PreflightVerdict",
]

__version__ = "0.7.0"
