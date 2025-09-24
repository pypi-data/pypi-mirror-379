"""Inspect-AI–native building blocks for Inspect Agents.

Exports lightweight state models backed by Inspect-AI's Store/StoreModel and
agent builders (react supervisor and iterative supervisor).
"""

# Re-export builders from the unified agents surface for discoverability
from .agents import build_basic_submit_agent, build_iterative_agent, build_supervisor
from .model import (
    ModelResolutionStep,
    ModelResolutionTrace,
    ResolveModelError,
    resolve_model,
    resolve_model_explain,
)
from .state import Files, Todo, Todos

__all__ = [
    "Todo",
    "Todos",
    "Files",
    "resolve_model",
    "resolve_model_explain",
    "ResolveModelError",
    "ModelResolutionTrace",
    "ModelResolutionStep",
    "build_supervisor",
    "build_basic_submit_agent",
    "build_iterative_agent",
]
