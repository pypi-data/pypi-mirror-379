"""MCP Configuration Manager.

Manages loading, saving, and merging MCP configurations from local and global locations.
Follows the hierarchy: local (.askbudi/mcp.json) overrides global (~/.ASKBUDI/mcp.json).
"""

import json
import os
from pathlib import Path
from typing import Dict, List, Optional, Tuple, Union
from pydantic import ValidationError

from .mcp_config import MCPConfiguration, MCPServerConfig
import logging

mcp_logger = logging.getLogger("mcp_feature")


class MCPConfigManager:
    """Manages MCP configuration loading and saving with local/global hierarchy."""

    def __init__(self, project_root: Optional[Path] = None):
        """Initialize configuration manager.

        Args:
            project_root: Root directory of the project. If None, uses current working directory.
        """
        self.project_root = Path(project_root) if project_root else Path.cwd()
        self.local_config_dir = self.project_root / ".askbudi"
        self.local_config_file = self.local_config_dir / "mcp.json"

        # Global configuration directory
        self.global_config_dir = Path.home() / ".ASKBUDI"
        self.global_config_file = self.global_config_dir / "mcp.json"

        mcp_logger.info(f"MCPConfigManager initialized with project root: {self.project_root}")
        mcp_logger.debug(f"Local config file: {self.local_config_file}")
        mcp_logger.debug(f"Global config file: {self.global_config_file}")

    def _ensure_config_dir(self, config_dir: Path) -> None:
        """Ensure configuration directory exists with proper permissions."""
        try:
            config_dir.mkdir(parents=True, exist_ok=True)
            # Set restrictive permissions on config directory
            if os.name != 'nt':  # Unix-like systems
                os.chmod(config_dir, 0o755)
            mcp_logger.debug(f"Ensured config directory exists: {config_dir}")
        except Exception as e:
            mcp_logger.error(f"Failed to create config directory {config_dir}: {e}")
            raise

    def _load_config_file(self, config_file: Path) -> Optional[MCPConfiguration]:
        """Load configuration from a specific file.

        Args:
            config_file: Path to the configuration file

        Returns:
            MCPConfiguration if file exists and is valid, None otherwise
        """
        if not config_file.exists():
            mcp_logger.debug(f"Configuration file does not exist: {config_file}")
            return None

        try:
            with open(config_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            config = MCPConfiguration(**data)
            mcp_logger.info(f"Loaded MCP configuration from {config_file}: {len(config.servers)} servers")
            return config

        except json.JSONDecodeError as e:
            mcp_logger.error(f"Invalid JSON in config file {config_file}: {e}")
            raise ValueError(f"Invalid JSON in config file {config_file}: {e}")

        except ValidationError as e:
            mcp_logger.error(f"Invalid configuration in {config_file}: {e}")
            raise ValueError(f"Invalid configuration in {config_file}: {e}")

        except Exception as e:
            mcp_logger.error(f"Failed to load config file {config_file}: {e}")
            raise

    def _save_config_file(self, config: MCPConfiguration, config_file: Path) -> None:
        """Save configuration to a specific file.

        Args:
            config: Configuration to save
            config_file: Path to save the configuration
        """
        try:
            # Ensure parent directory exists
            self._ensure_config_dir(config_file.parent)

            # Write configuration
            with open(config_file, 'w', encoding='utf-8') as f:
                json.dump(config.dict(), f, indent=2, sort_keys=True)

            # Set restrictive permissions on config file
            if os.name != 'nt':  # Unix-like systems
                os.chmod(config_file, 0o600)

            mcp_logger.info(f"Saved MCP configuration to {config_file}: {len(config.servers)} servers")

        except Exception as e:
            mcp_logger.error(f"Failed to save config file {config_file}: {e}")
            raise

    def load_global_config(self) -> MCPConfiguration:
        """Load global MCP configuration.

        Returns:
            MCPConfiguration from global file, or empty configuration if file doesn't exist
        """
        config = self._load_config_file(self.global_config_file)
        return config or MCPConfiguration()

    def load_local_config(self) -> MCPConfiguration:
        """Load local MCP configuration.

        Returns:
            MCPConfiguration from local file, or empty configuration if file doesn't exist
        """
        config = self._load_config_file(self.local_config_file)
        return config or MCPConfiguration()

    def load_merged_config(self) -> MCPConfiguration:
        """Load and merge global and local configurations.

        Local configuration takes precedence over global configuration.
        Servers with the same name in local config override global servers.

        Returns:
            Merged MCPConfiguration
        """
        mcp_logger.info("Loading merged MCP configuration")

        # Load configurations
        global_config = self.load_global_config()
        local_config = self.load_local_config()

        # If no local config, return global
        if not local_config.servers:
            mcp_logger.debug("No local config, returning global config")
            return global_config

        # If no global config, return local
        if not global_config.servers:
            mcp_logger.debug("No global config, returning local config")
            return local_config

        # Merge configurations: local overrides global
        merged_servers = {}

        # Add global servers first
        for server in global_config.servers:
            merged_servers[server.name] = server
            mcp_logger.debug(f"Added global server: {server.name}")

        # Override with local servers
        for server in local_config.servers:
            if server.name in merged_servers:
                mcp_logger.info(f"Local server '{server.name}' overrides global server")
            else:
                mcp_logger.debug(f"Added local server: {server.name}")
            merged_servers[server.name] = server

        # Create merged configuration
        merged_config = MCPConfiguration(
            servers=list(merged_servers.values()),
            version=local_config.version or global_config.version,
            metadata={
                **(global_config.metadata or {}),
                **(local_config.metadata or {}),
                "merged": True,
                "sources": {
                    "global": str(self.global_config_file) if global_config.servers else None,
                    "local": str(self.local_config_file) if local_config.servers else None
                }
            }
        )

        mcp_logger.info(f"Merged configuration: {len(merged_config.servers)} total servers")
        return merged_config

    def save_global_config(self, config: MCPConfiguration) -> None:
        """Save global MCP configuration.

        Args:
            config: Configuration to save
        """
        self._save_config_file(config, self.global_config_file)

    def save_local_config(self, config: MCPConfiguration) -> None:
        """Save local MCP configuration.

        Args:
            config: Configuration to save
        """
        self._save_config_file(config, self.local_config_file)

    def add_server(self, server: MCPServerConfig, scope: str = "local") -> None:
        """Add a server to the specified configuration scope.

        Args:
            server: Server configuration to add
            scope: Either "local" or "global"
        """
        if scope not in ["local", "global"]:
            raise ValueError("Scope must be 'local' or 'global'")

        # Load appropriate configuration
        if scope == "local":
            config = self.load_local_config()
        else:
            config = self.load_global_config()

        # Add server
        config.add_server(server)

        # Save configuration
        if scope == "local":
            self.save_local_config(config)
        else:
            self.save_global_config(config)

        mcp_logger.info(f"Added server '{server.name}' to {scope} configuration")

    def remove_server(self, server_name: str, scope: str = "local") -> bool:
        """Remove a server from the specified configuration scope.

        Args:
            server_name: Name of the server to remove
            scope: Either "local" or "global"

        Returns:
            True if server was removed, False if not found
        """
        if scope not in ["local", "global"]:
            raise ValueError("Scope must be 'local' or 'global'")

        # Load appropriate configuration
        if scope == "local":
            config = self.load_local_config()
        else:
            config = self.load_global_config()

        # Remove server
        removed = config.remove_server(server_name)

        # Save configuration if something was removed
        if removed:
            if scope == "local":
                self.save_local_config(config)
            else:
                self.save_global_config(config)

            mcp_logger.info(f"Removed server '{server_name}' from {scope} configuration")

        return removed

    def list_servers(self, scope: str = "merged") -> List[MCPServerConfig]:
        """List servers from the specified configuration scope.

        Args:
            scope: "local", "global", or "merged"

        Returns:
            List of server configurations
        """
        if scope == "local":
            config = self.load_local_config()
        elif scope == "global":
            config = self.load_global_config()
        elif scope == "merged":
            config = self.load_merged_config()
        else:
            raise ValueError("Scope must be 'local', 'global', or 'merged'")

        return config.servers

    def get_server(self, server_name: str, scope: str = "merged") -> Optional[MCPServerConfig]:
        """Get a specific server configuration.

        Args:
            server_name: Name of the server
            scope: "local", "global", or "merged"

        Returns:
            Server configuration if found, None otherwise
        """
        servers = self.list_servers(scope)
        for server in servers:
            if server.name == server_name:
                return server
        return None

    def config_exists(self, scope: str) -> bool:
        """Check if configuration file exists for the specified scope.

        Args:
            scope: "local" or "global"

        Returns:
            True if configuration file exists
        """
        if scope == "local":
            return self.local_config_file.exists()
        elif scope == "global":
            return self.global_config_file.exists()
        else:
            raise ValueError("Scope must be 'local' or 'global'")

    def get_config_info(self) -> Dict[str, any]:
        """Get information about configuration files and contents.

        Returns:
            Dictionary with configuration information
        """
        local_exists = self.config_exists("local")
        global_exists = self.config_exists("global")

        local_servers = len(self.list_servers("local")) if local_exists else 0
        global_servers = len(self.list_servers("global")) if global_exists else 0
        merged_servers = len(self.list_servers("merged"))

        return {
            "local": {
                "file": str(self.local_config_file),
                "exists": local_exists,
                "servers": local_servers
            },
            "global": {
                "file": str(self.global_config_file),
                "exists": global_exists,
                "servers": global_servers
            },
            "merged": {
                "servers": merged_servers
            },
            "project_root": str(self.project_root)
        }