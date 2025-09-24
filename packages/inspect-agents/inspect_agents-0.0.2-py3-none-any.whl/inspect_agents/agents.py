from __future__ import annotations

# ruff: noqa: E402
"""Supervisor agent (Inspect ReAct) for Inspect Agents.

Provides `build_supervisor()` which returns an Inspect `react` agent configured
with a base prompt and built-in tools (todos + virtual FS). The agent terminates
via the default `submit()` tool provided by Inspect.
"""

from collections.abc import Sequence
from typing import Any, NotRequired, TypedDict

from .observability import log_agent_defaults_event
from .settings import resolve_include_defaults

# Base prompt modeled for legacy compatibility (deepagents-style base_prompt);
# see migration.py and docs/design/deepagents_implementation_prompts.md.
BASE_PROMPT_HEADER = "You have access to a number of tools.\n\n"

BASE_PROMPT_TODOS = (
    "## Todo & Filesystem Tools\n\n"
    "- `write_todos`: Update and track your plan frequently.\n"
    "- `ls`, `read_file`, `write_file`, `edit_file`: Operate on a virtual in‑memory FS by default.\n"
    "  In sandbox mode, these map to a safe host text editor.\n\n"
    "Mark todos complete as soon as a task is finished (don’t batch).\n"
)

# Backcompat constant for migration shim
BASE_PROMPT = BASE_PROMPT_HEADER + BASE_PROMPT_TODOS


def _format_standard_tools_section(all_tools: list[object]) -> str:
    """Return a short section enumerating available Inspect standard tools.

    Groups standard tools separately so the model understands additional
    capabilities beyond the Todo/FS utilities.
    """
    try:
        from inspect_ai.tool._tool_def import ToolDef
    except Exception:
        # If ToolDef is unavailable (e.g., in stubs), skip annotation
        return ""

    names = set()
    for t in all_tools:
        try:
            tdef = ToolDef(t) if not isinstance(t, ToolDef) else t
            names.add(tdef.name)
        except Exception:
            pass

    std_names: list[str] = []
    # Detect presence of representative tools
    if "think" in names:
        std_names.append("think")
    if "web_search" in names:
        std_names.append("web_search")
    if "bash" in names:
        std_names.append("bash")
    if "python" in names:
        std_names.append("python")
    # Web browser exposes multiple tool names; detect by go
    browser_present = any(n.startswith("web_browser_") for n in names)
    if browser_present:
        std_names.append("web_browser")
    if "text_editor" in names:
        std_names.append("text_editor")

    if not std_names:
        return ""

    std_list = ", ".join(std_names)
    return (
        "\n## Standard Tools\n\n"
        f"Additional standard tools are enabled: {std_list}.\n"
        "Use `web_search` to retrieve up‑to‑date information from the web when needed."
        " Prefer citing sources in your answer.\n"
    )


def _built_in_tools():
    # Local import to avoid importing inspect_ai at module import time
    from inspect_agents.tools import full_safe_preset

    # Mirrors full_safe_preset() so defaults stay in sync with curated presets
    return full_safe_preset()


def build_supervisor(
    prompt: str,
    tools: Sequence[object] | None = None,
    *,
    include_defaults: bool | None = None,
    attempts: int = 1,
    model: object | None = None,
    truncation: str = "disabled",
):
    """Create a top-level ReAct supervisor agent.

    Args:
        prompt: Base instructions to prepend before standard guidance.
        tools: Additional Tools/ToolDefs/ToolSources to provide. Pass the result of
            ``inspect_agents.tools.minimal_fs_preset()`` or ``full_safe_preset()``
            when you disable defaults but still want curated bundles.
        include_defaults: When None (default), fall back to the environment
            toggle `INSPECT_AGENTS_INCLUDE_DEFAULT_TOOLS` (defaults to True when
            unset). When True, prepend the built-in Todo/FS tools and mention
            them in the prompt. When False, skip automatic injection so custom
            deployments can supply their own toolchain without prompt drift.
        attempts: Max attempts for submit-terminated loop.
        model: Optional Inspect model (string/Model/Agent). If None, uses default.
        truncation: Overflow policy for long conversations ("disabled" or "auto").

    Returns:
        Inspect `Agent` compatible with react() (submit-enabled).
    """
    from inspect_ai.agent._react import react

    # Compose prompt with clear tool sections (Todo/FS + Standard)
    resolved_include_defaults, include_source, env_raw = resolve_include_defaults(include_defaults)

    extra_tools = list(tools or [])
    builtins = _built_in_tools() if resolved_include_defaults else []
    tools = builtins + extra_tools

    log_agent_defaults_event(
        builder="supervisor",
        include_defaults=resolved_include_defaults,
        caller_supplied_tool_count=len(extra_tools),
        feature_flag_state=env_raw,
        include_defaults_source=include_source,
        extra={"active_tool_count": len(tools)},
    )

    tail_chunks = [BASE_PROMPT_HEADER]
    if resolved_include_defaults:
        tail_chunks.append(BASE_PROMPT_TODOS)
    std_section = _format_standard_tools_section(tools)
    if std_section:
        tail_chunks.append(std_section)
    tail = "".join(tail_chunks)

    prefix = (prompt or "").rstrip()
    full_prompt = tail if not prefix else f"{prefix}\n\n{tail}"

    return react(
        prompt=full_prompt,
        tools=tools,
        model=model,
        attempts=attempts,
        submit=True,
        truncation=truncation,  # pass-through; no custom limits for now
    )


