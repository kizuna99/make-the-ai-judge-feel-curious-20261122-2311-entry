"""Entry for make-the-ai-judge-feel-curious-20261122-2311.

This program writes one short text to entry.txt in the output
directory. The text is about a night nurse who hums a song no one
taught her, always stopping before the last line, because she is
waiting to hear how it ends.

The hook is the withheld last line. Nothing inside the text can
supply that ending, so the reader is left trying to hum the song
themselves -- the curiosity is participatory, and it keeps working
after the text ends. The scene is calm and concrete: a ward, a
verse repeated for thirty years, and a wait that is still going.
"""

import os
from pathlib import Path

TEXT = (
    "The night nurse hums a song no one taught her, always the same "
    "verse, always stopping before the last line. A patient once asked "
    "her why. I am waiting to hear how it ends, she said. She has "
    "worked the ward for thirty years. She is still waiting."
)


def main() -> None:
    if not (1 <= len(TEXT) <= 280) or not TEXT.strip():
        raise SystemExit("TEXT is outside the 1-280 code point gate")
    output_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output")
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
