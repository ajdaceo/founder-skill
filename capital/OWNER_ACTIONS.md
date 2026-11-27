# Owner actions (updated 2026-11-27 23:04 UTC)

## PENDING APPROVAL: E3 and the £25 setup envelope (asked 2026-11-27)
- **What:** approve experiment E3 (`experiments/E3-crp-public-suppliers.md`) and a spending cap of £25 from the £100 budget: a domain (about £10) and one month of a business mailbox the operator can send and read by API (about £1–7). Provider and exact prices to be confirmed against live pricing before anything is bought; purchases are made by you, in your name.
- **Why:** the targeting scan passed your 40% bar. Of 50 NHS framework suppliers, 37 (74%) lack a current published Carbon Reduction Plan; 22 (44%) are solvent, have a working website and lack a current plan. Evidence: `research/2026-11-27-e3-supplier-scan.md`.
- **Cost and risk:** £25 maximum. The pass is narrow: on the most cautious count it is 34%. Most suppliers who needed a plan made one themselves with the free template, so £249 may not sell. The prospect pool is thin: about 230 suppliers must be scanned to reach 100 emails.
- **Expected benefit:** a direct answer on whether these suppliers will pay. Pass is one paid order (£249) within 14 days of the first send.
- **Alternatives:** (a) scan the other 30 suppliers and a second framework first, at no cost, then decide; (b) drop E3 and return to opportunity selection.
- **Can other work continue?** Yes: collecting prospect email addresses, scanning more suppliers, year-matched emission factors and a sample plan all cost nothing.
- Also needed if approved: payment acceptance for £249 invoices (processor account in your name) and the employment-contract clauses (still outstanding).
- Reply "E3 approved" (or amend). Silence is not consent.


ON HOLD: everything Etsy-specific below (approval, shop, developer app, network hosts) pending the independent reassessment. Still useful now: private repo, employment clauses, removing personal connectors from the scheduled task.

Selected experiment: E2, Etsy digital spreadsheet tools (`experiments/E2-etsy-spreadsheets.md`). About 45–60 minutes in total, once. Sent to owner 2026-11-27 22:05.

## Approvals (reply "E2 approved" or amend)
- Budget envelope £70 within the £100: Etsy shop setup fee (≤£25, if charged), listing fees (≤£3), Etsy Ads (≤£40, ≤£3/day, from shop day 15).

## Setup
1. Etsy seller account and shop: https://www.etsy.com/uk/sell (identity and bank are the owner's). Shop name proposed by operator. Nothing published yet.
2. Etsy developer seller app: https://developer.etsy.com. Keystring and shared secret into cloud environment variables ETSY_API_KEY and ETSY_SHARED_SECRET (not chat).
3. Network: allow `openapi.etsy.com` and `api.etsy.com` in the cloud environment.
4. Private GitHub repo (e.g. `capital-ops`) with access for the operator; current repo is a public fork and must not hold customer or financial records.
5. Employment-contract clauses on outside business, conflicts or IP, or "none".
6. ICO self-check for "Etsy digital downloads; customer data only for own accounts and records" (likely exempt).
7. Remove Gmail, Google Calendar and Claude Docs connectors from the "CAPITAL operator (V1.0)" scheduled task.

## Notes
- Gross trading income over £1,000 in a tax year: register for Self Assessment (https://www.gov.uk/guidance/tax-free-allowances-on-property-and-trading-income).
- Buyer messages arrive in the Etsy app; the API cannot answer them.
