"""Recalculate the EXAMPLE workbook in LibreOffice and check figures against hand-computed values."""
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
                str(tmp / "src" / "UK-Reseller-Tracker-EXAMPLE.xlsx")], check=True, capture_output=True)
wb = load_workbook(tmp / "calc" / "UK-Reseller-Tracker-EXAMPLE.xlsx", data_only=True)
checks = []


def eq(name, got, want, tol=0.005):
    ok = isinstance(got, (int, float)) and abs(float(got) - want) <= tol
    checks.append((ok, name, got, want))


s = wb["Sales"]
hd = [c.value for c in s[4]]
rows = {r[0].value: r for r in s.iter_rows(min_row=5, max_row=10)}
p = hd.index("Net profit")
for k, want in {"R001": 22, "R002": 32.4, "R003": 54.9, "R004": 20, "R005": -6.9}.items():
    eq(f"{k} profit", rows[k][p].value, want)
d = wb["Dashboard"]
k = {d.cell(row=r, column=1).value: d.cell(row=r, column=2).value for r in range(5, 14)}
eq("recorded", k["Items recorded"], 6)
eq("sold", k["Items sold"], 5)
eq("sales", k["Sales incl. postage charged"], 222.5)
eq("profit", k["Net profit"], 122.4)
eq("avg", k["Average profit per item"], 24.48)
eq("margin", k["Overall margin"], 122.4 / 222.5, 1e-4)
eq("days", k["Average days to sell"], 18.5)
eq("stock", k["Stock at cost (unsold)"], 35)
eq("losing", k["Items losing money"], 1)
plat = {d.cell(row=r, column=4).value: (d.cell(row=r, column=5).value, d.cell(row=r, column=6).value, d.cell(row=r, column=7).value) for r in range(6, 14)}
eq("eBay sold", plat["eBay"][0], 3)
eq("eBay sales", plat["eBay"][1], 174.5)
eq("eBay profit", plat["eBay"][2], 80.4)
pc = wb["Platform Check"]
if pc["B3"].value == 2026:
    row = {pc.cell(row=r, column=1).value: r for r in range(6, 14)}["eBay"]
    eq("pc eBay count", pc.cell(row=row, column=2).value, 3)
    checks.append((pc.cell(row=row, column=6).value == "Below thresholds", "pc status", pc.cell(row=row, column=6).value, "Below thresholds"))
t = wb["Tax Year"]
ty = {t.cell(row=r, column=1).value: r for r in range(5, 11)}
if "2025/26" in ty:
    r = ty["2025/26"]
    eq("25/26 takings", t.cell(row=r, column=5).value, 87.5)
    eq("25/26 profit", t.cell(row=r, column=6).value, 54.4)
if "2026/27" in ty:
    r = ty["2026/27"]
    eq("26/27 takings", t.cell(row=r, column=5).value, 115)
    eq("26/27 profit", t.cell(row=r, column=6).value, 48)
    eq("26/27 own", t.cell(row=r, column=7).value, 20)
bad = [c for c in checks if not c[0]]
for ok, n, g, w in checks:
    print("PASS" if ok else "FAIL", n, g, w)
print(f"{len(checks)-len(bad)}/{len(checks)} passed")
shutil.rmtree(tmp)
sys.exit(1 if bad else 0)
