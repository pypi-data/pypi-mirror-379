"""
Lace Cloud API Client - Minimal implementation for PyPI.
All processing happens in the cloud for IP protection.
"""

import os
import json
import time
import uuid
import random
import base64
from typing import Dict, Any, Optional, List, Tuple
from pathlib import Path
import hashlib
import logging

import httpx

from .bloom_filter import BloomFilter
from .constants import (
    X_LACE_API_VERSION,
    CLIENT_RUN_ID,
    CONNECT_TIMEOUT,
    READ_TIMEOUT,
    WRITE_TIMEOUT,
    POOL_TIMEOUT,
    MAX_RETRIES,
    RETRY_BACKOFF_BASE,
    RETRY_BACKOFF_JITTER,
)

# Custom exceptions for job states
class JobFailed(RuntimeError):
    """Raised when a job fails on the server."""
    pass

class JobCanceled(RuntimeError):
    """Raised when a job is canceled."""
    pass
from .utils import redact_sensitive, extract_domain
from . import __version__

logger = logging.getLogger(__name__)


class LaceException(Exception):
    """Base exception for Lace client."""
    def __init__(self, message: str, status_code: Optional[int] = None, body: Optional[str] = None):
        super().__init__(message)
        self.status_code = status_code
        self.body = redact_sensitive(body) if body else None


class ValidationError(LaceException):
    """Local validation error."""
    pass


class PaymentRequiredError(LaceException):
    """Payment required or aborted."""
    pass


class ServerError(LaceException):
    """Server error (5xx)."""
    pass


class NetworkError(LaceException):
    """Network or timeout error."""
    pass


class PolicyViolationError(LaceException):
    """Policy violation (missing required facts)."""
    pass


