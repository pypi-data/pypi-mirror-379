"""
OpenAI proxy for GPT-5 attribution via Lace cloud endpoint.
Requires explicit consent and uses deterministic prompts.
"""

import asyncio
import hashlib
import json
import logging
import os
import time
from collections import Counter
from datetime import datetime, timedelta
from typing import Any, Dict, List, Optional

try:
    import httpx
except ImportError:
    raise ImportError("Please install httpx: pip install httpx")

logger = logging.getLogger(__name__)


class AttributionProxy:
    """GPT attribution via Lace cloud proxy."""

    # Deterministic system prompt
    SYSTEM_PROMPT = """You are a compliance attribution assistant. Return most likely source domains for the provided redacted content. Never output URLs beyond domain+TLD. Calibrate confidence strictly. Output JSON array only."""

    # Track budget usage across all calls
    _total_calls_attempted = 0
    _total_calls_made = 0
    _total_calls_skipped = 0
    _latencies = []  # Track call latencies for p50/p95
    _skip_reasons = Counter()  # Track skip reasons with Counter
    _failure_reasons = Counter()  # Track failure reasons with Counter for diagnostics
    _model_validated = False  # Lazy model validation flag
    _response_ids = []  # Track all OpenAI response IDs for provenance

    # Token budget tracking
    _total_input_tokens = 0
    _total_output_tokens = 0
    MAX_CALLS_PER_RUN = int(os.environ.get("LACE_MAX_CALLS", 25))
    MAX_TOTAL_TOKENS_PER_RUN = int(os.environ.get("LACE_MAX_TOKENS", 50000))

    def __init__(
        self,
        api_url: Optional[str] = None,
        api_key: Optional[str] = None,
        timeout: float = 30.0,
        max_retries: int = 3,
        initial_backoff: float = 1.0,
    ):
        """
        Initialize attribution proxy.

        Args:
            api_url: Lace API URL (or from LACE_API_URL env)
            api_key: Lace API key (or from LACE_API_KEY env)
            timeout: Request timeout in seconds
            max_retries: Maximum retry attempts
            initial_backoff: Initial backoff time for retries
        """
        # Get API configuration
        self.api_url = api_url or os.environ.get(
            "LACE_API_URL",
            "https://usgf90tw68.execute-api.eu-west-1.amazonaws.com/prod",
        )
        self.api_key = api_key or os.environ.get("LACE_API_KEY")

        if not self.api_key:
            logger.warning("No LACE_API_KEY found - attribution will not be available")

        self.timeout = timeout
        self.max_retries = max_retries
        self.initial_backoff = initial_backoff

        # Circuit breaker state
        self.circuit_open = False
        self.circuit_open_until = None
        self.consecutive_failures = 0
        self.circuit_threshold = 5  # Open circuit after 5 consecutive failures
        self.circuit_cooldown = 300  # 5 minutes

        # Model validation state
        self._model_validated = False

    def _check_circuit(self) -> bool:
        """
        Check if circuit breaker is open.

        Returns:
            True if circuit is open (requests should be blocked)
        """
        if not self.circuit_open:
            return False

        # Check if cooldown period has passed
        if datetime.utcnow() > self.circuit_open_until:
            logger.info("Circuit breaker reset - allowing requests")
            self.circuit_open = False
            self.consecutive_failures = 0
            return False

        return True

    def _open_circuit(self):
        """Open the circuit breaker."""
        self.circuit_open = True
        self.circuit_open_until = datetime.utcnow() + timedelta(
            seconds=self.circuit_cooldown
        )
        logger.warning(
            f"Circuit breaker opened - blocking requests for {self.circuit_cooldown}s"
        )

    def _record_success(self, latency_ms: float = None):
        """Record successful request."""
        self.consecutive_failures = 0
        if self.circuit_open:
            logger.info("Circuit breaker closed after successful request")
            self.circuit_open = False
        if latency_ms is not None:
            AttributionProxy._latencies.append(latency_ms)

    def _record_failure(self, reason: str = None):
        """Record failed request with optional reason."""
        self.consecutive_failures += 1
        if reason:
            AttributionProxy._failure_reasons[reason] += 1
        if self.consecutive_failures >= self.circuit_threshold:
            self._open_circuit()

    async def attribute(
        self,
        snippet: str,
        language_hint: Optional[str] = None,
        candidate_domains: Optional[List[str]] = None,
        consent_confirmed: bool = False,
    ) -> List[Dict[str, Any]]:
        """
        Get attribution for a redacted snippet via GPT.

        Args:
            snippet: Redacted text snippet (≤1KB)
            language_hint: Optional language code
            candidate_domains: Optional list of candidate domains
            consent_confirmed: Must be True to proceed

        Returns:
            List of attribution results with domains and confidence
        """
        # Enforce consent
        if not consent_confirmed:
            logger.error("Attribution requires explicit consent (--consent-snippets)")
            return []

        # Check for direct OpenAI mode
        attribution_mode = os.environ.get("LACE_ATTRIBUTION_MODE", "proxy")
        openai_api_key = os.environ.get("OPENAI_API_KEY")

        if attribution_mode == "direct" and openai_api_key:
            logger.info("Using direct OpenAI mode for attribution")
            return await self._call_openai_direct(
                snippet, language_hint, candidate_domains
            )

        # Check prerequisites for proxy mode
        if not self.api_key:
            logger.debug("No LACE API key available for attribution")
            AttributionProxy._skip_reasons["missing_lace_api_key"] += 1
            return [{"gpt_skipped": True, "skip_reason": "missing_lace_api_key"}]

        # Check circuit breaker
        if self._check_circuit():
            logger.debug("Circuit breaker open - skipping attribution")
            AttributionProxy._total_calls_skipped += 1
            AttributionProxy._skip_reasons["circuit_open"] += 1
            return []

        # Verify snippet is redacted and within size limit
        if len(snippet.encode("utf-8")) > 1024:
            logger.warning("Snippet exceeds 1KB limit")
            snippet = snippet[:1024]

        # Log SHA256 only (never log content)
        snippet_hash = hashlib.sha256(snippet.encode("utf-8")).hexdigest()
        logger.debug(f"Attributing snippet SHA256: {snippet_hash}")

        # Track call start time
        start_time = time.time()

        # Build request payload
        payload = {
            "sha256": snippet_hash,
            "snippet": snippet,
            "consent_snippets": consent_confirmed,
            "domain_hints": candidate_domains[:10] if candidate_domains else [],
        }

        # Attempt request with retries
        # Track attempt
        AttributionProxy._total_calls_attempted += 1

        backoff = self.initial_backoff
        last_error = None

        for attempt in range(self.max_retries):
            try:
                async with httpx.AsyncClient(timeout=self.timeout) as client:
                    response = await client.post(
                        f"{self.api_url}/api/check/attribute",
                        json=payload,
                        headers={
                            "Authorization": f"Bearer {self.api_key}",
                            "Content-Type": "application/json",
                        },
                    )

                    # Check for model mismatch
                    if response.status_code == 422:
                        error_data = response.json()
                        if error_data.get("error") == "model_not_allowed":
                            required = error_data.get("required_model", "gpt-5")
                            received = error_data.get("model_received", "(unknown)")
                            AttributionProxy._total_calls_skipped += 1
                            AttributionProxy._skip_reasons["model_not_allowed"] += 1
                            logger.warning(
                                f"Model mismatch: expected {required}, got {received}. Update AWS secret lace/prod/openai and retry."
                            )
                            return []

                    # Check status
                    elif response.status_code == 200:
                        result = response.json()
                        # Calculate latency
                        latency_ms = (time.time() - start_time) * 1000
                        self._record_success(latency_ms)

                        # Track usage metrics and response IDs
                        if "usage" in result:
                            usage = result["usage"]
                            if "calls_made" in usage:
                                AttributionProxy._total_calls_made = usage["calls_made"]
                            if "calls_skipped" in usage:
                                AttributionProxy._total_calls_skipped = usage[
                                    "calls_skipped"
                                ]

                        # Track response ID from proxy if available
                        if "response_id" in result:
                            response_id = result["response_id"]
                            if (
                                response_id
                                and response_id not in AttributionProxy._response_ids
                            ):
                                AttributionProxy._response_ids.append(response_id)
                        elif "openai_response_id" in result:
                            response_id = result["openai_response_id"]
                            if (
                                response_id
                                and response_id not in AttributionProxy._response_ids
                            ):
                                AttributionProxy._response_ids.append(response_id)

                        # Check if budget was exceeded or rate limited
                        if result.get("gpt_skipped"):
                            reason = result.get("reason", "budget_limit")
                            logger.info(f"Attribution skipped: {reason}")
                            AttributionProxy._total_calls_skipped += 1
                            return [{"gpt_skipped": True, "reason": reason}]

                        # Validate and normalize response
                        if isinstance(result, dict) and "gpt_sources" in result:
                            sources = result["gpt_sources"]
                        elif isinstance(result, dict) and "top_sources" in result:
                            sources = result["top_sources"]
                        else:
                            sources = result if isinstance(result, list) else []

                        # Ensure proper format
                        normalized = []
                        for source in sources:
                            if isinstance(source, dict) and "domain" in source:
                                normalized.append(
                                    {
                                        "domain": source["domain"],
                                        "confidence": float(
                                            source.get("confidence", 0.5)
                                        ),
                                        "evidence": source.get("evidence", ""),
                                    }
                                )

                        return normalized

                    elif response.status_code == 429:
                        # Rate limited - track as skipped
                        logger.warning("Rate limited by attribution API")
                        self._record_failure("rate_limit")
                        AttributionProxy._total_calls_skipped += 1
                        AttributionProxy._skip_reasons["rate_limit"] += 1

                        # Check for Retry-After header
                        retry_after = response.headers.get("Retry-After")
                        if retry_after:
                            backoff = float(retry_after)

                        last_error = "Rate limited (429)"

                    elif response.status_code >= 500:
                        # Server error - track as skipped
                        logger.warning(
                            f"Server error from attribution API: {response.status_code}"
                        )
                        self._record_failure(f"server_error_{response.status_code}")
                        AttributionProxy._total_calls_skipped += 1
                        AttributionProxy._skip_reasons["server_error"] += 1
                        last_error = f"Server error ({response.status_code})"

                    else:
                        # Client error - don't retry
                        logger.error(
                            f"Client error from attribution API: {response.status_code}"
                        )
                        self._record_failure(f"client_error_{response.status_code}")
                        return []

            except httpx.TimeoutException:
                logger.warning(f"Attribution request timeout (attempt {attempt + 1})")
                self._record_failure("timeout")
                last_error = "Timeout"

            except Exception as e:
                logger.warning(f"Attribution request failed: {e}")
                self._record_failure(reason=str(e)[:50])  # Truncate reason
                last_error = str(e)

            # Wait before retry (except on last attempt)
            if attempt < self.max_retries - 1:
                logger.debug(f"Retrying in {backoff}s...")
                time.sleep(backoff)
                backoff = min(backoff * 2, 60)  # Exponential backoff with cap

        logger.warning(
            f"Attribution failed after {self.max_retries} attempts: {last_error}"
        )
        return []

    @classmethod
    def get_budget_summary(cls) -> str:
        """Get budget usage summary with latency metrics."""
        made = cls._total_calls_made
        skipped = cls._total_calls_skipped

        # Calculate latency percentiles if we have data
        latency_info = ""
        if cls._latencies:
            sorted_latencies = sorted(cls._latencies)
            p50_idx = len(sorted_latencies) // 2
            p95_idx = int(len(sorted_latencies) * 0.95)
            p50 = sorted_latencies[p50_idx]
            p95 = (
                sorted_latencies[p95_idx]
                if p95_idx < len(sorted_latencies)
                else sorted_latencies[-1]
            )
            latency_info = f", p50={p50:.0f}ms, p95={p95:.0f}ms"

        # Include failure reasons if any
        failure_info = ""
        if cls._failure_reasons:
            top_reason = max(cls._failure_reasons.items(), key=lambda x: x[1])
            failure_info = f" (top failure: {top_reason[0]})"

        if made > 0 or skipped > 0:
            return f"GPT attribution: {made} made, {skipped} skipped{latency_info}{failure_info}"
        return ""

    @classmethod
    def get_metrics(cls) -> Dict[str, Any]:
        """Get detailed metrics for reporting."""
        metrics = {
            "calls_attempted": cls._total_calls_attempted,
            "calls_made": cls._total_calls_made,
            "calls_skipped": cls._total_calls_skipped,
            "skip_reasons": dict(cls._skip_reasons),  # Convert Counter to dict
            "failure_reasons": dict(cls._failure_reasons),  # Include failure reasons
            "latencies": cls._latencies,
        }

        # Add percentiles if we have data
        if cls._latencies:
            sorted_latencies = sorted(cls._latencies)
            p50_idx = len(sorted_latencies) // 2
            p95_idx = int(len(sorted_latencies) * 0.95)
            metrics["p50_ms"] = sorted_latencies[p50_idx]
            metrics["p95_ms"] = (
                sorted_latencies[p95_idx]
                if p95_idx < len(sorted_latencies)
                else sorted_latencies[-1]
            )

        return metrics

    async def _call_openai_direct(
        self,
        snippet: str,
        language_hint: Optional[str] = None,
        candidate_domains: Optional[List[str]] = None,
    ) -> List[Dict[str, Any]]:
        """
        Call OpenAI directly without going through Lace proxy.

        Args:
            snippet: Redacted text snippet
            language_hint: Optional language code
            candidate_domains: Optional list of candidate domains

        Returns:
            List of attribution results
        """
        # Check call budget
        if AttributionProxy._total_calls_made >= AttributionProxy.MAX_CALLS_PER_RUN:
            logger.info(
                f"Call budget limit reached ({AttributionProxy.MAX_CALLS_PER_RUN} calls)"
            )
            AttributionProxy._skip_reasons["budget_limit_calls"] += 1
            return [{"gpt_skipped": True, "skip_reason": "budget_limit_calls"}]

        # Check token budget
        if (
            AttributionProxy._total_input_tokens + AttributionProxy._total_output_tokens
            >= AttributionProxy.MAX_TOTAL_TOKENS_PER_RUN
        ):
            logger.info(
                f"Token budget limit reached ({AttributionProxy.MAX_TOTAL_TOKENS_PER_RUN} tokens)"
            )
            AttributionProxy._skip_reasons["budget_limit_tokens"] += 1
            return [{"gpt_skipped": True, "skip_reason": "budget_limit_tokens"}]

        try:
            # Import OpenAI client
            try:
                from openai import AsyncOpenAI
            except ImportError:
                logger.error("OpenAI library not installed. Run: pip install openai")
                AttributionProxy._skip_reasons["missing_openai_lib"] += 1
                return [{"gpt_skipped": True, "skip_reason": "missing_openai_lib"}]

            # Check for API key
            api_key = os.environ.get("OPENAI_API_KEY")
            if not api_key:
                logger.debug("No OPENAI_API_KEY found")
                AttributionProxy._skip_reasons["missing_openai_key"] += 1
                return [{"gpt_skipped": True, "skip_reason": "missing_openai_key"}]

            # Initialize client
            client = AsyncOpenAI(api_key=api_key)

            # Build structured prompt for better JSON response
            prompt = """Analyze this redacted text snippet and identify likely source domains.
Return a JSON object with this exact structure:
{
  "domains": ["example.com", "another.com"],
  "confidence": 0.85,
  "licenses": ["MIT", "Apache-2.0"],
  "citations": []
}

Text snippet"""
            if language_hint:
                prompt += f" (language: {language_hint})"
            if candidate_domains:
                prompt += (
                    f". Consider these domains: {', '.join(candidate_domains[:5])}"
                )
            prompt += f":\n\n{snippet[:1000]}"

            # Track attempt
            AttributionProxy._total_calls_attempted += 1
            start_time = time.time()

            # Get model from env or use default
            model = os.environ.get("LACE_ATTRIBUTION_MODEL", "gpt-4o-mini")

            # Implement retry logic with exponential backoff
            max_retries = 3
            backoff = 1.0
            last_error = None

            for attempt in range(max_retries):
                try:
                    # Call OpenAI
                    response = await client.chat.completions.create(
                        model=model,
                        messages=[
                            {"role": "system", "content": self.SYSTEM_PROMPT},
                            {"role": "user", "content": prompt},
                        ],
                        temperature=0.1,
                        max_tokens=200,
                        response_format={"type": "json_object"},
                    )

                    # Track success
                    latency_ms = (time.time() - start_time) * 1000
                    AttributionProxy._total_calls_made += 1
                    AttributionProxy._latencies.append(latency_ms)
                    self._record_success(latency_ms)

                    # Track token usage
                    if hasattr(response, "usage") and response.usage:
                        AttributionProxy._total_input_tokens += (
                            response.usage.prompt_tokens
                        )
                        AttributionProxy._total_output_tokens += (
                            response.usage.completion_tokens
                        )

                    # Save raw response for audit trail
                    try:
                        from pathlib import Path

                        run_id = os.environ.get("LACE_RUN_ID", "unknown")
                        mode = os.environ.get("LACE_MODE", "full")
                        raw_dir = (
                            Path.home()
                            / "Desktop"
                            / "lace_runs"
                            / run_id
                            / mode
                            / "openai_raw"
                        )
                        raw_dir.mkdir(parents=True, exist_ok=True)

                        response_id = getattr(
                            response,
                            "id",
                            f"response_{AttributionProxy._total_calls_made}",
                        )
                        # Track response ID for provenance
                        if (
                            response_id
                            and response_id not in AttributionProxy._response_ids
                        ):
                            AttributionProxy._response_ids.append(response_id)

                        raw_file = (
                            raw_dir
                            / f"{AttributionProxy._total_calls_made:03d}_{response_id}.json"
                        )

                        raw_data = {
                            "response_id": response_id,
                            "x_request_id": getattr(response, "request_id", None),
                            "model": model,
                            "created": getattr(response, "created", int(time.time())),
                            "prompt_sha256": hashlib.sha256(
                                prompt.encode()
                            ).hexdigest(),
                            "response_sha256": (
                                hashlib.sha256(
                                    str(response.choices[0].message.content).encode()
                                ).hexdigest()
                                if response.choices
                                else None
                            ),
                            "usage": {
                                "prompt_tokens": (
                                    response.usage.prompt_tokens
                                    if hasattr(response, "usage") and response.usage
                                    else 0
                                ),
                                "completion_tokens": (
                                    response.usage.completion_tokens
                                    if hasattr(response, "usage") and response.usage
                                    else 0
                                ),
                                "total_tokens": (
                                    response.usage.total_tokens
                                    if hasattr(response, "usage") and response.usage
                                    else 0
                                ),
                            },
                            "finish_reason": (
                                response.choices[0].finish_reason
                                if response.choices
                                else None
                            ),
                            "reason": "attr:domain_inference",
                            "latency_ms": latency_ms,
                        }

                        with open(raw_file, "w") as f:
                            json.dump(raw_data, f, indent=2)

                        logger.debug(f"Saved OpenAI response to {raw_file}")
                    except Exception as e:
                        logger.debug(f"Could not save raw response: {e}")
                        # Don't fail attribution if we can't save raw response

                    # Parse response
                    if response.choices and response.choices[0].message.content:
                        try:
                            result = json.loads(response.choices[0].message.content)

                            # Add GPT metadata
                            gpt_sources = []

                            # Handle different response formats defensively
                            if isinstance(result, dict):
                                domains = result.get("domains", [])
                                confidence = result.get("confidence", 0.5)
                                licenses = result.get("licenses", [])
                                citations = result.get("citations", [])

                                for domain in domains[:10]:  # Limit to 10 domains
                                    gpt_sources.append(
                                        {
                                            "domain": domain,
                                            "confidence": confidence,
                                            "licenses": licenses,
                                            "citations": citations,
                                        }
                                    )
                            elif isinstance(result, list):
                                # Handle array response
                                for item in result[:10]:
                                    if isinstance(item, dict):
                                        gpt_sources.append(item)
                                    elif isinstance(item, str):
                                        gpt_sources.append(
                                            {"domain": item, "confidence": 0.5}
                                        )

                            # Add response ID for audit trail
                            if hasattr(response, "id"):
                                for source in gpt_sources:
                                    source["gpt_response_id"] = response.id

                            return (
                                gpt_sources
                                if gpt_sources
                                else [
                                    {
                                        "gpt_skipped": True,
                                        "skip_reason": "empty_response",
                                    }
                                ]
                            )

                        except json.JSONDecodeError as e:
                            logger.warning(
                                f"Failed to parse OpenAI response as JSON: {e}"
                            )
                            AttributionProxy._skip_reasons["parse_error"] += 1
                            return [{"gpt_skipped": True, "skip_reason": "parse_error"}]

                    return [{"gpt_skipped": True, "skip_reason": "empty_response"}]

                except Exception as e:
                    last_error = e
                    error_str = str(e)

                    # Check for rate limit (429) or server errors (5xx)
                    if "429" in error_str or "rate" in error_str.lower():
                        logger.info(
                            f"Rate limit hit, attempt {attempt + 1}/{max_retries}"
                        )
                        if attempt < max_retries - 1:
                            # Exponential backoff with jitter
                            import random

                            sleep_time = backoff * (1 + random.random() * 0.1)
                            await asyncio.sleep(sleep_time)
                            backoff *= 2
                            continue
                    elif any(
                        code in error_str for code in ["500", "502", "503", "504"]
                    ):
                        logger.warning(
                            f"Server error, attempt {attempt + 1}/{max_retries}"
                        )
                        if attempt < max_retries - 1:
                            await asyncio.sleep(backoff)
                            backoff *= 2
                            continue

                    # For other errors, don't retry
                    break

            # All retries failed
            logger.error(
                f"Direct OpenAI call failed after {max_retries} attempts: {last_error}"
            )
            AttributionProxy._total_calls_skipped += 1
            AttributionProxy._skip_reasons["openai_error"] += 1
            self._record_failure("openai_error")
            return [
                {
                    "gpt_skipped": True,
                    "skip_reason": "openai_error",
                    "error": str(last_error),
                }
            ]

        except Exception as e:
            logger.error(f"Direct OpenAI call failed: {e}")
            AttributionProxy._total_calls_skipped += 1
            AttributionProxy._skip_reasons["openai_error"] += 1
            self._record_failure("openai_error")
            return [{"gpt_skipped": True, "skip_reason": "openai_error"}]

    def attribute_sync(
        self,
        snippet: str,
        language_hint: Optional[str] = None,
        candidate_domains: Optional[List[str]] = None,
        consent_confirmed: bool = False,
    ) -> List[Dict[str, Any]]:
        """
        Synchronous wrapper for attribution.

        Args:
            snippet: Redacted text snippet (≤1KB)
            language_hint: Optional language code
            candidate_domains: Optional list of candidate domains
            consent_confirmed: Must be True to proceed

        Returns:
            List of attribution results
        """
        import asyncio

        try:
            loop = asyncio.get_event_loop()
        except RuntimeError:
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)

        return loop.run_until_complete(
            self.attribute(snippet, language_hint, candidate_domains, consent_confirmed)
        )


