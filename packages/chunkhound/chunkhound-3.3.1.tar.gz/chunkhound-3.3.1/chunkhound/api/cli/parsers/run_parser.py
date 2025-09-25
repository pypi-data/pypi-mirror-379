"""Run command argument parser for ChunkHound CLI."""

import argparse
from pathlib import Path
from typing import Any, cast

from .common_arguments import add_common_arguments, add_config_arguments


def validate_batch_sizes(
    embedding_batch_size: int | None, db_batch_size: int | None, provider: str
) -> tuple[bool, str]:
    """Validate batch size arguments against provider limits and system constraints.

    Args:
        embedding_batch_size: Number of texts per embedding API request
            (None uses default)
        db_batch_size: Number of records per database transaction (None uses default)
        provider: Embedding provider name

    Returns:
        Tuple of (is_valid, error_message)
    """
    # Use defaults if None
    if embedding_batch_size is None:
        embedding_batch_size = 50  # Default from EmbeddingConfig
    if db_batch_size is None:
        db_batch_size = 100  # Default from IndexingConfig
    # Provider-specific embedding batch limits
    embedding_limits: dict[str, tuple[int, int]] = {
        "openai": (1, 2048),
    }

    # Database batch limits (DuckDB optimized for large batches)
    db_limits = (1, 10000)

    # Validate embedding batch size
    if provider in embedding_limits:
        min_emb, max_emb = embedding_limits[provider]
        if not (min_emb <= embedding_batch_size <= max_emb):
            return (
                False,
                f"Embedding batch size {embedding_batch_size} invalid for provider "
                f"'{provider}'. Must be between {min_emb} and {max_emb}.",
            )
    else:
        # Default limits for unknown providers
        if not (1 <= embedding_batch_size <= 1000):
            return (
                False,
                f"Embedding batch size {embedding_batch_size} invalid. "
                f"Must be between 1 and 1000.",
            )

    # Validate database batch size
    min_db, max_db = db_limits
    if not (min_db <= db_batch_size <= max_db):
        return (
            False,
            f"Database batch size {db_batch_size} invalid. "
            f"Must be between {min_db} and {max_db}.",
        )

    return True, ""


def process_batch_arguments(args: argparse.Namespace) -> None:
    """Process and validate batch arguments, handle deprecation warnings.

    Args:
        args: Parsed command line arguments

    Raises:
        SystemExit: If batch size validation fails
    """
    import sys

    # Only process batch arguments if embedding config is present
    if not hasattr(args, "embedding_batch_size"):
        return

    # Handle backward compatibility - --batch-size maps to --embedding-batch-size
    batch_size = getattr(args, "batch_size", None)
    if batch_size is not None:
        print(
            f"WARNING: --batch-size is deprecated. "
            f"Use --embedding-batch-size instead.\n"
            f"         Using --embedding-batch-size {batch_size} based on "
            f"your --batch-size {batch_size}\n"
            f"         Consider also setting --db-batch-size for optimal performance",
            file=sys.stderr,
        )
        # Only override if embedding_batch_size is still default
        if args.embedding_batch_size == 100:  # Default value
            args.embedding_batch_size = batch_size

    # Validate batch sizes if all required arguments are present
    if hasattr(args, "db_batch_size"):
        is_valid, error_msg = validate_batch_sizes(
            args.embedding_batch_size,
            args.db_batch_size,
            getattr(args, "provider", "openai"),
        )

        if not is_valid:
            print(f"Error: {error_msg}", file=sys.stderr)
            sys.exit(1)


def add_run_subparser(subparsers: Any) -> argparse.ArgumentParser:
    """Add run command subparser to the main parser.

    Args:
        subparsers: Subparsers object from the main argument parser

    Returns:
        The configured run subparser
    """
    run_parser = subparsers.add_parser(
        "index",
        help="Index directory for code search",
        description=(
            "Scan and index a directory for code search, "
            "generating embeddings for semantic search."
        ),
    )

    # Optional positional argument with default to current directory
    run_parser.add_argument(
        "path",
        nargs="?",
        type=Path,
        default=Path("."),
        help="Directory path to index (default: current directory)",
    )

    # Add common arguments
    add_common_arguments(run_parser)

    # Add config-specific arguments
    add_config_arguments(run_parser, ["database", "embedding", "indexing", "mcp"])

    return cast(argparse.ArgumentParser, run_parser)


__all__: list[str] = ["add_run_subparser"]
