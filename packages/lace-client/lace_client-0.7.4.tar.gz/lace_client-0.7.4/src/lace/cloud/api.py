"""
Cloud API wrapper for IP-protected SDS generation.
All intelligence (prompts, templates, narrative) stays server-side.
"""

import base64
import hashlib
import json
import logging
import os
import uuid
from datetime import datetime
from typing import Any, Dict, Optional, Tuple

import httpx

logger = logging.getLogger(__name__)

# API configuration
DEFAULT_API_BASE = "https://usgf90tw68.execute-api.eu-west-1.amazonaws.com/prod"
DEFAULT_TIMEOUT = 30.0
MAX_RETRIES = 3


class LaceCloudAPI:
    """Client for Lace Cloud SDS generation."""

    def __init__(self, api_key: Optional[str] = None, api_base: Optional[str] = None):
        """
        Initialize cloud API client.

        Args:
            api_key: API key (or from LACE_API_KEY env)
            api_base: API base URL (or from LACE_API_BASE env)
        """
        self.api_key = api_key or os.environ.get("LACE_API_KEY")
        if not self.api_key:
            raise ValueError("No API key found. Set LACE_API_KEY or pass api_key")

        # Check LACE_API_URL first, then LACE_API_BASE
        self.api_base = (
            api_base
            or os.environ.get("LACE_API_URL")  # Check this FIRST
            or os.environ.get("LACE_API_BASE")
            or DEFAULT_API_BASE
        )
        logger.info(f"Using API base: {self.api_base}")
        self.client = httpx.Client(
            timeout=DEFAULT_TIMEOUT,
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "x-api-key": self.api_key,  # Add for API Gateway compatibility
                "User-Agent": "lace-client/0.7.0",
            },
        )

    def prepare_sds(
        self, local_facts: Dict[str, Any], provider_hints: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Step 1: Get needed questions from server (NEW /v1/sds API).

        Args:
            local_facts: Metadata from local scanner
            provider_hints: Optional provider/model hints

        Returns:
            Response with session_id and questions list
        """
        request_id = str(uuid.uuid4())

        try:
            response = self._post_with_retry(
                "/api/sds/prepare",
                json={
                    "local_facts": local_facts,
                    "provider_hints": provider_hints or {},
                },
                headers={"X-Request-Id": request_id},
            )

            return {
                "session_id": response.get("session_id"),
                "questions": response.get("questions", []),
                "request_id": response.get("request_id", request_id),
            }

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                raise AuthError("Invalid API key")
            elif e.response.status_code == 422:
                raise ValidationError(f"Invalid analysis payload: {e.response.text}")
            else:
                raise ServerError(f"Server error: {e.response.status_code}")
        except httpx.TimeoutException:
            raise NetworkError("Request timed out")
        except Exception as e:
            raise NetworkError(f"Network error: {e}")

    def generate_sds(
        self,
        session_id: str,
        answers: Dict[str, Any],
        format: str = "docx",
        local_facts: Dict[str, Any] = None,
    ) -> Dict[str, Any]:
        """
        Step 2: Generate SDS documents (NEW /v1/sds API).

        Args:
            session_id: Session ID from prepare step
            answers: User answers to questions
            format: Output format ('docx' or 'md')
            local_facts: Local dataset facts from scanner

        Returns:
            SDSArtifacts with documents and provenance
        """
        request_id = str(uuid.uuid4())

        payload = {
            "session_id": session_id,
            "answers": answers,
            "format": format,
            "local_facts": local_facts or {},
            "contract_version": "v1",
        }

        try:
            response = self._post_with_retry(
                "/api/sds/generate", json=payload, headers={"X-Request-Id": request_id}
            )

            # Return response based on format
            return response

        except httpx.HTTPStatusError as e:
            if e.response.status_code == 401:
                raise AuthError("Invalid API key")
            elif e.response.status_code == 402:
                raise PaymentRequiredError("Payment required")
            elif e.response.status_code == 422:
                raise ValidationError(f"Invalid request: {e.response.text}")
            elif e.response.status_code == 429:
                raise RateLimitError("Rate limit exceeded")
            else:
                raise ServerError(f"Server error: {e.response.status_code}")
        except httpx.TimeoutException:
            raise NetworkError("Request timed out")
        except Exception as e:
            raise NetworkError(f"Network error: {e}")

    def _post_with_retry(self, path: str, **kwargs) -> Dict:
        """POST with exponential backoff retry."""
        url = self.api_base + path

        for attempt in range(MAX_RETRIES):
            try:
                response = self.client.post(url, **kwargs)
                response.raise_for_status()
                return response.json()
            except httpx.HTTPStatusError as e:
                if e.response.status_code in [429, 502, 503, 504]:
                    # Retryable errors
                    if attempt < MAX_RETRIES - 1:
                        wait_time = 2**attempt  # Exponential backoff
                        logger.info(
                            f"Retry {attempt + 1}/{MAX_RETRIES} after {wait_time}s"
                        )
                        import time

                        time.sleep(wait_time)
                        continue
                raise
            except httpx.TimeoutException:
                if attempt < MAX_RETRIES - 1:
                    logger.info(f"Timeout, retry {attempt + 1}/{MAX_RETRIES}")
                    continue
                raise

        raise NetworkError(f"Failed after {MAX_RETRIES} retries")

    def __enter__(self):
        """Context manager entry."""
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit - close client."""
        self.client.close()


# Custom exceptions with exit codes


class LaceCloudError(Exception):
    """Base exception for cloud API errors."""

    exit_code = 1


class NoAPIKeyError(LaceCloudError):
    """No API key provided."""

    exit_code = 10

    def __str__(self):
        return "No API key found. Run: export LACE_API_KEY=lace_sk_..."


class NetworkError(LaceCloudError):
    """Network/connectivity error."""

    exit_code = 11


class AuthError(LaceCloudError):
    """Authentication failed."""

    exit_code = 12


class ValidationError(LaceCloudError):
    """Request validation failed."""

    exit_code = 13


class ServerError(LaceCloudError):
    """Server-side error."""

    exit_code = 14


class PaymentRequiredError(LaceCloudError):
    """Payment required."""

    exit_code = 15


class RateLimitError(LaceCloudError):
    """Rate limit exceeded."""

    exit_code = 16
