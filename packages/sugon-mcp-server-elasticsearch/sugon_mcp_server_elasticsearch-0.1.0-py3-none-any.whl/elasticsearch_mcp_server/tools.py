"""Elasticsearch MCP tools implementation."""

import json
import traceback
from typing import Any, Dict, List, Optional, Sequence

from mcp.server import Server
from mcp.types import CallToolResult, TextContent, Tool
from pydantic import BaseModel, Field

from .client import ElasticsearchClient, logger
from .config import ElasticsearchConfig, EsqlTool, SearchTemplateTool


class ListIndicesParams(BaseModel):
    """Parameters for list_indices tool."""
    index_pattern: str = Field(description="Index pattern to filter indices")


class GetMappingsParams(BaseModel):
    """Parameters for get_mappings tool."""
    index: str = Field(description="Index name to get mappings for")


class SearchParams(BaseModel):
    """Parameters for search tool."""
    index: str = Field(description="Index name to search")
    query: Dict[str, Any] = Field(description="Elasticsearch query DSL")
    size: Optional[int] = Field(default=10, description="Number of results to return")
    from_: Optional[int] = Field(default=0, alias="from", description="Starting offset")
    source: Optional[List[str]] = Field(default=None, description="Fields to include in response")


class EsqlQueryParams(BaseModel):
    """Parameters for esql tool."""
    query: str = Field(description="ES|QL query to execute")


class GetShardsParams(BaseModel):
    """Parameters for get_shards tool."""
    index: Optional[str] = Field(default=None, description="Index name to get shards for")


