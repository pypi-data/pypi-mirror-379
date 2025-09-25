"""Types and configurations for long-term memory."""

from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum
from typing import Any, Dict, List, Optional


class ChunkingStrategy(Enum):
    """Document chunking strategies."""
    TURN_BASED = "turn_based"
    TOKEN_BASED = "token_based"
    SEMANTIC = "semantic"
    SLIDING_WINDOW = "sliding_window"


class RetrievalStrategy(Enum):
    """Memory retrieval strategies."""
    SEMANTIC = "semantic"
    HYBRID = "hybrid"
    METADATA_FILTERED = "metadata_filtered"


class IngestionTrigger(Enum):
    """Triggers for memory ingestion."""
    MANUAL = "manual"
    ON_SUMMARY = "on_summary"
    SESSION_END = "session_end"
    IMPORTANT_INFO = "important_info"
    PERIODIC = "periodic"


@dataclass
class LTMConfig:
    """Configuration for long-term memory."""

    # Connection settings
    enabled: bool = False
    host: str = "localhost"
    port: int = 8000
    collection_name: str = "agent_memory"

    # Embedding settings
    embedding_model: str = "text-embedding-3-small"
    embedding_dimension: int = 1536

    # Ingestion settings
    auto_ingest: bool = True
    ingestion_triggers: List[IngestionTrigger] = field(
        default_factory=lambda: [IngestionTrigger.ON_SUMMARY, IngestionTrigger.SESSION_END]
    )
    chunking_strategy: ChunkingStrategy = ChunkingStrategy.TURN_BASED
    chunk_size: int = 500
    chunk_overlap: int = 50

    # Retrieval settings
    retrieval_strategy: RetrievalStrategy = RetrievalStrategy.SEMANTIC
    max_retrieved_chunks: int = 5
    similarity_threshold: float = 0.7
    include_metadata: bool = True

    # Memory management
    max_memories: int = 10000
    cleanup_strategy: str = "lru"  # lru, fifo, importance
    memory_decay: bool = False
    decay_factor: float = 0.95

    # Advanced settings
    enable_reranking: bool = True
    recency_weight: float = 0.1
    importance_weight: float = 0.2


@dataclass
class MemoryChunk:
    """Represents a chunk of memory stored in the vector database."""

    # Core content
    content: str
    embedding: Optional[List[float]] = None

    # Metadata
    chunk_id: str = ""
    session_id: str = ""
    timestamp: datetime = field(default_factory=datetime.utcnow)

    # Context information
    message_roles: List[str] = field(default_factory=list)
    turn_count: int = 0
    token_count: int = 0

    # Importance and quality metrics
    importance_score: float = 0.0
    quality_score: float = 1.0
    access_count: int = 0
    last_accessed: Optional[datetime] = None

    # Custom metadata
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for storage."""
        return {
            "content": self.content,
            "chunk_id": self.chunk_id,
            "session_id": self.session_id,
            "timestamp": self.timestamp.isoformat(),
            "message_roles": self.message_roles,
            "turn_count": self.turn_count,
            "token_count": self.token_count,
            "importance_score": self.importance_score,
            "quality_score": self.quality_score,
            "access_count": self.access_count,
            "last_accessed": self.last_accessed.isoformat() if self.last_accessed else None,
            **self.metadata
        }

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "MemoryChunk":
        """Create from dictionary."""
        # Extract custom metadata (anything not in the standard fields)
        standard_fields = {
            "content", "chunk_id", "session_id", "timestamp", "message_roles",
            "turn_count", "token_count", "importance_score", "quality_score",
            "access_count", "last_accessed"
        }
        metadata = {k: v for k, v in data.items() if k not in standard_fields}

        return cls(
            content=data.get("content", ""),
            chunk_id=data.get("chunk_id", ""),
            session_id=data.get("session_id", ""),
            timestamp=datetime.fromisoformat(data.get("timestamp", datetime.utcnow().isoformat())),
            message_roles=data.get("message_roles", []),
            turn_count=data.get("turn_count", 0),
            token_count=data.get("token_count", 0),
            importance_score=data.get("importance_score", 0.0),
            quality_score=data.get("quality_score", 1.0),
            access_count=data.get("access_count", 0),
            last_accessed=datetime.fromisoformat(data["last_accessed"]) if data.get("last_accessed") else None,
            metadata=metadata
        )


@dataclass
class RetrievalResult:
    """Result of memory retrieval operation."""

    chunk: MemoryChunk
    similarity_score: float
    relevance_score: float = 0.0  # Computed relevance (similarity + recency + importance)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "chunk": self.chunk.to_dict(),
            "similarity_score": self.similarity_score,
            "relevance_score": self.relevance_score,
        }


@dataclass
class IngestionResult:
    """Result of memory ingestion operation."""

    chunks_stored: int
    chunks_updated: int
    chunks_skipped: int
    errors: List[str] = field(default_factory=list)

    @property
    def success(self) -> bool:
        """Whether the ingestion was successful."""
        return len(self.errors) == 0

    @property
    def total_processed(self) -> int:
        """Total chunks processed."""
        return self.chunks_stored + self.chunks_updated + self.chunks_skipped


class LTMError(Exception):
    """Base exception for LTM-related errors."""
    pass


class VectorStoreError(LTMError):
    """Exception for vector store operations."""
    pass


class ChunkingError(LTMError):
    """Exception for document chunking operations."""
    pass


class RetrievalError(LTMError):
    """Exception for memory retrieval operations."""
    pass