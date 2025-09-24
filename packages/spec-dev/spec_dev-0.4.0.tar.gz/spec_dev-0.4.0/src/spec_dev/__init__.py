"""Utilities for distributing the .spec-dev workspace template."""
from __future__ import annotations

from contextlib import contextmanager
from importlib import resources
from pathlib import Path
import re
import shutil

from .memories import create_session_summary  # noqa: F401

__all__ = [
    "copy",
    "template_dir",
    "create_session_summary",
    "complete_cycle",
]
__version__ = "0.4.0"

_SPEC_ROOT = ".spec-dev"
_HISTORY_DIR = "history"


@contextmanager
def template_dir() -> Path:
    """Yield the location of the packaged .spec-dev directory."""
    source = resources.files("spec_dev.data") / _SPEC_ROOT
    with resources.as_file(source) as path:
        yield Path(path)


def copy(destination: Path | str = Path.cwd(), *, overwrite: bool = False) -> Path:
    """Copy the bundled .spec-dev folder into *destination*.

    Args:
        destination: Directory that should receive the .spec-dev folder.
        overwrite: Overwrite an existing .spec-dev folder when set to True.

    Returns:
        Path to the copied .spec-dev directory.
    """
    dest_path = _validate_destination(destination)

    target_dir = dest_path / _SPEC_ROOT
    if target_dir.exists() and not overwrite:
        raise FileExistsError(
            ".spec-dev already exists; pass overwrite=True to replace it."
        )

    source = resources.files("spec_dev.data") / _SPEC_ROOT
    with resources.as_file(source) as source_dir:
        shutil.copytree(Path(source_dir), target_dir, dirs_exist_ok=overwrite)

    return target_dir



def complete_cycle(
    destination: Path | str = Path.cwd(),
    *,
    label: str | None = None,
) -> Path:
    """Archive the current active artifacts and reset the workspace.

    Args:
        destination: Project directory containing the `.spec-dev` folder.
        label: Optional label appended to the archived cycle directory name.

    Returns:
        Path to the archived cycle directory.
    """
    dest_path = _validate_destination(destination)
    spec_dir = dest_path / _SPEC_ROOT
    if not spec_dir.exists():
        raise FileNotFoundError(
            f"No .spec-dev directory found in {dest_path}. Run copy() first."
        )

    active_dev = spec_dir / "active-dev"
    history_dir = spec_dir / _HISTORY_DIR
    history_dir.mkdir(parents=True, exist_ok=True)

    timestamp = _timestamp()
    if label:
        label_slug = re.sub(r"[^a-zA-Z0-9]+", "-", label).strip("-").lower()
        archive_name = f"{timestamp}-{label_slug}" if label_slug else timestamp
    else:
        archive_name = timestamp

    archive_dir = history_dir / archive_name
    if archive_dir.exists():
        raise FileExistsError(f"Archive already exists: {archive_dir}")

    shutil.copytree(active_dev, archive_dir)
    _reset_active_dev(active_dev)

    memories_dir = spec_dir / "active-memories"
    if memories_dir.exists():
        shutil.rmtree(memories_dir)
    memories_dir.mkdir(parents=True, exist_ok=True)

    return archive_dir


def _timestamp() -> str:
    from datetime import datetime

    return datetime.utcnow().strftime("%Y%m%d-%H%M%S")


def _reset_active_dev(active_dev: Path) -> None:
    for item in active_dev.iterdir():
        if item.name == "README.md":
            continue
        if item.is_file():
            item.unlink()
        elif item.is_dir():
            shutil.rmtree(item)

    template_root = resources.files("spec_dev.data") / _SPEC_ROOT / "templates" / "active"
    with resources.as_file(template_root) as templates_dir:
        for template in Path(templates_dir).iterdir():
            target = active_dev / template.name
            if not target.exists():
                target.write_text(template.read_text())


def _validate_destination(destination: Path | str) -> Path:
    dest_path = Path(destination).expanduser().resolve()
    if not dest_path.exists():
        raise FileNotFoundError(f"Destination does not exist: {dest_path}")
    if not dest_path.is_dir():
        raise NotADirectoryError(f"Destination is not a directory: {dest_path}")
    return dest_path
