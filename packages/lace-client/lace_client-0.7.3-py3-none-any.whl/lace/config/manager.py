"""
Configuration manager for Lace client.
Handles local salt, consent tracking, and answer caching.
"""

import json
import logging
import os
import secrets
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

logger = logging.getLogger(__name__)


class ConfigManager:
    """Manages local configuration, consent, and caching."""

    def __init__(self):
        """Initialize config manager."""
        self.global_config_path = Path.home() / ".lace" / "config.json"
        self.project_config_path = Path(".lace") / "config.json"
        self.project_answers_path = Path(".lace") / "answers.json"

        # Ensure directories exist
        self.global_config_path.parent.mkdir(parents=True, exist_ok=True)

        # Load or initialize config
        self.config = self._load_config()

    def _load_config(self) -> Dict[str, Any]:
        """Load global config or create default."""
        if self.global_config_path.exists():
            try:
                with open(self.global_config_path, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError) as e:
                logger.warning(f"Failed to load config: {e}")

        # Create default config
        return {
            "local_salt": secrets.token_hex(16),
            "consents": {},
            "global_answers": {},
            "created_at": datetime.utcnow().isoformat() + "Z",
        }

    def save_config(self):
        """Save config to disk."""
        try:
            with open(self.global_config_path, "w") as f:
                json.dump(self.config, f, indent=2)
        except IOError as e:
            logger.error(f"Failed to save config: {e}")

    def get_local_salt(self) -> str:
        """Get or create local salt for dataset ID generation."""
        if "local_salt" not in self.config:
            self.config["local_salt"] = secrets.token_hex(16)
            self.save_config()
        return self.config["local_salt"]

    def has_consent(self, payload_class: str) -> bool:
        """Check if user has consented to this exact payload class."""
        consents = self.config.get("consents", {})
        return payload_class in consents

    def save_consent(self, payload_class: str):
        """Record consent for a payload class."""
        if "consents" not in self.config:
            self.config["consents"] = {}

        self.config["consents"][payload_class] = {
            "timestamp": datetime.utcnow().isoformat() + "Z",
            "tool_version": self._get_version(),
        }
        self.save_config()

    def get_consent_info(self, payload_class: str) -> Optional[Dict]:
        """Get consent information for a payload class."""
        return self.config.get("consents", {}).get(payload_class)

    def get_global_answers(self) -> Dict[str, Any]:
        """Get cached global answers."""
        return self.config.get("global_answers", {})

    def save_global_answer(self, question_id: str, value: Any):
        """Save an answer globally."""
        if "global_answers" not in self.config:
            self.config["global_answers"] = {}
        self.config["global_answers"][question_id] = value
        self.save_config()

    def get_project_answers(self) -> Dict[str, Any]:
        """Get cached project-level answers."""
        if self.project_answers_path.exists():
            try:
                with open(self.project_answers_path, "r") as f:
                    return json.load(f)
            except (json.JSONDecodeError, IOError):
                pass
        return {}

    def save_project_answer(self, question_id: str, value: Any):
        """Save an answer at project level."""
        # Ensure project directory exists
        self.project_answers_path.parent.mkdir(parents=True, exist_ok=True)

        # Load existing answers
        answers = self.get_project_answers()
        answers[question_id] = value

        # Save back
        try:
            with open(self.project_answers_path, "w") as f:
                json.dump(answers, f, indent=2)
        except IOError as e:
            logger.error(f"Failed to save project answer: {e}")

    def clear_consent(self, payload_class: Optional[str] = None):
        """Clear consent records."""
        if payload_class:
            # Clear specific consent
            if "consents" in self.config and payload_class in self.config["consents"]:
                del self.config["consents"][payload_class]
                self.save_config()
        else:
            # Clear all consents
            self.config["consents"] = {}
            self.save_config()

    def _get_version(self) -> str:
        """Get tool version."""
        try:
            from lace import __version__

            return __version__
        except ImportError:
            return "unknown"


def build_payload_class(profile: str, send_domains: str) -> str:
    """
    Build exact payload class string encoding all options.

    Args:
        profile: 'minimal' or 'enhanced'
        send_domains: 'none', 'hashed', or 'clear'

    Returns:
        Exact payload class string like:
        - "analysis.min.v1@with_ext_hist"
        - "analysis.enhanced.v1@with_ext_hist@domains=clear"
    """
    if profile == "minimal":
        base = "analysis.min.v1@with_ext_hist"
    else:  # enhanced
        base = "analysis.enhanced.v1@with_ext_hist"
        if send_domains != "none":
            base += f"@domains={send_domains}"

    return base


def show_consent_dialog(payload_class: str) -> bool:
    """
    Show consent dialog for a payload class.

    Args:
        payload_class: The exact payload class string

    Returns:
        True if user consents, False otherwise
    """
    import click

    # Parse payload class for human-readable description
    if payload_class.startswith("analysis.min.v1"):
        mode = "minimal"
        details = [
            "✓ File counts, sizes, and modification times",
            "✓ Extension histogram (top-15 file types)",
            "✗ No file paths or names",
            "✗ No file content",
            "✗ No domains or URLs",
            "✗ No language detection",
        ]
    else:  # enhanced
        mode = "enhanced"
        details = [
            "✓ Everything from minimal mode, plus:",
            "✓ Language distribution (e.g., 72% English, 18% German)",
            "✓ License hints (e.g., MIT: 5 files, Apache: 2 files)",
            "✓ Synthetic data markers if detected",
        ]

        if "@domains=clear" in payload_class:
            details.append("✓ Top domain names in clear text")
        elif "@domains=hashed" in payload_class:
            details.append("✓ Top domains as hashed identifiers")
        else:
            details.append("✗ No domains sent (kept local)")

    click.echo("\n" + "=" * 60)
    click.echo(f"CONSENT REQUIRED: {mode.upper()} analysis mode")
    click.echo("=" * 60)
    click.echo("\nThis mode will send the following to Lace servers:")
    for detail in details:
        click.echo(f"  {detail}")

    click.echo("\nIMPORTANT:")
    click.echo("• No raw file content is ever uploaded")
    click.echo("• Dataset paths are replaced with non-reversible IDs")
    click.echo("• You'll only be asked once per exact configuration")
    click.echo(f"\nPayload class: {payload_class}")

    return click.confirm("\nDo you consent to send this data?", default=False)
