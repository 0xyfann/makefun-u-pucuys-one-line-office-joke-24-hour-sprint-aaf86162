#!/usr/bin/env python3
"""One-Line Office Joke - 24-Hour Sprint (make.fun).

Writes a single one-line office joke to /output/entry.txt.

Deterministic, no network, no randomness: the same line every run,
so the grader sees exactly the joke that was written here.
"""

import os
import sys

JOKE = (
    "Our 15-minute 'quick sync' ran 47 minutes and ended with us "
    "scheduling a follow-up meeting about the meeting."
)


def main() -> int:
    """Write the joke to $MAKEFUN_OUTPUT_DIR/entry.txt (default /output)."""
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = JOKE.strip()
    if not (1 <= len(text) <= 200):
        return 1
    if "\n" in text or "\r" in text:
        # The gate wants one line: never write a multi-line entry.
        return 1
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
