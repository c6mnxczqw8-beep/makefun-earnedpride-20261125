#!/usr/bin/env python3
"""Entry program for One Line of Earned Pride.

Writes one line (1 to 240 characters) to the output directory
(MAKEFUN_OUTPUT_DIR, default /output) as entry.txt: a quiet,
earned moment of pride for someone in a concrete scene. He
re-taught himself to tie his shoes at 71, one-handed, and
refused the applause.
"""

import os

LINE = (
    "At 58, after the night shift, she finally passed "
    "the exam she had failed at 19 -- and framed the "
    "certificate beside her daughter's, at the same "
    "height."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
