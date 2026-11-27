"""Tests for the CRP generator. Expected figures are worked by hand from the published factor tables."""
import copy
import datetime as dt
import build_crp as B

F = B.load_factors()
n = 0


def ok(cond, msg):
    global n
    assert cond, msg
    n += 1


# 1. Factor year: majority rule, with half-and-half periods going to the later year
D = dt.date
ok(B.factor_year(D(2025, 1, 1), D(2025, 12, 31)) == 2025, "calendar year")
ok(B.factor_year(D(2023, 4, 1), D(2024, 3, 31)) == 2023, "April-March uses the first year")
ok(B.factor_year(D(2025, 7, 1), D(2026, 6, 30)) == 2026, "July-June uses the later year")
ok(B.factor_year(D(2024, 9, 1), D(2025, 8, 31)) == 2025, "September-August: 8 of 12 months in the later year")
ok(B.factor_year(D(2024, 2, 1), D(2025, 1, 31)) == 2024, "February-January")
for bad in ((D(2025, 1, 1), D(2025, 6, 30)), (D(2025, 1, 1), D(2024, 12, 31)), (D(2024, 1, 1), D(2025, 6, 30))):
    try:
        B.factor_year(*bad); raise AssertionError("bad period accepted")
    except B.InputError:
        n += 1

# 2. Published factors spot-checked against the official tables (kg CO2e per unit)
for year, key, value in ((2026, "electricity_kwh", 0.13096), (2025, "electricity_kwh", 0.177), (2024, "electricity_kwh", 0.20705),
                         (2023, "electricity_kwh", 0.20707), (2022, "electricity_kwh", 0.19338), (2021, "electricity_kwh", 0.21233),
                         (2020, "electricity_kwh", 0.23314), (2019, "electricity_kwh", 0.2556), (2024, "natural_gas_kwh", 0.1829),
                         (2023, "natural_gas_kwh", 0.18293), (2024, "diesel_litre", 2.51279), (2023, "diesel_litre", 2.51206),
                         (2026, "diesel_litre", 2.58354), (2026, "waste_landfill_tonne", 520.58023), (2026, "rail_km", 0.03092)):
    ok(abs(F[(year, key)]["factor"] - value) < 6e-6, f"{year} {key}: {F[(year, key)]['factor']} != {value}")
ok(F[(2026, "electricity_kwh")]["scope"] == 2 and F[(2026, "natural_gas_kwh")]["scope"] == 1 and F[(2026, "van_diesel_km")]["scope"] == 3, "scopes")
ok((2023, "waste_recycled_tonne") not in F and (2026, "waste_recycled_tonne") in F, "unpublished factor is absent, not guessed")
ok(all(v["factor"] >= 0 for v in F.values()) and len({y for y, _ in F}) == 9, "nine years, no negative factors")

# 3. Hand-worked plan. Baseline April 2023-March 2024 -> 2023 factors. Current calendar 2025 -> 2025 factors.
C = {"supplier": "Test Foods Ltd", "publication_date": "2026-05-01", "net_zero_year": 2045,
     "baseline": {"label": "2023/24", "period_start": "2023-04-01", "period_end": "2024-03-31",
                  "activities": {"electricity_kwh": 100000, "natural_gas_kwh": 50000, "diesel_litre": 10000, "car_km": 20000,
                                 "commute_km": 100000, "waste_landfill_tonne": 5}},
     "current": {"label": "2025", "period_start": "2025-01-01", "period_end": "2025-12-31",
                 "activities": {"electricity_kwh": 90000, "natural_gas_kwh": 45000, "diesel_litre": 9000, "car_km": 20000,
                                "commute_km": 100000, "waste_landfill_tonne": 4, "downstream:van_diesel_km": 10000}},
     "scope3_not_applicable": {"4": "Suppliers deliver on their own account; no transport is bought.", "9": "Customers collect."},
     "target_pct": 20, "target_year": 2031, "projects_done": ["LED lighting"], "projects_planned": ["Electric vans"],
     "signatory_name": "A Director", "signatory_role": "Managing Director"}
