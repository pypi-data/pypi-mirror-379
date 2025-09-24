# Inspect Agents Test Guides

Central index of testing guides for this repository. Tests default to offline, fast, and deterministic runs.

## Structure
- unit: fast, isolated tests (`tests/unit/**`).
  - Each `inspect_agents/<domain>/` has its own [README](../unit/inspect_agents/) with scope, fixtures, and selection examples.
  - `inspect_agents/approvals`: approval policies, handoff exclusivity, kill-switch.
  - `inspect_agents/filters`: input/output filters and quarantine modes.
  - `inspect_agents/fs`: files tool + sandbox FS behaviors.
  - `inspect_agents/iterative`: iterative agent limits, productive time.
  - `inspect_agents/model`: model resolution + role mapping.
  - `inspect_agents/tools`: tool schemas, observability, todos tool.
  - `inspect_agents/schema`: pydantic models, typed results.
  - `inspect_agents/state`: store-backed state shims.
  - `inspect_agents/config`: YAML loader + limits.
  - `inspect_agents/logging`: transcript + redaction logic.
  - `inspect_agents/migration`: legacy→deep agent migration path.
  - `inspect_agents/observability`: observability and monitoring.
  - `inspect_agents/planner`: planning functionality.
  - `inspect_agents/profiles`: profiles management.
  - `inspect_agents/run`: run-related functionality.
- integration: end-to-end and script-driven tests (`tests/integration/**`).
  - `examples/`, `research/` consolidated here.
  - Offline-hardening: a root autouse fixture clears approvals, disables
    optional tools, and defaults to `NO_NETWORK=1`. It lives in
    `tests/conftest.py` as `_default_env_guard`. Integration tests no longer
    carry their own copy.
- fixtures: shared helpers and test data (`tests/fixtures/**`).
- docs: local testing guides (this directory, `TESTING_*.md`).
- perf: opt-in performance suites (`tests/perf/**`); marker-friendly even when `pytest-benchmark` is absent.

Recent tidy-up:
- Moved `tests/inspect_agents/*` into `tests/unit/inspect_agents/` with domain subfolders.
- Moved runner examples under `tests/integration/examples/`.
- Moved research runner CI checks under `tests/integration/research/`.

## Guides
- Pytest core: `TESTING_PYTEST_CORE.md`
- Async tests (pytest-asyncio): `TESTING_ASYNC.md`
- Approvals & policies: `TESTING_APPROVALS_POLICIES.md`
- E2E sandbox (Docker/K8s): `TESTING_E2E.md`
- Filters: `TESTING_FILTERS.md`
- Subagents & handoffs: `TESTING_SUBAGENTS_HANDOFFS.md`
- Tools & filesystem: `TESTING_TOOLS_FILESYSTEM.md`
- Tool timeouts: `TESTING_TOOL_TIMEOUTS.md`
- Limits & truncation: `TESTING_LIMITS_TRUNCATION.md`
- Model resolution: `TESTING_MODEL_RESOLUTION.md`
- Coverage (pytest-cov/coverage.py): `TESTING_COVERAGE.md`
- Parallel (pytest-xdist): `TESTING_PARALLEL.md`
- Benchmarks (pytest-benchmark): `TESTING_BENCHMARKS.md`
- Property-based (Hypothesis): `TESTING_PROPERTY_BASED.md`
- Mocking (pytest-mock): `TESTING_MOCKING.md`

## Quick Commands
- Run all tests offline (parallel by default): `CI=1 NO_NETWORK=1 uv run pytest -q`
- Narrow to a subset: `uv run pytest -q -k <expr>`
- Disable parallel: `uv run pytest -q -n 0`
- Set explicit workers: `uv run pytest -q -n 4`

### Run a Domain (Examples)
- Unit (filesystem): `uv run pytest -q tests/unit/inspect_agents/fs -k read`
- Unit (iterative): `uv run pytest -q tests/unit/inspect_agents/iterative -k truncation`
- Integration by marker: `uv run pytest -q -m handoff tests/integration/inspect_agents`
- Single test: `uv run pytest -q tests/unit/inspect_agents/iterative/test_iterative_limits.py::test_env_fallback_max_steps`

## CI Surfacing vs Local
- In CI, failing tests print links to relevant guides automatically (see `tests/conftest.py`).
- Locally, this is off by default to reduce noise. Opt in with:
  ```bash
  export DEEPAGENTS_SHOW_TEST_GUIDES=1
  uv run pytest -q
  ```

## Markers
- Network control: use `@pytest.mark.network` to allow real network for a test; default is offline via root guard.
- We tag suites with markers to improve guide suggestions in CI:
  - `approvals`, `handoff`, `filters`, `kill_switch`, `timeout`, `truncation`, `parallel`, `model_flags`.
- List markers: `pytest --markers`.
- Select by marker: `pytest -m handoff -q`.

## Benchmarks (opt-in)
- PR: add the label `run-benchmarks` to trigger the Benchmarks workflow.
- Manual: you can also run it via the “Benchmarks (on label)” workflow_dispatch.
- Local: `pytest -q -m benchmark --benchmark-only tests/perf`.

## Conventions
- Keep tests deterministic; set env in-tests via `monkeypatch`.
- Prefer small, behavior-focused tests; use fixtures for shared setup.

## Domain-Specific READMEs

For detailed guidance on each unit test domain, see the individual READMEs:

- [Approvals](../unit/inspect_agents/approvals/README.md) – approval policies, handoff exclusivity, kill-switch
- [Config](../unit/inspect_agents/config/README.md) – YAML loader + limits
- [Filters](../unit/inspect_agents/filters/README.md) – input/output filters and quarantine modes
- [Filesystem](../unit/inspect_agents/fs/README.md) – files tool + sandbox FS behaviors
- [Iterative](../unit/inspect_agents/iterative/README.md) – iterative agent limits, productive time
- [Logging](../unit/inspect_agents/logging/README.md) – transcript + redaction logic
- [Migration](../unit/inspect_agents/migration/README.md) – legacy→deep agent migration path
- [Model](../unit/inspect_agents/model/README.md) – model resolution + role mapping
- [Observability](../unit/inspect_agents/observability/README.md) – observability and monitoring
- [Planner](../unit/inspect_agents/planner/README.md) – planning functionality
- [Profiles](../unit/inspect_agents/profiles/README.md) – profiles management
- [Run](../unit/inspect_agents/run/README.md) – run-related functionality
- [Schema](../unit/inspect_agents/schema/README.md) – pydantic models, typed results
- [State](../unit/inspect_agents/state/README.md) – store-backed state shims
- [Tools](../unit/inspect_agents/tools/README.md) – tool schemas, observability, todos tool
