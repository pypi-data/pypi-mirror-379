"""Secure MCP Server Configuration Models.

This module provides Pydantic models for MCP server configuration with
security validation and type safety.
"""

import os
import re
from pathlib import Path
from typing import Dict, List, Optional, Literal, Any, Union
from pydantic import BaseModel, Field, field_validator, model_validator

import logging

mcp_logger = logging.getLogger("mcp_feature")


class MCPServerConfig(BaseModel):
    """Secure configuration for an MCP server connection."""

    name: str = Field(..., pattern=r'^[a-zA-Z0-9_-]+$', description="Server name (alphanumeric, underscore, hyphen only)")
    transport: Literal["stdio", "sse", "streamable-http"] = Field(default="stdio", description="Transport protocol")
    command: Optional[str] = Field(None, description="Command to start server (required for stdio)")
    args: List[str] = Field(default_factory=list, description="Command arguments")
    env: Optional[Dict[str, str]] = Field(None, description="Environment variables")
    url: Optional[str] = Field(None, description="Server URL (required for sse/streamable-http)")
    headers: Optional[Dict[str, str]] = Field(None, description="HTTP headers")
    timeout: float = Field(default=300.0, ge=1.0, le=7200.0, description="Connection timeout (1-7200 seconds)")
    include_tools: Optional[List[str]] = Field(None, description="Only include these tools")
    exclude_tools: Optional[List[str]] = Field(None, description="Exclude these tools")
    enabled: bool = Field(default=True, description="Whether server is enabled")

    @field_validator('name')
    @classmethod
    def validate_name_security(cls, v):
        """Validate server name for security."""
        if not v or len(v.strip()) == 0:
            raise ValueError("Server name cannot be empty")
        if len(v) > 50:
            raise ValueError("Server name too long (max 50 characters)")
        # Additional check for potentially dangerous names
        dangerous_names = ['root', 'admin', 'system', 'daemon', 'null', 'con', 'prn', 'aux']
        if v.lower() in dangerous_names:
            raise ValueError(f"Server name '{v}' is reserved and not allowed")
        return v

    @field_validator('command')
    @classmethod
    def validate_command_security(cls, v):
        """Validate command for security vulnerabilities."""
        if v is None:
            return v

        # Check for command injection patterns
        dangerous_chars = ['&', '|', ';', '`', '$', '>', '<', '&&', '||', '$(', '${']
        for char in dangerous_chars:
            if char in v:
                raise ValueError(f"Security: Command contains dangerous character/sequence: {char}")

        # Check for suspicious patterns
        suspicious_patterns = [
            r'rm\s+-rf',  # rm -rf
            r'sudo\s+',   # sudo commands
            r'su\s+',     # su commands
            r'chmod\s+',  # chmod commands
            r'chown\s+',  # chown commands
            r'/bin/',     # direct binary calls
            r'\.\./',     # directory traversal
            r'eval\s*\(',  # eval calls
            r'exec\s*\(',  # exec calls
        ]

        for pattern in suspicious_patterns:
            if re.search(pattern, v, re.IGNORECASE):
                raise ValueError(f"Security: Command contains suspicious pattern: {pattern}")

        # Command should be a simple executable
        if not v.strip():
            raise ValueError("Command cannot be empty when specified")

        return v

    @field_validator('args')
    @classmethod
    def validate_args_security(cls, v):
        """Validate command arguments for security."""
        if not v:
            return v

        for arg in v:
            if not isinstance(arg, str):
                raise ValueError("All arguments must be strings")

            # Check for dangerous patterns in arguments
            dangerous_chars = ['&', '|', ';', '`', '$', '>', '<']
            for char in dangerous_chars:
                if char in arg:
                    raise ValueError(f"Security: Argument contains dangerous character: {char}")

        return v

    @field_validator('env')
    @classmethod
    def validate_env_security(cls, v):
        """Validate environment variables for security."""
        if not v:
            return v

        # Whitelist of safe environment variables
        safe_env_prefixes = [
            'PATH', 'HOME', 'USER', 'LANG', 'LC_', 'TZ', 'TERM',
            'PYTHON', 'NODE', 'NPM', 'VIRTUAL_ENV', 'CONDA',
            'MCP_', 'ASKBUDI_', 'OPENAI_', 'ANTHROPIC_', 'GOOGLE_'
        ]

        for key, value in v.items():
            # Check key format
            if not re.match(r'^[A-Z_][A-Z0-9_]*$', key):
                raise ValueError(f"Environment variable key '{key}' has invalid format")

            # Check if key is safe
            is_safe = any(key.startswith(prefix) for prefix in safe_env_prefixes)
            if not is_safe:
                mcp_logger.warning(f"Environment variable '{key}' not in safe list")

            # Check value for dangerous content
            if any(char in value for char in ['`', '$(']):
                raise ValueError(f"Environment variable '{key}' contains dangerous characters")

        return v

    @field_validator('url')
    @classmethod
    def validate_url_security(cls, v):
        """Validate URL for security."""
        if v is None:
            return v

        # Basic URL validation
        if not v.startswith(('http://', 'https://')):
            raise ValueError("URL must start with http:// or https://")

        # Check for suspicious patterns
        if any(pattern in v.lower() for pattern in ['localhost', '127.0.0.1', '0.0.0.0']):
            mcp_logger.warning(f"URL points to localhost: {v}")

        return v

    @model_validator(mode='after')
    def validate_transport_requirements(self):
        """Validate transport-specific requirements."""
        if self.transport == 'stdio':
            if not self.command:
                raise ValueError("stdio transport requires 'command' to be specified")
        elif self.transport in ['sse', 'streamable-http']:
            if not self.url:
                raise ValueError(f"{self.transport} transport requires 'url' to be specified")

        return self

    class Config:
        """Pydantic configuration."""
        extra = "forbid"  # Forbid extra fields for security
        validate_assignment = True  # Validate on assignment


