"""E4: turn checked vendor sites into a prospect list with an individual five-row sample each, and render draft emails.
Usage: python3 e4_prepare.py E4_WORK_DIR OUT_DIR
Needs in E4_WORK_DIR: <slug>-calendar.csv, <slug>-summary.json, prospect_enriched.csv, sites.out.jsonl. Nothing is sent."""
import collections, csv, json, os, re, sys, urllib.parse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import cf_report, qualify
work, out = sys.argv[1], sys.argv[2]
LABEL = {"oh-eap": "occupational health and employee assistance", "lms": "learning management system and e-learning"}
GENERIC_NAME = {"health", "group", "services", "solutions", "learning", "management", "healthcare", "occupational", "consultancy", "medical", "wellbeing", "software", "digital", "limited", "ltd", "uk", "the"}
ROLE_OK = ("info", "enquiries", "enquiry", "sales", "hello", "contact", "office", "admin", "marketing", "businessdevelopment", "bd", "bids", "tenders",
           "newbusiness", "commercial", "partnerships", "salessupport", "team", "mail")
SAME_FIRM = {"vitahealthgroup.co.uk": "vhg.co.uk"}  # a firm's published address on its other domain, checked by hand


def pick_role_email(site):
    """A published company role address (never a named person) on the firm's own domain."""
    host = urllib.parse.urlparse(site.get("final") or site["url"]).netloc.lower().replace("www.", "")
    best = []
    for e in site.get("emails", []):
        if not re.fullmatch(r"[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}", e):
            continue
        local, dom = e.split("@")
        if local in ROLE_OK and (dom == host or host.endswith("." + dom) or dom.endswith("." + host) or SAME_FIRM.get(host) == dom):
            best.append((ROLE_OK.index(local), e))
    return sorted(best)[0][1] if best else ""


def company_type(number):
    import enrich
    r = enrich.get(f"{enrich.CH}/company/{number}", 25)
    if not r:
        return ""
    m = re.search(r"Company type (.{5,120}?) (?:Incorporated|Registered|Converted|Formed) on", enrich.text_of(r))
    return m.group(1).strip() if m else ""


enr = {r["id"]: r for r in csv.DictReader(open(f"{work}/prospect_enriched.csv"))}
sites = {}
for l in open(f"{work}/sites.out.jsonl"):
    if l.strip():
        d = json.loads(l); sites[d["id"]] = d
