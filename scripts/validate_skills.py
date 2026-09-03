#!/usr/bin/env python3
"""Validate the portable structure and public-safety basics of Fuhao Skills."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_ROOT = ROOT / "skills"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
PRIVATE_PATTERNS = {
    "/Users/": "absolute macOS user path",
    "oc_": "possible chat identifier",
    "APP_SECRET": "possible application secret",
    "access_token": "possible access token",
}
TEXT_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".json", ".txt"}


def frontmatter(text: str) -> dict[str, str]:
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        raise ValueError("SKILL.md must start with YAML frontmatter")
    try:
        end = lines.index("---", 1)
    except ValueError as error:
        raise ValueError("SKILL.md frontmatter is not closed") from error
    values: dict[str, str] = {}
    for line in lines[1:end]:
        match = re.match(r"^([a-zA-Z0-9_-]+):\s*(.*?)\s*$", line)
        if match and match.group(2):
            values[match.group(1)] = match.group(2).strip('"\'')
    return values


def validate_skill(skill_dir: Path) -> list[str]:
    errors: list[str] = []
    entrypoint = skill_dir / "SKILL.md"
    if not entrypoint.exists():
        return [f"{skill_dir}: missing SKILL.md"]
    text = entrypoint.read_text(encoding="utf-8")
    try:
        metadata = frontmatter(text)
    except ValueError as error:
        return [f"{entrypoint}: {error}"]
    name = metadata.get("name", "")
    description = metadata.get("description", "")
    if not NAME_PATTERN.fullmatch(name):
        errors.append(f"{entrypoint}: invalid skill name {name!r}")
    if name != skill_dir.name:
        errors.append(f"{entrypoint}: name must match directory {skill_dir.name!r}")
    if not description or len(description) > 1024:
        errors.append(f"{entrypoint}: description must contain 1-1024 characters")
    if len(text.splitlines()) > 500:
        errors.append(f"{entrypoint}: keep SKILL.md at or below 500 lines")
    return errors


def validate_public_content() -> list[str]:
    errors: list[str] = []
    for path in ROOT.rglob("*"):
        if (
            ".git" in path.parts
            or path.resolve() == Path(__file__).resolve()
            or not path.is_file()
            or path.suffix not in TEXT_SUFFIXES
        ):
            continue
        text = path.read_text(encoding="utf-8")
        for pattern, label in PRIVATE_PATTERNS.items():
            if pattern in text:
                errors.append(f"{path.relative_to(ROOT)}: contains {label} pattern {pattern!r}")
    return errors


def main() -> int:
    errors: list[str] = []
    skill_dirs = sorted(path for path in SKILLS_ROOT.iterdir() if path.is_dir())
    if not skill_dirs:
        errors.append("skills/: no skill directories found")
    for skill_dir in skill_dirs:
        errors.extend(validate_skill(skill_dir))
    errors.extend(validate_public_content())
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Validated {len(skill_dirs)} skill(s): " + ", ".join(path.name for path in skill_dirs))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
