# E6: Checked prospect list for firms that sell Carbon Reduction Plans

Status: PREPARED 2026-11-28 as the shorter-cycle experiment the owner asked for. Not approved, not live. Uses the shared Oakmarch infrastructure. Nothing has been sent.

## Why this one
The owner asked for an opportunity where demand can be tested, a customer won, value delivered and payment received within days. This is the only candidate whose product already exists and can be delivered the day it is paid for. It carries no liability for anyone's plan, needs no client data, and exercises every stage of the commercial cycle that is still untested.

Candidates considered for the short cycle:
| Candidate | Days to first payment if it works | Why not first |
|---|---|---|
| **Checked list of NHS suppliers without a current plan, sold to plan sellers (this one)** | 3 to 10 | Chosen |
| Refer the same 213 companies to an established plan seller for a fee (one advertises £1,000 per referred client) | 30 to 90 | Paid only after the seller closes the sale; needs a partner account. Kept as the follow-on if list buyers say "we pay on results" |
| Fixed-fee pre-submission check of a live tender response | 7 to 21 | Urgency is real, but it needs a customer's confidential bid and carries advice risk; nothing built |
| E5 fixing a measured website weakness | 14 to 30 | Needs building and trust; no finished product |

## Hypothesis
Firms that sell Carbon Reduction Plan services will pay £195 for a list of NHS suppliers that verifiably lack a current plan, ahead of the 1 April 2027 rule change.

## Evidence for and against (collected 2026-11-28)
- **For.** 39 UK sellers of this service were identified in two passes; their published prices run from £199 to £4,195 a plan, so one sale from the list repays it. About two thirds of the sellers' pages name the NHS or its supplier assessment. One seller pays £1,000 for a referred client, which shows what a customer is worth to them.
- **Against.** No seller advertises buying leads or data. They rely on inbound marketing: free templates, free calls. Referral schemes in this market pay on results. Paying up front for a list may be a harder sell than a success fee. This is inference from their websites, not a test.
- **Own estimate:** a sale is less likely than not. The test costs nothing beyond the shared infrastructure and takes ten days.

## Product (exists today)
213 companies, each: a small or medium-sized company, active at Companies House, winner of English NHS work by open competition since January 2025, with a working website on which no Carbon Reduction Plan dated within the last 15 months was found (168 none found; 45 out of date). For each: company number and type, website, published company email where there is one (183), plan status and date, the evidence link, the NHS buyer, contract and award notice. Checked 28 November 2026. A second check of 12 found 1 wrong, so about 1 entry in 12 may be wrong.

Built by `ops/e6_build.py` from the checked list; it runs release checks (every row a company or LLP, no duplicate, no address that looks like a named person, evidence link present for every out-of-date plan) and wrote a 213-row spreadsheet with a "Read me" sheet on 2026-11-28 with no release problems.

## Customer
UK firms that sell Carbon Reduction Plan or carbon-footprint services to small suppliers. `E6-assets/prospects.csv`: 22 firms with a published company email address on their own site; 16 confirmed as active limited companies and ready, 6 held for a hand-check of the company's identity. Seventeen further sellers publish only a contact form and are left out: forms are not used for outreach.

## Offer and price
- The full list for **£195**, fixed, paid by card through a payment link, delivered by email within one working day.
- Sold to **no more than five firms**. Stated in the email.
- Five real rows free in the email; ten more on request.
- Full refund on request within 14 days.

## Channel
One individual email per firm to its published company address, one follow-up after five days. Sender identity, AI disclosure, opt-out. Messages: `E6-assets/outreach-draft.md`. Terms: `E6-assets/terms.md`.

## Cost cap
£0 beyond the shared infrastructure. Payment processing takes about £3 to £6 of each £195.

## Exposure target and deadline
Every ready prospect (16 to 22) within three working days of approval, at no more than five on the first day. Judged 10 days after the first send.

## Pass and fail lines
- **Pass:** at least one paid order. **Strong:** three or more, which would justify a refreshed list each month and lists built on other signals.
- **Continue with one change:** no order but three or more serious replies. Change one thing: offer the same companies on results-based terms.
- **Fail:** anything less. Record whether it failed on reach, offer, product or price.

## What a pass would prove
The whole cycle inside two weeks: outreach, reply handling, payment, delivery, support, accounting. And that checked lists are a product line the existing pipeline can refill from new award notices every month.

## Conditions before anything is sent
1. The owner approves the messages, the terms and the prospect list.
2. **The list must not be publicly available.** It sits in this repository, which is public. "Sold to no more than five firms" would mislead while anyone can download it. The owner makes the repository private (set-up guide, step 5), or the list is refreshed and held only in a private repository. E6 does not start until one of these is done.
3. Set-up steps 0 to 6 are complete and the test email and £1 test invoice have passed.
4. On the day of sending, the five example companies are re-checked and each recipient is confirmed as a limited company or LLP.

## Trade-off the owner must weigh
Up to five firms would contact the same companies E3 would have approached. E3 is suspended; a restart would need a fresh list from the wider pool of about 1,400 firms. Recommendation: sell the list. A suspended option earns nothing.

## Timing of money
A buyer can pay on day one. The payment processor holds a new account's first payout for 7 to 14 days, so the first cash reaches the bank one to two weeks after the first sale.

## Legal and data points
- Company-level data and published company addresses only. Addresses that belong to a named person are left out. Buyers are told they must follow the email-marketing rules themselves.
- Every statement about a company is what its website showed on the date of checking, with the evidence link and the stated error rate.
- Contains public sector information licensed under the Open Government Licence v3.0.
- No Freedom of Information requests, no client data, no personal data in the product.

## Results
None yet.

## Next decision
Owner: approve or amend the messages, terms and prospect list in `E6-assets/`, and choose how the list is taken out of public view.
