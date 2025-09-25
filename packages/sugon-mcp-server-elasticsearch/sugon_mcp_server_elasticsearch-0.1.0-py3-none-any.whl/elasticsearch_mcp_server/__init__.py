"""Elasticsearch MCP Server - Python Implementation.

A Model Context Protocol (MCP) server for Elasticsearch, providing core
Elasticsearch functionality through MCP tools.
"""

__version__ = "0.1.0"
__author__ = "alcoris"
__license__ = "Apache-2.0"

from .server import ElasticsearchMCPServer
from .config import ElasticsearchConfig

__all__ = ["ElasticsearchMCPServer", "ElasticsearchConfig"]