class ElasticsearchTools:
    """Elasticsearch tools for MCP server."""

    def __init__(self, client: ElasticsearchClient, config: ElasticsearchConfig, server: Server):
        self.client = client
        self.config = config
        self.server = server
        self._available_tools = []
        self._setup_tools()

    def _setup_tools(self) -> None:
        """Setup all available tools."""
        # Check which tools to include/exclude
        tools_config = self.config.tools
        excluded_tools = set(tools_config.exclude or [])
        included_tools = set(tools_config.include) if tools_config.include else None

        # Setup base tools
        if "list_indices" not in excluded_tools and (not included_tools or "list_indices" in included_tools):
            self._available_tools.append(Tool(
                name="list_indices",
                description="List all available Elasticsearch indices",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "index_pattern": {
                            "type": "string",
                            "description": "Index pattern to filter indices"
                        }
                    },
                    "required": ["index_pattern"]
                }
            ))

        if "get_mappings" not in excluded_tools and (not included_tools or "get_mappings" in included_tools):
            self._available_tools.append(Tool(
                name="get_mappings",
                description="Get field mappings for a specific Elasticsearch index",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "index": {
                            "type": "string",
                            "description": "Index name to get mappings for"
                        }
                    },
                    "required": ["index"]
                }
            ))

        if "search" not in excluded_tools and (not included_tools or "search" in included_tools):
            self._available_tools.append(Tool(
                name="search",
                description="Search documents in an Elasticsearch index",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "index": {
                            "type": "string",
                            "description": "Index name to search"
                        },
                        "query": {
                            "type": "object",
                            "description": "Elasticsearch query DSL"
                        },
                        "size": {
                            "type": "integer",
                            "description": "Number of results to return",
                            "default": 10
                        },
                        "from": {
                            "type": "integer",
                            "description": "Starting offset",
                            "default": 0
                        },
                        "source": {
                            "type": "array",
                            "items": {"type": "string"},
                            "description": "Fields to include in response"
                        }
                    },
                    "required": ["index", "query"]
                }
            ))

        if "esql" not in excluded_tools and (not included_tools or "esql" in included_tools):
            self._available_tools.append(Tool(
                name="esql",
                description="Execute ES|QL query",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "query": {
                            "type": "string",
                            "description": "ES|QL query to execute"
                        }
                    },
                    "required": ["query"]
                }
            ))

        if "get_shards" not in excluded_tools and (not included_tools or "get_shards" in included_tools):
            self._available_tools.append(Tool(
                name="get_shards",
                description="Get shard information for indices",
                inputSchema={
                    "type": "object",
                    "properties": {
                        "index": {
                            "type": "string",
                            "description": "Index name to get shards for (optional)"
                        }
                    }
                }
            ))

        # Register custom tools
        for tool_name, tool_config in tools_config.custom.items():
            if tool_name in excluded_tools:
                continue
            if included_tools and tool_name not in included_tools:
                continue
            self._register_custom_tool(tool_name, tool_config)

    def _register_custom_tool(self, name: str, config: EsqlTool | SearchTemplateTool) -> None:
        """Register a custom tool."""
        if isinstance(config, EsqlTool):
            self._available_tools.append(Tool(
                name=name,
                description=config.description,
                inputSchema={
                    "type": "object",
                    "properties": {
                        param: {
                            "type": "string",
                            "description": f"Parameter {param} for the ES|QL query"
                        }
                        for param in config.parameters
                    },
                    "required": config.parameters
                }
            ))
        elif isinstance(config, SearchTemplateTool):
            self._available_tools.append(Tool(
                name=name,
                description=config.description,
                inputSchema={
                    "type": "object",
                    "properties": {
                        param: {
                            "type": "string",
                            "description": f"Parameter {param} for the search template"
                        }
                        for param in config.parameters
                    },
                    "required": config.parameters
                }
            ))

    def get_available_tools(self) -> List[Tool]:
        """Return the list of available tools."""
        return self._available_tools

    async def call_tool(self, name: str, arguments: Dict[str, Any]) -> Sequence[TextContent]:
        """Handle tool calls."""
        try:
            if name == "list_indices":
                return await self.list_indices(arguments)
            elif name == "get_mappings":
                return await self.get_mappings(arguments)
            elif name == "search":
                return await self.search(arguments)
            elif name == "esql":
                return await self.esql(arguments)
            elif name == "get_shards":
                return await self.get_shards(arguments)
            elif name in self.config.tools.custom:
                return await self.call_custom_tool(name, arguments)
            else:
                return [TextContent(type="text", text=f"Unknown tool: {name}")]
        except Exception as e:
            # 打印错误栈信息
            traceback.print_exception(
                type(e),
                e,
                e.__traceback__
            )
            return [TextContent(type="text", text=f"Error executing tool {name}: {str(e)}")]

    async def list_indices(self, arguments: Dict[str, Any]) -> Sequence[TextContent]:
        """List Elasticsearch indices."""
        try:
            params = ListIndicesParams(**arguments)
            result = await self.client.list_indices(params.index_pattern)
            return [TextContent(type="text", text=json.dumps(result.body, indent=2))]
        except Exception as e:
            # 打印错误栈信息
            traceback.print_exception(
                type(e),
                e,
                e.__traceback__
            )
            return [TextContent(type="text", text=f"Error listing indices: {str(e)}")]

    async def get_mappings(self, arguments: Dict[str, Any]) -> Sequence[TextContent]:
        """Get index mappings."""
        try:
            params = GetMappingsParams(**arguments)
            result = await self.client.get_mappings(params.index)
            return [TextContent(type="text", text=json.dumps(result.body, indent=2))]
        except Exception as e:
            # 打印错误栈信息
            traceback.print_exception(
                type(e),
                e,
                e.__traceback__
            )
            return [TextContent(type="text", text=f"Error listing indices: {str(e)}")]

    async def get_mappings(self, arguments: Dict[str, Any]) -> Sequence[TextContent]:
        """Get index mappings."""
        try:
            params = GetMappingsParams(**arguments)
            result = await self.client.get_mappings(params.index)
            return [TextContent(type="text", text=json.dumps(result.body, indent=2))]
        except Exception as e:
            # 打印错误栈信息
            traceback.print_exception(
                type(e),
                e,
                e.__traceback__
            )
            return [TextContent(type="text", text=f"Error getting mappings: {str(e)}")]

    async def search(self, arguments: Dict[str, Any]) -> Sequence[TextContent]:
        """Search documents."""
        try:
            params = SearchParams(**arguments)
            result = await self.client.search(
                index=params.index,
                query=params.query,
                size=params.size,
                from_=params.from_,
                source=params.source
            )
            text = json.dumps(result.body, indent=2);
            return [TextContent(type="text", text=text)]
        except Exception as e:
            # 打印错误栈信息
            traceback.print_exception(
                type(e),
                e,
                e.__traceback__
            )
            # Return error CallToolResult using dict constructor
            return [TextContent(type="text", text=f"Error searching: {str(e)}")]

    async def esql(self, arguments: Dict[str, Any])  -> Sequence[TextContent]:
        """Execute ES|QL query."""
        try:
            params = EsqlQueryParams(**arguments)
            result = await self.client.esql_query(params.query)
            return [TextContent(type="text", text=json.dumps(result.body, indent=2))]
        except Exception as e:
            # 打印错误栈信息
            traceback.print_exception(
                type(e),
                e,
                e.__traceback__
            )
            return [TextContent(type="text", text=f"Error executing ES|QL query: {str(e)}")]

    async def get_shards(self, arguments: Dict[str, Any])  -> Sequence[TextContent]:
        """Get shard information."""
        try:
            params = GetShardsParams(**arguments)
            result = await self.client.get_shards(params.index)
            return [TextContent(type="text", text=json.dumps(result.body, indent=2))]
        except Exception as e:
            # 打印错误栈信息
            traceback.print_exception(
                type(e),
                e,
                e.__traceback__
            )
            return [TextContent(type="text", text=f"Error getting shards: {str(e)}")]

    async def call_custom_tool(self, name: str, arguments: Dict[str, Any])  -> Sequence[TextContent]:
        """Execute custom tool."""
        try:
            config = self.config.tools.custom[name]

            if isinstance(config, EsqlTool):
                # Replace parameters in the ES|QL query
                query = config.query
                for param, value in arguments.items():
                    query = query.replace(f"${{{param}}}", str(value))

                result = await self.client.esql_query(query)
                return [TextContent(type="text", text=json.dumps(result.body, indent=2))]

            elif isinstance(config, SearchTemplateTool):
                # Execute search template
                result = await self.client.search_template(
                    index=config.index,
                    template=config.template,
                    params=arguments
                )
                return [TextContent(type="text", text=json.dumps(result.body, indent=2))]

            else:
                return [TextContent(type="text", text=f"Unknown custom tool type for {name}")]

        except Exception as e:
            # 打印错误栈信息
            traceback.print_exception(
                type(e),
                e,
                e.__traceback__
            )
            return [TextContent(type="text", text=f"Error executing custom tool {name}: {str(e)}")]
