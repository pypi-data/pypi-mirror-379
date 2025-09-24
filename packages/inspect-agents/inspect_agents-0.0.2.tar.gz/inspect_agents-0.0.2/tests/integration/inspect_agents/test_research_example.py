import asyncio
import os

import pytest
from inspect_ai.agent._agent import AgentState, agent
from inspect_ai.model._chat_message import ChatMessageAssistant
from inspect_ai.tool._tool_call import ToolCall

from inspect_agents.agents import build_subagents, build_supervisor
from inspect_agents.logging import write_transcript
from inspect_agents.run import run_agent
from inspect_agents.tools import edit_file, ls, read_file, update_todo_status, write_file, write_todos

pytestmark = pytest.mark.handoff


# Toy model that immediately calls submit with a fixed completion.
@agent
def toy_submit_model():
    async def execute(state: AgentState, tools):
        state.messages.append(
            ChatMessageAssistant(
                content="",
                tool_calls=[ToolCall(id="1", function="submit", arguments={"answer": "DONE"})],
            )
        )
        return state

    return execute


def test_research_example_offline_smoke(monkeypatch, tmp_path):
    """Offline smoke test: build research sub-agents and run with a toy model.

    Asserts that run_agent returns a state with a completion and that a transcript
    file is written. No network or real LLMs involved.
    """

    # Write logs to a temp dir (offline is enforced by the root env guard)
    monkeypatch.setenv("INSPECT_LOG_DIR", str(tmp_path))

    import inspect_agents.observability as observability

    captured_events: list[dict[str, object]] = []
    original_log_tool_event = observability.log_tool_event

    def _capture(name, phase, args=None, extra=None, t0=None):
        captured_events.append({"name": name, "phase": phase, "extra": extra})
        return original_log_tool_event(name, phase, args=args, extra=extra, t0=t0)

    monkeypatch.setattr(observability, "log_tool_event", _capture)

    # Root autouse fixture handles environment hardening (approvals cleared,
    # optional tools disabled, provider keys unset, and NO_NETWORK=1).

    # Build a minimal base toolset (no web_search providers required)
    builtins = [write_todos(), update_todo_status(), write_file(), read_file(), ls(), edit_file()]
    base_tools = builtins  # keep deterministic and offline

    # Define research + critique sub-agents (handoffs) with safe tools only
    sub_configs = [
        {
            "name": "research-agent",
            "description": "Research a topic and summarize findings.",
            "prompt": "Research the user question and provide a concise answer.",
            "tools": ["read_file", "write_file", "ls"],
            "mode": "handoff",
        },
        {
            "name": "critique-agent",
            "description": "Critique the draft report and suggest improvements.",
            "prompt": "Critique the report for clarity, completeness, and structure.",
            "tools": ["read_file", "write_file", "ls"],
            "mode": "handoff",
        },
    ]

    subagent_tools = build_subagents(configs=sub_configs, base_tools=base_tools)

    sup = build_supervisor(prompt="You are helpful.", tools=subagent_tools, attempts=1, model=toy_submit_model())

    result = asyncio.run(run_agent(sup, "Delegate research, then finish."))

    # Result assertions
    assert isinstance(result, AgentState)
    assert result.output is not None
    assert "DONE" in (result.output.completion or "")

    # Transcript assertions
    path = write_transcript()
    assert os.path.exists(path)
    defaults_events = [ev for ev in captured_events if ev["name"] == "agent_defaults"]
    assert defaults_events, "expected agent_defaults telemetry"
    assert any(ev.get("extra", {}).get("builder") == "supervisor" for ev in defaults_events)
    assert any(ev.get("extra", {}).get("include_defaults") is True for ev in defaults_events)
    assert any(ev.get("extra", {}).get("include_defaults_source") == "default" for ev in defaults_events)
