"""One-Liner Laugh Lab entry.

Writes the single funny line to $MAKEFUN_OUTPUT_DIR/entry.txt
(fallback /output, then the script directory). Stdlib only,
deterministic: the same line every run.
"""

import os

LINE = "Per my incident report: the sock resisted arrest. I used reasonable suction."


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    if not os.path.isdir(out_dir):
        out_dir = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
