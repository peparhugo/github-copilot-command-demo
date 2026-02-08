#!/usr/bin/env python3
"""Report symlinked skills in source snapshots."""

from __future__ import annotations

import argparse
from pathlib import Path
import sys

SKILL_FILE = "SKILL.md"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Detect skill directories that are symlinks in a source snapshot root."
    )
    parser.add_argument(
        "roots",
        nargs="+",
        help="One or more source snapshot roots to scan (for example, .github/skills).",
    )
    return parser.parse_args()


def detect_symlinked_skills(root: Path) -> list[tuple[Path, Path]]:
    symlinked_skills: list[tuple[Path, Path]] = []
    for skill_file in root.rglob(SKILL_FILE):
        skill_dir = skill_file.parent
        if skill_dir.is_symlink():
            symlinked_skills.append((skill_dir.relative_to(root), skill_dir.resolve()))
    return sorted(symlinked_skills, key=lambda row: str(row[0]))


def main() -> int:
    args = parse_args()
    had_missing_root = False

    for raw_root in args.roots:
        root = Path(raw_root)
        if not root.is_dir():
            print(f"ERROR: root does not exist: {root}", file=sys.stderr)
            had_missing_root = True
            continue

        symlinks = detect_symlinked_skills(root)
        print(f"== {root} ==")
        if not symlinks:
            print("(no symlinked skills found)")
            continue

        for rel_path, target in symlinks:
            print(f"- {rel_path} -> {target}")

    return 1 if had_missing_root else 0


if __name__ == "__main__":
    raise SystemExit(main())
