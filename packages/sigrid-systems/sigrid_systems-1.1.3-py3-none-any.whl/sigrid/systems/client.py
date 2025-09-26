"""
SIGRID Systems Client

HTTP client interface for SIGRID legal analysis.

Available Classes:
    Client - Main HTTP client for SIGRID API
        - analyze_stream(): Stream analysis results with real-time events
        - analyze(): Get all analysis results at once
        - get_session_log(): Retrieve session audit logs
        - get_user_logs(): Get all user activity logs

Features:
    - Automatic retry with exponential backoff (5xx, 429)
    - Structured error handling with specific exceptions
    - Streaming and batch analysis interfaces
    - Session management and audit logging
    - Request timeout handling

Usage:
    api_client = client.Client(
        api_key="your-subscription-key",
        user_id="user-123"
    )
    
    Streaming analysis (real-time events):
    async with api_client.analyze_stream(documents, query) as stream:
        async for event in stream:
            print(event.type, event.data)
    
    Batch analysis (get all results):
    results = await api_client.analyze(documents, query)
    
    Audit logs:
    session_logs = await api_client.get_session_log(session_id)
    user_logs = await api_client.get_user_logs()
"""

import httpx
import json
import asyncio
import uuid
from typing import List, Dict, Any, Optional, AsyncIterator, Union

from .exceptions import (
    from_http_status,
    NetworkError,
    SigridError,
    ClientError,
    ServerError,
    AuthenticationError,
    RateLimitError,
    ValidationError,
)
from .types import Document, AnalysisEvent, AnalysisRequest, ClientConfig, Documents, RawEvents
from .stream import AnalysisStream
from .tyr import TYRClient

# Make exceptions available at module level
__all__ = [
    "Client",
    "SigridError",
    "ClientError", 
    "ServerError",
    "AuthenticationError",
    "RateLimitError",
    "ValidationError",
    "NetworkError",
]


