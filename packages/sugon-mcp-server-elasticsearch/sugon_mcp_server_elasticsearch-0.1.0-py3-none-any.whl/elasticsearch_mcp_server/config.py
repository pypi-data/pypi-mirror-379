"""Configuration management for Elasticsearch MCP Server."""

import os
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import pyjson5
from pydantic import BaseModel, Field, validator
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import AliasChoices


class IncludeExclude(BaseModel):
    """Include/exclude configuration for tools."""

    include: Optional[List[str]] = None
    exclude: Optional[List[str]] = None


class ToolBase(BaseModel):
    """Base configuration for custom tools."""

    description: str
    parameters: Dict[str, Any]
    annotations: Optional[Dict[str, Any]] = None


class EsqlTool(ToolBase):
    """ES|QL custom tool configuration."""

    type: str = Field(default="esql", alias="type")
    query: str
    format: str = "json"  # json, csv, value


class SearchTemplateTool(ToolBase):
    """Search template custom tool configuration."""

    type: str = Field(default="search_template", alias="type")
    template_id: Optional[str] = None
    template: Optional[Dict[str, Any]] = None

    @validator('template_id', 'template')
    def validate_template_config(cls, v, values):
        """Ensure either template_id or template is provided."""
        template_id = values.get('template_id')
        template = values.get('template')

        if not template_id and not template:
            raise ValueError("Either template_id or template must be provided")
        if template_id and template:
            raise ValueError("Only one of template_id or template should be provided")
        return v


class CustomTool(BaseModel):
    """Custom tool configuration."""

    type: str
    description: str
    parameters: Dict[str, Any]
    annotations: Optional[Dict[str, Any]] = None
    query: Optional[str] = None  # for esql tools
    format: Optional[str] = None  # for esql tools
    template_id: Optional[str] = None  # for search_template tools
    template: Optional[Dict[str, Any]] = None  # for search_template tools


class ToolsConfig(BaseModel):
    """Tools configuration."""

    include: Optional[List[str]] = None
    exclude: Optional[List[str]] = None
    custom: Dict[str, CustomTool] = Field(default_factory=dict)


class ElasticsearchConfig(BaseSettings):
    """Elasticsearch MCP Server configuration."""

    # Connection settings
    url: str = Field(default="http://localhost:9200", validation_alias=AliasChoices('url', 'ELASTICSEARCH_URL'))
    api_key: Optional[str] = Field(default=None, validation_alias=AliasChoices('api_key', 'ELASTICSEARCH_API_KEY'))
    login: Optional[str] = Field(default=None, validation_alias=AliasChoices('login', 'ELASTICSEARCH_USERNAME'))
    password: Optional[str] = Field(default=None, validation_alias=AliasChoices('password', 'ELASTICSEARCH_PASSWORD'))
    ssl_skip_verify: bool = Field(default=False, validation_alias=AliasChoices('ssl_skip_verify', 'ELASTICSEARCH_SSL_SKIP_VERIFY'))

    # Tool configuration
    tools: ToolsConfig = Field(default_factory=ToolsConfig)
    prompts: List[str] = Field(default_factory=list)

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False
    )

    @validator('url')
    def validate_url(cls, v):
        """Validate that URL is not empty."""
        if not v or not v.strip():
            raise ValueError("Elasticsearch URL cannot be empty")
        return v.strip()

    @validator('api_key', 'login', 'password', pre=True)
    def empty_string_to_none(cls, v):
        """Convert empty strings to None."""
        if isinstance(v, str) and not v.strip():
            return None
        return v

    def get_auth_config(self) -> Optional[Dict[str, Any]]:
        """Get authentication configuration for Elasticsearch client."""
        if self.api_key:
            return {"api_key": self.api_key}
        elif self.login and self.password:
            return {"basic_auth": (self.login, self.password)}
        return None

    def get_client_config(self) -> Dict[str, Any]:
        """Get complete client configuration for Elasticsearch."""
        config = {
            "hosts": [self.url],
            "verify_certs": not self.ssl_skip_verify,
        }

        auth_config = self.get_auth_config()
        if auth_config:
            config.update(auth_config)

        return config


def load_config(config_path: Optional[Union[str, Path]] = None) -> ElasticsearchConfig:
    """Load configuration from file and environment variables.

    Args:
        config_path: Path to JSON5 configuration file

    Returns:
        ElasticsearchConfig instance
    """
    config_data = {}

    # Load from file if provided
    if config_path:
        config_path = Path(config_path)
        if config_path.exists():
            with open(config_path, 'r', encoding='utf-8') as f:
                config_data = pyjson5.load(f)

    # Create config with file data and environment variables
    return ElasticsearchConfig(**config_data)


def rewrite_localhost_for_container(url: str) -> str:
    """Rewrite localhost URLs for container environments.

    Args:
        url: Original URL

    Returns:
        Modified URL with container-friendly hostname
    """
    import socket
    from urllib.parse import urlparse, urlunparse

    parsed = urlparse(url)
    if parsed.hostname == "localhost":
        # Try common container host aliases
        aliases = ["host.docker.internal", "host.containers.internal"]

        for alias in aliases:
            try:
                socket.gethostbyname(alias)
                # Replace hostname
                new_netloc = parsed.netloc.replace("localhost", alias)
                new_parsed = parsed._replace(netloc=new_netloc)
                return urlunparse(new_parsed)
            except socket.gaierror:
                continue

    return url