#!/usr/bin/env python3
"""Install this repository's skills into one or more project agent folders."""

import argparse
import filecmp
import shutil
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / "skills"
DESTINATIONS = {
    "claude": Path(".claude/skills"),
    "codex": Path(".agents/skills"),
    "copilot": Path(".github/skills"),
}


def same_tree(source: Path, destination: Path) -> bool:
    if destination.is_symlink() or not destination.is_dir():
        return False
    source_files = {p.relative_to(source) for p in source.rglob("*") if p.is_file()}
    destination_files = {
        p.relative_to(destination) for p in destination.rglob("*") if p.is_file()
    }
    return source_files == destination_files and all(
        filecmp.cmp(source / name, destination / name, shallow=False)
        for name in source_files
    )


def install(project: Path, tools: list[str]) -> int:
    if not project.is_dir():
        print(f"Project directory does not exist: {project}", file=sys.stderr)
        return 2
    skills = sorted(p for p in SOURCE.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())
    if not skills:
        print("No skills found in package", file=sys.stderr)
        return 2

    actions = []
    conflicts = []
    for tool in tools:
        for skill in skills:
            target = project / DESTINATIONS[tool] / skill.name
            if target.exists() or target.is_symlink():
                if not same_tree(skill, target):
                    conflicts.append(target)
            else:
                actions.append((skill, target))

    if conflicts:
        print("Existing skills differ; no files were copied:", file=sys.stderr)
        for target in conflicts:
            print(f"  {target}", file=sys.stderr)
        return 1

    for skill, target in actions:
        target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copytree(skill, target)
        print(f"Installed {target}")
    if not actions:
        print("Skills are already up to date")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--project", type=Path, required=True, help="existing project directory")
    parser.add_argument("--tool", choices=[*DESTINATIONS, "all"], default="all")
    args = parser.parse_args()
    selected = list(DESTINATIONS) if args.tool == "all" else [args.tool]
    return install(args.project.resolve(), selected)


if __name__ == "__main__":
    raise SystemExit(main())
