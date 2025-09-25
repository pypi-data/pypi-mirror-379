"""
SDS Scanner - Combines existing scanners for EU AI Act compliance.
Reuses DatasetAnalyzer, DatasetScanner, and MinimalAnalyzer.
"""

import logging
import time
from collections import Counter
from pathlib import Path
from typing import Any, Dict, List, Optional

from ..preflight.registry import Registry
from ..preflight.scanner import DatasetScanner
from ..wizard.analyzer import DatasetAnalyzer
from ..wizard.analyzer_minimal import MinimalAnalyzer


# Simple config class for preflight scanner
class Config:
    def __init__(self, sample_rate=0.1, pii_mode="off", max_concurrency=10):
        self.sample_rate = sample_rate
        self.pii_mode = pii_mode
        self.max_concurrency = max_concurrency


logger = logging.getLogger(__name__)


class SDSScanner:
    """
    Thin wrapper combining existing scanners for EU AI Act SDS generation.

    Leverages:
    - DatasetAnalyzer: modalities, languages, volumes, public datasets
    - DatasetScanner: opt-out checking, license detection
    - MinimalAnalyzer: fast metadata for consent
    """

    def __init__(self, config: Optional[Dict] = None):
        """Initialize with existing scanner components."""
        self.config = config or {}

        # Initialize existing scanners
        self.analyzer = DatasetAnalyzer(allow_external_ai=False)
        self.minimal = MinimalAnalyzer(config)

        # For opt-out checking
        self.preflight_config = Config(
            sample_rate=0.1,
            pii_mode="off",  # We don't need PII for SDS
            max_concurrency=10,
        )
        self.preflight = DatasetScanner(self.preflight_config)
        self.registry = Registry()

        # Try to load registry, create dev registry if missing
        loaded = False
        try:
            loaded = self.registry.load()
        except Exception:
            loaded = False

        if not loaded:
            from ..preflight.registry import RegistryManager

            mgr = RegistryManager()
            # Try to refresh; if fails, create dev registry
            ok = False
            try:
                ok = mgr.refresh(force=False)
            except Exception:
                ok = False
            if not ok:
                mgr.create_dev_registry()
            # Attempt to load again
            self.registry.load()

    def quick_scan(
        self, dataset_path: str, max_files: int = 5000, max_seconds: int = 60
    ) -> Dict[str, Any]:
        """
        Quick scan for consent prompt - uses MinimalAnalyzer.
        Returns only metadata that will be sent to server.

        Args:
            dataset_path: Path to dataset
            max_files: Maximum files to scan
            max_seconds: Maximum seconds to spend

        Returns:
            Minimal metadata for consent display
        """
        start_time = time.time()

        # Use MinimalAnalyzer for fast, content-free scan
        analysis = self.minimal.analyze(
            [dataset_path],
            profile="minimal",
            send_domains="none",  # No domains in consent
        )

        # Extract key fields for consent
        dataset = analysis["datasets"][0] if analysis.get("datasets") else {}

        # Calculate modalities from extensions
        modalities = self._detect_modalities_from_extensions(
            analysis.get("extensions", {})
        )

        # Format for consent display
        result = {
            "file_count": dataset.get("files", 0),
            "total_bytes": dataset.get("bytes", 0),
            "total_gb": round(dataset.get("bytes", 0) / (1024**3), 2),
            "latest_mtime": dataset.get("latest_mtime", "unknown"),
            "extensions": dict(list(analysis.get("extensions", {}).items())[:10]),
            "modalities": modalities,
        }

        # Convert latest_mtime to MM/YYYY with leading zeros
        if result["latest_mtime"] != "unknown":
            try:
                from datetime import datetime

                dt = datetime.fromisoformat(result["latest_mtime"])
                # Ensure MM/YYYY format with leading zeros
                result["latest_acquisition"] = dt.strftime(
                    "%m/%Y"
                )  # %m gives 01-12 with leading zeros
            except:
                result["latest_acquisition"] = "unknown"
        else:
            result["latest_acquisition"] = "unknown"

        elapsed = time.time() - start_time
        logger.info(f"Quick scan completed in {elapsed:.1f}s")

        return result

    def full_scan(
        self, dataset_path: str, include_opt_out: bool = True
    ) -> Dict[str, Any]:
        """
        Full scan for SDS generation - combines all scanners.

        Args:
            dataset_path: Path to dataset
            include_opt_out: Whether to check opt-out signals

        Returns:
            Complete analysis for SDS generation with standardized field names
        """
        logger.info(f"Starting full SDS scan of {dataset_path}")

        # 1. Run DatasetAnalyzer for comprehensive analysis
        analysis = self.analyzer.analyze_dataset(dataset_path)

        # 2. Enhance language detection (sample more files)
        lang_data = self._enhance_language_detection(dataset_path)

        # 3. Detect known public datasets with 3% threshold
        public_datasets = self._detect_public_datasets_with_threshold(
            dataset_path, analysis
        )

        # 4. Add opt-out signals if requested
        opt_out_signals = {}
        if include_opt_out:
            opt_out_signals = self._check_opt_out_signals(dataset_path, analysis)

        # 5. Calculate training data size bands
        size_bands = self._calculate_size_bands(analysis)

        # 6. Determine if provider crawling occurred (for Section 2.3 gating)
        provider_crawling = self._detect_provider_crawling(analysis)

        # Extract modality info from analysis - fix mapping from analyzer format
        modalities_data = analysis.get("modalities", {})
        modalities_list = (
            modalities_data.get("values", [])
            if isinstance(modalities_data, dict)
            else []
        )

        # Convert file types to extensions
        extensions_raw = analysis.get("file_types", {}).get("values", {})
        extensions = {
            k: v for k, v in extensions_raw.items() if v >= 3
        }  # k-anonymity threshold

        # Get volume data
        volume = analysis.get("volume", {})

        # Format languages as list with percentages
        languages_list = []
        if isinstance(lang_data, dict):
            total = sum(lang_data.values())
            if total > 0:
                for lang, count in sorted(
                    lang_data.items(), key=lambda x: x[1], reverse=True
                ):
                    pct = round((count / total) * 100, 1)
                    if pct >= 0.1:  # Only include languages with >0.1%
                        languages_list.append({"lang": lang, "pct": pct})

        # Calculate token estimate for text with language-aware adjustment
        text_tokens_est = self._estimate_tokens(volume.get("bytes", 0), languages_list)

        # Format latest acquisition date with leading zeros (MM/YYYY)
        latest_mtime = volume.get("latest_mtime", None)
        latest_acquisition = "unknown"
        if latest_mtime:
            try:
                from datetime import datetime

                dt = datetime.fromisoformat(latest_mtime)
                # Ensure MM/YYYY format with leading zeros
                latest_acquisition = dt.strftime(
                    "%m/%Y"
                )  # %m gives 01-12 with leading zeros
            except:
                pass

        # Build standardized response matching Lambda expectations
        result = {
            "modalities_detected": {
                "text": "text" in modalities_list or "code" in modalities_list,
                "image": "image" in modalities_list,
                "audio": "audio" in modalities_list,
                "video": "video" in modalities_list,
                "other": "other" in modalities_list,
            },
            "sizes": {
                "text_tokens_est": text_tokens_est,
                "images_count": sum(
                    extensions_raw.get(ext, 0)
                    for ext in [
                        ".jpg",
                        ".jpeg",
                        ".png",
                        ".gif",
                        ".bmp",
                        ".svg",
                        ".webp",
                    ]
                ),
                "audio_hours_est": 0.0,  # TODO: Implement actual audio duration extraction
                "video_hours_est": 0.0,  # TODO: Implement actual video duration extraction
            },
            "volume": {
                "file_count": volume.get("files", 0),
                "total_bytes": volume.get("bytes", 0),
                "latest_acquisition_mm_yyyy": latest_acquisition,
            },
            "languages": languages_list,
            "known_public_datasets": public_datasets.get("detected", []),
            "large_public_datasets": public_datasets.get("large", []),
            "opt_out_summary": self._format_opt_out_summary(opt_out_signals),
            "provider_crawled_evidence": {
                "observed_domains": opt_out_signals.get("domains_checked", 0),
                "policy_signals_seen": opt_out_signals.get("opt_out_found", 0) > 0,
                "domains_top": [
                    {
                        "domain": ex.get("domain"),
                        "source": ex.get("source", "robots.txt"),
                    }
                    for ex in opt_out_signals.get("examples", [])[:5]
                ],
            },
            "tdm_meta": {
                "registry_source": "dev",
                "registry_version": (
                    self.registry.manifest.get("version", "unknown")
                    if hasattr(self.registry, "manifest") and self.registry.manifest
                    else "unknown"
                ),
                "entries": (
                    self.registry.manifest.get("count", 0)
                    if hasattr(self.registry, "manifest") and self.registry.manifest
                    else 0
                ),
            },
        }

        return result

    def _format_opt_out_summary(
        self, opt_out_signals: Dict[str, Any]
    ) -> Dict[str, Any]:
        """Format opt-out summary with proper deny/allow/no_signal counts."""
        domains_checked = opt_out_signals.get("domains_checked", 0)
        deny_count = opt_out_signals.get("opt_out_found", 0) + opt_out_signals.get(
            "suspect_found", 0
        )

        # Get example domains (max 5)
        examples = []
        for ex in opt_out_signals.get("examples", [])[:5]:
            if isinstance(ex, dict) and "domain" in ex:
                examples.append(ex.get("domain"))
            elif isinstance(ex, str):
                examples.append(ex)

        return {
            "domains_checked": domains_checked,
            "deny": deny_count,
            "allow": max(0, domains_checked - deny_count) if domains_checked > 0 else 0,
            "no_signal": 0,  # Could be tracked separately in future
            "sample_rate": 0.1,  # We use 10% sampling
            "signals": ["robots.txt", "ai.txt", "x-robots-tag", "trust.txt"],
            "examples": examples,
        }

    def _detect_modalities_from_extensions(
        self, extensions: Dict[str, int]
    ) -> Dict[str, bool]:
        """Detect modalities from file extensions."""
        modalities = {
            "text": False,
            "image": False,
            "audio": False,
            "video": False,
            "other": False,
        }

        # Extension to modality mapping
        text_exts = {".txt", ".md", ".json", ".jsonl", ".csv", ".tsv", ".xml", ".html"}
        image_exts = {".jpg", ".jpeg", ".png", ".gif", ".bmp", ".svg", ".webp", ".tiff"}
        audio_exts = {".mp3", ".wav", ".flac", ".ogg", ".m4a", ".aac", ".wma"}
        video_exts = {".mp4", ".avi", ".mov", ".mkv", ".webm", ".flv", ".wmv", ".mpg"}

        for ext in extensions:
            ext_lower = ext.lower()
            if ext_lower in text_exts:
                modalities["text"] = True
            elif ext_lower in image_exts:
                modalities["image"] = True
            elif ext_lower in audio_exts:
                modalities["audio"] = True
            elif ext_lower in video_exts:
                modalities["video"] = True
            else:
                modalities["other"] = True

        return modalities

    def _enhance_language_detection(
        self, dataset_path: str, sample_size: int = 500
    ) -> Dict[str, Any]:
        """
        Enhanced language detection sampling more files.

        Args:
            dataset_path: Path to dataset
            sample_size: Number of files to sample

        Returns:
            Language distribution with percentages
        """
        logger.info(f"Enhanced language detection: sampling up to {sample_size} files")

        # Use analyzer's existing method but with more samples
        path = Path(dataset_path)
        files = []

        # Collect text files
        for ext in ["*.txt", "*.md", "*.json", "*.jsonl", "*.csv", "*.html"]:
            files.extend(path.rglob(ext))
            if len(files) >= sample_size:
                break

        # Sample files
        files = files[:sample_size]

        # Use existing language detection
        if hasattr(self.analyzer, "_detect_languages_with_percentages"):
            return self.analyzer._detect_languages_with_percentages(files)
        else:
            # Fallback to basic detection
            return self.analyzer._detect_languages(files)

    def _detect_public_datasets_with_threshold(
        self,
        dataset_path: str,
        analysis: Dict[str, Any],
        use_global_comparison: bool = False,
    ) -> Dict[str, List[Dict[str, Any]]]:
        """
        Detect known public datasets and apply 3% threshold for "large" classification.

        By default, uses provider-relative calculation:
        A dataset is "large" if it represents ≥3% of provider's disclosed public datasets for that modality.

        If use_global_comparison=True, compares against global public totals.
        """
        # Load reference totals for 3% calculation
        import json
        from pathlib import Path as PathLib

        reference_file = (
            PathLib(__file__).parent.parent / "data" / "reference_public_totals.json"
        )
        reference_totals = {}

        try:
            if reference_file.exists():
                with open(reference_file) as f:
                    ref_data = json.load(f)
                    reference_totals = ref_data.get("totals", {})
                    known_datasets_info = ref_data.get("known_datasets", {})
            else:
                logger.warning(f"Reference file not found: {reference_file}")
                known_datasets_info = {}
        except Exception as e:
            logger.warning(f"Failed to load reference totals: {e}")
            known_datasets_info = {}

        # Known datasets with their typical characteristics
        KNOWN_DATASETS = {
            "pile": {
                "name": "The Pile",
                "link": "https://pile.eleuther.ai",
                "modality": "text",
            },
            "c4": {
                "name": "C4",
                "link": "https://www.tensorflow.org/datasets/catalog/c4",
                "modality": "text",
            },
            "commoncrawl": {
                "name": "Common Crawl",
                "link": "https://commoncrawl.org",
                "modality": "text",
            },
            "common_crawl": {
                "name": "Common Crawl",
                "link": "https://commoncrawl.org",
                "modality": "text",
            },
            "wikipedia": {
                "name": "Wikipedia",
                "link": "https://dumps.wikimedia.org",
                "modality": "text",
            },
            "openwebtext": {
                "name": "OpenWebText",
                "link": "https://github.com/jcpeterson/openwebtext",
                "modality": "text",
            },
            "bookcorpus": {
                "name": "BookCorpus",
                "link": "https://github.com/soskek/bookcorpus",
                "modality": "text",
            },
            "arxiv": {"name": "arXiv", "link": "https://arxiv.org", "modality": "text"},
            "cc-news": {
                "name": "CC-News",
                "link": "https://commoncrawl.org/2016/10/news-dataset-available/",
                "modality": "text",
            },
            "opensubtitles": {
                "name": "OpenSubtitles",
                "link": "https://opensubtitles.org",
                "modality": "text",
            },
            "imagenet": {
                "name": "ImageNet",
                "link": "https://image-net.org",
                "modality": "image",
            },
            "laion": {"name": "LAION", "link": "https://laion.ai", "modality": "image"},
            "coco": {
                "name": "MS-COCO",
                "link": "https://cocodataset.org",
                "modality": "image",
            },
            "librispeech": {
                "name": "LibriSpeech",
                "link": "https://www.openslr.org/12/",
                "modality": "audio",
            },
            "commonvoice": {
                "name": "Common Voice",
                "link": "https://commonvoice.mozilla.org",
                "modality": "audio",
            },
            "youtube-8m": {
                "name": "YouTube-8M",
                "link": "https://research.google.com/youtube8m/",
                "modality": "video",
            },
        }

        detected = []
        path_str = str(dataset_path).lower()

        # Check for dataset indicators in path or filenames
        for key, info in KNOWN_DATASETS.items():
            # Check in path or check for characteristic file patterns
            if key in path_str or (key.replace("_", "-") in path_str):
                dataset_info = info.copy()

                # Get known size from reference data if available
                modality = info["modality"]
                dataset_ref = known_datasets_info.get(modality, {}).get(key, {})

                if dataset_ref:
                    dataset_info["estimated_size"] = dataset_ref.get("bytes_est", 0)
                else:
                    # Fallback to actual size of this subset
                    dataset_info["estimated_size"] = analysis.get("volume", {}).get(
                        "bytes", 0
                    )

                # Calculate if it's "large" based on 3% threshold
                total_for_modality = reference_totals.get(modality, {}).get(
                    "total_public_bytes_est", 0
                )
                if modality == "image":
                    total_for_modality = reference_totals.get(modality, {}).get(
                        "total_public_count_est", 0
                    )
                elif modality in ["audio", "video"]:
                    total_for_modality = reference_totals.get(modality, {}).get(
                        "total_public_hours_est", 0
                    )

                # Store size info for later calculation
                dataset_info["estimated_size"] = dataset_info.get("estimated_size", 0)
                detected.append(dataset_info)

        # Calculate relative percentages and determine "large" status
        if use_global_comparison and reference_totals:
            # Global comparison mode (optional)
            for ds in detected:
                modality = ds["modality"]
                total_for_modality = reference_totals.get(modality, {}).get(
                    "total_public_bytes_est", 0
                )
                if modality == "image":
                    total_for_modality = reference_totals.get(modality, {}).get(
                        "total_public_count_est", 0
                    )
                elif modality in ["audio", "video"]:
                    total_for_modality = reference_totals.get(modality, {}).get(
                        "total_public_hours_est", 0
                    )

                if total_for_modality > 0:
                    percentage = (ds["estimated_size"] / total_for_modality) * 100
                    ds["est_share_pct"] = round(percentage, 1)
                    ds["is_large"] = percentage >= 3.0
                    ds["large_reason"] = f"≥3% of global public {modality} corpus"
                else:
                    ds["est_share_pct"] = 0.0
                    ds["is_large"] = False
        else:
            # Provider-relative calculation (default)
            # Group by modality and calculate total per modality
            modality_totals = {}
            for ds in detected:
                modality = ds["modality"]
                if modality not in modality_totals:
                    modality_totals[modality] = 0
                modality_totals[modality] += ds.get("estimated_size", 0)

            # Calculate relative percentages
            for ds in detected:
                modality = ds["modality"]
                total_for_modality = modality_totals.get(modality, 0)

                if total_for_modality > 0:
                    percentage = (ds["estimated_size"] / total_for_modality) * 100
                    ds["est_share_pct"] = round(percentage, 1)
                    ds["is_large"] = percentage >= 3.0
                    ds["large_reason"] = f"≥3% of disclosed public {modality} datasets"
                else:
                    ds["est_share_pct"] = 0.0
                    ds["is_large"] = False

        # Split into regular and large datasets
        regular = []
        large = []

        for ds in detected:
            formatted_ds = {
                "name": ds["name"],
                "link": ds["link"],
                "modality": [ds["modality"]],  # As list per contract
                "est_share_pct": ds.get("est_share_pct", 0.0),
            }

            if ds.get("is_large", False):
                formatted_ds["reason"] = ds.get(
                    "large_reason", "≥3% of disclosed public datasets"
                )
                large.append(formatted_ds)
            else:
                regular.append(formatted_ds)

        return {"detected": regular, "large": large}

    def _check_opt_out_signals(
        self, dataset_path: str, analysis: Dict[str, Any]
    ) -> Dict[str, Any]:
        """
        Check for TDM opt-out signals using existing DatasetScanner.

        Returns:
            Dictionary with opt-out statistics
        """
        logger.info("Checking TDM opt-out signals")

        # Use preflight scanner for opt-out checking
        path = Path(dataset_path)

        # Run scanner with 30 second budget
        signals = self.preflight.scan(
            dataset_path=path,
            registry=self.registry,
            budget_seconds=30,
            network_tracker={"used_ms": 0, "calls": 0},
            no_network=False,
        )

        # Extract opt-out information
        opt_out = signals.get("opt_out", {})

        # Format for SDS
        result = {
            "domains_checked": len(analysis.get("domains", {}).get("values", [])),
            "opt_out_found": opt_out.get("summary", {}).get("deny", 0),
            "suspect_found": opt_out.get("summary", {}).get("suspect", 0),
            "examples": [],
        }

        # Add examples (domain only, no sensitive data)
        for domain_info in opt_out.get("deny_domains", [])[:5]:
            result["examples"].append(
                {
                    "domain": domain_info.get("domain"),
                    "source": domain_info.get("source", "robots.txt"),
                }
            )

        return result

    def _calculate_size_bands(self, analysis: Dict[str, Any]) -> Dict[str, str]:
        """
        Calculate size bands for each modality according to EU template.

        Text: <1B tokens, 1B-10T tokens, >10T tokens
        Image: <1M images, 1M-1B images, >1B images
        Audio/Video: <10K hours, 10K-1M hours, >1M hours
        """
        bands = {}
        volume = analysis.get("volume", {})

        # Text band (using token estimate)
        tokens = volume.get("estimated_tokens", 0)
        if tokens < 1_000_000_000:
            bands["text"] = "<1B tokens"
        elif tokens < 10_000_000_000_000:
            bands["text"] = "1B-10T tokens"
        else:
            bands["text"] = ">10T tokens"

        # Image band (would need actual image counting)
        # For now, estimate from file types
        image_count = sum(
            analysis.get("file_types", {}).get("values", {}).get(ext, 0)
            for ext in [".jpg", ".jpeg", ".png", ".gif", ".bmp"]
        )
        if image_count < 1_000_000:
            bands["image"] = "<1M images"
        elif image_count < 1_000_000_000:
            bands["image"] = "1M-1B images"
        else:
            bands["image"] = ">1B images"

        # Audio/Video bands (would need duration extraction)
        # For MVP, mark as "Not known" unless we can extract
        bands["audio"] = "Not known"
        bands["video"] = "Not known"

        return bands

    def _estimate_tokens(
        self, total_bytes: int, languages: List[Dict[str, Any]]
    ) -> int:
        """
        Estimate token count based on byte size and detected languages.

        Uses language-specific heuristics:
        - CJK languages (Chinese, Japanese, Korean): ~0.5 tokens per byte
        - Latin scripts: ~0.25 tokens per byte (4 bytes per token)
        - Mixed/unknown: weighted average based on language percentages
        """
        # Try to use tiktoken if available
        try:
            import tiktoken

            # If tiktoken is available, we could sample files and get exact counts
            # For now, still use heuristics but note tiktoken is available
            logger.info("tiktoken available for more accurate token counting")
        except ImportError:
            pass

        if not languages:
            # Default assumption: mostly English/Latin text
            return total_bytes // 4

        # CJK languages that typically have higher byte-to-token ratios
        cjk_languages = {"zh", "ja", "ko", "chinese", "japanese", "korean"}

        # Calculate weighted average tokens per byte
        total_pct = 0
        weighted_tpb = 0  # tokens per byte

        for lang_info in languages:
            lang = lang_info.get("lang", "").lower()
            pct = lang_info.get("pct", 0) / 100.0  # Convert percentage to fraction

            if lang in cjk_languages:
                # CJK: approximately 2 bytes per token
                tokens_per_byte = 0.5
            elif lang in ["ar", "he", "fa", "ur"]:  # Arabic, Hebrew, Persian, Urdu
                # RTL scripts: approximately 3 bytes per token
                tokens_per_byte = 0.33
            else:
                # Latin and other scripts: approximately 4 bytes per token
                tokens_per_byte = 0.25

            weighted_tpb += tokens_per_byte * pct
            total_pct += pct

        # Handle any remaining percentage (unknown languages)
        if total_pct < 1.0:
            remaining_pct = 1.0 - total_pct
            weighted_tpb += 0.25 * remaining_pct  # Assume Latin for unknown

        # Calculate final token estimate
        estimated_tokens = int(total_bytes * weighted_tpb)

        logger.debug(
            f"Token estimation: {total_bytes} bytes → {estimated_tokens} tokens "
            f"(weighted TPB: {weighted_tpb:.3f})"
        )

        return estimated_tokens

    def _detect_provider_crawling(self, analysis: Dict[str, Any]) -> bool:
        """
        Detect if provider crawling occurred (for Section 2.3 gating).

        Provider crawling = web crawling by provider, NOT using public datasets.
        """
        # Check for crawling indicators
        has_domains = bool(analysis.get("domains", {}).get("values"))

        # Check if domains are from known public datasets
        public_datasets = analysis.get("public_datasets", [])
        is_public_dataset = any(
            ds["name"] in ["Common Crawl", "C4", "OpenWebText"]
            for ds in public_datasets
        )

        # Provider crawling = has domains but NOT from public datasets
        return has_domains and not is_public_dataset
