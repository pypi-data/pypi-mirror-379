# Elasticsearch MCP Server

A Model Context Protocol (MCP) server for Elasticsearch, providing core Elasticsearch functionality through MCP tools.

## Features

- **Search Operations**: Perform full-text search, term queries, and complex aggregations
- **Index Management**: Create, delete, and manage Elasticsearch indices
- **Document Operations**: Index, update, delete, and retrieve documents
- **Cluster Information**: Get cluster health, stats, and node information
- **Mapping Management**: Create and manage index mappings
- **Template Management**: Manage index templates and component templates

## Installation

### From PyPI

```bash
pip install mcp-server-elasticsearch
```

### From Source

```bash
git clone https://github.com/your-username/mcp-server-elasticsearch.git
cd mcp-server-elasticsearch
pip install -e .
```

## Configuration

Create a configuration file (e.g., `elastic-mcp.json5`) with your Elasticsearch connection details:

```json5
{
  "elasticsearch": {
    "hosts": ["http://localhost:9200"],
    "username": "your_username",  // optional
    "password": "your_password",  // optional
    "api_key": "your_api_key",    // optional, alternative to username/password
    "verify_certs": true,
    "ca_certs": "/path/to/ca.pem", // optional
    "timeout": 30
  },
  "server": {
    "host": "localhost",
    "port": 8000,
    "log_level": "INFO"
  }
}
```

## Usage

### As a Standalone Server

```bash
# Using configuration file
elasticsearch-mcp-server --config elastic-mcp.json5

# Using environment variables
export ELASTICSEARCH_HOSTS=http://localhost:9200
export ELASTICSEARCH_USERNAME=your_username
export ELASTICSEARCH_PASSWORD=your_password
elasticsearch-mcp-server
```

### As a Python Module

```python
from elasticsearch_mcp_server import ElasticsearchMCPServer, ElasticsearchConfig

# Load configuration
config = ElasticsearchConfig.from_file("elastic-mcp.json5")

# Create and run server
server = ElasticsearchMCPServer(config)
await server.run_stdio()
```

### Environment Variables

You can configure the server using environment variables:

- `ELASTICSEARCH_HOSTS`: Comma-separated list of Elasticsearch hosts
- `ELASTICSEARCH_USERNAME`: Username for authentication
- `ELASTICSEARCH_PASSWORD`: Password for authentication
- `ELASTICSEARCH_API_KEY`: API key for authentication (alternative to username/password)
- `ELASTICSEARCH_VERIFY_CERTS`: Whether to verify SSL certificates (default: true)
- `ELASTICSEARCH_CA_CERTS`: Path to CA certificate file
- `ELASTICSEARCH_TIMEOUT`: Request timeout in seconds (default: 30)

## Available Tools

The server provides the following MCP tools:

### Search Operations
- `search`: Perform search queries with various parameters
- `msearch`: Execute multiple search requests
- `count`: Count documents matching a query

### Document Operations
- `index_document`: Index a single document
- `get_document`: Retrieve a document by ID
- `update_document`: Update a document
- `delete_document`: Delete a document
- `bulk_operations`: Perform bulk operations

### Index Management
- `create_index`: Create a new index
- `delete_index`: Delete an index
- `get_index_info`: Get index information
- `list_indices`: List all indices

### Mapping Management
- `put_mapping`: Create or update index mapping
- `get_mapping`: Retrieve index mapping

### Cluster Operations
- `cluster_health`: Get cluster health status
- `cluster_stats`: Get cluster statistics
- `node_info`: Get node information

## Requirements

- Python 3.12+
- Elasticsearch 8.0+

## Dependencies

- `elasticsearch>=8.0.0,<9.0.0`
- `mcp>=1.0.0`
- `pydantic>=2.0.0`
- `pydantic-settings>=2.0.0`
- `click>=8.0.0`
- `aiohttp>=3.8.0`
- `python-dotenv>=1.0.0`
- `pyjson5>=1.6.0`
- `structlog>=23.0.0`
- `anyio>=4.0.0`
- `uvicorn>=0.24.0`
- `starlette>=0.27.0`

## License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Support

If you encounter any issues or have questions, please file an issue on the GitHub repository.