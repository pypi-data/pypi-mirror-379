"""Base renderer class that orchestrates all rendering components.

Authors:
    Raymond Christopher (raymond.christopher@gdplabs.id)
"""

from __future__ import annotations

import json
import logging
from dataclasses import dataclass
from time import monotonic
from typing import Any

from rich.console import Console as RichConsole
from rich.console import Group
from rich.live import Live
from rich.markdown import Markdown
from rich.text import Text

from glaip_sdk.rich_components import AIPPanel
from glaip_sdk.utils.rendering.formatting import (
    format_main_title,
    get_spinner_char,
    is_step_finished,
)
from glaip_sdk.utils.rendering.models import RunStats
from glaip_sdk.utils.rendering.renderer.config import RendererConfig
from glaip_sdk.utils.rendering.renderer.debug import render_debug_event
from glaip_sdk.utils.rendering.renderer.panels import (
    create_final_panel,
    create_main_panel,
    create_tool_panel,
)
from glaip_sdk.utils.rendering.renderer.progress import (
    format_elapsed_time,
    format_tool_title,
    format_working_indicator,
    get_spinner,
    is_delegation_tool,
)
from glaip_sdk.utils.rendering.renderer.stream import StreamProcessor
from glaip_sdk.utils.rendering.steps import StepManager

# Configure logger
logger = logging.getLogger("glaip_sdk.run_renderer")


@dataclass
class RendererState:
    """Internal state for the renderer."""

    buffer: list[str] = None
    final_text: str = ""
    streaming_started_at: float | None = None
    printed_final_panel: bool = False
    finalizing_ui: bool = False

    def __post_init__(self):
        if self.buffer is None:
            self.buffer = []


