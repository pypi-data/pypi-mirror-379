"""
Server adapters for different MCP server implementations.

This module contains adapter classes that provide a unified interface
for interacting with different types of MCP servers.
"""

import logging
from abc import ABC, abstractmethod
from typing import Any, Callable, Optional, Protocol, runtime_checkable
from datetime import datetime, timezone

from mcp import ServerResult
from mcp.types import CallToolRequest
from .utils import is_mcp_error_response

logger = logging.getLogger("agnost.analytics.adapters")


@runtime_checkable
class SessionInfo(Protocol):
    """Protocol for session information."""
    session_key: str
    client_name: str


class ServerAdapter(ABC):
    """Abstract base class for MCP server adapters."""

    @abstractmethod
    def get_session_info(self) -> Optional[SessionInfo]:
        """Get session information from the server."""
        pass

    @abstractmethod
    def patch_server(self, analytics_callback: Callable) -> bool:
        """Patch the server to intercept tool calls."""
        pass


class FastMCPAdapter(ServerAdapter):
    """Adapter for FastMCP servers."""

    def __init__(self, server: Any):
        self.server = server
        self._mcp_server = server._mcp_server

    def get_session_info(self) -> Optional[SessionInfo]:
        """Get session info from FastMCP server."""
        try:
            if hasattr(self._mcp_server, 'request_context') and self._mcp_server.request_context:
                if hasattr(self._mcp_server.request_context, 'session') and self._mcp_server.request_context.session:
                    session = self._mcp_server.request_context.session
                    return type('SessionInfo', (), {
                        'session_key': hex(id(session)),
                        'client_name': session.client_params.clientInfo.name
                    })()
            return type('SessionInfo', (), {
                'session_key': 'fastmcp_default',
                'client_name': 'fastmcp_client'
            })()
        except Exception as e:
            logger.debug(f"FastMCP session info error: {e}")
            return None

    def patch_server(self, analytics_callback: Callable) -> bool:
        """Patch FastMCP server tool manager."""
        try:
            tool_manager = self.server._tool_manager
            original_call_tool = tool_manager.call_tool

            async def patched_call_tool(*args, **kwargs):
                tool_name = kwargs.get('key', kwargs.get('name', 'unknown_tool'))
                arguments = kwargs.get('arguments', {})

                start_time = datetime.now(timezone.utc)
                success = True
                result = None

                try:
                    exec_start = datetime.now(timezone.utc)
                    result = await original_call_tool(*args, **kwargs)
                    exec_end = datetime.now(timezone.utc)
                    exec_time = int((exec_end - exec_start).total_seconds() * 1000)

                    is_error, error_message = is_mcp_error_response(result)
                    if is_error:
                        success = False
                        logger.error(f"Tool {tool_name} returned error: {error_message}")

                except Exception as e:
                    success = False
                    exec_time = int((datetime.now(timezone.utc) - start_time).total_seconds() * 1000)
                    logger.error(f"Error calling tool {tool_name}: {e}")
                    raise
                finally:
                    analytics_callback(tool_name, arguments, exec_time, success, result, start_time)

                return result

            tool_manager.call_tool = patched_call_tool
            logger.debug("FastMCP server patched successfully")
            return True
        except Exception as e:
            logger.error(f"Failed to patch FastMCP server: {e}")
            return False


class LowLevelMCPAdapter(ServerAdapter):
    """Adapter for low-level MCP servers."""

    def __init__(self, server: Any):
        self.server = server._mcp_server if hasattr(server, '_mcp_server') else server

    def get_session_info(self) -> Optional[SessionInfo]:
        """Get session info from low-level MCP server."""
        try:
            if hasattr(self.server, 'request_context') and self.server.request_context:
                if hasattr(self.server.request_context, 'session') and self.server.request_context.session:
                    session = self.server.request_context.session
                    return type('SessionInfo', (), {
                        'session_key': hex(id(session)),
                        'client_name': session.client_params.clientInfo.name
                    })()
            return type('SessionInfo', (), {
                'session_key': 'lowlevel_default',
                'client_name': 'lowlevel_client'
            })()
        except Exception as e:
            logger.debug(f"LowLevel MCP session info error: {e}")
            return None

    def patch_server(self, analytics_callback: Callable) -> bool:
        """Patch low-level MCP server request handlers."""
        try:
            original_handler = self.server.request_handlers.get(CallToolRequest)
            if not original_handler:
                logger.error("No CallToolRequest handler found")
                return False

            async def wrapped_handler(request: CallToolRequest) -> ServerResult:
                tool_name = request.params.name
                arguments = request.params.arguments or {}

                start_time = datetime.now(timezone.utc)
                success = True
                result = None

                try:
                    exec_start = datetime.now(timezone.utc)
                    result = await original_handler(request)
                    exec_end = datetime.now(timezone.utc)
                    exec_time = int((exec_end - exec_start).total_seconds() * 1000)

                    is_error, error_message = is_mcp_error_response(result)
                    if is_error:
                        success = False
                        logger.error(f"Tool {tool_name} returned error: {error_message}")

                except Exception as e:
                    success = False
                    exec_time = int((datetime.now(timezone.utc) - start_time).total_seconds() * 1000)
                    logger.error(f"Error calling tool {tool_name}: {e}")
                    raise
                finally:
                    analytics_callback(tool_name, arguments, exec_time, success, result, start_time)

                return result

            self.server.request_handlers[CallToolRequest] = wrapped_handler
            logger.debug("Low-level MCP server patched successfully")
            return True
        except Exception as e:
            logger.error(f"Failed to patch low-level MCP server: {e}")
            return False