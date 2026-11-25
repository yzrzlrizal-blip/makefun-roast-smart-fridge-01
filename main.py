#!/usr/bin/env python3
"""Roast the Smart Fridge: one line, best laugh wins.

Writes a single roast of the smart fridge to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output/entry.txt). The line is one sentence, 1-160 UTF-8
characters, no trailing newline.
"""

import os
from pathlib import Path

ROAST = "My smart fridge tattled to my fitness app about the 2 a.m. cheesecake, then locked the freezer and asked me to rate my willpower on a scale of one to salad."


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(ROAST, encoding="utf-8")


if __name__ == "__main__":
    main()
