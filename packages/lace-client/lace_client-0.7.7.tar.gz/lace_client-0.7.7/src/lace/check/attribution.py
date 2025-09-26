"""
Attribution engine for offline heuristic source detection.
Extracts URLs, citations, metadata without network calls.
"""

import json
import logging
import re
from pathlib import Path
from typing import Any, Dict, List, Optional, Set
from urllib.parse import urlparse

logger = logging.getLogger(__name__)


class AttributionEngine:
    """Extract source attribution signals from content (offline only)."""

    def __init__(self):
        """Initialize attribution engine."""
        # Common citation patterns
        self.citation_patterns = [
            # URLs
            r'https?://[^\s<>"{}|\\^`\[\]]+',
            r'www\.[^\s<>"{}|\\^`\[\]]+',
            # DOI
            r"doi:\s*10\.\d{4,}/[-._;()/:\w]+",
            r"https?://doi\.org/10\.\d{4,}/[-._;()/:\w]+",
            # ArXiv
            r"arXiv:\d{4}\.\d{4,5}(?:v\d+)?",
            # Academic citations
            r"\([A-Z][a-z]+ et al\.?,? \d{4}\)",
            r"\([A-Z][a-z]+ \d{4}\)",
            # Copyright notices
            r"(?:©|\(c\)|Copyright)\s+\d{4}\s+[A-Z][^.]*",
            r"All rights reserved",
        ]

        # Common domain indicators in file metadata
        self.metadata_keys = {
            "source",
            "origin",
            "website",
            "url",
            "link",
            "author",
            "creator",
            "publisher",
            "copyright",
            "license",
            "attribution",
            "citation",
        }

        # License indicators
        self.license_patterns = {
            "cc-by": r"CC[\s-]?BY(?:-\d\.\d)?",
            "cc-by-sa": r"CC[\s-]?BY[\s-]?SA(?:-\d\.\d)?",
            "cc-by-nc": r"CC[\s-]?BY[\s-]?NC(?:-\d\.\d)?",
            "cc-by-nd": r"CC[\s-]?BY[\s-]?ND(?:-\d\.\d)?",
            "cc0": r"CC0(?:\s+1\.0)?",
            "mit": r"MIT License",
            "apache": r"Apache License(?:\s+(?:Version\s+)?2\.0)?",
            "gpl": r"GPL(?:v?\d)?",
            "bsd": r"BSD(?:\s+\d-Clause)?",
            "public-domain": r"Public Domain",
        }

        # Copyright indicators
        self.copyright_indicators = [
            r"©\s*\d{4}",
            r"\(c\)\s*\d{4}",
            r"Copyright\s+\d{4}",
            r"All\s+rights\s+reserved",
            r"Proprietary\s+and\s+confidential",
        ]

    def attribute(
        self, content: str, metadata: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Extract attribution signals from content and metadata.

        Args:
            content: Text content or snippet
            metadata: Optional metadata dict (EXIF, headers, etc.)

        Returns:
            Attribution signals dict
        """
        result = {
            "domains": [],
            "citations": [],
            "licenses": [],
            "copyright_signals": [],
            "confidence": 0.0,
            "evidence": [],
        }

        if not content and not metadata:
            return result

        # Extract from content
        if content:
            # Extract URLs and domains
            urls = self._extract_urls(content)
            domains = self._urls_to_domains(urls)
            result["domains"] = list(domains)

            # Extract citations
            citations = self._extract_citations(content)
            result["citations"] = citations

            # Extract licenses
            licenses = self._extract_licenses(content)
            result["licenses"] = licenses

            # Extract copyright signals
            copyright_signals = self._extract_copyright(content)
            result["copyright_signals"] = copyright_signals

        # Extract from metadata
        if metadata:
            metadata_domains = self._extract_from_metadata(metadata)
            result["domains"].extend(metadata_domains)
            result["domains"] = list(set(result["domains"]))  # Dedupe

        # Calculate confidence based on evidence strength
        result["confidence"] = self._calculate_confidence(result)

        # Build evidence list
        if result["domains"]:
            result["evidence"].append(f"Found {len(result['domains'])} domain(s)")
        if result["citations"]:
            result["evidence"].append(f"Found {len(result['citations'])} citation(s)")
        if result["licenses"]:
            result["evidence"].append(
                f"Detected license: {', '.join(result['licenses'])}"
            )
        if result["copyright_signals"]:
            result["evidence"].append("Copyright indicators present")

        return result

    def _extract_urls(self, text: str) -> List[str]:
        """Extract URLs from text."""
        urls = []

        # Find all URL-like patterns
        url_pattern = re.compile(
            r'(?:https?://|www\.)[^\s<>"{}|\\^`\[\]]+', re.IGNORECASE
        )

        matches = url_pattern.findall(text)
        for match in matches:
            # Clean up common trailing punctuation
            match = re.sub(r"[.,;:!?\)]+$", "", match)

            # Add scheme if missing
            if match.startswith("www."):
                match = "http://" + match

            urls.append(match)

        return urls

    def _urls_to_domains(self, urls: List[str]) -> Set[str]:
        """Convert URLs to unique domains."""
        domains = set()

        for url in urls:
            try:
                parsed = urlparse(url)
                domain = parsed.netloc or parsed.path.split("/")[0]

                # Clean up domain
                domain = domain.lower()
                if domain.startswith("www."):
                    domain = domain[4:]

                if domain and "." in domain:
                    domains.add(domain)
            except Exception:
                continue

        return domains

    def _extract_citations(self, text: str) -> List[str]:
        """Extract academic citations from text."""
        citations = []

        # DOI patterns
        doi_pattern = re.compile(
            r"(?:doi:\s*|https?://doi\.org/)10\.\d{4,}/[-._;()/:\w]+", re.IGNORECASE
        )
        citations.extend(doi_pattern.findall(text))

        # ArXiv patterns
        arxiv_pattern = re.compile(r"arXiv:\d{4}\.\d{4,5}(?:v\d+)?", re.IGNORECASE)
        citations.extend(arxiv_pattern.findall(text))

        # Author-year citations
        author_year = re.compile(r"\([A-Z][a-z]+(?:\s+et\s+al\.?)?,?\s+\d{4}\)")
        citations.extend(author_year.findall(text))

        return list(set(citations))  # Dedupe

    def _extract_licenses(self, text: str) -> List[str]:
        """Extract license indicators from text."""
        found_licenses = []

        for license_name, pattern in self.license_patterns.items():
            if re.search(pattern, text, re.IGNORECASE):
                found_licenses.append(license_name.upper())

        # Also check for SPDX identifiers
        spdx_pattern = re.compile(r"SPDX-License-Identifier:\s*([\w.-]+)")
        spdx_matches = spdx_pattern.findall(text)
        found_licenses.extend(spdx_matches)

        return list(set(found_licenses))  # Dedupe

    def _extract_copyright(self, text: str) -> List[str]:
        """Extract copyright signals from text."""
        signals = []

        for pattern in self.copyright_indicators:
            matches = re.findall(pattern, text, re.IGNORECASE)
            signals.extend(matches)

        # Extract copyright holders
        copyright_holder = re.compile(
            r"(?:©|\(c\)|Copyright)\s+(?:\d{4}\s+)?([A-Z][^.,\n]*)", re.IGNORECASE
        )
        holders = copyright_holder.findall(text)
        for holder in holders:
            holder = holder.strip()
            if len(holder) < 100:  # Sanity check
                signals.append(f"Copyright: {holder}")

        return list(set(signals))  # Dedupe

    def _extract_from_metadata(self, metadata: Dict) -> List[str]:
        """Extract domains from file metadata."""
        domains = []

        def extract_recursive(obj, depth=0):
            """Recursively extract domain-like values."""
            if depth > 5:  # Prevent infinite recursion
                return

            if isinstance(obj, dict):
                for key, value in obj.items():
                    # Check if key suggests source/domain info
                    if any(k in key.lower() for k in self.metadata_keys):
                        if isinstance(value, str):
                            # Try to extract domain
                            urls = self._extract_urls(value)
                            if urls:
                                domains.extend(self._urls_to_domains(urls))
                            # Also check if value itself looks like domain
                            elif "." in value and len(value) < 100:
                                # Simple domain heuristic
                                if re.match(r"^[\w.-]+\.\w{2,}$", value):
                                    domains.append(value.lower())

                    # Recurse into nested structures
                    extract_recursive(value, depth + 1)

            elif isinstance(obj, list):
                for item in obj:
                    extract_recursive(item, depth + 1)

        extract_recursive(metadata)
        return list(set(domains))  # Dedupe

    def _calculate_confidence(self, signals: Dict) -> float:
        """
        Calculate confidence score based on evidence strength.

        Args:
            signals: Attribution signals dict

        Returns:
            Confidence score 0-1
        """
        confidence = 0.0

        # Strong signals
        if signals["domains"]:
            confidence += 0.4 * min(len(signals["domains"]) / 3, 1.0)

        if signals["citations"]:
            confidence += 0.3 * min(len(signals["citations"]) / 2, 1.0)

        # Medium signals
        if signals["licenses"]:
            confidence += 0.2

        if signals["copyright_signals"]:
            confidence += 0.1

        return min(confidence, 1.0)

    def merge_attributions(self, attributions: List[Dict]) -> Dict[str, Any]:
        """
        Merge multiple attribution results.

        Args:
            attributions: List of attribution dicts

        Returns:
            Merged attribution with aggregated confidence
        """
        if not attributions:
            return {
                "domains": [],
                "citations": [],
                "licenses": [],
                "copyright_signals": [],
                "confidence": 0.0,
                "evidence": [],
            }

        # Aggregate all signals
        all_domains = set()
        all_citations = set()
        all_licenses = set()
        all_copyright = set()
        all_evidence = []

        for attr in attributions:
            all_domains.update(attr.get("domains", []))
            all_citations.update(attr.get("citations", []))
            all_licenses.update(attr.get("licenses", []))
            all_copyright.update(attr.get("copyright_signals", []))
            all_evidence.extend(attr.get("evidence", []))

        # Calculate domain scores (frequency-based)
        domain_counts = {}
        for attr in attributions:
            for domain in attr.get("domains", []):
                domain_counts[domain] = domain_counts.get(domain, 0) + 1

        # Sort domains by frequency
        top_domains = sorted(domain_counts.items(), key=lambda x: x[1], reverse=True)

        # Build result
        result = {
            "domains": [d for d, _ in top_domains],
            "domain_scores": {d: c / len(attributions) for d, c in top_domains},
            "citations": list(all_citations),
            "licenses": list(all_licenses),
            "copyright_signals": list(all_copyright),
            "confidence": sum(a.get("confidence", 0) for a in attributions)
            / len(attributions),
            "evidence": list(set(all_evidence)),  # Dedupe evidence
        }

        return result
