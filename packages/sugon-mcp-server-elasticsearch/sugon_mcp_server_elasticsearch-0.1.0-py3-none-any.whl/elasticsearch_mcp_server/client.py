"""Elasticsearch client wrapper with API version compatibility."""

import logging
from typing import Any, Dict, List, Optional, Union

from elasticsearch import AsyncElasticsearch
from elasticsearch.exceptions import ConnectionError, NotFoundError

from .config import ElasticsearchConfig

logger = logging.getLogger(__name__)


class ElasticsearchClient:
    """Elasticsearch client wrapper with enhanced functionality."""

    def __init__(self, config: ElasticsearchConfig):
        """Initialize Elasticsearch client.

        Args:
            config: Elasticsearch configuration
        """
        self.config = config
        self._client: Optional[AsyncElasticsearch] = None

    async def connect(self) -> None:
        """Establish connection to Elasticsearch."""
        if self._client is not None:
            return

        client_config = self.config.get_client_config()

        # Handle API version compatibility
        # Set Accept header to be compatible with Elasticsearch 8.x
        headers = {
            "Accept": "application/vnd.elasticsearch+json;compatible-with=8",
            "Content-Type": "application/vnd.elasticsearch+json;compatible-with=8"
        }

        # Add custom headers to client config
        if "headers" in client_config:
            client_config["headers"].update(headers)
        else:
            client_config["headers"] = headers

        self._client = AsyncElasticsearch(**client_config)

        # Test connection
        try:
            info = await self._client.info()
            logger.info(f"Connected to Elasticsearch {info['version']['number']}")
        except Exception as e:
            logger.error(f"Failed to connect to Elasticsearch: {e}")
            await self.close()
            raise

    async def close(self) -> None:
        """Close Elasticsearch connection."""
        if self._client is not None:
            await self._client.close()
            self._client = None

    @property
    def client(self) -> AsyncElasticsearch:
        """Get the underlying Elasticsearch client."""
        if self._client is None:
            raise RuntimeError("Client not connected. Call connect() first.")
        return self._client

    async def list_indices(self, pattern: Optional[str] = None) -> List[Dict[str, Any]]:
        """List Elasticsearch indices.

        Args:
            pattern: Index pattern to filter by

        Returns:
            List of index information
        """
        try:
            if pattern:
                response = await self.client.cat.indices(
                    index=pattern,
                    format="json",
                    h="index,status,health,pri,rep,docs.count,store.size"
                )
            else:
                response = await self.client.cat.indices(
                    format="json",
                    h="index,status,health,pri,rep,docs.count,store.size"
                )
            return response
        except Exception as e:
            logger.error(f"Failed to list indices: {e}")
            raise

    async def get_mappings(self, index: str) -> Dict[str, Any]:
        """Get mappings for an index.

        Args:
            index: Index name

        Returns:
            Index mappings
        """
        try:
            response = await self.client.indices.get_mapping(index=index)
            return response
        except NotFoundError:
            raise ValueError(f"Index '{index}' not found")
        except Exception as e:
            logger.error(f"Failed to get mappings for index '{index}': {e}")
            raise

    async def search(
            self,
            index: str,
            query: Optional[Dict[str, Any]] = None,
            size: int = 10,
            from_: int = 0,
            sort: Optional[List[Dict[str, Any]]] = None,
            source: Optional[Union[bool, List[str]]] = None,
            **kwargs
    ) -> Dict[str, Any]:
        """Search documents in an index.

        Args:
            index: Index name
            query: Elasticsearch query DSL
            size: Number of results to return
            from_: Starting offset
            sort: Sort configuration
            source: Source filtering
            **kwargs: Additional search parameters

        Returns:
            Search results
        """
        try:
            body = {}
            if query:
                body["query"] = query
            if sort:
                body["sort"] = sort
            if source is not None:
                body["_source"] = source

            response = await self.client.search(
                index=index,
                body=body,
                size=size,
                from_=from_,
                **kwargs
            )
            return response
        except Exception as e:
            logger.error(f"Search failed for index '{index}': {e}")
            raise

    async def esql_query(
            self,
            query: str,
            format: str = "json",
            **kwargs
    ) -> Dict[str, Any]:
        """Execute ES|QL query.

        Args:
            query: ES|QL query string
            format: Response format (json, csv, txt)
            **kwargs: Additional query parameters

        Returns:
            Query results
        """
        try:
            # Use the _query endpoint for ES|QL
            response = await self.client.transport.perform_request(
                "POST",
                "/_query",
                params={"format": format, **kwargs},
                body={"query": query},
                headers={
                    "Accept": f"application/{format}",
                    "Content-Type": "application/json"
                }
            )
            return response
        except Exception as e:
            logger.error(f"ES|QL query failed: {e}")
            raise

    async def get_shards(self, index: Optional[str] = None) -> List[Dict[str, Any]]:
        """Get shard information.

        Args:
            index: Index name (optional)

        Returns:
            Shard information
        """
        try:
            params = {
                "format": "json",
                "h": "index,shard,prirep,state,docs,store,node"
            }
            if index:
                params["index"] = index

            response = await self.client.cat.shards(**params)
            return response
        except Exception as e:
            logger.error(f"Failed to get shard information: {e}")
            raise

    async def get_cluster_health(self) -> Dict[str, Any]:
        """Get cluster health information.

        Returns:
            Cluster health data
        """
        try:
            response = await self.client.cluster.health()
            return response
        except Exception as e:
            logger.error(f"Failed to get cluster health: {e}")
            raise

    async def get_cluster_stats(self) -> Dict[str, Any]:
        """Get cluster statistics.

        Returns:
            Cluster statistics
        """
        try:
            response = await self.client.cluster.stats()
            return response
        except Exception as e:
            logger.error(f"Failed to get cluster stats: {e}")
            raise

    async def search_template(
            self,
            index: str,
            template_id: Optional[str] = None,
            template: Optional[Dict[str, Any]] = None,
            params: Optional[Dict[str, Any]] = None,
            **kwargs
    ) -> Dict[str, Any]:
        """Execute a search template.

        Args:
            index: Index name
            template_id: Stored template ID
            template: Inline template
            params: Template parameters
            **kwargs: Additional search parameters

        Returns:
            Search results
        """
        try:
            body = {}
            if template_id:
                body["id"] = template_id
            elif template:
                body["source"] = template
            else:
                raise ValueError("Either template_id or template must be provided")

            if params:
                body["params"] = params

            response = await self.client.search_template(
                index=index,
                body=body,
                **kwargs
            )
            return response
        except Exception as e:
            logger.error(f"Search template failed for index '{index}': {e}")
            raise

    async def __aenter__(self):
        """Async context manager entry."""
        await self.connect()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        """Async context manager exit."""
        await self.close()