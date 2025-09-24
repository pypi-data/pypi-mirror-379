"""Agent CLI commands for AIP SDK.

Authors:
    Raymond Christopher (raymond.christopher@gdplabs.id)
"""

import json
import os
from pathlib import Path

import click
from rich.console import Console
from rich.text import Text

from glaip_sdk.cli.agent_config import (
    merge_agent_config_with_cli_args as merge_import_with_cli_args,
)
from glaip_sdk.cli.agent_config import (
    resolve_agent_language_model_selection as resolve_language_model_selection,
)
from glaip_sdk.cli.agent_config import (
    sanitize_agent_config_for_cli as sanitize_agent_config,
)
from glaip_sdk.cli.display import (
    build_resource_result_data,
    display_agent_run_suggestions,
    display_confirmation_prompt,
    display_creation_success,
    display_deletion_success,
    display_update_success,
    handle_json_output,
    handle_rich_output,
    print_api_error,
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
    _fuzzy_pick_for_resources,
    build_renderer,
    coerce_to_row,
    get_client,
    output_flags,
    output_list,
    output_result,
)
from glaip_sdk.cli.validators import (
    validate_agent_instruction_cli as validate_agent_instruction,
)
from glaip_sdk.cli.validators import (
    validate_agent_name_cli as validate_agent_name,
)
from glaip_sdk.cli.validators import (
    validate_timeout_cli as validate_timeout,
)
from glaip_sdk.config.constants import DEFAULT_AGENT_RUN_TIMEOUT, DEFAULT_MODEL
from glaip_sdk.exceptions import AgentTimeoutError
from glaip_sdk.utils import format_datetime, is_uuid
from glaip_sdk.utils.agent_config import normalize_agent_config_for_import
from glaip_sdk.utils.import_export import convert_export_to_import_format
from glaip_sdk.utils.validation import coerce_timeout

console = Console()

# Error message constants
AGENT_NOT_FOUND_ERROR = "Agent not found"


def _fetch_full_agent_details(client, agent):
    """Fetch full agent details by ID to ensure all fields are populated."""
    try:
        agent_id = str(getattr(agent, "id", "")).strip()
        if agent_id:
            return client.agents.get_agent_by_id(agent_id)
    except Exception:
        # If fetching full details fails, continue with the resolved object
        pass
    return agent


def _get_agent_model_name(agent):
    """Extract model name from agent configuration."""
    # Try different possible locations for model name
    if hasattr(agent, "agent_config") and agent.agent_config:
        if isinstance(agent.agent_config, dict):
            return agent.agent_config.get("lm_name") or agent.agent_config.get("model")

    if hasattr(agent, "model") and agent.model:
        return agent.model

    # Default fallback
    return DEFAULT_MODEL


def _resolve_resources_by_name(
    _client, items: tuple[str, ...], resource_type: str, find_func, label: str
) -> list[str]:
    """Resolve resource names/IDs to IDs, handling ambiguity.

    Args:
        client: API client
        items: Tuple of resource names/IDs
        resource_type: Type of resource ("tool" or "agent")
        find_func: Function to find resources by name
        label: Label for error messages

    Returns:
        List of resolved resource IDs
    """
    out = []
    for ref in list(items or ()):
        if is_uuid(ref):
            out.append(ref)
            continue

        matches = find_func(name=ref)
        if not matches:
            raise click.ClickException(f"{label} not found: {ref}")
        if len(matches) > 1:
            raise click.ClickException(
                f"Multiple {resource_type}s named '{ref}'. Use ID instead."
            )
        out.append(str(matches[0].id))
    return out


