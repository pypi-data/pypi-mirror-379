# Testing Guide — Parallel Execution (xdist)

Use `pytest-xdist` to parallelize where safe, and avoid shared global state.

## Running
- Default parallel: `pytest -q` (configured via `addopts`)
- Disable parallel: `pytest -q -n 0`
- Explicit workers: `pytest -q -n 4`

## Design for safety
- Tests must be order- and process-independent; avoid writes to the same temp path.
- Avoid global singletons; prefer per-test stores/fixtures.
- For stateful subsystems (e.g., approvals, env toggles), scope with `monkeypatch` and clear between tests.

## When to avoid xdist
- Tests that rely on process-global mocks shims without isolation.
- Tests that intentionally serialize heavy resources.

## Examples
- Safe tmp isolation with `tmp_path`:
  ```python
  def test_parallel_safe_tmp(tmp_path):
      p = tmp_path / "out.txt"
      p.write_text("ok", encoding="utf-8")
      assert p.read_text(encoding="utf-8") == "ok"
  ```

## References
- pytest-xdist docs (overview and usage).
