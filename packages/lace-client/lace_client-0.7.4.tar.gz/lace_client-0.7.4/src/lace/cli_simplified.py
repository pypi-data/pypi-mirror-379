"""
Simplified cloud-only pack command for Lace CLI.
"""

import base64
import hashlib
import json
import logging
import os
import sys
import tempfile
import time
import uuid
import webbrowser
import zipfile
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Optional

import click

# Suppress verbose logging
logging.getLogger("lace").setLevel(logging.WARNING)
logging.getLogger("httpx").setLevel(logging.WARNING)

# Exit codes
EXIT_SUCCESS = 0
EXIT_GENERAL_ERROR = 1
EXIT_CLIENT_ERROR = 2
EXIT_SERVER_ERROR = 3
EXIT_VALIDATION_ERROR = 4
EXIT_USER_ABORT = 5


def get_dataset_metadata(dataset_path: str) -> Dict[str, Any]:
    """
    Get basic metadata about a dataset without scanning content.

    Args:
        dataset_path: Path to dataset

    Returns:
        Basic metadata dict with file count and size
    """
    path = Path(dataset_path)
    if not path.exists():
        raise ValueError(f"Dataset path does not exist: {dataset_path}")

    total_files = 0
    total_bytes = 0
    extensions = {}

    # Simple walk through dataset
    for root, dirs, files in os.walk(path):
        for file in files:
            total_files += 1
            file_path = Path(root) / file
            try:
                total_bytes += file_path.stat().st_size
                ext = file_path.suffix.lower()
                if ext:
                    extensions[ext] = extensions.get(ext, 0) + 1
            except:
                pass  # Skip files we can't access

    # Get top extensions
    top_extensions = dict(
        sorted(extensions.items(), key=lambda x: x[1], reverse=True)[:5]
    )

    return {
        "dataset_path": str(path.absolute()),
        "file_count": total_files,
        "total_bytes": total_bytes,
        "total_gb": round(total_bytes / (1024**3), 2),
        "extensions": top_extensions,
    }


def format_bytes(num_bytes):
    """Format bytes as human-readable size."""
    for unit in ["B", "KB", "MB", "GB", "TB"]:
        if num_bytes < 1024.0:
            return f"{num_bytes:.1f} {unit}"
        num_bytes /= 1024.0
    return f"{num_bytes:.1f} PB"


def format_number(num):
    """Format large numbers with abbreviations."""
    if num < 1000:
        return str(num)
    elif num < 1_000_000:
        return f"{num/1000:.1f}K"
    elif num < 1_000_000_000:
        return f"{num/1_000_000:.1f}M"
    else:
        return f"{num/1_000_000_000:.1f}B"


