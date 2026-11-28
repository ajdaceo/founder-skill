"""Build a category "renewals calendar" from Contracts Finder award notices (Open Government Licence v3.0).

Usage: python3 cf_report.py OUT_DIR SLUG "phrase one" ["phrase two" ...] [--from 2020-01-01] [--today YYYY-MM-DD]
Writes OUT_DIR/SLUG-calendar.csv (one row per awarded contract), OUT_DIR/SLUG-suppliers.csv and OUT_DIR/SLUG-summary.json.
A notice is included when its title contains one of the phrases. Read-only; one request per phrase.
The full calendar is the paid product: keep OUT_DIR outside the public repository.
"""
import csv
import datetime as dt
import html
import json
import os
import re
import statistics
import sys
import time

import requests

URL = "https://www.contractsfinder.service.gov.uk/api/rest/2/search_notices/json"
NOTICE = "https://www.contractsfinder.service.gov.uk/notice/"


def search(phrase, frm, to=None):
    crit = {"types": ["Contract"], "statuses": ["Awarded"], "keyword": f'"{phrase}"', "publishedFrom": frm + "T00:00:00"}
    if to:
        crit["publishedTo"] = to + "T23:59:59"
    r = requests.post(URL, json={"searchCriteria": crit, "size": 1000}, headers={"Accept": "application/json", "User-Agent": "CAPITAL research (read-only)"}, timeout=120)
    r.raise_for_status()
    d = r.json()
    return d.get("hitCount", 0), [x.get("item", x) for x in d.get("noticeList", [])]


def search_all(phrase, frm, today):
    """Year-by-year windows so no search hits the 1,000-result ceiling."""
    hits_total, items, truncated = 0, [], []
    start = dt.date.fromisoformat(frm)
    while start <= today:
        end = min(dt.date(start.year, 12, 31), today)
        hits, got = search(phrase, start.isoformat(), end.isoformat())
        hits_total += hits
        items += got
        if hits > len(got):
            truncated.append((phrase, start.year, hits, len(got)))
        start = dt.date(start.year + 1, 1, 1)
        time.sleep(0.8)
    return hits_total, items, truncated


def norm(s):
    s = re.sub(r"\b(limited|ltd|llp|plc|uk|group|the)\b\.?", " ", (s or "").lower().replace("&", " and "))
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def months_between(a, b):
    return round((b - a).days / 30.44, 1)


def build(out_dir, slug, phrases, frm, today):
    os.makedirs(out_dir, exist_ok=True)
    seen, rows, truncated = set(), [], []
    for ph in phrases:
        hits, items, trunc = search_all(ph, frm, today)
        truncated += trunc
        for i in items:
            title = i.get("title") or ""
            if ph.lower() not in title.lower() or not i.get("awardedSupplier"):
                continue
            end = (i.get("end") or "")[:10]
            key = (norm(i.get("organisationName")), norm(i.get("awardedSupplier")), end, round(i.get("awardedValue") or 0))
            if key in seen:
                continue
            seen.add(key)
            start = (i.get("start") or "")[:10]
            try:
                end_d = dt.date.fromisoformat(end)
                to_end = months_between(today, end_d)
                term = months_between(dt.date.fromisoformat(start), end_d) if start else ""
            except ValueError:
                to_end, term = "", ""
            rows.append({"buyer": html.unescape(i.get("organisationName") or ""), "contract": html.unescape(re.sub(r"\s+", " ", title).strip()), "incumbent_supplier": html.unescape(i.get("awardedSupplier") or ""),
                         "supplier_is_sme": "yes" if i.get("awardedToSme") else "no", "awarded_value_gbp": i.get("awardedValue") or "",
                         "awarded_date": (i.get("awardedDate") or "")[:10], "contract_start": start, "contract_end": end, "term_months": term,
                         "months_until_end": to_end, "region": i.get("regionText") or i.get("region") or "", "buyer_postcode": i.get("postcode") or "",
                         "source_notice": NOTICE + str(i.get("id")), "published": (i.get("publishedDate") or "")[:10]})
    rows.sort(key=lambda r: (r["contract_end"] or "9999"))
    with open(os.path.join(out_dir, f"{slug}-calendar.csv"), "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()))
        w.writeheader()
        w.writerows(rows)
    live = [r for r in rows if r["months_until_end"] != "" and r["months_until_end"] >= 0]
    soon = [r for r in live if r["months_until_end"] <= 18]
    sup = {}
    for r in rows:
        k = norm(r["incumbent_supplier"])
        s = sup.setdefault(k, {"supplier": r["incumbent_supplier"], "sme": r["supplier_is_sme"], "contracts": 0, "live_contracts": 0, "ending_within_18_months": 0, "total_awarded_value_gbp": 0, "buyers": set()})
        s["contracts"] += 1
        s["total_awarded_value_gbp"] += r["awarded_value_gbp"] or 0
        s["buyers"].add(r["buyer"])
        if r in live:
            s["live_contracts"] += 1
        if r in soon:
            s["ending_within_18_months"] += 1
    with open(os.path.join(out_dir, f"{slug}-suppliers.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["supplier", "sme", "contracts", "live_contracts", "ending_within_18_months", "total_awarded_value_gbp", "distinct_buyers"])
        for s in sorted(sup.values(), key=lambda s: -s["contracts"]):
            w.writerow([s["supplier"], s["sme"], s["contracts"], s["live_contracts"], s["ending_within_18_months"], round(s["total_awarded_value_gbp"]), len(s["buyers"])])
    vals = [r["awarded_value_gbp"] for r in rows if r["awarded_value_gbp"]]
    summary = {"slug": slug, "phrases": phrases, "published_from": frm, "as_of": today.isoformat(), "contracts": len(rows), "live_contracts": len(live),
               "ending_within_18_months": len(soon), "ending_within_18_months_value_gbp": round(sum((r["awarded_value_gbp"] or 0) for r in soon)),
               "suppliers": len(sup), "sme_suppliers": sum(1 for s in sup.values() if s["sme"] == "yes"), "buyers": len({r["buyer"] for r in rows}),
               "median_awarded_value_gbp": round(statistics.median(vals)) if vals else 0, "truncated_searches": truncated}
    json.dump(summary, open(os.path.join(out_dir, f"{slug}-summary.json"), "w"), indent=1)
    return summary


if __name__ == "__main__":
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    frm = sys.argv[sys.argv.index("--from") + 1] if "--from" in sys.argv else "2020-01-01"
    today = dt.date.fromisoformat(sys.argv[sys.argv.index("--today") + 1]) if "--today" in sys.argv else dt.date.today()
    args = [a for a in args if a not in (frm, today.isoformat())]
    print(json.dumps(build(args[0], args[1], args[2:], frm, today), indent=1))
