"""Main Elasticsearch MCP Server implementation."""

import asyncio
import logging
from pathlib import Path
from typing import Optional, Union, Sequence

import uvicorn
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.responses import Response
from starlette.routing import Mount, Route

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.server.sse import SseServerTransport
from mcp.types import CallToolResult, Tool, TextContent
from mcp.types import ServerCapabilities

from .client import ElasticsearchClient
from .config import ElasticsearchConfig, load_config
from .tools import ElasticsearchTools

logger = logging.getLogger(__name__)


class ElasticsearchMCPServer:
    """Elasticsearch MCP Server implementation."""

    def __init__(self, config: ElasticsearchConfig):
        """Initialize the MCP server.

        Args:
            config: Elasticsearch configuration
        """
        self.config = config
        self.client = ElasticsearchClient(config)
        self.server = Server("elasticsearch-mcp-server")
        self.tools: Optional[ElasticsearchTools] = None

        # Set up server capabilities
        self.server.capabilities = ServerCapabilities(
            tools={},
            prompts={},
            resources={},
            logging={}
        )

        # Register call_tool handler
        @self.server.call_tool()
        # async def handle_call_tool(name: str, arguments: dict) -> CallToolResult:
        async def handle_call_tool(name: str, arguments: dict) -> Sequence[TextContent]:
            return await self.tools.call_tool(name, arguments)

        # Register list_tools handler
        @self.server.list_tools()
        async def handle_list_tools() -> list[Tool]:
            return self.tools.get_available_tools() if self.tools else []

        # Set up logging
        self._setup_logging()

    def _setup_logging(self) -> None:
        """Set up logging configuration."""
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )

    async def initialize(self) -> None:
        """Initialize the server and connect to Elasticsearch."""
        try:
            # Connect to Elasticsearch
            await self.client.connect()
            logger.info("Connected to Elasticsearch successfully")

            # Initialize tools
            self.tools = ElasticsearchTools(self.client, self.config, self.server)
            logger.info("Elasticsearch tools initialized")

        except Exception as e:
            logger.error(f"Failed to initialize server: {e}")
            raise

    async def cleanup(self) -> None:
        """Clean up resources."""
        if self.client:
            await self.client.close()
            logger.info("Elasticsearch client closed")

    async def run_stdio(self) -> None:
        """Run the server using stdio transport."""
        try:
            await self.initialize()

            # Run stdio server
            async with stdio_server() as (read_stream, write_stream):
                await self.server.run(
                    read_stream,
                    write_stream,
                    self.server.create_initialization_options()
                )

        except Exception as e:
            logger.error(f"Error running stdio server: {e}")
            raise
        finally:
            await self.cleanup()

    async def run_http(self, host: str = "localhost", port: int = 3000) -> None:
        """Run the server using HTTP transport.

        Args:
            host: Host to bind to
            port: Port to bind to
        """
        try:
            await self.initialize()

            # Create SSE transport
            sse_transport = SseServerTransport("/messages")

            # Define SSE endpoint handler
            async def handle_sse(request: Request) -> Response:
                """Handle SSE connections."""
                async with sse_transport.connect_sse(
                        request.scope, request.receive, request._send
                ) as streams:
                    await self.server.run(
                        streams[0], streams[1], self.server.create_initialization_options()
                    )
                return Response()

            # Create Starlette application with routes
            app = Starlette(
                routes=[
                    Route("/sse", endpoint=handle_sse, methods=["GET"]),
                    Mount("/messages", app=sse_transport.handle_post_message),
                ]
            )

            logger.info(f"Starting HTTP server on {host}:{port}")
            logger.info(f"SSE endpoint available at: http://{host}:{port}/sse")
            logger.info(f"Message endpoint available at: http://{host}:{port}/messages")

            # Run HTTP server with uvicorn
            config = uvicorn.Config(
                app=app,
                host=host,
                port=port,
                log_level="info"
            )
            server = uvicorn.Server(config)
            await server.serve()

        except Exception as e:
            logger.error(f"Error running HTTP server: {e}")
            raise
        finally:
            await self.cleanup()


async def create_server(
        config_path: Optional[Union[str, Path]] = None
) -> ElasticsearchMCPServer:
    """Create and initialize an Elasticsearch MCP server.

    Args:
        config_path: Path to configuration file

    Returns:
        Initialized server instance
    """
    config = load_config(config_path)
    server = ElasticsearchMCPServer(config)
    return server


async def run_stdio_server(
        config_path: Optional[Union[str, Path]] = None
) -> None:
    """Run the server in stdio mode.

    Args:
        config_path: Path to configuration file
    """
    server = await create_server(config_path)
    await server.run_stdio()


async def run_http_server(
        config_path: Optional[Union[str, Path]] = None,
        host: str = "localhost",
        port: int = 3000
) -> None:
    """Run the server in HTTP mode.

    Args:
        config_path: Path to configuration file
        host: Host to bind to
        port: Port to bind to
    """
    server = await create_server(config_path)
    await server.run_http(host, port)