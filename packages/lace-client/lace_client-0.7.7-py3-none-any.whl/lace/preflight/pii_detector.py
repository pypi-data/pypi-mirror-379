"""
PII detection with deterministic sampling.
"""

import hashlib
import logging
import re
from pathlib import Path
from typing import Any, Dict, List

logger = logging.getLogger(__name__)


class PIIDetector:
    """Detects PII signals in text files."""

    # Regex patterns for common PII
    PATTERNS = {
        "email": re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b"),
        "phone": re.compile(
            r"\b(?:\+?1[-.]?)?\(?[0-9]{3}\)?[-.]?[0-9]{3}[-.]?[0-9]{4}\b"
        ),
        "ssn": re.compile(
            r"\b(?!000|666|9\d{2})\d{3}[-]?(?!00)\d{2}[-]?(?!0000)\d{4}\b"
        ),
        "credit_card": re.compile(
            r"\b(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|6(?:011|5[0-9]{2})[0-9]{12})\b"
        ),
        "ip_address": re.compile(
            r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\b"
        ),
    }

    def __init__(self, mode: str = "light"):
        """
        Initialize PII detector.

        Args:
            mode: 'off', 'light' (regex only), or 'standard' (with NER if available)
        """
        self.mode = mode
        self.has_presidio = False

        if mode == "standard":
            try:
                import presidio_analyzer

                self.has_presidio = True
                self.analyzer = presidio_analyzer.AnalyzerEngine()
                logger.debug("Presidio available for standard PII detection")
            except ImportError:
                logger.debug("Presidio not available, falling back to light mode")
                self.mode = "light"

    def scan_files(self, files: List[Path], time_budget: float) -> Dict[str, Any]:
        """
        Scan files for PII.

        Returns:
            Dict with counts and severity assessment
        """
        import time

        start = time.time()

        counts = {
            "email": 0,
            "phone": 0,
            "ssn": 0,
            "credit_card": 0,
            "ip_address": 0,
        }

        if self.mode == "off":
            return {"counts": counts, "severity": "none"}

        files_checked = 0

        for f in files:
            # Check time budget
            if time.time() - start > time_budget:
                break

            # Skip large files
            if f.stat().st_size > 1024 * 1024:  # 1MB
                continue

            try:
                with open(f, "r", encoding="utf-8", errors="ignore") as fh:
                    # Read first 50KB
                    content = fh.read(51200)

                # Light mode: regex patterns
                for pii_type, pattern in self.PATTERNS.items():
                    matches = pattern.findall(content)
                    counts[pii_type] += len(matches)

                # Standard mode: use Presidio if available
                if self.mode == "standard" and self.has_presidio:
                    results = self.analyzer.analyze(text=content[:10000], language="en")
                    for result in results:
                        entity_type = result.entity_type.lower()
                        if entity_type == "email_address":
                            counts["email"] += 1
                        elif entity_type == "phone_number":
                            counts["phone"] += 1
                        elif entity_type == "us_ssn":
                            counts["ssn"] += 1
                        elif entity_type == "credit_card":
                            counts["credit_card"] += 1
                        elif entity_type == "ip_address":
                            counts["ip_address"] += 1

                files_checked += 1

            except Exception as e:
                logger.debug(f"Failed to scan {f} for PII: {e}")

        # Assess severity
        severity = self._assess_severity(counts)

        return {"counts": counts, "severity": severity, "files_checked": files_checked}

    def _assess_severity(self, counts: Dict[str, int]) -> str:
        """
        Assess PII severity based on counts.

        Returns:
            'none', 'low', 'medium', or 'high'
        """
        total = sum(counts.values())

        if total == 0:
            return "none"
        elif counts["ssn"] > 0 or counts["credit_card"] > 0:
            return "high"
        elif counts["email"] > 10 or counts["phone"] > 10:
            return "medium"
        elif total > 0:
            return "low"
        else:
            return "none"
