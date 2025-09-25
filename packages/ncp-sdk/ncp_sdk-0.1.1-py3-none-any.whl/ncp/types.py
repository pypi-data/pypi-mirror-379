"""NCP SDK Type definitions.

This module provides all the type definitions used throughout the NCP SDK
for type safety and IDE support during development.
"""

from typing import Any, Dict, List, Optional, Union, Callable, TYPE_CHECKING
from typing_extensions import TypedDict, Literal
from pydantic import BaseModel, Field, SkipValidation
from enum import Enum
from datetime import datetime

if TYPE_CHECKING:
    from .agents.config import ModelConfig





class ToolResult(BaseModel):
    """Result from a tool execution."""

    success: bool = Field(..., description="Whether the tool executed successfully")
    result: Any = Field(None, description="The actual result data")
    error: Optional[str] = Field(None, description="Error message if execution failed")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    execution_time: Optional[float] = Field(None, description="Execution time in seconds")
    timestamp: Optional[datetime] = Field(None, description="When the tool was executed")

    model_config = {"arbitrary_types_allowed": True}


class ToolDefinition(BaseModel):
    """Definition of a tool that can be used by agents."""
    
    name: str = Field(..., description="Tool name")
    description: str = Field(..., description="Tool description")
    function: SkipValidation[Callable] = Field(..., description="The actual function implementation")
    parameters: Dict[str, Any] = Field(default_factory=dict, description="Parameter schema")
    async_tool: bool = Field(False, description="Whether the tool is async")
    
    model_config = {"arbitrary_types_allowed": True}


class AgentConfig(BaseModel):
    """Configuration for an NCP Agent."""

    name: str = Field(..., description="Agent name")
    description: str = Field(..., description="Brief description of the agent")
    instructions: str = Field(..., description="Detailed instructions for the agent")
    llm_config: Optional["ModelConfig"] = Field(None, description="LLM configuration")
    tools: List[str] = Field(default_factory=list, description="List of tool names")
    mcp_servers: List[Union[str, Dict[str, Any]]] = Field(
        default_factory=list,
        description="MCP server configurations (URLs or config dicts)"
    )
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")

    model_config = {"extra": "forbid"}


class PackageManifest(BaseModel):
    """Manifest for an NCP package."""
    
    name: str = Field(..., description="Package name")
    version: str = Field(..., description="Package version")
    description: str = Field(..., description="Package description")
    author: Optional[str] = Field(None, description="Package author")
    license: Optional[str] = Field(None, description="Package license")
    dependencies: List[str] = Field(default_factory=list, description="Python dependencies")
    agents: List[str] = Field(default_factory=list, description="Agent module paths")
    tools: List[str] = Field(default_factory=list, description="Tool module paths")
    entry_point: Optional[str] = Field(None, description="Main entry point")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional metadata")
    
    model_config = {"extra": "forbid"}


class DeploymentConfig(BaseModel):
    """Configuration for deploying to NCP platform."""
    
    platform_url: str = Field(..., description="NCP platform URL")
    api_key: Optional[str] = Field(None, description="API key for authentication")
    project_id: Optional[str] = Field(None, description="Target project ID")
    environment: Literal["dev", "staging", "prod"] = Field("dev", description="Deployment environment")
    timeout: int = Field(300, description="Deployment timeout in seconds")
    
    model_config = {"extra": "forbid"}


# Type aliases for common patterns
ToolFunction = Callable[..., Any]
AsyncToolFunction = Callable[..., Any]  # Should be awaitable
ParameterSchema = Dict[str, Any]
SchemaDict = Dict[str, Any]

# Runtime types (what actually gets executed on platform)
class AgentRuntime(TypedDict):
    """Runtime representation of an agent on the platform."""
    id: str
    name: str
    status: Literal["active", "inactive", "error"]
    created_at: str
    updated_at: str
    

class ExecutionResult(TypedDict):
    """Result from executing an agent on the platform."""
    agent_id: str
    execution_id: str
    status: Literal["running", "completed", "failed"]
    result: Optional[str]
    error: Optional[str]
    started_at: str
    completed_at: Optional[str]
    

# Additional useful types for SDK users
class AgentStatus(str, Enum):
    """Status of an agent."""
    ACTIVE = "active"
    INACTIVE = "inactive"
    ERROR = "error"
    DEPLOYING = "deploying"
    UPDATING = "updating"


class ExecutionStatus(str, Enum):
    """Status of an agent execution."""
    RUNNING = "running"
    COMPLETED = "completed"
    FAILED = "failed"
    CANCELLED = "cancelled"


class LogLevel(str, Enum):
    """Logging levels for agent output."""
    DEBUG = "debug"
    INFO = "info"
    WARNING = "warning"
    ERROR = "error"
    CRITICAL = "critical"


class ToolExecutionResult(BaseModel):
    """Enhanced result from tool execution with timing and metadata."""

    tool_name: str = Field(..., description="Name of the executed tool")
    success: bool = Field(..., description="Whether execution was successful")
    result: Any = Field(None, description="Tool execution result")
    error: Optional[str] = Field(None, description="Error message if failed")
    execution_time_ms: float = Field(..., description="Execution time in milliseconds")
    timestamp: datetime = Field(default_factory=datetime.utcnow, description="Execution timestamp")
    metadata: Dict[str, Any] = Field(default_factory=dict, description="Additional execution metadata")

    model_config = {"arbitrary_types_allowed": True}


# Validation schemas
TOOL_PARAMETER_TYPES = {
    "string", "integer", "number", "boolean", "array", "object"
}