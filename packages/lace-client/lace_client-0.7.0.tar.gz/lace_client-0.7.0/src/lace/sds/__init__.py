"""
SDS (Sufficiently Detailed Summary) generation for EU AI Act compliance.
"""

from .scanner import SDSScanner
from .questions import SDS_QUESTIONS, get_required_questions, validate_answer

__all__ = [
    'SDSScanner',
    'SDS_QUESTIONS',
    'get_required_questions',
    'validate_answer'
]