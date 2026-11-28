# Approvals and standing authorisations (proposal, 2026-11-28)

**Nothing here is in force.** No message has been sent, no request submitted, no authorisation activated. Each item starts only when you say so, by its number.

There are two kinds of permission. A **one-off approval** covers named texts to a named list, once. A **standing authorisation** lets a routine action repeat within a hard limit without asking each time.

## Part 1. One-off approvals needed first (in this order)

| # | What you approve | Exactly what it permits | What must be true before I act on it |
|---|---|---|---|
| P1 | **E6 pack**: `experiments/E6-assets/outreach-draft.md`, `terms.md`, `prospects.csv` | The first email to the firms marked ready (16, up to 22 after hand-checks); one follow-up after five days; the listed template replies; the delivery email with the list attached once the processor shows £195 paid. Nothing else. | Set-up steps 0 to 6 done; test email and £1 test invoice passed; the list is no longer public (set-up step 5) |
| P2 | **E4 pack**: `experiments/E4-assets/outreach-drafts.md`, `terms.md`, `prospects.csv` | The first email to the 28 firms; one follow-up after seven days; a one-line acknowledgement of a "reserve" reply. No statutory requests. | Set-up steps 0 to 6 done; tests passed |
| P3 | **E4 statutory requests**: `experiments/E4-assets/foi-request-draft.md` | About 280 requests in your name, 60 a day | Asked for only if three or more firms reserve within 14 days of P2. Not before. |

To approve: reply "approve P1" or "approve P2", with any changes to the wording. Sending starts at five messages on the first day and never exceeds twenty a day.

## Part 2. Standing authorisations (proposed order of activation)

| # | Routine action | Hard limit | Audit trail | Earliest sensible start |
|---|---|---|---|---|
| A7 | Renew a subscription you have already approved (domain, mailbox) | Listed services at listed prices | Ledger entry | Now, if you wish |
| A1 | Send an outreach email whose template and prospect rules you have approved | 20 a day; 60 per experiment; companies and LLPs only; one follow-up | Every message and recipient logged in the private repository | After P1 or P2 has gone out with no complaint |
| A2 | Reply to prospects and customers from approved templates | Templates only; anything else is drafted and waits for you | Thread log | After ten replies handled under your review |
| A3 | Issue an invoice or payment link for a fixed-price product | Listed prices only; no discounts | Processor records; ledger entry | After the first one issued under your review |
| A4 | Deliver a paid product after its release checks pass | Only products you have approved | Delivery log with file checksum | After the first delivery under your review |
| A5 | Refund in full on request inside the stated refund period | The price paid; once per customer; needs refund permission added to the Stripe key | Processor records; ledger entry | After five sales |
| A6 | Send a statutory request to a public body using an approved text | 60 a day; one per body per topic per year | Request log | After P3's first batch |
| A8 | Start a validation-tier experiment | £25 each, £50 a month in total, loss limited to the stake | Experiment record written before any spend | After one experiment has completed a full cycle |

To activate one: reply "activate A1" (or whichever). To withdraw one: "withdraw A1". Each is independent.

## Always yours
New accounts; anything involving your identity; prices and terms; spending above the limits; asset purchases; real-money trading; any reply to a complaint or to a legal or regulatory contact.

## Monitoring
The dashboard lists every action taken under an approval or authorisation since the last run, with counts against limits. The Friday report repeats the totals.

## Emergency stop
Any one of these halts all outward action at the next run and blocks it until you clear it: a file named `STOP` in `capital/`; the word STOP sent in a session; disabling the scheduled task. Deleting the mailbox app's client secret or the Stripe key cuts access at once, independently of me.

## Automatic pauses
Two bounced or complaining recipients in a batch; a payment dispute; any message that mentions a solicitor, a regulator or a complaint; spending within 10% of a limit. A pause is reported on the dashboard and waits for you.
