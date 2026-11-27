"""Loader for DESNZ/BEIS flat-file conversion factors. Data only; run with python3 -I."""
import openpyxl

def load(base, year):
    p = f"{base}/{year}/flat.xlsx"
    wb = openpyxl.load_workbook(p, read_only=True, data_only=True)
    ws = wb["Factors by Category"]
    rows = list(ws.iter_rows(values_only=True))
    # find header row
    hi = None
    for i, r in enumerate(rows[:15]):
        vals = [str(c).strip() if c is not None else "" for c in r]
        if "Scope" in vals and "Level 1" in vals:
            hi = i
            hdr = vals
            break
    assert hi is not None, year
    def col(name_opts):
        for n in name_opts:
            if n in hdr:
                return hdr.index(n)
        raise KeyError((year, name_opts, hdr))
    c_scope = col(["Scope"]); c_l1 = col(["Level 1"]); c_l2 = col(["Level 2"]); c_l3 = col(["Level 3"])
    c_l4 = col(["Level 4"]); c_ct = col(["Column Text"]); c_uom = col(["UOM"])
    c_ghg = col(["GHG", "GHG/Unit"])
    c_f = None
    for j, h in enumerate(hdr):
        if h.startswith("GHG Conversion Factor"):
            c_f = j
            assert str(year) in h, (year, h)
    assert c_f is not None
    out = []
    for r in rows[hi+1:]:
        if r is None or all(c is None for c in r):
            continue
        def g(j):
            v = r[j] if j < len(r) else None
            return "" if v is None else str(v)
        out.append({
            "scope": g(c_scope), "l1": g(c_l1), "l2": g(c_l2), "l3": g(c_l3), "l4": g(c_l4),
            "ct": g(c_ct), "uom": g(c_uom), "ghg": g(c_ghg), "factor": r[c_f] if c_f < len(r) else None,
        })
    return out

def co2e_only(rows):
    return [r for r in rows if r["ghg"] == "kg CO2e"]
