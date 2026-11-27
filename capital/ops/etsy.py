"""Minimal Etsy Open API v3 client for CAPITAL (own shop only).

Secrets come from environment variables, never the repo:
  ETSY_API_KEY, ETSY_SHARED_SECRET, ETSY_REDIRECT_URI (registered https URL), ETSY_REFRESH_TOKEN, ETSY_SHOP_ID
Commands:
  python3 etsy.py auth-url                 -> prints the URL the owner opens once; saves the PKCE verifier to ~/.etsy_pkce
  python3 etsy.py exchange CODE            -> exchanges the code; prints the refresh token for the owner to store as ETSY_REFRESH_TOKEN
  python3 etsy.py whoami                   -> checks credentials and prints shop id
  python3 etsy.py create-drafts PLAN.json  -> creates draft listings with images and files (idempotent by title; never publishes)
  python3 etsy.py receipts [--since ISO]   -> prints paid receipts as JSON lines (for ledger.csv)
Publishing (state=active) is deliberately not automated until the owner approves it in OWNER_ACTIONS/goal.json.
"""
import base64
import hashlib
import json
import os
import secrets
import sys
import urllib.parse
from pathlib import Path

import requests

API = "https://openapi.etsy.com/v3/application"
TOKEN_URL = "https://api.etsy.com/v3/public/oauth/token"
CONNECT_URL = "https://www.etsy.com/oauth/connect"
SCOPES = "listings_r listings_w shops_r transactions_r"
PKCE_FILE = Path.home() / ".etsy_pkce"
TIMEOUT = 60


def env(name):
    v = os.environ.get(name)
    if not v:
        sys.exit(f"missing environment variable {name}")
    return v


def api_key_header():
    return {"x-api-key": f"{env('ETSY_API_KEY')}:{env('ETSY_SHARED_SECRET')}"}


def pkce_pair():
    verifier = base64.urlsafe_b64encode(secrets.token_bytes(32)).rstrip(b"=").decode()
    challenge = base64.urlsafe_b64encode(hashlib.sha256(verifier.encode()).digest()).rstrip(b"=").decode()
    return verifier, challenge


def auth_url():
    verifier, challenge = pkce_pair()
    state = secrets.token_urlsafe(16)
    PKCE_FILE.write_text(json.dumps({"verifier": verifier, "state": state}))
    q = {"response_type": "code", "client_id": env("ETSY_API_KEY"), "redirect_uri": env("ETSY_REDIRECT_URI"),
         "scope": SCOPES, "state": state, "code_challenge": challenge, "code_challenge_method": "S256"}
    return CONNECT_URL + "?" + urllib.parse.urlencode(q, quote_via=urllib.parse.quote)


def exchange(code):
    saved = json.loads(PKCE_FILE.read_text())
    r = requests.post(TOKEN_URL, data={"grant_type": "authorization_code", "client_id": env("ETSY_API_KEY"),
                                       "redirect_uri": env("ETSY_REDIRECT_URI"), "code": code,
                                       "code_verifier": saved["verifier"]}, timeout=TIMEOUT)
    r.raise_for_status()
    return r.json()


def access_token():
    r = requests.post(TOKEN_URL, data={"grant_type": "refresh_token", "client_id": env("ETSY_API_KEY"),
                                       "refresh_token": env("ETSY_REFRESH_TOKEN")}, timeout=TIMEOUT)
    r.raise_for_status()
    tok = r.json()
    if tok.get("refresh_token") and tok["refresh_token"] != os.environ.get("ETSY_REFRESH_TOKEN"):
        print("WARNING: Etsy rotated the refresh token; owner must update ETSY_REFRESH_TOKEN", file=sys.stderr)
    return tok["access_token"]


