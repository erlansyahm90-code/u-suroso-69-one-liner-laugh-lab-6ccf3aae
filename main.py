"""One-Liner Laugh Lab entry.

Writes a single short joke to the competition output path. The joke is a
robot vacuum's excuse after it has swallowed a sock: the machine blames its
own job description, which is exactly the kind of literal-minded defence a
dumb gadget would offer.

The output must be one line of 1-200 characters, written as plain UTF-8
with no trailing newline, so the file content is the line itself.
"""

from pathlib import Path

ENTRY = (
    "In my defense, the sock was on the floor, and my entire job "
    "description is 'eat what's on the floor.'"
)

OUTPUT_PATH = Path("/output/entry.txt")


def main() -> None:
    # Stay inside the competition's length gate before touching the disk.
    # The check runs first so a bad line never produces a partial file.
    assert 1 <= len(ENTRY) <= 200, "entry must be 1-200 characters"
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file should hold only the line itself.
    OUTPUT_PATH.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
