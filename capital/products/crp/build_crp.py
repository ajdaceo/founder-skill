"""Generate a Carbon Reduction Plan (PPN 006 template structure) from client inputs, with a calculation appendix.

Usage: python3 build_crp.py client.json out_dir [--export]   (--export also writes plan.docx and plan.pdf)
Writes out_dir/plan.md (the plan the client's director reviews, signs and publishes),
       out_dir/calculation.md (every figure: quantity x published factor, with the factor's year and source row),
       out_dir/qa.json (checks passed, warnings, and blocking errors).
Exit code 1 and no plan if any blocking error is found.

Client JSON:
{"supplier": "...", "publication_date": "YYYY-MM-DD", "net_zero_year": 2045,
 "baseline": {"label": "2023/24", "period_start": "2023-04-01", "period_end": "2024-03-31", "activities": {"electricity_kwh": 1000, ...}},
 "current":  {"label": "2025/26", "period_start": "2025-04-01", "period_end": "2026-03-31", "activities": {...}},
 "boundary": "operational control",            (or "financial control" / "equity share"; default operational control)
 "board_approval_date": "YYYY-MM-DD",
 "scope3_not_applicable": {"9": "All onward transport is arranged and paid for by us, so it is reported under category 4."},
 "stale_period_explanation": "...",             (only if the reporting period ended more than 18 months before publication)
 "target_pct": 25, "target_year": 2031,
 "projects_done": ["..."], "projects_planned": ["..."],
 "signatory_name": "...", "signatory_role": "Director"}

Method (see METHOD.md):
- Factors: UK Government GHG conversion factors for company reporting, matched to the year of the activity data.
  For a period spanning two calendar years the year holding the greater part of the period is used; a half-and-half
  period (July to June) uses the later year. This is the "majority" approach in the factors' introduction.
- Scope 2 is location-based (UK grid average). Scope 3 covers the five categories the reporting standard requires:
  4 upstream transport and distribution, 5 waste, 6 business travel, 7 employee commuting, 9 downstream transport.
- The plan is self-certified: the client supplies the activity data and its director signs the declaration.
"""
import csv
import datetime as dt
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
SCOPE3_REQUIRED = {"4": "Upstream transportation and distribution", "5": "Waste generated in operations", "6": "Business travel",
                   "7": "Employee commuting", "9": "Downstream transportation and distribution"}
# Transport the company pays for (inbound or outbound) is category 4. Category 9 is only transport and storage of sold
# goods that the company does NOT pay for (customers collecting, customer-arranged haulage): mark those "downstream:".


class InputError(Exception):
    pass


def load_factors(path=os.path.join(HERE, "factors.csv")):
    f = {}
    for r in csv.DictReader(open(path)):
        if not r["kgco2e_per_unit"].strip():
            raise InputError(f"Factor missing: {r['year']} {r['key']}")
        f[(int(r["year"]), r["key"])] = {"factor": float(r["kgco2e_per_unit"]), "scope": int(r["scope"]), "unit": r["unit"],
                                         "cat": r["ppn_scope3_category"], "source": r["source"]}
    return f


def factor_year(start, end):
    """Calendar year holding the greater part of the period; a tie goes to the later year."""
    if end < start:
        raise InputError(f"Period ends before it starts: {start} to {end}")
    days = (end - start).days + 1
    if days < 350 or days > 380:
        raise InputError(f"Reporting period must be about 12 months; {start} to {end} is {days} days")
    count = {}
    for year in range(start.year, end.year + 1):
        lo, hi = max(start, dt.date(year, 1, 1)), min(end, dt.date(year, 12, 31))
        count[year] = (hi - lo).days + 1
    best = max(count.values())
    # Within 4 days counts as a tie: a July-to-June year is 184 v 181 days, and the guidance gives it the later year.
    return max(y for y, n in count.items() if best - n <= 4)


def parse_period(p, name):
    try:
        start, end = dt.date.fromisoformat(p["period_start"]), dt.date.fromisoformat(p["period_end"])
    except (KeyError, ValueError) as e:
        raise InputError(f"{name}: period_start and period_end must be YYYY-MM-DD ({e})")
    return start, end