def simplified_pack_cmd(dataset_path, yes, format, out, answers, open_after, bundle):
    """
    Simplified cloud-only SDS generation flow.

    1. Get basic dataset metadata
    2. Send to cloud for analysis
    3. Get questions back
    4. Answer questions (with AI suggestions)
    5. Generate SDS
    """
    try:
        from lace.cloud import LaceCloudAPI
        from lace.sds import validate_answer

        # 1. Get basic dataset metadata
        click.echo(f"\nAnalyzing dataset: {dataset_path}")
        with click.progressbar(
            length=100,
            label="Preparing",
            show_percent=True,
            width=40,
            fill_char="━",
            empty_char="━",
        ) as bar:
            bar.update(20)
            metadata = get_dataset_metadata(dataset_path)
            bar.update(80)

        # Show clean summary
        click.echo("\nDataset Summary:")
        click.echo(f"  • Files: {metadata['file_count']:,}")
        click.echo(f"  • Total size: {format_bytes(metadata['total_bytes'])}")
        if metadata["extensions"]:
            ext_str = ", ".join(
                [
                    f"{k.upper()}({v})"
                    for k, v in list(metadata["extensions"].items())[:3]
                ]
            )
            click.echo(f"  • File types: {ext_str}")

        # 2. Initialize API client
        try:
            api = LaceCloudAPI()
        except Exception as e:
            click.echo(f"\n❌ {e}", err=True)
            click.echo("Run: export LACE_API_KEY=lace_sk_...", err=True)
            sys.exit(EXIT_VALIDATION_ERROR)

        # 3. Load previous session for AI suggestions
        session_cache_dir = Path.home() / ".lace" / "sessions"
        session_cache_dir.mkdir(parents=True, exist_ok=True)
        last_answers_file = session_cache_dir / "last_answers.json"

        previous_answers = {}
        provider_hints = {}

        if last_answers_file.exists():
            try:
                with open(last_answers_file) as f:
                    cached = json.load(f)
                    if "timestamp" in cached:
                        age_seconds = (
                            datetime.now() - datetime.fromisoformat(cached["timestamp"])
                        ).total_seconds()
                        if age_seconds < 30 * 24 * 3600:  # 30 days
                            previous_answers = cached.get("answers", {})
                            provider_hints = {
                                "previous_answers": previous_answers,
                                "current_date": datetime.now().strftime("%m/%Y"),
                            }
            except:
                pass  # Ignore cache errors

        # 4. Send metadata to cloud and get questions
        click.echo("\n🤖 Analyzing in secure cloud environment...")
        click.echo("   (No data is stored - analysis only)")

        try:
            # Send basic metadata to cloud - cloud will do the full analysis
            local_facts = {
                "dataset_metadata": metadata,
                "analysis_requested": True,  # Tell cloud to do full analysis
            }

            prepare_resp = api.prepare_sds(local_facts, provider_hints=provider_hints)
            session_id = prepare_resp.get("session_id")
            questions = prepare_resp.get("questions", [])

            # Extract AI suggestions from question defaults
            ai_suggestions = {}
            for q in questions:
                if q.get("ai_suggested") and q.get("default"):
                    ai_suggestions[q["id"]] = q["default"]

        except Exception as e:
            click.echo(f"\n❌ Error preparing SDS: {str(e)}", err=True)
            sys.exit(EXIT_SERVER_ERROR)

        # 5. Handle answers - from file or interactive
        if answers and yes:
            # Load from file
            try:
                with open(answers, "r") as f:
                    answers = json.load(f)
                click.echo(f"\n✅ Loaded {len(answers)} answers from file")
            except Exception as e:
                click.echo(f"❌ Failed to load answers: {e}")
                sys.exit(EXIT_CLIENT_ERROR)
        else:
            # Interactive Q&A
            if ai_suggestions and previous_answers:
                click.echo(
                    f"\n📝 Review AI-suggested answers ({len(questions)} questions):"
                )
                click.echo("Press Enter to accept suggestions, or type new values")
            else:
                click.echo(f"\n📝 Please answer {len(questions)} questions:")
            click.echo("=" * 50)

            answers = {}
            for i, question in enumerate(questions, 1):
                q_id = question.get("id")
                q_text = question.get("text", q_id)
                q_type = question.get("type", "text")
                q_help = question.get("help", "")

                # Get default value
                default = None
                if q_id in ai_suggestions:
                    default = ai_suggestions[q_id]
                elif q_id in previous_answers:
                    default = previous_answers[q_id]
                elif question.get("default"):
                    default = question.get("default")
                elif q_id == "date_market_mm_yyyy":
                    default = datetime.now().strftime("%m/%Y")

                # Add examples for common questions
                example_text = ""
                examples = {
                    "provider_name": "e.g., 'OpenAI Inc.' or 'Acme AI Labs'",
                    "provider_contact": "e.g., 'legal@example.com'",
                    "model_names": "e.g., 'GPT-4' or 'LLaMA-2-70B'",
                    "date_market_mm_yyyy": "e.g., '09/2025'",
                }
                if q_id in examples and not default:
                    example_text = f"\n    💡 Example: {examples[q_id]}"

                # Show question
                click.echo(f"\n[{i}/{len(questions)}] {q_text}")
                if q_help:
                    click.echo(f"    ℹ️  {q_help}")
                if example_text:
                    click.echo(example_text)

                # Get answer based on type
                if q_type in ["boolean", "yesno"]:
                    answer = click.confirm(
                        "   ", default=bool(default) if default else False
                    )
                    answer = "yes" if answer else "no"
                elif q_type == "textarea":
                    click.echo("    (Enter multiple lines, end with empty line)")
                    lines = []
                    while True:
                        line = click.prompt("   ", default="", show_default=False)
                        if not line:
                            break
                        lines.append(line)
                    answer = "\n".join(lines) if lines else (default or "")
                elif q_type in ["date-ym", "date_mm_yyyy"]:
                    while True:
                        answer = click.prompt(
                            "    (MM/YYYY)", type=str, default=default or ""
                        )
                        if answer:
                            import re

                            if re.match(r"^(0[1-9]|1[0-2])/\d{4}$", answer):
                                break
                            else:
                                click.echo("    ⚠️  Please use MM/YYYY format")
                        elif not question.get("required", True):
                            break
                else:
                    # Text input
                    answer = click.prompt("   ", type=str, default=default or "")

                answers[q_id] = answer

            # Save answers for future use
            try:
                last_answers_cache = {
                    "answers": answers,
                    "timestamp": datetime.now().isoformat(),
                    "dataset_hash": hashlib.md5(str(dataset_path).encode()).hexdigest(),
                }
                with open(last_answers_file, "w") as f:
                    json.dump(last_answers_cache, f, indent=2)
            except:
                pass  # Ignore cache save errors

        # Show summary
        click.echo("\n" + "=" * 50)
        click.echo("📋 Summary:")
        click.echo(f"  Provider: {answers.get('provider_name', 'Not provided')}")
        click.echo(f"  Model: {answers.get('model_names', 'Not provided')}")
        click.echo(
            f"  Placed on market: {answers.get('date_market_mm_yyyy', 'Not provided')}"
        )

        if not click.confirm("\nProceed with SDS generation?"):
            click.echo("Aborted by user.")
            sys.exit(EXIT_USER_ABORT)

        # 6. Generate SDS
        click.echo("\n🚀 Generating SDS documents...")
        output_dir = Path(out)
        output_dir.mkdir(parents=True, exist_ok=True)

        try:
            # Send to cloud for generation
            with click.progressbar(
                length=100,
                label="Generating",
                show_percent=True,
                width=40,
                fill_char="━",
                empty_char="━",
            ) as bar:
                bar.update(30)
                sds_resp = api.generate_sds(
                    session_id=session_id,
                    answers=answers,
                    format=format,
                    local_facts=local_facts,  # Cloud has the analysis
                )
                bar.update(70)

        except Exception as e:
            error_msg = str(e)
            try:
                if hasattr(e, "response") and hasattr(e.response, "json"):
                    error_data = e.response.json()
                    click.echo("\n❌ Error generating SDS:", err=True)
                    click.echo(
                        f"  Code: {error_data.get('error_code', 'UNKNOWN')}", err=True
                    )
                    click.echo(
                        f"  Message: {error_data.get('message', error_msg)}", err=True
                    )
                else:
                    click.echo(f"\n❌ Error generating SDS: {error_msg}", err=True)
            except:
                click.echo(f"\n❌ Error generating SDS: {error_msg}", err=True)
            sys.exit(EXIT_SERVER_ERROR)

        # 7. Save outputs
        if format == "docx":
            eu_sds_path = output_dir / "eu_sds.docx"
            with open(eu_sds_path, "wb") as f:
                f.write(base64.b64decode(sds_resp.get("docx_b64", "")))
        else:
            eu_sds_path = output_dir / "eu_sds.md"
            with open(eu_sds_path, "w") as f:
                f.write(sds_resp.get("markdown", ""))

        click.echo(f"\n✅ Generated: {eu_sds_path}")

        # Save metadata
        metadata_path = output_dir / "eu_sds.json"
        with open(metadata_path, "w") as f:
            json.dump(
                {
                    "session_id": session_id,
                    "generated_at": sds_resp.get("generated_at"),
                    "provider": answers.get("provider_name"),
                    "model": answers.get("model_names"),
                    "date_market": answers.get("date_market_mm_yyyy"),
                },
                f,
                indent=2,
            )

        # Create bundle if requested
        if bundle:
            bundle_name = f"sds_bundle_{datetime.now().strftime('%Y%m%d_%H%M%S')}.zip"
            bundle_path = output_dir / bundle_name

            with zipfile.ZipFile(bundle_path, "w", zipfile.ZIP_DEFLATED) as zf:
                zf.write(eu_sds_path, eu_sds_path.name)
                zf.write(metadata_path, metadata_path.name)

                # Add domains CSV if provided
                if "domains_csv" in sds_resp:
                    domains_path = output_dir / "domains_top.csv"
                    domains_path.write_text(sds_resp["domains_csv"])
                    zf.write(domains_path, domains_path.name)

            click.echo(f"✅ Bundle created: {bundle_path}")

        # Open if requested
        if open_after and format == "docx":
            import platform

            if platform.system() == "Darwin":
                os.system(f'open "{eu_sds_path}"')
            elif platform.system() == "Windows":
                os.startfile(eu_sds_path)
            else:
                webbrowser.open(f"file://{eu_sds_path}")

        click.echo("\n✨ SDS generation complete!")

    except Exception as e:
        click.echo(f"\n❌ Unexpected error: {e}", err=True)
        import traceback

        traceback.print_exc()
        sys.exit(EXIT_GENERAL_ERROR)
