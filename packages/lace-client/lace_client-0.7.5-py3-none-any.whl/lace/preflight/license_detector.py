"""
License detection for datasets.
"""

import json
import logging
import re
from pathlib import Path
from typing import Any, Dict, List, Optional

logger = logging.getLogger(__name__)


class LicenseDetector:
    """Detects licenses in files and dataset cards."""

    # Common SPDX identifiers
    SPDX_LICENSES = {
        "MIT": ["mit license", "mit licence", "spdx: mit", "license: mit"],
        "Apache-2.0": [
            "apache license 2.0",
            "apache 2.0",
            "apache-2.0",
            "spdx: apache-2.0",
        ],
        "GPL-3.0": [
            "gpl-3.0",
            "gplv3",
            "gnu general public license v3",
            "spdx: gpl-3.0",
        ],
        "BSD-3-Clause": ["bsd-3-clause", "3-clause bsd", "spdx: bsd-3-clause"],
        "CC-BY-4.0": [
            "cc-by-4.0",
            "creative commons attribution 4.0",
            "spdx: cc-by-4.0",
        ],
        "CC-BY-SA-4.0": ["cc-by-sa-4.0", "creative commons attribution-sharealike 4.0"],
        "CC-BY-NC-4.0": [
            "cc-by-nc-4.0",
            "creative commons attribution-noncommercial 4.0",
        ],
        "CC-BY-ND-4.0": [
            "cc-by-nd-4.0",
            "creative commons attribution-noderivatives 4.0",
        ],
        "CC0-1.0": ["cc0", "public domain", "no rights reserved", "spdx: cc0-1.0"],
    }

    # Problematic license indicators
    PROBLEMATIC_PATTERNS = [
        "non-commercial",
        "noncommercial",
        "nc-only",
        "no derivatives",
        "noderivatives",
        "nd-only",
        "copyleft",
        "viral",
        "share-alike",
        "academic use only",
        "research only",
        "proprietary",
        "all rights reserved",
        "confidential",
        "internal use only",
    ]

    def detect(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """
        Detect license in file.

        Returns:
            None or dict with license info
        """
        # Check for LICENSE files
        if "license" in file_path.name.lower():
            return self._detect_in_license_file(file_path)

        # Check dataset cards
        if file_path.name.lower() in ("dataset_card.md", "readme.md", "datasheet.md"):
            return self._detect_in_dataset_card(file_path)

        # Check for package.json, pyproject.toml, etc.
        if file_path.name == "package.json":
            return self._detect_in_package_json(file_path)

        return None

    def _detect_in_license_file(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Detect license in LICENSE file."""
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read(10000).lower()

            # Check for SPDX identifiers
            for spdx_id, patterns in self.SPDX_LICENSES.items():
                for pattern in patterns:
                    if pattern in content:
                        # Check if it's a problematic license
                        is_problematic = False
                        confidence = 0.95

                        if "nc" in spdx_id.lower() or "nd" in spdx_id.lower():
                            is_problematic = True
                            confidence = 0.99

                        return {
                            "type": "flag" if is_problematic else "spdx",
                            "identifier": spdx_id,
                            "file": str(file_path),
                            "confidence": confidence,
                            "hint": (
                                spdx_id
                                if not is_problematic
                                else f"{spdx_id} (non-commercial/no-derivatives)"
                            ),
                        }

            # Check for problematic patterns
            for pattern in self.PROBLEMATIC_PATTERNS:
                if pattern in content:
                    return {
                        "type": "flag",
                        "identifier": "unknown",
                        "file": str(file_path),
                        "confidence": 0.7,
                        "hint": f"Contains '{pattern}'",
                    }

            # License file exists but couldn't identify
            return {
                "type": "noassertion",
                "identifier": "unknown",
                "file": str(file_path),
                "confidence": 0.5,
                "hint": "License file present but type unclear",
            }

        except Exception as e:
            logger.debug(f"Failed to read license file {file_path}: {e}")
            return None

    def _detect_in_dataset_card(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Detect license in dataset card/README."""
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                content = f.read(20000)

            # Look for license section
            license_section = None
            lines = content.split("\n")
            for i, line in enumerate(lines):
                if re.match(r"^#+\s*licen[cs]e", line, re.IGNORECASE):
                    # Found license section, extract next few lines
                    license_section = "\n".join(lines[i : i + 20]).lower()
                    break

            if not license_section:
                # Look for inline license mentions
                for line in lines:
                    if "license:" in line.lower() or "licence:" in line.lower():
                        license_section = line.lower()
                        break

            if license_section:
                # Check for SPDX
                for spdx_id, patterns in self.SPDX_LICENSES.items():
                    for pattern in patterns:
                        if pattern in license_section:
                            is_problematic = (
                                "nc" in spdx_id.lower() or "nd" in spdx_id.lower()
                            )
                            return {
                                "type": "flag" if is_problematic else "spdx",
                                "identifier": spdx_id,
                                "file": str(file_path),
                                "confidence": 0.85,
                                "hint": (
                                    spdx_id
                                    if not is_problematic
                                    else f"{spdx_id} (restrictions)"
                                ),
                                "where": "dataset_card",
                            }

                # Check problematic
                for pattern in self.PROBLEMATIC_PATTERNS:
                    if pattern in license_section:
                        return {
                            "type": "flag",
                            "identifier": "unknown",
                            "file": str(file_path),
                            "confidence": 0.65,
                            "hint": f"Dataset card mentions '{pattern}'",
                            "where": "dataset_card",
                        }

        except Exception as e:
            logger.debug(f"Failed to read dataset card {file_path}: {e}")

        return None

    def _detect_in_package_json(self, file_path: Path) -> Optional[Dict[str, Any]]:
        """Detect license in package.json."""
        try:
            with open(file_path, "r") as f:
                data = json.load(f)

            if "license" in data:
                license_str = data["license"]

                # Check if SPDX
                for spdx_id in self.SPDX_LICENSES:
                    if spdx_id.lower() == license_str.lower():
                        is_problematic = (
                            "nc" in spdx_id.lower() or "nd" in spdx_id.lower()
                        )
                        return {
                            "type": "flag" if is_problematic else "spdx",
                            "identifier": spdx_id,
                            "file": str(file_path),
                            "confidence": 0.9,
                            "hint": spdx_id,
                            "where": "package.json",
                        }

                # Unknown license
                return {
                    "type": "noassertion",
                    "identifier": license_str,
                    "file": str(file_path),
                    "confidence": 0.6,
                    "hint": f"package.json license: {license_str}",
                    "where": "package.json",
                }

        except Exception as e:
            logger.debug(f"Failed to read package.json {file_path}: {e}")

        return None
