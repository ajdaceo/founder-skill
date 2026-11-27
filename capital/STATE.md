# State (updated 2026-11-27)

Revenue to date: £0. Costs to date: £0. Nothing is published or on sale.

## Product 1: QuarterReady MTD workbook
- Built: `products/mtd-workbook/dist/QuarterReady-MTD-Workbook.xlsx` (v1.0.0), from `build.py`.
- Tested: `test.py`, 1,788 checks against independent maths via LibreOffice recalculation, 4 scenarios. Passing.
- Not yet checked: appearance and dropdowns in real Excel and Google Sheets (no access here). Owner or a first buyer should open it once.
- Landing page: `site/index.html`, checker logic and mobile layout tested. Buy button inactive until `CHECKOUT_URL` is set.
- Store copy: `products/mtd-workbook/LISTING.md`.

## Backlog (priority order)
1. [blocked: owner] Open store, upload file, set `CHECKOUT_URL`. See OWNER_ACTIONS.md.
2. [blocked: owner] Host `site/`.
3. Listing images: render workbook screenshots for the store (LibreOffice to PNG).
4. One-page PDF quick-start guide to include in the download.
5. Trade-specific editions with sample data (CIS subcontractor, taxi/private hire, childminder, single-property landlord). Each is a separate marketplace listing and search term.
6. SEO pages for `site/`: "MTD spreadsheet for landlords", "MTD for income tax deadlines 2027-28", "do I need MTD if I earn £30,000".
7. Document step-by-step linking of the workbook to two free bridging tools (needs their docs; verify, do not guess).
8. Product 2 discovery: next candidates in `research/2026-11-27-market-discovery.md`.

## Known facts to re-verify before each tax year
Thresholds, deadline dates, penalty easement, mileage rates, tax rates. Sources in the research note.
