"""MCP评估服务器包初始化"""

from .main import mcp, search_mcp_tools, health_check

__version__ = "0.2.2"
__all__ = [
    "mcp",
    "search_mcp_tools", 
    "health_check"
]