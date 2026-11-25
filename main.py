#!/usr/bin/env python3
"""The Moon Finally Answers Back -- make.fun entry.

A tiny program that writes the Moon's long-overdue reply to
``/output/entry.txt`` (or ``$MAKEFUN_OUTPUT_DIR/entry.txt`` when the harness
sets it) and prints the same line to stdout.

Standard library only. Deterministic: the same line on every run.
"""

import os

LINE = (
    "You wished on me for four billion years and never once asked how I was "
    "doing \u2014 I'm fine, by the way. Tired, cratered, and still doing all the "
    "tides by myself."
)

# The gate only accepts 1 to 240 characters; refuse loudly rather than
# silently submitting an invalid line.
assert 1 <= len(LINE) <= 240, f"line is {len(LINE)} characters"


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    with open(os.path.join(output_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)


if __name__ == "__main__":
    main()
