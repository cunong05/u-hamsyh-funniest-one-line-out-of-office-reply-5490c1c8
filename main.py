#!/usr/bin/env python3
"""Funniest One-Line Out-of-Office Reply — make.fun bounty.

Writes a single funny out-of-office reply to /output/entry.txt.
The entry must be exactly one line, 1-160 characters, UTF-8.
"""

import os

ENTRY = (
    "I'm away until Monday — my inbox is on holiday too, "
    "and unlike me, it won't be checking email."
)


def main():
    output_dir = "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")
    print(f"Wrote {len(ENTRY)} characters to {path}")


if __name__ == "__main__":
    main()
