"""
Preflight orchestrator - coordinates all checks and enforces budget.
"""

import hashlib
import json
import logging
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

from .. import __version__
from ..utils import redact_sensitive
from .registry import RegistryManager
from .scanner import DatasetScanner
from .verdict import VerdictEngine

logger = logging.getLogger(__name__)


@dataclass
class PreflightConfig:
    """Configuration for preflight checks."""

    budget_s: int = 60
    sample_rate: float = 0.01
    pii_mode: str = "light"  # off|light|standard
    max_concurrency: int = 8
    policy_mode: str = "default"  # default|strict|lenient
    no_network: bool = False
    registry_path: Optional[Path] = None
    debug: bool = False

    def validate(self):
        """Validate configuration."""
        if not 1 <= self.budget_s <= 3600:
            raise ValueError(f"Budget must be 1-3600 seconds, got {self.budget_s}")
        if not 0 < self.sample_rate <= 1:
            raise ValueError(f"Sample rate must be 0-1, got {self.sample_rate}")
        if self.pii_mode not in ("off", "light", "standard"):
            raise ValueError(
                f"PII mode must be off|light|standard, got {self.pii_mode}"
            )
        if self.policy_mode not in ("default", "strict", "lenient"):
            raise ValueError(
                f"Policy mode must be default|strict|lenient, got {self.policy_mode}"
            )
        if not 1 <= self.max_concurrency <= 100:
            raise ValueError(
                f"Max concurrency must be 1-100, got {self.max_concurrency}"
            )


def preflight_check(
    dataset_path: str,
    config: Optional[PreflightConfig] = None,
    output_path: Optional[str] = None,
) -> Dict[str, Any]:
    """
    Run preflight checks on a dataset.

    Args:
        dataset_path: Path to dataset file or directory
        config: Preflight configuration
        output_path: Optional path to write JSON report

    Returns:
        Preflight report dict
    """
    if config is None:
        config = PreflightConfig()
    config.validate()

    start_time = time.time()
    network_start_ms = 0

    # Initialize components
    registry_mgr = RegistryManager(config.registry_path)
    scanner = DatasetScanner(config)
    verdict_engine = VerdictEngine(config.policy_mode)

    # Load registry
    registry_info = registry_mgr.load()
    if not registry_info["loaded"] and config.no_network:
        logger.warning("No registry loaded and --no-network specified")

    # Reserve 20% of budget for finalization
    scan_budget = config.budget_s * 0.8

    # Scan dataset
    dataset_path = Path(dataset_path)
    if not dataset_path.exists():
        raise FileNotFoundError(f"Dataset not found: {dataset_path}")

    # Track network usage
    network_tracker = {"used_ms": 0, "calls": 0}

    # Run scanner with budget
    scan_start = time.time()
    signals = scanner.scan(
        dataset_path,
        registry_mgr.registry,
        scan_budget,
        network_tracker,
        config.no_network,
    )
    scan_elapsed = time.time() - scan_start

    # Check if budget exhausted
    total_elapsed = time.time() - start_time
    budget_exhausted = total_elapsed >= config.budget_s or scan_elapsed >= scan_budget

    # Calculate verdict
    verdict = verdict_engine.calculate(signals, registry_info["verified"])

    # Build report
    report = {
        "schema_version": "preflight.v0.1",
        "dataset": {
            "locator": str(dataset_path.absolute()),
            "files": signals.get("file_count", 0),
            "bytes": signals.get("byte_count", 0),
        },
        "config": {
            "budget_s": config.budget_s,
            "sample_rate": config.sample_rate,
            "pii_mode": config.pii_mode,
            "max_concurrency": config.max_concurrency,
        },
        "registry": {
            "version": registry_info.get("version", "unknown"),
            "sources": registry_info.get("sources", []),
            "verified": registry_info.get("verified", False),
        },
        "policy": {"mode": config.policy_mode, "version": "preflight-policy.v1"},
        "signals": signals,
        "verdict": asdict(verdict),
        "budget_exhausted": budget_exhausted,
        "network_used_ms": network_tracker["used_ms"],
        "created_at": datetime.now(timezone.utc).isoformat(),
        "tool": {"name": "lace", "version": __version__},
    }

    # Write output if requested
    if output_path:
        with open(output_path, "w") as f:
            json.dump(report, f, indent=2, default=str)
        logger.info(f"Preflight report written to {output_path}")

    # Log verdict
    if not config.debug:
        # One-line verdict for CLI
        print(
            f"Preflight: {verdict.status.upper()} (confidence: {verdict.confidence:.2f})"
        )
        if verdict.rationale:
            print(f"Reasons: {'; '.join(verdict.rationale[:3])}")

    return report
