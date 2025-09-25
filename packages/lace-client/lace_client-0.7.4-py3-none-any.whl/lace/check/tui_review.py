"""
TUI (Text User Interface) for reviewing and marking items as licensed.
Simple Click-based interface for allowlist management.
"""

import json
import logging
import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Set

import click

logger = logging.getLogger(__name__)


class ReviewInterface:
    """Interactive review interface for check results."""

    def __init__(self, allowlist_path: Optional[Path] = None):
        """
        Initialize review interface.

        Args:
            allowlist_path: Path to allowlist file
        """
        self.allowlist_path = (
            allowlist_path or Path.home() / ".lace" / "licenses_allowlist.json"
        )
        self.allowlist = self._load_allowlist()
        self.changes_made = False

    def _load_allowlist(self) -> Dict[str, Any]:
        """Load existing allowlist or create new."""
        if self.allowlist_path.exists():
            try:
                with open(self.allowlist_path, "r") as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Failed to load allowlist: {e}")

        # Default structure
        return {
            "version": "1.0",
            "domains": {},  # domain -> license info
            "sha256": {},  # sha256 -> license info
            "patterns": [],  # glob patterns for paths
        }

    def _save_allowlist(self):
        """Save allowlist to disk."""
        # Ensure directory exists
        self.allowlist_path.parent.mkdir(parents=True, exist_ok=True)

        try:
            with open(self.allowlist_path, "w") as f:
                json.dump(self.allowlist, f, indent=2)
            logger.info(f"Saved allowlist to {self.allowlist_path}")
        except Exception as e:
            logger.error(f"Failed to save allowlist: {e}")

    def review(self, report_path: Path) -> int:
        """
        Interactive review of report items.

        Args:
            report_path: Path to JSONL report

        Returns:
            Number of items marked as licensed
        """
        # Load report
        results = self._load_report(report_path)
        if not results:
            click.echo("No results to review")
            return 0

        # Filter to items needing review
        review_items = [
            r
            for r in results
            if r.get("status") not in ["LICENSED_OK", "PUBLIC_WITH_LICENSE"]
        ]

        if not review_items:
            click.echo("All items already licensed or public")
            return 0

        click.echo(f"\n{'='*60}")
        click.echo(f"Lace Check Review - {len(review_items)} items need review")
        click.echo(f"{'='*60}\n")

        marked_count = 0

        # Review each item
        for i, item in enumerate(review_items, 1):
            click.echo(f"\n[{i}/{len(review_items)}] {'-'*40}")
            self._display_item(item)

            # Ask for action
            action = self._prompt_action(item)

            if action == "licensed":
                self._mark_licensed(item)
                marked_count += 1
                click.echo(click.style("✓ Marked as LICENSED_OK", fg="green"))

            elif action == "skip":
                continue

            elif action == "quit":
                break

        # Save if changes made
        if self.changes_made:
            self._save_allowlist()
            click.echo(f"\n✓ Saved {marked_count} items to allowlist")

            # Offer to regenerate report
            if click.confirm("\nRegenerate report with allowlist applied?"):
                self._regenerate_report(report_path, results)

        return marked_count

    def _load_report(self, report_path: Path) -> List[Dict]:
        """Load JSONL report."""
        results = []

        try:
            with open(report_path, "r") as f:
                for line in f:
                    try:
                        data = json.loads(line)
                        # Skip metadata lines
                        if data.get("_type") != "metadata":
                            results.append(data)
                    except json.JSONDecodeError:
                        continue
        except Exception as e:
            click.echo(f"Error loading report: {e}", err=True)

        return results

    def _display_item(self, item: Dict):
        """Display item details for review."""
        # Basic info
        click.echo(f"Path: {item.get('path', 'unknown')}")
        click.echo(f"Status: {click.style(item.get('status', 'UNKNOWN'), fg='yellow')}")
        click.echo(f"Confidence: {item.get('confidence', 0.0):.2f}")

        # Sources
        sources = item.get("top_sources", [])
        if sources:
            domains = [s.get("domain", "unknown") for s in sources[:3]]
            click.echo(f"Sources: {', '.join(domains)}")

        # Signals
        signals = item.get("signals", [])
        if signals:
            click.echo("Signals:")
            for signal in signals[:3]:
                click.echo(f"  • {signal.get('type')}: {signal.get('value')}")

        # Snippet preview
        snippet = item.get("snippet", "")
        if snippet:
            preview = snippet[:200] + "..." if len(snippet) > 200 else snippet
            # Clean up for display
            preview = preview.replace("\n", " ").replace("\r", "")
            click.echo(f"\nSnippet: {preview}")

    def _prompt_action(self, item: Dict) -> str:
        """Prompt user for action on item."""
        click.echo("\nActions:")
        click.echo("  [L]icensed - Mark as LICENSED_OK")
        click.echo("  [S]kip     - Skip this item")
        click.echo("  [Q]uit     - Save and exit")

        while True:
            choice = click.prompt("Choice", type=str).lower()

            if choice in ["l", "licensed"]:
                # Ask for license details
                license_info = click.prompt(
                    "License/reason (optional)",
                    default="User confirmed",
                    show_default=True,
                )
                return "licensed"

            elif choice in ["s", "skip"]:
                return "skip"

            elif choice in ["q", "quit"]:
                return "quit"

            else:
                click.echo("Invalid choice. Please enter L, S, or Q")

    def _mark_licensed(self, item: Dict):
        """Mark item as licensed in allowlist."""
        # Add by SHA256 if available
        if item.get("sha256"):
            self.allowlist["sha256"][item["sha256"]] = {
                "status": "LICENSED_OK",
                "path": item.get("path"),
                "marked_at": item.get("timestamp"),
            }

        # Also add domains if present
        sources = item.get("top_sources", [])
        for source in sources:
            domain = source.get("domain")
            if domain:
                if click.confirm(f"  Also allowlist domain '{domain}'?"):
                    self.allowlist["domains"][domain] = {
                        "status": "LICENSED_OK",
                        "marked_at": item.get("timestamp"),
                    }

        self.changes_made = True

    def _regenerate_report(self, original_path: Path, results: List[Dict]):
        """Regenerate report with allowlist applied."""
        from .report import ReportGenerator

        # Apply allowlist to results
        updated_results = []
        override_count = 0

        for result in results:
            # Check SHA256
            if result.get("sha256") in self.allowlist["sha256"]:
                result["status"] = "LICENSED_OK"
                result["confidence"] = 1.0
                result["allowlist_override"] = "sha256"
                override_count += 1

            # Check domains
            else:
                sources = result.get("top_sources", [])
                for source in sources:
                    domain = source.get("domain")
                    if domain and domain in self.allowlist["domains"]:
                        result["status"] = "LICENSED_OK"
                        result["confidence"] = 1.0
                        result["allowlist_override"] = f"domain:{domain}"
                        override_count += 1
                        break

            updated_results.append(result)

        # Generate new report
        output_path = original_path.parent / f"{original_path.stem}_reviewed.jsonl"

        generator = ReportGenerator()
        generator.write_jsonl(
            updated_results,
            output_path,
            metadata={"allowlist_applied": True, "overrides": override_count},
        )

        # Also generate updated CSV
        csv_path = output_path.with_suffix(".csv")
        generator.write_csv(updated_results, csv_path)

        click.echo(f"\n✓ Generated reviewed report: {output_path}")
        click.echo(f"✓ Generated summary CSV: {csv_path}")
        click.echo(f"  Applied {override_count} allowlist overrides")

    def batch_mark(
        self, patterns: List[str], license_info: str = "Batch licensed"
    ) -> int:
        """
        Batch mark items matching patterns.

        Args:
            patterns: List of domain/path patterns
            license_info: License description

        Returns:
            Number of patterns added
        """
        count = 0

        for pattern in patterns:
            # Check if it's a domain
            if "." in pattern and "/" not in pattern:
                self.allowlist["domains"][pattern] = {
                    "status": "LICENSED_OK",
                    "info": license_info,
                }
                count += 1
            # Otherwise treat as path pattern
            else:
                self.allowlist["patterns"].append(
                    {"pattern": pattern, "status": "LICENSED_OK", "info": license_info}
                )
                count += 1

        if count > 0:
            self.changes_made = True
            self._save_allowlist()

        return count
