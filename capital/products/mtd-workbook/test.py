"""End-to-end test: build, fill with sample data, recalculate in LibreOffice, compare with independent Python maths."""
import subprocess, sys, os, tempfile, datetime as dt, random, shutil
from openpyxl import load_workbook
D = dt.date; here = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, here)
tmp = tempfile.mkdtemp(); src = os.path.join(tmp, "t.xlsx")
subprocess.run([sys.executable, os.path.join(here, "build.py"), src], check=True, capture_output=True)
import importlib.util
def cats():
    ns = {}; code = open(os.path.join(here, "build.py")).read().split("wb = Workbook()")[0]
    exec(code, ns); return ns
C = cats()

def run(year, mode, mileage, seed):
    random.seed(seed)
    wb = load_workbook(src)
    wb["Settings"]["B4"] = year; wb["Settings"]["B5"] = mode; wb["Settings"]["B6"] = "Yes" if mileage else "No"
    wb["Tax_Estimate"]["B4"] = 8000
    start = D(year, 4, 6) if mode == "Standard" else D(year, 4, 1)
    ends = ([D(year,7,5),D(year,10,5),D(year+1,1,5),D(year+1,4,5)] if mode == "Standard"
            else [D(year,6,30),D(year,9,30),D(year,12,31),D(year+1,3,31)])
    def rdate():  # includes boundary dates and out-of-year dates
        pool = [start, start - dt.timedelta(days=1)] + ends + [e + dt.timedelta(days=1) for e in ends]
        return random.choice(pool) if random.random() < .3 else start + dt.timedelta(days=random.randint(-20, 385))
    exp = {}
    def add(key, d, amt):
        for q, e in enumerate(ends):
            if start <= d <= e: exp[(key, q)] = exp.get((key, q), 0) + amt
    def fill(sheet, catlist, priv):
        ws = wb[sheet]
        for r in range(2, 302):
            d, cat, amt = rdate(), random.choice(catlist), round(random.uniform(1, 3000), 2)
            ws[f"A{r}"] = d; ws[f"D{r}"] = cat; ws[f"E{r}"] = amt; p = 0
            if priv and random.random() < .2: p = round(amt * random.random(), 2); ws[f"F{r}"] = p
            add((sheet, cat), d, round(amt - p, 2))
    fill("SE_Income", C["SE_INCOME"], False); fill("SE_Expenses", C["SE_EXP"], True)
    fill("Prop_Income", C["P_INCOME"], False); fill("Prop_Expenses", C["P_EXP"] + [C["RES_FIN"]], True)
    miles = [0]*4
    for r in range(2, 202):
        d, m = rdate(), random.randint(1, 180); wb["Mileage"][f"A{r}"] = d; wb["Mileage"][f"C{r}"] = m
        for q, e in enumerate(ends):
            if start <= d <= e: miles[q] += m
    f = os.path.join(tmp, f"case{seed}.xlsx"); wb.save(f)
    out = os.path.join(tmp, f"out{seed}"); os.makedirs(out)
    subprocess.run(["soffice", "--headless", "--convert-to", "xlsx", "--outdir", out, f], check=True, capture_output=True)
    v = load_workbook(os.path.join(out, f"case{seed}.xlsx"), data_only=True)
    n = 0
    def check(name, got, want):
        nonlocal n; n += 1
        assert got is not None and abs(got - want) < 0.005, f"{name}: got {got} want {want} (year={year},{mode})"
    def summ(sname, inc, expn, ilist, elist, extra=None):
        ws = v[sname]; rows = {ws[f"A{r}"].value: r for r in range(5, 45) if ws[f"A{r}"].value}
        tots = []
        for q, col in enumerate("BCDE"):
            ti = te = 0
            for cat in ilist:
                w = exp.get(((inc, cat), q), 0); ti += w; check(f"{sname} {cat} Q{q+1}", ws[f"{col}{rows[cat]}"].value, w)
            for cat in elist:
                w = exp.get(((expn, cat), q), 0)
                if sname == "SE_Summary" and cat == C["TRAVEL"] and mileage:
                    w += min(miles[q], 10000)*.45 + max(miles[q]-10000, 0)*.25
                te += w; check(f"{sname} {cat} Q{q+1}", ws[f"{col}{rows[cat]}"].value, w)
            check("total income", ws[f"{col}{rows['Total income']}"].value, ti)
            check("total exp", ws[f"{col}{rows['Total allowable expenses']}"].value, te)
            check("net", ws[f"{col}{rows['Net profit (or loss)']}"].value, ti - te)
            if extra: check("resfin", ws[f"{col}{rows[extra]}"].value, exp.get(((expn, extra), q), 0))
            tots.append(ti - te)
        # quarter-only columns reconcile to cumulative
        r = rows["Net profit (or loss)"]
        check("q-only sum", sum(ws[f"{c}{r}"].value for c in "FGHI"), tots[3])
        return tots[3]
    sp = summ("SE_Summary", "SE_Income", "SE_Expenses", C["SE_INCOME"], C["SE_EXP"])
    pp = summ("Prop_Summary", "Prop_Income", "Prop_Expenses", C["P_INCOME"], C["P_EXP"], C["RES_FIN"])
    dl = v["Deadlines"]
    for q in range(4):
        assert dl[f"C{5+q}"].value.date() == ends[q], "period end"; n += 1
    assert dl["B5"].value.date() == start and dl["E5"].value.date() == D(year, 8, 7) and dl["E8"].value.date() == D(year+1, 5, 7)
    assert dl["E10"].value.date() == D(year+2, 1, 31)
    # tax estimate
    t = v["Tax_Estimate"]; other = 8000
    def tax(x): return min(x, 37700)*.2 + max(0, min(x, 125140) - 37700)*.4 + max(0, x - 125140)*.45
    ti = max(0, max(0, sp) + max(0, pp) + other - 12570)
    it = tax(ti) - tax(max(0, other - 12570))
    upl = (0.02 if year >= 2027 else 0) * max(0, min(max(0, pp), ti))
    c4 = max(0, min(sp, 50270) - 12570)*.06 + max(0, sp - 50270)*.02
    check("set aside", t["B25"].value, it + upl + c4)
    # quarter labels
    ws = v["SE_Income"]
    for r in range(2, 302):
        d = ws[f"A{r}"].value.date()
        want = "Before" if d < start else next((f"Q{i+1}" for i, e in enumerate(ends) if d <= e), "After")
        assert ws[f"F{r}"].value == want, (d, ws[f"F{r}"].value, want); n += 1
    return n

total = 0
for i, (y, m, mi) in enumerate([(2027, "Standard", True), (2027, "Calendar", False), (2026, "Standard", False), (2028, "Calendar", True)]):
    total += run(y, m, mi, i + 1)
# empty workbook must calculate to zero with no errors
out = os.path.join(tmp, "empty"); os.makedirs(out)
subprocess.run(["soffice", "--headless", "--convert-to", "xlsx", "--outdir", out, src], check=True, capture_output=True)
v = load_workbook(os.path.join(out, "t.xlsx"), data_only=True)
for ws in v:
    for row in ws.iter_rows():
        for c in row:
            assert not (isinstance(c.value, str) and c.value.startswith(("#", "Err:"))), f"error value {ws.title}!{c.coordinate}"
assert v["Tax_Estimate"]["B25"].value == 0
shutil.rmtree(tmp); print(f"PASS: {total} checks")
