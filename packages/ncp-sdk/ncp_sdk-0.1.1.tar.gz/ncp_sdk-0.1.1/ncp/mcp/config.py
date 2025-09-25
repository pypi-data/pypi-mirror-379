"""
MCP Server Configuration.

Configuration for MCP servers supporting all transport types.
"""

from typing import Dict, Optional, Any, List, Literal
from dataclasses import dataclass, field


TransportType = Literal["stdio", "sse", "streamable-http"]


@dataclass
class MCPServerConfig:
    """
    Configuration for MCP servers supporting all transport types.

    Supports:
    - STDIO: command-based transport
    - SSE: Server-Sent Events transport
    - Streamable HTTP: HTTP streaming transport

    Examples:
        # STDIO transport (local command)
        config = MCPServerConfig(
            transport_type="stdio",
            command="python",
            args=["-m", "my_mcp_server"],
            timeout=30.0
        )

        # SSE transport (Server-Sent Events)
        config = MCPServerConfig(
            transport_type="sse",
            url="https://mcp-server.example.com/sse",
            headers={"Authorization": "Bearer token"}
        )

        # Streamable HTTP transport
        config = MCPServerConfig(
            transport_type="streamable-http",
            url="https://mcp-server.example.com/stream",
            timeout=60.0
        )
    """

    transport_type: TransportType
    timeout: float = 30.0
    env: Optional[Dict[str, str]] = None  # Environment variables for all transports

    # STDIO transport fields
    command: Optional[str] = None
    args: List[str] = field(default_factory=list)
    cwd: Optional[str] = None

    # URL-based transport fields (SSE and Streamable HTTP)
    url: Optional[str] = None
    headers: Optional[Dict[str, str]] = None

    def __post_init__(self):
        """Validate configuration."""
        if self.timeout <= 0:
            raise ValueError("Timeout must be positive")

        if self.transport_type == "stdio":
            if not self.command:
                raise ValueError("Command is required for stdio transport")
        elif self.transport_type in ["sse", "streamable-http"]:
            if not self.url:
                raise ValueError(f"URL is required for {self.transport_type} transport")

        # Initialize empty dicts if None
        if self.env is None:
            self.env = {}
        if self.headers is None:
            self.headers = {}

    @property
    def is_stdio(self) -> bool:
        """Check if this is a stdio transport."""
        return self.transport_type == "stdio"

    @property
    def is_url_based(self) -> bool:
        """Check if this is a URL-based transport (SSE or streamable-http)."""
        return self.transport_type in ["sse", "streamable-http"]

    def get_command_list(self) -> List[str]:
        """Get the full command list for stdio transport."""
        if not self.is_stdio or not self.command:
            return []
        return [self.command] + self.args

    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary representation."""
        data = {
            "transport_type": self.transport_type,
            "timeout": self.timeout,
        }

        if self.env:
            data["env"] = self.env

        if self.is_stdio:
            data["command"] = self.command
            if self.args:
                data["args"] = self.args
            if self.cwd:
                data["cwd"] = self.cwd
        else:
            data["url"] = self.url
            if self.headers:
                data["headers"] = self.headers

        return data

    def __str__(self) -> str:
        """String representation."""
        if self.is_stdio:
            return f"MCPServerConfig(stdio: {self.command})"
        else:
            return f"MCPServerConfig({self.transport_type}: {self.url})"

    def __repr__(self) -> str:
        """Detailed representation."""
        if self.is_stdio:
            return (
                f"MCPServerConfig(transport_type='{self.transport_type}', "
                f"command='{self.command}', args={self.args}, timeout={self.timeout})"
            )
        else:
            return (
                f"MCPServerConfig(transport_type='{self.transport_type}', "
                f"url='{self.url}', timeout={self.timeout})"
            )