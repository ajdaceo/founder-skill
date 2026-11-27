"""Build the UK Vehicle Flipping Profit Tracker (Excel + Google Sheets compatible).

Usage: python3 build.py [outdir]
Produces: Vehicle-Flip-Tracker-UK.xlsx (blank) and Vehicle-Flip-Tracker-UK-EXAMPLE.xlsx (sample data).
Only functions that exist in both Excel and Google Sheets are used.
"""
import sys
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import CellIsRule, FormulaRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

VERSION = "1.0.0"
ROWS = 300  # vehicle rows
COST_ROWS = 1500
NAVY = "1F2A44"
ACCENT = "2E7D5B"
LIGHT = "EEF2F7"
INPUT = "FFF8E1"
WHITE = "FFFFFF"
thin = Side(style="thin", color="D0D7E2")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
HFONT = Font(name="Arial", bold=True, color=WHITE, size=10)
BFONT = Font(name="Arial", size=10)
GBP = '£#,##0;[Red]-£#,##0'
GBP2 = '£#,##0.00;[Red]-£#,##0.00'
PCT = '0.0%;[Red]-0.0%'
DATE = 'dd/mm/yyyy'

SOURCES = ["Auction", "Private seller", "Trade", "Part-exchange", "Online marketplace", "Other"]
STATUSES = ["Buying", "In prep", "Listed", "Sold", "Scrapped / written off"]
CHANNELS = ["Private sale", "AutoTrader", "eBay", "Facebook Marketplace", "Gumtree", "Trade / auction", "Other"]
COST_TYPES = ["Parts", "Labour", "MOT / service", "Valeting", "Transport", "Advertising", "Fuel", "Insurance / road tax", "Admin / HPI check", "Other"]

# Vehicles sheet columns: (header, width, kind)
VCOLS = [
    ("Stock ID", 10, "in"), ("Reg", 11, "in"), ("Make", 12, "in"), ("Model", 14, "in"), ("Year", 7, "in"),
    ("Mileage in", 10, "in"), ("Source", 15, "list:src"), ("Purchase date", 12, "date"),
    ("Purchase price", 12, "gbp"), ("Buyer's fees", 11, "gbp"), ("Logged costs", 12, "calc"),
    ("Total cost", 12, "calc"), ("Listed date", 12, "date"), ("Asking price", 12, "gbp"),
    ("Sale date", 12, "date"), ("Sale price", 12, "gbp"), ("Selling fees", 11, "gbp"),
    ("Sold via", 16, "list:ch"), ("Net profit", 12, "calc"), ("ROI", 8, "calc"), ("Days in stock", 9, "calc"),
    ("Status", 14, "list:st"), ("Notes", 30, "in"),
]
COL = {h: get_column_letter(i + 1) for i, (h, _, _) in enumerate(VCOLS)}


def hdr(ws, row, values, widths=None, fill=NAVY):
    for i, v in enumerate(values, start=1):
        c = ws.cell(row=row, column=i, value=v)
        c.font = HFONT
        c.fill = PatternFill("solid", fgColor=fill)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        c.border = BORDER
        if widths:
            ws.column_dimensions[get_column_letter(i)].width = widths[i - 1]
    ws.row_dimensions[row].height = 30


def title(ws, text, sub=None):
    ws["A1"] = text
    ws["A1"].font = Font(name="Arial", bold=True, size=16, color=NAVY)
    if sub:
        ws["A2"] = sub
        ws["A2"].font = Font(name="Arial", italic=True, size=9, color="5A6475")


