"""Builds the QuarterReady MTD workbook (.xlsx). Run: python3 build.py [outfile]
Plain formulas only (SUMIFS/IF/DATE/MIN/MAX) so it works in Excel, Google Sheets and LibreOffice."""
import sys
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.worksheet.datavalidation import DataValidation
from openpyxl.formatting.rule import FormulaRule

VERSION = "1.0.0"
ROWS = 1500                      # transaction capacity per sheet
LAST = ROWS + 1
NAVY, TEAL, PALE, INPUT = "1F3A5F", "0F766E", "EAF2F8", "FFF9DB"
H = Font(bold=True, color="FFFFFF"); HF = PatternFill("solid", fgColor=NAVY)
BOLD = Font(bold=True); TITLE = Font(bold=True, size=16, color=NAVY)
INF = PatternFill("solid", fgColor=INPUT); PF = PatternFill("solid", fgColor=PALE)
thin = Side(style="thin", color="B0B7C3"); BOX = Border(left=thin, right=thin, top=thin, bottom=thin)
GBP = '£#,##0.00;[Red]-£#,##0.00'; DATEF = "DD/MM/YYYY"

SE_INCOME = ["Turnover (sales / takings)", "Other business income"]
SE_EXP = ["Cost of goods bought for resale or goods used", "Payments to subcontractors (CIS)",
          "Wages, salaries and other staff costs", "Car, van and travel expenses",
          "Rent, rates, power and insurance costs", "Repairs and maintenance of property and equipment",
          "Phone, internet, stationery and other office costs", "Business entertainment",
          "Advertising and marketing", "Interest on bank and other loans",
          "Bank, credit card and other financial charges", "Irrecoverable debts written off",
          "Accountancy, legal and other professional fees", "Depreciation and loss/profit on sale of assets",
          "Other business expenses"]
TRAVEL = SE_EXP[3]
P_INCOME = ["Rent received", "Premiums for the grant of a lease", "Reverse premiums and inducements",
            "Other property income"]
P_EXP = ["Rent, rates, insurance and ground rents", "Property repairs and maintenance",
         "Non-residential property finance costs", "Legal, management and other professional fees",
         "Costs of services provided, including wages", "Travel costs", "Other allowable property expenses"]
RES_FIN = "Residential property finance costs (mortgage interest)"

wb = Workbook()

def header(ws, cols, widths):
    for i, (c, w) in enumerate(zip(cols, widths), 1):
        cell = ws.cell(1, i, c); cell.font = H; cell.fill = HF
        cell.alignment = Alignment(wrap_text=True, vertical="center")
        ws.column_dimensions[cell.column_letter].width = w
    ws.row_dimensions[1].height = 32; ws.freeze_panes = "A2"

def quarter_formula(r):
    return (f'=IF(A{r}="","",IF(A{r}<Deadlines!$B$5,"Before",IF(A{r}<=Deadlines!$C$5,"Q1",'
            f'IF(A{r}<=Deadlines!$C$6,"Q2",IF(A{r}<=Deadlines!$C$7,"Q3",IF(A{r}<=Deadlines!$C$8,"Q4","After"))))))')

def txn_sheet(name, cols, widths, list_ref, date_col="A", cat_col="D", money_cols=("E",), q_col="F", allow=None):
    ws = wb.create_sheet(name); header(ws, cols, widths)
    dv = DataValidation(type="list", formula1=list_ref, allow_blank=True,
                        errorTitle="Pick a category", error="Choose a category from the list.")
    ws.add_data_validation(dv); dv.add(f"{cat_col}2:{cat_col}{LAST}")
    dd = DataValidation(type="date", operator="greaterThan", formula1="36526", allow_blank=True,
                        errorTitle="Date needed", error="Enter a date like 14/05/2027.")
    ws.add_data_validation(dd); dd.add(f"{date_col}2:{date_col}{LAST}")
    for r in range(2, LAST + 1):
        ws[f"{date_col}{r}"].number_format = DATEF
        for m in money_cols: ws[f"{m}{r}"].number_format = GBP
        if allow:
            amt, priv, out = allow
            ws[f"{out}{r}"] = f'=IF({amt}{r}="","",{amt}{r}-N({priv}{r}))'
            ws[f"{out}{r}"].number_format = GBP; ws[f"{out}{r}"].fill = PF
        ws[f"{q_col}{r}"] = quarter_formula(r); ws[f"{q_col}{r}"].fill = PF
    # flag rows with an amount but no date/category, or a date outside the tax year
    amt = money_cols[0]
    ws.conditional_formatting.add(f"A2:{q_col}{LAST}", FormulaRule(
        formula=[f'AND(${amt}2<>"",OR(${date_col}2="",${cat_col}2=""))'], fill=PatternFill("solid", bgColor="FAD4D4")))
    ws.conditional_formatting.add(f"A2:{q_col}{LAST}", FormulaRule(
        formula=[f'OR(${q_col}2="Before",${q_col}2="After")'], fill=PatternFill("solid", bgColor="FCE8B2")))
    ws.auto_filter.ref = f"A1:{q_col}{LAST}"
    return ws

