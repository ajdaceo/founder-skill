"""Build the UK Reseller Profit & HMRC Threshold Tracker (Excel + Google Sheets compatible).

Usage: python3 build.py [outdir]
Outputs: UK-Reseller-Tracker.xlsx (blank) and UK-Reseller-Tracker-EXAMPLE.xlsx.
"""
import sys
from datetime import date
from pathlib import Path

from openpyxl import Workbook
from openpyxl.formatting.rule import CellIsRule
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter
from openpyxl.worksheet.datavalidation import DataValidation

VERSION = "1.0.0"
ROWS = 1000
NAVY, ACCENT, LIGHT, INPUT, WHITE = "1F2A44", "2E7D5B", "EEF2F7", "FFF8E1", "FFFFFF"
thin = Side(style="thin", color="D0D7E2")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)
HFONT = Font(name="Arial", bold=True, color=WHITE, size=10)
BFONT = Font(name="Arial", size=10)
GBP = '£#,##0.00;[Red]-£#,##0.00'
PCT = '0.0%;[Red]-0.0%'
DATE = 'dd/mm/yyyy'
PLATFORMS = ["eBay", "Vinted", "Depop", "Etsy", "Amazon", "Facebook Marketplace", "In person / car boot", "Other"]
SOURCES = ["Charity shop", "Car boot", "Online", "Retail clearance", "Wholesale / bundle", "Own item (personal)", "Other"]
STATUSES = ["In stock", "Listed", "Sold", "Returned", "Donated / binned"]
CATS = ["Clothing", "Shoes", "Accessories", "Electronics", "Books / media", "Toys / games", "Home", "Collectables", "Other"]
COLS = [("Item ID", 9, "in"), ("Item", 28, "in"), ("Category", 13, "list:cat"), ("Source", 16, "list:src"),
        ("Bought date", 11, "date"), ("Cost", 9, "gbp"), ("Platform", 16, "list:pl"), ("Listed date", 11, "date"),
        ("Sale date", 11, "date"), ("Sale price", 10, "gbp"), ("Postage charged", 10, "gbp"), ("Postage cost", 10, "gbp"),
        ("Platform fees", 10, "gbp"), ("Other costs", 10, "gbp"), ("Net profit", 11, "calc"), ("Margin", 8, "calc"),
        ("Days to sell", 8, "calc"), ("Status", 13, "list:st"), ("Notes", 24, "in")]
C = {h: get_column_letter(i + 1) for i, (h, _, _) in enumerate(COLS)}


def hdr(ws, row, values, widths=None):
    for i, v in enumerate(values, start=1):
        c = ws.cell(row=row, column=i, value=v)
        c.font, c.border = HFONT, BORDER
        c.fill = PatternFill("solid", fgColor=NAVY)
        c.alignment = Alignment(horizontal="center", vertical="center", wrap_text=True)
        if widths:
            ws.column_dimensions[get_column_letter(i)].width = widths[i - 1]
    ws.row_dimensions[row].height = 30


def title(ws, text, sub):
    ws["A1"], ws["A2"] = text, sub
    ws["A1"].font = Font(name="Arial", bold=True, size=16, color=NAVY)
    ws["A2"].font = Font(name="Arial", italic=True, size=9, color="5A6475")