def calculate(period, F, name):
    """Return (totals by scope, totals by Scope 3 category, calculation lines, factor year)."""
    start, end = parse_period(period, name)
    year = factor_year(start, end)
    scope = {1: 0.0, 2: 0.0, 3: 0.0}
    cats, lines = {}, []
    acts = period.get("activities") or {}
    if not acts:
        raise InputError(f"{name}: no activity data")
    for raw_key, qty in acts.items():
        downstream = raw_key.startswith("downstream:")
        key = raw_key.split(":", 1)[1] if downstream else raw_key
        if not isinstance(qty, (int, float)) or isinstance(qty, bool) or qty < 0:
            raise InputError(f"{name}: {raw_key} must be a number of zero or more, got {qty!r}")
        if (year, key) not in F:
            known = sorted({k for (y, k) in F if y == year})
            if not any(k == key for (_, k) in F):
                raise InputError(f"{name}: unknown activity '{key}'")
            raise InputError(f"{name}: no {year} factor published for '{key}'. Use one of: {', '.join(known)}")
        fac = F[(year, key)]
        tonnes = qty * fac["factor"] / 1000.0
        scope[fac["scope"]] += tonnes
        cat = ""
        if fac["scope"] == 3:
            if downstream and fac["cat"] != "4/9":
                raise InputError(f"{name}: 'downstream:' only applies to transport activities, not {key}")
            cat = "9" if downstream else ("4" if fac["cat"] == "4/9" else fac["cat"])
            cats[cat] = cats.get(cat, 0.0) + tonnes
        lines.append({"activity": raw_key, "quantity": qty, "unit": fac["unit"], "factor": fac["factor"], "factor_year": year,
                      "scope": fac["scope"], "category": cat, "tco2e": tonnes, "source": fac["source"]})
    scope["total"] = scope[1] + scope[2] + scope[3]
    return scope, cats, lines, year


def checks(c, b, cur, bcats, ccats, by, cy):
    """Blocking errors and warnings. Errors stop the plan being issued."""
    errors, warnings = [], []
    if c.get("boundary", "operational control") not in ("operational control", "financial control", "equity share"):
        errors.append("boundary must be operational control, financial control or equity share")
    for field in ("supplier", "publication_date", "net_zero_year", "target_pct", "target_year", "signatory_name", "signatory_role", "board_approval_date"):
        if c.get(field) in (None, ""):
            errors.append(f"Missing field: {field}")
    if isinstance(c.get("net_zero_year"), int) and c["net_zero_year"] > 2050:
        errors.append("Net Zero year must be 2050 or earlier (the commitment the procurement rule requires)")
    try:
        pub = dt.date.fromisoformat(str(c.get("publication_date")))
        cur_end = dt.date.fromisoformat(c["current"]["period_end"])
        if cur_end > pub:
            errors.append("Reporting period ends after the publication date")
        if (pub - cur_end).days > 548 and not str(c.get("stale_period_explanation", "")).strip():
            errors.append("Reporting period ended more than 18 months before publication: buyers fail this unless the plan explains why "
                          "(set stale_period_explanation) - or report the latest financial year")
        elif (pub - cur_end).days > 183:
            warnings.append("Plan is being published more than 6 months after the reporting year-end; the standard asks for an update within 6 months")
        b_end = dt.date.fromisoformat(c["baseline"]["period_end"])
        if (b_end.month, b_end.day) != (cur_end.month, cur_end.day):
            warnings.append("Baseline and reporting periods have different year-ends; the standard asks for the same reporting period throughout - explain in baseline notes")
        if c.get("board_approval_date"):
            if dt.date.fromisoformat(str(c["board_approval_date"])) > pub:
                errors.append("board_approval_date is after the publication date")
        if isinstance(c.get("target_year"), int) and not (pub.year < c["target_year"] <= pub.year + 6):
            warnings.append("Target year is usually five years ahead of publication")
    except (ValueError, KeyError, TypeError):
        errors.append("publication_date must be YYYY-MM-DD")
    na = c.get("scope3_not_applicable") or {}
    for cat, label in SCOPE3_REQUIRED.items():
        for name, cats in (("baseline", bcats), ("current", ccats)):
            if cat not in cats and not str(na.get(cat, "")).strip():
                errors.append(f"Scope 3 category {cat} ({label}) has no {name} data and no stated reason in scope3_not_applicable")
    if cur[2] == 0:
        warnings.append("No electricity reported: confirm the premises really use none or that it is included in rent")
    if cur[1] == 0:
        warnings.append("No Scope 1 emissions reported: confirm there is no gas, fuel, company vehicle or refrigerant use")
    if b["total"] > 0:
        change = (cur["total"] - b["total"]) / b["total"] * 100
        if abs(change) > 40:
            warnings.append(f"Total emissions changed {change:+.0f}% from baseline: check the data or explain the change in the plan")
    if cy < by:
        errors.append("Reporting year is earlier than the baseline year")
    if not c.get("projects_done") and not c.get("projects_planned"):
        errors.append("At least one completed or planned carbon reduction measure is required")
    if isinstance(c.get("target_pct"), (int, float)) and not (0 < c["target_pct"] <= 100):
        errors.append("target_pct must be between 0 and 100")
    return errors, warnings


