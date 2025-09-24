"""Tool management commands.

Authors:
    Raymond Christopher (raymond.christopher@gdplabs.id)
"""

import json
import re
from pathlib import Path

import click
from rich.console import Console
from rich.text import Text

from glaip_sdk.cli.display import (
    display_api_error,
    display_confirmation_prompt,
    display_creation_success,
    display_deletion_success,
    display_update_success,
    handle_json_output,
    handle_rich_output,
)
from glaip_sdk.cli.io import (
    export_resource_to_file_with_validation as export_resource_to_file,
)
from glaip_sdk.cli.io import (
    fetch_raw_resource_details,
)
from glaip_sdk.cli.io import (
    load_resource_from_file_with_validation as load_resource_from_file,
)
from glaip_sdk.cli.resolution import resolve_resource_reference
from glaip_sdk.cli.utils import (
    coerce_to_row,
    get_client,
    output_flags,
    output_list,
    output_result,
)
from glaip_sdk.utils import format_datetime
from glaip_sdk.utils.import_export import merge_import_with_cli_args

console = Console()


@click.group(name="tools", no_args_is_help=True)
def tools_group():
    """Tool management operations."""
    pass


def _resolve_tool(ctx, client, ref, select=None):
    """Resolve tool reference (ID or name) with ambiguity handling."""
    return resolve_resource_reference(
        ctx,
        client,
        ref,
        "tool",
        client.get_tool,
        client.find_tools,
        "Tool",
        select=select,
    )


# ----------------------------- Helpers --------------------------------- #


def _extract_internal_name(code: str) -> str:
    """Extract plugin class name attribute from tool code."""
    m = re.search(r'^\s*name\s*:\s*str\s*=\s*"([^"]+)"', code, re.M)
    if not m:
        m = re.search(r'^\s*name\s*=\s*"([^"]+)"', code, re.M)
    if not m:
        raise click.ClickException(
            "Could not find plugin 'name' attribute in the tool file. "
            'Ensure your plugin class defines e.g. name: str = "my_tool".'
        )
    return m.group(1)


def _validate_name_match(provided: str | None, internal: str) -> str:
    """Validate provided --name against internal name; return effective name."""
    if provided and provided != internal:
        raise click.ClickException(
            f"--name '{provided}' does not match plugin internal name '{internal}'. "
            "Either update the code or pass a matching --name."
        )
    return provided or internal


def _check_duplicate_name(client, tool_name: str) -> None:
    """Raise if a tool with the same name already exists."""
    try:
        existing = client.find_tools(name=tool_name)
        if existing:
            raise click.ClickException(
                f"A tool named '{tool_name}' already exists. "
                "Please change your plugin's 'name' to a unique value, then re-run."
            )
    except click.ClickException:
        # Re-raise ClickException (intended error)
        raise
    except Exception:
        # Non-fatal: best-effort duplicate check for other errors
        pass


def _parse_tags(tags: str | None) -> list[str]:
    return [t.strip() for t in (tags.split(",") if tags else []) if t.strip()]


@tools_group.command(name="list")
@output_flags()
@click.option(
    "--type",
    "tool_type",
    help="Filter tools by type (e.g., custom, native)",
    type=str,
    required=False,
)
@click.pass_context
def list_tools(ctx, tool_type):
    """List all tools."""
    try:
        client = get_client(ctx)
        tools = client.list_tools(tool_type=tool_type)

        # Define table columns: (data_key, header, style, width)
        columns = [
            ("id", "ID", "dim", 36),
            ("name", "Name", "cyan", None),
            ("framework", "Framework", "blue", None),
        ]

        # Transform function for safe dictionary access
        def transform_tool(tool):
            row = coerce_to_row(tool, ["id", "name", "framework"])
            # Ensure id is always a string
            row["id"] = str(row["id"])
            return row

        output_list(ctx, tools, "🔧 Available Tools", columns, transform_tool)

    except Exception as e:
        raise click.ClickException(str(e))


