#!/usr/bin/env python3
"""Entry for make.fun's "Make the AI judge feel curious" bounty.

The program writes one short text to the output directory's entry.txt.
The text is a small, calm mystery: a night nurse who hums a song no one
taught her and always stops before the last line, because she is waiting
to hear how it ends. The withheld last line is the hook — a reader is
left trying to hum it for themselves.
"""

import os
from pathlib import Path

TEXT = (
    "The night nurse hums a song no one taught her, always the same verse, "
    "always stopping before the last line. A patient once asked her why. "
    "I am waiting to hear how it ends, she said. She has worked the ward "
    "for thirty years. She is still waiting."
)


def main() -> None:
    # The bounty's gate: UTF-8 text of 1 to 280 characters (Unicode code
    # points), not only white space. Fail loudly rather than hand in a
    # text the gate would refuse.
    if not 1 <= len(TEXT) <= 280 or not TEXT.strip():
        raise SystemExit("entry text is outside the 1-280 character gate")
    output = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output.mkdir(parents=True, exist_ok=True)
    (output / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
