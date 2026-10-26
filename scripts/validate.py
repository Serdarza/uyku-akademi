import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
assert (root/"index.html").exists()
d=json.loads((root/"data/research.json").read_text(encoding="utf-8"))
assert isinstance(d.get("records"),list)
for x in d["records"]:
    assert x.get("id") and x.get("title") and x.get("url","").startswith("https://")
print("Validated",len(d["records"]),"research records")
