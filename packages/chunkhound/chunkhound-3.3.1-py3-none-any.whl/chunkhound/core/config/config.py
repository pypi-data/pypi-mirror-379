"""Centralized configuration management for ChunkHound.

This module provides a unified configuration system with clear precedence:
1. CLI arguments (highest priority)
2. Local .chunkhound.json in target directory (if present)
3. Config file (via --config path)
4. Environment variables
5. Default values (lowest priority)
"""

import os
from pathlib import Path
from typing import Any

from pydantic import BaseModel, ConfigDict, Field, model_validator

from .database_config import DatabaseConfig
from .embedding_config import EmbeddingConfig
from .indexing_config import IndexingConfig
from .mcp_config import MCPConfig


class Config(BaseModel):
    """Centralized configuration for ChunkHound."""

    model_config = ConfigDict(validate_assignment=True)

    database: DatabaseConfig = Field(default_factory=DatabaseConfig)
    embedding: EmbeddingConfig | None = Field(default=None)
    mcp: MCPConfig = Field(default_factory=MCPConfig)
    indexing: IndexingConfig = Field(default_factory=IndexingConfig)
    debug: bool = Field(default=False)

    # Private field to store the target directory from CLI args
    target_dir: Path | None = Field(default=None, exclude=True)
    # Private field to track if embeddings were explicitly disabled
    embeddings_disabled: bool = Field(default=False, exclude=True)

    def __init__(self, args: Any | None = None, **kwargs: Any) -> None:
        """Universal configuration initialization that handles all contexts.

        Automatically applies correct precedence order:
        1. CLI arguments (highest priority)
        2. Environment variables
        3. Config file (via --config path, env var, or local .chunkhound.json)
        4. Default values (lowest priority)

        Args:
            args: Optional argparse.Namespace from command line parsing
            **kwargs: Direct overrides for testing or special cases
        """
        # Start with defaults
        config_data: dict[str, Any] = {}

        # 1. Smart config file resolution (before env vars)
        config_file = None
        target_dir = None

        # Extract config file and target directory from args if provided
        if args:
            # Get config file from --config if present
            if hasattr(args, "config") and args.config:
                config_file = Path(args.config)

            # Get target directory from args.path for local config detection
            if hasattr(args, "path") and args.path:
                target_dir = Path(args.path)

        # If no config file from args, check environment variable
        if not config_file:
            env_config_file = os.getenv("CHUNKHOUND_CONFIG_FILE")
            if env_config_file:
                config_file = Path(env_config_file)

        # Always detect project root for local config detection
        if target_dir is None:
            from chunkhound.utils.project_detection import find_project_root

            target_dir = find_project_root(
                getattr(args, "path", None) if args else None
            )

        # 2. Load config file if found
        if config_file and config_file.exists():
            import json

            try:
                with open(config_file) as f:
                    file_config = json.load(f)
                    self._deep_merge(config_data, file_config)
            except json.JSONDecodeError as e:
                raise ValueError(
                    f"Invalid JSON in config file {config_file}: {e}. "
                    "Please check the file format and try again."
                )

        # 3. Check for local .chunkhound.json in target directory
        if target_dir and target_dir.exists():
            local_config_path = target_dir / ".chunkhound.json"
            if local_config_path.exists() and local_config_path != config_file:
                import json

                try:
                    with open(local_config_path) as f:
                        local_config = json.load(f)
                        self._deep_merge(config_data, local_config)
                except json.JSONDecodeError as e:
                    raise ValueError(
                        f"Invalid JSON in config file {local_config_path}: {e}. "
                        "Please check the file format and try again."
                    )

        # 4. Load environment variables (override config files)
        env_vars = self._load_env_vars()
        self._deep_merge(config_data, env_vars)

        # 5. Apply CLI arguments (highest precedence)
        if args:
            cli_overrides = self._extract_cli_overrides(args)
            self._deep_merge(config_data, cli_overrides)

        # 6. Apply any direct kwargs (for testing)
        if kwargs:
            self._deep_merge(config_data, kwargs)

        # Special handling for EmbeddingConfig
        if "embedding" in config_data and isinstance(config_data["embedding"], dict):
            # Create EmbeddingConfig instance with the data
            config_data["embedding"] = EmbeddingConfig(**config_data["embedding"])

        # Add target_dir to config_data for initialization
        config_data["target_dir"] = target_dir

        # Initialize the model
        super().__init__(**config_data)

    def _load_env_vars(self) -> dict[str, Any]:
        """Load configuration from environment variables.

        Supports both legacy and new environment variable names.
        Uses CHUNKHOUND_ prefix with __ delimiter for nested values.
        """
        config: dict[str, Any] = {}

        # Debug mode
        if os.getenv("CHUNKHOUND_DEBUG"):
            config["debug"] = os.getenv("CHUNKHOUND_DEBUG", "").lower() in (
                "true",
                "1",
                "yes",
            )

        # Delegate to each config class
        if db_config := DatabaseConfig.load_from_env():
            config["database"] = db_config
        if embedding_config := EmbeddingConfig.load_from_env():
            config["embedding"] = embedding_config
        if mcp_config := MCPConfig.load_from_env():
            config["mcp"] = mcp_config
        if indexing_config := IndexingConfig.load_from_env():
            config["indexing"] = indexing_config

        return config

    def _extract_cli_overrides(self, args: Any) -> dict[str, Any]:
        """Extract configuration overrides from CLI arguments.

        Args:
            args: Parsed command line arguments

        Returns:
            Dictionary of configuration overrides
        """
        overrides: dict[str, Any] = {}

        # Common CLI args
        if hasattr(args, "debug") and args.debug:
            overrides["debug"] = args.debug
        elif hasattr(args, "verbose") and args.verbose:
            overrides["debug"] = args.verbose

        # Delegate to each config class
        if db_overrides := DatabaseConfig.extract_cli_overrides(args):
            overrides["database"] = db_overrides
        if embedding_overrides := EmbeddingConfig.extract_cli_overrides(args):
            # Handle special case for --no-embeddings
            if embedding_overrides.get("disabled"):
                overrides["embedding"] = None
                overrides["embeddings_disabled"] = True
            else:
                overrides["embedding"] = embedding_overrides
        if mcp_overrides := MCPConfig.extract_cli_overrides(args):
            overrides["mcp"] = mcp_overrides
        if indexing_overrides := IndexingConfig.extract_cli_overrides(args):
            overrides["indexing"] = indexing_overrides

        return overrides

    def _deep_merge(self, base: dict[str, Any], update: dict[str, Any]) -> None:
        """Deep merge update dictionary into base dictionary."""
        for key, value in update.items():
            if key in base and isinstance(base[key], dict) and isinstance(value, dict):
                self._deep_merge(base[key], value)
            else:
                base[key] = value

    @model_validator(mode="after")
    def validate_config(self) -> "Config":
        """Validate the configuration after initialization."""
        # Ensure target_dir is always set and resolved (never None)
        if self.target_dir is None:
            from chunkhound.utils.project_detection import find_project_root

            detected_root = find_project_root(None)
            # Fallback to current working directory if no project root found
            resolved_target = (
                detected_root.resolve() if detected_root else Path.cwd().resolve()
            )
            # Use object.__setattr__ to avoid Pydantic validation recursion
            object.__setattr__(self, "target_dir", resolved_target)
        else:
            # Ensure target_dir is resolved to canonical path (handles symlinks)
            # Use object.__setattr__ to avoid Pydantic validation recursion
            object.__setattr__(self, "target_dir", self.target_dir.resolve())

        # Ensure database path is set
        if not self.database.path:
            # Try to detect project root from target_dir or auto-detect
            from chunkhound.utils.project_detection import find_project_root

            # Use the target_dir if it was provided during initialization
            start_path = self.target_dir
            project_root = find_project_root(start_path)

            # Set default database path in project root
            self.database.path = project_root / ".chunkhound" / "db"

        # Ensure database path is resolved to canonical form (handles symlinks)
        if self.database.path:
            self.database.path = self.database.path.resolve()

        return self

    def to_dict(self) -> dict[str, Any]:
        """Convert configuration to dictionary."""
        return self.model_dump(exclude_none=True)

    def validate_for_command(self, command: str) -> list[str]:
        """
        Validate configuration for a specific command.

        Args:
            command: Command name ('index', 'mcp', etc.)

        Returns:
            List of validation errors (empty if valid)
        """
        errors: list[str] = []

        # Check for missing configuration
        missing_config = self.get_missing_config()
        if missing_config:
            errors.extend(
                f"Missing required configuration: {item}" for item in missing_config
            )

        # Validate embedding provider requirements for index command
        if command == "index":
            # Skip embedding validation if embeddings were explicitly disabled
            if not self.embeddings_disabled:
                if self.embedding is None:
                    errors.append("No embedding provider configured")
                elif self.embedding and not self.embedding.is_provider_configured():
                    errors.append("Embedding provider not properly configured")

        # For MCP command, embedding is optional
        elif command == "mcp":
            if self.embedding and not self.embedding.is_provider_configured():
                errors.append("Embedding provider not properly configured")

        # For search command, embedding is optional but must be valid if present
        elif command == "search":
            if self.embedding and not self.embedding.is_provider_configured():
                errors.append("Embedding provider not properly configured")

        return errors

    def get_missing_config(self) -> list[str]:
        """
        Get list of missing required configuration parameters.

        Returns:
            List of missing configuration parameter names
        """
        missing = []

        # Check embedding configuration if it exists
        if self.embedding:
            if hasattr(self.embedding, "get_missing_config"):
                embedding_missing = self.embedding.get_missing_config()
                for item in embedding_missing:
                    missing.append(f"embedding.{item}")
        # Note: If embedding is None, we don't assume a default provider
        # Commands like index and search can work without embeddings

        return missing

    def is_fully_configured(self) -> bool:
        """
        Check if all required configuration is present.

        Returns:
            True if fully configured, False otherwise
        """
        return self.embedding is not None and self.embedding.is_provider_configured()
