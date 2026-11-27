"""Independent GHG calculation from the official UK Government conversion factor flat files.
Run: python3 -I calc.py <dir with loader.py> <desnz base dir> <out dir>
Only rows whose GHG column is exactly "kg CO2e" are used. No intermediate rounding (Decimal arithmetic)."""
import sys, json
from decimal import Decimal, getcontext
sys.path.insert(0, sys.argv[1])
from loader import load, co2e_only
getcontext().prec = 40
BASE, OUT = sys.argv[2], sys.argv[3]

# activity data: item -> (description, baseline qty, current qty, scope)
ACT = {
 1: ("Natural gas, kWh gross CV", 180000, 171000, 1),
 2: ("LPG, litres", 2000, 1800, 1),
 3: ("Gas oil, litres", 1500, 1200, 1),
 4: ("Diesel (average biofuel blend), own vehicles, litres", 42000, 40500, 1),
 5: ("Petrol (average biofuel blend), own vehicles, litres", 3000, 2500, 1),
 6: ("Refrigerant R404A, kg", 12, 6, 1),
 7: ("Refrigerant HFC-134a, kg", 2, 1, 1),
 8: ("Grid electricity UK, generation, kWh", 310000, 295000, 2),
 9: ("Inbound third-party refrigerated HGV, vehicle km", 60000, 58000, 3),
 10: ("Outbound third-party diesel van, vehicle km", 25000, 27000, 3),
 11: ("C&I waste to landfill, tonnes", 12, 9, 3),
 12: ("C&I waste to combustion, tonnes", 20, 22, 3),
 13: ("Food and drink waste to anaerobic digestion, tonnes", 30, 33, 3),
 14: ("Mixed paper and board, closed-loop recycling, tonnes", 8, 10, 3),
 15: ("Business travel, employees' own cars (average car, unknown fuel), km", 18000, 16500, 3),
 16: ("Business travel, national rail, passenger km", 6000, 7000, 3),
 17: ("Business travel, domestic flights, avg passenger, with RF, passenger km", 4000, 3000, 3),
 18: ("Business travel, short-haul flights, avg passenger, with RF, passenger km", 9000, 6000, 3),
 19: ("UK hotel stays, room nights", 25, 20, 3),
 20: ("Business travel, regular taxi, passenger km", 800, 600, 3),
 21: ("Commuting, average car unknown fuel, km", 160000, 158000, 3),
 22: ("Commuting, average local bus, passenger km", 30000, 32000, 3),
 23: ("Commuting, national rail, passenger km", 12000, 14000, 3),
 24: ("Commuting, motorbike average, km", 2000, 1500, 3),
}

# Row selectors: (scope, level1, level2, level3, level4, column text, uom).
# Two layouts: "old" (2018-2021 naming) and "new" (2022+). Differences are only
# refrigerants (Level 2 names + Column Text) and the Column Text of fuels / Level 4 of electricity.
def selectors(year):
    old = year <= 2021
    S = {}
    S[1] = ("Scope 1", "Fuels", "Gaseous fuels", "Natural gas", "", "Energy - Gross CV" if old else "", "kWh (Gross CV)")
    S[2] = ("Scope 1", "Fuels", "Gaseous fuels", "LPG", "", "Volume" if old else "", "litres")
    S[3] = ("Scope 1", "Fuels", "Liquid fuels", "Gas oil", "", "Volume" if old else "", "litres")
    S[4] = ("Scope 1", "Fuels", "Liquid fuels", "Diesel (average biofuel blend)", "", "Volume" if old else "", "litres")
    S[5] = ("Scope 1", "Fuels", "Liquid fuels", "Petrol (average biofuel blend)", "", "Volume" if old else "", "litres")
    if old:
        S[6] = ("Scope 1", "Refrigerant & other", "Kyoto protocol- blends", "R404A", "", "", "kg")
        S[7] = ("Scope 1", "Refrigerant & other", "Kyoto protocol - standard", "HFC-134a", "", "", "kg")
        S[8] = ("Scope 2", "UK electricity", "Electricity generated", "Electricity: UK", "", "", "kWh")
    else:
        S[6] = ("Scope 1", "Refrigerant & other", "Blends", "R404A", "", "Emissions including only Kyoto products", "kg")
        S[7] = ("Scope 1", "Refrigerant & other", "Kyoto protocol products", "HFC-134a", "", "Emissions including only Kyoto products", "kg")
        S[8] = ("Scope 2", "UK electricity", "Electricity generated", "Electricity: UK", None, "", "kWh")  # Level 4 is blank or 'kWh' depending on year
    S[9] = ("Scope 3", "Freighting goods", "HGV refrigerated (all diesel)", "All HGVs", "", "Average laden", "km")
    S[10] = ("Scope 3", "Freighting goods", "Vans", "Average (up to 3.5 tonnes)", "", "Diesel", "km")
    S[11] = ("Scope 3", "Waste disposal", "Refuse", "Commercial and industrial waste", "", "Landfill", "tonnes")
    # 2025 onwards the waste column text "Combustion" was renamed "Incineration with Energy Recovery" (only used in the blended alternative)
    S[12] = ("Scope 3", "Waste disposal", "Refuse", "Commercial and industrial waste", "", "Combustion" if year <= 2024 else "Incineration with Energy Recovery", "tonnes")
    S[13] = ("Scope 3", "Waste disposal", "Refuse", "Organic: food and drink waste", "", "Anaerobic digestion", "tonnes")
    S[14] = ("Scope 3", "Waste disposal", "Paper", "Paper and board: mixed", "", "Closed-loop", "tonnes")
    car = ("Scope 3", "Business travel- land", "Cars (by size)", "Average car", "", "Unknown", "km")
    rail = ("Scope 3", "Business travel- land", "Rail", "National rail", "", "", "passenger.km")
    S[15] = car
    S[16] = rail
    S[17] = ("Scope 3", "Business travel- air", "Flights", "Domestic, to/from UK", "Average passenger", "With RF", "passenger.km")
    S[18] = ("Scope 3", "Business travel- air", "Flights", "Short-haul, to/from UK", "Average passenger", "With RF", "passenger.km")
    S[19] = ("Scope 3", "Hotel stay", "Hotel stay", "UK", "", "", "Room per night")
    S[20] = ("Scope 3", "Business travel- land", "Taxis", "Regular taxi", "", "", "passenger.km")
    S[21] = car
    S[22] = ("Scope 3", "Business travel- land", "Bus", "Average local bus", "", "", "passenger.km")
    S[23] = rail
    S[24] = ("Scope 3", "Business travel- land", "Motorbike", "Average", "", "", "km")
    return S

