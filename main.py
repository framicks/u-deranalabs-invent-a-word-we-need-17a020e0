#!/usr/bin/env python3
"""Invent a Word We Need — writes the entry to /output/entry.txt.

The entry is one invented English word with a one-line definition.
Deterministic: the same bytes are written on every run.
No network access, no external files: everything is in this file.
"""

import os

ENTRY = "showerwit (n.) \u2014 the perfect reply you think of in the shower, hours after the argument ended."

OUTPUT_PATH = "/output/entry.txt"


def main() -> None:
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