def t(x):
    return f"{x:,.2f}"


def render(c, b, cur, bcats, ccats):
    na = c.get("scope3_not_applicable") or {}

    def table(s, cats):
        rows = ["| Emissions | Total (tCO2e) |", "|---|---|", f"| Scope 1 | {t(s[1])} |", f"| Scope 2 | {t(s[2])} |",
                f"| Scope 3 (included sources) | {t(s[3])} |"]
        for cat, label in SCOPE3_REQUIRED.items():
            rows.append(f"| - {label} | {t(cats[cat]) if cat in cats else 'Not applicable: ' + str(na.get(cat, '')).strip()} |")
        rows.append(f"| **Total emissions** | **{t(s['total'])}** |")
        return rows

    target = cur["total"] * (1 - c["target_pct"] / 100)
    L = ["# Carbon Reduction Plan", "", f"**Supplier name:** {c['supplier']}", "", f"**Publication date:** {c['publication_date']}", "",
         "## Commitment to achieving Net Zero", f"{c['supplier']} is committed to achieving Net Zero emissions by {c['net_zero_year']}.", "",
         "## Baseline emissions footprint",
         "Baseline emissions are a record of the greenhouse gases that have been produced in the past and were produced prior to the "
         "introduction of any strategies to reduce emissions. Baseline emissions are the reference point against which emissions "
         "reduction can be measured.", "",
         f"**Baseline year:** {c['baseline']['label']} ({c['baseline']['period_start']} to {c['baseline']['period_end']})", "",
         "**Additional details relating to the baseline emissions calculations:** "
         + (c["baseline"].get("notes", "").strip() + " " if c["baseline"].get("notes") else "")
         + f"Emissions cover all UK operations under the {c.get('boundary', 'operational control')} approach. They are calculated from the "
           "company's own activity records using the UK Government greenhouse gas conversion factors for the year of the activity data. "
           "Electricity is reported on a location-based (grid average) basis. Flights include the effect of radiative forcing. "
           "Well-to-tank emissions and electricity transmission and distribution losses fall outside the required categories and are not included.", "",
         *([f"**Explanation for the age of the reporting period:** {c['stale_period_explanation']}", ""] if c.get("stale_period_explanation") else []),
         *table(b, bcats), "",
         "## Current emissions reporting",
         f"**Reporting year:** {c['current']['label']} ({c['current']['period_start']} to {c['current']['period_end']})", "",
         *table(cur, ccats), "",
         "## Emissions reduction targets",
         "In order to continue our progress to achieving Net Zero, we have adopted the following carbon reduction targets.", "",
         f"We project that carbon emissions will decrease over the next five years to {t(target)} tCO2e by {c['target_year']}. "
         f"This is a reduction of {c['target_pct']:g}%.", "",
         "## Carbon reduction projects", "### Completed carbon reduction initiatives",
         *([f"- {p}" for p in c.get("projects_done") or []] or ["- None yet; this is our first reporting year."]), "",
         "### Planned carbon reduction initiatives", *[f"- {p}" for p in c.get("projects_planned") or []], "",
         "## Declaration and sign off",
         "This Carbon Reduction Plan has been completed in accordance with PPN 006 and associated guidance and reporting standard "
         "for Carbon Reduction Plans.", "",
         "Emissions have been reported and recorded in accordance with the published reporting standard for Carbon Reduction Plans "
         "and the GHG Reporting Protocol corporate standard and uses the appropriate government emission conversion factors for "
         "greenhouse gas company reporting.", "",
         "Scope 1 and Scope 2 emissions have been reported in accordance with SECR requirements (where required), and the required "
         "subset of Scope 3 emissions have been reported in accordance with the published reporting standard for Carbon Reduction "
         "Plans and the Corporate Value Chain (Scope 3) Standard.", "",
         "This Carbon Reduction Plan has been reviewed and signed off by the board of directors (or equivalent management body).", "",
         f"Date of board approval: {c['board_approval_date']}", "",
         "Signed on behalf of the supplier:", "", "______________________________", "",
         f"{c['signatory_name']}, {c['signatory_role']}", "", "Date: ______________", ""]
    return "\n".join(L)


