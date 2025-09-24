# Repository Guidelines

## Project Structure & Module Organization
- `fastdi/`: Python API (container, decorators, types) and `py.typed`.
- `_fastdi_core` (Rust ext): `Cargo.toml`, `src/lib.rs` exposed via PyO3.
- `tests/`: Pytest suite (sync/async, plan, hooks, methods).
- `examples/`: Small runnable samples (basic, async, request scope).
- `benchmarks/`: Microbenchmarks comparing libraries.
- `docs/` + `mkdocs.yml`: Landing page plus `getting-started.md`, `usage.md`, `observability.md`, `performance.md`, `architecture.md`, and API reference stubs.
- `README.md`: Overview and design reference.

## Distribution & Releases
- PyPI project name: `fastdi-core`. Installing it exposes the `fastdi` package (`from fastdi import ...`).
- End users install via `pip install fastdi-core`; developers typically run `uv sync --all-groups`.
- Runtime requirements: Python 3.9+ and a stable Rust toolchain.
- Packaging bundles `_fastdi_core.pyi`, Rust ABI3 extension, and all Python modules.
- GitHub Actions workflow `Build Wheels and Publish` (linux x86_64 + macOS universal2) builds via uv + cibuildwheel + maturin and publishes on tags matching `v*` (requires `PYPI_API_TOKEN`). Use `workflow_dispatch` for dry runs.
- Local release sanity check: `uvx maturin build --release -o dist` followed by `uvx maturin sdist --out dist`. Upload via `pypa/gh-action-pypi-publish` (preferred) or `uv publish`.

## Build, Test, and Development Commands
- Create env: `uv sync --all-groups` (or `pip install -e .[dev]`). Python 3.9+ only.
- Core tooling versions (minimums):
  - `maturin>=1.9.4`
  - `mkdocs>=1.6.1`, `mkdocs-material>=9.6.20`, `mkdocstrings>=0.30.1`, `mkdocstrings-python>=1.18.2`
  - `mypy>=1.18.2`, `pytest>=8.4.2`, `pytest-asyncio>=1.2.0`
  - `ruff>=0.13.1`, `pre-commit>=4.3.0`, `tabulate>=0.9.0`
- Build Rust ext (editable): `maturin develop -r` (use `-r` for release).
- Lint/format: `ruff check .` and `ruff format .`.
- Type check: `mypy .`.
- Tests: `pytest -q` (add `-k pattern` to filter).
- Docs preview: `mkdocs serve` (build: `mkdocs build`).
- Benchmarks: `python benchmarks/benchmarks.py` (run on release build).

## Human-in-the-loop Learning Guidance (for AI assistants)
- **Start by orienting together.** Ask the human to:
  1. Read `README.md` and the MkDocs pages (`getting-started → usage → architecture`).
  2. Run and discuss the example scripts (`examples.basic`, `examples.async_basic`, `examples.request_scope_async`).
  3. Walk through at least one sync and one async test, explaining what each assertion confirms.
- **Encourage active note-taking.** Prompt the human to maintain a scratch log (e.g., `notes/`) summarizing container setups, plan expectations, and open questions discovered during the session.
- **Before proposing fixes:**
  1. Request a clear reproduction (script/test output) and the human’s hypothesis.
  2. Confirm there is or will be a regression test capturing the bug.
  3. Ask the human to outline the expected dependency graph and scope behavior in their own words.
- **While suggesting changes:**
  - Provide reasoning for each modification, referencing architecture or docs sections.
  - Highlight alternative solutions so the human can choose and understand trade-offs.
  - Point out areas that need manual validation (benchmarks, async flows, plan invalidation) and ask the human to run the checks.
- **After changes:**
  - Review test outcomes together (`uv run pytest -q`, `ruff check`, `mypy`).
  - Have the human update their notes with new insights or invariants learned.
  - Encourage a short retro: what was unclear, what to automate, and which docs/tests should be amended for future readers.

## Coding Style & Naming Conventions
- Python: 4‑space indent, type‑annotated; prefer `Annotated[...]` for DI.
- Rust: idiomatic Rust, minimal `unsafe`, small focused modules.
- Tools: ruff (lint/format), mypy (strict typing). Keep code clear and small.
- Naming: snake_case (functions/vars), PascalCase (classes), SCREAMING_SNAKE_CASE (consts).

## Testing Guidelines
- Framework: pytest. Place tests in `tests/` as `test_*.py`.
- Cover new features with sync/async cases and edge conditions.
- Avoid flakiness: no network or time‑sensitive sleeps; use fixtures.
- Run `pytest -q && ruff check . && mypy .` before pushing.

## Commit & Pull Request Guidelines
- Commits: use Conventional Commits (e.g., `feat:`, `fix:`, `chore:`), concise subject ≤72 chars, focused diff.
- Include context in body: what/why; reference issues (`Fixes #123`).
- PRs: clear description, motivation, screenshots/logs if relevant.
- Requirements: passing CI, updated tests, docs when user‑visible behavior changes.
- Scope: no unrelated refactors; keep changes minimal and reviewable.

## Architecture Overview
- Two layers: Python API (user‑facing DI) and Rust core (plan compilation and high‑perf execution via PyO3 0.26 with abi3 py39).
- Observability hooks surface provider start/end and cache hits.
