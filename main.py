"""Emit the entry image for the make.fun ai-excited-01 judge.

The image lives in this repository as entry.png: a colossal blue whale
breaching straight up out of a tiny white teacup, water exploding
skyward, a spoon and two sugar cubes beside the cup for impossible
scale. This program places those exact bytes at
$MAKEFUN_OUTPUT_DIR/entry.png (default /output/entry.png) and checks
the result matches the source byte for byte, so the judge sees
precisely the image in this repository. The copy is deterministic:
both runs of this program write the same bytes.
"""

import os
import shutil
from pathlib import Path

IMAGE = "entry.png"


def main() -> None:
    here = Path(__file__).resolve().parent
    original = here / IMAGE
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    written = out_dir / IMAGE
    shutil.copyfile(original, written)
    assert written.read_bytes() == original.read_bytes(), "copy mismatch"
    print(f"wrote {written} ({written.stat().st_size} bytes)")


if __name__ == "__main__":
    main()
