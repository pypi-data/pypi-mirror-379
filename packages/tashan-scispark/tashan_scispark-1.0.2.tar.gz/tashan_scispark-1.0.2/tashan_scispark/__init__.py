"""
TaShan SciSpark - Academic Research Assistant MCP Server

A comprehensive academic research assistant that provides:
- Paper search and analysis
- Keyword extraction
- Research idea generation
- Research review and evaluation
- Paper content compression

This package can be used as an MCP server for Claude Desktop or as a standalone tool.
"""

__version__ = "1.0.0"
__author__ = "TaShan SciSpark Team"
__email__ = "support@tashan-scispark.com"
__description__ = "Academic Research Assistant MCP Server"

# 导出主要功能
from .mcp_server import main as run_mcp_server
from .cli import main as run_cli

__all__ = [
    "__version__",
    "__author__", 
    "__email__",
    "__description__",
    "run_mcp_server",
    "run_cli",
]