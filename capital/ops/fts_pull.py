"""Pull Find a Tender award-stage OCDS releases and write one slim JSON line per (release, supplier).
Usage: python3 fts_pull.py OUT.jsonl UPDATED_FROM(YYYY-MM-DD) [MAX_PAGES]
Open data under the Open Government Licence. Read-only, one request at a time."""
import json, sys, time, requests
out, start = sys.argv[1], sys.argv[2]
max_pages = int(sys.argv[3]) if len(sys.argv) > 3 else 400
url = f"https://www.find-tender.service.gov.uk/api/1.0/ocdsReleasePackages?stages=award&limit=100&updatedFrom={start}T00:00:00" + (f"&updatedTo={sys.argv[4]}T00:00:00" if len(sys.argv) > 4 else "")
UA = {"User-Agent": "CAPITAL research (read-only)"}
n_rel = n_rows = 0
with open(out, "w") as f:
    for page in range(max_pages):
        for attempt in range(5):
            try:
                r = requests.get(url, headers=UA, timeout=90)
                if r.status_code == 200:
                    break
                time.sleep(10 * (attempt + 1))
            except requests.RequestException:
                time.sleep(10 * (attempt + 1))
        else:
            print("giving up at page", page, flush=True); break
        d = r.json()
        for rel in d.get("releases", []):
            n_rel += 1
            t = rel.get("tender") or {}
            parties = {p.get("id"): p for p in rel.get("parties", [])}
            buyers = [p for p in rel.get("parties", []) if "buyer" in (p.get("roles") or [])]
            b = buyers[0] if buyers else {}
            ends, values = [], []
            for c in rel.get("contracts", []) or []:
                if (c.get("period") or {}).get("endDate"): ends.append(c["period"]["endDate"][:10])
                if (c.get("value") or {}).get("amount"): values.append(c["value"]["amount"])
            for a in rel.get("awards", []) or []:
                if (a.get("contractPeriod") or {}).get("endDate"): ends.append(a["contractPeriod"]["endDate"][:10])
                if (a.get("value") or {}).get("amount"): values.append(a["value"]["amount"])
            sup_ids = {s.get("id") for a in rel.get("awards", []) or [] for s in a.get("suppliers", []) or []}
            for p in rel.get("parties", []):
                if "supplier" not in (p.get("roles") or []) and p.get("id") not in sup_ids:
                    continue
                ident = p.get("identifier") or {}
                det = p.get("details") or {}
                addr = p.get("address") or {}
                cp = p.get("contactPoint") or {}
                f.write(json.dumps({
                    "rel": rel.get("id"), "date": (rel.get("date") or "")[:10], "title": (t.get("title") or "")[:140],
                    "cpv": (t.get("classification") or {}).get("id"), "cpv_desc": (t.get("classification") or {}).get("description"),
                    "cat": t.get("mainProcurementCategory"), "framework": bool((t.get("techniques") or {}).get("hasFrameworkAgreement")),
                    "legal": (t.get("legalBasis") or {}).get("id"), "method": t.get("procurementMethod"), "method_details": t.get("procurementMethodDetails"),
                    "tags": rel.get("tag"), "award_date": next((a.get("date", "")[:10] for a in rel.get("awards", []) or [] if a.get("date")), None),
                    "street": addr.get("streetAddress"),
                    "buyer": b.get("name"), "buyer_scheme": (b.get("identifier") or {}).get("scheme"),
                    "buyer_class": [c.get("id") for c in (b.get("details") or {}).get("classifications", []) or []],
                    "supplier": p.get("name"), "scheme": ident.get("scheme"), "coh": ident.get("id"), "scale": det.get("scale"),
                    "url": det.get("url") or cp.get("url"), "email": cp.get("email"), "town": addr.get("locality"), "postcode": addr.get("postalCode"),
                    "country": addr.get("country") or addr.get("countryName"), "n_suppliers": len(sup_ids), "ends": max(ends) if ends else None,
                    "value": max(values) if values else None}) + "\n")
                n_rows += 1
        nxt = (d.get("links") or {}).get("next")
        if page % 10 == 0:
            print(f"page {page} releases {n_rel} rows {n_rows}", flush=True)
        if not nxt or not d.get("releases"):
            break
        url = nxt
        time.sleep(1.0)
print(f"DONE releases {n_rel} rows {n_rows}", flush=True)
