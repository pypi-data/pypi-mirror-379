"""
SDS (Sufficiently Detailed Summary) generation for EU AI Act compliance.
"""

from .questions import SDS_QUESTIONS, get_required_questions, validate_answer
from .scanner import SDSScanner

__all__ = ["SDSScanner", "SDS_QUESTIONS", "get_required_questions", "validate_answer"]