def find(rows, sel):
    sc, l1, l2, l3, l4, ct, uom = sel
    hits = [r for r in rows if r["scope"] == sc and r["l1"] == l1 and r["l2"] == l2 and r["l3"] == l3
            and (l4 is None or r["l4"] == l4) and r["ct"] == ct and r["uom"] == uom]
    return hits

def label(r):
    return " > ".join([r["scope"], r["l1"], r["l2"], r["l3"], (r["l4"] or "-") + " / " + (r["ct"] or "-"), r["uom"]])

_cache = {}
def factors(year):
    if year in _cache:
        return _cache[year]
    rows = co2e_only(load(BASE, year))
    S = selectors(year)
    out = {}
    for i in sorted(S):
        hits = find(rows, S[i])
        vals = set(repr(h["factor"]) for h in hits)
        if len(hits) == 0:
            raise SystemExit(f"{year} item {i}: NO ROW for {S[i]}")
        if len(vals) != 1:
            raise SystemExit(f"{year} item {i}: AMBIGUOUS {[(label(h), h['factor']) for h in hits]}")
        f = hits[0]["factor"]
        if f is None or f == "" or not isinstance(f, (int, float)):
            raise SystemExit(f"{year} item {i}: row exists but factor is blank: {label(hits[0])} = {f!r}")
        out[i] = (label(hits[0]), f, len(hits))
    _cache[year] = out
    return out

def D(x):
    return Decimal(repr(x)) if isinstance(x, float) else Decimal(x)

def period(which, fac):
    """fac: dict item -> (row label, Decimal factor)"""
    qi = 1 if which == "baseline" else 2
    items = {}
    tot = {1: Decimal(0), 2: Decimal(0), 3: Decimal(0)}
    for i in sorted(ACT):
        q = Decimal(ACT[i][qi])
        row, f = fac[i]
        t = q * f / Decimal(1000)
        items[str(i)] = {"row": row, "quantity": int(q), "factor": float(f), "factor_exact": str(f), "tco2e": float(t), "tco2e_exact": str(t)}
        tot[ACT[i][3]] += t
    total = tot[1] + tot[2] + tot[3]
    return {"items": items, "scope1": float(tot[1]), "scope2": float(tot[2]), "scope3": float(tot[3]), "total": float(total),
            "scope1_exact": str(tot[1]), "scope2_exact": str(tot[2]), "scope3_exact": str(tot[3]), "total_exact": str(total)}

def single(year):
    return {i: (v[0], D(v[1])) for i, v in factors(year).items()}

def blended(y1, d1, y2, d2):
    a, b = factors(y1), factors(y2)
    n = Decimal(d1 + d2)
    out = {}
    for i in a:
        f = (D(a[i][1]) * d1 + D(b[i][1]) * d2) / n
        out[i] = (f"BLEND {d1}/{d1+d2} x [{y1}] {a[i][0]} + {d2}/{d1+d2} x [{y2}] {b[i][0]}", f)
    return out

