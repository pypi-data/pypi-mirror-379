"""Memory presets for common use cases."""

from .types import MemoryConfig, STMStrategy
from .ltm.types import LTMConfig, ChunkingStrategy, RetrievalStrategy, IngestionTrigger


class MemoryPresets:
    """Pre-configured memory settings for common use cases."""

    @staticmethod
    def basic_stm_only(max_messages: int = 30) -> MemoryConfig:
        """Basic short-term memory only configuration.

        Args:
            max_messages: Maximum number of messages to keep in STM

        Returns:
            MemoryConfig with only STM enabled
        """
        return MemoryConfig(
            stm_enabled=True,
            stm_strategy=STMStrategy.LAST_N_MESSAGES,
            stm_config={"max_messages": max_messages},
            ltm_enabled=False,
        )

    @staticmethod
    def token_window_stm(max_tokens: int = 4000) -> MemoryConfig:
        """Token window based short-term memory.

        Args:
            max_tokens: Maximum tokens to keep in STM

        Returns:
            MemoryConfig with token window STM strategy
        """
        return MemoryConfig(
            stm_enabled=True,
            stm_strategy=STMStrategy.TOKEN_WINDOW,
            stm_config={"max_tokens": max_tokens},
            ltm_enabled=False,
        )

    @staticmethod
    def adaptive_summary_stm(
        max_messages: int = 50,
        summary_trigger: int = 30
    ) -> MemoryConfig:
        """Adaptive summary based short-term memory.

        Args:
            max_messages: Maximum messages before triggering summary
            summary_trigger: Number of messages to trigger summary

        Returns:
            MemoryConfig with adaptive summary STM strategy
        """
        return MemoryConfig(
            stm_enabled=True,
            stm_strategy=STMStrategy.ADAPTIVE_SUMMARY,
            stm_config={
                "max_messages": max_messages,
                "summary_trigger": summary_trigger,
            },
            ltm_enabled=False,
        )

    @staticmethod
    def basic_ltm_only(collection_name: str = "agent_memory") -> MemoryConfig:
        """Basic long-term memory only configuration.

        Args:
            collection_name: Name of the vector database collection

        Returns:
            MemoryConfig with only LTM enabled
        """
        return MemoryConfig(
            stm_enabled=False,
            ltm_enabled=True,
            ltm_config=LTMConfig(
                enabled=True,
                collection_name=collection_name,
                chunking_strategy=ChunkingStrategy.TURN_BASED,
                retrieval_strategy=RetrievalStrategy.SEMANTIC,
                max_retrieved_chunks=5,
            ),
        )

    @staticmethod
    def hybrid_memory(
        stm_max_messages: int = 20,
        ltm_collection: str = "agent_memory",
        coordination: bool = True
    ) -> MemoryConfig:
        """Hybrid STM + LTM configuration with coordination.

        Args:
            stm_max_messages: Maximum messages in STM
            ltm_collection: LTM collection name
            coordination: Enable STM-LTM coordination

        Returns:
            MemoryConfig with both STM and LTM enabled
        """
        return MemoryConfig(
            stm_enabled=True,
            stm_strategy=STMStrategy.HYBRID,
            stm_config={"max_messages": stm_max_messages},
            ltm_enabled=True,
            ltm_config=LTMConfig(
                enabled=True,
                collection_name=ltm_collection,
                chunking_strategy=ChunkingStrategy.TURN_BASED,
                retrieval_strategy=RetrievalStrategy.HYBRID,
                max_retrieved_chunks=3,
                auto_ingest=True,
                ingestion_triggers=[
                    IngestionTrigger.ON_SUMMARY,
                    IngestionTrigger.SESSION_END
                ],
            ),
            stm_ltm_coordination=coordination,
            memory_priority="relevance",
        )

    @staticmethod
    def conversational_agent(
        max_messages: int = 40,
        enable_cross_session: bool = False
    ) -> MemoryConfig:
        """Configuration optimized for conversational agents.

        Args:
            max_messages: Maximum messages to keep in conversation
            enable_cross_session: Enable cross-session context

        Returns:
            MemoryConfig optimized for conversations
        """
        return MemoryConfig(
            stm_enabled=True,
            stm_strategy=STMStrategy.ADAPTIVE_SUMMARY,
            stm_config={
                "max_messages": max_messages,
                "summary_trigger": max_messages // 2,
            },
            ltm_enabled=enable_cross_session,
            ltm_config=LTMConfig(
                enabled=enable_cross_session,
                collection_name="conversation_memory",
                chunking_strategy=ChunkingStrategy.TURN_BASED,
                retrieval_strategy=RetrievalStrategy.SEMANTIC,
                max_retrieved_chunks=3,
                similarity_threshold=0.75,
                auto_ingest=True,
                ingestion_triggers=[IngestionTrigger.ON_SUMMARY],
                recency_weight=0.2,
                importance_weight=0.1,
            ) if enable_cross_session else None,
            stm_ltm_coordination=enable_cross_session,
            cross_session_context=enable_cross_session,
        )

    @staticmethod
    def research_agent(
        max_chunks: int = 10,
        chunk_size: int = 1000
    ) -> MemoryConfig:
        """Configuration optimized for research and analysis agents.

        Args:
            max_chunks: Maximum chunks to retrieve from LTM
            chunk_size: Size of each memory chunk

        Returns:
            MemoryConfig optimized for research tasks
        """
        return MemoryConfig(
            stm_enabled=True,
            stm_strategy=STMStrategy.TOKEN_WINDOW,
            stm_config={"max_tokens": 6000},
            ltm_enabled=True,
            ltm_config=LTMConfig(
                enabled=True,
                collection_name="research_memory",
                chunking_strategy=ChunkingStrategy.SEMANTIC,
                chunk_size=chunk_size,
                retrieval_strategy=RetrievalStrategy.HYBRID,
                max_retrieved_chunks=max_chunks,
                similarity_threshold=0.6,
                enable_reranking=True,
                auto_ingest=True,
                ingestion_triggers=[
                    IngestionTrigger.IMPORTANT_INFO,
                    IngestionTrigger.SESSION_END
                ],
                recency_weight=0.1,
                importance_weight=0.3,
            ),
            stm_ltm_coordination=True,
            memory_priority="importance",
        )

    @staticmethod
    def task_oriented_agent(max_messages: int = 25) -> MemoryConfig:
        """Configuration optimized for task-oriented agents.

        Args:
            max_messages: Maximum messages in working memory

        Returns:
            MemoryConfig optimized for task execution
        """
        return MemoryConfig(
            stm_enabled=True,
            stm_strategy=STMStrategy.LAST_N_MESSAGES,
            stm_config={"max_messages": max_messages},
            ltm_enabled=False,
            memory_priority="recency",
        )