def _display_agent_details(ctx, client, agent):
    """Display full agent details using raw API data to preserve ALL fields."""
    if agent is None:
        handle_rich_output(ctx, Text("[red]❌ No agent provided[/red]"))
        return

    # Try to fetch raw API data first to preserve ALL fields
    raw_agent_data = fetch_raw_resource_details(client, agent, "agents")

    if raw_agent_data:
        # Use raw API data - this preserves ALL fields including account_id
        # Format dates for better display (minimal postprocessing)
        formatted_data = raw_agent_data.copy()
        if "created_at" in formatted_data:
            formatted_data["created_at"] = format_datetime(formatted_data["created_at"])
        if "updated_at" in formatted_data:
            formatted_data["updated_at"] = format_datetime(formatted_data["updated_at"])

        # Display using output_result with raw data
        output_result(
            ctx,
            formatted_data,
            title="Agent Details",
            panel_title=f"🤖 {raw_agent_data.get('name', 'Unknown')}",
        )
    else:
        # Fall back to original method if raw fetch fails
        handle_rich_output(
            ctx, Text("[yellow]Falling back to Pydantic model data[/yellow]")
        )
        full_agent = _fetch_full_agent_details(client, agent)

        # Build result data using standardized helper
        fields = [
            "id",
            "name",
            "type",
            "framework",
            "version",
            "description",
            "instruction",
            "created_at",
            "updated_at",
            "metadata",
            "language_model_id",
            "agent_config",
            "tool_configs",
            "tools",
            "agents",
            "mcps",
            "a2a_profile",
        ]
        result_data = build_resource_result_data(full_agent, fields)
        if not result_data.get("instruction"):
            result_data["instruction"] = "-"  # pragma: no cover - cosmetic fallback

        # Format dates for better display
        if "created_at" in result_data and result_data["created_at"] not in [
            "N/A",
            None,
        ]:
            result_data["created_at"] = format_datetime(result_data["created_at"])
        if "updated_at" in result_data and result_data["updated_at"] not in [
            "N/A",
            None,
        ]:
            result_data["updated_at"] = format_datetime(result_data["updated_at"])

        # Display using output_result
        output_result(
            ctx,
            result_data,
            title="Agent Details",
            panel_title=f"🤖 {full_agent.name}",
        )


@click.group(name="agents", no_args_is_help=True)
def agents_group():
    """Agent management operations."""
    pass


def _resolve_agent(ctx, client, ref, select=None, interface_preference="fuzzy"):
    """Resolve agent reference (ID or name) with ambiguity handling.

    Args:
        interface_preference: "fuzzy" for fuzzy picker, "questionary" for up/down list
    """
    return resolve_resource_reference(
        ctx,
        client,
        ref,
        "agent",
        client.agents.get_agent_by_id,
        client.agents.find_agents,
        "Agent",
        select=select,
        interface_preference=interface_preference,
    )


@agents_group.command(name="list")
@click.option(
    "--simple", is_flag=True, help="Show simple table without interactive picker"
)
@click.option(
    "--type", "agent_type", help="Filter by agent type (config, code, a2a, langflow)"
)
@click.option(
    "--framework", help="Filter by framework (langchain, langgraph, google_adk)"
)
@click.option("--name", help="Filter by partial name match (case-insensitive)")
@click.option("--version", help="Filter by exact version match")
@click.option(
    "--sync-langflow",
    is_flag=True,
    help="Sync with LangFlow server before listing (only applies when filtering by langflow type)",
)
@output_flags()
@click.pass_context
def list_agents(ctx, simple, agent_type, framework, name, version, sync_langflow):
    """List agents with optional filtering."""
    try:
        client = get_client(ctx)
        agents = client.agents.list_agents(
            agent_type=agent_type,
            framework=framework,
            name=name,
            version=version,
            sync_langflow_agents=sync_langflow,
        )

        # Define table columns: (data_key, header, style, width)
        columns = [
            ("id", "ID", "dim", 36),
            ("name", "Name", "cyan", None),
            ("type", "Type", "yellow", None),
            ("framework", "Framework", "blue", None),
            ("version", "Version", "green", None),
        ]

        # Transform function for safe attribute access
        def transform_agent(agent):
            row = coerce_to_row(agent, ["id", "name", "type", "framework", "version"])
            # Ensure id is always a string
            row["id"] = str(row["id"])
            return row

        # Use fuzzy picker for interactive agent selection and details (default behavior)
        # Skip if --simple flag is used
        if not simple and console.is_terminal and os.isatty(1) and len(agents) > 0:
            picked_agent = _fuzzy_pick_for_resources(agents, "agent", "")
            if picked_agent:
                _display_agent_details(ctx, client, picked_agent)
                # Show run suggestions via centralized display helper
                handle_rich_output(ctx, display_agent_run_suggestions(picked_agent))
                return

        # Show simple table (either --simple flag or non-interactive)
        output_list(ctx, agents, "🤖 Available Agents", columns, transform_agent)

    except Exception as e:
        raise click.ClickException(str(e))


