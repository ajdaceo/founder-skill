import csv, collections, re, sys, urllib.parse, html, requests
sys.path.insert(0, "/home/user/founder-skill/capital/ops")
import enrich
P = {"no_crp": "No plan found", "crp_outdated": "Plan dated 2024 or earlier", "crp_overdue": "Plan more than 15 months old", "crp_unpublished": "Plan not published"}
rows = []
for f in ("data/q_given_ch.csv", "data/q_enriched.csv"):
    rows += list(csv.DictReader(open(f)))
print("classified sites:", len(rows), collections.Counter(r["status"] for r in rows).most_common())
working = [r for r in rows if r["status"] not in ("blocked", "error", "dead")]
print("working sites:", len(working), "| no current plan (incl. borderline):", sum(1 for r in working if r["status"] in P or r["status"] == "crp_borderline"),
      "| prospect statuses:", sum(1 for r in working if r["status"] in P))
# fix empty company type with a looser pattern
def ctype(number):
    r = enrich.get(f"{enrich.CH}/company/{number}", 25)
    if not r: return ""
    t = enrich.text_of(r)
    m = re.search(r"Company type (.{5,120}?) (?:Incorporated|Registered|Converted|Formed) on", t)
    return m.group(1).strip() if m else ""
out, seen_no, seen_dom = [], set(), set()
drop = collections.Counter()
for r in rows:
    if r["status"] not in P: continue
    if r.get("ch_status") != "Active": drop["not an active company on the register"] += 1; continue
    if not r.get("ch_type") and r.get("ch_number"):
        r["ch_type"] = ctype(r["ch_number"])
    t = (r.get("ch_type") or "").lower()
    if not ("limited" in t or "community interest" in t or "plc" in t) or "limited partnership" == t.strip():
        drop["company type not confirmed as a corporate body"] += 1; continue
    if not r["email"] or r["email_domain"] != "own-domain": drop["no email on own domain"] += 1; continue
    dom = urllib.parse.urlparse(r["website"]).netloc.lower().replace("www.", "")
    if r["ch_number"] in seen_no or dom in seen_dom: drop["duplicate"] += 1; continue
    seen_no.add(r["ch_number"]); seen_dom.add(dom)
    fw = r["n_framework_awards"] not in ("0", "")
    out.append({
        "supplier": r["supplier"], "company_number": r["ch_number"], "company_type": r["ch_type"], "incorporated": r["ch_incorporated"],
        "last_accounts_to": r["ch_last_accounts"], "sic": r["ch_sic"], "website": r["website"], "website_basis": r.get("website_basis") or "given in the award notice",
        "email": r["email"], "email_kind": r["email_kind"], "plan_status": P[r["status"]], "plan_date": r["plan_date"], "plan_evidence": r["evidence"],
        "tier": "A: on an NHS framework (plan required at any new framework tender now)" if fw else "B: NHS contract by open competition (plan required at any new tender from 1 Apr 2027)",
        "competitive_awards": r["n_awards"], "latest_award": r["latest_award"], "latest_buyer": r["latest_buyer"], "latest_contract": r["latest_title"],
        "latest_notice": "https://www.find-tender.service.gov.uk/Notice/" + r["latest_notice"], "sector": r["cpv"], "procedure": r["method"]})
out.sort(key=lambda r: (r["tier"][0], r["plan_status"] != "No plan found", r["latest_award"]), reverse=False)
out.sort(key=lambda r: r["latest_award"], reverse=True); out.sort(key=lambda r: r["tier"][0])
w = csv.DictWriter(open("data/prospects_qualified.csv", "w", newline=""), fieldnames=list(out[0].keys())); w.writeheader(); w.writerows(out)
print("QUALIFIED:", len(out), "| dropped:", dict(drop))
print("tier:", collections.Counter(r["tier"][:1] for r in out), "| plan status:", collections.Counter(r["plan_status"] for r in out))
print("email kind:", collections.Counter(r["email_kind"] for r in out), "| website basis:", collections.Counter(r["website_basis"][:24] for r in out).most_common(4))
print("sector:", collections.Counter(r["sector"] for r in out).most_common(12))
print("buyer:", collections.Counter(r["latest_buyer"][:38] for r in out).most_common(8))
print("company type:", collections.Counter(r["company_type"][:45] for r in out).most_common(5))
print("last award year:", collections.Counter(r["latest_award"][:4] for r in out))
b = [r for r in rows if r["status"] == "crp_borderline" and r.get("ch_status") == "Active" and r["email"]]
print("renewal-due (12-15 months) with email, not counted:", len(b))