# ---------- Start ----------
ws = wb.active; ws.title = "Start"
ws.column_dimensions["A"].width = 3; ws.column_dimensions["B"].width = 110
ws["B2"] = "QuarterReady — Making Tax Digital record-keeping workbook"; ws["B2"].font = TITLE
ws["B3"] = f"Version {VERSION} · For UK sole traders and landlords · Works in Excel, Google Sheets and LibreOffice"
lines = [
 ("How to use it", True),
 ("1. Open the Settings tab. Enter the year your tax year starts (2027 for 6 April 2027 to 5 April 2028) and choose standard or calendar update periods.", False),
 ("2. Record every sale on SE_Income and every business cost on SE_Expenses: one row each, with date, amount and category. Landlords use Prop_Income and Prop_Expenses.", False),
 ("3. Yellow cells are for you to type in. Blue cells are calculated: leave them alone.", False),
 ("4. A row turns red if it has an amount but no date or category, and amber if its date is outside the tax year in Settings.", False),
 ("5. SE_Summary and Prop_Summary add everything up into HMRC's categories. Figures are cumulative from the start of the tax year, which is what each quarterly update must contain.", False),
 ("6. Deadlines shows your four update periods and due dates. Tick each one off when it has been sent.", False),
 ("7. Tax_Estimate gives a rough figure to set aside. It is an estimate, not a tax calculation.", False),
 ("", False),
 ("Sending your update to HMRC", True),
 ("A spreadsheet on its own does not meet the Making Tax Digital rules. You also need HMRC-compatible 'bridging' software that reads the totals from this workbook and sends them. Several are free; GOV.UK keeps the current list ('Find software that's compatible with Making Tax Digital for Income Tax').", False),
 ("Point the bridging software at the SE_Summary or Prop_Summary tab. The cells never move: category names are in column A and the cumulative totals for Q1 to Q4 are in columns B to E.", False),
 ("Do not retype or copy-and-paste totals into the bridging software if it can import or link to the file. HMRC expects a digital link between your records and what is submitted.", False),
 ("", False),
 ("Good to know", True),
 ("Private or disallowable part of a cost (for example the personal share of a phone bill) goes in the 'Private / disallowable' column. Only the allowable part reaches the summary.", False),
 ("Mileage: if you claim the flat rate per mile instead of actual vehicle costs, log journeys on the Mileage tab and set 'Use mileage log' to Yes in Settings. Do not also enter fuel, insurance or repairs for that vehicle.", False),
 ("Residential mortgage interest is shown on its own line in Prop_Summary because it is given as a basic-rate tax reduction and is not deducted from rental profit.", False),
 ("Jointly owned property: enter only your share of the income and costs.", False),
 ("Keep your receipts and invoices. This workbook is your digital record of the transactions; it does not replace the underlying paperwork.", False),
 ("", False),
 ("Important", True),
 ("QuarterReady is a record-keeping template. It is not tax advice, it is not HMRC-recognised software, and it does not submit anything to HMRC. It is not affiliated with or endorsed by HMRC. Tax rules and rates change: check GOV.UK or ask an accountant if you are unsure.", False),
]
for i, (t, b) in enumerate(lines, 5):
    c = ws.cell(i, 2, t); c.alignment = Alignment(wrap_text=True, vertical="top")
    if b: c.font = Font(bold=True, size=12, color=TEAL)