@agents_group.command()
@click.argument("agent_ref")
@click.option("--select", type=int, help="Choose among ambiguous matches (1-based)")
@click.option(
    "--export",
    type=click.Path(dir_okay=False, writable=True),
    help="Export complete agent configuration to file (format auto-detected from .json/.yaml extension)",
)
@output_flags()
@click.pass_context
def get(ctx, agent_ref, select, export):
    """Get agent details.

    Examples:
        aip agents get my-agent
        aip agents get my-agent --export agent.json    # Exports complete configuration as JSON
        aip agents get my-agent --export agent.yaml    # Exports complete configuration as YAML
    """
    try:
        client = get_client(ctx)

        # Resolve agent with ambiguity handling - use questionary interface for traditional UX
        agent = _resolve_agent(
            ctx, client, agent_ref, select, interface_preference="questionary"
        )

        # Handle export option
        if export:  # pragma: no cover - requires filesystem verification
            export_path = Path(export)
            # Auto-detect format from file extension
            if export_path.suffix.lower() in [".yaml", ".yml"]:
                detected_format = "yaml"
            else:
                detected_format = "json"

            # Always export comprehensive data - re-fetch agent with full details
            try:
                agent = client.agents.get_agent_by_id(agent.id)
            except Exception as e:  # pragma: no cover - best-effort fallback messaging
                handle_rich_output(
                    ctx,
                    Text(
                        f"[yellow]⚠️  Could not fetch full agent details: {e}[/yellow]"
                    ),
                )
                handle_rich_output(
                    ctx, Text("[yellow]⚠️  Proceeding with available data[/yellow]")
                )

            export_resource_to_file(agent, export_path, detected_format)
            handle_rich_output(
                ctx,
                Text(
                    f"[green]✅ Complete agent configuration exported to: {export_path} (format: {detected_format})[/green]"
                ),
            )

        # Display full agent details using the standardized helper
        _display_agent_details(ctx, client, agent)

        # Show run suggestions via centralized display helper
        handle_rich_output(ctx, display_agent_run_suggestions(agent))

    except Exception as e:
        raise click.ClickException(str(e))


def _validate_run_input(input_option, input_text):
    """Validate and determine the final input text for agent run."""
    final_input_text = input_option if input_option else input_text

    if not final_input_text:
        raise click.ClickException(
            "Input text is required. Use either positional argument or --input option."
        )

    return final_input_text


def _parse_chat_history(chat_history):
    """Parse chat history JSON if provided."""
    if not chat_history:
        return None

    try:
        return json.loads(chat_history)
    except json.JSONDecodeError:
        raise click.ClickException("Invalid JSON in chat history")


def _setup_run_renderer(ctx, save, verbose):
    """Set up renderer and working console for agent run."""
    tty_enabled = bool((ctx.obj or {}).get("tty", True))
    return build_renderer(
        ctx,
        save_path=save,
        verbose=verbose,
        _tty_enabled=tty_enabled,
    )


def _prepare_run_kwargs(
    agent, final_input_text, files, parsed_chat_history, renderer, tty_enabled
):
    """Prepare kwargs for agent run."""
    run_kwargs = {
        "agent_id": agent.id,
        "message": final_input_text,
        "files": list(files),
        "agent_name": agent.name,
        "tty": tty_enabled,
    }

    if parsed_chat_history:
        run_kwargs["chat_history"] = parsed_chat_history

    if renderer is not None:
        run_kwargs["renderer"] = renderer

    return run_kwargs


def _handle_run_output(ctx, result, renderer):
    """Handle output formatting for agent run results."""
    printed_by_renderer = bool(renderer)
    selected_view = (ctx.obj or {}).get("view", "rich")

    if not printed_by_renderer:
        if selected_view == "json":
            handle_json_output(ctx, {"output": result})
        elif selected_view == "md":
            click.echo(f"# Assistant\n\n{result}")
        elif selected_view == "plain":
            click.echo(result)


