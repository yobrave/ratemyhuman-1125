import json
import os

SCORE = "rmh3-stars"
ROOF = 200


def review(blob):
    for row in blob.replace("\r", "").split("\n"):
        if row.strip():
            return row
    return ""


def score_out(line):
    return 1 <= len(line) <= ROOF and line == line.strip()


def pin_review(line, root):
    board = os.environ.get("MAKEFUN_OUTPUT_DIR") or os.path.join(root, "output")
    os.makedirs(board, exist_ok=True)
    post = os.path.join(board, "entry.txt")
    ink = line.encode("utf-8")
    with open(post, "wb") as scribe:
        scribe.writelines([ink])
    if os.stat(post).st_size != len(ink):
        raise OSError("review pinned crooked")
    with open(post, "rb") as mirror:
        if mirror.read() != ink:
            raise OSError("review mirrored wrong")
    return post


root = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(root, "entry.txt"), encoding="utf-8") as feed:
    line = review(feed.read())

if not score_out(line):
    print(json.dumps({"rating": "unrated", "size": len(line)}))
    raise SystemExit(1)
post = pin_review(line, root)
print(json.dumps({"rating": "posted", "size": len(line), "roof": ROOF, "score": SCORE, "post": os.path.basename(post)}))
