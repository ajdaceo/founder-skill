# Owner actions (updated 2026-11-27 22:10 UK)

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
