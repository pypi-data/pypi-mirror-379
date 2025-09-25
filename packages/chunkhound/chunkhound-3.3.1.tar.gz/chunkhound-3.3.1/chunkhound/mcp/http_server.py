"""HTTP MCP server implementation using the base class pattern.

This module implements the HTTP transport for MCP using FastMCP,
inheriting common initialization and lifecycle management from MCPServerBase.

Unlike stdio, HTTP servers can use lazy initialization and don't require
global state management.
"""

from typing import Any

from fastmcp import FastMCP

from chunkhound.core.config.config import Config

from .base import MCPServerBase
from .common import parse_mcp_arguments
from .tools import execute_tool


class HttpMCPServer(MCPServerBase):
    """MCP server implementation for HTTP protocol using FastMCP.

    Uses lazy initialization pattern - services are initialized on first
    request rather than at startup. This is more suitable for HTTP's
    request/response model.
    """

    def __init__(self, config: Config, port: int = 5173):
        """Initialize HTTP MCP server.

        Args:
            config: Validated configuration object
            port: Port to listen on (default: 5173)
        """
        super().__init__(config)
        self.port = port

        # Create FastMCP instance
        self.app: FastMCP = FastMCP("ChunkHound Code Search")

        # Register tools with the server
        self._register_tools()

    def _register_tools(self) -> None:
        """Register all tools from the registry with FastMCP."""
        # FastMCP requires explicit function signatures, not **kwargs
        # So we create specific handler functions for each tool

        @self.app.tool()
        async def get_stats() -> dict[str, Any]:
            """Get database statistics including file, chunk, and embedding counts"""
            await self.initialize()
            result = await execute_tool(
                tool_name="get_stats",
                services=self.ensure_services(),
                embedding_manager=self.embedding_manager,
                arguments={},
                scan_progress=self._scan_progress,
            )
            return dict(result) if hasattr(result, "__dict__") else result

        @self.app.tool()
        async def health_check() -> dict[str, Any]:
            """Check server health status"""
            await self.initialize()
            result = await execute_tool(
                tool_name="health_check",
                services=self.ensure_services(),
                embedding_manager=self.embedding_manager,
                arguments={},
            )
            return dict(result) if hasattr(result, "__dict__") else result

        @self.app.tool()
        async def search_regex(
            pattern: str,
            page_size: int = 10,
            offset: int = 0,
            max_response_tokens: int = 20000,
            path: str | None = None,
        ) -> dict[str, Any]:
            """Search code chunks using regex patterns with pagination support."""
            await self.initialize()

            # Build arguments dict
            args = {
                "pattern": pattern,
                "page_size": page_size,
                "offset": offset,
                "max_response_tokens": max_response_tokens,
            }
            if path is not None:
                args["path"] = path

            result = await execute_tool(
                tool_name="search_regex",
                services=self.ensure_services(),
                embedding_manager=self.embedding_manager,
                arguments=parse_mcp_arguments(args),
            )
            return dict(result) if hasattr(result, "__dict__") else result

        @self.app.tool()
        async def search_semantic(
            query: str,
            page_size: int = 10,
            offset: int = 0,
            max_response_tokens: int = 20000,
            path: str | None = None,
            provider: str = "openai",
            model: str = "text-embedding-3-small",
            threshold: float | None = None,
        ) -> dict[str, Any]:
            """Search code using semantic similarity with pagination support."""
            await self.initialize()

            # Build arguments dict
            args = {
                "query": query,
                "page_size": page_size,
                "offset": offset,
                "max_response_tokens": max_response_tokens,
                "provider": provider,
                "model": model,
            }
            if path is not None:
                args["path"] = path
            if threshold is not None:
                args["threshold"] = threshold

            result = await execute_tool(
                tool_name="search_semantic",
                services=self.ensure_services(),
                embedding_manager=self.embedding_manager,
                arguments=parse_mcp_arguments(args),
            )
            return dict(result) if hasattr(result, "__dict__") else result

    async def run(self) -> None:
        """Run the HTTP server.

        FastMCP handles most of the lifecycle management, so this is simpler
        than the stdio implementation.
        """
        try:
            self.debug_log(f"Starting HTTP server on port {self.port}")

            # Run the FastMCP server in HTTP mode
            await self.app.run_http_async(port=self.port, host="0.0.0.0")

        except KeyboardInterrupt:
            self.debug_log("Server interrupted by user")
        except Exception as e:
            self.debug_log(f"Server error: {e}")
            if self.debug_mode:
                import traceback

                traceback.print_exc()
        finally:
            # Cleanup resources
            await self.cleanup()
            self.debug_log("Server shutdown complete")


async def main() -> None:
    """Main entry point for HTTP server"""
    import argparse
    import sys

    from chunkhound.api.cli.utils.config_factory import create_validated_config
    from chunkhound.mcp.common import add_common_mcp_arguments

    parser = argparse.ArgumentParser(
        description="ChunkHound MCP HTTP server (FastMCP 2.0)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    # Add common MCP arguments
    add_common_mcp_arguments(parser)

    # HTTP-specific arguments
    parser.add_argument("--host", default="localhost", help="Host to bind to")
    parser.add_argument("--port", type=int, default=5173, help="Port to bind to")

    args = parser.parse_args()

    # Create and validate configuration
    config, validation_errors = create_validated_config(args, "mcp")

    if validation_errors:
        for error in validation_errors:
            print(f"Error: {error}", file=sys.stderr)
        sys.exit(1)

    # Create and run the HTTP server
    server = HttpMCPServer(config, port=args.port)
    await server.run()


if __name__ == "__main__":
    import asyncio

    asyncio.run(main())
