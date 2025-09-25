"""
Report generation for copyright and opt-out checking results.
Outputs JSONL, CSV, and SDS source summary.
"""

import csv
import json
import logging
import os
from datetime import datetime
from pathlib import Path
from typing import IO, Any, Dict, List, Optional, Tuple

logger = logging.getLogger(__name__)


class ReportGenerator:
    """Generate reports in various formats."""

    def __init__(self):
        """Initialize report generator."""
        self.timestamp = datetime.utcnow().isoformat() + "Z"

    def write_jsonl(
        self,
        results: List[Dict[str, Any]],
        output_path: Path,
        metadata: Optional[Dict[str, Any]] = None,
    ):
        """
        Write results to JSONL file with online signal support.

        Args:
            results: List of check results
            output_path: Path for JSONL output
            metadata: Optional metadata to include
        """
        with open(output_path, "w") as f:
            # Write metadata line if provided
            if metadata:
                meta_line = {
                    "_type": "metadata",
                    "timestamp": self.timestamp,
                    **metadata,
                }
                f.write(json.dumps(meta_line) + "\n")

            # Write result lines
            for result in results:
                # Ensure required fields
                line = {
                    "id": result.get("id", result.get("sha256", "unknown")),
                    "path": str(result.get("path", "")),
                    "sha256": result.get("sha256"),
                    "mime": result.get("mime_type", result.get("mime")),
                    "snippet": result.get("snippet", ""),
                    "phash": result.get("phash"),
                    "top_sources": self._format_sources(result),
                    "signals": self._format_signals(result),
                    "status": result.get("status", "UNKNOWN"),
                    "confidence": result.get("confidence", 0.0),
                    "timestamp": self.timestamp,
                    "attribution": result.get(
                        "attribution", {}
                    ),  # Preserve attribution for GPT processing
                }

                # Add online signals if present
                if "policy_signals" in result:
                    line["policy_signals"] = result["policy_signals"]

                if "gpt_sources" in result:
                    line["gpt_sources"] = result["gpt_sources"]

                # Add evidence if present
                if "evidence" in result:
                    line["evidence"] = result["evidence"]

                f.write(json.dumps(line) + "\n")

        logger.info(f"Wrote {len(results)} results to {output_path}")

    def write_csv(self, results: List[Dict[str, Any]], output_path: Path):
        """
        Write summary CSV by domain and status.

        Args:
            results: List of check results
            output_path: Path for CSV output
        """
        # Aggregate by domain and status
        domain_stats = {}

        for result in results:
            status = result.get("status", "UNKNOWN")

            # Get domains from result
            domains = []
            if "attribution" in result:
                domains = result["attribution"].get("domains", [])
            if "top_sources" in result:
                domains.extend(
                    [s["domain"] for s in result["top_sources"] if "domain" in s]
                )

            if not domains:
                domains = ["unknown"]

            for domain in domains:
                key = (domain, status)
                if key not in domain_stats:
                    domain_stats[key] = {"count": 0, "confidence_sum": 0.0}
                domain_stats[key]["count"] += 1
                domain_stats[key]["confidence_sum"] += result.get("confidence", 0.0)

        # Write CSV
        with open(output_path, "w", newline="") as f:
            writer = csv.writer(f)
            writer.writerow(["domain", "status", "count", "confidence_mean"])

            for (domain, status), stats in sorted(domain_stats.items()):
                confidence_mean = (
                    stats["confidence_sum"] / stats["count"]
                    if stats["count"] > 0
                    else 0.0
                )
                writer.writerow(
                    [domain, status, stats["count"], f"{confidence_mean:.3f}"]
                )

        logger.info(f"Wrote summary CSV to {output_path}")

    def generate_sds_summary(
        self,
        results: List[Dict[str, Any]],
        dataset_info: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Generate SDS sources summary for EU compliance.

        Args:
            results: List of check results
            dataset_info: Optional dataset metadata

        Returns:
            SDS sources summary dict
        """
        # Categorize results
        categories = {
            "public": [],
            "private": [],
            "crawled": [],
            "user": [],
            "synthetic": [],
            "other": [],  # For unknown/uncategorized content
            "demo": [],  # Demo content (not real data)
        }

        # Domain tracking
        all_domains = set()
        opted_out_domains = set()
        licensed_domains = {}

        for result in results:
            status = result.get("status", "UNKNOWN")

            # Extract domains
            domains = []
            if "attribution" in result:
                domains = result["attribution"].get("domains", [])
            elif "top_sources" in result:
                domains = [s["domain"] for s in result["top_sources"] if "domain" in s]

            all_domains.update(domains)

            # Helper functions for better classification
            def has_url_evidence(r):
                """Check if result has URL/domain evidence suggesting web crawl."""
                # Check for domains
                if domains:
                    return True
                # Check snippet for URLs
                snippet = r.get("snippet", "")
                if "http://" in snippet or "https://" in snippet:
                    return True
                # Check signals for domain evidence
                signals = r.get("signals", [])
                for signal in signals:
                    if signal.get("type") == "domain" and signal.get("value"):
                        return True
                return False

            def has_recognized_license(r):
                """Check if result has a recognized public license."""
                # Recognized public licenses (stricter list)
                recognized_licenses = [
                    "MIT",
                    "Apache-2.0",
                    "Apache",
                    "BSD-2-Clause",
                    "BSD-3-Clause",
                    "BSD",
                    "GPL-2.0",
                    "GPL-3.0",
                    "LGPL",
                    "MPL-2.0",
                    "CC-BY",
                    "CC-BY-SA",
                    "CC-BY-ND",
                    "CC-BY-NC",
                    "CC0",
                    "Public Domain",
                    "Unlicense",
                ]

                # Check signals
                signals = r.get("signals", [])
                for signal in signals:
                    if signal.get("type") == "license_public":
                        value = signal.get("value", "").upper()
                        # Require exact match or clear substring match
                        for lic in recognized_licenses:
                            if lic.upper() in value or value in lic.upper():
                                return True

                # Check attribution
                attribution = r.get("attribution", {})
                licenses = attribution.get("licenses", [])
                for lic in licenses:
                    if any(rec.upper() in lic.upper() for rec in recognized_licenses):
                        return True

                return False

            # Check for demo content first
            if result.get("demo") or result.get("metadata", {}).get("demo"):
                categories["demo"].append(result)
                continue  # Don't categorize demo content further

            # IMPORTANT: Use the ACTUAL status from the classifier, not path-based guessing
            # This ensures consistency between JSONL and summary

            # 1. Public: Files with explicit public license status
            if status == "PUBLIC_WITH_LICENSE" or status == "LICENSED_OK":
                categories["public"].append(result)
                # Track license
                licenses = result.get("attribution", {}).get("licenses", [])
                for domain in domains:
                    if domain not in licensed_domains:
                        licensed_domains[domain] = set()
                    licensed_domains[domain].update(licenses)

            # 2. Private/Copyrighted: Files with copyright status
            elif status == "COPYRIGHTED":
                categories["private"].append(result)

            # 3. Opted-out: Files from domains that opted out
            elif status in ["OPTED_OUT", "PROBABLY_OPTED_OUT"]:
                categories["other"].append(result)
                opted_out_domains.update(domains)

            # 4. User-provided data (if flagged)
            elif result.get("is_user_data") or result.get("user_provided"):
                categories["user"].append(result)

            # 5. Synthetic: AI-generated markers
            elif result.get("is_synthetic") or result.get("synthetic_markers"):
                categories["synthetic"].append(result)

            # 6. Crawled: ONLY if online mode, has domains, checked policy, and not opted out
            elif (
                result.get("policy_signals")
                and domains
                and status not in ["OPTED_OUT", "PROBABLY_OPTED_OUT"]
            ):
                categories["crawled"].append(result)

            # 7. Unknown: Everything else (including UNKNOWN status)
            else:
                categories["other"].append(
                    result
                )  # Will be mapped to 'unknown' in output

        # Build summary
        summary = {
            "public": {
                "count": len(categories["public"]),
                "domains": list(
                    set(
                        d
                        for r in categories["public"]
                        for d in r.get("attribution", {}).get("domains", [])
                    )
                ),
                "licenses": list(
                    set(l for d, ls in licensed_domains.items() for l in ls)
                ),
            },
            "private": {
                "count": len(categories["private"]),
                "domains": list(
                    set(
                        d
                        for r in categories["private"]
                        for d in r.get("attribution", {}).get("domains", [])
                    )
                ),
                "evidence": "Copyright notices detected",
            },
            "crawled": {
                "count": len(categories["crawled"]),
                "domains": list(
                    set(
                        d
                        for r in categories["crawled"]
                        for d in r.get("attribution", {}).get("domains", [])
                    )
                ),
                "opted_out": len(opted_out_domains),
                "opted_out_domains": list(opted_out_domains),
            },
            "user": {
                "count": len(categories["user"]),
                "domains": [],
                "evidence": "User-provided with confirmed licenses",
            },
            "synthetic": {
                "count": len(categories["synthetic"]),
                "domains": [],
                "evidence": "Generated or synthetic markers detected",
            },
            "unknown": {  # Changed key from 'other' to 'unknown' for clarity
                "count": len(
                    categories["other"]
                ),  # Still use internal 'other' category
                "domains": list(
                    set(
                        d
                        for r in categories["other"]
                        for d in r.get("attribution", {}).get("domains", [])
                    )
                ),
                "evidence": "Unknown provenance - insufficient information for categorization",
                "note": "Categorized as Unknown (Section 2.6) due to lack of clear signals",
            },
            "demo": {
                "count": len(categories["demo"]),
                "domains": [],
                "evidence": "Demo content - not real training data",
                "note": "demo-content",  # Special marker as requested
            },
        }

        # Add dataset info if provided
        if dataset_info:
            summary["dataset"] = {
                "total_files": dataset_info.get("total_files", len(results)),
                "total_bytes": dataset_info.get("total_bytes", 0),
                "sampled_files": len(results),
                "sample_rate": dataset_info.get("sample_rate", 0.01),
            }

        # Add generation metadata
        summary["metadata"] = {
            "generated_at": self.timestamp,
            "generator": "lace.check",
            "version": "0.1.0",
            "total_items_checked": len(results),
            "confidence_threshold": 0.5,
        }

        # Add dataset provenance if available
        if dataset_info and "provenance" in dataset_info:
            summary["dataset_provenance"] = dataset_info["provenance"]
        elif dataset_info:
            # Basic provenance from dataset_info
            summary["dataset_provenance"] = {
                "total_files": dataset_info.get("total_files", len(results)),
                "sampled_files": len(results),
                "sample_rate": dataset_info.get("sample_rate", 0.01),
                "dataset_name": dataset_info.get("dataset_name", "unknown"),
                "fetch_timestamp": self.timestamp,
            }

        return summary

    def load_jsonl(self, input_path: Path) -> List[Dict[str, Any]]:
        """
        Load results from JSONL file.

        Args:
            input_path: Path to JSONL file

        Returns:
            List of result dicts
        """
        results = []
        metadata = None

        with open(input_path, "r") as f:
            for line_num, line in enumerate(f, 1):
                try:
                    data = json.loads(line)

                    # Skip metadata lines
                    if data.get("_type") == "metadata":
                        metadata = data
                        continue

                    results.append(data)

                except json.JSONDecodeError as e:
                    logger.warning(f"Skipping invalid JSON at line {line_num}: {e}")

        logger.info(f"Loaded {len(results)} results from {input_path}")
        return results

    def merge_allowlist(
        self, results: List[Dict[str, Any]], allowlist_path: Path
    ) -> List[Dict[str, Any]]:
        """
        Apply allowlist overrides to results.

        Args:
            results: List of check results
            allowlist_path: Path to allowlist JSON

        Returns:
            Updated results with allowlist applied
        """
        # Load allowlist
        try:
            with open(allowlist_path, "r") as f:
                allowlist = json.load(f)
        except Exception as e:
            logger.error(f"Failed to load allowlist: {e}")
            return results

        # Apply overrides
        updated = []
        override_count = 0

        for result in results:
            # Check if item is allowlisted
            override = False

            # Check by SHA256
            if "sha256" in allowlist and result.get("sha256") in allowlist["sha256"]:
                result["status"] = "LICENSED_OK"
                result["confidence"] = 1.0
                result["allowlist_override"] = "sha256"
                override = True
                override_count += 1

            # Check by domain
            elif "domains" in allowlist:
                domains = []
                if "attribution" in result:
                    domains = result["attribution"].get("domains", [])
                elif "top_sources" in result:
                    domains = [
                        s["domain"] for s in result["top_sources"] if "domain" in s
                    ]

                for domain in domains:
                    if domain in allowlist["domains"]:
                        result["status"] = "LICENSED_OK"
                        result["confidence"] = 1.0
                        result["allowlist_override"] = f"domain:{domain}"
                        override = True
                        override_count += 1
                        break

            updated.append(result)

        logger.info(f"Applied {override_count} allowlist overrides")
        return updated

    def _format_sources(self, result: Dict) -> List[Dict]:
        """Format top sources for JSONL output."""
        sources = []

        # Get from attribution
        if "attribution" in result:
            attr = result["attribution"]
            domain_scores = attr.get("domain_scores", {})

            for domain, score in list(domain_scores.items())[:3]:
                sources.append({"domain": domain, "confidence": score})

        # Get from top_sources if present
        elif "top_sources" in result:
            sources = result["top_sources"][:3]

        return sources

    def _format_signals(self, result: Dict) -> List[Dict]:
        """Format signals for JSONL output."""
        signals = []

        # Get from classification signals
        if "signals" in result:
            for signal in result["signals"][:5]:  # Limit to top 5
                signals.append(
                    {
                        "type": signal.get("type"),
                        "value": signal.get("value"),
                        "confidence": signal.get("confidence", 0.0),
                        "source": signal.get("source"),
                    }
                )

        # Add from evidence if no signals
        elif "evidence" in result:
            for evidence in result["evidence"][:3]:
                signals.append(
                    {
                        "type": "evidence",
                        "value": evidence,
                        "confidence": result.get("confidence", 0.0),
                        "source": "heuristic",
                    }
                )

        return signals

    def generate_sds_section2_narrative(
        self,
        results: List[Dict[str, Any]],
        dataset_info: Optional[Dict[str, Any]] = None,
    ) -> str:
        """
        Generate SDS Section 2 narrative for EU Commission template with real counts.

        Args:
            results: List of check results
            dataset_info: Optional dataset metadata

        Returns:
            Markdown narrative for Section 2
        """
        # Generate the structured summary
        summary = self.generate_sds_summary(results, dataset_info)

        # Collect real counts
        total_items = len(results)
        public_count = summary.get("public", {}).get("count", 0)
        private_count = summary.get("private", {}).get("count", 0)
        crawled_count = summary.get("crawled", {}).get("count", 0)
        unknown_count = summary.get("unknown", {}).get("count", 0)

        # Count opted-out specifically
        opted_out_count = len(
            [
                r
                for r in results
                if r.get("status") in ["OPTED_OUT", "PROBABLY_OPTED_OUT"]
            ]
        )
        opted_out_domains = set()
        for r in results:
            if r.get("status") in ["OPTED_OUT", "PROBABLY_OPTED_OUT"]:
                if "attribution" in r and "domains" in r["attribution"]:
                    opted_out_domains.update(r["attribution"]["domains"])

        # Count unique domains
        unique_domains = set()
        for r in results:
            if "attribution" in r and "domains" in r["attribution"]:
                unique_domains.update(r["attribution"]["domains"])

        # Check attribution status
        gpt_attempted = sum(1 for r in results if r.get("gpt_attempted"))
        gpt_made = sum(1 for r in results if r.get("gpt_sources"))
        gpt_skipped = sum(1 for r in results if r.get("gpt_skipped"))

        # Determine analysis mode
        online_mode = any(r.get("policy_signals") for r in results)
        attribution_mode = gpt_attempted > 0

        if attribution_mode:
            mode_str = "full (online with attribution)"
        elif online_mode:
            mode_str = "domains-only (policy signals)"
        else:
            mode_str = "offline (no network calls)"

        # Build simple, deterministic narrative
        narrative = f"""# Section 2 - Data Sources (Summary)

**Analysis Mode: {mode_str}**

**Dataset Overview:**
- Total files analyzed: {total_items}
- Files successfully scanned: {len([r for r in results if r.get('status')])}
- Unique domains observed: {len(unique_domains)}

**Source Categories:**
- Publicly licensed files: {public_count}
- Private/copyrighted files: {private_count}
- Web-crawled files (no explicit license): {crawled_count}
- Opt-out detected (robots/headers): {opted_out_count}
- Unknown sources: {unknown_count}

**Attribution Status:**
"""

        if attribution_mode:
            narrative += f"- Attempts: {gpt_attempted}\n"
            narrative += f"- Successful: {gpt_made}\n"
            narrative += f"- Skipped: {gpt_skipped}"
            if gpt_skipped > 0:
                # Get skip reasons
                skip_reasons = {}
                for r in results:
                    if r.get("gpt_skipped"):
                        reason = r.get("skip_reason", "unknown")
                        skip_reasons[reason] = skip_reasons.get(reason, 0) + 1
                if skip_reasons:
                    top_reason = max(skip_reasons.items(), key=lambda x: x[1])
                    narrative += f" (primary reason: {top_reason[0]})\n"
                else:
                    narrative += "\n"
            else:
                narrative += "\n"
        elif online_mode:
            narrative += "- Not attempted (domains-only mode)\n"
        else:
            narrative += "- Not available (offline mode)\n"

        narrative += "\n**Compliance Information:**\n"

        if opted_out_count > 0:
            top_opted = list(opted_out_domains)[:5]
            if top_opted:
                narrative += f"- Files from these domains have opt-out preferences: {', '.join(top_opted)}\n"
            narrative += (
                "- We respect TDM-reservation signals and exclude opted-out content\n"
            )

        if private_count > 0:
            narrative += (
                f"- {private_count} files require licensing verification before use\n"
            )

        narrative += "\nSee `domains.csv` for the complete domain histogram and `sds_sources_summary.json` for detailed counts.\n"

        total_checked = summary.get("metadata", {}).get(
            "total_items_checked", len(results)
        )
        narrative += (
            f"- Analysis based on {total_checked} sampled files from the dataset.\n"
        )

        return narrative

    def write_sds_outputs(
        self,
        results: List[Dict[str, Any]],
        output_dir: Path,
        dataset_info: Optional[Dict[str, Any]] = None,
    ):
        """
        Write all SDS-related outputs.

        Args:
            results: List of check results
            output_dir: Directory for outputs
            dataset_info: Optional dataset metadata
        """
        output_dir = Path(output_dir)
        output_dir.mkdir(parents=True, exist_ok=True)

        # Generate and write SDS sources summary
        sds_summary = self.generate_sds_summary(results, dataset_info)
        summary_path = output_dir / "sds_sources_summary.json"
        with open(summary_path, "w") as f:
            json.dump(sds_summary, f, indent=2)
        logger.info(f"Wrote SDS sources summary to {summary_path}")

        # Generate and write Section 2 narrative
        narrative = self.generate_sds_section2_narrative(results, dataset_info)
        narrative_path = output_dir / "sds_section2_narrative.md"
        with open(narrative_path, "w") as f:
            f.write(narrative)
        logger.info(f"Wrote SDS Section 2 narrative to {narrative_path}")

        # Generate domain histogram (top 200)
        domain_hist = self.generate_domain_histogram(results, top_n=200)
        domains_path = output_dir / "domains.csv"
        items_scanned = len(results)
        mode = dataset_info.get("mode", "unknown") if dataset_info else "unknown"
        self.write_domain_histogram(
            domain_hist, domains_path, items_scanned=items_scanned, mode=mode
        )
        logger.info(f"Wrote domain histogram to {domains_path}")

        # Also generate full histogram with all domains
        domain_hist_full = self.generate_domain_histogram(results, top_n=None)
        domains_full_path = output_dir / "domains_full.csv"
        self.write_domain_histogram(
            domain_hist_full, domains_full_path, items_scanned=items_scanned, mode=mode
        )
        logger.info(f"Wrote full domain histogram to {domains_full_path}")

        # Generate run summary with metrics
        run_summary = self.generate_run_summary(results, dataset_info)

        # Merge AttributionProxy metrics if available (for online mode with attribution)
        # Check if any results have attribution data or attempts
        has_attribution = any(
            r.get("gpt_attempted")
            or r.get("gpt_skipped")
            or "gpt_sources" in r
            or ("attribution" in r and r["attribution"])
            for r in results
        )

        if has_attribution:
            try:
                from .providers.openai_proxy import AttributionProxy

                proxy_metrics = AttributionProxy.get_metrics()

                # Merge proxy metrics into run_summary
                if proxy_metrics:
                    # Update calls from proxy if they're more accurate
                    if proxy_metrics.get("calls_attempted", 0) > 0:
                        run_summary["calls_attempted"] = proxy_metrics[
                            "calls_attempted"
                        ]
                        run_summary["calls_made"] = proxy_metrics["calls_made"]
                        run_summary["calls_skipped"] = proxy_metrics["calls_skipped"]

                    # Merge skip reasons
                    if (
                        "skip_reasons" in proxy_metrics
                        and proxy_metrics["skip_reasons"]
                    ):
                        run_summary["skip_reasons"].update(
                            proxy_metrics["skip_reasons"]
                        )

                    # Add failure reasons if present
                    if (
                        "failure_reasons" in proxy_metrics
                        and proxy_metrics["failure_reasons"]
                    ):
                        run_summary["failure_reasons"] = proxy_metrics[
                            "failure_reasons"
                        ]

                    # Add latency percentiles if available
                    if "p50_ms" in proxy_metrics:
                        if "latencies" not in run_summary:
                            run_summary["latencies"] = {}
                        run_summary["latencies"]["attribution_p50_ms"] = proxy_metrics[
                            "p50_ms"
                        ]

                    if "p95_ms" in proxy_metrics:
                        if "latencies" not in run_summary:
                            run_summary["latencies"] = {}
                        run_summary["latencies"]["attribution_p95_ms"] = proxy_metrics[
                            "p95_ms"
                        ]

                    logger.debug(
                        f"Merged AttributionProxy metrics: {proxy_metrics.get('calls_attempted', 0)} attempts"
                    )
            except ImportError:
                # AttributionProxy not available in this context
                pass
            except Exception as e:
                logger.warning(f"Could not merge AttributionProxy metrics: {e}")

        # Add mode to run_summary if provided in dataset_info
        if dataset_info and "mode" in dataset_info:
            run_summary["mode"] = dataset_info["mode"]

        run_summary_path = output_dir / "run_summary.json"
        with open(run_summary_path, "w") as f:
            json.dump(run_summary, f, indent=2, default=str)
        logger.info(f"Wrote run summary to {run_summary_path}")

        # Write validation file and check for blockers
        validation_passed = self.write_validation_file(
            output_dir=output_dir,
            results=results,
            summary=sds_summary,
            run_summary=run_summary,
            histogram=(
                domain_hist[:10] if domain_hist else None
            ),  # Top 10 for validation file
        )

        if not validation_passed:
            logger.error("Validation failed with blockers - see VALIDATION.txt")
            # Optionally raise an exception or return error status
            import sys

            sys.exit(1)

    def generate_domain_histogram(
        self, results: List[Dict[str, Any]], top_n: Optional[int] = 200
    ) -> List[Tuple[str, int, float]]:
        """
        Generate domain histogram from results.

        Args:
            results: List of check results
            top_n: Number of top domains to return (None for all)

        Returns:
            List of (domain, count, percentage) tuples
        """
        domain_counts = {}

        for result in results:
            domains = []

            # Extract domains from various fields
            if "policy_signals" in result and "domain" in result["policy_signals"]:
                domains.append(result["policy_signals"]["domain"])

            if "attribution" in result and "domains" in result["attribution"]:
                domains.extend(result["attribution"]["domains"])

            if "top_sources" in result:
                for source in result["top_sources"]:
                    if isinstance(source, dict) and "domain" in source:
                        domains.append(source["domain"])

            # Count unique domains per item (a file can have multiple domains)
            for domain in set(domains):
                domain_counts[domain] = domain_counts.get(domain, 0) + 1

        # Sort by count and calculate percentages
        sorted_domains = sorted(domain_counts.items(), key=lambda x: x[1], reverse=True)

        # Return top N or all
        if top_n:
            result_domains = sorted_domains[:top_n]
        else:
            result_domains = sorted_domains

        # Calculate percentages based on total files, not total domains
        total_files = len(results)
        histogram = []
        for domain, count in result_domains:
            percentage = (count / total_files * 100) if total_files > 0 else 0
            histogram.append((domain, count, percentage))

        # Validate and warn if percentages exceed 100%
        if histogram:
            max_pct = max(p for _, _, p in histogram)
            if max_pct > 100:
                logger.warning(
                    f"Invalid domain percentages detected: max={max_pct:.2f}% (capping at 100%)"
                )
                histogram = [(d, c, min(100.0, p)) for d, c, p in histogram]

        return histogram

    def write_domain_histogram(
        self,
        histogram: List[Tuple[str, int, float]],
        output_path: Path,
        items_scanned: int = None,
        mode: str = None,
    ):
        """Write domain histogram to CSV with explanatory header."""
        with open(output_path, "w", newline="") as f:
            # Write header comments with metadata
            f.write(
                f"# Domain histogram showing top {len(histogram)} domains by occurrence\n"
            )
            if items_scanned:
                f.write(f"# items_scanned={items_scanned}\n")
            if mode:
                f.write(f"# mode={mode}\n")
            f.write(
                "# Percentage = (files containing domain / total files scanned) * 100\n"
            )
            f.write(
                "# Note: A file can contain multiple domains, so percentages may sum > 100%\n"
            )

            writer = csv.writer(f)
            writer.writerow(["domain", "count", "percentage"])

            for domain, count, percentage in histogram:
                # Extra validation to ensure percentages are reasonable
                if percentage > 100:
                    logger.error(
                        f"Invalid percentage {percentage}% for domain {domain} - capping at 100%"
                    )
                    percentage = 100.0
                writer.writerow([domain, count, f"{percentage:.2f}"])

    def generate_run_summary(
        self,
        results: List[Dict[str, Any]],
        dataset_info: Optional[Dict[str, Any]] = None,
    ) -> Dict[str, Any]:
        """
        Generate comprehensive run summary with metrics.

        Args:
            results: List of check results

        Returns:
            Run summary dict with metrics
        """
        # Collect metrics
        total_items = len(results)
        unique_domains = set()
        gpt_calls_attempted = 0
        gpt_calls_made = 0
        gpt_calls_skipped = 0
        skip_reasons = {}
        policy_latencies = []
        gpt_latencies = []

        for result in results:
            # Count domains
            if "policy_signals" in result and "domain" in result["policy_signals"]:
                unique_domains.add(result["policy_signals"]["domain"])

            if "attribution" in result and "domains" in result["attribution"]:
                for domain in result["attribution"]["domains"]:
                    unique_domains.add(domain)

            # Count GPT calls from result data (not class counters)
            if result.get("gpt_attempted"):
                gpt_calls_attempted += 1

                # Check outcome
                if result.get("gpt_sources"):
                    gpt_calls_made += 1
                elif result.get("gpt_skipped"):
                    gpt_calls_skipped += 1
                    reason = result.get("skip_reason", "unknown")
                    # Special case: detect missing LACE_API_KEY
                    if reason == "api_error" and not os.environ.get("LACE_API_KEY"):
                        reason = "missing_lace_api_key"
                    skip_reasons[reason] = skip_reasons.get(reason, 0) + 1

            # Collect latencies if available
            if "latency_ms" in result:
                if "policy_signals" in result:
                    policy_latencies.append(result["latency_ms"])
                elif "gpt_sources" in result:
                    gpt_latencies.append(result["latency_ms"])

        # Calculate percentiles
        def calculate_percentile(data: List[float], percentile: float) -> float:
            if not data:
                return 0.0
            sorted_data = sorted(data)
            idx = int(len(sorted_data) * percentile)
            return sorted_data[min(idx, len(sorted_data) - 1)]

        summary = {
            "items_scanned": total_items,
            "unique_domains": len(unique_domains),
            "calls_attempted": gpt_calls_attempted,  # New
            "calls_made": gpt_calls_made,  # Renamed for consistency
            "calls_skipped": gpt_calls_skipped,  # Renamed for consistency
            "skip_reasons": {
                "server_error": skip_reasons.get("server_error", 0),
                "rate_limit": skip_reasons.get("rate_limit", 0),
                "model_not_allowed": skip_reasons.get("model_not_allowed", 0),
                "unknown": skip_reasons.get("unknown", 0),
            },
            "timestamp": self.timestamp,
            # Legacy field names for backward compatibility
            "gpt_calls_made": gpt_calls_made,
            "gpt_calls_skipped": gpt_calls_skipped,
        }

        # Add latency metrics if available
        if policy_latencies:
            summary["latencies"] = {
                "policy_p50_ms": calculate_percentile(policy_latencies, 0.5),
                "policy_p95_ms": calculate_percentile(policy_latencies, 0.95),
            }

        if gpt_latencies:
            if "latencies" not in summary:
                summary["latencies"] = {}
            summary["latencies"].update(
                {
                    "gpt_p50_ms": calculate_percentile(gpt_latencies, 0.5),
                    "gpt_p95_ms": calculate_percentile(gpt_latencies, 0.95),
                }
            )

        # Add domain coverage info
        if gpt_calls_made > 0 or len(unique_domains) > 0:
            summary["domain_coverage"] = (
                f"{len(unique_domains)} unique domains identified"
            )

        # Add dataset metadata if provided
        if dataset_info:
            summary["dataset"] = {
                "name": dataset_info.get("dataset", "unknown"),
                "config": dataset_info.get("config", ""),
                "seed": dataset_info.get("seed"),
                "sampled": len(results),
                "total": dataset_info.get("total_samples", len(results)),
            }

        return summary

    def validate_category_counts(
        self, results: List[Dict[str, Any]], summary: Dict[str, Any]
    ) -> Tuple[bool, List[str]]:
        """
        Validate that category counts match actual JSONL status counts.

        Args:
            results: List of check results from JSONL
            summary: SDS sources summary

        Returns:
            (is_valid, list_of_errors)
        """
        errors = []

        # Recompute counts from JSONL data
        actual_counts = {
            "public": 0,
            "private": 0,
            "crawled": 0,
            "unknown": 0,
            "user": 0,
            "synthetic": 0,
            "demo": 0,
        }

        for result in results:
            if result.get("type") == "metadata":
                continue

            status = result.get("status", "UNKNOWN")
            domains = result.get("attribution", {}).get("domains", [])

            # Apply exact same logic as categorize_results
            if result.get("demo") or result.get("metadata", {}).get("demo"):
                actual_counts["demo"] += 1
            elif status in ["PUBLIC_WITH_LICENSE", "LICENSED_OK"]:
                actual_counts["public"] += 1
            elif status == "COPYRIGHTED":
                actual_counts["private"] += 1
            elif status in ["OPTED_OUT", "PROBABLY_OPTED_OUT"]:
                actual_counts["unknown"] += 1  # Maps to 'other' internally
            elif result.get("is_user_data") or result.get("user_provided"):
                actual_counts["user"] += 1
            elif result.get("is_synthetic") or result.get("synthetic_markers"):
                actual_counts["synthetic"] += 1
            elif (
                result.get("policy_signals")
                and domains
                and status not in ["OPTED_OUT", "PROBABLY_OPTED_OUT"]
            ):
                actual_counts["crawled"] += 1
            else:
                actual_counts["unknown"] += 1

        # Compare with summary counts
        for category in actual_counts:
            summary_count = summary.get(category, {}).get("count", 0)
            if actual_counts[category] != summary_count:
                errors.append(
                    f"Category '{category}': JSONL={actual_counts[category]}, "
                    f"Summary={summary_count}"
                )

        # Check total
        total_actual = sum(actual_counts.values())
        total_summary = sum(
            s.get("count", 0) for s in summary.values() if isinstance(s, dict)
        )
        if total_actual != total_summary:
            errors.append(
                f"Total mismatch: JSONL={total_actual}, Summary={total_summary}"
            )

        return len(errors) == 0, errors

    def write_validation_file(
        self,
        output_dir: Path,
        results: List[Dict[str, Any]],
        summary: Dict[str, Any],
        run_summary: Dict[str, Any],
        histogram: List[Tuple[str, int, float]] = None,
    ):
        """
        Write validation file with key metrics for audit trail.

        Args:
            output_dir: Directory for validation file
            results: List of check results
            summary: SDS sources summary
            run_summary: Run summary metrics
            histogram: Optional domain histogram
        """
        validation_path = output_dir / "VALIDATION.txt"

        with open(validation_path, "w") as f:
            f.write("=" * 60 + "\n")
            f.write("LACE CHECK VALIDATION REPORT\n")
            f.write("=" * 60 + "\n\n")

            # Run metadata
            f.write("RUN METADATA:\n")
            f.write(f"  Mode: {run_summary.get('mode', 'unknown')}\n")
            f.write(f"  Items Scanned: {run_summary.get('items_scanned', 0)}\n")
            f.write(f"  Timestamp: {run_summary.get('timestamp', 'unknown')}\n")
            f.write(f"  Unique Domains: {run_summary.get('unique_domains', 0)}\n")
            f.write("\n")

            # Attribution metrics
            f.write("ATTRIBUTION METRICS:\n")
            f.write(f"  Calls Attempted: {run_summary.get('calls_attempted', 0)}\n")
            f.write(f"  Calls Made: {run_summary.get('calls_made', 0)}\n")
            f.write(f"  Calls Skipped: {run_summary.get('calls_skipped', 0)}\n")

            skip_reasons = run_summary.get("skip_reasons", {})
            if skip_reasons:
                f.write("  Skip Reasons:\n")
                for reason, count in skip_reasons.items():
                    f.write(f"    - {reason}: {count}\n")
            f.write("\n")

            # Category breakdown
            f.write("CATEGORY BREAKDOWN:\n")
            if summary:
                for category in [
                    "public",
                    "private",
                    "crawled",
                    "unknown",
                    "user",
                    "synthetic",
                ]:
                    if category in summary:
                        count = summary[category].get("count", 0)
                        if count > 0:
                            f.write(f"  {category.capitalize()}: {count}\n")
            f.write("\n")

            # Top domains if available
            if histogram and len(histogram) > 0:
                f.write("TOP 10 DOMAINS:\n")
                for domain, count, pct in histogram[:10]:
                    f.write(f"  {domain}: {count} files ({pct:.2f}%)\n")
                f.write("\n")

            # Validation commands
            f.write("VALIDATION COMMANDS:\n")
            f.write("  Check metrics:\n")
            f.write(
                "    jq '.calls_attempted, .calls_made, .calls_skipped' run_summary.json\n"
            )
            f.write("  Count statuses:\n")
            f.write("    jq -r '.status' *.jsonl | sort | uniq -c\n")
            f.write("  Check mode consistency:\n")
            f.write("    grep -h mode *.json | sort | uniq\n")
            f.write("\n")

            # Data consistency checks
            f.write("DATA CONSISTENCY:\n")
            items_in_results = len(results)
            items_in_summary = run_summary.get("items_scanned", 0)
            f.write(f"  Results count: {items_in_results}\n")
            f.write(f"  Summary items_scanned: {items_in_summary}\n")
            f.write(
                f"  Match: {'✓' if items_in_results == items_in_summary else '✗'}\n"
            )

            # Check for data anomalies
            f.write("\nANOMALY CHECKS:\n")
            anomalies = []
            blockers = []  # Critical errors that should block execution

            # Check for >100% domain percentages
            if histogram:
                over_100 = [d for d, c, p in histogram if p > 100]
                if over_100:
                    anomalies.append(
                        f"Domains with >100% coverage: {', '.join(over_100)}"
                    )

            # Check for mismatched counts
            if items_in_results != items_in_summary:
                anomalies.append(
                    f"Count mismatch: results={items_in_results}, summary={items_in_summary}"
                )

            # Check attribution math
            attempted = run_summary.get("calls_attempted", 0)
            made = run_summary.get("calls_made", 0)
            skipped = run_summary.get("calls_skipped", 0)
            if attempted > 0 and (made + skipped) != attempted:
                anomalies.append(
                    f"Attribution math error: {attempted} != {made} + {skipped}"
                )

            # Validate category counts match JSONL
            category_match, category_errors = self.validate_category_counts(
                results, summary
            )
            if not category_match:
                blockers.extend(category_errors)

            # Check totals match
            if summary:
                category_total = sum(
                    s.get("count", 0) for s in summary.values() if isinstance(s, dict)
                )
                if category_total != items_in_results:
                    blockers.append(
                        f"Category total {category_total} != items scanned {items_in_results}"
                    )

            # Check mode consistency
            mode = run_summary.get("mode", "unknown")
            if mode == "offline" and attempted > 0:
                blockers.append(
                    f"Mode is 'offline' but calls_attempted={attempted} (should be 0)"
                )
            elif mode == "domains" and attempted > 0:
                blockers.append(
                    f"Mode is 'domains' but calls_attempted={attempted} (should be 0)"
                )
            elif mode == "full" and attempted == 0 and items_in_results > 0:
                anomalies.append("Mode is 'full' but no attribution attempted")

            # Check percentage math
            if histogram:
                total_pct = sum(p for _, _, p in histogram)
                # Allow up to 200% since files can have multiple domains
                if total_pct > 200 * len(histogram):
                    blockers.append(
                        f"Domain percentages sum to {total_pct:.1f}% which is impossible"
                    )

            # Write blocking errors first
            if blockers:
                f.write("  ❌ BLOCKERS DETECTED:\n")
                for blocker in blockers:
                    f.write(f"    - {blocker}\n")
                f.write("\n")

            # Then write warnings
            if anomalies:
                for anomaly in anomalies:
                    f.write(f"  ⚠️ {anomaly}\n")

            if not blockers and not anomalies:
                f.write("  ✓ No anomalies detected\n")

            f.write("\n" + "=" * 60 + "\n")

            # Add blocker summary at the end
            if blockers:
                f.write("\n❌ VALIDATION FAILED - BLOCKERS DETECTED\n")
                f.write("Fix the above issues before proceeding.\n")
                f.write("=" * 60 + "\n")

        logger.info(f"Wrote validation file to {validation_path}")

        # Also write machine-readable validation.json
        validation_json = {
            "timestamp": datetime.now().isoformat(),
            "passed": len(blockers) == 0,
            "blockers": blockers,
            "warnings": anomalies,
            "checks": {
                "category_counts_match": category_match,
                "math_consistency": len([b for b in blockers if "math" in b.lower()])
                == 0,
                "budget_respected": len([b for b in blockers if "budget" in b.lower()])
                == 0,
                "mode_consistency": len([b for b in blockers if "mode" in b.lower()])
                == 0,
            },
            "metrics": {
                "items_scanned": items_in_results,
                "calls_attempted": attempted,
                "calls_made": made,
                "calls_skipped": skipped,
                "mode": run_summary.get("mode", "unknown"),
            },
        }

        validation_json_path = output_dir / "validation.json"
        with open(validation_json_path, "w") as f:
            json.dump(validation_json, f, indent=2)

        logger.info(f"Wrote validation.json to {validation_json_path}")

        # Return whether validation passed (no blockers)
        return len(blockers) == 0