def _save_run_transcript(save, result, working_console):
    """Save transcript to file if requested."""
    if not save:
        return

    ext = (save.rsplit(".", 1)[-1] or "").lower()
    if ext == "json":
        save_data = {
            "output": result or "",
            "full_debug_output": getattr(
                working_console, "get_captured_output", lambda: ""
            )(),
            "timestamp": "captured during agent execution",
        }
        content = json.dumps(save_data, indent=2)
    else:
        full_output = getattr(working_console, "get_captured_output", lambda: "")()
        if full_output:
            content = f"# Agent Debug Log\n\n{full_output}\n\n---\n\n## Final Result\n\n{result or ''}\n"
        else:
            content = f"# Assistant\n\n{result or ''}\n"

    with open(save, "w", encoding="utf-8") as f:
        f.write(content)
    console.print(Text(f"[green]Full debug output saved to: {save}[/green]"))


@agents_group.command()
@click.argument("agent_ref")
@click.argument("input_text", required=False)
@click.option("--select", type=int, help="Choose among ambiguous matches (1-based)")
@click.option("--input", "input_option", help="Input text for the agent")
@click.option("--chat-history", help="JSON string of chat history")
@click.option(
    "--timeout",
    default=DEFAULT_AGENT_RUN_TIMEOUT,
    type=int,
    help="Agent execution timeout in seconds (default: 300s)",
)
@click.option(
    "--save",
    type=click.Path(dir_okay=False, writable=True),
    help="Save transcript to file (md or json)",
)
@click.option(
    "--file",
    "files",
    multiple=True,
    type=click.Path(exists=True),
    help="Attach file(s)",
)
@click.option(
    "--verbose/--no-verbose",
    default=False,
    help="Show detailed SSE events during streaming",
)
@output_flags()
@click.pass_context
def run(
    ctx,
    agent_ref,
    select,
    input_text,
    input_option,
    chat_history,
    timeout,
    save,
    files,
    verbose,
):
    """Run an agent with input text.

    Usage: aip agents run <agent_ref> <input_text> [OPTIONS]

    Examples:
        aip agents run my-agent "Hello world"
        aip agents run agent-123 "Process this data" --timeout 600
        aip agents run my-agent --input "Hello world"  # Legacy style
    """
    final_input_text = _validate_run_input(input_option, input_text)

    try:
        client = get_client(ctx)
        agent = _resolve_agent(
            ctx, client, agent_ref, select, interface_preference="fuzzy"
        )

        parsed_chat_history = _parse_chat_history(chat_history)
        renderer, working_console = _setup_run_renderer(ctx, save, verbose)

        try:
            client.timeout = float(timeout)
        except Exception:
            pass

        run_kwargs = _prepare_run_kwargs(
            agent,
            final_input_text,
            files,
            parsed_chat_history,
            renderer,
            bool((ctx.obj or {}).get("tty", True)),
        )

        result = client.agents.run_agent(**run_kwargs, timeout=timeout)

        _handle_run_output(ctx, result, renderer)
        _save_run_transcript(save, result, working_console)

    except AgentTimeoutError as e:
        error_msg = str(e)
        handle_json_output(ctx, error=Exception(error_msg))
        raise click.ClickException(error_msg)
    except Exception as e:
        handle_json_output(ctx, error=e)
        raise click.ClickException(str(e))


