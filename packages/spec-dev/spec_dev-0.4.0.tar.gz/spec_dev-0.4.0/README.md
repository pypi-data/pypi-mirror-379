# spec-dev

A small helper package that bundles the `.spec-dev` workspace template so it can be
installed with `pip` and copied into new projects.

## Installation

```bash
pip install spec-dev
```

If you are working from the repository source, you can install it locally instead:

```bash
pip install .
```

## CLI Usage

```bash
# Initialise a project (default destination is the current directory)
spec-dev init
spec-dev init path/to/app
spec-dev init --force                  # overwrite an existing .spec-dev folder

# Capture a session summary before handing work to another agent
spec-dev session --label agent-alpha

# Archive the current cycle and reset active templates/memories
spec-dev cycle --label fal-ai-image-gen

# Regenerate and validate the file coverage manifest for the current tasks
# Regenerate and validate the file coverage manifest for the current tasks
spec-dev tasks-manifest --rewrite --check

# Update task status without editing Markdown manually
spec-dev tasks-status T-123 --set done
spec-dev sessions               # list existing session summaries
```

Run `spec-dev --help` for the full command list and examples.

## Python API

```python
from spec_dev import copy, create_session_summary, complete_cycle
from spec_dev.tasks_manifest import cmd_build_manifest

root = copy("/path/to/project", overwrite=True)
session = create_session_summary(root, label="agent-alpha")
archive = complete_cycle(root, label="fal-ai-image-gen")
manifest = cmd_build_manifest(root)  # also available via CLI: spec-dev tasks-manifest
```

Each helper returns the `Path` it creates (the `.spec-dev` directory, the new
session summary, or the archived history folder).

## Workflow Primer

The bundled instructions under `.spec-dev/*.md` walk you through the
Plan & Intent → Tasks → Implementation phases. Highlights:

- `.spec-dev/templates/active/` contains fresh templates for each phase, ready
  to copy into `.spec-dev/active-dev/`. Add deeper discovery material alongside the plan only when it adds value.
- The Plan & Intent artifact must list every existing file to modify, every new file to create, and spell out ordered phases (Phase 0, Phase 1, …) with objectives and exit criteria.
- Run `spec-dev tasks-manifest --auto-scope --rewrite --check` after the task board
  is in place. It regenerates `active-dev/file-coverage.json`, validates that each
  `(path, selector)` maps to exactly one task (use `@ <selector>` to scope to a
  region), and becomes the checklist before you flip the
  gate to READY FOR IMPLEMENTATION.
- Tasks mirror the plan phases using `## Phase N — …` headings with status badges while keeping the strict `### T-###` + `changes` blocks for manifest compatibility.
- Implementation logs capture each finished task while you keep the phase badges in sync (note phase completion in a task entry only if it helps reviewers).
- Update task status (`pending`, `in-progress`, `done`) with
  `spec-dev tasks-status T-XXX --set <status>` so history stays intact until you
  archive the cycle.
- Session summaries live under `.spec-dev/active-memories/`; run
  `spec-dev session [--label <agent-name>]` before you hand the work to another agent, and use `spec-dev sessions` to review existing notes.
- After delivering a cycle, run `spec-dev cycle [--label <name>]` to move the
  finished plan/tasks/implementation log and active memories into
  `.spec-dev/history/`, then reset `active-dev/` and `active-memories/` with clean
  templates for the next iteration.
- After delivering a cycle, run `spec-dev cycle [--label <name>]` to move the
  finished plan/tasks/implementation log and active memories into
  `.spec-dev/history/`, then reset `active-dev/` and `active-memories/` with clean
  templates for the next iteration.

### Key Files

- `.spec-dev/Plan.md`, `.spec-dev/Tasks.md`, `.spec-dev/Implementation.md` — phase instructions that govern the agent. Add any deeper discovery material alongside the plan on an as-needed basis.
- `.spec-dev/active-dev/` — working copies for the current cycle.
- `.spec-dev/active-memories/` — session summaries for hand-offs.
- `.spec-dev/active-dev/file-coverage.json` — auto-generated manifest of task
  changes (maintained via `spec-dev tasks-manifest`).
- `.spec-dev/history/` — archived cycles produced by `spec-dev cycle`.
