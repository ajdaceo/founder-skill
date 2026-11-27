"""Recalculate the EXAMPLE workbook in LibreOffice and check every headline figure by hand-computed values."""
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

from openpyxl import load_workbook

here = Path(__file__).parent
tmp = Path(tempfile.mkdtemp())
subprocess.run([sys.executable, str(here / "build.py"), str(tmp / "src")], check=True)
subprocess.run(["soffice", "--headless", "--calc", "--convert-to", "xlsx", "--outdir", str(tmp / "calc"),
                str(tmp / "src" / "Vehicle-Flip-Tracker-UK-EXAMPLE.xlsx")], check=True, capture_output=True)
wb = load_workbook(tmp / "calc" / "Vehicle-Flip-Tracker-UK-EXAMPLE.xlsx", data_only=True)
d, v, t = wb["Dashboard"], wb["Vehicles"], wb["Tax Year"]

checks = []
def eq(name, got, want, tol=0.005):
    ok = got is not None and abs(float(got) - want) <= tol
    checks.append((ok, name, got, want))

hdrs = [c.value for c in v[4]]
col = {h: i for i, h in enumerate(hdrs)}
rows = {r[0].value: r for r in v.iter_rows(min_row=5, max_row=10)}
eq("V001 total cost", rows["V001"][col["Total cost"]].value, 2586.40)
eq("V001 profit", rows["V001"][col["Net profit"]].value, 713.60)
eq("V002 profit", rows["V002"][col["Net profit"]].value, 1028.00)
eq("V003 profit", rows["V003"][col["Net profit"]].value, 555.02)
eq("V005 profit", rows["V005"][col["Net profit"]].value, -420.00)
eq("V001 days", rows["V001"][col["Days in stock"]].value, 26)
eq("V002 ROI", rows["V002"][col["ROI"]].value, 1028 / 3883, 1e-4)

k = {d.cell(row=r, column=1).value: d.cell(row=r, column=2).value for r in range(5, 16)}
eq("bought", k["Vehicles bought"], 6)
eq("sold", k["Vehicles sold"], 4)
eq("total profit", k["Total net profit (sold)"], 1876.62)
eq("avg profit", k["Average profit per sale"], 1876.62 / 4)
eq("avg days", k["Average days to sell"], (26 + 36 + 29 + 49) / 4)
eq("tied up", k["Money tied up in unsold stock"], 5980 + 4945)
eq("in stock", k["Vehicles in stock"], 2)
eq("loss sales", k["Loss-making sales"], 1)
eq("best", k["Best deal (profit)"], 1028)
eq("worst", k["Worst deal (profit)"], -420)

# Monthly table for the year in F4 (example data is 2026)
if d["F4"].value == 2026:
    eq("Jul profit", d["G12"].value, 713.60)
    eq("Sep takings", d["F14"].value, 4950)
    eq("Nov profit", d["G16"].value, -420)
    eq("year profit", d["G18"].value, 1876.62)
for r in range(5, 11):
    if t.cell(row=r, column=1).value == "2026/27":
        eq("tax year takings", t.cell(row=r, column=5).value, 12650)
        eq("tax year profit", t.cell(row=r, column=7).value, 1876.62)

da = wb["Deal Analyser"]
avg = (3495 + 3250 + 3600 + 2995) / 4
sale = avg * 0.95
costs = 0 + 120 + 80 + 60 + 45 + 0
maxbid = (sale - costs - 75 - 400) / 1.08
eq("deal avg", da["B9"].value, avg)
eq("deal sale", da["B11"].value, sale)
eq("deal max bid", da["B22"].value, maxbid)
eq("deal profit at max", da["B23"].value, 400)
cl = wb["Cost Log"]
for r in range(5, 19):
    if cl.cell(row=r, column=7).value == "Unknown Stock ID":
        checks.append((False, f"cost log row {r} unmatched", None, None))

bad = [c for c in checks if not c[0]]
for ok, name, got, want in checks:
    print("PASS" if ok else "FAIL", name, got, want)
print(f"{len(checks)-len(bad)}/{len(checks)} passed")
shutil.rmtree(tmp)
sys.exit(1 if bad else 0)
