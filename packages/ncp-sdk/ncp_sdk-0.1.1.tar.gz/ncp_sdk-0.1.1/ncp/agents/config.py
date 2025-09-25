"""Model configuration for NCP SDK agents."""

from dataclasses import dataclass
from typing import Optional, Dict, Any
from pydantic import BaseModel, Field, validator


class ModelConfig(BaseModel):
    """Configuration for LLM models used by agents (user-configurable parameters only).

    This class provides type-safe configuration for LLM generation parameters
    that users are allowed to modify. API keys and base URLs are managed by the platform.

    Example:
        config = ModelConfig(
            model="gpt-4-turbo",
            temperature=0.7,
            max_tokens=2000
        )
    """

    model: str = Field(..., description="Model identifier (e.g., 'gpt-4', 'claude-3-opus')")
    temperature: float = Field(0.7, ge=0.0, le=2.0, description="Sampling temperature")
    max_tokens: Optional[int] = Field(None, description="Maximum tokens to generate")
    top_p: float = Field(1.0, ge=0.0, le=1.0, description="Nucleus sampling parameter")
    frequency_penalty: float = Field(0.0, ge=-2.0, le=2.0, description="Frequency penalty")
    presence_penalty: float = Field(0.0, ge=-2.0, le=2.0, description="Presence penalty")

    model_config = {"extra": "forbid", "validate_assignment": True}
    
    @validator('model')
    def validate_model(cls, v: str) -> str:
        """Validate model name against known providers."""
        if not v:
            raise ValueError("Model name cannot be empty")
        return v
    
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary for serialization."""
        data = {
            "model": self.model,
            "temperature": self.temperature,
            "top_p": self.top_p,
            "frequency_penalty": self.frequency_penalty,
            "presence_penalty": self.presence_penalty,
        }
        if self.max_tokens:
            data["max_tokens"] = self.max_tokens
        return data
    
    def to_completion_kwargs(self) -> Dict[str, Any]:
        """Convert to completion API kwargs (generation parameters only)."""
        kwargs = {
            "model": self.model,
            "temperature": self.temperature,
            "top_p": self.top_p,
            "frequency_penalty": self.frequency_penalty,
            "presence_penalty": self.presence_penalty,
        }
        if self.max_tokens:
            kwargs["max_tokens"] = self.max_tokens
        return kwargs