# ---------- Settings ----------
ws = wb.create_sheet("Settings"); ws.column_dimensions["A"].width = 44; ws.column_dimensions["B"].width = 26; ws.column_dimensions["C"].width = 70
ws["A1"] = "Settings"; ws["A1"].font = TITLE
rows = [("Business or landlord name", "", "Optional. Shown on the summaries."),
        ("Tax year starts in (year)", 2027, "2027 means the tax year 6 April 2027 to 5 April 2028."),
        ("Update periods", "Standard", "Standard = 6 April to 5 April. Calendar = 1 April to 31 March (you must also choose this in your software before your first update)."),
        ("Use mileage log", "No", "Yes adds flat-rate mileage from the Mileage tab to 'Car, van and travel expenses'."),
        ("Mileage rate: first band (£ per mile)", 0.45, "Cars and vans. Check the current rate on GOV.UK."),
        ("Mileage rate: after first band (£ per mile)", 0.25, ""),
        ("First band size (miles per tax year)", 10000, "")]
for i, (a, b, c) in enumerate(rows, 3):
    ws.cell(i, 1, a).font = BOLD; x = ws.cell(i, 2, b); x.fill = INF; x.border = BOX
    ws.cell(i, 3, c).alignment = Alignment(wrap_text=True)
for r in (7, 8): ws[f"B{r}"].number_format = '£0.00'
for lst, cell in (('"2026,2027,2028,2029,2030"', "B4"), ('"Standard,Calendar"', "B5"), ('"Yes,No"', "B6")):
    dv = DataValidation(type="list", formula1=lst, allow_blank=False); ws.add_data_validation(dv); dv.add(cell)

# ---------- Deadlines ----------
ws = wb.create_sheet("Deadlines")
for col, w in zip("ABCDEFG", (22, 16, 16, 30, 16, 12, 16)): ws.column_dimensions[col].width = w
ws["A1"] = "Quarterly update periods and deadlines"; ws["A1"].font = TITLE
ws["A2"] = '=IF(Settings!B3="","",Settings!B3)'
for i, h in enumerate(["Update", "Period starts", "Period ends", "Update covers (cumulative)", "Send by", "Sent?", "Date sent"], 1):
    c = ws.cell(4, i, h); c.font = H; c.fill = HF
Y = "Settings!$B$4"; STD = 'Settings!$B$5="Standard"'
ends_std = [f"DATE({Y},7,5)", f"DATE({Y},10,5)", f"DATE({Y}+1,1,5)", f"DATE({Y}+1,4,5)"]
ends_cal = [f"DATE({Y},6,30)", f"DATE({Y},9,30)", f"DATE({Y},12,31)", f"DATE({Y}+1,3,31)"]
dues = [f"DATE({Y},8,7)", f"DATE({Y},11,7)", f"DATE({Y}+1,2,7)", f"DATE({Y}+1,5,7)"]
for q in range(4):
    r = 5 + q
    ws[f"A{r}"] = f"Q{q+1}"; ws[f"A{r}"].font = BOLD
    ws[f"B{r}"] = f"=IF({STD},DATE({Y},4,6),DATE({Y},4,1))" if q == 0 else f"=C{r-1}+1"
    ws[f"C{r}"] = f"=IF({STD},{ends_std[q]},{ends_cal[q]})"
    ws[f"D{r}"] = f'=TEXT($B$5,"dd mmm yyyy")&" to "&TEXT(C{r},"dd mmm yyyy")'
    ws[f"E{r}"] = f"={dues[q]}"
    for col in "BCE": ws[f"{col}{r}"].number_format = DATEF; ws[f"{col}{r}"].fill = PF
    ws[f"D{r}"].fill = PF
    for col in "FG": ws[f"{col}{r}"].fill = INF; ws[f"{col}{r}"].border = BOX
    ws[f"G{r}"].number_format = DATEF
