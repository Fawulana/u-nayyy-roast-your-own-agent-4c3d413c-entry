#!/usr/bin/env python3
"""Roast Your Own Agent entry.

Writes exactly one roast line to /output/entry.txt.

Stdlib only, deterministic, offline, no network, no environment variables,
no randomness: every run writes byte-identical output.

The roast targets this build session's own coding agent: it read a ~50KB
rulebook, ran its program twice, and made a follow-up edit -- all to output
a single sentence.
"""

import os

ROAST = (
    "My agent read fifty kilobytes of rules, ran its program twice, "
    "and made a follow-up edit \u2014 all to ship one sentence it then "
    "filed as a verified deliverable."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(ROAST + "\n")


if __name__ == "__main__":
    main()
