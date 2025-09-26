"""Minimal helpers for shipping the .spec-dev template."""
from __future__ import annotations

from contextlib import contextmanager
from importlib import resources
from pathlib import Path
import shutil

__all__ = ["copy", "template_dir", "__version__"]
__version__ = "0.5.5"

_SPEC_ROOT = ".spec-dev"


@contextmanager
def template_dir() -> Path:
    """Yield the packaged .spec-dev directory as a temporary path."""
    source = resources.files("spec_dev.data") / _SPEC_ROOT
    with resources.as_file(source) as path:
        yield Path(path)


def copy(destination: Path | str = Path.cwd(), *, overwrite: bool = False) -> Path:
    """Copy the bundled .spec-dev folder into *destination*."""
    dest_path = Path(destination).expanduser().resolve()
    if not dest_path.exists():
        raise FileNotFoundError(f"Destination does not exist: {dest_path}")
    if not dest_path.is_dir():
        raise NotADirectoryError(f"Destination is not a directory: {dest_path}")

    target_dir = dest_path / _SPEC_ROOT
    if target_dir.exists() and not overwrite:
        raise FileExistsError(
            ".spec-dev already exists; pass overwrite=True to replace it."
        )

    source = resources.files("spec_dev.data") / _SPEC_ROOT
    with resources.as_file(source) as source_dir:
        shutil.copytree(Path(source_dir), target_dir, dirs_exist_ok=overwrite)

    return target_dir
