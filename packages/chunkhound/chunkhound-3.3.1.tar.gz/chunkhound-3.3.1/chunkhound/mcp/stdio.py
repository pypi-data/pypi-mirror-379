"""Stdio MCP server implementation using the base class pattern.

This module implements the stdio (stdin/stdout) JSON-RPC protocol for MCP,
inheriting common initialization and lifecycle management from MCPServerBase.

CRITICAL: NO stdout output allowed - breaks JSON-RPC protocol
ARCHITECTURE: Global state required for stdio communication model
"""

import asyncio
import logging
import sys
import warnings

# CRITICAL: Suppress SWIG warnings that break JSON-RPC protocol in CI
# The DuckDB Python bindings generate a DeprecationWarning that goes to stdout
# in some environments (Ubuntu CI with Python 3.12), breaking MCP protocol
warnings.filterwarnings(
    "ignore", message=".*swigvarlink.*", category=DeprecationWarning
)
from collections.abc import AsyncIterator
from contextlib import asynccontextmanager
from typing import Any

import mcp.server.stdio
import mcp.types as types
from mcp.server import Server
from mcp.server.models import InitializationOptions

from chunkhound.core.config.config import Config
from chunkhound.version import __version__

from .base import MCPServerBase
from .common import handle_tool_call
from .tools import TOOL_REGISTRY

# CRITICAL: Disable ALL logging to prevent JSON-RPC corruption
logging.disable(logging.CRITICAL)
for logger_name in ["", "mcp", "server", "fastmcp"]:
    logging.getLogger(logger_name).setLevel(logging.CRITICAL + 1)

# Disable loguru logger
try:
    from loguru import logger as loguru_logger

    loguru_logger.remove()
    loguru_logger.add(lambda _: None, level="CRITICAL")
except ImportError:
    pass


class StdioMCPServer(MCPServerBase):
    """MCP server implementation for stdio protocol.

    Uses global state as required by the stdio protocol's persistent
    connection model. All initialization happens eagerly during startup.
    """

    def __init__(self, config: Config, args: Any = None):
        """Initialize stdio MCP server.

        Args:
            config: Validated configuration object
            args: Original CLI arguments for direct path access
        """
        super().__init__(config, args=args)

        # Create MCP server instance
        self.server: Server = Server("ChunkHound Code Search")

        # Event to signal initialization completion
        self._initialization_complete = asyncio.Event()

        # Register tools with the server
        self._register_tools()

    def _register_tools(self) -> None:
        """Register tool handlers with the stdio server."""

        # The MCP SDK's call_tool decorator expects a SINGLE handler function
        # with signature (tool_name: str, arguments: dict) that handles ALL tools

        @self.server.call_tool()  # type: ignore[misc]
        async def handle_all_tools(
            tool_name: str, arguments: dict[str, Any]
        ) -> list[types.TextContent]:
            """Universal tool handler that routes to the unified handler."""
            return await handle_tool_call(
                tool_name=tool_name,
                arguments=arguments,
                services=self.ensure_services(),
                embedding_manager=self.embedding_manager,
                initialization_complete=self._initialization_complete,
                debug_mode=self.debug_mode,
                scan_progress=self._scan_progress,
            )

        self._register_list_tools()

    def _register_list_tools(self) -> None:
        """Register list_tools handler."""

        @self.server.list_tools()  # type: ignore[misc]
        async def list_tools() -> list[types.Tool]:
            """List available tools."""
            # Wait for initialization
            try:
                await asyncio.wait_for(
                    self._initialization_complete.wait(), timeout=5.0
                )
            except asyncio.TimeoutError:
                # Return basic tools even if not fully initialized
                pass

            tools = []
            for tool_name, tool in TOOL_REGISTRY.items():
                # Skip embedding-dependent tools if no providers available
                if tool.requires_embeddings and (
                    not self.embedding_manager
                    or not self.embedding_manager.list_providers()
                ):
                    continue

                tools.append(
                    types.Tool(
                        name=tool_name,
                        description=tool.description,
                        inputSchema=tool.parameters,
                    )
                )

            return tools

    @asynccontextmanager
    async def server_lifespan(self) -> AsyncIterator[dict]:
        """Manage server lifecycle with proper initialization and cleanup."""
        try:
            # Initialize services
            await self.initialize()
            self._initialization_complete.set()
            self.debug_log("Server initialization complete")

            # Yield control to server
            yield {"services": self.services, "embeddings": self.embedding_manager}

        finally:
            # Cleanup on shutdown
            await self.cleanup()

    async def run(self) -> None:
        """Run the stdio server with proper lifecycle management."""
        try:
            # Set initialization options with capabilities
            from mcp.server.lowlevel import NotificationOptions

            init_options = InitializationOptions(
                server_name="ChunkHound Code Search",
                server_version=__version__,
                capabilities=self.server.get_capabilities(
                    notification_options=NotificationOptions(),
                    experimental_capabilities={},
                ),
            )

            # Run with lifespan management
            async with self.server_lifespan():
                # Run the stdio server
                async with mcp.server.stdio.stdio_server() as (
                    read_stream,
                    write_stream,
                ):
                    self.debug_log("Stdio server started, awaiting requests")
                    await self.server.run(
                        read_stream,
                        write_stream,
                        init_options,
                    )

        except KeyboardInterrupt:
            self.debug_log("Server interrupted by user")
        except Exception as e:
            self.debug_log(f"Server error: {e}")
            if self.debug_mode:
                import traceback

                traceback.print_exc(file=sys.stderr)


async def main(args: Any = None) -> None:
    """Main entry point for the MCP stdio server.

    Args:
        args: Pre-parsed arguments. If None, will parse from sys.argv.
    """
    import argparse

    from chunkhound.api.cli.utils.config_factory import create_validated_config
    from chunkhound.mcp.common import add_common_mcp_arguments

    if args is None:
        # Direct invocation - parse arguments
        parser = argparse.ArgumentParser(
            description="ChunkHound MCP stdio server",
            formatter_class=argparse.RawDescriptionHelpFormatter,
        )
        # Add common MCP arguments
        add_common_mcp_arguments(parser)
        # Parse arguments
        args = parser.parse_args()

    # Create and validate configuration
    config, validation_errors = create_validated_config(args, "mcp")

    if validation_errors:
        # CRITICAL: Cannot print to stderr in MCP mode - breaks JSON-RPC protocol
        # Exit silently with error code
        sys.exit(1)

    # Create and run the stdio server
    try:
        server = StdioMCPServer(config, args=args)
        await server.run()
    except Exception:
        # CRITICAL: Cannot print to stderr in MCP mode - breaks JSON-RPC protocol
        # Exit silently with error code
        sys.exit(1)


def main_sync() -> None:
    """Synchronous wrapper for CLI entry point."""
    asyncio.run(main())


if __name__ == "__main__":
    main_sync()