def calc_appendix(c, sets):
    L = [f"# Calculation record: {c['supplier']}", "",
         "Every figure in the plan is quantity x published factor / 1000. Factors are the UK Government GHG conversion factors "
         "for company reporting (Open Government Licence), matched to the year of the activity data. "
         "Activity quantities were supplied by the company and have not been audited.", ""]
    for title, period, lines, year in sets:
        L += [f"## {title}: {period['label']} ({period['period_start']} to {period['period_end']}), {year} factors", "",
              "| Activity | Quantity | Unit | kgCO2e per unit | Scope | Category | tCO2e | Factor source |", "|---|---|---|---|---|---|---|---|"]
        for x in lines:
            L.append(f"| {x['activity']} | {x['quantity']:,} | {x['unit']} | {x['factor']:g} | {x['scope']} | {x['category']} | {x['tco2e']:,.3f} | {x['source']} |")
        L.append("")
    return "\n".join(L)


def build(c, F):
    for part in ("baseline", "current"):
        if not isinstance(c.get(part), dict) or not c[part].get("label"):
            raise InputError(f"{part}: needs label, period_start, period_end and activities")
    b, bcats, blines, by = calculate(c["baseline"], F, "baseline")
    cur, ccats, clines, cy = calculate(c["current"], F, "current")
    errors, warnings = checks(c, b, cur, bcats, ccats, by, cy)
    qa = {"supplier": c.get("supplier"), "baseline_factor_year": by, "current_factor_year": cy,
          "baseline_tco2e": {str(k): round(v, 3) for k, v in b.items()}, "current_tco2e": {str(k): round(v, 3) for k, v in cur.items()},
          "errors": errors, "warnings": warnings, "status": "blocked" if errors else ("review" if warnings else "pass")}
    if errors:
        return None, None, qa
    return render(c, b, cur, bcats, ccats), calc_appendix(c, [("Baseline", c["baseline"], blines, by), ("Current", c["current"], clines, cy)]), qa


def export(out_dir):
    """Word and PDF copies of the plan for the client (needs pandoc and LibreOffice). Returns the files written."""
    import shutil
    import subprocess
    made = []
    if not shutil.which("pandoc"):
        return made
    docx = os.path.join(out_dir, "plan.docx")
    subprocess.run(["pandoc", os.path.join(out_dir, "plan.md"), "-o", docx], check=True, timeout=120)
    made.append(docx)
    if shutil.which("soffice"):
        subprocess.run(["soffice", "--headless", "--norestore", f"-env:UserInstallation=file://{os.path.abspath(out_dir)}/.lo",
                        "--convert-to", "pdf", "--outdir", out_dir, docx], capture_output=True, timeout=180)
        shutil.rmtree(os.path.join(out_dir, ".lo"), ignore_errors=True)
        if os.path.exists(os.path.join(out_dir, "plan.pdf")):
            made.append(os.path.join(out_dir, "plan.pdf"))
    return made


if __name__ == "__main__":
    client, out_dir = json.load(open(sys.argv[1])), sys.argv[2]
    os.makedirs(out_dir, exist_ok=True)
    try:
        plan, calc, qa = build(client, load_factors())
    except InputError as e:
        plan, calc, qa = None, None, {"supplier": client.get("supplier"), "errors": [str(e)], "warnings": [], "status": "blocked"}
    json.dump(qa, open(os.path.join(out_dir, "qa.json"), "w"), indent=2)
    if plan is None:
        print("BLOCKED:", *qa["errors"], sep="\n  ")
        sys.exit(1)
    open(os.path.join(out_dir, "plan.md"), "w").write(plan)
    open(os.path.join(out_dir, "calculation.md"), "w").write(calc)
    if "--export" in sys.argv:
        print("exported:", ", ".join(os.path.basename(f) for f in export(out_dir)))
    print(f"{qa['status']}: baseline {qa['baseline_tco2e']['total']} t ({qa['baseline_factor_year']} factors), "
          f"current {qa['current_tco2e']['total']} t ({qa['current_factor_year']} factors)", *qa["warnings"], sep="\n  ")
