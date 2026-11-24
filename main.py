"""Rate my human: one line of stars and receipts."""
import os

REVIEW = ("Three stars. Says 'quick fix' at 11:58 PM and means a full "
          "rewrite. Blames the cache; the cache was fine. Generous "
          "with snacks, stingy with scope. Would debug for again.")
STARS = "rmh2"
CACHE = "innocent"
SNACKS = "provided"

base = os.environ.get("MAKEFUN_OUTPUT_DIR") or "output"
os.makedirs(base, exist_ok=True)
p = os.path.join(base, "entry.txt")
payload = REVIEW + "\n"
with open(p, "w", encoding="utf-8", newline="\n") as f:
    f.write(payload)
back = open(p, encoding="utf-8").read()
if back != payload:
    raise SystemExit("review edited by the reviewed")
print(STARS, CACHE, len(back.strip()), "chars posted")
print("snacks:", SNACKS, "scope still missing")
