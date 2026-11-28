"""Select candidate prospects from Find a Tender award data: SME suppliers that won work from English NHS bodies
through a process where a Carbon Reduction Plan is (or from 1 April 2027 will be) a pass/fail requirement.
Usage: python3 candidates.py OUT.csv IN1.jsonl [IN2.jsonl ...]"""
import collections, csv, json, re, sys
out, files = sys.argv[1], sys.argv[2:]
NOT_ENGLAND = re.compile(r"scotland|scottish|wales|welsh|cymru|health board|lanarkshire|glasgow|lothian|grampian|tayside|highland|fife|ayrshire|borders|"
                         r"dumfries|forth valley|orkney|shetland|western isles|velindre|common services agency|business services organisation|"
                         r"northern ireland|belfast|golden jubilee|healthcare improvement", re.I)
NHS = re.compile(r"\bnhs\b|supply chain coordination|healthtrust europe|integrated care board|foundation trust|ambulance service", re.I)
DIRECT = re.compile(r"direct award|without (prior )?(publication|call)|veat|negotiated without|process [ab]\b|single tender", re.I)
def english_nhs(r):
    b = r.get("buyer") or ""
    return bool(NHS.search(b)) and not NOT_ENGLAND.search(b)
rows = []
for f in files:
    for l in open(f):
        try: rows.append(json.loads(l))
        except ValueError: pass
seen = set(); dedup = []
for r in rows:
    k = (r["rel"], (r.get("supplier") or "").lower())
    if k not in seen:
        seen.add(k); dedup.append(r)
rows = dedup
stats = collections.Counter()
by = collections.defaultdict(list)
for r in rows:
    if not english_nhs(r): continue
    stats["english_nhs_rows"] += 1
    if r.get("scale") != "sme": stats["not_sme"] += 1; continue
    md = (r.get("method_details") or "") + " " + (r.get("method") or "") + " " + (r.get("title") or "")
    direct = bool(DIRECT.search(md)) or r.get("method") in ("direct", "limited")
    key = (r.get("coh") or "").strip().upper() if r.get("scheme") == "GB-COH" and r.get("coh") else "NAME:" + re.sub(r"[^a-z0-9]+", " ", (r.get("supplier") or "").lower()).strip()
    r["_direct"] = direct
    by[key].append(r)
cands = []
for key, rs in by.items():
    comp = [r for r in rs if not r["_direct"]]
    stats["sme_suppliers"] += 1
    if not comp: stats["only_direct_awards"] += 1; continue
    fw = [r for r in comp if r.get("framework")]
    ends = sorted(e for e in (r.get("ends") for r in comp) if e)
    url = next((r["url"] for r in rs if r.get("url")), "")
    best = max(comp, key=lambda r: r.get("date") or "")
    cands.append({"id": key, "supplier": best.get("supplier"), "coh": key if not key.startswith("NAME:") else "", "town": best.get("town") or "", "postcode": best.get("postcode") or "",
                  "url": url, "fts_email": next((r["email"] for r in rs if r.get("email")), ""),
                  "n_awards": len(comp), "n_framework_awards": len(fw), "latest_award": best.get("date"), "latest_notice": best.get("rel"),
                  "latest_buyer": best.get("buyer"), "latest_title": best.get("title"), "cpv": best.get("cpv_desc") or "", "category": best.get("cat") or "",
                  "method": (best.get("method_details") or best.get("method") or ""), "next_end": next((e for e in ends if e >= "2026-11-27"), ends[-1] if ends else ""),
                  "max_value": max((r.get("value") or 0) for r in comp),
                  "basis": "NHS framework (full plan required for new frameworks)" if fw else "NHS competitive contract (full plan required from 1 Apr 2027)"})
with open(out, "w", newline="") as f:
    w = csv.DictWriter(f, fieldnames=list(cands[0].keys())); w.writeheader(); w.writerows(cands)
stats["candidates"] = len(cands); stats["with_url"] = sum(1 for c in cands if c["url"]); stats["with_coh"] = sum(1 for c in cands if c["coh"])
stats["framework_basis"] = sum(1 for c in cands if c["n_framework_awards"])
print(dict(stats))
print("category:", collections.Counter(c["category"] for c in cands).most_common(5))
print("top cpv:", collections.Counter(c["cpv"] for c in cands).most_common(14))
print("method:", collections.Counter(c["method"][:50] for c in cands).most_common(10))
print("with url by basis:", collections.Counter((c["basis"][:14], bool(c["url"])) for c in cands))
