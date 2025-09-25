"""Command line interface for Elasticsearch MCP Server."""

import argparse
import asyncio
import logging
import sys
from pathlib import Path
from typing import Optional

from .server import run_http_server, run_stdio_server

logger = logging.getLogger(__name__)


def create_parser() -> argparse.ArgumentParser:
    """Create command line argument parser."""
    parser = argparse.ArgumentParser(
        description="Elasticsearch MCP Server",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run in stdio mode (default)
  elasticsearch-mcp-server

  # Run in stdio mode with custom config
  elasticsearch-mcp-server --config /path/to/config.json5

  # Run in HTTP mode
  elasticsearch-mcp-server --http --host 0.0.0.0 --port 8080

  # Run with debug logging
  elasticsearch-mcp-server --log-level debug

Environment Variables:
  ELASTICSEARCH_URL          - Elasticsearch server URL
  ELASTICSEARCH_API_KEY      - API key for authentication
  ELASTICSEARCH_USERNAME     - Username for basic auth
  ELASTICSEARCH_PASSWORD     - Password for basic auth
  ELASTICSEARCH_SSL_SKIP_VERIFY - Skip SSL certificate verification
        """
    )

    # Transport options
    transport_group = parser.add_mutually_exclusive_group()
    transport_group.add_argument(
        "--stdio",
        action="store_true",
        default=True,
        help="Use stdio transport (default)"
    )
    transport_group.add_argument(
        "--http",
        action="store_true",
        help="Use HTTP transport with SSE"
    )

    # HTTP options
    http_group = parser.add_argument_group("HTTP options")
    http_group.add_argument(
        "--host",
        default="localhost",
        help="Host to bind HTTP server to (default: localhost)"
    )
    http_group.add_argument(
        "--port",
        type=int,
        default=3000,
        help="Port to bind HTTP server to (default: 3000)"
    )

    # Configuration
    config_group = parser.add_argument_group("Configuration")
    config_group.add_argument(
        "--config",
        "-c",
        type=Path,
        help="Path to JSON5 configuration file"
    )

    # Logging
    logging_group = parser.add_argument_group("Logging")
    logging_group.add_argument(
        "--log-level",
        choices=["debug", "info", "warning", "error", "critical"],
        default="info",
        help="Set logging level (default: info)"
    )
    logging_group.add_argument(
        "--log-file",
        type=Path,
        help="Log to file instead of stderr"
    )

    # Version
    parser.add_argument(
        "--version",
        action="version",
        version="%(prog)s 1.0.0"
    )

    return parser


def setup_logging(level: str, log_file: Optional[Path] = None) -> None:
    """Set up logging configuration.

    Args:
        level: Logging level
        log_file: Optional log file path
    """
    log_level = getattr(logging, level.upper())

    # Configure logging format
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )

    # Set up handler
    if log_file:
        handler = logging.FileHandler(log_file)
    else:
        handler = logging.StreamHandler(sys.stderr)

    handler.setFormatter(formatter)

    # Configure root logger
    root_logger = logging.getLogger()
    root_logger.setLevel(log_level)
    root_logger.addHandler(handler)

    # Reduce noise from some libraries
    logging.getLogger("elasticsearch").setLevel(logging.WARNING)
    logging.getLogger("urllib3").setLevel(logging.WARNING)


async def main() -> None:
    """Main entry point."""
    parser = create_parser()
    args = parser.parse_args()

    # Set up logging
    setup_logging(args.log_level, args.log_file)

    try:
        if args.http:
            logger.info(f"Starting Elasticsearch MCP Server in HTTP mode on {args.host}:{args.port}")
            await run_http_server(
                config_path=args.config,
                host=args.host,
                port=args.port
            )
        else:
            logger.info("Starting Elasticsearch MCP Server in stdio mode")
            await run_stdio_server(config_path=args.config)

    except KeyboardInterrupt:
        logger.info("Server stopped by user")
    except Exception as e:
        logger.error(f"Server error: {e}")
        sys.exit(1)


def cli_main() -> None:
    """CLI entry point that handles asyncio."""
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass


if __name__ == "__main__":
    cli_main()