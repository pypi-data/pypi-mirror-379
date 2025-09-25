"""
Lace Check - Opt-out and copyright detection for training data.
Offline-first design with optional online enhancement.
"""

from .sampler import DataSampler
from .fingerprint import Fingerprinter
from .attribution import AttributionEngine
from .classifier import StatusClassifier
from .report import ReportGenerator
from .tui_review import ReviewInterface

__all__ = [
    'DataSampler',
    'Fingerprinter',
    'AttributionEngine',
    'StatusClassifier',
    'ReportGenerator',
    'ReviewInterface',
]

__version__ = '0.1.0'