# E3 readiness note (2026-11-28, checkpoint written at the usage limit; not yet the final pack)

## Reassessment in one paragraph
E3 is still worth a small, time-boxed test, but the opportunity is weaker and smaller than when proposed. The realistic ceiling looks like a few hundred pounds a month, with £1,000 a month at the optimistic end and £10,000 a month not credible for this model. The compliant setup costs more than £25.

## What is verified
- **Rules.** Today a full plan is required only for NHS frameworks and for contracts of £5m a year or more. From 1 April 2027 every new above-threshold NHS tender needs a full plan, pass or fail (NHS England guidance of 9 June 2026, checked at source). Outside the NHS, small suppliers are rarely obliged. Plans are self-certified; free templates, training and an NHS checking service exist. Sources: `research/e3-sources/requirements.md`.
- **Prospects.** 213 qualified, in `research/e3-prospects-qualified.csv`: SME, active company on Companies House, won English NHS work by open competition since January 2025, working website with no plan published in the last 15 months, published email on its own domain. 166 are on frameworks (tier A), 47 hold competitively won contracts (tier B). Of 475 working sites checked, 61% had no current plan.
- **Accuracy.** A random 12 of the "no plan" prospects were rechecked by web search: 10 confirmed, 1 had an unlinked 2023 plan (still a prospect), 1 was the wrong website and has been removed. Expect roughly 1 in 12 errors; hand-check before any send.
- **Market.** 23 months of Find a Tender awards: 6,059 distinct SME suppliers to English NHS bodies, 2,346 through competitive procedures (1,544 on frameworks). That winners' pool, times 61%, is about 1,400 firms. £1,000 a month needs about 50 sales a year, 3 to 4% of that pool every year.
- **Product.** Year-matched factors 2018 to 2026 (428 factors). An independent recalculation from the raw files matched all 48 line items. Method fixes from the official standard applied. 63 tests pass. See `products/crp/VALIDATION.md`, `METHOD.md`, `OPERATIONS.md`.

## What weakens the case
1. Free do-it-yourself route, and the plan passes on structure, not on the accuracy of figures.
2. Every mailbox provider restricts unsolicited email; Microsoft 365 is the least restrictive. Lawful to limited companies under PECR, but account suspension is a real risk. Posted letters by API cost about £0.80 each plus VAT.
3. ICO fee £52 (£47 by direct debit) unless the marketing-and-records exemption holds. That alone exceeds the £25 cap.
4. Sole trader means unlimited personal liability. Insurance is not legally required; published prices start at about £74 to £123 a year. A solicitor should check the liability cap.
5. Framework suppliers (most of the list) need a wider plan for tenders starting after 1 April 2027, which is not built.
6. Contract end dates are not in the award data, so re-tender timing per prospect is unknown.

## DRAFT consolidated setup request (not final; do not act yet)
| Item | Cost | Owner action |
|---|---|---|
| Domain (.co.uk) | about £4.50 a year | Register in your name |
| Mailbox with API (Microsoft 365 Business Basic) | £0 first month, then £6.48 a month; avoid the annual term | Sign up, verify domain, create app credentials |
| Hosting and DNS (Cloudflare) | £0 | Free account, scoped token |
| Payments (Stripe, sole trader) | no fixed fee; £2.25 to £7.17 per £249 sale | Identity and bank details |
| Intake form (Tally) | £0 | Free account, API key |
| ICO | £0 if exempt, else £47 to £52 | Take the ICO self-assessment |
| Private repository for client data | £0 | Create and grant access |
| Insurance (before first paid delivery) | about £74 to £123 a year | Get a quote, disclosing AI delivery |
| Employment-contract check | £0 | Confirm no restriction on outside business |
Decisions needed: email or post as the channel; budget above £25 (about £57 with ICO, more with insurance); prices for renewals and revisions; trading name.
Infrastructure and legal sources: `research/e3-sources/infrastructure.md`, `research/e3-sources/regulatory.md`.

## Not done
Final setup request in OWNER_ACTIONS.md, offer page, terms and privacy notice, hand-check of all 213, wider-plan product.
