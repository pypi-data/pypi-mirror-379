"""Command-line entrypoint for managing the .spec-dev template."""
from __future__ import annotations

import argparse
from pathlib import Path

from . import copy, __version__


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Copy the bundled .spec-dev folder into a project directory."
    )
    parser.add_argument(
        "command",
        nargs="?",
        default="init",
        help="Only 'init' is supported; defaults to 'init' when omitted.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=".",
        help="Destination directory for the .spec-dev folder (defaults to current directory).",
    )
    parser.add_argument(
        "--overwrite",
        action="store_true",
        help="Overwrite an existing .spec-dev folder if present.",
    )
    parser.add_argument(
        "--version",
        action="version",
        version=f"spec-dev {__version__}",
    )

    args = parser.parse_args(argv)
    if args.command != "init":
        parser.error("Only the 'init' command is supported.")
    return args


def main(argv: list[str] | None = None) -> None:
    args = parse_args(argv)
    destination = Path(args.path)
    target = copy(destination, overwrite=args.overwrite)
    print(f".spec-dev template copied to {target}")


if __name__ == "__main__":
    main()
