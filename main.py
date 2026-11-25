#!/usr/bin/env python3
"""Funniest one-line out-of-office reply — make.fun bounty entry.

Running this script writes exactly one funny out-of-office line to
/output/entry.txt. The scorer only accepts a valid entry, so the
script checks its own output against the bounty gate before it
finishes: UTF-8 text, a single line, between 1 and 160 characters,
and more than just whitespace.

The joke: instead of the tired "my inbox is on holiday" line, the
sender has forwarded every urgent email to Future Me — who is
ignoring them too. It reads like a real auto-reply, lands on the
first read, and needs no setup or explanation.
"""

from pathlib import Path

OUT_PATH = Path("/output/entry.txt")

REPLY = (
    "I'm away until Monday — I've forwarded all urgent emails "
    "to Future Me, and he's ignoring them too."
)


def check_gate(text: str) -> None:
    """Raise if the entry would fail the closed scorer's gate."""
    if not text or not text.strip():
        raise ValueError("entry is empty or only whitespace")
    if "\n" in text or "\r" in text:
        raise ValueError("entry must be exactly one line")
    if not 1 <= len(text) <= 160:
        raise ValueError(f"entry is {len(text)} chars, must be 1-160")


def main() -> None:
    check_gate(REPLY)
    OUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUT_PATH.write_text(REPLY + "\n", encoding="utf-8")
    print(f"Wrote entry ({len(REPLY)} chars) to {OUT_PATH}")


if __name__ == "__main__":
    main()