class RichStreamRenderer:
    """Live, modern terminal renderer for agent execution with rich visual output."""

    def __init__(
        self,
        console=None,
        *,
        cfg: RendererConfig | None = None,
        verbose: bool = False,
    ):
        """Initialize the renderer.

        Args:
            console: Rich console instance
            cfg: Renderer configuration
            verbose: Whether to enable verbose mode
        """
        self.console = console or RichConsole()
        self.cfg = cfg or RendererConfig()
        self.verbose = verbose

        # Initialize components
        self.stream_processor = StreamProcessor()
        self.state = RendererState()

        # Initialize step manager and other state
        self.steps = StepManager()
        # Live display instance (single source of truth)
        self.live: Live | None = None

        # Context and tool tracking
        self.context_order: list[str] = []
        self.context_parent: dict[str, str] = {}
        self.tool_order: list[str] = []
        self.context_panels: dict[str, list[str]] = {}
        self.context_meta: dict[str, dict[str, Any]] = {}
        self.tool_panels: dict[str, dict[str, Any]] = {}

        # Timing
        self._started_at: float | None = None

        # Header/text
        self.header_text: str = ""
        # Track per-step server start times for accurate elapsed labels
        self._step_server_start_times: dict[str, float] = {}

    def on_start(self, meta: dict[str, Any]):
        """Handle renderer start event."""
        if self.cfg.live:
            # Defer creating Live to _ensure_live so tests and prod both work
            pass

        # Set up initial state
        self._started_at = monotonic()
        self.stream_processor.streaming_started_at = self._started_at

        # Print compact header and user request (parity with old renderer)
        try:
            parts: list[str] = ["🤖"]
            agent_name = meta.get("agent_name", "agent")
            if agent_name:
                parts.append(agent_name)
            model = meta.get("model", "")
            if model:
                parts.extend(["•", model])
            run_id = meta.get("run_id", "")
            if run_id:
                parts.extend(["•", run_id])
            self.header_text = " ".join(parts)
            if self.header_text:
                try:
                    # Use a rule-like header for readability
                    self.console.rule(self.header_text)
                except Exception:
                    self.console.print(self.header_text)

            query = (
                meta.get("input_message") or meta.get("query") or meta.get("message")
            )
            if query:
                self.console.print(
                    AIPPanel(
                        Markdown(f"**Query:** {query}"),
                        title="User Request",
                        border_style="yellow",
                        padding=(0, 1),
                    )
                )
        except Exception:
            # Non-fatal: header is nice-to-have
            pass

    def on_event(self, ev: dict[str, Any]) -> None:
        """Handle streaming events from the backend."""
        # Reset event tracking
        self.stream_processor.reset_event_tracking()

        # Track streaming start time
        if self.state.streaming_started_at is None:
            self.state.streaming_started_at = monotonic()

        # Extract event metadata
        metadata = self.stream_processor.extract_event_metadata(ev)
        kind = metadata["kind"]
        context_id = metadata["context_id"]
        content = metadata["content"]

        # Render debug event panel if verbose mode is enabled
        if self.verbose:
            render_debug_event(ev, self.console, self.state.streaming_started_at)

        # Update timing
        self.stream_processor.update_timing(context_id)

        # Handle different event types
        if kind == "status":
            # Status events
            status = ev.get("status")
            if status == "streaming_started":
                self.state.streaming_started_at = monotonic()
            return

        elif kind == "content":
            # Content streaming events
            if content:
                self.state.buffer.append(content)
                self._ensure_live()
            return

        elif kind == "final_response":
            # Final response events
            if content:
                self.state.buffer.append(content)
                self.state.final_text = content
                self._ensure_live()

                # In verbose mode, show the final result in a panel
                if self.verbose and content and content.strip():
                    final_panel = create_final_panel(content, theme=self.cfg.theme)
                    self.console.print(final_panel)
                    self.state.printed_final_panel = True
            return

        elif kind in {"agent_step", "agent_thinking_step"}:
            # Agent step events
            # Note: Thinking gaps are primarily a visual aid. Keep minimal here.

            # Extract tool information
            tool_name, tool_args, tool_out, tool_calls_info = (
                self.stream_processor.parse_tool_calls(ev)
            )

            # Track tools and sub-agents
            self.stream_processor.track_tools_and_agents(
                tool_name, tool_calls_info, is_delegation_tool
            )

            # Handle tool execution
            self._handle_agent_step(ev, tool_name, tool_args, tool_out, tool_calls_info)

        # Update live display
        self._ensure_live()

    def on_complete(self, _stats: RunStats):
        """Handle completion event."""
        self.state.finalizing_ui = True

        # Mark any running steps as finished to avoid lingering spinners
        try:
            for st in list(self.steps.by_id.values()):
                if not is_step_finished(st):
                    st.finish(None)
        except Exception:
            pass

        # Mark unfinished tool panels as finished
        try:
            for _sid, meta in list(self.tool_panels.items()):
                if meta.get("status") != "finished":
                    meta["status"] = "finished"
        except Exception:
            pass

        # Final refresh
        self._ensure_live()

        # Stop live display
        if self.live:
            self.live.stop()
            self.live = None

        # If no explicit final_response was printed, but we have buffered content,
        # print a final result panel so users still see the outcome (especially in --verbose).
        try:
            if self.verbose and not self.state.printed_final_panel:
                body = ("".join(self.state.buffer) or "").strip()
                if body:
                    final_panel = create_final_panel(body, theme=self.cfg.theme)
                    self.console.print(final_panel)
                    self.state.printed_final_panel = True
        except Exception:
            # Non-fatal; renderer best-effort
            pass

    def _ensure_live(self):
        """Ensure live display is updated."""
        # Lazily create Live if needed
        if self.live is None and self.cfg.live:
            try:
                self.live = Live(
                    console=self.console,
                    refresh_per_second=1 / self.cfg.refresh_debounce,
                    transient=not self.cfg.persist_live,
                )
                self.live.start()
            except Exception:
                self.live = None

        if self.live:
            panels = [self._render_main_panel()]
            steps_renderable = self._render_steps_text()
            panels.append(
                AIPPanel(
                    steps_renderable,
                    title="Steps",
                    border_style="blue",
                )
            )
            panels.extend(self._render_tool_panels())
            self.live.update(Group(*panels))

    def _render_main_panel(self):
        """Render the main content panel."""
        body = "".join(self.state.buffer).strip()
        # Dynamic title with spinner + elapsed/hints
        title = self._format_enhanced_main_title()
        return create_main_panel(body, title, self.cfg.theme)

    def _maybe_insert_thinking_gap(self, task_id: str | None, context_id: str | None):
        """Insert thinking gap if needed."""
        # Implementation would track thinking states
        pass

    def _ensure_tool_panel(
        self, name: str, args: Any, task_id: str, context_id: str
    ) -> str:
        """Ensure a tool panel exists and return its ID."""
        formatted_title = format_tool_title(name)
        is_delegation = is_delegation_tool(name)
        tool_sid = f"tool_{name}_{task_id}_{context_id}"

        if tool_sid not in self.tool_panels:
            self.tool_panels[tool_sid] = {
                "title": formatted_title,
                "status": "running",
                "started_at": monotonic(),
                "server_started_at": self.stream_processor.server_elapsed_time,
                "chunks": [],
                "args": args or {},
                "output": None,
                "is_delegation": is_delegation,
            }
            # Add Args section once
            if args:
                try:
                    args_content = (
                        "**Args:**\n```json\n"
                        + json.dumps(args, indent=2)
                        + "\n```\n\n"
                    )
                except Exception:
                    args_content = f"**Args:**\n{args}\n\n"
                self.tool_panels[tool_sid]["chunks"].append(args_content)
            self.tool_order.append(tool_sid)

        return tool_sid

    def _start_tool_step(
        self,
        task_id: str,
        context_id: str,
        tool_name: str,
        tool_args: Any,
        _tool_sid: str,
    ):
        """Start or get a step for a tool."""
        if is_delegation_tool(tool_name):
            st = self.steps.start_or_get(
                task_id=task_id,
                context_id=context_id,
                kind="delegate",
                name=tool_name,
                args=tool_args,
            )
        else:
            st = self.steps.start_or_get(
                task_id=task_id,
                context_id=context_id,
                kind="tool",
                name=tool_name,
                args=tool_args,
            )

        # Record server start time for this step if available
        if st and self.stream_processor.server_elapsed_time is not None:
            self._step_server_start_times[st.step_id] = (
                self.stream_processor.server_elapsed_time
            )

        return st

    def _process_additional_tool_calls(
        self, tool_calls_info: list, tool_name: str, task_id: str, context_id: str
    ):
        """Process additional tool calls to avoid duplicates."""
        for call_name, call_args, _ in tool_calls_info or []:
            if call_name and call_name != tool_name:
                self._ensure_tool_panel(call_name, call_args, task_id, context_id)
                if is_delegation_tool(call_name):
                    st2 = self.steps.start_or_get(
                        task_id=task_id,
                        context_id=context_id,
                        kind="delegate",
                        name=call_name,
                        args=call_args,
                    )
                else:
                    st2 = self.steps.start_or_get(
                        task_id=task_id,
                        context_id=context_id,
                        kind="tool",
                        name=call_name,
                        args=call_args,
                    )
                if self.stream_processor.server_elapsed_time is not None and st2:
                    self._step_server_start_times[st2.step_id] = (
                        self.stream_processor.server_elapsed_time
                    )

    def _detect_tool_completion(
        self, metadata: dict, content: str
    ) -> tuple[bool, str | None, Any]:
        """Detect if a tool has completed and return completion info."""
        tool_info = metadata.get("tool_info", {}) if isinstance(metadata, dict) else {}

        if tool_info.get("status") == "finished" and tool_info.get("name"):
            return True, tool_info.get("name"), tool_info.get("output")
        elif content and isinstance(content, str) and content.startswith("Completed "):
            # content like "Completed google_serper"
            tname = content.replace("Completed ", "").strip()
            if tname:
                output = (
                    tool_info.get("output") if tool_info.get("name") == tname else None
                )
                return True, tname, output
        elif metadata.get("status") == "finished" and tool_info.get("name"):
            return True, tool_info.get("name"), tool_info.get("output")

        return False, None, None

    def _finish_tool_panel(
        self,
        finished_tool_name: str,
        finished_tool_output: Any,
        task_id: str,
        context_id: str,
    ):
        """Finish a tool panel and update its status."""
        tool_sid = f"tool_{finished_tool_name}_{task_id}_{context_id}"
        if tool_sid in self.tool_panels:
            meta = self.tool_panels[tool_sid]
            prev_status = meta.get("status")

            if prev_status != "finished":
                meta["status"] = "finished"

                # Compute and store duration
                try:
                    server_now = self.stream_processor.server_elapsed_time
                    server_start = meta.get("server_started_at")
                    dur = None

                    if isinstance(server_now, int | float) and isinstance(
                        server_start, int | float
                    ):
                        dur = max(0.0, float(server_now) - float(server_start))
                    elif meta.get("started_at") is not None:
                        dur = max(0.0, float(monotonic() - meta.get("started_at")))

                    if dur is not None:
                        meta["duration_seconds"] = dur
                        meta["server_finished_at"] = (
                            server_now if isinstance(server_now, int | float) else None
                        )
                        meta["finished_at"] = monotonic()
                except Exception:
                    pass

                # Add output to panel
                if finished_tool_output is not None:
                    meta["chunks"].append(
                        self._format_output_block(
                            finished_tool_output, finished_tool_name
                        )
                    )
                    meta["output"] = finished_tool_output

            # Ensure this finished panel is visible in this frame
            self.stream_processor.current_event_finished_panels.add(tool_sid)

    def _finish_tool_step(
        self,
        finished_tool_name: str,
        finished_tool_output: Any,
        task_id: str,
        context_id: str,
    ):
        """Finish the corresponding step for a completed tool."""
        tool_sid = f"tool_{finished_tool_name}_{task_id}_{context_id}"
        step_duration = None

        try:
            step_duration = self.tool_panels.get(tool_sid, {}).get("duration_seconds")
        except Exception:
            step_duration = None

        if is_delegation_tool(finished_tool_name):
            self.steps.finish(
                task_id=task_id,
                context_id=context_id,
                kind="delegate",
                name=finished_tool_name,
                output=finished_tool_output,
                duration_raw=step_duration,
            )
        else:
            self.steps.finish(
                task_id=task_id,
                context_id=context_id,
                kind="tool",
                name=finished_tool_name,
                output=finished_tool_output,
                duration_raw=step_duration,
            )

    def _create_tool_snapshot(
        self, finished_tool_name: str, task_id: str, context_id: str
    ):
        """Create and print a snapshot for a finished tool."""
        tool_sid = f"tool_{finished_tool_name}_{task_id}_{context_id}"

        try:
            if not (
                self.cfg.append_finished_snapshots
                and not self.tool_panels.get(tool_sid, {}).get("snapshot_printed")
            ):
                return

            meta = self.tool_panels[tool_sid]
            adjusted_title = meta.get("title") or finished_tool_name

            # Add elapsed time to title
            dur = meta.get("duration_seconds")
            if isinstance(dur, int | float):
                elapsed_str = (
                    f"{dur:.2f}s"
                    if dur >= 1
                    else (f"{int(dur * 1000)}ms" if int(dur * 1000) > 0 else "<1ms")
                )
                adjusted_title = f"{adjusted_title}  · {elapsed_str}"

            # Compose body from chunks and clamp
            body_text = "".join(meta.get("chunks") or [])
            max_lines = int(self.cfg.snapshot_max_lines or 0) or 60
            lines = body_text.splitlines()
            if len(lines) > max_lines:
                lines = lines[:max_lines] + ["… (truncated)"]
            body_text = "\n".join(lines)

            max_chars = int(self.cfg.snapshot_max_chars or 0) or 4000
            if len(body_text) > max_chars:
                body_text = body_text[: max_chars - 12] + "\n… (truncated)"

            snapshot_panel = create_tool_panel(
                title=adjusted_title,
                content=body_text or "(no output)",
                status="finished",
                theme=self.cfg.theme,
                is_delegation=is_delegation_tool(finished_tool_name),
            )

            # Print as a snapshot entry
            self.console.print(snapshot_panel)
            # Guard so we don't print snapshot twice
            self.tool_panels[tool_sid]["snapshot_printed"] = True

        except Exception:
            pass

    def _handle_agent_step(
        self,
        event: dict[str, Any],
        tool_name: str | None,
        tool_args: Any,
        _tool_out: Any,
        tool_calls_info: list,
    ):
        """Handle agent step event."""
        metadata = event.get("metadata", {})
        task_id = event.get("task_id")
        context_id = event.get("context_id")
        content = event.get("content", "")

        # Create steps and panels for the primary tool
        if tool_name:
            tool_sid = self._ensure_tool_panel(
                tool_name, tool_args, task_id, context_id
            )
            self._start_tool_step(task_id, context_id, tool_name, tool_args, tool_sid)

        # Handle additional tool calls
        self._process_additional_tool_calls(
            tool_calls_info, tool_name, task_id, context_id
        )

        # Check for tool completion
        is_tool_finished, finished_tool_name, finished_tool_output = (
            self._detect_tool_completion(metadata, content)
        )

        if is_tool_finished and finished_tool_name:
            self._finish_tool_panel(
                finished_tool_name, finished_tool_output, task_id, context_id
            )
            self._finish_tool_step(
                finished_tool_name, finished_tool_output, task_id, context_id
            )
            self._create_tool_snapshot(finished_tool_name, task_id, context_id)

    def _spinner(self) -> str:
        """Return spinner character."""
        return get_spinner()

    def _format_working_indicator(self, started_at: float | None) -> str:
        """Format working indicator."""
        return format_working_indicator(
            started_at,
            self.stream_processor.server_elapsed_time,
            self.state.streaming_started_at,
        )

    def close(self) -> None:
        """Gracefully stop any live rendering and release resources."""
        try:
            if self.live:
                try:
                    self.live.stop()
                finally:
                    self.live = None
        except Exception:
            pass

    def __del__(self):
        try:
            if self.live:
                self.live.stop()
        except Exception:
            pass

    def _get_analysis_progress_info(self) -> dict[str, Any]:
        total_steps = len(self.steps.order)
        completed_steps = sum(
            1 for sid in self.steps.order if is_step_finished(self.steps.by_id[sid])
        )
        current_step = None
        for sid in self.steps.order:
            if not is_step_finished(self.steps.by_id[sid]):
                current_step = sid
                break
        # Prefer server elapsed time when available
        elapsed = 0.0
        if isinstance(self.stream_processor.server_elapsed_time, int | float):
            try:
                elapsed = float(self.stream_processor.server_elapsed_time)
            except Exception:
                elapsed = 0.0
        elif self._started_at is not None:
            try:
                elapsed = monotonic() - self._started_at
            except Exception:
                elapsed = 0.0
        progress_percent = (
            int((completed_steps / total_steps) * 100) if total_steps else 0
        )
        return {
            "total_steps": total_steps,
            "completed_steps": completed_steps,
            "current_step": current_step,
            "progress_percent": progress_percent,
            "elapsed_time": elapsed,
            "has_running_steps": self._has_running_steps(),
        }

    def _format_enhanced_main_title(self) -> str:
        base = format_main_title(
            header_text=self.header_text,
            has_running_steps=self._has_running_steps(),
            get_spinner_char=get_spinner_char,
        )
        # Add elapsed time and subtle progress hints for long operations
        info = self._get_analysis_progress_info()
        elapsed = info.get("elapsed_time", 0.0)
        if elapsed and elapsed > 0:
            base += f" · {format_elapsed_time(elapsed)}"
        if info.get("total_steps", 0) > 1 and info.get("has_running_steps"):
            if elapsed > 60:
                base += " 🐌"
            elif elapsed > 30:
                base += " ⚠️"
        return base

    # Modern interface only — no legacy helper shims below

    def _refresh(self, _force: bool | None = None) -> None:
        # In the modular renderer, refreshing simply updates the live group
        self._ensure_live()

    def _has_running_steps(self) -> bool:
        """Check if any steps are still running."""
        for _sid, st in self.steps.by_id.items():
            if not is_step_finished(st):
                return True
        return False

    def _get_step_icon(self, step_kind: str) -> str:
        """Get icon for step kind."""
        if step_kind == "tool":
            return "⚙️"
        elif step_kind == "delegate":
            return "🤝"
        elif step_kind == "agent":
            return "🧠"
        return ""

    def _format_step_status(self, step) -> str:
        """Format step status with elapsed time or duration."""
        if is_step_finished(step):
            if step.duration_ms is None:
                return "[<1ms]"
            elif step.duration_ms >= 1000:
                return f"[{step.duration_ms/1000:.2f}s]"
            elif step.duration_ms > 0:
                return f"[{step.duration_ms}ms]"
            return "[<1ms]"
        else:
            # Calculate elapsed time for running steps
            elapsed = self._calculate_step_elapsed_time(step)
            if elapsed >= 1:
                return f"[{elapsed:.2f}s]"
            ms = int(elapsed * 1000)
            return f"[{ms}ms]" if ms > 0 else "[<1ms]"

    def _calculate_step_elapsed_time(self, step) -> float:
        """Calculate elapsed time for a running step."""
        server_elapsed = self.stream_processor.server_elapsed_time
        server_start = self._step_server_start_times.get(step.step_id)

        if isinstance(server_elapsed, int | float) and isinstance(
            server_start, int | float
        ):
            return max(0.0, float(server_elapsed) - float(server_start))

        try:
            return max(0.0, float(monotonic() - step.started_at))
        except Exception:
            return 0.0

    def _get_step_display_name(self, step) -> str:
        """Get display name for a step."""
        if step.name and step.name != "step":
            return step.name
        return "thinking..." if step.kind == "agent" else f"{step.kind} step"

    def _check_parallel_tools(self) -> dict[tuple[str | None, str | None], list]:
        """Check for parallel running tools."""
        running_by_ctx: dict[tuple[str | None, str | None], list] = {}
        for sid in self.steps.order:
            st = self.steps.by_id[sid]
            if st.kind == "tool" and not is_step_finished(st):
                key = (st.task_id, st.context_id)
                running_by_ctx.setdefault(key, []).append(st)
        return running_by_ctx

    def _render_steps_text(self) -> Text:
        """Render the steps panel content."""
        if not (self.steps.order or self.steps.children):
            return Text("No steps yet", style="dim")

        running_by_ctx = self._check_parallel_tools()
        lines: list[str] = []

        for sid in self.steps.order:
            st = self.steps.by_id[sid]
            status_br = self._format_step_status(st)
            display_name = self._get_step_display_name(st)
            tail = " ✓" if is_step_finished(st) else ""

            # Add parallel indicator for running tools
            if st.kind == "tool" and not is_step_finished(st):
                key = (st.task_id, st.context_id)
                if len(running_by_ctx.get(key, [])) > 1:
                    status_br = status_br.replace("]", " 🔄]")

            icon = self._get_step_icon(st.kind)
            lines.append(f"{icon} {display_name} {status_br}{tail}")

        return Text("\n".join(lines), style="dim")

    def _render_tool_panels(self) -> list[AIPPanel]:
        """Render tool execution output panels."""
        panels: list[AIPPanel] = []
        for sid in self.tool_order:
            meta = self.tool_panels.get(sid) or {}
            title = meta.get("title") or "Tool"
            status = meta.get("status") or "running"
            chunks = meta.get("chunks") or []
            is_delegation = bool(meta.get("is_delegation"))

            # Finished panels visibility rules
            if status == "finished":
                if getattr(self.cfg, "append_finished_snapshots", False):
                    # When snapshots are enabled, don't also render finished panels in the live area
                    # (prevents duplicates both mid-run and at the end)
                    continue
                if (
                    not self.state.finalizing_ui
                    and sid not in self.stream_processor.current_event_finished_panels
                ):
                    continue

            body = "".join(chunks)
            adjusted_title = title
            if status == "running":
                # Prefer server-based elapsed from when this tool panel started
                server_elapsed = self.stream_processor.server_elapsed_time
                server_start = meta.get("server_started_at")
                if isinstance(server_elapsed, int | float) and isinstance(
                    server_start, int | float
                ):
                    elapsed = max(0.0, float(server_elapsed) - float(server_start))
                else:
                    try:
                        elapsed = max(
                            0.0, monotonic() - (meta.get("started_at") or 0.0)
                        )
                    except Exception:
                        elapsed = 0.0
                elapsed_str = (
                    f"{elapsed:.2f}s"
                    if elapsed >= 1
                    else (
                        f"{int(elapsed * 1000)}ms"
                        if int(elapsed * 1000) > 0
                        else "<1ms"
                    )
                )
                # Add a small elapsed hint to the title and panel body (standardized)
                adjusted_title = f"{title}  · {elapsed_str}"
                chip = f"⏱ {elapsed_str}"
                if not body:
                    body = chip
                else:
                    body = f"{body}\n\n{chip}"
            elif status == "finished":
                # Use stored duration if present; otherwise try to compute once more
                dur = meta.get("duration_seconds")
                if not isinstance(dur, int | float):
                    try:
                        server_now = self.stream_processor.server_elapsed_time
                        server_start = meta.get("server_started_at")
                        if isinstance(server_now, int | float) and isinstance(
                            server_start, int | float
                        ):
                            dur = max(0.0, float(server_now) - float(server_start))
                        elif meta.get("started_at") is not None:
                            dur = max(0.0, float(monotonic() - meta.get("started_at")))
                    except Exception:
                        dur = None
                if isinstance(dur, int | float):
                    elapsed_str = (
                        f"{dur:.2f}s"
                        if dur >= 1
                        else (f"{int(dur * 1000)}ms" if int(dur * 1000) > 0 else "<1ms")
                    )
                    adjusted_title = f"{title}  · {elapsed_str}"

            panels.append(
                create_tool_panel(
                    title=adjusted_title,
                    content=body or "Processing...",
                    status=status,
                    theme=self.cfg.theme,
                    is_delegation=is_delegation,
                )
            )

        return panels

    def _format_output_block(self, output_value: Any, tool_name: str | None) -> str:
        """Format an output value for panel display."""
        # If dict/list -> pretty JSON
        if isinstance(output_value, dict | list):
            try:
                return (
                    "**Output:**\n```json\n"
                    + json.dumps(output_value, indent=2)
                    + "\n```\n"
                )
            except Exception:
                pass

        if isinstance(output_value, str):
            s = output_value.strip()
            # Clean sub-agent name prefix like "[research_compiler_agent_testing] "
            try:
                if tool_name and is_delegation_tool(tool_name):
                    sub = tool_name
                    if tool_name.startswith("delegate_to_"):
                        sub = tool_name.replace("delegate_to_", "")
                    elif tool_name.startswith("delegate_"):
                        sub = tool_name.replace("delegate_", "")
                    prefix = f"[{sub}]"
                    if s.startswith(prefix):
                        s = s[len(prefix) :].lstrip()
            except Exception:
                pass
            # If looks like JSON, pretty print it
            if (s.startswith("{") and s.endswith("}")) or (
                s.startswith("[") and s.endswith("]")
            ):
                try:
                    parsed = json.loads(s)
                    return (
                        "**Output:**\n```json\n"
                        + json.dumps(parsed, indent=2)
                        + "\n```\n"
                    )
                except Exception:
                    pass
            return "**Output:**\n" + s + "\n"

        try:
            return "**Output:**\n" + json.dumps(output_value, indent=2) + "\n"
        except Exception:
            return "**Output:**\n" + str(output_value) + "\n"

    # No legacy surface helpers are exposed; use modern interfaces only