class Client:
    """
    SIGRID Legal Analysis API Client.

    HTTP client with structured error handling and automatic retry logic.

    Usage:
        from sigrid.systems import client, types, exceptions

        try:
            api_client = client.Client(
                api_key="your-key",
                user_id="user-123"
            )

            doc = types.Document(id="case_1", content="...")

            # TYR API - ECHR Analysis
            async with api_client.tyr.analyze_stream([doc], query) as stream:
                async for event in stream:
                    print(event)

            # Get all results at once
            results = await api_client.tyr.analyze([doc], query)

        except exceptions.ValidationError as e:
            print(f"Input error: {e}")
        except exceptions.AuthenticationError:
            print("Check API key")

    Error Codes:
        400: Validation error on input data
        401: Missing authentication headers
        403: Authentication failure
        422: Document size/count limits exceeded
        429: Rate limit exceeded (auto-retry with backoff)
        500: Internal server error (auto-retry)
        504: Analysis timeout exceeded
    """

    def __init__(
        self,
        *,
        api_key: str,
        user_id: str,
        config: Optional[ClientConfig] = None
    ):
        """
        Initialize SIGRID client.

        Args:
            api_key: Your tenant-specific API subscription key
            user_id: User identifier to act on behalf of
            config: Optional client configuration
        """
        if not all([api_key, user_id]):
            raise ValueError("api_key and user_id are required")

        self._config = config or ClientConfig()

        self._headers = {
            "Ocp-Apim-Subscription-Key": api_key,
            "X-Tenant-Id": api_key, # The API key is the Tenant ID
            "X-User-Id": user_id,
            "X-On-Behalf-Of-User": user_id,
            "Content-Type": "application/json",
        }

        # Initialize API namespaces
        self.tyr = TYRClient(self)
    
    # Deprecated methods - kept for backwards compatibility
    async def analyze(
        self,
        documents: Documents,
        query: str,
        *,
        correlation_id: Optional[str] = None,
        idempotency_key: Optional[str] = None
    ) -> List[AnalysisEvent]:
        """
        [DEPRECATED] Use api_client.tyr.analyze() instead.

        Analyze documents and return all events.
        """
        return await self.tyr.analyze(
            documents=documents,
            query=query,
            correlation_id=correlation_id,
            idempotency_key=idempotency_key
        )

    def analyze_stream(
        self,
        documents: Documents,
        query: str,
        *,
        correlation_id: Optional[str] = None,
        idempotency_key: Optional[str] = None
    ) -> AnalysisStream:
        """
        [DEPRECATED] Use api_client.tyr.analyze_stream() instead.

        Analyze documents with streaming results using context manager.
        """
        return self.tyr.analyze_stream(
            documents=documents,
            query=query,
            correlation_id=correlation_id,
            idempotency_key=idempotency_key
        )

    # Internal implementation methods used by API namespaces
    async def _analyze_impl(
        self,
        documents: Documents,
        query: str,
        *,
        correlation_id: Optional[str] = None,
        idempotency_key: Optional[str] = None
    ) -> List[AnalysisEvent]:
        """Internal implementation for analyze."""
        events = []
        async for event in self._analyze_stream_impl(
            documents=documents,
            query=query,
            correlation_id=correlation_id,
            idempotency_key=idempotency_key
        ):
            events.append(event)
        return events

    def _analyze_stream_impl(
        self,
        documents: Documents,
        query: str,
        *,
        correlation_id: Optional[str] = None,
        idempotency_key: Optional[str] = None
    ) -> AnalysisStream:
        """Internal implementation for analyze_stream."""
        # Convert all inputs to Document objects upfront.
        # This ensures bytes are encoded and MIME types are set correctly.
        doc_objects = []
        for doc in documents:
            if isinstance(doc, Document):
                doc_objects.append(doc)
            elif isinstance(doc, dict):
                # This allows passing raw dicts, which are converted to Document objects.
                doc_objects.append(Document.create(**doc))
            else:
                raise ValueError(f"Input document must be a Document instance or a dict, not {type(doc).__name__}")

        request = AnalysisRequest(
            documents=doc_objects,
            query=query,
            correlation_id=correlation_id,
            idempotency_key=idempotency_key
        )

        raw_stream = self._stream_analysis(request)
        return AnalysisStream(raw_stream)
    
    async def get_session_log(
        self, 
        session_id: str, 
        *,
        correlation_id: Optional[str] = None
    ) -> Dict[str, Any]:
        """
        Get session log by ID.
        
        Args:
            session_id: Session identifier
            correlation_id: Optional correlation ID
            
        Returns:
            Session log data
        """
        headers = self._headers.copy()
        if correlation_id:
            headers["X-Correlation-Id"] = correlation_id
            
        response = await self._request(
            "GET", 
            f"/v1/analysis/sigrid/logs/session/{session_id}",
            headers=headers
        )
        return response.json()
    
    async def get_user_logs(self, *, correlation_id: Optional[str] = None) -> Dict[str, Any]:
        """
        Get all logs for the current user.
        
        Args:
            correlation_id: Optional correlation ID
            
        Returns:
            User logs data
        """
        headers = self._headers.copy()
        if correlation_id:
            headers["X-Correlation-Id"] = correlation_id
            
        user_id = self._headers["X-User-Id"]
        response = await self._request(
            "GET",
            f"/v1/analysis/sigrid/logs/user/{user_id}", 
            headers=headers
        )
        return response.json()
    
    async def _stream_analysis(self, request: AnalysisRequest) -> RawEvents:
        """Internal method to stream raw analysis events."""
        headers = self._headers.copy()
        headers["Accept"] = "text/event-stream"
        
        if request.correlation_id:
            headers["X-Correlation-Id"] = request.correlation_id
        # Always add idempotency key - generate if not provided    
        idempotency_key = request.idempotency_key or f"sigrid-{uuid.uuid4()}"
        headers["Idempotency-Key"] = idempotency_key
            
        payload = {
            "documents": [doc.to_dict() for doc in request.documents],
            "query": request.query,
            "streaming": True
        }
        
        # DEBUG: Print the final payload to inspect its structure
        print("--- DEBUG: PAYLOAD BEING SENT ---")
        import json
        print(json.dumps(payload, indent=2))
        print("---------------------------------")
        
        url = f"{self._config.base_url}/v1/analysis/sigrid/analyze"
        
        try:
            async with httpx.AsyncClient(timeout=self._config.timeout, verify=self._config.verify_ssl) as client:
                async with client.stream(
                    "POST", 
                    url, 
                    json=payload, 
                    headers=headers
                ) as response:
                    if not response.is_success:
                        error_msg = f"HTTP {response.status_code} error"
                        raise from_http_status(response.status_code, error_msg, response_body="")


                    async for line in response.aiter_lines():
                        if line.startswith("data:"):
                            data = line[len("data:"):].strip()
                            if data:
                                try:
                                    yield json.loads(data)
                                except json.JSONDecodeError:
                                    continue
                                    
        except httpx.RequestError as e:
            raise NetworkError(f"Network error during streaming: {e}", cause=e)
    
    async def _request(
        self, 
        method: str, 
        endpoint: str, 
        **kwargs
    ) -> httpx.Response:
        """Make HTTP request with retry logic."""
        url = f"{self._config.base_url}{endpoint}"
        last_exception = None
        
        for attempt in range(self._config.max_retries + 1):
            try:
                async with httpx.AsyncClient(
                    headers=self._headers, 
                    timeout=self._config.timeout,
                    verify=self._config.verify_ssl
                ) as client:
                    response = await client.request(method, url, **kwargs)
                    self._raise_for_status(response)
                    return response
                    
            except httpx.HTTPStatusError as e:
                if not self._should_retry(e.response.status_code, attempt):
                    self._raise_for_status(e.response)
                last_exception = e
                
            except httpx.RequestError as e:
                if attempt >= self._config.max_retries:
                    raise NetworkError(f"Request failed after {self._config.max_retries} retries: {e}", cause=e)
                last_exception = e
                
            # Exponential backoff
            if attempt < self._config.max_retries:
                sleep_time = self._config.retry_backoff ** attempt
                await asyncio.sleep(sleep_time)
        
        # Should not reach here, but fallback
        if last_exception:
            raise last_exception
        raise NetworkError("Request failed due to unknown error")
    
    def _should_retry(self, status_code: int, attempt: int) -> bool:
        """Determine if request should be retried."""
        if attempt >= self._config.max_retries:
            return False
        # Retry on server errors (5xx) and rate limits (429)
        return status_code >= 500 or status_code == 429
    
    def _raise_for_status(self, response: httpx.Response) -> None:
        """Raise appropriate exception for HTTP status."""
        if response.is_success:
            return
            
        try:
            response.raise_for_status()
        except httpx.HTTPStatusError as e:
            status_code = response.status_code
            message = f"HTTP {status_code} error"
            response_body = response.text
            
            # Try to extract error message from response
            try:
                error_data = response.json()
                if "message" in error_data:
                    message = error_data["message"]
                elif "error" in error_data:
                    message = error_data["error"]
            except (json.JSONDecodeError, ValueError):
                pass
            
            raise from_http_status(
                status_code, 
                message, 
                response_body=response_body,
                cause=e
            )