@agents_group.command()
@click.option("--name", help="Agent name")
@click.option("--instruction", help="Agent instruction (prompt)")
@click.option(
    "--model",
    help=f"Language model to use (e.g., {DEFAULT_MODEL}, default: {DEFAULT_MODEL})",
)
@click.option("--tools", multiple=True, help="Tool names or IDs to attach")
@click.option("--agents", multiple=True, help="Sub-agent names or IDs to attach")
@click.option("--mcps", multiple=True, help="MCP names or IDs to attach")
@click.option(
    "--timeout",
    default=DEFAULT_AGENT_RUN_TIMEOUT,
    type=int,
    help="Agent execution timeout in seconds (default: 300s)",
)
@click.option(
    "--import",
    "import_file",
    type=click.Path(exists=True, dir_okay=False),
    help="Import agent configuration from JSON file",
)
@output_flags()
@click.pass_context
def create(
    ctx,
    name,
    instruction,
    model,
    tools,
    agents,
    mcps,
    timeout,
    import_file,
):
    """Create a new agent.

    Examples:
        aip agents create --name "My Agent" --instruction "You are a helpful assistant"
        aip agents create --import agent.json
    """
    try:
        client = get_client(ctx)

        # Initialize merged_data for cases without import_file
        merged_data = {}

        # Handle import from file
        if (
            import_file
        ):  # pragma: no cover - exercised in higher-level integration tests
            import_data = load_resource_from_file(Path(import_file), "agent")

            # Convert export format to import-compatible format
            import_data = convert_export_to_import_format(import_data)

            # Auto-normalize agent config (extract LM settings from agent_config)
            import_data = normalize_agent_config_for_import(import_data, model)

            # Merge CLI args with imported data
            cli_args = {
                "name": name,
                "instruction": instruction,
                "model": model,
                "tools": tools or (),
                "agents": agents or (),
                "mcps": mcps or (),
                "timeout": timeout if timeout != DEFAULT_AGENT_RUN_TIMEOUT else None,
            }

            merged_data = merge_import_with_cli_args(import_data, cli_args)
        else:
            # No import file - use CLI args directly
            merged_data = {
                "name": name,
                "instruction": instruction,
                "model": model,
                "tools": tools or (),
                "agents": agents or (),
                "mcps": mcps or (),
                "timeout": timeout if timeout != DEFAULT_AGENT_RUN_TIMEOUT else None,
            }

        # Extract merged values
        name = merged_data.get("name")
        instruction = merged_data.get("instruction")
        model = merged_data.get("model")
        tools = tuple(merged_data.get("tools", ()))
        agents = tuple(merged_data.get("agents", ()))
        mcps = tuple(merged_data.get("mcps", ()))
        timeout = merged_data.get("timeout", DEFAULT_AGENT_RUN_TIMEOUT)
        # Coerce timeout to proper integer type
        timeout = coerce_timeout(timeout)

        # Validate required fields using centralized validators
        if not name:
            raise click.ClickException("Agent name is required (--name or --import)")
        if not instruction:
            raise click.ClickException(
                "Agent instruction is required (--instruction or --import)"
            )

        # Apply validation
        name = validate_agent_name(name)
        instruction = validate_agent_instruction(instruction)
        if timeout is not None:
            timeout = validate_timeout(timeout)

        # Resolve tool and agent references: accept names or IDs
        resolved_tools = _resolve_resources_by_name(
            client, tools, "tool", client.find_tools, "Tool"
        )
        resolved_agents = _resolve_resources_by_name(
            client, agents, "agent", client.find_agents, "Agent"
        )
        resolved_mcps = _resolve_resources_by_name(
            client, mcps, "mcp", client.find_mcps, "MCP"
        )

        # Create agent with comprehensive attribute support
        create_kwargs = {
            "name": name,
            "instruction": instruction,
            "tools": resolved_tools or None,
            "agents": resolved_agents or None,
            "mcps": resolved_mcps or None,
            "timeout": timeout,
        }

        # Handle language model selection using helper function
        lm_selection_dict, should_strip_lm_identity = resolve_language_model_selection(
            merged_data, model
        )
        create_kwargs.update(lm_selection_dict)

        # If importing from file, include agent_config (pass-through minus credentials)
        if import_file:
            agent_config_raw = (
                merged_data.get("agent_config")
                if isinstance(merged_data, dict)
                else None
            )
            if isinstance(agent_config_raw, dict):
                # If language_model_id is used, strip LM identity keys from agent_config to avoid conflicts
                create_kwargs["agent_config"] = sanitize_agent_config(
                    agent_config_raw, strip_lm_identity=should_strip_lm_identity
                )

        # If importing from file, include all other detected attributes
        if import_file:
            # Add all other attributes from import data (excluding already handled ones and system-only fields)
            excluded_fields = {
                "name",
                "instruction",
                "model",
                "language_model_id",
                "tools",
                "agents",
                "timeout",
                "agent_config",  # handled explicitly above
                # System-only fields that shouldn't be passed to create_agent
                "id",
                "created_at",
                "updated_at",
                "type",
                "framework",
                "version",
                "tool_configs",
                "mcps",
                "a2a_profile",
            }
            for key, value in merged_data.items():
                if key not in excluded_fields and value is not None:
                    create_kwargs[key] = value

        agent = client.agents.create_agent(**create_kwargs)

        handle_json_output(ctx, agent.model_dump())

        lm_display = getattr(agent, "model", None)
        if not lm_display:
            cfg = getattr(agent, "agent_config", {}) or {}
            lm_display = (
                cfg.get("lm_name")
                or cfg.get("model")
                or model
                or f"{DEFAULT_MODEL} (backend default)"
            )

        handle_rich_output(
            ctx,
            display_creation_success(
                "Agent",
                agent.name,
                agent.id,
                Model=lm_display,
                Type=getattr(agent, "type", "config"),
                Framework=getattr(agent, "framework", "langchain"),
                Version=getattr(agent, "version", "1.0"),
            ),
        )
        handle_rich_output(ctx, display_agent_run_suggestions(agent))

    except (
        click.ClickException
    ):  # pragma: no cover - error formatting verified elsewhere
        # Handle JSON output for ClickExceptions if view is JSON
        if ctx.obj.get("view") == "json":
            handle_json_output(ctx, error=Exception(AGENT_NOT_FOUND_ERROR))
        # Re-raise ClickExceptions without additional processing
        raise
    except Exception as e:  # pragma: no cover - defensive logging path
        handle_json_output(ctx, error=e)
        if ctx.obj.get("view") != "json":
            print_api_error(e)
        raise click.ClickException(str(e))


