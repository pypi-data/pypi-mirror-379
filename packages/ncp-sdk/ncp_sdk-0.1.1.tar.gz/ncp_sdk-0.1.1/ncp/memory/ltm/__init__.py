"""Long-term memory types and configurations."""

from .types import (
    # Core LTM types
    LTMConfig,
    MemoryChunk,
    RetrievalResult,
    IngestionResult,

    # Enums
    ChunkingStrategy,
    RetrievalStrategy,
    IngestionTrigger,

    # Errors
    LTMError,
    VectorStoreError,
    ChunkingError,
    RetrievalError,
)

__all__ = [
    # Core types
    "LTMConfig",
    "MemoryChunk",
    "RetrievalResult",
    "IngestionResult",

    # Enums
    "ChunkingStrategy",
    "RetrievalStrategy",
    "IngestionTrigger",

    # Errors
    "LTMError",
    "VectorStoreError",
    "ChunkingError",
    "RetrievalError",
]