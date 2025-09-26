# spec-dev

A minimal helper that ships a `.spec-dev` folder containing empty role guides for
three agents: architect, tasker, and coder. The package exists so the template can
be installed with `pip` and copied into any project without manual setup.

## Installation

```bash
pip install spec-dev
```

Working from a clone of this repository? Install it locally instead:

```bash
pip install .
```

## CLI Usage

```bash
# Copy the template into the current directory
spec-dev init

# Copy into a specific project directory
spec-dev init path/to/project

# Replace an existing .spec-dev folder
spec-dev init path/to/project --overwrite
```

The command always produces a `.spec-dev/` folder with the following files ready
for you to populate:

- `.spec-dev/architect.md` — guidance for the planning agent.
- `.spec-dev/tasker.md` — instructions for turning the plan into phase/task lists.
- `.spec-dev/coder.md` — instructions for the implementation agent.

Each file ships empty so teams can supply the wording that best matches their
workflow.

## Python API

```python
from spec_dev import copy

root = copy("/path/to/project", overwrite=True)
print(root / "architect.md")  # => Path to the empty template file
```

`copy()` returns the path to the freshly created `.spec-dev` directory, making it
convenient to script project bootstrapping.

## License

MIT