def build(example: bool) -> Workbook:
    wb = Workbook()
    s = wb.active
    s.title = "Start Here"
    s.sheet_view.showGridLines = False
    s.column_dimensions["A"].width, s.column_dimensions["B"].width = 3, 100
    s["B2"] = "UK Reseller Profit & HMRC Threshold Tracker"
    s["B2"].font = Font(name="Arial", bold=True, size=20, color=NAVY)
    s["B3"] = f"Version {VERSION}. Works in Microsoft Excel and Google Sheets."
    s["B3"].font = Font(name="Arial", size=10, color="5A6475")
    lines = [
        ("How it works", True),
        ("1. Sales: one row per item. Yellow cells are yours; white cells calculate. Set Status to Sold when it sells.", False),
        ("2. Dashboard: profit, margin, days to sell, stock value, best platforms and categories.", False),
        ("3. Platform Check: per platform and calendar year, how close you are to the sales count and value at which UK platforms report sellers to HMRC.", False),
        ("4. Tax Year: gross takings and profit by UK tax year (6 April to 5 April) against the trading allowance in Settings.", False),
        ("5. Settings: the thresholds used. Update them if HMRC or your platform changes them.", False),
        ("", False),
        ("Good to know", True),
        ("Being reported by a platform is not a tax bill. HMRC says reporting is not a new tax; selling your own unwanted items is not usually trading.", False),
        ("Mark personal items as Source = 'Own item (personal)' so you can see them separately.", False),
        ("Platforms decide exactly what counts toward their thresholds; the Platform Check is an estimate from your own records.", False),
        ("", False),
        ("Important", True),
        ("This is a record-keeping tool, not tax, legal or accounting advice. Check your obligations with HMRC or an accountant.", False),
        ("Selling on digital platforms (GOV.UK): https://www.gov.uk/guidance/selling-goods-or-services-on-a-digital-platform", False),
        ("Trading allowance: https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income", False),
    ]
    for r, (text, bold) in enumerate(lines, start=5):
        c = s.cell(row=r, column=2, value=text)
        c.font = Font(name="Arial", size=12 if bold else 10, bold=bold, color=NAVY if bold else "222222")
        c.alignment = Alignment(wrap_text=True, vertical="top")

    L = wb.create_sheet("Lists")
    for ci, items in enumerate([PLATFORMS, SOURCES, STATUSES, CATS], start=1):
        for ri, it in enumerate(items, start=1):
            L.cell(row=ri, column=ci, value=it)
    L.sheet_state = "hidden"

    st = wb.create_sheet("Settings")
    title(st, "Settings", "Change these if the rules or your platform's figures change.")
    st.column_dimensions["A"].width, st.column_dimensions["B"].width, st.column_dimensions["C"].width = 46, 14, 70
    settings = [
        ("Platform reporting: number of sales in a calendar year", 30, "GOV.UK: platforms report sellers with 30+ sales or about £1,700 (€2,000) a year"),
        ("Platform reporting: sales value in a calendar year (£)", 1707, "eBay's 2026 figure was £1,707; platforms convert €2,000 yearly"),
        ("Warn me at this share of a threshold", 0.8, "e.g. 0.8 = warn at 80%"),
        ("Trading allowance per tax year (£)", 1000, "Check GOV.UK for the current figure"),
    ]
    for r, (a, b, c) in enumerate(settings, start=4):
        st.cell(row=r, column=1, value=a).font = BFONT
        cell = st.cell(row=r, column=2, value=b)
        cell.fill, cell.border = PatternFill("solid", fgColor=INPUT), BORDER
        st.cell(row=r, column=3, value=c).font = Font(name="Arial", size=9, color="5A6475")
    st["B5"].number_format = '£#,##0'
    st["B6"].number_format = '0%'
    st["B7"].number_format = '£#,##0'

    v = wb.create_sheet("Sales", 1)
    title(v, "Sales and stock", "One row per item. Status 'Sold' needs a sale date and sale price.")
    hdr(v, 4, [h for h, _, _ in COLS], [w for _, w, _ in COLS])
    v.freeze_panes = "C5"
    last = 4 + ROWS
    for key, col, n in (("pl", "A", PLATFORMS), ("src", "B", SOURCES), ("st", "C", STATUSES), ("cat", "D", CATS)):
        dv = DataValidation(type="list", formula1=f"=Lists!${col}$1:${col}${len(n)}", allow_blank=True)
        v.add_data_validation(dv)
        target = {"pl": "Platform", "src": "Source", "st": "Status", "cat": "Category"}[key]
        dv.add(f"{C[target]}5:{C[target]}{last}")
    for r in range(5, last + 1):
        f = {
            "Net profit": f'=IF({C["Sale price"]}{r}="","",{C["Sale price"]}{r}+N({C["Postage charged"]}{r})-N({C["Postage cost"]}{r})-N({C["Platform fees"]}{r})-N({C["Other costs"]}{r})-N({C["Cost"]}{r}))',
            "Margin": f'=IF(OR({C["Net profit"]}{r}="",N({C["Sale price"]}{r})=0),"",{C["Net profit"]}{r}/({C["Sale price"]}{r}+N({C["Postage charged"]}{r})))',
            "Days to sell": f'=IF(OR({C["Sale date"]}{r}="",{C["Bought date"]}{r}=""),"",{C["Sale date"]}{r}-{C["Bought date"]}{r})',
        }
        for ci, (h, _, kind) in enumerate(COLS, start=1):
            c = v.cell(row=r, column=ci)
            c.border, c.font = BORDER, BFONT
            c.fill = PatternFill("solid", fgColor=LIGHT if kind == "calc" else INPUT)
            if kind == "calc":
                c.value = f[h]
            if kind == "gbp" or h == "Net profit":
                c.number_format = GBP
            if kind == "date":
                c.number_format = DATE
            if h == "Margin":
                c.number_format = PCT
    v.conditional_formatting.add(f"{C['Net profit']}5:{C['Net profit']}{last}", CellIsRule(operator="lessThan", formula=["0"], font=Font(color="C62828", bold=True)))

    S = "Sales!"
    R = {h: f"{S}${C[h]}$5:${C[h]}${last}" for h, _, _ in COLS}
    sold = f'{R["Status"]},"Sold"'

    d = wb.create_sheet("Dashboard", 0)
    d.sheet_view.showGridLines = False
    title(d, "Dashboard", "Updates automatically from the Sales sheet.")
    for col, w in zip("ABCDEFG", [32, 14, 4, 22, 10, 13, 13]):
        d.column_dimensions[col].width = w
    kpis = [
        ("Items recorded", f'=COUNTA({R["Item ID"]})', "0"),
        ("Items sold", f'=COUNTIF({R["Status"]},"Sold")', "0"),
        ("Sales incl. postage charged", f'=SUMIFS({R["Sale price"]},{sold})+SUMIFS({R["Postage charged"]},{sold})', GBP),
        ("Net profit", f'=SUMIFS({R["Net profit"]},{sold})', GBP),
        ("Average profit per item", f'=IFERROR(AVERAGEIFS({R["Net profit"]},{sold}),0)', GBP),
        ("Overall margin", f'=IFERROR(B8/B7,0)', PCT),
        ("Average days to sell", f'=IFERROR(AVERAGEIFS({R["Days to sell"]},{sold}),0)', "0"),
        ("Stock at cost (unsold)", f'=SUMIFS({R["Cost"]},{R["Status"]},"In stock")+SUMIFS({R["Cost"]},{R["Status"]},"Listed")', GBP),
        ("Items losing money", f'=COUNTIFS({R["Status"]},"Sold",{R["Net profit"]},"<0")', "0"),
    ]
    d["A4"] = "Headline numbers"
    d["A4"].font = Font(name="Arial", bold=True, size=12, color=NAVY)
    for i, (label, formula, fmt) in enumerate(kpis, start=5):
        a, b = d.cell(row=i, column=1, value=label), d.cell(row=i, column=2, value=formula)
        a.font, b.font, b.number_format = BFONT, Font(name="Arial", bold=True, size=11, color=NAVY), fmt
        for c in (a, b):
            c.border, c.fill = BORDER, PatternFill("solid", fgColor=LIGHT)
    d["D4"] = "By platform"
    d["D4"].font = Font(name="Arial", bold=True, size=12, color=NAVY)
    for i, h in enumerate(["Platform", "Sold", "Sales", "Profit"]):
        c = d.cell(row=5, column=4 + i, value=h)
        c.font, c.fill = HFONT, PatternFill("solid", fgColor=NAVY)
    for i, p in enumerate(PLATFORMS, start=6):
        crit = f'{sold},{R["Platform"]},D{i}'
        d.cell(row=i, column=4, value=p).font = BFONT
        d.cell(row=i, column=5, value=f"=COUNTIFS({crit})").number_format = "0"
        d.cell(row=i, column=6, value=f"=SUMIFS({R['Sale price']},{crit})+SUMIFS({R['Postage charged']},{crit})").number_format = GBP
        d.cell(row=i, column=7, value=f"=SUMIFS({R['Net profit']},{crit})").number_format = GBP
        for ci in range(4, 8):
            d.cell(row=i, column=ci).border = BORDER
    r0 = 16
    d.cell(row=r0, column=1, value="Profit by category").font = Font(name="Arial", bold=True, size=12, color=NAVY)
    for i, cat in enumerate(CATS, start=1):
        d.cell(row=r0 + i, column=1, value=cat).font = BFONT
        c = d.cell(row=r0 + i, column=2, value=f'=SUMIFS({R["Net profit"]},{sold},{R["Category"]},A{r0+i})')
        c.number_format, c.border = GBP, BORDER

    pc = wb.create_sheet("Platform Check", 2)
    pc.sheet_view.showGridLines = False
    title(pc, "Platform reporting check", "Estimate from your records: sales per platform per calendar year (1 Jan to 31 Dec) against the thresholds in Settings.")
    pc["A3"], pc["B3"] = "Calendar year:", date.today().year
    pc["A3"].font = Font(name="Arial", bold=True, color=NAVY)
    pc["B3"].fill, pc["B3"].border = PatternFill("solid", fgColor=INPUT), BORDER
    hdr(pc, 5, ["Platform", "Sales count", "Sales value", "Count used", "Value used", "Status"], [22, 11, 13, 11, 11, 34])
    for i, p in enumerate(PLATFORMS, start=6):
        crit = f'{sold},{R["Platform"]},A{i},{R["Sale date"]},">="&DATE($B$3,1,1),{R["Sale date"]},"<="&DATE($B$3,12,31)'
        pc.cell(row=i, column=1, value=p)
        pc.cell(row=i, column=2, value=f"=COUNTIFS({crit})").number_format = "0"
        pc.cell(row=i, column=3, value=f"=SUMIFS({R['Sale price']},{crit})+SUMIFS({R['Postage charged']},{crit})").number_format = GBP
        pc.cell(row=i, column=4, value=f"=B{i}/Settings!$B$4").number_format = "0%"
        pc.cell(row=i, column=5, value=f"=C{i}/Settings!$B$5").number_format = "0%"
        pc.cell(row=i, column=6, value=(
            f'=IF(OR(B{i}>=Settings!$B$4,C{i}>=Settings!$B$5),"Likely reported to HMRC",'
            f'IF(OR(D{i}>=Settings!$B$6,E{i}>=Settings!$B$6),"Getting close","Below thresholds"))'))
        for ci in range(1, 7):
            pc.cell(row=i, column=ci).border = BORDER
            pc.cell(row=i, column=ci).font = BFONT
    pc.conditional_formatting.add("F6:F13", CellIsRule(operator="equal", formula=['"Likely reported to HMRC"'], font=Font(color="C62828", bold=True)))
    pc.conditional_formatting.add("F6:F13", CellIsRule(operator="equal", formula=['"Getting close"'], font=Font(color="B26A00", bold=True)))

    t = wb.create_sheet("Tax Year", 3)
    t.sheet_view.showGridLines = False
    title(t, "UK tax year summary", "6 April to 5 April. Own personal items are shown separately because selling them is not usually trading.")
    hdr(t, 4, ["Tax year", "Starts", "Ends", "Items sold", "Gross takings (excl. own items)", "Net profit (excl. own items)", "Own items: takings", "Above trading allowance?"], [11, 11, 11, 10, 16, 16, 14, 18])
    base = date.today().year - 2
    for i in range(6):
        r, y = 5 + i, base + i
        t.cell(row=r, column=1, value=f"{y}/{str(y+1)[2:]}")
        t.cell(row=r, column=2, value=f"=DATE({y},4,6)").number_format = DATE
        t.cell(row=r, column=3, value=f"=DATE({y+1},4,5)").number_format = DATE
        base_crit = f'{sold},{R["Sale date"]},">="&B{r},{R["Sale date"]},"<="&C{r}'
        trade = f'{base_crit},{R["Source"]},"<>Own item (personal)"'
        own = f'{base_crit},{R["Source"]},"Own item (personal)"'
        t.cell(row=r, column=4, value=f"=COUNTIFS({base_crit})").number_format = "0"
        t.cell(row=r, column=5, value=f"=SUMIFS({R['Sale price']},{trade})+SUMIFS({R['Postage charged']},{trade})").number_format = GBP
        t.cell(row=r, column=6, value=f"=SUMIFS({R['Net profit']},{trade})").number_format = GBP
        t.cell(row=r, column=7, value=f"=SUMIFS({R['Sale price']},{own})+SUMIFS({R['Postage charged']},{own})").number_format = GBP
        t.cell(row=r, column=8, value=f'=IF(E{r}>Settings!$B$7,"Yes - check HMRC","No")')
        for ci in range(1, 9):
            t.cell(row=r, column=ci).border = BORDER
            t.cell(row=r, column=ci).font = BFONT

    if example:
        rows = [
            ("R001", "Levi's 501 jeans W32", "Clothing", "Charity shop", date(2026, 1, 10), 6, "Vinted", date(2026, 1, 11), date(2026, 1, 20), 28, 0, 0, 0, 0, "Sold"),
            ("R002", "Nintendo DS Lite", "Electronics", "Car boot", date(2026, 3, 1), 15, "eBay", date(2026, 3, 2), date(2026, 3, 9), 55, 4.5, 4.5, 7.6, 0, "Sold"),
            ("R003", "Barbour jacket", "Clothing", "Charity shop", date(2026, 5, 2), 18, "eBay", date(2026, 5, 3), date(2026, 6, 1), 85, 6, 6.2, 11.9, 0, "Sold"),
            ("R004", "Old sofa cushions", "Home", "Own item (personal)", None, 0, "Facebook Marketplace", None, date(2026, 6, 15), 20, 0, 0, 0, 0, "Sold"),
            ("R005", "Lego bundle 2kg", "Toys / games", "Online", date(2026, 7, 4), 22, "eBay", date(2026, 7, 5), date(2026, 7, 30), 19, 5, 5.8, 3.1, 0, "Sold"),
            ("R006", "Nike Air Max 90", "Shoes", "Retail clearance", date(2026, 10, 2), 35, "Depop", date(2026, 10, 3), None, None, None, None, None, None, "Listed"),
        ]
        order = ["Item ID", "Item", "Category", "Source", "Bought date", "Cost", "Platform", "Listed date", "Sale date", "Sale price", "Postage charged", "Postage cost", "Platform fees", "Other costs", "Status"]
        idx = {h: i + 1 for i, (h, _, _) in enumerate(COLS)}
        for r, vals in enumerate(rows, start=5):
            for h, val in zip(order, vals):
                if val is not None:
                    v.cell(row=r, column=idx[h], value=val)
    wb.properties.title = "UK Reseller Profit & HMRC Threshold Tracker"
    wb.properties.creator = "CAPITAL"
    return wb


if __name__ == "__main__":
    out = Path(sys.argv[1] if len(sys.argv) > 1 else "dist")
    out.mkdir(parents=True, exist_ok=True)
    build(False).save(out / "UK-Reseller-Tracker.xlsx")
    build(True).save(out / "UK-Reseller-Tracker-EXAMPLE.xlsx")
    print("built", out)
