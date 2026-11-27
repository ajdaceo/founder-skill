"""Generate a PPN 006 Annex A-style Carbon Reduction Plan (Markdown) from client inputs.
Usage: python3 build_crp.py client.json out.md
Client JSON: {"supplier","publication_date","baseline_year","reporting_year","net_zero_year",
 "baseline":{activity_key: qty}, "current":{activity_key: qty}, "target_pct","target_year",
 "projects_done":[...], "projects_planned":[...], "signatory_name","signatory_role"}
The plan is a self-certified document; the client's director must review and sign."""
import csv, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))

def load_factors(path=os.path.join(HERE, "factors.csv")):
    f = {}
    for r in csv.DictReader(l for l in open(path) if not l.startswith("#")):
        if not r["kgco2e_per_unit"].strip():
            raise SystemExit(f"Factor missing: {r['key']} — fill factors.csv from DESNZ before use")
        f[r["key"]] = (float(r["kgco2e_per_unit"]), int(r["scope"]), r["unit"])
    return f

def totals(acts, F):
    s = {1: 0.0, 2: 0.0, 3: 0.0}
    for k, q in acts.items():
        if k not in F: raise SystemExit(f"Unknown activity {k}")
        s[F[k][1]] += q * F[k][0] / 1000.0
    s["total"] = s[1] + s[2] + s[3]
    return s

def render(c, F):
    b, cur = totals(c["baseline"], F), totals(c["current"], F)
    t = lambda s, k: f"{s[k]:,.2f}"
    L = [f"# Carbon Reduction Plan", "", f"**Supplier name:** {c['supplier']}", f"**Publication date:** {c['publication_date']}", "",
         "## Commitment to achieving Net Zero", f"{c['supplier']} is committed to achieving Net Zero emissions by {c['net_zero_year']}.", "",
         "## Baseline emissions footprint", f"Baseline year: {c['baseline_year']}", "",
         "| Emissions | Total (tCO2e) |", "|---|---|",
         f"| Scope 1 | {t(b,1)} |", f"| Scope 2 | {t(b,2)} |", f"| Scope 3 (included sources) | {t(b,3)} |", f"| Total emissions | {t(b,'total')} |", "",
         "## Current emissions reporting", f"Reporting year: {c['reporting_year']}", "",
         "| Emissions | Total (tCO2e) |", "|---|---|",
         f"| Scope 1 | {t(cur,1)} |", f"| Scope 2 | {t(cur,2)} |", f"| Scope 3 (included sources) | {t(cur,3)} |", f"| Total emissions | {t(cur,'total')} |", "",
         "## Emissions reduction targets",
         f"We project that carbon emissions will decrease over the next five years to {cur['total']*(1-c['target_pct']/100):,.2f} tCO2e by {c['target_year']}. This is a reduction of {c['target_pct']}%.", "",
         "## Carbon reduction projects", "### Completed carbon reduction initiatives", *[f"- {p}" for p in c["projects_done"]], "",
         "### Planned initiatives", *[f"- {p}" for p in c["projects_planned"]], "",
         "## Declaration and sign off",
         "This Carbon Reduction Plan has been completed in accordance with PPN 006 and associated guidance and reporting standard for Carbon Reduction Plans.",
         "Emissions have been reported and recorded in accordance with the published reporting standard for Carbon Reduction Plans and the GHG Reporting Protocol corporate standard, and use the appropriate Government emission conversion factors for greenhouse gas company reporting.",
         "This Carbon Reduction Plan has been reviewed and signed off by the board of directors (or equivalent management body).", "",
         f"Signed on behalf of the supplier: ______________________  {c['signatory_name']}, {c['signatory_role']}", "Date: __________", ""]
    return "\n".join(L), b, cur

if __name__ == "__main__":
    c = json.load(open(sys.argv[1])); md, b, cur = render(c, load_factors())
    open(sys.argv[2], "w").write(md); print(f"baseline {b['total']:.2f} t, current {cur['total']:.2f} t")
