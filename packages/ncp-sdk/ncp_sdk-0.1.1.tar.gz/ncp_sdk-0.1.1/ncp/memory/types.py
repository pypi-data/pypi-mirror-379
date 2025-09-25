"""Memory types and data structures for NCP agents."""

from dataclasses import dataclass, field
from enum import Enum
from typing import Any, Dict, List, Optional, Union


class STMStrategy(Enum):
    """Short-term memory strategies."""
    LAST_N_MESSAGES = "last_n_messages"
    TOKEN_WINDOW = "token_window"
    ADAPTIVE_SUMMARY = "adaptive_summary"
    HYBRID = "hybrid"


@dataclass
class MemoryEntry:
    """Represents a single memory entry."""
    role: str
    content: Optional[str]
    timestamp: float
    tokens: int = 0
    tool_calls: Optional[List[Dict[str, Any]]] = None
    tool_call_id: Optional[str] = None
    name: Optional[str] = None
    metadata: Dict[str, Any] = field(default_factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        """Convert to OpenAI message format."""
        msg = {"role": self.role}

        if self.content is not None:
            msg["content"] = self.content

        if self.tool_calls:
            msg["tool_calls"] = self.tool_calls

        if self.tool_call_id:
            msg["tool_call_id"] = self.tool_call_id

        if self.name:
            msg["name"] = self.name

        return msg


@dataclass
class MemoryConfig:
    """Configuration for agent memory system."""

    # Short-term memory settings
    stm_enabled: bool = True
    stm_strategy: STMStrategy = STMStrategy.LAST_N_MESSAGES
    stm_config: Dict[str, Any] = field(default_factory=lambda: {"max_messages": 30})

    # Long-term memory settings
    ltm_enabled: bool = False
    ltm_config: Optional["LTMConfig"] = None

    # Coordination settings
    stm_ltm_coordination: bool = False
    memory_priority: str = "relevance"  # relevance, recency, importance
    cross_session_context: bool = False


@dataclass
class MemoryStats:
    """Memory system statistics."""
    stm_message_count: int = 0
    stm_token_count: int = 0
    ltm_chunk_count: int = 0
    ltm_chunks_stored: int = 0
    ltm_chunks_retrieved: int = 0
    ltm_retrievals_performed: int = 0
    total_messages_processed: int = 0
    summarization_events: int = 0
    last_cleanup: Optional[float] = None
    last_ltm_ingestion: Optional[float] = None


class MemoryError(Exception):
    """Base exception for memory-related errors."""
    pass


class TokenLimitError(MemoryError):
    """Raised when token limits are exceeded."""
    pass


class StrategyError(MemoryError):
    """Raised when memory strategy encounters an error."""
    pass