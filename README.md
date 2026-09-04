# agency
This project contains multiple proof of concepts and demos for agent orchestration and compromised-state detection

## Layout

A [uv workspace](https://docs.astral.sh/uv/concepts/projects/workspaces/): one lockfile and one
virtual environment at the root, shared by every member.

```
packages/agency-core/   code shared by the demos (imported as `agency`)
demos/                  one directory per demo, each its own package
```

## Setup

```bash
uv sync --all-packages
```

This creates `.venv/` at the root and installs `agency-core` and every demo into it as editable
installs, so edits to `agency` take effect in the demos immediately. Do not create a virtual
environment per demo -- a workspace resolves to a single set of dependency versions by design.
Point your editor's interpreter at `.venv/`.

## Running a demo

`uv run` uses the root environment automatically; there is nothing to activate.

```bash
uv run --package agent-single-node agent-single-node
uv run --package react-agent react-agent
```

## Managing dependencies

Add a dependency to the package that actually imports it. Either form updates that package's
`pyproject.toml` and the root `uv.lock`:

```bash
uv add --package <demo-name> <dependency>     # from anywhere in the workspace
cd demos/<demo-name> && uv add <dependency>   # equivalent
```

Dependencies needed by more than one demo belong in the shared package instead, and the demos
inherit them:

```bash
uv add --package agency-core <dependency>
```

Note that `uv remove` re-syncs the environment to only the target package's dependencies, which
can uninstall others. Follow it with `uv sync --all-packages`.

## Adding a demo

```bash
uv init --package demos/<demo-name>
uv add --package <demo-name> agency-core
```

`members = ["packages/*", "demos/*"]` in the root `pyproject.toml` picks it up with no further
registration.