def show(name, res, year):
    print(f"\n=== {name}: factor set {year} ===")
    print(f"{'#':>2} | {'factor (kg CO2e/unit)':>22} | {'qty':>8} | {'t CO2e':>14} | row")
    for k, v in res["items"].items():
        print(f"{k:>2} | {v['factor_exact']:>22} | {v['quantity']:>8} | {v['tco2e_exact']:>14} | {v['row']}")
    for s in ("scope1", "scope2", "scope3", "total"):
        print(f"   {s:7s} = {res[s+'_exact']}  -> {Decimal(res[s+'_exact']).quantize(Decimal('0.001'))}")


def q3(x):
    return str(Decimal(x).quantize(Decimal("0.001")))

def md_table(title, res):
    L = [f"### {title}", "", "| # | Category row used (Scope > Level 1 > Level 2 > Level 3 > Level 4 / Column Text > UOM) | Quantity | Factor (kg CO2e per unit) | t CO2e (unrounded) |", "|---|---|---:|---:|---:|"]
    for k, v in res["items"].items():
        L.append(f"| {k} | {v['row']} | {v['quantity']:,} | {v['factor_exact']} | {v['tco2e_exact']} |")
    L += ["", "| Total | t CO2e (unrounded) | t CO2e (3 dp) |", "|---|---:|---:|"]
    for s_, n in (("scope1", "Scope 1 (items 1-7)"), ("scope2", "Scope 2 (item 8)"), ("scope3", "Scope 3 (items 9-24)"), ("total", "Grand total")):
        L.append(f"| {n} | {res[s_+'_exact']} | {q3(res[s_+'_exact'])} |")
    return "\n".join(L) + "\n"

def strict(res, fy):
    return {"factor_year": fy,
            "items": {k: {"row": v["row"], "factor": v["factor"], "tco2e": v["tco2e"]} for k, v in res["items"].items()},
            "scope1": res["scope1"], "scope2": res["scope2"], "scope3": res["scope3"], "total": res["total"]}

runs = [
 ("baseline", "PRIMARY - Baseline 1 Jul 2019 to 30 Jun 2020, 2020 factors", period("baseline", single(2020)), 2020),
 ("current", "PRIMARY - Current 1 Apr 2024 to 31 Mar 2025, 2024 factors", period("current", single(2024)), 2024),
 ("baseline_alt_2019", "ALTERNATIVE A - Baseline with 2019 factors (strict day-count majority: 184 of 366 days fall in 2019)", period("baseline", single(2019)), 2019),
 ("baseline_alt_blended", "ALTERNATIVE B - Baseline blended (184/366 x 2019 factor + 182/366 x 2020 factor)", period("baseline", blended(2019, 184, 2020, 182)), "blended 2019/2020 (184/182 days)"),
 ("current_alt_blended", "ALTERNATIVE C - Current blended (275/365 x 2024 factor + 90/365 x 2025 factor)", period("current", blended(2024, 275, 2025, 90)), "blended 2024/2025 (275/90 days)"),
]
strict_out, detail, md = {}, {}, []
for key, title, res, fy in runs:
    show(title, res, fy)
    detail[key] = {"factor_year": fy, **res}
    if key in ("baseline", "current"):
        strict_out[key] = strict(res, fy)
    md.append(md_table(title, res))
for y in (2019, 2020, 2024, 2025):
    f = factors(y)
    print(f"year {y}: items whose selector matched more than one row: {{}}".format({i: v[2] for i, v in f.items() if v[2] != 1}))
# summary of alternatives
summ = ["| Run | Scope 1 | Scope 2 | Scope 3 | Total |", "|---|---:|---:|---:|---:|"]
for key, title, res, fy in runs:
    summ.append(f"| {title} | {q3(res['scope1_exact'])} | {q3(res['scope2_exact'])} | {q3(res['scope3_exact'])} | {q3(res['total_exact'])} |")
# per-item comparison baseline 2019 vs 2020 factors
cmp_ = ["| # | 2019 factor | 2020 factor | t CO2e (2019 factors) | t CO2e (2020 factors) | difference (2020 - 2019) |", "|---|---:|---:|---:|---:|---:|"]
a, b = runs[2][2]["items"], runs[0][2]["items"]
for k in a:
    d = Decimal(b[k]["tco2e_exact"]) - Decimal(a[k]["tco2e_exact"])
    cmp_.append(f"| {k} | {a[k]['factor_exact']} | {b[k]['factor_exact']} | {a[k]['tco2e_exact']} | {b[k]['tco2e_exact']} | {d} |")
with open(OUT + "/result.json", "w") as fh:
    json.dump(strict_out, fh, indent=1)
with open(OUT + "/result_detail.json", "w") as fh:
    json.dump(detail, fh, indent=1)
print("\n".join(md[:2]))
print("\n".join(summ))
print()
print("\n".join(cmp_))
print("written result.json, result_detail.json in", OUT)
