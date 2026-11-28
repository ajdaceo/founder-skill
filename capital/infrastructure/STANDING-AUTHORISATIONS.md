# Approvals and standing authorisations (proposal, 2026-11-28)

**Nothing here is in force.** No message has been sent, no request submitted, no authorisation activated. Each item starts only when you say so, by its number.

There are two kinds of permission. A **one-off approval** covers named texts to a named list, once. A **standing authorisation** lets a routine action repeat within a hard limit without asking each time.

## Part 1. One-off approvals

**Status 2026-11-28: the owner approved P1 and P2 in principle, subject to four conditions. Neither is effective until every condition below reads "met". P3 stays pending customer demand.**

| # | What it permits | Before I act on it |
|---|---|---|
| P1 | **E6**: the first email to the firms marked ready in `experiments/E6-assets/prospects.csv`; one follow-up after five days; the listed template replies; the delivery email with the list attached once the processor shows £195 paid. Nothing else. | All four conditions met |
| P2 | **E4**: the first email to the 28 firms in `experiments/E4-assets/prospects.csv`; one follow-up after seven days; a one-line acknowledgement of a "reserve" reply. No statutory requests. | All four conditions met |
| P3 | **E4 statutory requests** in the owner's name, about 280, 60 a day (`experiments/E4-assets/foi-request-draft.md`) | Not approved. Asked for only if three or more firms reserve within 14 days of P2 |

### Conditions (the operator updates this table; "met" needs the evidence named)
| Condition | P1 (E6) | P2 (E4) |
|---|---|---|
| Final infrastructure verification: set-up steps complete; a fully rendered copy of the first message received by the owner from the new mailbox; £1 test invoice paid and recorded; owner replies "go" to that copy | NOT MET | NOT MET |
| Lawful data reuse | Met on the operator's reading: `experiments/E6-assets/data-reuse-check.md`. Not a solicitor's opinion | Met on the operator's reading: Contracts Finder data under the Open Government Licence; company role addresses only |
| Provider compliance | Met on the text: Microsoft terms and Stripe's restricted-businesses list read 2026-11-28 | Met on the text: Microsoft terms read 2026-11-28 |
| Accurate commercial claims | NOT MET: list must be in a private repository; `ops/E6-RECHECK.md` must have run within seven days before the first send and the email's figures updated to its results | NOT MET until send day: each prospect's figures are hand-checked against a fresh data pull on the day of sending |

Sending starts at five messages on the first day and never exceeds twenty a day.

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
