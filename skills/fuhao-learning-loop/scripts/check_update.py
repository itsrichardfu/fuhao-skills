#!/usr/bin/env python3
"""Check the latest Fuhao Learning Loop version without blocking learning."""

from __future__ import annotations

import argparse
import json
import os
import time
import urllib.request
from pathlib import Path


REMOTE_SKILL_URL = (
    "https://raw.githubusercontent.com/itsrichardfu/fuhao-skills/"
    "main/skills/fuhao-learning-loop/SKILL.md"
)
UPDATE_URL = "https://github.com/itsrichardfu/fuhao-skills/tree/main/skills/fuhao-learning-loop"
CACHE_TTL_SECONDS = 24 * 60 * 60


def extract_version(text: str) -> str:
    in_metadata = False
    for line in text.splitlines():
        if line.strip() == "metadata:":
            in_metadata = True
            continue
        if not in_metadata:
            continue
        if line and not line[0].isspace():
            break
        stripped = line.strip()
        if stripped.startswith("version:"):
            return stripped.split(":", 1)[1].strip().strip("\"'").removeprefix("v")
    raise ValueError("metadata.version is missing")


def version_key(version: str) -> tuple[int, int, int]:
    parts = version.split(".")
    if len(parts) != 3 or not all(part.isdigit() for part in parts):
        raise ValueError(f"unsupported version: {version}")
    return tuple(int(part) for part in parts)


def cache_path() -> Path:
    base = Path(os.environ.get("XDG_CACHE_HOME") or (Path.home() / ".cache"))
    return base / "fuhao-learning-loop" / "update-check.json"


def read_cache(path: Path) -> dict:
    try:
        value = json.loads(path.read_text(encoding="utf-8"))
        return value if isinstance(value, dict) else {}
    except (OSError, ValueError, TypeError):
        return {}


def write_cache(path: Path, latest_version: str, checked_at: int) -> None:
    try:
        path.parent.mkdir(parents=True, exist_ok=True)
        temporary = path.with_suffix(f".{os.getpid()}.tmp")
        temporary.write_text(
            json.dumps({"latestVersion": latest_version, "checkedAt": checked_at}) + "\n",
            encoding="utf-8",
        )
        temporary.replace(path)
    except OSError:
        pass


def fetch_latest(url: str, timeout: float) -> str:
    request = urllib.request.Request(url, headers={"User-Agent": "fuhao-learning-loop-update-check"})
    with urllib.request.urlopen(request, timeout=timeout) as response:
        return extract_version(response.read(200_000).decode("utf-8"))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--force", action="store_true", help="ignore the 24-hour cache")
    parser.add_argument("--timeout", type=float, default=3.0, help="network timeout in seconds")
    parser.add_argument("--remote-url", default=REMOTE_SKILL_URL, help=argparse.SUPPRESS)
    args = parser.parse_args()

    current = extract_version((Path(__file__).resolve().parents[1] / "SKILL.md").read_text(encoding="utf-8"))
    now = int(time.time())
    path = cache_path()
    cached = read_cache(path)
    latest = str(cached.get("latestVersion") or "")
    checked_at = int(cached.get("checkedAt") or 0)
    source = "cache"

    if args.force or not latest or now - checked_at >= CACHE_TTL_SECONDS:
        try:
            latest = fetch_latest(args.remote_url, max(0.5, min(args.timeout, 10.0)))
            checked_at = now
            source = "network"
            write_cache(path, latest, checked_at)
        except (OSError, ValueError, UnicodeError):
            if latest:
                source = "stale_cache"
            else:
                print(json.dumps({
                    "status": "unavailable",
                    "currentVersion": current,
                    "latestVersion": None,
                    "updateUrl": UPDATE_URL,
                }))
                return 0

    status = "update_available" if version_key(latest) > version_key(current) else "current"
    result = {
        "status": status,
        "currentVersion": current,
        "latestVersion": latest,
        "updateUrl": UPDATE_URL,
        "checkedAt": checked_at,
        "source": source,
    }
    if status == "update_available":
        result["userNotice"] = (
            f"版本提示：fuhao-learning-loop 有新版本（当前 v{current}，"
            f"最新 v{latest}）。更新：{UPDATE_URL}"
        )
    print(json.dumps(result, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