def build(example: bool) -> Workbook:
    wb = Workbook()

    # ---------- Start Here ----------
    s = wb.active
    s.title = "Start Here"
    s.sheet_view.showGridLines = False
    s.column_dimensions["A"].width = 3
    s.column_dimensions["B"].width = 100
    s["B2"] = "UK Vehicle Flipping Profit Tracker"
    s["B2"].font = Font(name="Arial", bold=True, size=20, color=NAVY)
    s["B3"] = f"Version {VERSION}. Works in Microsoft Excel and Google Sheets (File > Import, or open from Google Drive)."
    s["B3"].font = Font(name="Arial", size=10, color="5A6475")
    lines = [
        ("How it works", True),
        ("1. Vehicles: one row per car, van or bike you buy. Yellow cells are for you; white cells calculate themselves.", False),
        ("2. Cost Log: every extra cost (parts, labour, MOT, valeting, transport, adverts). Use the same Stock ID as the vehicle. Totals flow into the Vehicles sheet automatically.", False),
        ("3. When a vehicle sells, enter the sale date, sale price and any selling fees, and set Status to Sold.", False),
        ("4. Dashboard: profit, average days to sell, money tied up in stock, best and worst deals, and month-by-month results for the year you pick.", False),
        ("5. Tax Year: takings and profit by UK tax year (6 April to 5 April), to make your records easier to keep.", False),
        ("", False),
        ("Tips", True),
        ("Give every vehicle a short Stock ID (e.g. V001) and use it in the Cost Log. Logged costs only count when the IDs match exactly.", False),
        ("Buyer's fees = auction buyer's premium, online bidding fee or anything paid to buy the vehicle on top of the hammer price.", False),
        ("Selling fees = advert listing fees, marketplace fees or auction seller's fees paid when selling.", False),
        ("Delete the sample rows in the EXAMPLE file, or start from the blank file.", False),
        ("", False),
        ("Important", True),
        ("This is a record-keeping tool, not tax, legal or accounting advice. Check your own obligations with HMRC or an accountant.", False),
        ("Trading allowance and Self Assessment: https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income", False),
        ("Selling vehicles regularly for profit can count as trading. HMRC guidance: https://www.gov.uk/working-for-yourself", False),
        ("If you are VAT registered or use the second-hand margin scheme, keep the records HMRC requires; this tracker does not calculate VAT.", False),
    ]
    r = 5
    for text, bold in lines:
        c = s.cell(row=r, column=2, value=text)
        c.font = Font(name="Arial", size=12 if bold else 10, bold=bold, color=NAVY if bold else "222222")
        c.alignment = Alignment(wrap_text=True, vertical="top")
        r += 1

    # ---------- Lists (hidden) ----------
    L = wb.create_sheet("Lists")
    for ci, (name, items) in enumerate([("Source", SOURCES), ("Status", STATUSES), ("Sold via", CHANNELS), ("Cost type", COST_TYPES)], start=1):
        L.cell(row=1, column=ci, value=name).font = Font(bold=True)
        for ri, it in enumerate(items, start=2):
            L.cell(row=ri, column=ci, value=it)
    L.sheet_state = "hidden"

    # ---------- Vehicles ----------
    v = wb.create_sheet("Vehicles", 1)
    title(v, "Vehicles", "Yellow = your input. One row per vehicle. Status 'Sold' needs a sale date and sale price.")
    hdr(v, 4, [h for h, _, _ in VCOLS], [w for _, w, _ in VCOLS])
    v.freeze_panes = "C5"
    first, last = 5, 4 + ROWS
    dv_src = DataValidation(type="list", formula1=f"=Lists!$A$2:$A${len(SOURCES)+1}", allow_blank=True)
    dv_st = DataValidation(type="list", formula1=f"=Lists!$B$2:$B${len(STATUSES)+1}", allow_blank=True)
    dv_ch = DataValidation(type="list", formula1=f"=Lists!$C$2:$C${len(CHANNELS)+1}", allow_blank=True)
    for dv in (dv_src, dv_st, dv_ch):
        v.add_data_validation(dv)
    dv_src.add(f"{COL['Source']}{first}:{COL['Source']}{last}")
    dv_st.add(f"{COL['Status']}{first}:{COL['Status']}{last}")
    dv_ch.add(f"{COL['Sold via']}{first}:{COL['Sold via']}{last}")
    for row in range(first, last + 1):
        A = COL["Stock ID"]
        f = {
            "Logged costs": f'=IF({A}{row}="","",SUMIFS(\'Cost Log\'!$D:$D,\'Cost Log\'!$B:$B,{A}{row}))',
            "Total cost": f'=IF({A}{row}="","",N({COL["Purchase price"]}{row})+N({COL["Buyer\'s fees"]}{row})+N({COL["Logged costs"]}{row}))',
            "Net profit": f'=IF({COL["Sale price"]}{row}="","",{COL["Sale price"]}{row}-N({COL["Selling fees"]}{row})-{COL["Total cost"]}{row})',
            "ROI": f'=IF(OR({COL["Net profit"]}{row}="",N({COL["Total cost"]}{row})=0),"",{COL["Net profit"]}{row}/{COL["Total cost"]}{row})',
            "Days in stock": f'=IF({COL["Purchase date"]}{row}="","",IF({COL["Sale date"]}{row}="",TODAY(),{COL["Sale date"]}{row})-{COL["Purchase date"]}{row})',
        }
        for ci, (h, _, kind) in enumerate(VCOLS, start=1):
            c = v.cell(row=row, column=ci)
            c.border = BORDER
            c.font = BFONT
            if kind == "calc":
                c.value = f[h]
                c.fill = PatternFill("solid", fgColor=LIGHT)
            else:
                c.fill = PatternFill("solid", fgColor=INPUT)
            if kind in ("gbp",) or h in ("Logged costs", "Total cost", "Net profit"):
                c.number_format = GBP
            if kind == "date":
                c.number_format = DATE
            if h == "ROI":
                c.number_format = PCT
            if h in ("Mileage in",):
                c.number_format = "#,##0"
            if h == "Days in stock":
                c.number_format = "0"
    np_rng = f"{COL['Net profit']}{first}:{COL['Net profit']}{last}"
    v.conditional_formatting.add(np_rng, CellIsRule(operator="lessThan", formula=["0"], font=Font(color="C62828", bold=True)))
    v.conditional_formatting.add(np_rng, CellIsRule(operator="greaterThan", formula=["0"], font=Font(color=ACCENT, bold=True)))
    st = COL["Status"]
    v.conditional_formatting.add(f"A{first}:{get_column_letter(len(VCOLS))}{last}",
        FormulaRule(formula=[f'AND(${st}{first}="Sold",OR(${COL["Sale date"]}{first}="",${COL["Sale price"]}{first}=""))'],
                    fill=PatternFill("solid", fgColor="FDE2E2")))

    # ---------- Cost Log ----------
    cl = wb.create_sheet("Cost Log", 2)
    title(cl, "Cost Log", "Every cost after purchase. Stock ID must match the Vehicles sheet.")
    hdr(cl, 4, ["Date", "Stock ID", "Cost type", "Amount", "Supplier", "Description", "Vehicle"], [12, 10, 18, 11, 18, 36, 26])
    cl.freeze_panes = "A5"
    dv_ct = DataValidation(type="list", formula1=f"=Lists!$D$2:$D${len(COST_TYPES)+1}", allow_blank=True)
    cl.add_data_validation(dv_ct)
    dv_ct.add(f"C5:C{4+COST_ROWS}")
    for row in range(5, 5 + COST_ROWS):
        for ci in range(1, 8):
            c = cl.cell(row=row, column=ci)
            c.border = BORDER
            c.font = BFONT
            c.fill = PatternFill("solid", fgColor=LIGHT if ci == 7 else INPUT)
        cl.cell(row=row, column=1).number_format = DATE
        cl.cell(row=row, column=4).number_format = GBP2
        cl.cell(row=row, column=7).value = (
            f'=IF(B{row}="","",IFERROR(INDEX(Vehicles!$C:$C,MATCH(B{row},Vehicles!$A:$A,0))&" "&'
            f'INDEX(Vehicles!$D:$D,MATCH(B{row},Vehicles!$A:$A,0)),"Unknown Stock ID"))')
    cl.conditional_formatting.add(f"G5:G{4+COST_ROWS}", CellIsRule(operator="equal", formula=['"Unknown Stock ID"'], font=Font(color="C62828", bold=True)))

    # ---------- Dashboard ----------
    d = wb.create_sheet("Dashboard", 0)
    d.sheet_view.showGridLines = False
    title(d, "Dashboard", "Updates automatically from Vehicles and Cost Log.")
    for col, w in zip("ABCDEFGH", [30, 16, 4, 14, 14, 14, 14, 14]):
        d.column_dimensions[col].width = w
    V = "Vehicles!"
    sold = f'{V}${st}$5:${st}${last},"Sold"'
    rngs = {k: f"{V}${COL[k]}$5:${COL[k]}${last}" for k in ("Net profit", "Total cost", "Days in stock", "Sale price", "Stock ID", "Status", "Sale date", "Source", "Sold via")}
    kpis = [
        ("Vehicles bought", f'=COUNTA({rngs["Stock ID"]})', "0"),
        ("Vehicles sold", f'=COUNTIF({rngs["Status"]},"Sold")', "0"),
        ("Total net profit (sold)", f'=SUMIFS({rngs["Net profit"]},{sold})', GBP),
        ("Average profit per sale", f'=IFERROR(AVERAGEIFS({rngs["Net profit"]},{sold}),0)', GBP),
        ("Average ROI per sale", f'=IFERROR(SUMIFS({rngs["Net profit"]},{sold})/SUMIFS({rngs["Total cost"]},{sold}),0)', PCT),
        ("Average days to sell", f'=IFERROR(AVERAGEIFS({rngs["Days in stock"]},{sold}),0)', "0"),
        ("Money tied up in unsold stock", f'=SUMIFS({rngs["Total cost"]},{rngs["Status"]},"<>Sold",{rngs["Status"]},"<>Scrapped / written off")', GBP),
        ("Vehicles in stock", f'=COUNTIFS({rngs["Stock ID"]},"<>",{rngs["Status"]},"<>Sold",{rngs["Status"]},"<>Scrapped / written off")', "0"),
        ("Loss-making sales", f'=COUNTIFS({rngs["Status"]},"Sold",{rngs["Net profit"]},"<0")', "0"),
        ("Best deal (profit)", f'=IF(COUNTIF({rngs["Status"]},"Sold")=0,0,MAX({rngs["Net profit"]}))', GBP),
        ("Worst deal (profit)", f'=IF(COUNTIF({rngs["Status"]},"Sold")=0,0,MIN({rngs["Net profit"]}))', GBP),
    ]
    d["A4"] = "Headline numbers"
    d["A4"].font = Font(name="Arial", bold=True, size=12, color=NAVY)
    for i, (label, formula, fmt) in enumerate(kpis, start=5):
        a = d.cell(row=i, column=1, value=label)
        b = d.cell(row=i, column=2, value=formula)
        a.font = BFONT
        b.font = Font(name="Arial", bold=True, size=11, color=NAVY)
        b.number_format = fmt
        for c in (a, b):
            c.border = BORDER
            c.fill = PatternFill("solid", fgColor=LIGHT)
    # Monthly table
    d["D4"] = "Year to show:"
    d["D4"].font = Font(name="Arial", bold=True, size=11, color=NAVY)
    d["F4"] = date.today().year
    d["F4"].fill = PatternFill("solid", fgColor=INPUT)
    d["F4"].border = BORDER
    hdr_cells = ["Month", "Sold", "Takings", "Profit", "Avg days"]
    for i, h in enumerate(hdr_cells):
        c = d.cell(row=5, column=4 + i, value=h)
        c.font = HFONT
        c.fill = PatternFill("solid", fgColor=NAVY)
        c.alignment = Alignment(horizontal="center")
    for m in range(1, 13):
        r = 5 + m
        start = f"DATE($F$4,{m},1)"
        end = f"EOMONTH(DATE($F$4,{m},1),0)"
        crit = f'{rngs["Status"]},"Sold",{rngs["Sale date"]},">="&{start},{rngs["Sale date"]},"<="&{end}'
        d.cell(row=r, column=4, value=f"=DATE($F$4,{m},1)").number_format = "mmm yyyy"
        d.cell(row=r, column=5, value=f"=COUNTIFS({crit})").number_format = "0"
        d.cell(row=r, column=6, value=f"=SUMIFS({rngs['Sale price']},{crit})").number_format = GBP
        d.cell(row=r, column=7, value=f"=SUMIFS({rngs['Net profit']},{crit})").number_format = GBP
        d.cell(row=r, column=8, value=f"=IFERROR(AVERAGEIFS({rngs['Days in stock']},{crit}),\"\")").number_format = "0"
        for ci in range(4, 9):
            d.cell(row=r, column=ci).border = BORDER
            d.cell(row=r, column=ci).font = BFONT
    tr = 18
    d.cell(row=tr, column=4, value="Year total").font = Font(name="Arial", bold=True)
    for ci, colL in zip(range(5, 8), "EFG"):
        c = d.cell(row=tr, column=ci, value=f"=SUM({colL}6:{colL}17)")
        c.font = Font(name="Arial", bold=True)
        c.number_format = "0" if colL == "E" else GBP
        c.border = BORDER
    d.conditional_formatting.add("G6:G18", CellIsRule(operator="lessThan", formula=["0"], font=Font(color="C62828", bold=True)))
    # Profit by source and channel
    r0 = 18
    d.cell(row=r0, column=1, value="Profit by where you bought").font = Font(name="Arial", bold=True, size=12, color=NAVY)
    for i, sname in enumerate(SOURCES, start=1):
        d.cell(row=r0 + i, column=1, value=sname).font = BFONT
        c = d.cell(row=r0 + i, column=2, value=f'=SUMIFS({rngs["Net profit"]},{sold},{rngs["Source"]},A{r0+i})')
        c.number_format = GBP
        c.border = BORDER
    r1 = r0 + len(SOURCES) + 2
    d.cell(row=r1, column=1, value="Profit by where you sold").font = Font(name="Arial", bold=True, size=12, color=NAVY)
    for i, cname in enumerate(CHANNELS, start=1):
        d.cell(row=r1 + i, column=1, value=cname).font = BFONT
        c = d.cell(row=r1 + i, column=2, value=f'=SUMIFS({rngs["Net profit"]},{sold},{rngs["Sold via"]},A{r1+i})')
        c.number_format = GBP
        c.border = BORDER

    # ---------- Tax Year ----------
    t = wb.create_sheet("Tax Year", 3)
    t.sheet_view.showGridLines = False
    title(t, "UK tax year summary", "Tax years run 6 April to 5 April. Record-keeping aid only; not tax advice.")
    hdr(t, 4, ["Tax year", "Starts", "Ends", "Vehicles sold", "Gross takings", "Purchase & costs of sold vehicles", "Net profit", "Takings above £1,000?"], [12, 12, 12, 12, 14, 18, 14, 16])
    base = date.today().year - 2
    for i in range(6):
        r = 5 + i
        y = base + i
        t.cell(row=r, column=1, value=f"{y}/{str(y+1)[2:]}")
        t.cell(row=r, column=2, value=f"=DATE({y},4,6)").number_format = DATE
        t.cell(row=r, column=3, value=f"=DATE({y+1},4,5)").number_format = DATE
        crit = f'{rngs["Status"]},"Sold",{rngs["Sale date"]},">="&B{r},{rngs["Sale date"]},"<="&C{r}'
        t.cell(row=r, column=4, value=f"=COUNTIFS({crit})").number_format = "0"
        t.cell(row=r, column=5, value=f"=SUMIFS({rngs['Sale price']},{crit})").number_format = GBP
        t.cell(row=r, column=6, value=f"=SUMIFS({rngs['Total cost']},{crit})").number_format = GBP
        t.cell(row=r, column=7, value=f"=SUMIFS({rngs['Net profit']},{crit})").number_format = GBP
        t.cell(row=r, column=8, value=f'=IF(E{r}>1000,"Yes - check HMRC","No")')
        for ci in range(1, 9):
            t.cell(row=r, column=ci).border = BORDER
            t.cell(row=r, column=ci).font = BFONT
    t["A12"] = "The £1,000 trading allowance and Self Assessment rules: https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income"
    t["A12"].font = Font(name="Arial", size=9, color="5A6475")

    if example:
        add_example(v, cl)
    wb.properties.title = "UK Vehicle Flipping Profit Tracker"
    wb.properties.creator = "CAPITAL"
    return wb