def _get_agent_for_update(client, agent_id):
    """Retrieve agent by ID for update operation."""
    try:
        return client.agents.get_agent_by_id(agent_id)
    except Exception as e:
        raise click.ClickException(f"Agent with ID '{agent_id}' not found: {e}")


def _handle_update_import_file(import_file, name, instruction, tools, agents, timeout):
    """Handle import file processing for agent update."""
    if not import_file:
        return None, name, instruction, tools, agents, timeout

    import_data = load_resource_from_file(Path(import_file), "agent")
    import_data = convert_export_to_import_format(import_data)
    import_data = normalize_agent_config_for_import(import_data, None)

    cli_args = {
        "name": name,
        "instruction": instruction,
        "tools": tools or (),
        "agents": agents or (),
        "timeout": timeout,
    }

    merged_data = merge_import_with_cli_args(import_data, cli_args)

    return (
        merged_data,
        merged_data.get("name"),
        merged_data.get("instruction"),
        tuple(merged_data.get("tools", ())),
        tuple(merged_data.get("agents", ())),
        coerce_timeout(merged_data.get("timeout")),
    )


def _build_update_data(name, instruction, tools, agents, timeout):
    """Build the update data dictionary from provided parameters."""
    update_data = {}
    if name is not None:
        update_data["name"] = name
    if instruction is not None:
        update_data["instruction"] = instruction
    if tools:
        update_data["tools"] = list(tools)
    if agents:
        update_data["agents"] = list(agents)
    if timeout is not None:
        update_data["timeout"] = timeout
    return update_data


def _handle_update_import_config(import_file, merged_data, update_data):
    """Handle agent config and additional attributes for import-based updates."""
    if not import_file:
        return

    lm_selection, should_strip_lm_identity = resolve_language_model_selection(
        merged_data, None
    )
    update_data.update(lm_selection)

    raw_cfg = merged_data.get("agent_config") if isinstance(merged_data, dict) else None
    if isinstance(raw_cfg, dict):
        update_data["agent_config"] = sanitize_agent_config(
            raw_cfg, strip_lm_identity=should_strip_lm_identity
        )

    excluded_fields = {
        "name",
        "instruction",
        "tools",
        "agents",
        "timeout",
        "agent_config",
        "language_model_id",
        "id",
        "created_at",
        "updated_at",
        "type",
        "framework",
        "version",
        "tool_configs",
        "mcps",
        "a2a_profile",
    }
    for key, value in merged_data.items():
        if key not in excluded_fields and value is not None:
            update_data[key] = value


