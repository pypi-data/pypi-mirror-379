"""MCP (Model Context Protocol) support for NCP SDK.

This module provides configuration for connecting to MCP servers,
allowing agents to access external tools and resources.
"""

from .config import MCPServerConfig, TransportType

__all__ = ["MCPServerConfig", "TransportType"]