#!/usr/bin/env python3
"""Validate package structure and required skill metadata without dependencies."""

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS = ROOT / "skills"
NAME = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*\Z")


def validate() -> list[str]:
    errors = []
    for skill in sorted(SKILLS.iterdir()):
        if not skill.is_dir():
            errors.append(f"{skill}: expected a skill directory")
            continue
        file = skill / "SKILL.md"
        if not file.is_file():
            errors.append(f"{file}: missing")
            continue
        content = file.read_text(encoding="utf-8")
        match = re.match(r"\A---\n(.*?)\n---\n", content, re.S)
        if not match:
            errors.append(f"{file}: missing YAML frontmatter")
            continue
        fields = dict(re.findall(r"^(name|description):\s*(.+)$", match.group(1), re.M))
        if fields.get("name") != skill.name or not NAME.fullmatch(skill.name):
            errors.append(f"{file}: name must match a lowercase hyphenated folder name")
        if not fields.get("description") or len(fields["description"].strip()) < 30:
            errors.append(f"{file}: description is missing or too short")
        if not content[match.end():].strip():
            errors.append(f"{file}: body is empty")
        if "TODO" in content or "[INSERT" in content:
            errors.append(f"{file}: unfinished placeholder")
    if not any(SKILLS.iterdir()):
        errors.append("No skills found")
    return errors


if __name__ == "__main__":
    failures = validate()
    if failures:
        print("\n".join(failures), file=sys.stderr)
        raise SystemExit(1)
    print("All skills valid")
