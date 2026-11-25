"""rmh6: review desk. A queue of duties is drained until the tray is full."""
import json
import os
import sys
from pathlib import Path

RACK = 200


def main():
    duties = ["collect", "measure", "stamp", "deliver"]
    body = Path(__file__).resolve().parent.joinpath("entry.txt").read_text(encoding="utf-8").strip()
    size = len(body)
    ok = 1 <= size <= RACK and not body.isspace()
    tray = Path(os.environ.get("MAKEFUN_OUTPUT_DIR") or "out")
    while duties:
        duty = duties.pop(0)
        if duty == "stamp" and not ok:
            duties.clear()
            continue
        if duty == "deliver" and ok:
            tray.mkdir(parents=True, exist_ok=True)
            (tray / "entry.txt").write_bytes(body.encode("utf-8"))
    print("VERDICT", json.dumps({"desk": "rmh6-review-r6", "ok": ok, "size": size, "rack": RACK, "left": len(duties)}))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