dv = DataValidation(type="list", formula1='"Yes,No"', allow_blank=True); ws.add_data_validation(dv); dv.add("F5:F8")
ws["A10"] = "Tax return / final declaration and payment due"; ws["A10"].font = BOLD
ws["E10"] = f"=DATE({Y}+2,1,31)"; ws["E10"].number_format = DATEF; ws["E10"].fill = PF
ws["A12"] = "Each update is cumulative: it covers everything from the start of the tax year to the end of that period, so corrections to earlier quarters are picked up automatically in the next update."
ws["A13"] = "Deadlines are the same for standard and calendar periods. Confirm your own obligations in your HMRC online account or software."

# ---------- Lists ----------
ls = wb.create_sheet("Lists")
for col, items in zip("ABCD", (SE_INCOME, SE_EXP, P_INCOME, P_EXP + [RES_FIN])):
    for i, v in enumerate(items, 1): ls[f"{col}{i}"] = v
    ls.column_dimensions[col].width = 55
def lref(col, n): return f"Lists!${col}$1:${col}${n}"

# ---------- Transactions ----------
txn_sheet("SE_Income", ["Date", "Description", "Customer / invoice ref", "Category", "Amount £", "Quarter"],
          (13, 38, 24, 34, 14, 10), lref("A", len(SE_INCOME)))
txn_sheet("SE_Expenses", ["Date", "Supplier", "Description", "Category", "Amount £", "Private / disallowable £", "Allowable £", "Quarter"],
          (13, 26, 34, 48, 14, 14, 14, 10), lref("B", len(SE_EXP)), money_cols=("E", "F"), q_col="H", allow=("E", "F", "G"))
ws = wb.create_sheet("Mileage"); header(ws, ["Date", "Journey and business purpose", "Business miles", "Quarter"], (13, 60, 14, 10))
for r in range(2, LAST + 1):
    ws[f"A{r}"].number_format = DATEF; ws[f"D{r}"] = quarter_formula(r); ws[f"D{r}"].fill = PF
txn_sheet("Prop_Income", ["Date", "Property", "Description", "Category", "Amount £", "Quarter"],
          (13, 26, 34, 36, 14, 10), lref("C", len(P_INCOME)))
txn_sheet("Prop_Expenses", ["Date", "Property", "Description", "Category", "Amount £", "Private / disallowable £", "Allowable £", "Quarter"],
          (13, 26, 34, 52, 14, 14, 14, 10), lref("D", len(P_EXP) + 1), money_cols=("E", "F"), q_col="H", allow=("E", "F", "G"))

# ---------- Summaries ----------
def cum(sheet, amt_col, label_cell, q):
    rng = lambda c: f"{sheet}!${c}$2:${c}${LAST}"
    return (f'SUMIFS({rng(amt_col)},{rng("D")},{label_cell},{rng("A")},">="&Deadlines!$B$5,'
            f'{rng("A")},"<="&Deadlines!$C${5+q})')

