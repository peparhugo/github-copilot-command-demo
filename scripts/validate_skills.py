#!/usr/bin/env python3
"""Validate wave-level skill migration metadata."""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys


REQUIRED_FILES = [
    Path("skills_index.json"),
    Path("data/catalog.json"),
    Path("data/aliases.json"),
]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate skill migration metadata files.")
    parser.add_argument(
        "--wave",
        default="all",
        help="Wave label for logging purposes (e.g. PR-0, PR-1).",
    )
    return parser.parse_args()


def validate_json_file(path: Path) -> None:
    if not path.exists():
        raise FileNotFoundError(f"Missing required metadata file: {path}")

    with path.open("r", encoding="utf-8") as file:
        json.load(file)


def main() -> int:
    args = parse_args()

    try:
        for json_file in REQUIRED_FILES:
            validate_json_file(json_file)
    except Exception as exc:  # noqa: BLE001
        print(f"ERROR [{args.wave}]: {exc}", file=sys.stderr)
        return 1

    print(f"Validation passed for wave '{args.wave}'.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