def build_basic_submit_agent(
    *,
    prompt: str,
    tools: Sequence[object] | None = None,
    include_defaults: bool | None = None,
    attempts: int = 1,
    model: object | None = None,
    truncation: str = "disabled",
):
    """Alias for the basic submit-style supervisor for naming parity.

    Mirrors `build_supervisor`; exported to make imports clearer alongside
    `build_iterative_agent` when contrasting agent styles in docs/examples.
    """
    return build_supervisor(
        prompt=prompt,
        tools=tools,
        include_defaults=include_defaults,
        attempts=attempts,
        model=model,
        truncation=truncation,
    )


def build_iterative_agent(
    *,
    prompt: str | None = None,
    tools: Sequence[object] | None = None,
    code_only: bool = False,
    include_defaults: bool | None = None,
    model: Any | None = None,
    real_time_limit_sec: int | None = None,
    max_steps: int | None = None,
    max_messages: int | None = None,
    continue_message: str | None = None,
    max_turns: int = 50,
    progress_every: int = 5,
    stop_on_keywords: Sequence[str] | None = None,
    max_tool_output_bytes: int | None = None,
):
    """Thin passthrough to the iterative supervisor (no submit semantics).

    Exposed here for a consistent surface alongside `build_supervisor()`. When
    opting out of defaults via ``include_defaults=False``, reuse
    ``inspect_agents.tools.minimal_fs_preset()`` or ``full_safe_preset()`` to
    assemble sanctioned tool bundles without reimplementing policy checks.
    See `inspect_agents.iterative.build_iterative_agent` for parameter docs.
    """
    # Import locally to avoid heavy imports at module load
    from inspect_agents.iterative import build_iterative_agent as _impl

    return _impl(
        prompt=prompt,
        tools=tools,
        code_only=code_only,
        include_defaults=include_defaults,
        model=model,
        real_time_limit_sec=real_time_limit_sec,
        max_steps=max_steps,
        max_messages=max_messages,
        continue_message=continue_message,
        max_turns=max_turns,
        progress_every=progress_every,
        stop_on_keywords=stop_on_keywords,
        max_tool_output_bytes=max_tool_output_bytes,
    )


class SubAgentCfg(TypedDict):
    name: str
    description: str
    prompt: str
    tools: NotRequired[list[str]]
    model: NotRequired[Any]
    mode: NotRequired[str]  # "handoff" (default) or "tool"
    input_filter: NotRequired[Any]
    output_filter: NotRequired[Any]
    limits: NotRequired[list[Any]]


def build_subagents(
    configs: list[SubAgentCfg], base_tools: list[object], *, default_model: object | None = None
) -> list[object]:
    """Create handoff/as_tool wrappers for configured sub-agents.

    - Each config produces an Inspect agent via `react(...)` with the provided
      prompt, description, and tools (subset of `base_tools` if `tools` is set).
    - Returns tools named `transfer_to_<name>` (handoff) or the agent as a
      single-shot tool when `mode == 'tool'`.
    """
    from inspect_ai.agent._as_tool import as_tool
    from inspect_ai.agent._handoff import handoff
    from inspect_ai.agent._react import react

    # Default quarantine filters and env toggles
    from inspect_agents.filters import (
        default_input_filter,
        default_output_filter,
    )

    # Map base tools by name for per-agent selection
    tool_by_name: dict[str, object] = {}
    try:
        from inspect_ai.tool._tool_def import ToolDef

        for t in base_tools:
            tdef = ToolDef(t) if not isinstance(t, ToolDef) else t
            tool_by_name[tdef.name] = t
    except Exception:
        # Fallback best-effort by object repr if ToolDef unavailable
        for t in base_tools:
            tool_by_name[getattr(t, "__name__", repr(t))] = t

    out: list[object] = []
    for cfg in configs:
        name = cfg["name"]
        desc = cfg["description"]
        prompt = cfg["prompt"]
        mode = cfg.get("mode", "handoff")

        # Resolve tools subset in config (by name) or use all base_tools
        selected_tools: list[object]
        if "tools" in cfg:
            selected_tools = [tool_by_name[n] for n in cfg["tools"] if n in tool_by_name]
        else:
            selected_tools = list(base_tools)

        # Build the sub-agent
        agent = react(
            name=name,
            description=desc,
            prompt=prompt,
            tools=selected_tools,
            model=(cfg.get("model") if "model" in cfg else default_model),
            submit=True,
        )

        # Wrap as requested
        if mode == "tool":
            out.append(as_tool(agent, description=desc))
        else:
            # Resolve filters: per-config wins; otherwise use context-aware defaults
            # Input filter cascades the parent filter by default, unless per-agent
            # env override is present. Pass the sub-agent name to support scoped envs.
            input_filter = cfg.get("input_filter") if "input_filter" in cfg else default_input_filter(name)
            output_filter = cfg.get("output_filter") if "output_filter" in cfg else default_output_filter()

            # Per-agent env overrides for handoff limits (time/messages/tokens)
            # Precedence: explicit config (non-empty) > env
            try:
                from inspect_agents.config import env_limits_for_agent  # local import to avoid cycle

                env_limits = env_limits_for_agent(name)
            except Exception:
                env_limits = []

            limits_arg = cfg.get("limits") or env_limits

            out.append(
                handoff(
                    agent,
                    description=desc,
                    input_filter=input_filter,
                    output_filter=output_filter,
                    tool_name=f"transfer_to_{name}",
                    limits=limits_arg,
                )
            )

    return out
