"""The Funniest Sick-Day Excuse entry: the cat did the research."""

import os

EXCUSE = (
    "I can't come in — my cat sat on my laptop, opened 40 tabs of "
    "'how to fake a fever,' and honestly the research deserves a field test."
)

CHAR_COUNT = len(EXCUSE)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(EXCUSE + "\n")
    print(f"wrote {path} ({CHAR_COUNT} characters)")


if __name__ == "__main__":
    main()