@agents_group.command()
@click.argument("agent_id")
@click.option("--name", help="New agent name")
@click.option("--instruction", help="New instruction")
@click.option("--tools", multiple=True, help="New tool names or IDs")
@click.option("--agents", multiple=True, help="New sub-agent names")
@click.option("--timeout", type=int, help="New timeout value")
@click.option(
    "--import",
    "import_file",
    type=click.Path(exists=True, dir_okay=False),
    help="Import agent configuration from JSON file",
)
@output_flags()
@click.pass_context
def update(ctx, agent_id, name, instruction, tools, agents, timeout, import_file):
    """Update an existing agent.

    Examples:
        aip agents update my-agent --instruction "New instruction"
        aip agents update my-agent --import agent.json
    """
    try:
        client = get_client(ctx)
        agent = _get_agent_for_update(client, agent_id)

        # Handle import file processing
        merged_data, name, instruction, tools, agents, timeout = (
            _handle_update_import_file(
                import_file, name, instruction, tools, agents, timeout
            )
        )

        update_data = _build_update_data(name, instruction, tools, agents, timeout)

        if merged_data:
            _handle_update_import_config(import_file, merged_data, update_data)

        if not update_data:
            raise click.ClickException("No update fields specified")

        updated_agent = client.agents.update_agent(agent.id, **update_data)

        handle_json_output(ctx, updated_agent.model_dump())
        handle_rich_output(ctx, display_update_success("Agent", updated_agent.name))
        handle_rich_output(ctx, display_agent_run_suggestions(updated_agent))

    except click.ClickException:
        # Handle JSON output for ClickExceptions if view is JSON
        if ctx.obj.get("view") == "json":
            handle_json_output(ctx, error=Exception(AGENT_NOT_FOUND_ERROR))
        # Re-raise ClickExceptions without additional processing
        raise
    except Exception as e:
        handle_json_output(ctx, error=e)
        if ctx.obj.get("view") != "json":
            print_api_error(e)
        raise click.ClickException(str(e))


@agents_group.command()
@click.argument("agent_id")
@click.option("-y", "--yes", is_flag=True, help="Skip confirmation")
@output_flags()
@click.pass_context
def delete(ctx, agent_id, yes):
    """Delete an agent."""
    try:
        client = get_client(ctx)

        # Get agent by ID (no ambiguity handling needed)
        try:
            agent = client.agents.get_agent_by_id(agent_id)
        except Exception as e:
            raise click.ClickException(f"Agent with ID '{agent_id}' not found: {e}")

        # Confirm deletion when not forced
        if not yes and not display_confirmation_prompt("Agent", agent.name):
            return

        client.agents.delete_agent(agent.id)

        handle_json_output(
            ctx,
            {
                "success": True,
                "message": f"Agent '{agent.name}' deleted",
            },
        )
        handle_rich_output(ctx, display_deletion_success("Agent", agent.name))

    except click.ClickException:
        # Handle JSON output for ClickExceptions if view is JSON
        if ctx.obj.get("view") == "json":
            handle_json_output(ctx, error=Exception(AGENT_NOT_FOUND_ERROR))
        # Re-raise ClickExceptions without additional processing
        raise
    except Exception as e:
        handle_json_output(ctx, error=e)
        if ctx.obj.get("view") != "json":
            print_api_error(e)
        raise click.ClickException(str(e))


@agents_group.command()
@click.option(
    "--base-url",
    help="Custom LangFlow server base URL (overrides LANGFLOW_BASE_URL env var)",
)
@click.option(
    "--api-key", help="Custom LangFlow API key (overrides LANGFLOW_API_KEY env var)"
)
@output_flags()
@click.pass_context
def sync_langflow(ctx, base_url, api_key):  # pragma: no cover - integration-only path
    """Sync agents with LangFlow server flows.

    This command fetches all flows from the configured LangFlow server and
    creates/updates corresponding agents in the platform.

    The LangFlow server configuration can be provided via:
    - Command options (--base-url, --api-key)
    - Environment variables (LANGFLOW_BASE_URL, LANGFLOW_API_KEY)

    Examples:
        aip agents sync-langflow
        aip agents sync-langflow --base-url https://my-langflow.com --api-key my-key
    """
    try:
        client = get_client(ctx)

        # Perform the sync
        result = client.sync_langflow_agents(base_url=base_url, api_key=api_key)

        # Handle output format
        handle_json_output(ctx, result)

        # Show success message for non-JSON output
        if ctx.obj.get("view") != "json":
            from rich.text import Text

            # Extract some useful info from the result
            success_count = result.get("data", {}).get("created_count", 0) + result.get(
                "data", {}
            ).get("updated_count", 0)
            total_count = result.get("data", {}).get("total_processed", 0)

            handle_rich_output(
                ctx,
                Text(
                    f"[green]✅ Successfully synced {success_count} LangFlow agents ({total_count} total processed)[/green]"
                ),
            )

    except Exception as e:
        handle_json_output(ctx, error=e)
        if ctx.obj.get("view") != "json":
            print_api_error(e)
        raise click.ClickException(str(e))