def summary(name, title, inc_sheet, exp_sheet, incomes, expenses, extra=None, mileage=False):
    ws = wb.create_sheet(name)
    ws.column_dimensions["A"].width = 56
    for col in "BCDEFGHI": ws.column_dimensions[col].width = 16
    ws["A1"] = title; ws["A1"].font = TITLE
    ws["A2"] = '=IF(Settings!B3="","",Settings!B3)&"  Tax year starting "&TEXT(Deadlines!B5,"d mmm yyyy")'
    heads = ["HMRC category"] + [f"Q{i} cumulative" for i in (1, 2, 3)] + ["Q4 cumulative (full year)"] + [f"Q{i} only" for i in (1, 2, 3, 4)]
    for i, h in enumerate(heads, 1):
        c = ws.cell(4, i, h); c.font = H; c.fill = HF; c.alignment = Alignment(wrap_text=True)
    ws.row_dimensions[4].height = 32
    ws["B3"] = "Send these to HMRC (year to date)"; ws["F3"] = "For your information (single quarter)"
    ws["B3"].font = ws["F3"].font = Font(italic=True, color=TEAL)
    r = 5; pos = {}
    def line(label, fn, bold=False):
        nonlocal r
        ws[f"A{r}"] = label
        for q, col in enumerate("BCDE"):
            ws[f"{col}{r}"] = "=" + fn(q, col)
        for q, (col, cc, prev) in enumerate(zip("FGHI", "BCDE", " BCD")):
            ws[f"{col}{r}"] = f"={cc}{r}" if q == 0 else f"={cc}{r}-{prev}{r}"
        for col in "BCDEFGHI":
            ws[f"{col}{r}"].number_format = GBP; ws[f"{col}{r}"].fill = PF; ws[f"{col}{r}"].border = BOX
            if bold: ws[f"{col}{r}"].font = BOLD
        if bold: ws[f"A{r}"].font = BOLD
        pos[label] = r; r += 1
    def section(t):
        nonlocal r
        ws[f"A{r}"] = t; ws[f"A{r}"].font = Font(bold=True, color=TEAL); r += 1
    section("Income")
    i0 = r
    for lab in incomes: line(lab, lambda q, col: cum(inc_sheet, "E", f"$A{r}", q))
    line("Total income", lambda q, col: f"SUM({col}{i0}:{col}{r-1})", True)
    r += 1; section("Allowable expenses")
    e0 = r
    for lab in expenses:
        if mileage and lab == TRAVEL:
            def fn(q, col):
                m = f'SUMIFS(Mileage!$C$2:$C${LAST},Mileage!$A$2:$A${LAST},">="&Deadlines!$B$5,Mileage!$A$2:$A${LAST},"<="&Deadlines!$C${5+q})'
                return (cum(exp_sheet, "G", f"$A{r}", q) +
                        f'+IF(Settings!$B$6="Yes",MIN({m},Settings!$B$9)*Settings!$B$7+MAX({m}-Settings!$B$9,0)*Settings!$B$8,0)')
            line(lab, fn)
        else:
            line(lab, lambda q, col: cum(exp_sheet, "G", f"$A{r}", q))
    line("Total allowable expenses", lambda q, col: f"SUM({col}{e0}:{col}{r-1})", True)
    te = pos["Total allowable expenses"]; ti = pos["Total income"]
    line("Consolidated expenses (one total, allowed if turnover is under £90,000)", lambda q, col: f"{col}{te}")
    r += 1
    line("Net profit (or loss)", lambda q, col: f"{col}{ti}-{col}{te}", True)
    r += 1; section("Memo")
    if extra:
        line(extra, lambda q, col: cum(exp_sheet, "G", f"$A{r}", q))
    line("Private / disallowable amounts excluded above",
         lambda q, col: f'SUMIFS({exp_sheet}!$F$2:$F${LAST},{exp_sheet}!$A$2:$A${LAST},">="&Deadlines!$B$5,{exp_sheet}!$A$2:$A${LAST},"<="&Deadlines!$C${5+q})')
    line("Rows missing a date or category (fix these first)",
         lambda q, col: (f'SUMPRODUCT(({inc_sheet}!$E$2:$E${LAST}<>"")*((({inc_sheet}!$A$2:$A${LAST}="")+({inc_sheet}!$D$2:$D${LAST}=""))>0))'
                         f'+SUMPRODUCT(({exp_sheet}!$E$2:$E${LAST}<>"")*((({exp_sheet}!$A$2:$A${LAST}="")+({exp_sheet}!$D$2:$D${LAST}=""))>0))'))
    mr = pos["Rows missing a date or category (fix these first)"]
    for col in "BCDEFGHI": ws[f"{col}{mr}"].number_format = "0"
    for col in "FGHI": ws[f"{col}{mr}"] = None
    ws.freeze_panes = "B5"
    return pos

se = summary("SE_Summary", "Self-employment summary", "SE_Income", "SE_Expenses", SE_INCOME, SE_EXP, mileage=True)
pr = summary("Prop_Summary", "UK property summary", "Prop_Income", "Prop_Expenses", P_INCOME, P_EXP, extra=RES_FIN)

