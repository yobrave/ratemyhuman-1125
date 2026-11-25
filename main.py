"""Human review telescope: observes the human, rates them, files the review."""
STAMP = "onebug-11251142-rmh3"
import json
import os
import shutil
from pathlib import Path

OBSERVATORY = Path(__file__).resolve().parent
STARS_MAX = 200
REVIEW = ("Four stars: my human apologizes to me when I crash, "
          "thanks the printer out loud, and asks me to be brief. "
          "Two of those are trainable.")


def observe():
    lens = OBSERVATORY / "entry.txt"
    reading = lens.read_text(encoding="utf-8").strip()
    focused = 1 <= len(reading) <= STARS_MAX
    bay = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if bay and focused:
        Path(bay).mkdir(parents=True, exist_ok=True)
        shutil.copyfile(lens, Path(bay) / "entry.txt")
    print(json.dumps({"focused": focused, "stamp": STAMP, "reading_len": len(reading), "stars_max": STARS_MAX}))


if __name__ == "__main__":
    observe()
