from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
import re
from typing import List, Optional

_SESSION_DIR = Path('.spec-dev/active-memories')
_SESSION_TEMPLATE = Path('.spec-dev/templates/memories/session-summary-template.md')
_SESSION_PATTERN = re.compile(r'^session-(\d{3})(?:-.*)?\.md$')


@dataclass
class SessionSummary:
    path: Path
    index: int
    label: Optional[str]


def _sanitize_label(label: str) -> str:
    slug = re.sub(r'[^a-zA-Z0-9]+', '-', label.strip()).strip('-').lower()
    return slug or 'notes'


def _next_session_index(session_dir: Path) -> int:
    max_index = 0
    if session_dir.exists():
        for file in session_dir.iterdir():
            if not file.is_file():
                continue
            match = _SESSION_PATTERN.match(file.name)
            if match:
                index = int(match.group(1))
                if index > max_index:
                    max_index = index
    return max_index + 1


def create_session_summary(
    destination: Path | str = Path.cwd(),
    *,
    label: str | None = None,
    overwrite: bool = False,
) -> Path:
    root = Path(destination).expanduser().resolve()
    session_dir = root / _SESSION_DIR
    session_dir.mkdir(parents=True, exist_ok=True)

    index = _next_session_index(session_dir)
    name = f"session-{index:03d}"
    slug = _sanitize_label(label) if label else None
    filename = f"{name}.md" if not slug else f"{name}-{slug}.md"
    target = session_dir / filename

    if target.exists() and not overwrite:
        raise FileExistsError(f"Session summary already exists: {target}")

    template = root / _SESSION_TEMPLATE
    if not template.exists():
        raise FileNotFoundError(f"Template not found: {template}")

    content = template.read_text()
    content = content.replace('<SESSION_ID>', name)
    if label:
        content = content.replace('<SESSION_LABEL>', label)
    else:
        content = content.replace('<SESSION_LABEL>', '')
    target.write_text(content)
    return target


def list_session_summaries(destination: Path | str = Path.cwd()) -> List[SessionSummary]:
    root = Path(destination).expanduser().resolve()
    session_dir = root / _SESSION_DIR
    summaries: List[SessionSummary] = []
    if not session_dir.exists():
        return summaries

    for file in sorted(session_dir.iterdir()):
        if not file.is_file():
            continue
        match = _SESSION_PATTERN.match(file.name)
        if not match:
            continue
        index = int(match.group(1))
        label: Optional[str] = None
        parts = file.stem.split('-', 2)
        if len(parts) == 3:
            label = parts[2]
        summaries.append(SessionSummary(path=file, index=index, label=label))
    return summaries
