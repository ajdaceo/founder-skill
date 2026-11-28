# Standing authorisations: PROPOSAL, none in force

Purpose: after the commercial cycle has been run once under your eye, let routine work proceed without asking each time. Each authorisation is narrow, has a hard limit, leaves an audit trail and can be stopped at once. Nothing here applies until you say so, one item at a time.

| # | Routine action | Limit | Audit trail | Suggested to start after |
|---|---|---|---|---|
| A1 | Send an outreach email whose template and prospect rules you have approved | 20 a day; 60 per experiment; limited companies and LLPs only; one follow-up | Every message and recipient logged in the private repository | The first approved batch has gone out with no complaint |
| A2 | Reply to prospects and customers using approved templates (sample, scope, delivery date, how to pay, opt-out) | Templates only; anything else is drafted and waits for you | Thread log | Ten replies handled under your review |
| A3 | Issue a Stripe invoice for a fixed-price product on delivery | Listed prices only; no discounts | Stripe records; ledger entry | First invoice issued under your review |
| A4 | Deliver a paid product after the release checks pass | Only products you have approved | Delivery log with file checksum | First delivery under your review |
| A5 | Refund in full on request inside the stated refund period | Up to the price paid; one per customer; needs Stripe refund permission added to the key | Stripe records; ledger entry | Five sales |
| A6 | Send a statutory request to a public body using an approved text | 60 a day; one per body per topic per year | Request log | The first approved batch |
| A7 | Renew existing subscriptions already approved (domain, mailbox) | Listed services at listed prices | Ledger entry | Now, if you wish |
| A8 | Start a validation-tier experiment | Up to £25 each, £50 a month in total, loss limited to the stake | Experiment record before any spend | One experiment has completed a full cycle |

**Always yours:** new accounts, anything involving your identity, prices and terms, spending above the limits, asset purchases, real-money trading, any reply to a complaint or legal or regulatory contact.

**Monitoring.** The dashboard shows every action taken under an authorisation since the last run. A weekly report lists counts against limits.

**Emergency stop.** Any one of these halts all outward actions at the next run and blocks them until you clear it: a file named `STOP` in `capital/`; the word STOP sent in the session; disabling the scheduled task. Revoking the mailbox app secret or the Stripe key cuts access immediately and independently of me.

**Automatic pauses.** Two bounced or complaining recipients in a batch; a payment dispute; any message that mentions a solicitor, a regulator or a complaint; spending within 10% of a limit.