EXAMPLE_VEHICLES = [
    # id, reg, make, model, year, miles, source, pdate, price, bfees, listed, ask, sdate, sprice, sfees, via, status
    ("V001", "AB12 CDE", "Ford", "Fiesta 1.25 Zetec", 2012, 78400, "Auction", date(2026, 7, 3), 2150, 245, date(2026, 7, 12), 3495, date(2026, 7, 29), 3300, 0, "Facebook Marketplace", "Sold"),
    ("V002", "CD15 FGH", "Volkswagen", "Golf 1.6 TDI SE", 2015, 112000, "Private seller", date(2026, 8, 9), 3600, 0, date(2026, 8, 20), 5250, date(2026, 9, 14), 4950, 39, "AutoTrader", "Sold"),
    ("V003", "EF63 JKL", "Vauxhall", "Corsa 1.2 SXi", 2013, 91500, "Part-exchange", date(2026, 9, 2), 900, 0, date(2026, 9, 6), 1795, date(2026, 10, 1), 1500, 0, "Gumtree", "Sold"),
    ("V004", "GH17 MNO", "Toyota", "Yaris 1.33 Icon", 2017, 64000, "Auction", date(2026, 10, 15), 5400, 410, date(2026, 10, 28), 6995, None, None, None, None, "Listed"),
    ("V005", "JK11 PQR", "BMW", "320d SE", 2011, 145000, "Online marketplace", date(2026, 9, 20), 2600, 0, date(2026, 10, 3), 3750, date(2026, 11, 8), 2900, 0, "Trade / auction", "Sold"),
    ("V006", "LM19 STU", "Kia", "Picanto 1.0 2", 2019, 38000, "Trade", date(2026, 11, 10), 4850, 0, None, None, None, None, None, None, "In prep"),
]
EXAMPLE_COSTS = [
    (date(2026, 7, 5), "V001", "Parts", 86.40, "Euro Car Parts", "Front pads and discs"),
    (date(2026, 7, 6), "V001", "Labour", 60, "Local garage", "Fit brakes"),
    (date(2026, 7, 8), "V001", "Valeting", 45, "Mobile valet", "Full valet"),
    (date(2026, 7, 4), "V001", "Transport", 0, "", "Collected myself"),
    (date(2026, 8, 12), "V002", "MOT / service", 189, "Main dealer", "Major service + MOT"),
    (date(2026, 8, 14), "V002", "Advertising", 39, "AutoTrader", "Private advert"),
    (date(2026, 8, 15), "V002", "Valeting", 55, "Mobile valet", "Valet + machine polish"),
    (date(2026, 9, 3), "V003", "Parts", 34.99, "eBay", "Wiper motor"),
    (date(2026, 9, 3), "V003", "Admin / HPI check", 9.99, "HPI", "History check"),
    (date(2026, 9, 22), "V005", "Parts", 420, "GSF", "Clutch kit + DMF"),
    (date(2026, 9, 25), "V005", "Labour", 300, "Local garage", "Fit clutch"),
    (date(2026, 10, 16), "V004", "Transport", 120, "Transporter", "Auction to home"),
    (date(2026, 10, 20), "V004", "Valeting", 50, "Mobile valet", "Full valet"),
    (date(2026, 11, 12), "V006", "MOT / service", 95, "Local garage", "Service"),
]


def add_example(v, cl):
    order = ["Stock ID", "Reg", "Make", "Model", "Year", "Mileage in", "Source", "Purchase date", "Purchase price",
             "Buyer's fees", "Listed date", "Asking price", "Sale date", "Sale price", "Selling fees", "Sold via", "Status"]
    idx = {h: i + 1 for i, (h, _, _) in enumerate(VCOLS)}
    for r, rowvals in enumerate(EXAMPLE_VEHICLES, start=5):
        for h, val in zip(order, rowvals):
            if val is not None:
                v.cell(row=r, column=idx[h], value=val)
    for r, rowvals in enumerate(EXAMPLE_COSTS, start=5):
        for ci, val in enumerate(rowvals, start=1):
            if val != "":
                cl.cell(row=r, column=ci, value=val)


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    out.mkdir(parents=True, exist_ok=True)
    build(False).save(out / "Vehicle-Flip-Tracker-UK.xlsx")
    build(True).save(out / "Vehicle-Flip-Tracker-UK-EXAMPLE.xlsx")
    print("built", out)