class DirectOpenAIProxy:
    """
    Direct OpenAI API proxy (for Lambda/server-side use).
    This should only be used in trusted environments with proper key management.
    """

    def __init__(self, api_key: Optional[str] = None):
        """
        Initialize direct OpenAI proxy.

        Args:
            api_key: OpenAI API key (or from OPENAI_API_KEY env)
        """
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self.model = None  # Model will be determined from Secrets Manager

        if not self.api_key:
            # Try AWS Secrets Manager if in Lambda
            if os.environ.get("AWS_LAMBDA_FUNCTION_NAME"):
                creds = self._get_credentials_from_secrets_manager()
                if creds:
                    self.api_key, self.model = creds

        if not self.api_key:
            raise ValueError("No OpenAI API key available")

    def _get_credentials_from_secrets_manager(self) -> Optional[tuple]:
        """Get OpenAI credentials from AWS Secrets Manager."""
        try:
            import boto3

            sm = boto3.client("secretsmanager", region_name="eu-west-1")

            # Try different secret names
            for secret_name in [
                "lace/prod/openai",
                "openai/api/key",
                "lace/openai/key",
            ]:
                try:
                    secret = sm.get_secret_value(SecretId=secret_name)
                    secret_data = json.loads(secret["SecretString"])
                    api_key = (
                        secret_data.get("OPENAI_API_KEY")
                        or secret_data.get("api_key")
                        or secret_data.get("key")
                    )
                    model = secret_data.get("OPENAI_MODEL")  # No default
                    if api_key and model:
                        return api_key, model
                except:
                    continue
        except Exception as e:
            logger.warning(
                f"Failed to get OpenAI credentials from Secrets Manager: {e}"
            )

        return None

    async def call_gpt(
        self,
        snippet: str,
        language_hint: Optional[str] = None,
        candidate_domains: Optional[List[str]] = None,
    ) -> List[Dict[str, Any]]:
        """
        Call GPT directly for attribution.

        Args:
            snippet: Redacted snippet (≤1KB)
            language_hint: Optional language code
            candidate_domains: Optional candidate domains

        Returns:
            Attribution results
        """
        # Build user prompt
        user_prompt = (
            f"Identify the most likely source domains for this content:\n\n{snippet}"
        )

        if language_hint:
            user_prompt += f"\n\nLanguage: {language_hint}"

        if candidate_domains:
            user_prompt += f"\n\nCandidate domains: {', '.join(candidate_domains[:10])}"

        user_prompt += (
            "\n\nReturn JSON array with domain and confidence (0.0-1.0) only."
        )

        # Call OpenAI API
        try:
            async with httpx.AsyncClient(timeout=30) as client:
                # Build request payload
                payload = {
                    "model": self.model,
                    "messages": [
                        {"role": "system", "content": AttributionProxy.SYSTEM_PROMPT},
                        {"role": "user", "content": user_prompt},
                    ],
                    "temperature": 0.1,  # Low temperature for consistency
                    "max_tokens": 500,
                }

                # JSON format support check (no fallback)
                if self.model and "gpt-" in self.model:
                    payload["response_format"] = {"type": "json_object"}

                response = await client.post(
                    "https://api.openai.com/v1/chat/completions",
                    json=payload,
                    headers={
                        "Authorization": f"Bearer {self.api_key}",
                        "Content-Type": "application/json",
                    },
                )

                if response.status_code == 200:
                    result = response.json()
                    content = result["choices"][0]["message"]["content"]

                    # Parse JSON response
                    try:
                        attributions = json.loads(content)
                        if isinstance(attributions, dict) and "domains" in attributions:
                            attributions = attributions["domains"]

                        # Normalize format
                        normalized = []
                        for item in attributions:
                            if isinstance(item, dict) and "domain" in item:
                                normalized.append(
                                    {
                                        "domain": item["domain"],
                                        "confidence": float(
                                            item.get("confidence", 0.5)
                                        ),
                                        "evidence": item.get("evidence", ""),
                                    }
                                )

                        return normalized

                    except json.JSONDecodeError:
                        logger.error(
                            f"Failed to parse GPT JSON response from {self.model}"
                        )
                        return []

                else:
                    logger.error(f"OpenAI API error: {response.status_code}")
                    return []

        except Exception as e:
            logger.error(f"Failed to call GPT ({self.model}): {e}")
            return []
