"""Build the E6 deliverable: a checked list of NHS suppliers with no current Carbon Reduction Plan.

Usage: python3 e6_build.py research/e3-prospects-qualified.csv OUT_DIR [--checked 2026-11-28]
Writes OUT_DIR/nhs-suppliers-without-current-plan-<date>.xlsx and a five-row sample CSV.
The full file is the paid product: keep OUT_DIR outside any public repository.
Company-level data only. Addresses that belong to a named person are left out.
"""
import csv
import datetime as dt
import os
import sys

from openpyxl import Workbook
from openpyxl.styles import Font
from openpyxl.utils import get_column_letter

COLS = [("Company", "supplier", 34), ("Company number", "company_number", 12), ("Company type", "company_type", 22),
        ("Website", "website", 34), ("Published company email", "_email", 32), ("Plan status when checked", "plan_status", 26),
        ("Date on the plan found", "plan_date", 14), ("Evidence (plan page or file)", "plan_evidence", 40),
        ("NHS route", "_route", 26), ("Competitive NHS awards since Jan 2025", "competitive_awards", 10),
        ("Latest award", "latest_award", 12), ("Latest NHS buyer", "latest_buyer", 40), ("Latest contract", "latest_contract", 50),
        ("Award notice", "latest_notice", 44), ("Sector", "sector", 28)]


def load(path):
    rows = []
    for r in csv.DictReader(open(path)):
        r["_email"] = r["email"] if r.get("email_kind") == "generic" and "@" in r["email"] and " " not in r["email"].strip() else ""
        r["_route"] = "On an NHS framework" if r["tier"].startswith("A") else "NHS contract won by open competition"
        rows.append(r)
    rows.sort(key=lambda r: (r["tier"][:1], r["plan_status"], r["supplier"].lower()))
    return rows


def checks(rows):
    """Release checks. Returns a list of problems; empty means the file can go out."""
    bad = []
    seen = set()
    for r in rows:
        if not r["company_number"] or not r["website"].startswith("http"):
            bad.append(f"missing company number or website: {r['supplier']}")
        if r["company_number"] in seen:
            bad.append(f"duplicate company: {r['supplier']}")
        seen.add(r["company_number"])
        if "limited" not in r["company_type"].lower() and "llp" not in r["company_type"].lower() and "plc" not in r["company_type"].lower():
            bad.append(f"not a company or LLP: {r['supplier']} ({r['company_type']})")
        if r["plan_status"] != "No plan found" and not r["plan_evidence"]:
            bad.append(f"out-of-date plan with no evidence link: {r['supplier']}")
        if r["_email"] and r["_email"].split("@")[0].count(".") and r["_email"].split("@")[0].split(".")[0].isalpha() and len(r["_email"].split("@")[0].split(".")) == 2:
            bad.append(f"address looks like a named person: {r['supplier']} {r['_email']}")
        if not r["latest_notice"].startswith("http"):
            bad.append(f"no award notice link: {r['supplier']}")
    return bad


def build(src, out_dir, checked):
    rows = load(src)
    problems = checks(rows)
    os.makedirs(out_dir, exist_ok=True)
    wb = Workbook()
    ws = wb.active
    ws.title = "Companies"
    ws.append([c[0] for c in COLS])
    for c in ws[1]:
        c.font = Font(bold=True)
    for r in rows:
        ws.append([r.get(c[1], "") for c in COLS])
    for i, c in enumerate(COLS, 1):
        ws.column_dimensions[get_column_letter(i)].width = c[2]
    ws.freeze_panes = "B2"
    ws.auto_filter.ref = ws.dimensions
    notes = wb.create_sheet("Read me")
    none = sum(1 for r in rows if r["plan_status"] == "No plan found")
    for line in [
        f"NHS suppliers with no current Carbon Reduction Plan on their website. Checked {checked}.",
        "",
        f"{len(rows)} companies: {none} with no plan found, {len(rows) - none} with a plan published more than 15 months before the check.",
        f"{sum(1 for r in rows if r['_email'])} have a published company email address. Addresses that belong to a named person are left out.",
        "",
        "How each company was selected: a small or medium-sized company, active at Companies House, that won English NHS work by open competition",
        "since January 2025 (Find a Tender award notices), with a working website on which no Carbon Reduction Plan dated within the last 15 months was found.",
        "Each site was read by software in a browser; plan documents were opened and dated, including scanned files.",
        "",
        "Accuracy: a second check of 12 entries found 1 wrong. Expect about 1 entry in 12 to be wrong. Companies may have published a plan since the check.",
        "A plan can also exist without being published; the list records only what the website showed.",
        "",
        "Use: for the buyer's own marketing and research; not for resale. Unsolicited email may be sent only to companies and LLPs, with your identity and an opt-out.",
        "Refund: in full on request within 14 days of delivery.",
        "",
        "Contains public sector information licensed under the Open Government Licence v3.0 (Find a Tender, Contracts Finder, Companies House).",
        "Compiled by AI software and checked before delivery. Oakmarch.",
    ]:
        notes.append([line])
    notes.column_dimensions["A"].width = 140
    name = f"nhs-suppliers-without-current-plan-{checked}.xlsx"
    wb.save(os.path.join(out_dir, name))
    return {"file": os.path.join(out_dir, name), "companies": len(rows), "no_plan_found": none, "out_of_date": len(rows) - none,
            "with_company_email": sum(1 for r in rows if r["_email"]), "release_problems": problems}


if __name__ == "__main__":
    checked = sys.argv[sys.argv.index("--checked") + 1] if "--checked" in sys.argv else dt.date.today().isoformat()
    import json
    print(json.dumps(build(sys.argv[1], sys.argv[2], checked), indent=1))