cal = {s: list(csv.DictReader(open(f"{work}/{s}-calendar.csv"))) for s in LABEL}
summ = {s: json.load(open(f"{work}/{s}-summary.json")) for s in LABEL}
prospects, seen_hosts = [], set()
for pid, site in sorted(sites.items(), key=lambda kv: -int(enr[kv[0]]['contracts'])):
    e = enr[pid]
    slug = e["category"]
    if site.get("status") != 200 or site.get("dead"):
        continue
    email = pick_role_email(site)
    if not email:
        continue
    toks = [t for t in cf_report.norm(e["supplier"].split(" t/a ")[0]).split() if t not in GENERIC_NAME and len(t) > 2]
    text = (site.get("title", "") + " " + site.get("final", "")).lower().replace("-", "")
    number = (e.get("ch_number") or "").lstrip("0")
    id_ok = (number and any(n.lstrip("0") == number for n in site.get("company_nos", []))) or (toks and all(t in text for t in toks[:2])) or e.get("website_basis", "").startswith(("company number", "name"))
    if not id_ok:
        continue
    host = urllib.parse.urlparse(site.get("final") or site["url"]).netloc.lower().replace("www.", "")
    if host in seen_hosts:
        continue  # merged or acquired firms that now share one website are approached once
    seen_hosts.add(host)
    if e.get("ch_number") and not e.get("ch_type"):
        e["ch_type"] = company_type(e["ch_number"])
    me = cf_report.norm(e["supplier"])
    want = toks[:2] if toks else me.split()[:2]
    mine = [r for r in cal[slug] if all(re.search(rf"\b{re.escape(t)}\b", cf_report.norm(r["incumbent_supplier"])) for t in want)]
    live = [r for r in mine if r["months_until_end"] not in ("",) and float(r["months_until_end"]) >= 0]
    ending = [r for r in live if float(r["months_until_end"]) <= 18]
    own_vals = sorted(float(r["awarded_value_gbp"]) for r in mine if r["awarded_value_gbp"])
    typical = own_vals[len(own_vals) // 2] if own_vals else 150000.0
    lo, hi = max(30000.0, typical / 3), max(typical * 4, 250000.0)  # contracts of a size this firm actually wins
    pool = [r for r in cal[slug] if r not in mine and r["months_until_end"] not in ("",) and 4 <= float(r["months_until_end"]) <= 14
            and r["awarded_value_gbp"] and lo <= float(r["awarded_value_gbp"]) <= hi]
    pool.sort(key=lambda r: -float(r["awarded_value_gbp"]))
    sample, seen_buyers = [], set()
    for r in pool:
        if r["buyer"] in seen_buyers: continue
        seen_buyers.add(r["buyer"]); sample.append(r)
        if len(sample) == 5: break
    prospects.append({"arm": slug, "company": e["supplier"], "company_number": e.get("ch_number", ""), "company_status": e.get("ch_status", ""), "company_type": e.get("ch_type", ""),
                      "website": site.get("final") or site["url"], "email": email, "contracts_on_record": len(mine), "live_contracts": len(live), "own_ending_within_18_months": len(ending),
                      "flagged_small_firm": e.get("sme", ""), "_sample": sample})
# keep active limited companies or LLPs only; mid-sized record first; 20 per arm
final = []
for slug in LABEL:
    arm = [p for p in prospects if p["arm"] == slug and p["company_status"] == "Active" and re.search(r"limited|plc|llp|community interest", p["company_type"], re.I) and len(p["_sample"]) == 5]
    arm.sort(key=lambda p: (not (2 <= p["contracts_on_record"] <= 20), -p["contracts_on_record"]))
    final += arm[:20]
os.makedirs(out, exist_ok=True)
with open(f"{out}/prospects.csv", "w", newline="") as f:
    w = csv.writer(f)
    w.writerow(["arm", "company", "company_number", "company_type", "website", "email", "contracts_on_record", "live_contracts", "own_ending_within_18_months"])
    for p in final:
        w.writerow([p["arm"], p["company"], p["company_number"], p["company_type"], p["website"], p["email"], p["contracts_on_record"], p["live_contracts"], p["own_ending_within_18_months"]])
def coverage(slug):
    live = [r for r in cal[slug] if r["months_until_end"] not in ("",) and float(r["months_until_end"]) >= 0]
    count = lambda pat: len({r["buyer"].strip().lower() for r in live if re.search(pat, r["buyer"].lower())})
    return count(r"council|borough|corporation of london"), count(r"\bnhs\b"), count(r"police|constab|crime commissioner")


SHORT = {"oh-eap": "occupational health", "lms": "learning management system"}


def render(p):
    s, lab, short = summ[p["arm"]], LABEL[p["arm"]], SHORT[p["arm"]]
    councils, nhs, police = coverage(p["arm"])
    own = (f"{p['company']} holds {p['live_contracts']} live public-sector contract{'s' if p['live_contracts'] != 1 else ''} in this market that I can find in published award notices"
           + (f", {p['own_ending_within_18_months']} of them ending within 18 months." if p["own_ending_within_18_months"] else "."))
    rows = "\n".join(f"- {r['buyer']}: held by {r['incumbent_supplier']}, £{float(r['awarded_value_gbp']):,.0f}, ends {r['contract_end']}" for r in p["_sample"])
    return (f"To: {p['email']}\nSubject: {short.capitalize()} contracts with no published award notice\n\nHello,\n\n{own}\n\n"
            f"Published award notices cover only part of this market. I can find a live {short} contract in published notices for only {councils} English councils, {nhs} NHS bodies and {police} police forces. "
            "For the rest I can find no award notice.\n\n"
            "We are considering compiling the missing ones: asking each of those bodies, under the Freedom of Information Act, who holds the contract, what it is worth, when it ends and what extensions remain, "
            f"and putting the replies into one spreadsheet with the source for every row, alongside the published contracts ({s['contracts']} since 2020, {s['ending_within_18_months']} ending within 18 months). "
            "No requests have been sent yet. We will go ahead only if enough suppliers want the result.\n\n"
            f"To show the format, five published contracts ending in the next 4 to 14 months that you do not hold:\n{rows}\n\n"
            "The report would be £295, payable on delivery. Public bodies have 20 working days to reply, so delivery would be about eight weeks after we go ahead. "
            "Reply \"reserve\" and we will tell you within two weeks whether it is going ahead. There is nothing to pay unless and until you receive it, and a full refund within 14 days if it is not as described.\n\n"
            "Some bodies answer late or refuse. The report would list exactly which bodies were asked and which answered.\n\n"
            "{owner_name}, sole trader trading as {trading_name}\n{service_address} · {phone}\n"
            "The figures above were compiled by AI software from Contracts Finder award notices (Open Government Licence v3.0) and checked before sending.\n"
            f"You are receiving this once because {p['company']} is a supplier in this market. Reply \"stop\" and we will not contact you again.\n")
with open(f"{out}/outreach-drafts.md", "w") as f:
    f.write("# E4 outreach drafts (NOT SENT)\n\nExamples only (two per arm); `ops/e4_prepare.py` generates one per prospect. Placeholders in braces are filled after owner set-up.\n\n"
            "Before any send: rebuild the calendar that day, and check by hand that each prospect's own-contract count and five sample rows are right. "
            "Own contracts are matched by company name and can miscount where firms trade under several names.\n")
    shown = collections.Counter()
    for p in final:
        shown[p["arm"]] += 1
        if shown[p["arm"]] > 2:
            continue
        f.write(f"\n---\n\n## {p['arm']}: {p['company']}\n\n```\n{render(p)}```\n")
print("prospects passing all checks:", len(prospects), collections.Counter(p["arm"] for p in prospects), "| selected:", collections.Counter(p["arm"] for p in final))
print("selected by record size:", collections.Counter(("1" if p["contracts_on_record"] <= 1 else "2-9" if p["contracts_on_record"] <= 9 else "10+") for p in final))
ex = next(p for p in final if p["arm"] == "oh-eap" and 2 <= p["contracts_on_record"] <= 9)
print("\n" + render(ex))