class LaceClient:
    """
    Minimal Lace client for cloud operations.
    All algorithms and processing happen securely in the cloud.
    """
    
    def __init__(self, api_key: Optional[str] = None, api_base: Optional[str] = None, verbose_http: bool = False):
        """
        Initialize Lace client.
        
        Args:
            api_key: API key for authentication. If not provided, uses LACE_API_KEY env var.
            api_base: API base URL. Priority: param > env > config > default
            verbose_http: Enable verbose HTTP logging for debugging
        """
        self.api_key = api_key or os.getenv('LACE_API_KEY')
        self.verbose_http = verbose_http
        
        # Load config file if exists
        config = self._load_config()
        
        # API base priority: param > env > config > default
        self.api_base = (
            api_base or
            os.getenv('LACE_API_BASE') or
            os.getenv('LACE_API_URL') or  # Legacy support
            config.get('api_base') or
            'https://usgf90tw68.execute-api.eu-west-1.amazonaws.com/prod'
        )
        
        # Set up HTTP client with proxy support
        self.session = self._create_session()
        
        # Get platform info for user agent
        import platform
        os_info = platform.system().lower()
        py_version = platform.python_version()
        
        # Base headers
        self.headers = {
            'Content-Type': 'application/json',
            'User-Agent': f'lace-client/{__version__} ({os_info}; py{py_version})',
            'X-Lace-Client': f'lace-cli/{__version__}',
            'X-Lace-Api-Version': X_LACE_API_VERSION,
            'X-Lace-Client-Run-Id': CLIENT_RUN_ID,
        }
        
        if self.api_key:
            # Use uppercase X-API-Key for API Gateway compatibility
            self.headers['X-API-Key'] = self.api_key
    
    def _load_config(self) -> dict:
        """Load config from ~/.lace/config.json if exists."""
        config_path = Path.home() / '.lace' / 'config.json'
        if config_path.exists():
            try:
                with open(config_path, 'r') as f:
                    return json.load(f)
            except Exception:
                pass
        return {}
    
    def _create_session(self):
        """Create HTTP session with proxy support."""
        proxies = {}
        if http_proxy := os.getenv('HTTP_PROXY'):
            proxies['http'] = http_proxy
        if https_proxy := os.getenv('HTTPS_PROXY'):
            proxies['https'] = https_proxy
        
        # Use httpx with optimized connection pooling for parallel uploads
        proxy = proxies.get('https') or proxies.get('http')
        return httpx.Client(
            proxy=proxy if proxy else None,
            timeout=httpx.Timeout(
                connect=CONNECT_TIMEOUT,
                read=READ_TIMEOUT,
                write=WRITE_TIMEOUT,
                pool=POOL_TIMEOUT
            ),
            limits=httpx.Limits(
                max_connections=64,  # Total connections
                max_keepalive_connections=32,  # Persistent connections
                keepalive_expiry=30.0  # Seconds to keep connections alive
            ),
        )
    
    def _request(self, method: str, path: str, json_data: Optional[dict] = None,
                 headers: Optional[dict] = None, params: Optional[dict] = None,
                 idempotency_key: Optional[str] = None, retry: bool = True) -> Tuple[int, dict]:
        """Make HTTP request with retries and error handling."""
        url = f"{self.api_base}{path}"
        request_headers = {**self.headers}
        if headers:
            request_headers.update(headers)
        if idempotency_key:
            request_headers['Idempotency-Key'] = idempotency_key
        
        # Ensure Content-Type is set for JSON payloads
        if json_data is not None:
            request_headers['Content-Type'] = 'application/json'
        
        # Log request if verbose
        if self.verbose_http and json_data:
            sanitized = self._sanitize_for_logging(json_data)
            logger.info(f"HTTP {method} {path}")
            logger.info(f"Request payload: {json.dumps(sanitized, indent=2)}")
            
            # Guard log to ensure payload isn't corrupted
            manifest = json_data.get('manifest', {})
            files = manifest.get('files', [])
            bad = [f for f in files if not isinstance(f, dict) or 'hash' not in f or len(str(f.get('hash', ''))) < 64]
            if bad:
                logger.warning(f"Sending {len(files)} file descriptors; {len(bad)} have invalid/truncated hashes")
            else:
                logger.info(f"Sending {len(files)} file descriptors; invalid entries: 0")
        
        attempt = 0
        last_error = None
        
        while attempt <= (MAX_RETRIES if retry else 0):
            try:
                # httpx only
                response = self.session.request(
                    method,
                    url,
                    json=json_data,
                    headers=request_headers,
                    params=params,
                )
                
                # Check for rate limiting
                if response.status_code == 429:
                    if retry and attempt < MAX_RETRIES:
                        retry_after = int(response.headers.get('Retry-After', '5'))
                        time.sleep(retry_after)
                        attempt += 1
                        continue
                    else:
                        raise ServerError(
                            "Rate limited",
                            status_code=429,
                            body=response.text
                        )
                
                # Check for server errors (retry)
                if response.status_code >= 500:
                    # Log error details if verbose
                    if self.verbose_http:
                        request_id = (
                            response.headers.get('X-Request-Id') or 
                            response.headers.get('x-request-id') or 
                            response.headers.get('x-amzn-RequestId', 'unknown')
                        )
                        body_snippet = response.text[:512] if response.text else 'empty'
                        logger.error(f"HTTP {response.status_code} from {method} {path}")
                        logger.error(f"Request ID: {request_id}")
                        logger.error(f"Response body: {body_snippet}")
                    
                    if retry and attempt < MAX_RETRIES:
                        backoff = RETRY_BACKOFF_BASE ** attempt
                        jitter = random.uniform(*RETRY_BACKOFF_JITTER)
                        time.sleep(backoff + jitter)
                        attempt += 1
                        continue
                    else:
                        request_id = (
                            response.headers.get('X-Request-Id') or 
                            response.headers.get('x-request-id') or 
                            response.headers.get('x-amzn-RequestId', 'unknown')
                        )
                        body_snippet = response.text[:512] if response.text else 'empty'
                        raise ServerError(
                            f"Server error {response.status_code} (Request ID: {request_id})",
                            status_code=response.status_code,
                            body=response.text
                        )
                
                # Check for client errors (don't retry)
                if 400 <= response.status_code < 500:
                    error_body = response.text
                    try:
                        error_json = response.json()
                        error_msg = error_json.get('error', error_json.get('message', 'Client error'))
                    except:
                        error_msg = f"HTTP {response.status_code}"
                    
                    if response.status_code == 402:
                        raise PaymentRequiredError(error_msg, response.status_code, error_body)
                    else:
                        raise LaceException(error_msg, response.status_code, error_body)
                
                # Success (accept 200/201/202 for job creation)
                if response.status_code in (200, 201, 202):
                    if self.verbose_http:
                        logger.info(f"HTTP {response.status_code} success from {method} {path}")
                    try:
                        return response.status_code, response.json()
                    except:
                        return response.status_code, {}
                
                # Other 2xx codes
                try:
                    return response.status_code, response.json()
                except:
                    return response.status_code, {}
                    
            except Exception as e:
                # Handle timeout errors
                timeout_error = isinstance(e, (httpx.ConnectTimeout, httpx.ReadTimeout))
                
                if timeout_error:
                    last_error = e
                    if retry and attempt < MAX_RETRIES:
                        backoff = RETRY_BACKOFF_BASE ** attempt
                        jitter = random.uniform(*RETRY_BACKOFF_JITTER)
                        time.sleep(backoff + jitter)
                        attempt += 1
                        continue
                    else:
                        raise NetworkError(f"Request timeout: {redact_sensitive(str(e))}")
                
                # Handle network errors
                network_error = isinstance(e, httpx.NetworkError)
                
                if network_error:
                    last_error = e
                    if retry and attempt < MAX_RETRIES:
                        backoff = RETRY_BACKOFF_BASE ** attempt
                        jitter = random.uniform(*RETRY_BACKOFF_JITTER)
                        time.sleep(backoff + jitter)
                        attempt += 1
                        continue
                    else:
                        raise NetworkError(f"Network error: {redact_sensitive(str(e))}")
                
                # Re-raise other exceptions
                raise
        
        # Should never get here
        raise NetworkError(f"Max retries exceeded: {redact_sensitive(str(last_error))}")
    
    def ingest_analysis(self, analysis: dict) -> dict:
        """Ingest analysis data and get questions."""
        status, response = self._request(
            'POST',
            '/api/wizard/ingest-analysis',
            json_data={'analysis': analysis}
        )
        # Log warnings if present
        if 'warnings' in response:
            for warning in response.get('warnings', []):
                logger.info(f"Server warning: {warning.get('code', 'unknown')} - {warning.get('note', '')}")
        return response
    
    def answer(self, session_id: str, answers: dict) -> dict:
        """Submit answers for a session."""
        status, response = self._request(
            'POST',
            '/api/wizard/answer',
            json_data={'session_id': session_id, 'answers': answers}
        )
        return response
    
    def preview_generate(self, session_id: str) -> dict:
        """Generate preview token."""
        idempotency_key = str(uuid.uuid4())
        status, response = self._request(
            'POST',
            '/api/wizard/preview/generate',
            json_data={'session_id': session_id},
            idempotency_key=idempotency_key
        )
        return response
    
    def checkout(self, session_id: str) -> dict:
        """Create billing checkout session."""
        idempotency_key = str(uuid.uuid4())
        status, response = self._request(
            'POST',
            '/api/billing/checkout',
            json_data={'session_id': session_id},
            idempotency_key=idempotency_key
        )
        return response
    
    def billing_status(self, session_id: str) -> dict:
        """Check billing status."""
        status, response = self._request(
            'GET',
            f'/api/billing/status?session_id={session_id}'
        )
        return response
    
    def commit(self, session_id: str) -> dict:
        """Commit and get download URL."""
        idempotency_key = str(uuid.uuid4())
        status, response = self._request(
            'POST',
            '/api/wizard/commit',
            json_data={'session_id': session_id},
            idempotency_key=idempotency_key
        )
        return response
    
    def health(self) -> dict:
        """Check API health."""
        status, response = self._request(
            'GET',
            '/api/health',
            retry=False
        )
        return response
    
    def attest(self, dataset_path: str, name: Optional[str] = None) -> str:
        """
        Create attestation for a dataset.
        Privacy-preserving: Creates bloom filter locally, only sends filter bytes.
        
        Args:
            dataset_path: Path to dataset file or directory
            name: Optional name for the dataset
            
        Returns:
            Attestation ID
        """
        dataset_path = Path(dataset_path)
        if not dataset_path.exists():
            raise FileNotFoundError(f"Dataset not found: {dataset_path}")
        
        # Create bloom filter locally
        bloom = BloomFilter(expected_items=1_000_000, fp_rate=0.0001)
        
        # Process files and add to bloom filter
        if dataset_path.is_file():
            # Single file
            with open(dataset_path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                bloom.add_text_content(content, include_ngrams=True)
        else:
            # Directory of files
            for file_path in dataset_path.rglob('*'):
                if file_path.is_file():
                    try:
                        with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
                            content = f.read()
                            bloom.add_text_content(content, include_ngrams=True)
                    except Exception as e:
                        print(f"Warning: Skipped {file_path}: {e}")
        
        # Convert bloom filter to bytes (one-way transformation)
        bloom_bytes = bloom.to_bytes()
        bloom_b64 = base64.b64encode(bloom_bytes).decode('utf-8')
        
        # Start attestation session
        status, result = self._request(
            'POST',
            '/v1/attest/start',
            json_data={
                'dataset_path': str(dataset_path),
                'dataset_name': name or dataset_path.name,
                'dataset_size': len(bloom_bytes)
            }
        )
        
        if status != 200:
            raise Exception(f"Failed to start attestation: {result}")
        
        # Get dataset_id (NOT session_id - fixing the bug!)
        dataset_id = result.get('dataset_id') or result.get('session_id')  # Handle both
        
        # Send bloom filter chunks (not raw data!)
        chunk_size = 1024 * 1024  # 1MB chunks
        for i in range(0, len(bloom_b64), chunk_size):
            chunk = bloom_b64[i:i+chunk_size]
            status, response = self._request(
                'POST',
                '/v1/attest/chunk',
                json_data={
                    'dataset_id': dataset_id,  # Fixed: use dataset_id
                    'content': chunk,  # This is bloom filter data, not raw text
                    'is_bloom': True  # Flag to indicate this is bloom data
                }
            )
            
            if status != 200:
                print(f"Warning: Failed to send bloom chunk: {response}")
        
        # Finalize attestation
        status, response = self._request(
            'POST',
            '/v1/attest/finalize',
            json_data={'dataset_id': dataset_id}  # Fixed: use dataset_id not session_id
        )
        
        if status != 200:
            raise Exception(f"Failed to finalize attestation: {response}")
        
        attestation_id = response.get('attestation_id') or response.get('dataset_id') or dataset_id
        
        print(f"✅ Attestation created: {attestation_id}")
        
        return attestation_id
    
    def verify(self, attestation_id: str, check_copyright: Optional[str] = None) -> Dict[str, Any]:
        """
        Verify an attestation and optionally check for specific text.
        
        Args:
            attestation_id: ID of attestation to verify
            check_copyright: Optional text to check if it was in training data
            
        Returns:
            Verification result with confidence score
        """
        # Build request body
        body = {
            'attestation_id': attestation_id,
            'dataset_id': attestation_id  # Support both field names
        }
        
        if check_copyright:
            body['text_to_verify'] = check_copyright
            body['check_copyright'] = check_copyright  # Support both field names
        
        # POST request (not GET)
        response = self.session.post(
            f"{self.api_base}/v1/verify",
            json=body,
            headers=self.headers
        )
        
        if response.status_code != 200:
            raise Exception(f"Verification failed: {response.text}")
        
        result = response.json()
        
        # Don't print here - let the caller handle display
        # This makes the function more flexible
        return result
    
    def monitor_start(self, attestation_id: str) -> str:
        """
        Start monitoring session for training.
        
        Args:
            attestation_id: Attestation to monitor against
            
        Returns:
            Monitor session ID
        """
        response = self.session.post(
            f"{self.api_base}/v1/monitor/start",
            json={'attestation_id': attestation_id},
            headers=self.headers
        )
        
        if response.status_code != 200:
            raise Exception(f"Failed to start monitoring: {response.text}")
        
        return response.json()['session_id']
    
    def monitor_loss(self, session_id: str, step: int, loss: float):
        """
        Send loss value to cloud.
        
        Args:
            session_id: Monitor session ID
            step: Training step
            loss: Loss value
        """
        response = self.session.post(
            f"{self.api_base}/v1/monitor/loss",
            json={
                'session_id': session_id,
                'step': step,
                'loss': loss
            },
            headers=self.headers
        )
        
        if response.status_code != 200:
            # Don't fail training if monitoring fails
            print(f"Warning: Failed to send loss: {response.text}")
    
    def monitor_finalize(self, session_id: str) -> Dict[str, Any]:
        """
        Finalize monitoring and get correlation.
        
        Args:
            session_id: Monitor session ID
            
        Returns:
            Monitoring results with correlation
        """
        response = self.session.post(
            f"{self.api_base}/v1/monitor/finalize",
            json={'session_id': session_id},
            headers=self.headers
        )
        
        if response.status_code != 200:
            raise Exception(f"Failed to finalize monitoring: {response.text}")
        
        return response.json()
    
    def _hash_file(self, file_path: Path) -> str:
        """Hash file content."""
        hasher = hashlib.sha256()
        with open(file_path, 'rb') as f:
            while chunk := f.read(8192):
                hasher.update(chunk)
        return hasher.hexdigest()
    
    def _sanitize_for_logging(self, data: dict) -> dict:
        """Sanitize data for logging (remove sensitive info)."""
        import copy
        sanitized = copy.deepcopy(data)
        
        # Truncate file lists
        if 'manifest' in sanitized:
            manifest = sanitized['manifest']
            orig_count = len(manifest.get('files', []))
            if 'files' in manifest and len(manifest['files']) > 3:
                # Truncate but don't add non-schema items
                manifest['files'] = manifest['files'][:3]
                # Add truncation note outside the files array
                manifest['_truncated'] = f'{orig_count - 3} more files omitted from log'
            # Shorten hashes and remove full paths
            for f in manifest.get('files', []):
                if isinstance(f, dict):
                    if 'path' in f:
                        f['path'] = Path(f['path']).name  # Only show filename
                    if 'hash' in f and len(f['hash']) > 8:
                        f['hash'] = f['hash'][:8] + '...'
        
        # Truncate domain lists
        if 'config' in sanitized and 'local_facts' in sanitized['config']:
            facts = sanitized['config']['local_facts']
            if 'domains' in facts and len(facts['domains']) > 5:
                facts['domains'] = facts['domains'][:5] + ['...']
        
        return sanitized
    
    def _normalize_analyze_payload_for_server(self, payload: dict) -> dict:
        """Normalize payload to match server contract."""
        from datetime import datetime
        import sys
        import copy
        
        payload = copy.deepcopy(payload)
        
        # PERMANENT: Server expects local_facts at top-level, not nested in config
        if 'config' in payload and isinstance(payload['config'], dict):
            local_facts = payload['config'].pop('local_facts', None)
            if local_facts is not None:
                # Support both tdm_results and tdm_stats keys
                if 'tdm_results' in local_facts and 'tdm_stats' not in local_facts:
                    local_facts['tdm_stats'] = local_facts['tdm_results']
                payload['local_facts'] = local_facts
        
        # Fix manifest file entries
        manifest = payload.get('manifest', {})
        for f in manifest.get('files', []):
            # Ensure relpath exists
            if 'relpath' not in f:
                f['relpath'] = f.get('relpath') or Path(f.get('path', '')).name
            # Convert mtime to ISO8601 if it's a timestamp
            if 'mtime' in f and isinstance(f['mtime'], (int, float)):
                f['mtime'] = datetime.utcfromtimestamp(f['mtime']).strftime('%Y-%m-%dT%H:%M:%SZ')
        payload['manifest'] = manifest
        
        # Add client info
        if 'client' not in payload:
            payload['client'] = {
                'name': 'lace-cli',
                'version': __version__,
                'platform': sys.platform,
            }
        
        return payload
    
    # ============================================================================
    # ASYNC ANALYSIS METHODS - For large dataset processing
    # ============================================================================
    
    def start_async_analysis(self, manifest: dict, config: dict) -> dict:
        """
        Start async analysis job with dataset manifest.
        
        Args:
            manifest: Dataset manifest with file list and metadata
            config: Analysis configuration (tier, encryption, etc.)
            
        Returns:
            Job details including job_id and upload URLs
        """
        payload = {
            'manifest': manifest,
            'config': config,
            'idempotency_key': hashlib.sha256(
                json.dumps(manifest, sort_keys=True).encode()
            ).hexdigest()
        }
        
        # Normalize payload for server compatibility
        payload = self._normalize_analyze_payload_for_server(payload)
        
        status_code, response_data = self._request('POST', '/api/v1/sds/analyze', json_data=payload)
        
        # Accept 200/201/202 for job creation
        if status_code not in (200, 201, 202):
            raise ServerError(f"Failed to start analysis: {response_data}")
        
        return response_data
    
    def get_job_status(self, job_id: str) -> dict:
        """
        Get status of an async analysis job.
        
        Args:
            job_id: The job ID to check
            
        Returns:
            Job status including progress and phase details
        """
        # Add cache-busting params and headers
        params = {"_": str(int(time.time() * 1000))}  # Cache buster
        headers = {
            "Cache-Control": "no-cache",
            "Pragma": "no-cache"
        }
        
        status_code, response_data = self._request('GET', f'/api/v1/sds/status/{job_id}', 
                                                  params=params, headers=headers)
        
        if status_code == 404:
            raise ValidationError(f"Job {job_id} not found")
        elif status_code != 200:
            raise ServerError(f"Failed to get status: {response_data}")
        
        return response_data
    
    def get_analysis_results(self, job_id: str) -> dict:
        """
        Get results of completed async analysis.
        
        Args:
            job_id: The job ID to retrieve results for
            
        Returns:
            Analysis results with pre-filled questions
        """
        status_code, response_data = self._request('GET', f'/api/v1/sds/results/{job_id}')
        
        if status_code == 404:
            raise ValidationError(f"Job {job_id} not found")
        elif status_code != 200:
            raise ServerError(f"Failed to get results: {response_data}")
        
        return response_data
    
    def generate_sds_document(self, job_id: str, answers: dict, format: str = 'docx') -> dict:
        """
        Generate SDS document from async analysis results.
        
        Args:
            job_id: The job ID with completed analysis
            answers: User-provided or AI-suggested answers
            format: Output format ('docx' or 'json')
            
        Returns:
            Generated document (base64 encoded for docx, JSON for json format)
        """
        payload = {
            'job_id': job_id,
            'answers': answers,
            'format': format
        }
        
        status_code, response_data = self._request('POST', '/api/v1/sds/generate', json_data=payload)
        
        if status_code != 200:
            raise ServerError(f"Failed to generate document: {response_data}")
        
        return response_data
    
    def generate_pack(self, job_id: str, answers: Optional[dict] = None) -> dict:
        """
        Generate DOCX pack from completed async analysis job.
        
        Args:
            job_id: The job ID with completed analysis
            answers: Optional dictionary of answers to merge with auto-populated values
            
        Returns:
            Dictionary with 'url' for pre-signed download URL
        """
        body = {'answers': answers} if answers else None
        status_code, response_data = self._request('POST', f'/api/v1/sds/jobs/{job_id}/pack', json_data=body)
        
        if status_code == 409:
            raise ValueError("Job not completed yet")
        elif status_code != 200:
            raise ServerError(f"Failed to generate pack: {response_data}")
        
        return response_data
    
    def mark_upload_complete(self, job_id: str) -> dict:
        """
        Signal that file upload is complete for a job.
        
        Args:
            job_id: The job ID to mark as upload complete
            
        Returns:
            Updated job status
        """
        status_code, response_data = self._request('POST', f'/api/v1/sds/jobs/{job_id}/upload-complete')
        
        if status_code != 200:
            raise ServerError(f"Failed to mark upload complete: {response_data}")
        
        return response_data
    
    def complete_multipart_upload(self, job_id: str, file_hash: str, upload_id: str, parts: list) -> dict:
        """
        Complete multipart upload server-side.
        
        Args:
            job_id: The job ID
            file_hash: SHA256 hash of the file
            upload_id: S3 multipart upload ID
            parts: List of part numbers and ETags
            
        Returns:
            Completion response
        """
        payload = {
            'upload_id': upload_id,
            'parts': parts
        }
        
        status_code, response_data = self._request(
            'POST',
            f'/api/v1/sds/jobs/{job_id}/files/{file_hash}/complete',
            json_data=payload
        )
        
        if status_code != 200:
            raise ServerError(f"Failed to complete multipart upload: {response_data}")
        
        return response_data
    
    def wait_for_job_completion(self, job_id: str, timeout: Optional[float] = None,
                                poll_interval: float = 2.0, max_poll_interval: float = 15.0,
                                backoff_factor: float = 1.6) -> dict:
        """
        Wait for async job to complete with exponential backoff.
        
        Args:
            job_id: The job ID to wait for
            timeout: Maximum time to wait in seconds (None = wait indefinitely)
            poll_interval: Initial seconds between status checks (default: 2)
            max_poll_interval: Maximum poll interval in seconds (default: 15)
            backoff_factor: Backoff multiplier (default: 1.6)
            
        Returns:
            Final job status
            
        Raises:
            JobFailed: If job fails
            JobCanceled: If job is canceled
            TimeoutError: If timeout is specified and exceeded
        """
        import time
        import random
        import sys
        
        start = time.monotonic()
        next_sleep = poll_interval
        last_status = None
        last_progress = None
        last_progress_change = time.monotonic()
        last_heartbeat = time.monotonic()
        stall_warned = False
        
        while True:
            # Check timeout if specified
            if timeout is not None and (time.monotonic() - start) > timeout:
                return {"status": "timeout", "job_id": job_id}
            
            try:
                status_resp = self.get_job_status(job_id)
                status = status_resp.get('status', 'unknown')
                progress = status_resp.get('progress')
                
                now = time.monotonic()
                
                # Print on status or progress change
                if status != last_status or (isinstance(progress, (int, float)) and progress != last_progress):
                    if isinstance(progress, (int, float)):
                        print(f"   Status: {status} ({int(progress)}%)", file=sys.stderr, flush=True)
                    else:
                        print(f"   Status: {status}", file=sys.stderr, flush=True)
                    last_status = status
                    last_progress = progress
                    last_progress_change = now
                    stall_warned = False  # Reset stall warning on progress
                else:
                    # Print heartbeat every 60 seconds
                    if now - last_heartbeat >= 60:
                        elapsed = now - start
                        minutes = int(elapsed // 60)
                        seconds = int(elapsed % 60)
                        print(f"   Still {status} ({progress}%) — elapsed {minutes}m{seconds}s — polling every {next_sleep:.1f}s", 
                              file=sys.stderr, flush=True)
                        last_heartbeat = now
                    
                    # Warn if no progress for 10 minutes
                    if not stall_warned and (now - last_progress_change) >= 600:
                        print(f"   No visible progress for 10m; this can be normal during 'initializing' or while capacity is queued.", 
                              file=sys.stderr, flush=True)
                        print(f"   Tip: press Ctrl+C to detach; resume later with:", file=sys.stderr, flush=True)
                        print(f"        lace pack --resume {job_id} --out <your_output.docx>", file=sys.stderr, flush=True)
                        stall_warned = True
                
                # Terminal states
                if status == 'completed':
                    return status_resp
                elif status in ('failed', 'error'):
                    error_msg = status_resp.get('error', 'Unknown error')
                    raise JobFailed(f"Job {job_id} failed: {error_msg}")
                elif status in ('canceled', 'cancelled'):
                    raise JobCanceled(f"Job {job_id} canceled")
                
                # Check for Retry-After header (if available in response)
                retry_after = status_resp.get('retry_after')
                if retry_after:
                    sleep_for = float(retry_after)
                else:
                    # Use current interval with jitter
                    sleep_for = next_sleep + random.uniform(0, 0.5)
                    # Update for next iteration
                    next_sleep = min(next_sleep * backoff_factor, max_poll_interval)
                
                time.sleep(sleep_for)
                
            except ValidationError as e:
                # Job might not exist yet, wait and retry
                if "not found" in str(e):
                    time.sleep(poll_interval)
                    continue
                raise


# Convenience functions for one-line usage
_default_client = None

def get_client() -> LaceClient:
    """Get or create default client."""
    global _default_client
    if _default_client is None:
        _default_client = LaceClient()
    return _default_client

def attest(dataset_path: str, name: Optional[str] = None) -> str:
    """Quick attestation."""
    return get_client().attest(dataset_path, name)

def verify(attestation_id: str, check_copyright: Optional[str] = None) -> Dict[str, Any]:
    """Quick verification."""
    return get_client().verify(attestation_id, check_copyright)

def monitor():
    """
    One-line training monitor.
    Automatically hooks into PyTorch/TensorFlow training.
    """
    from .monitor import LaceMonitor
    monitor = LaceMonitor()
    monitor.start()
    return monitor