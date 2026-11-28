"""Add Companies House facts to classified rows that lack them (prospect statuses only)."""
import csv, sys, concurrent.futures
sys.path.insert(0, "/home/user/founder-skill/capital/ops")
import enrich
src, dst = sys.argv[1], sys.argv[2]
rows = list(csv.DictReader(open(src)))
WANT = {"no_crp", "crp_outdated", "crp_overdue", "crp_unpublished", "crp_borderline"}
def fill(r):
    if r["status"] not in WANT or r.get("ch_status"):
        return r
    number = (r.get("coh") or "").strip() or enrich.ch_find(r["supplier"])
    ch = enrich.ch_company(number) if number else {}
    for k in ("ch_number", "ch_name", "ch_status", "ch_type", "ch_incorporated", "ch_last_accounts", "ch_sic", "ch_postcode"):
        r[k] = ch.get(k, "")
    return r
with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
    rows = list(pool.map(fill, rows))
fields = list(dict.fromkeys(k for r in rows for k in r))
w = csv.DictWriter(open(dst, "w", newline=""), fieldnames=fields); w.writeheader(); w.writerows(rows)
want = [r for r in rows if r["status"] in WANT]
print("prospect-status rows", len(want), "with CH record", sum(1 for r in want if r.get("ch_number")), "active", sum(1 for r in want if r.get("ch_status") == "Active"))
