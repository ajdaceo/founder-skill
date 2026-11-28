# Owner actions (updated 2026-11-28 01:00 UTC)

## E3 CONSOLIDATED SETUP REQUEST (final, presented 2026-11-28). Awaiting your reply.

**Recommendation: run E3 as a lean, time-boxed test, but only if you accept that it is a small business.** Realistic ceiling a few hundred pounds a month (ASSUMPTION from market size: about 1,400 reachable NHS SME suppliers without a plan; research/2026-11-28-e3-readiness.md). The hook is real and dated: from 1 April 2027 every new above-threshold NHS tender needs a full published plan (EVIDENCE: NHS England guidance, 9 June 2026; research/e3-sources/requirements.md). If you would rather not spend more than £25, reply "E3 stop" and I return to opportunity selection; the product and 213-prospect list are kept as assets.

### 1. Money (needs your approval; the compliant setup costs more than the £25 cap)
| Item | Cost | When | Source |
|---|---|---|---|
| Domain .co.uk (Porkbun) | about £4.50 a year | now | infrastructure.md A (VERIFIED price) |
| Microsoft 365 Business Basic mailbox (Graph API) | £0 trial month, then £6.48 a month. **Choose monthly commitment or cancel inside the trial: the annual term is about £78** | now | infrastructure.md B (VERIFIED) |
| ICO data protection fee | £0 if the ICO self-check says exempt, else £47 by direct debit | before first send | regulatory.md 4.6 |
| Cloudflare (DNS, offer page), Tally (intake form), Stripe (payments) | £0 fixed; Stripe takes £2.25 to £7.17 per £249 sale | now | infrastructure.md C-F |
| **Envelope requested now** | **£60** (replaces the £25 cap) | | |
| Professional indemnity insurance | about £74 to £125 a year (published floors; needs a quote disclosing AI delivery) | **only after a first paid order, before delivery** | regulatory.md 3 |
| Possible total if a sale happens | about £185, inside the £250 maximum; needs your explicit yes | | |
Fixed rule proposed: if insurance cannot be bought within 5 working days of a paid order, that order is refunded in full. Alternative: you accept delivering uninsured with a liability cap equal to the fee (your risk as sole trader; your call).

### 2. Decisions (one word each is enough)
- **Channel:** email (recommended; ≤15 a day, one recipient per message, limited companies only, opt-out in every message). Post rejected: about £96 for 100 letters. Risk: Microsoft may suspend a new tenant it deems to be sending spam.
- **Prices (fixed, no negotiation):** £249 first plan; £149 annual update; £49 per extra re-issue; one round of corrections within 30 days included.
- **Trading name:** your choice, or one of: "Plainline Carbon Plans", "Ready CRP", "Tender Carbon Plans". Check the domain is free when you buy it.
- **Per-plan review by you:** about 10 minutes per plan, logged, until 20 clean deliveries, then a one-in-five sample. This is what insurers ask about. Yes/no.
- **Solicitor look at the terms:** optional; draft terms are in experiments/E3-assets/terms-draft.md with a cap equal to fees paid. Validate without one (my suggestion for a test this size), or pay for a review (cost not researched).

### 3. Setup actions (about 75 minutes once; all in your name)
1. **Network for this scheduled task (blocking research now).** This run's shell got "403 policy denial" for gov.uk and Companies House; the previous run had Full access. Set Network access = Full on the cloud environment this scheduled task uses.
2. Private GitHub repo (e.g. `capital-ops`) with operator access. Client data must not go in this public fork.
3. Domain at https://porkbun.com, nameservers to Cloudflare (https://dash.cloudflare.com/sign-up). Create a Cloudflare API token scoped to that zone + Pages; put it in the cloud environment as CLOUDFLARE_API_TOKEN (not in chat).
4. Microsoft 365 Business Basic trial (https://www.microsoft.com/en-gb/microsoft-365/business/microsoft-365-business-basic), verify the domain, create the mailbox, register an Entra app with Mail.Send and Mail.ReadWrite, grant admin consent. Put M365_TENANT_ID, M365_CLIENT_ID, M365_CLIENT_SECRET in the cloud environment.
5. Stripe (https://dashboard.stripe.com/register), business type sole proprietorship, verification, payout bank, enable bank transfers, restricted API key as STRIPE_RESTRICTED_KEY.
6. Tally free account (https://tally.so), API key as TALLY_API_KEY.
7. ICO self-check (https://ico.org.uk/for-organisations/data-protection-fee/data-protection-fee-self-assessment/): answer for "own marketing + own customer and accounts records; clients supply business totals only". Tell me exempt or paid.
8. Employment contract: any clause on outside business, conflicts or IP? Reply "none" or the clause text. (Still outstanding.)
9. Remove Gmail, Google Calendar and Claude Docs connectors from the "CAPITAL operator (V1.0)" scheduled task. (Still outstanding.)
10. Allow the network hosts graph.microsoft.com, login.microsoftonline.com, api.stripe.com, api.tally.so, api.cloudflare.com if Full access is not used.

### 4. Approve the wording
Outreach email: experiments/E3-assets/outreach-draft.md. Offer page: experiments/E3-assets/offer-page-draft.md. Terms and privacy notice: experiments/E3-assets/terms-draft.md, privacy-draft.md. Nothing is sent or published until you reply.

### Reply format
"E3 go: £60, email, prices ok, name X, review yes" (amend any part), or "E3 stop". Silence is not consent; other work continues meanwhile.

### Test once set up
100 delivered emails over about 10 working days. Pass: ≥1 paid order within 14 days of the first send. Fail: 0 orders and <3 substantive replies → stop and record whether reach, offer or economics failed. Programme review 2026-12-27.

---
## History (superseded by the request above)

## E3: CONDITIONALLY APPROVED by owner 2026-11-27 (validation only; max £25 setup; NO purchases yet)
Owner's conditions: no purchases until one consolidated setup request is presented; approval is for validation, not a commitment to the model; reassess independently if evidence weakens the case. Readiness work in progress (see goal.json next_actions). Original request kept below for the record.

### Original request (asked 2026-11-27)
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
