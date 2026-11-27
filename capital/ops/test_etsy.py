"""Offline test of the Etsy client: idempotent draft creation and request shapes (no network)."""
import json, os, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
os.environ.update({"ETSY_API_KEY": "k", "ETSY_SHARED_SECRET": "s", "ETSY_SHOP_ID": "123"})
import etsy

class Resp:
    def __init__(self, data, code=200): self.status_code, self._d, self.content, self.text = code, data, b"x", json.dumps(data)
    def json(self): return self._d

class FakeSession:
    def __init__(self): self.headers, self.calls, self.next_id = {}, [], 1000
    def request(self, method, url, **kw):
        self.calls.append((method, url, kw))
        if method == "GET" and url.endswith("/listings"):
            st = kw["params"]["state"]
            res = [{"title": json.load(open(Path(__file__).parent.parent / "listings/plan.json"))["listings"][0]["title"]}] if st == "active" else []
            return Resp({"count": len(res), "results": res})
        if method == "POST" and url.endswith("/listings"):
            self.next_id += 1
            return Resp({"listing_id": self.next_id})
        return Resp({"ok": True})

fs = FakeSession()
client = etsy.Etsy(session=fs, token="t")
assert fs.headers["x-api-key"] == "k:s" and fs.headers["Authorization"] == "Bearer t"
created = etsy.create_drafts(str(Path(__file__).parent.parent / "listings/plan.json"), client=client)
assert len(created) == 2, created  # first listing already active -> skipped
posts = [c for c in fs.calls if c[0] == "POST"]
assert sum(1 for c in posts if c[1].endswith("/images")) == 8
assert sum(1 for c in posts if c[1].endswith("/files")) == 6
draft = [c for c in posts if c[1].endswith("/listings")][0][2]["data"]
assert draft["type"] == "download" and draft["who_made"] == "i_did"
assert not any(c[0] in ("PATCH", "PUT") for c in fs.calls), "must never publish"
v, ch = etsy.pkce_pair(); assert len(v) >= 43 and len(ch) == 43
print("etsy client offline tests: PASS")
