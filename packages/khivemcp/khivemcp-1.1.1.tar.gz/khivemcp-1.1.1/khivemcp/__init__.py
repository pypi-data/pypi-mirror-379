# khivemcp/__init__.py
"""khivemcp: Configuration-driven MCP server framework using FastMCP."""

# Expose key components for users importing the library
from .decorators import operation
from .types import GroupConfig, ServiceConfig, ServiceGroup

__version__ = "1.1.1"

__all__ = [
    "operation",
    "ServiceConfig",
    "GroupConfig",
    "ServiceGroup",
]
