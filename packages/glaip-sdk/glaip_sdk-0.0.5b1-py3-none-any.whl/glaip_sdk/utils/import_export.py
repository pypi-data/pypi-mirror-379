"""Import/export utilities for schema transforms and data merging.

This module provides functions for converting between export and import formats,
merging imported data with CLI arguments, and handling relationship flattening.

Authors:
    Raymond Christopher (raymond.christopher@gdplabs.id)
"""

from typing import Any


def extract_ids_from_export(items: list[Any]) -> list[str]:
    """Extract IDs from export format (list of dicts with id/name fields).

    Args:
        items: List of items (dicts with id/name or strings)

    Returns:
        List of extracted IDs (only items with actual IDs)

    Examples:
        extract_ids_from_export([{"id": "123", "name": "tool"}]) -> ["123"]
        extract_ids_from_export(["123", "456"]) -> ["123", "456"]
        extract_ids_from_export([{"name": "tool"}, "123"]) -> ["123"]  # Skip items without ID
    """
    if not items:
        return []

    ids = []
    for item in items:
        if isinstance(item, str):
            ids.append(item)
        elif hasattr(item, "id"):
            ids.append(str(item.id))
        elif isinstance(item, dict) and "id" in item:
            ids.append(str(item["id"]))
        # Skip items without ID (don't convert to string)

    return ids


def convert_export_to_import_format(data: dict[str, Any]) -> dict[str, Any]:
    """Convert export format to import-compatible format (extract IDs from objects).

    Args:
        data: Export format data with full objects

    Returns:
        Import format data with extracted IDs

    Notes:
        - Converts tools/agents from dict objects to ID lists
        - Preserves all other data unchanged
    """
    import_data = data.copy()

    # Convert tools from dicts to IDs
    if "tools" in import_data and isinstance(import_data["tools"], list):
        import_data["tools"] = extract_ids_from_export(import_data["tools"])

    # Convert agents from dicts to IDs
    if "agents" in import_data and isinstance(import_data["agents"], list):
        import_data["agents"] = extract_ids_from_export(import_data["agents"])

    return import_data


def merge_import_with_cli_args(
    import_data: dict[str, Any],
    cli_args: dict[str, Any],
    array_fields: list[str] = None,
) -> dict[str, Any]:
    """Merge imported data with CLI arguments, preferring CLI args.

    Args:
        import_data: Data loaded from import file
        cli_args: Arguments passed via CLI
        array_fields: Fields that should be combined (merged) rather than replaced

    Returns:
        Merged data dictionary

    Notes:
        - CLI arguments take precedence over imported data
        - Array fields (tools, agents) are combined rather than replaced
        - Empty arrays/lists are treated as None (no override)
    """
    if array_fields is None:
        array_fields = ["tools", "agents"]

    merged = {}

    for key, cli_value in cli_args.items():
        if cli_value is not None and (
            not isinstance(cli_value, list | tuple) or len(cli_value) > 0
        ):
            # CLI value takes precedence (for non-empty values)
            if key in array_fields and key in import_data:
                # For array fields, combine CLI and imported values
                import_value = import_data[key]
                if isinstance(import_value, list):
                    merged[key] = list(cli_value) + import_value
                else:
                    merged[key] = cli_value
            else:
                merged[key] = cli_value
        elif key in import_data:
            # Use imported value if no CLI value
            merged[key] = import_data[key]

    # Add any import-only fields
    for key, import_value in import_data.items():
        if key not in merged:
            merged[key] = import_value

    return merged


def flatten_relationships_for_import(
    data: dict[str, Any], fields: tuple[str, ...] = ("tools", "agents")
) -> dict[str, Any]:
    """Flatten relationship fields for import format.

    This is an alias for convert_export_to_import_format with configurable fields.

    Args:
        data: Export format data with full objects
        fields: Tuple of field names to flatten to IDs

    Returns:
        Import format data with specified fields flattened to IDs
    """
    import_data = data.copy()

    for field in fields:
        if field in import_data and isinstance(import_data[field], list):
            import_data[field] = extract_ids_from_export(import_data[field])

    return import_data
