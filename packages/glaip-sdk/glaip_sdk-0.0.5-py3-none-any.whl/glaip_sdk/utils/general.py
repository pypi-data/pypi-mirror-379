"""General utility functions for AIP SDK.

Authors:
    Raymond Christopher (raymond.christopher@gdplabs.id)
"""

import re
from datetime import datetime
from uuid import UUID

import click


def is_uuid(value: str) -> bool:
    """Check if a string is a valid UUID.

    Args:
        value: String to check

    Returns:
        True if value is a valid UUID, False otherwise
    """
    try:
        UUID(value)
        return True
    except (ValueError, TypeError):
        return False


def sanitize_name(name: str) -> str:
    """Sanitize a name for resource creation.

    Args:
        name: Raw name input

    Returns:
        Sanitized name suitable for resource creation
    """
    # Remove special characters and normalize
    sanitized = re.sub(r"[^a-zA-Z0-9\-_]", "-", name.strip())
    sanitized = re.sub(r"-+", "-", sanitized)  # Collapse multiple dashes
    return sanitized.lower().strip("-")


def format_file_size(size_bytes: int) -> str:
    """Format file size in human readable format.

    Args:
        size_bytes: Size in bytes

    Returns:
        Human readable size string (e.g., "1.5 MB")
    """
    for unit in ["B", "KB", "MB", "GB"]:
        if size_bytes < 1024.0:
            return f"{size_bytes:.1f} {unit}"
        size_bytes /= 1024.0
    return f"{size_bytes:.1f} TB"


def format_datetime(dt):
    """Format datetime object to readable string.

    Args:
        dt: Datetime object or string to format

    Returns:
        Formatted datetime string or "N/A" if None
    """
    if isinstance(dt, datetime):
        return dt.strftime("%Y-%m-%d %H:%M:%S UTC")
    elif dt is None:
        return "N/A"
    return str(dt)


def progress_bar(iterable, description: str = "Processing"):
    """Simple progress bar using click.

    Args:
        iterable: Iterable to process
        description: Progress description

    Yields:
        Items from iterable with progress display
    """
    try:
        with click.progressbar(iterable, label=description) as bar:
            for item in bar:
                yield item
    except ImportError:
        # Fallback if click not available
        for item in iterable:
            yield item
