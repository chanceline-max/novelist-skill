#!/usr/bin/env python3
"""Search the bundled novel-writing corpus without loading it all into a prompt."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("query", help="text or regular expression to search")
    parser.add_argument("--file", type=Path, default=Path(__file__).parents[1] / "references" / "writing-training-map.md")
    parser.add_argument("--context", type=int, default=2, help="matching lines of context")
    parser.add_argument("--max", type=int, default=30, help="maximum matching lines")
    parser.add_argument("--regex", action="store_true", help="interpret query as a regular expression")
    args = parser.parse_args()

    pattern = re.compile(args.query, re.I) if args.regex else None
    lines = args.file.read_text(encoding="utf-8").splitlines()
    hits = []
    for index, line in enumerate(lines):
        matched = bool(pattern.search(line)) if pattern else args.query.casefold() in line.casefold()
        if matched:
            start = max(0, index - args.context)
            end = min(len(lines), index + args.context + 1)
            hits.append((index + 1, start, end, lines[start:end]))
            if len(hits) >= args.max:
                break

    for number, start, end, block in hits:
        print(f"--- match at line {number} ---")
        for offset, text in enumerate(block, start=start + 1):
            print(f"{offset}: {text}")
    print(f"matches_shown={len(hits)} file={args.file}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
