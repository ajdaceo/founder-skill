import build_crp as B
F = {"electricity_kwh": (0.2, 2, "kWh"), "diesel_litre": (2.5, 1, "litre"), "car_km": (0.17, 3, "km")}
c = {"supplier": "Test Foods Ltd", "publication_date": "Dec 2026", "baseline_year": "2024", "reporting_year": "2025",
     "net_zero_year": 2050, "baseline": {"electricity_kwh": 100000, "diesel_litre": 10000, "car_km": 10000},
     "current": {"electricity_kwh": 90000, "diesel_litre": 9000, "car_km": 10000}, "target_pct": 20, "target_year": 2030,
     "projects_done": ["LED lighting"], "projects_planned": ["EV vans"], "signatory_name": "A Director", "signatory_role": "Managing Director"}
md, b, cur = B.render(c, F)
assert abs(b[1] - 25.0) < 1e-9 and abs(b[2] - 20.0) < 1e-9 and abs(b[3] - 1.7) < 1e-9 and abs(b["total"] - 46.7) < 1e-9
assert abs(cur["total"] - (18 + 22.5 + 1.7)) < 1e-9
for s in ["Supplier name:** Test Foods Ltd", "PPN 006", "Net Zero emissions by 2050", "| Total emissions | 46.70 |", "reduction of 20%"]:
    assert s in md, s
import os, tempfile
real = B.load_factors()
assert len(real) == 9 and all(v[0] > 0 for v in real.values()), "factors.csv must hold 9 positive DESNZ factors"
assert real["electricity_kwh"] == (0.13096, 2, "kWh") and real["natural_gas_kwh"][1] == 1 and real["van_diesel_km"][1] == 3
with tempfile.NamedTemporaryFile("w", suffix=".csv", delete=False) as t:
    t.write("key,unit,kgco2e_per_unit,scope,source\nx,kWh,,1,blank\n")
try:
    B.load_factors(t.name); raise AssertionError("blank factors should refuse")
except SystemExit as e:
    assert "Factor missing" in str(e)
finally:
    os.unlink(t.name)
print("8/8 pass")
