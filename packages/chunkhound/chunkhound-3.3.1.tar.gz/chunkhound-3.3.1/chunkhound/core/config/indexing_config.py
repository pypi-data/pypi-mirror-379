"""Indexing configuration for ChunkHound.

This module provides configuration for the file indexing process including
batch processing, and pattern matching.
"""

import argparse
import os
from typing import Any

from pydantic import BaseModel, Field, field_validator


def _get_default_include_patterns() -> list[str]:
    """Get complete default patterns from Language enum.

    Returns all supported file extensions as glob patterns.
    This is the single source of truth for default file discovery.
    """
    from chunkhound.core.types.common import Language

    patterns = []
    for ext in Language.get_all_extensions():
        patterns.append(f"**/*{ext}")
    # Add special filename patterns
    patterns.extend(["**/Makefile", "**/makefile", "**/GNUmakefile", "**/gnumakefile"])
    return patterns


class IndexingConfig(BaseModel):
    """Configuration for file indexing behavior.

    Controls how files are discovered and indexed.
    """

    # Indexing behavior
    force_reindex: bool = Field(
        default=False, description="Force re-indexing of all files"
    )

    # Internal settings - not exposed to users
    batch_size: int = Field(default=50, description="Internal batch size")
    db_batch_size: int = Field(default=100, description="Internal DB batch size")
    max_concurrent: int = Field(default=5, description="Internal concurrency")
    cleanup: bool = Field(default=True, description="Internal cleanup setting")
    ignore_gitignore: bool = Field(
        default=False, description="Internal gitignore setting"
    )
    max_file_size_mb: int = Field(default=10, description="Internal file size limit")
    chunk_overlap: int = Field(default=50, description="Internal chunk overlap")
    min_chunk_size: int = Field(default=50, description="Internal min chunk size")
    max_chunk_size: int = Field(default=2000, description="Internal max chunk size")

    # File patterns
    include: list[str] = Field(
        default_factory=lambda: _get_default_include_patterns(),
        description="Glob patterns for files to include (all supported languages)",
    )

    exclude: list[str] = Field(
        default_factory=lambda: [
            # Virtual environments and package managers
            "**/node_modules/**",
            "**/.git/**",
            "**/__pycache__/**",
            "**/venv/**",
            "**/.venv/**",
            "**/.mypy_cache/**",
            # Build artifacts and distributions
            "**/dist/**",
            "**/build/**",
            "**/target/**",
            "**/.pytest_cache/**",
            # IDE and editor files
            "**/.vscode/**",
            "**/.idea/**",
            "**/.vs/**",
            # Cache and temporary directories
            "**/.cache/**",
            "tmp/**",
            "**/temp/**",
            # Static Site Generators (Docusaurus, Next.js, Gatsby, VuePress, Nuxt)
            "**/.docusaurus/**",
            "**/.docusaurus-cache/**",
            "**/.next/**",
            "**/out/**",
            "**/.nuxt/**",
            "**/.vuepress/dist/**",
            "**/.temp/**",
            # JavaScript bundler and build tool artifacts
            "**/.parcel-cache/**",
            "**/.serverless/**",
            "**/.fusebox/**",
            "**/.dynamodb/**",
            "**/.tern-port",
            "**/.vscode-test/**",
            # Yarn v2+ specific
            "**/.yarn/cache/**",
            "**/.yarn/unplugged/**",
            "**/.yarn/build-state.yml",
            "**/.yarn/install-state.gz",
            "**/.pnp.*",
            # Editor temporary file patterns
            # Vim patterns
            "**/*.swp",
            "**/*.swo",
            "**/.*.swp",
            "**/.*.swo",
            # VS Code / general patterns
            "**/*.tmp.*",
            "**/*.*.tmp",
            "**/*~.tmp",
            # Emacs patterns
            "**/.*#",
            "**/#*#",
            "**/.*~",
            # Generic temp patterns
            "**/*.tmp???",
            "**/*.???tmp",
            # Backup and old files
            "**/*.backup",
            "**/*.bak",
            "**/*~",
            "**/*.old",
            # Minified and generated files
            "**/*.min.js",
            "**/*.min.css",
            "**/*.min.html",
            "**/*.min.svg",
            "**/dist/*.js",
            "**/dist/*.css",
            "**/bundle.js",
            "**/vendor.js",
            "**/webpack.*.js",
            "**/*.bundle.js",
            "**/*.chunk.js",
            # JSON data files (not config)
            "**/*-lock.json",
            "**/package-lock.json",
            "**/yarn.lock",
            "**/composer.lock",
            "**/assets.json",
            "**/*.map.json",
            "**/*.min.json",
        ],
        description="Glob patterns for files to exclude",
    )

    @field_validator("include", "exclude")
    def validate_patterns(cls, v: list[str]) -> list[str]:
        """Validate glob patterns."""
        if not isinstance(v, list):
            raise ValueError("Patterns must be a list")

        # Remove duplicates while preserving order
        seen = set()
        unique = []
        for pattern in v:
            if pattern not in seen:
                seen.add(pattern)
                unique.append(pattern)

        return unique

    def get_max_file_size_bytes(self) -> int:
        """Get maximum file size in bytes."""
        return self.max_file_size_mb * 1024 * 1024

    def should_index_file(self, file_path: str) -> bool:
        """Check if a file should be indexed based on patterns.

        Note: This is a simplified check. The actual implementation
        should use proper glob matching.
        """
        # This is a placeholder - actual implementation would use
        # pathlib and fnmatch for proper pattern matching
        return True

    @classmethod
    def add_cli_arguments(cls, parser: argparse.ArgumentParser) -> None:
        """Add indexing-related CLI arguments."""
        parser.add_argument(
            "--force-reindex",
            action="store_true",
            help="Force reindexing of all files, even if they haven't changed",
        )

        parser.add_argument(
            "--include",
            action="append",
            help="File patterns to include (can be specified multiple times)",
        )

        parser.add_argument(
            "--exclude",
            action="append",
            help="File patterns to exclude (can be specified multiple times)",
        )

    @classmethod
    def load_from_env(cls) -> dict[str, Any]:
        """Load indexing config from environment variables."""
        config = {}

        if force_reindex := os.getenv("CHUNKHOUND_INDEXING__FORCE_REINDEX"):
            config["force_reindex"] = force_reindex.lower() in ("true", "1", "yes")

        # Handle comma-separated include/exclude patterns
        if include := os.getenv("CHUNKHOUND_INDEXING__INCLUDE"):
            config["include"] = include.split(",")
        if exclude := os.getenv("CHUNKHOUND_INDEXING__EXCLUDE"):
            config["exclude"] = exclude.split(",")

        return config

    @classmethod
    def extract_cli_overrides(cls, args: Any) -> dict[str, Any]:
        """Extract indexing config from CLI arguments."""
        overrides = {}

        if hasattr(args, "force_reindex") and args.force_reindex:
            overrides["force_reindex"] = args.force_reindex

        # Include/exclude patterns
        if hasattr(args, "include") and args.include:
            overrides["include"] = args.include
        if hasattr(args, "exclude") and args.exclude:
            overrides["exclude"] = args.exclude

        return overrides

    def __repr__(self) -> str:
        """String representation of indexing configuration."""
        return (
            f"IndexingConfig("
            f"force_reindex={self.force_reindex}, "
            f"patterns={len(self.include)} includes, {len(self.exclude)} excludes)"
        )
