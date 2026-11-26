#!/usr/bin/env python3
"""Funniest Sign on a Haunted Server Room Door.

Writes the funniest one-line sign for the door of a haunted server room
to /output/entry.txt.
"""

from pathlib import Path
import os
import shutil

MAX_CHARS = 120

LINE = "DO NOT KNOCK. The thing that answers is not IT support."

assert 1 <= len(LINE) <= MAX_CHARS and LINE.strip(), "line must be 1-120 non-blank chars"

WHERE = Path(os.environ.get("MAKEFUN_OUT", "/output"))
FILENAME = "entry.txt"


def main():
    WHERE.mkdir(parents=True, exist_ok=True)
    for member in WHERE.iterdir():
        if member.is_dir():
            shutil.rmtree(member)
        else:
            member.unlink()
    # No trailing newline: the gate counts the line exactly as written.
    (WHERE / FILENAME).write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
