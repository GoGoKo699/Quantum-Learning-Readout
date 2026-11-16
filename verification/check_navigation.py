#!/usr/bin/env python3
"""Check repository-local Markdown navigation and the thirty-milestone map.

This source check does not establish mathematical correctness or hosted rendering.
"""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import html
import json
from pathlib import Path
import re
import unicodedata
from urllib.parse import unquote, urlsplit


def visible_markdown(text: str) -> tuple[str, bool]:
    """Remove fenced blocks while reporting an unclosed fence."""
    rows = []
    fence = None
    for row in text.splitlines():
        match = re.match(r"^ {0,3}(`{3,}|~{3,})", row)
        if match:
            token = match.group(1)
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence):
                fence = None
            rows.append("")
        else:
            rows.append(row if fence is None else "")
    return "\n".join(rows), fence is None


def slug(text: str) -> str:
    text = html.unescape(re.sub(r"<[^>]+>", "", text)).strip().lower()
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = text.replace("`", "")
    text = "".join(c for c in text
                   if c in "-_ " or unicodedata.category(c)[0] not in "PS")
    return text.replace(" ", "-")


def anchors(text: str) -> set[str]:
    result = set(re.findall(r'<a\s+(?:id|name)=["\']([^"\']+)["\']', text))
    seen: dict[str, int] = {}
    for match in re.finditer(r"^ {0,3}#{1,6}\s+(.+?)\s*#*\s*$", text, re.MULTILINE):
        base = slug(match.group(1))
        count = seen.get(base, 0)
        result.add(base if count == 0 else f"{base}-{count}")
        seen[base] = count + 1
    return result


def destinations(text: str) -> list[str]:
    # The scientific account uses ordinary inline links; reference definitions
    # are included as destinations too, should that notation be introduced.
    plain = re.sub(r"(`+).*?\1", "", text)
    inline = re.findall(r"\[[^\]]*\]\((<[^>]+>|[^\s)]+)(?:\s+[^)]*)?\)", plain)
    defined = re.findall(r"^ {0,3}\[[^\]]+\]:\s*(<[^>]+>|\S+)", plain, re.MULTILINE)
    return [value[1:-1] if value.startswith("<") else value for value in inline + defined]


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path,
                        default=Path(__file__).with_name("structure_results.json"))
    args = parser.parse_args()
    root = Path(__file__).resolve().parents[1]
    files = sorted(path for path in root.rglob("*.md") if ".git" not in path.parts)
    errors = []
    texts = {}
    anchor_map = {}
    for path in files:
        text, balanced = visible_markdown(path.read_text(encoding="utf-8"))
        texts[path] = text
        anchor_map[path] = anchors(text)
        if not balanced:
            errors.append(f"{path.relative_to(root)}: unclosed fenced block")
    checked = 0
    for source, text in texts.items():
        for destination in destinations(text):
            parsed = urlsplit(destination)
            if parsed.scheme or parsed.netloc:
                continue
            target = (source.parent / unquote(parsed.path)).resolve() if parsed.path else source
            checked += 1
            if not target.is_relative_to(root):
                errors.append(f"{source.relative_to(root)}: destination leaves repository {destination}")
                continue
            if not target.exists():
                errors.append(f"{source.relative_to(root)}: missing destination {destination}")
            elif parsed.fragment and target.suffix.lower() == ".md":
                if unquote(parsed.fragment) not in anchor_map.get(target, set()):
                    errors.append(f"{source.relative_to(root)}: missing heading {destination}")
    map_path = root / "learning/MILESTONES.md"
    milestone_ids = []
    if map_path.exists():
        milestone_ids = re.findall(r"^#{2,6}\s+(M\d{2})\b", texts[map_path], re.MULTILINE)
    expected = [f"M{i:02d}" for i in range(1, 31)]
    if milestone_ids != expected:
        errors.append("learning/MILESTONES.md: milestone headings must be M01 through M30, once each in order")
    report = {
        "status": "passed" if not errors else "failed",
        "generated_at_utc": datetime.now(timezone.utc).isoformat(),
        "script_sha256": hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),
        "markdown_files": len(files), "checked_local_links": checked,
        "markdown_sha256": {str(path.relative_to(root)): hashlib.sha256(path.read_bytes()).hexdigest()
                            for path in files},
        "milestone_headings": milestone_ids, "errors": errors,
        "scope": "All current Markdown files: repository-local destinations, Markdown heading fragments, fenced-block balance, and exactly thirty ordered M01–M30 milestone headings. External links, scientific truth, pedagogical quality, and actual hosted mathematics/layout are outside this check.",
    }
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items()
                      if key not in ("milestone_headings", "markdown_sha256", "scope", "script_sha256", "generated_at_utc")}))
    if errors:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
