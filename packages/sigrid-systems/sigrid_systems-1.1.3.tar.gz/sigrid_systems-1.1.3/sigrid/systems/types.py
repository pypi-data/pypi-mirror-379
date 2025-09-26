"""
SIGRID Systems Types

Type definitions and data structures for SIGRID API.

Available Types:
    Document - Legal document for analysis
        - id: Document identifier (1-128 chars, URL-safe)
        - content: Document text (max 500KB per document)
        - metadata: Optional key-value pairs
    
    ClientConfig - Client configuration options
        - base_url: API endpoint URL
        - timeout: Request timeout (default 1200s)
        - max_retries: Retry attempts (default 3)
        - retry_backoff: Backoff multiplier (default 2.0)
    
    AnalysisEvent - Streaming analysis event
        - type: Event type ("connected", "sigrid_systems_response", etc.)
        - data: Event payload with route information
        - timestamp: Optional ISO timestamp
    
    AnalysisRequest - Analysis request configuration
        - documents: List of Document objects
        - query: Analysis query string
        - include_reasoning: Include LLM thinking steps

Usage:
    doc = types.Document(
        id="case_001",
        content="ECHR case content...",
        metadata={"filename": "application.pdf"}
    )
    
    config = types.ClientConfig(
        base_url="https://your-api.com",
        timeout=600
    )
"""

from typing import Dict, List, Any, Optional, Union, AsyncIterator
from dataclasses import dataclass, field
from enum import Enum
import base64
import re
from .exceptions import ValidationError

@dataclass(frozen=True)
class Document:
    """
    An immutable document for analysis. The content is always a string.
    To create an instance, use the `Document.create()` factory method.
    """
    id: str
    content: str
    metadata: Dict[str, Any] = field(default_factory=dict)

    def __post_init__(self):
        """Sanitize ID after initialization."""
        safe_id = re.sub(r'[^A-Za-z0-9._-]', '_', self.id)
        if safe_id != self.id:
            # Can't modify frozen dataclass, so we need to use object.__setattr__
            object.__setattr__(self, 'id', safe_id)

    @classmethod
    def create(
        cls,
        id: str,
        content: Union[str, bytes],
        metadata: Optional[Dict[str, Any]] = None
    ) -> "Document":
        """Creates a Document, automatically encoding bytes to base64 and sanitizing ID."""
        # Sanitize ID to be URL-safe (only A-Z a-z 0-9 . _ -)
        safe_id = re.sub(r'[^A-Za-z0-9._-]', '_', id)

        if isinstance(content, bytes):
            content = base64.b64encode(content).decode('utf-8')

        return cls(
            id=safe_id,
            content=content,
            metadata=metadata or {}
        )

    def to_dict(self) -> Dict[str, Any]:
        """Convert Document to a dictionary suitable for the API."""
        return {
            "id": self.id,
            "content": self.content,
            "metadata": self.metadata,
        }


@dataclass 
class AnalysisRequest:
    """Analysis request configuration."""
    documents: List[Document]
    query: str
    correlation_id: Optional[str] = None
    idempotency_key: Optional[str] = None


@dataclass(frozen=True)
class AnalysisEvent:
    """
    Event received during streaming analysis.
    
    Event Types:
        - "connected": Session established
        - "sigrid_systems_response": Main content events with routes:
            * "sigrid_system_analysis": Final analysis content
        - "heartbeat": Keep-alive every 15 seconds
        - "error": Analysis errors
    """
    type: str
    data: Dict[str, Any]
    timestamp: Optional[str] = None
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "AnalysisEvent":
        """Create AnalysisEvent from dictionary."""
        return cls(
            type=data.get("type", "unknown"),
            data=data,  # Use the whole event as data
            timestamp=data.get("timestamp")
        )


@dataclass
class ClientConfig:
    """Client configuration options."""
    base_url: str = "https://sigrid-systems.com"
    timeout: int = 1200  # Match backend timeout (20 minutes)
    max_retries: int = 3
    retry_backoff: float = 2.0
    verify_ssl: bool = True


class EventType(Enum):
    """Analysis event types."""
    STARTED = "analysis_started"
    PROGRESS = "analysis_progress" 
    RESULT = "analysis_result"
    COMPLETED = "analysis_completed"
    ERROR = "analysis_error"


# Type aliases for convenience
Documents = List[Union[Document, Dict[str, Any]]]
Events = AsyncIterator[AnalysisEvent]
RawEvents = AsyncIterator[Dict[str, Any]]