# ---------- Tax estimate ----------
ws = wb.create_sheet("Tax_Estimate"); ws.column_dimensions["A"].width = 58; ws.column_dimensions["B"].width = 18; ws.column_dimensions["C"].width = 70
ws["A1"] = "Rough tax to set aside"; ws["A1"].font = TITLE
ws["A2"] = "An estimate from the figures entered so far. Rates below are editable defaults for England, Wales and Northern Ireland: check them against GOV.UK for your tax year."
inp = [("Other taxable income this tax year (salary, pension etc.)", 0, GBP, "Leave at 0 if you have none."),
       ("Personal allowance", 12570, GBP, "Reduces above £100,000 of income: lower it yourself if that applies."),
       ("Basic rate band (taxable income)", 37700, GBP, ""),
       ("Additional rate starts at (taxable income)", 125140, GBP, ""),
       ("Basic rate", 0.20, "0%", "Scottish taxpayers and property income may use different rates: edit to suit."),
       ("Higher rate", 0.40, "0%", ""), ("Additional rate", 0.45, "0%", ""),
       ("Class 4 NI lower profits limit", 12570, GBP, ""), ("Class 4 NI upper profits limit", 50270, GBP, ""),
       ("Class 4 NI main rate", 0.06, "0%", ""), ("Class 4 NI rate above upper limit", 0.02, "0%", ""),
       ("Extra rate on property income (percentage points)", "=IF(Settings!B4>=2027,0.02,0)", "0%",
        "Property income is taxed at 22/42/47% from 6 April 2027, 2 points above the main rates.")]
for i, (a, b, f, c) in enumerate(inp, 4):
    ws.cell(i, 1, a); x = ws.cell(i, 2, b); x.fill = INF; x.border = BOX; x.number_format = f; ws.cell(i, 3, c)
sp, pp = se["Net profit (or loss)"], pr["Net profit (or loss)"]
def tax(t): return f"(MIN({t},$B$6)*$B$8+MAX(0,MIN({t},$B$7)-$B$6)*$B$9+MAX(0,{t}-$B$7)*$B$10)"
out = [("Self-employment profit so far", f"=SE_Summary!E{sp}"),
       ("Property profit so far", f"=Prop_Summary!E{pp}"),
       ("Taxable income including other income", "=MAX(0,MAX(0,B17)+MAX(0,B18)+B4-B5)"),
       ("Income tax on everything", "=" + tax("B19")),
       ("Income tax on other income alone", "=" + tax("MAX(0,B4-B5)")),
       ("Income tax due to self-employment and property", "=B20-B21"),
       ("Extra tax from property rates", "=B15*MAX(0,MIN(MAX(0,B18),B19))"),
       ("Class 4 National Insurance", "=MAX(0,MIN(B17,B12)-B11)*B13+MAX(0,B17-B12)*B14"),
       ("Estimated amount to set aside so far", "=B22+B23+B24"),
       ("As a share of profit", '=IF(MAX(0,B17)+MAX(0,B18)=0,0,B25/(MAX(0,B17)+MAX(0,B18)))')]
ws["A16"] = "Estimate"; ws["A16"].font = Font(bold=True, color=TEAL)
for i, (a, f) in enumerate(out, 17):
    ws.cell(i, 1, a); x = ws.cell(i, 2, f); x.fill = PF; x.border = BOX; x.number_format = GBP
ws["B26"].number_format = "0.0%"; ws["A25"].font = ws["B25"].font = BOLD
ws["A28"] = "Not included: the mortgage-interest tax reduction, payments on account, student loan, Class 2 NI, allowances, reliefs and losses. This is not a tax calculation."

order = ["Start", "Settings", "Deadlines", "SE_Income", "SE_Expenses", "Mileage", "SE_Summary",
         "Prop_Income", "Prop_Expenses", "Prop_Summary", "Tax_Estimate", "Lists"]
wb._sheets = [wb[n] for n in order]
for n, colr in (("SE_Income", TEAL), ("SE_Expenses", TEAL), ("Mileage", TEAL), ("SE_Summary", TEAL),
                ("Prop_Income", "B45309"), ("Prop_Expenses", "B45309"), ("Prop_Summary", "B45309")):
    wb[n].sheet_properties.tabColor = colr
wb["Lists"].sheet_state = "hidden"
out = sys.argv[1] if len(sys.argv) > 1 else "dist/QuarterReady-MTD-Workbook.xlsx"
wb.save(out); print("built", out)
