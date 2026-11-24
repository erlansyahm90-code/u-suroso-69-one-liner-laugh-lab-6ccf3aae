"""One-Liner Laugh Lab entry.

Writes a single one-liner joke to /output/entry.txt. The joke is a robot
vacuum's legal defense for eating a sock, citing its job description and
its owner's long sock-dropping record.
"""

import os

ENTRY = (
    "In my defense, the sock was on the floor. "
    "My job description says 'eat what's on the floor,' "
    "and Dave has left 312 socks there since March."
)


def main():
    # Create the output directory if it does not exist yet.
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