@tools_group.command()
@click.argument("file_arg", required=False, type=click.Path(exists=True))
@click.option(
    "--file",
    type=click.Path(exists=True),
    help="Tool file to upload (optional for metadata-only tools)",
)
@click.option(
    "--name",
    help="Tool name (required for metadata-only tools, extracted from script if file provided)",
)
@click.option(
    "--description",
    help="Tool description (optional - extracted from script if file provided)",
)
@click.option(
    "--tags",
    help="Comma-separated tags for the tool",
)
@click.option(
    "--import",
    "import_file",
    type=click.Path(exists=True, dir_okay=False),
    help="Import tool configuration from JSON file",
)
@output_flags()
@click.pass_context
def create(ctx, file_arg, file, name, description, tags, import_file):
    """Create a new tool.

    Examples:
        aip tools create --name "My Tool" --description "A helpful tool"
        aip tools create tool.py  # Create from file
        aip tools create --import tool.json  # Create from exported configuration
    """
    try:
        client = get_client(ctx)

        # Initialize merged_data for cases without import_file
        merged_data = {}

        # Handle import from file
        if import_file:
            import_data = load_resource_from_file(Path(import_file), "tool")

            # Merge CLI args with imported data
            cli_args = {
                "name": name,
                "description": description,
                "tags": tags,
            }

            merged_data = merge_import_with_cli_args(import_data, cli_args)
        else:
            # No import file - use CLI args directly
            merged_data = {
                "name": name,
                "description": description,
                "tags": tags,
            }

        # Extract merged values
        name = merged_data.get("name")
        description = merged_data.get("description")
        tags = merged_data.get("tags")

        # Allow positional file argument for better DX (matches examples)
        if not file and file_arg:
            file = file_arg

        # Validate required parameters based on creation method
        if not file and not import_file:
            # Metadata-only tool creation
            if not name:
                raise click.ClickException(
                    "--name is required when creating metadata-only tools"
                )

        # Create tool based on whether file is provided
        if file:
            # File-based tool creation — validate internal plugin name, no rewriting
            with open(file, encoding="utf-8") as f:
                code_content = f.read()

            internal_name = _extract_internal_name(code_content)
            tool_name = _validate_name_match(name, internal_name)
            _check_duplicate_name(client, tool_name)

            # Upload the plugin code as-is (no rewrite)
            tool = client.create_tool_from_code(
                name=tool_name,
                code=code_content,
                framework="langchain",  # Always langchain
                description=description,
                tags=_parse_tags(tags) if tags else None,
            )
        else:
            # Metadata-only tool creation or import from file
            tool_kwargs = {}
            if name:
                tool_kwargs["name"] = name
            tool_kwargs["tool_type"] = "custom"  # Always custom
            tool_kwargs["framework"] = "langchain"  # Always langchain
            if description:
                tool_kwargs["description"] = description
            if tags:
                tool_kwargs["tags"] = _parse_tags(tags)

            # If importing from file, include all other detected attributes
            if import_file:
                # Add all other attributes from import data (excluding already handled ones)
                excluded_fields = {
                    "name",
                    "description",
                    "tags",
                    # System-only fields that shouldn't be passed to create_tool
                    "id",
                    "created_at",
                    "updated_at",
                    "tool_type",
                    "framework",
                    "version",
                }
                for key, value in merged_data.items():
                    if key not in excluded_fields and value is not None:
                        tool_kwargs[key] = value

            tool = client.create_tool(**tool_kwargs)

        # Handle JSON output
        handle_json_output(ctx, tool.model_dump())

        # Handle Rich output
        creation_method = "file upload (custom)" if file else "metadata only (native)"
        rich_panel = display_creation_success(
            "Tool",
            tool.name,
            tool.id,
            Framework=getattr(tool, "framework", "N/A"),
            Type=getattr(tool, "tool_type", "N/A"),
            Description=getattr(tool, "description", "No description"),
            Method=creation_method,
        )
        handle_rich_output(ctx, rich_panel)

    except Exception as e:
        handle_json_output(ctx, error=e)
        if ctx.obj.get("view") != "json":
            display_api_error(e, "tool creation")
        raise click.ClickException(str(e))


@tools_group.command()
@click.argument("tool_ref")
@click.option("--select", type=int, help="Choose among ambiguous matches (1-based)")
@click.option(
    "--export",
    type=click.Path(dir_okay=False, writable=True),
    help="Export complete tool configuration to file (format auto-detected from .json/.yaml extension)",
)
@output_flags()
@click.pass_context
def get(ctx, tool_ref, select, export):
    """Get tool details.

    Examples:
        aip tools get my-tool
        aip tools get my-tool --export tool.json    # Exports complete configuration as JSON
        aip tools get my-tool --export tool.yaml    # Exports complete configuration as YAML
    """
    try:
        client = get_client(ctx)

        # Resolve tool with ambiguity handling
        tool = _resolve_tool(ctx, client, tool_ref, select)

        # Handle export option
        if export:
            export_path = Path(export)
            # Auto-detect format from file extension
            if export_path.suffix.lower() in [".yaml", ".yml"]:
                detected_format = "yaml"
            else:
                detected_format = "json"

            # Always export comprehensive data - re-fetch tool with full details if needed
            try:
                tool = client.get_tool_by_id(tool.id)
            except Exception as e:
                console.print(
                    Text(f"[yellow]⚠️  Could not fetch full tool details: {e}[/yellow]")
                )
                console.print(
                    Text("[yellow]⚠️  Proceeding with available data[/yellow]")
                )

            export_resource_to_file(tool, export_path, detected_format)
            console.print(
                Text(
                    f"[green]✅ Complete tool configuration exported to: {export_path} (format: {detected_format})[/green]"
                )
            )

        # Try to fetch raw API data first to preserve ALL fields
        raw_tool_data = fetch_raw_resource_details(client, tool, "tools")

        if raw_tool_data:
            # Use raw API data - this preserves ALL fields
            # Format dates for better display (minimal postprocessing)
            formatted_data = raw_tool_data.copy()
            if "created_at" in formatted_data:
                formatted_data["created_at"] = format_datetime(
                    formatted_data["created_at"]
                )
            if "updated_at" in formatted_data:
                formatted_data["updated_at"] = format_datetime(
                    formatted_data["updated_at"]
                )

            # Display using output_result with raw data
            output_result(
                ctx,
                formatted_data,
                title="Tool Details",
                panel_title=f"🔧 {raw_tool_data.get('name', 'Unknown')}",
            )
        else:
            # Fall back to original method if raw fetch fails
            console.print("[yellow]Falling back to Pydantic model data[/yellow]")

            # Create result data with all available fields from backend
            result_data = {
                "id": str(getattr(tool, "id", "N/A")),
                "name": getattr(tool, "name", "N/A"),
                "tool_type": getattr(tool, "tool_type", "N/A"),
                "framework": getattr(tool, "framework", "N/A"),
                "version": getattr(tool, "version", "N/A"),
                "description": getattr(tool, "description", "N/A"),
            }

            output_result(
                ctx, result_data, title="Tool Details", panel_title=f"🔧 {tool.name}"
            )

    except Exception as e:
        raise click.ClickException(str(e))