class MCPConfiguration(BaseModel):
    """Complete MCP configuration containing multiple servers."""

    servers: List[MCPServerConfig] = Field(default_factory=list, description="List of MCP servers")
    version: str = Field(default="1.0", description="Configuration version")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Additional metadata")

    @field_validator('servers')
    @classmethod
    def validate_unique_server_names(cls, v):
        """Ensure server names are unique."""
        names = [server.name for server in v]
        if len(names) != len(set(names)):
            duplicates = [name for name in names if names.count(name) > 1]
            raise ValueError(f"Duplicate server names found: {duplicates}")
        return v

    @model_validator(mode='after')
    def validate_at_least_one_enabled(self):
        """Ensure at least one server is enabled if any servers exist."""
        if self.servers:
            enabled_servers = [s for s in self.servers if s.enabled]
            if not enabled_servers:
                mcp_logger.warning("No MCP servers are enabled")
        return self

    def get_enabled_servers(self) -> List[MCPServerConfig]:
        """Get list of enabled servers."""
        return [server for server in self.servers if server.enabled]

    def get_server_by_name(self, name: str) -> Optional[MCPServerConfig]:
        """Get server configuration by name."""
        for server in self.servers:
            if server.name == name:
                return server
        return None

    def add_server(self, server: MCPServerConfig) -> None:
        """Add a new server configuration."""
        # Check for duplicate names
        if self.get_server_by_name(server.name):
            raise ValueError(f"Server with name '{server.name}' already exists")

        self.servers.append(server)
        mcp_logger.info(f"Added MCP server configuration: {server.name}")

    def remove_server(self, name: str) -> bool:
        """Remove server configuration by name."""
        original_count = len(self.servers)
        self.servers = [s for s in self.servers if s.name != name]
        removed = len(self.servers) < original_count

        if removed:
            mcp_logger.info(f"Removed MCP server configuration: {name}")
        else:
            mcp_logger.warning(f"Server '{name}' not found for removal")

        return removed

    class Config:
        """Pydantic configuration."""
        extra = "forbid"
        validate_assignment = True