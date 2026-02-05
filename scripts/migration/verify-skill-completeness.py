#!/usr/bin/env python3
"""Verify imported skills include all sibling files/directories from source snapshots."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

SKILL_FILE = "SKILL.md"
IGNORED_NAMES = {".DS_Store", "__pycache__"}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Assert that for each imported SKILL.md under --import-root, all sibling "
            "files/directories from the corresponding source skill are also imported."
        )
    )
    parser.add_argument(
        "--source-root",
        default=".github/skills",
        help="Root directory containing source snapshot skills.",
    )
    parser.add_argument(
        "--import-root",
        default="skills",
        help="Root directory containing imported skills.",
    )
    return parser.parse_args()


def visible_entries(skill_dir: Path) -> set[str]:
    return {
        child.name
        for child in skill_dir.iterdir()
        if child.name not in IGNORED_NAMES
    }


def main() -> int:
    args = parse_args()
    source_root = Path(args.source_root)
    import_root = Path(args.import_root)

    if not source_root.is_dir():
        print(f"ERROR: source root does not exist: {source_root}", file=sys.stderr)
        return 1

    if not import_root.is_dir():
        print(f"ERROR: import root does not exist: {import_root}", file=sys.stderr)
        return 1

    imported_skill_files = sorted(import_root.rglob(SKILL_FILE))

    failures: list[str] = []
    checked = 0

    for imported_skill_file in imported_skill_files:
        rel_skill = imported_skill_file.relative_to(import_root)
        source_skill_dir = source_root / rel_skill.parent

        if not source_skill_dir.is_dir():
            failures.append(
                f"{rel_skill.parent}: imported SKILL.md exists but source skill directory is missing ({source_skill_dir})"
            )
            continue

        source_entries = visible_entries(source_skill_dir)
        imported_entries = visible_entries(imported_skill_file.parent)

        missing = sorted(source_entries - imported_entries)
        if missing:
            failures.append(
                f"{rel_skill.parent}: missing sibling entries from source snapshot: {', '.join(missing)}"
            )

        checked += 1

    if failures:
        print("Skill completeness check failed:", file=sys.stderr)
        for failure in failures:
            print(f"- {failure}", file=sys.stderr)
        return 1

    print(
        f"Skill completeness check passed ({checked} imported skill(s) verified)."
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