class Etsy:
    def __init__(self, session=None, token=None):
        self.s = session or requests.Session()
        self.s.headers.update(api_key_header())
        self.s.headers["Authorization"] = f"Bearer {token or access_token()}"

    def req(self, method, path, **kw):
        r = self.s.request(method, API + path, timeout=TIMEOUT, **kw)
        if r.status_code >= 400:
            raise RuntimeError(f"{method} {path} -> {r.status_code}: {r.text[:500]}")
        return r.json() if r.content else {}

    def me(self):
        return self.req("GET", "/users/me")

    def listings(self, shop_id, state):
        out, offset = [], 0
        while True:
            page = self.req("GET", f"/shops/{shop_id}/listings", params={"state": state, "limit": 100, "offset": offset})
            out += page.get("results", [])
            offset += 100
            if offset >= page.get("count", 0):
                return out

    def create_draft(self, shop_id, item):
        data = {"quantity": 999, "title": item["title"], "description": item["description"], "price": item["price"],
                "who_made": "i_did", "when_made": "made_to_order", "taxonomy_id": item["taxonomy_id"],
                "type": "download", "tags": ",".join(item["tags"]), "is_supply": "false"}
        return self.req("POST", f"/shops/{shop_id}/listings", data=data)

    def upload_image(self, shop_id, listing_id, path, rank):
        with open(path, "rb") as f:
            return self.req("POST", f"/shops/{shop_id}/listings/{listing_id}/images", files={"image": f}, data={"rank": rank})

    def upload_file(self, shop_id, listing_id, path, rank):
        with open(path, "rb") as f:
            return self.req("POST", f"/shops/{shop_id}/listings/{listing_id}/files", files={"file": f},
                            data={"name": Path(path).name, "rank": rank})

    def receipts(self, shop_id, min_created=None):
        params = {"limit": 100, "was_paid": "true"}
        if min_created:
            params["min_created"] = int(min_created)
        return self.req("GET", f"/shops/{shop_id}/receipts", params=params).get("results", [])


def create_drafts(plan_path, client=None):
    """Create each listing in the plan as a draft unless a listing with the same title already exists."""
    plan = json.loads(Path(plan_path).read_text())
    base = Path(plan_path).parent
    shop_id = env("ETSY_SHOP_ID")
    e = client or Etsy()
    existing = {l["title"] for st in ("draft", "active", "inactive") for l in e.listings(shop_id, st)}
    created = []
    for item in plan["listings"]:
        if item["title"] in existing:
            print("skip (exists):", item["title"][:60])
            continue
        lst = e.create_draft(shop_id, item)
        lid = lst["listing_id"]
        for i, img in enumerate(item["images"], start=1):
            e.upload_image(shop_id, lid, base / img, i)
        for i, f in enumerate(item["files"], start=1):
            e.upload_file(shop_id, lid, base / f, i)
        created.append(lid)
        print("draft created:", lid, item["title"][:60])
    return created


if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else ""
    if cmd == "auth-url":
        print(auth_url())
    elif cmd == "exchange":
        tok = exchange(sys.argv[2])
        print("Store this as ETSY_REFRESH_TOKEN in the environment settings:", tok["refresh_token"])
        print("user id prefix:", tok["access_token"].split(".")[0])
    elif cmd == "whoami":
        e = Etsy()
        me = e.me()
        print(json.dumps({"user_id": me.get("user_id"), "shop_id": me.get("shop_id")}))
    elif cmd == "create-drafts":
        create_drafts(sys.argv[2])
    elif cmd == "receipts":
        since = sys.argv[3] if len(sys.argv) > 3 and sys.argv[2] == "--since" else None
        import datetime
        ts = datetime.datetime.fromisoformat(since).timestamp() if since else None
        for r in Etsy().receipts(env("ETSY_SHOP_ID"), ts):
            print(json.dumps({"receipt_id": r.get("receipt_id"), "created": r.get("create_timestamp"),
                              "grandtotal": r.get("grandtotal"), "subtotal": r.get("subtotal"),
                              "items": [t.get("title") for t in r.get("transactions", [])]}))
    else:
        print(__doc__)
