#!/usr/bin/env python3
"""The Router Confesses.

Writes a single original one-line excuse from a home Wi-Fi router for
dropping the connection at the climax of a movie to /output/entry.txt.

The gate requires UTF-8 text of 1 to 200 characters, not only white
space, so the program checks the length before writing and prints the
character count for the log.
"""

import os
import sys

# One line, in the router's own voice: a petty, jealous appliance that
# dropped the connection because the movie was getting all the
# attention. Setup in the first clause, smug punchline in the second.
# Avoids the obvious buffering / bandwidth / firmware-update jokes.
ROAST = "I dropped the connection at the climax because the movie was getting all the attention, and frankly, so should I."


def main() -> int:
    text = ROAST.strip()
    if not text or len(text) > 200:
        print(f"entry invalid: {len(text)} characters", file=sys.stderr)
        return 1
    output_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
