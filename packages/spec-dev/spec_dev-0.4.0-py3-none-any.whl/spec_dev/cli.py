"""Command line helpers for deploying the .spec-dev template."""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path
from textwrap import dedent

from . import __version__, complete_cycle, copy
from .tasks_manifest import cmd_build_manifest
from .tasks_board import set_task_status
from .memories import create_session_summary, list_session_summaries


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Manage the packaged .spec-dev workspace template.",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=dedent(
            """Examples:
            spec-dev
            spec-dev session --label agent-one
            spec-dev cycle --label fal-ai-image-gen"""
        ),
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"spec-dev {__version__}",
    )

    subparsers = parser.add_subparsers(dest="command")

    init_parser = subparsers.add_parser(
        "init",
        help="Copy the .spec-dev folder into the target directory.",
    )
    init_parser.add_argument(
        "destination",
        nargs="?",
        default=".",
        help="Directory that should receive the .spec-dev folder (default: current directory)",
    )
    init_parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite an existing .spec-dev directory if present.",
    )
    init_parser.set_defaults(handler=_handle_init)

    session_parser = subparsers.add_parser(
        "session",
        help="Create a session summary file for agent hand-off.",
    )
    session_parser.add_argument(
        "destination",
        nargs="?",
        default=".",
        help="Project directory containing .spec-dev (default: current directory)",
    )
    session_parser.add_argument(
        "--label",
        help="Optional label appended to the session filename (e.g. agent name).",
    )
    session_parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite the generated session file if it already exists.",
    )
    session_parser.set_defaults(handler=_handle_session)

    cycle_parser = subparsers.add_parser(
        "cycle",
        help="Archive the current active artifacts and reset the workspace.",
    )
    cycle_parser.add_argument(
        "destination",
        nargs="?",
        default=".",
        help="Project directory containing .spec-dev (default: current directory)",
    )
    cycle_parser.add_argument(
        "--label",
        help="Optional label appended to the archived cycle directory name.",
    )
    cycle_parser.set_defaults(handler=_handle_cycle)
    manifest_parser = subparsers.add_parser(
        "tasks-manifest",
        help="Generate or display the planned file coverage manifest.",
    )
    manifest_parser.add_argument(
        "destination",
        nargs="?",
        default=".",
        help="Project directory containing .spec-dev (default: current directory)",
    )
    manifest_parser.add_argument(
        "--rewrite",
        action="store_true",
        help="Rewrite active-dev/file-coverage.json with the latest task definitions.",
    )
    manifest_parser.add_argument(
        "--check",
        action="store_true",
        help="Validate that all task paths are well-formed and non-duplicated.",
    )
    manifest_parser.add_argument(
        "--auto-scope",
        action="store_true",
        help=(
            "Infer region selectors for duplicate file paths so multiple tasks can"
            " safely target different parts of the same file."
        ),
    )
    manifest_parser.set_defaults(handler=_handle_tasks_manifest)

    status_parser = subparsers.add_parser(
        "tasks-status",
        help="Update the status of a task card (pending, in-progress, done).",
    )
    status_parser.add_argument(
        "task_id",
        help="Task identifier (e.g. T-107).",
    )
    status_parser.add_argument(
        "--set",
        required=True,
        choices=["pending", "in-progress", "done"],
        help="Status to apply to the task card.",
    )
    status_parser.add_argument(
        "destination",
        nargs="?",
        default=".",
        help="Project directory containing .spec-dev (default: current directory)",
    )
    status_parser.set_defaults(handler=_handle_tasks_status)

    sessions_parser = subparsers.add_parser(
        "sessions",
        help="List session summaries stored in .spec-dev/active-memories.",
    )
    sessions_parser.add_argument(
        "destination",
        nargs="?",
        default=".",
        help="Project directory containing .spec-dev (default: current directory)",
    )
    sessions_parser.set_defaults(handler=_handle_sessions)

    return parser


def main(argv: list[str] | None = None) -> int:
    if argv is None:
        argv = sys.argv[1:]

    if not argv:
        argv = ["init"]
    elif argv[0] not in {"init", "session", "sessions", "cycle", "tasks-manifest", "tasks-status"} and not argv[0].startswith("-"):
        argv = ["init", *argv]

    parser = build_parser()
    args = parser.parse_args(argv)

    try:
        return args.handler(args)
    except FileExistsError as exc:
        parser.error(str(exc))
    except (FileNotFoundError, NotADirectoryError, ValueError) as exc:
        parser.error(str(exc))


def _handle_init(args: argparse.Namespace) -> int:
    destination = Path(args.destination)
    target = copy(destination, overwrite=args.force)
    print(f"Copied .spec-dev to {target}")
    return 0


def _handle_session(args: argparse.Namespace) -> int:
    destination = Path(args.destination)
    session_file = create_session_summary(destination, label=args.label, overwrite=args.overwrite)
    print(f"Created session summary at {session_file}")
    return 0


def _handle_cycle(args: argparse.Namespace) -> int:
    destination = Path(args.destination)
    archived = complete_cycle(destination, label=args.label)
    print(
        f"Archived active artifacts to {archived} and reset active-dev and active-memories"
    )
    return 0


def _handle_tasks_status(args: argparse.Namespace) -> int:
    destination = Path(args.destination)
    set_task_status(destination, args.task_id, args.set)
    print(
        f"Set {args.task_id} status to {args.set}. Run spec-dev tasks-manifest --rewrite --check to refresh coverage."
    )
    return 0


def _handle_sessions(args: argparse.Namespace) -> int:
    destination = Path(args.destination)
    sessions = list_session_summaries(destination)
    if not sessions:
        print("No session summaries found.")
        return 0
    for summary in sessions:
        label = f" ({summary.label})" if summary.label else ""
        print(f"{summary.index:03d}: {summary.path.name}{label}")
    return 0


def _handle_tasks_manifest(args: argparse.Namespace) -> int:
    destination = Path(args.destination)
    manifest = cmd_build_manifest(destination, auto_scope=args.auto_scope)
    if args.check:
        issues = manifest.validate()
        if issues:
            for issue in issues:
                print(f"[!] {issue}")
            sys.exit(1)
    if args.rewrite:
        manifest.write()
        print(f"Wrote manifest to {manifest.path}")
    else:
        print(json.dumps(manifest.to_dict(), indent=2))
    return 0


if __name__ == "__main__":  # pragma: no cover - CLI entry point
    sys.exit(main())