plan, calc, qa = B.build(copy.deepcopy(C), F)
# 2023: gas 50000*0.18293=9146.5; diesel 10000*2.51206=25120.6 -> Scope 1 34.267 t. Electricity 100000*0.20707=20.707 t.
# Scope 3: car 20000*0.16664=3.333; commute 100000*0.16664=16.664; landfill 5*520.33474=2.602 -> 22.599 t. Total 77.573 t.
ok(qa["baseline_factor_year"] == 2023 and qa["current_factor_year"] == 2025, "factor years")
ok(abs(qa["baseline_tco2e"]["1"] - 34.267) < 0.002 and abs(qa["baseline_tco2e"]["2"] - 20.707) < 0.002, f"baseline scopes 1-2 {qa['baseline_tco2e']}")
ok(abs(qa["baseline_tco2e"]["3"] - 22.599) < 0.002 and abs(qa["baseline_tco2e"]["total"] - 77.573) < 0.004, f"baseline scope 3 {qa['baseline_tco2e']}")
# 2025: electricity 90000*0.177=15.93 t. Gas 45000*0.18296=8.2332; diesel 9000*2.57082=23.13738 -> 31.371 t.
ok(abs(qa["current_tco2e"]["2"] - 15.93) < 0.001 and abs(qa["current_tco2e"]["1"] - 31.371) < 0.002, f"current scopes {qa['current_tco2e']}")
ok(qa["status"] == "pass" and not qa["errors"], f"status {qa}")
for s in ("**Supplier name:** Test Foods Ltd", "Net Zero emissions by 2045", "PPN 006", "| Scope 2 | 20.71 |", "reduction of 20%",
          "Downstream transportation and distribution | 2.", "Not applicable: Suppliers deliver", "A Director, Managing Director"):
    ok(s in plan, f"plan text missing: {s}")
ok("2023 factors" in calc and "2025 factors" in calc and "Electricity: UK" in calc, "calculation record shows factor years and sources")
target_line = [l for l in plan.splitlines() if l.startswith("We project")][0]
ok(f"{qa['current_tco2e']['total'] * 0.8:,.2f}" in target_line, "target is 20% below current total")


# 4. Blocking errors: nothing is issued
def blocked(change, expect):
    c = copy.deepcopy(C)
    change(c)
    try:
        plan, _, qa = B.build(c, F)
        msgs = qa["errors"]
    except B.InputError as e:
        plan, msgs = None, [str(e)]
    ok(plan is None and any(expect in m for m in msgs), f"expected block '{expect}', got {msgs}")


blocked(lambda c: c["scope3_not_applicable"].pop("4"), "Scope 3 category 4")
blocked(lambda c: c.update(net_zero_year=2055), "2050 or earlier")
blocked(lambda c: c["current"]["activities"].update(bitcoin_mined=3), "unknown activity")
blocked(lambda c: c["current"]["activities"].update(electricity_kwh=-5), "zero or more")
blocked(lambda c: c["baseline"]["activities"].update(waste_recycled_tonne=2), "no 2023 factor published")
blocked(lambda c: c["current"].update(period_end="2025-06-30"), "about 12 months")
blocked(lambda c: c.update(publication_date="2025-06-01"), "after the publication date")
blocked(lambda c: c.update(projects_done=[], projects_planned=[]), "carbon reduction measure")
blocked(lambda c: c.update(signatory_name=""), "Missing field: signatory_name")
blocked(lambda c: c["current"]["activities"].update({"downstream:car_km": 5}), "only applies to transport")

# 5. Warnings do not block but are recorded
c = copy.deepcopy(C)
c["current"]["activities"]["electricity_kwh"] = 0
c["current"]["activities"]["diesel_litre"] = 100
plan, _, qa = B.build(c, F)
ok(plan and qa["status"] == "review" and any("No electricity" in w for w in qa["warnings"]) and any("changed" in w for w in qa["warnings"]), f"warnings {qa['warnings']}")
print(f"{n}/{n} pass")