@tools_group.command()
@click.argument("tool_id")
@click.option(
    "--file",
    type=click.Path(exists=True),
    help="New tool file for code update (custom tools only)",
)
@click.option("--description", help="New description")
@click.option("--tags", help="Comma-separated tags")
@output_flags()
@click.pass_context
def update(ctx, tool_id, file, description, tags):
    """Update a tool (code or metadata)."""
    try:
        client = get_client(ctx)

        # Get tool by ID (no ambiguity handling needed)
        try:
            tool = client.get_tool_by_id(tool_id)
        except Exception as e:
            raise click.ClickException(f"Tool with ID '{tool_id}' not found: {e}")

        # Prepare update data
        update_data = {}
        if description:
            update_data["description"] = description
        if tags:
            update_data["tags"] = [tag.strip() for tag in tags.split(",")]

        if file:
            # Update code via file upload (custom tools only)
            if tool.tool_type != "custom":
                raise click.ClickException(
                    f"File updates are only supported for custom tools. Tool '{tool.name}' is of type '{tool.tool_type}'."
                )
            updated_tool = client.tools.update_tool_via_file(
                tool.id, file, framework=tool.framework
            )
            handle_rich_output(
                ctx, Text(f"[green]✓[/green] Tool code updated from {file}")
            )
        elif update_data:
            # Update metadata only (native tools only)
            if tool.tool_type != "native":
                raise click.ClickException(
                    f"Metadata updates are only supported for native tools. Tool '{tool.name}' is of type '{tool.tool_type}'."
                )
            updated_tool = tool.update(**update_data)
            handle_rich_output(ctx, Text("[green]✓[/green] Tool metadata updated"))
        else:
            handle_rich_output(ctx, Text("[yellow]No updates specified[/yellow]"))
            return

        handle_json_output(ctx, updated_tool.model_dump())
        handle_rich_output(ctx, display_update_success("Tool", updated_tool.name))

    except Exception as e:
        handle_json_output(ctx, error=e)
        if ctx.obj.get("view") != "json":
            display_api_error(e, "tool update")
        raise click.ClickException(str(e))


@tools_group.command()
@click.argument("tool_id")
@click.option("-y", "--yes", is_flag=True, help="Skip confirmation")
@output_flags()
@click.pass_context
def delete(ctx, tool_id, yes):
    """Delete a tool."""
    try:
        client = get_client(ctx)

        # Get tool by ID (no ambiguity handling needed)
        try:
            tool = client.get_tool_by_id(tool_id)
        except Exception as e:
            raise click.ClickException(f"Tool with ID '{tool_id}' not found: {e}")

        # Confirm deletion via centralized display helper
        if not yes and not display_confirmation_prompt("Tool", tool.name):
            return

        tool.delete()

        handle_json_output(
            ctx,
            {
                "success": True,
                "message": f"Tool '{tool.name}' deleted",
            },
        )
        handle_rich_output(ctx, display_deletion_success("Tool", tool.name))

    except Exception as e:
        handle_json_output(ctx, error=e)
        if ctx.obj.get("view") != "json":
            display_api_error(e, "tool deletion")
        raise click.ClickException(str(e))


@tools_group.command("script")
@click.argument("tool_id")
@output_flags()
@click.pass_context
def script(ctx, tool_id):
    """Get tool script content."""
    try:
        client = get_client(ctx)
        script_content = client.get_tool_script(tool_id)

        if ctx.obj.get("view") == "json":
            click.echo(json.dumps({"script": script_content}, indent=2))
        else:
            console.print(f"[green]📜 Tool Script for '{tool_id}':[/green]")
            console.print(script_content)

    except Exception as e:
        handle_json_output(ctx, error=e)
        if ctx.obj.get("view") != "json":
            console.print(Text(f"[red]Error getting tool script: {e}[/red]"))
        raise click.ClickException(str(e))
