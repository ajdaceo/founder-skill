# E4: Renewals calendar for suppliers in one public-sector category

Status: PREPARED 2026-11-28. Not live. Needs the owner's approval and set-up in `OWNER_ACTIONS.md` before anything is sent.

## Hypothesis
A supplier that depends on public-sector contracts in a narrow category will pay for a complete, checked calendar showing when its competitors' contracts end.

## Why a test and not more research
The data exists now, the buyers are identifiable from the same data, and forty individually written emails will show whether anyone pays. No desk research can answer that.

## Two arms (20 prospects each)
| | A. Occupational health and employee assistance | B. Learning management systems and e-learning |
|---|---|---|
| Published contracts since January 2023 | 449 | 303 |
| Still running | 265 | 149 |
| Ending within 18 months | 151, worth £95.3m | 102, worth £16.0m |
| Suppliers | 175 | 142 |
| Buyers | 318 | 210 |
| Median contract value | £157,000 | £75,000 |

Source: Contracts Finder award notices, pulled 2026-11-28 with `ops/cf_report.py` (Open Government Licence v3.0). Two arms so that one result is not mistaken for a verdict on the whole idea: A is a service market with large contracts; B is a software market with smaller ones.

## Customer
Limited companies that have won two or more published contracts in the category since 2023, or small firms with a live contract. Active on Companies House, with a working website and a published company email address. Twenty per arm, chosen by hand from the verified list.

## Offer and price
- **Renewals calendar:** every published contract in the category since January 2023 with buyer, incumbent, value, start, end, months left, region and a link to the source notice. Spreadsheet. One refresh after six months included.
- **£295, fixed.** Full refund on request within 14 days. No negotiation.
- **Free sample in the email:** five real contracts ending in 4 to 14 months that the recipient does not hold, and a count of the recipient's own contracts on record.
- Stated limits: published notices only; some bodies publish late or never; extensions are not always announced.

## Channel
One individually written email to the company's published address. One follow-up after seven days. Nothing further. Sender identity, AI disclosure and opt-out in every message. Limited companies and LLPs only.

## Cost cap
£25: domain (about £5) and the first month of a mailbox. No advertising.

## Exposure target and deadline
Forty delivered emails within five working days of approval. Judged 21 days after the first send.

## Pass and fail lines
- **Pass:** at least one paid order. **Strong:** three or more.
- **Continue with one change:** no orders but four or more substantive replies (asking about scope, price, sample or coverage). Change one thing (price or format) and send to twenty new prospects.
- **Fail:** anything less. Record whether it failed on reach (bounces, no opens), offer, product or economics.

## What is measured
Per arm: delivered, replies, substantive replies, orders, refunds, and what repliers say they already use.

## Fulfilment
`ops/cf_report.py` rebuilds the calendar on the day of the order. Delivery by email within 24 hours of payment. The paid calendars are kept out of this public repository.

## If it passes
Edition two adds contracts that were never published, obtained by statutory request to the bodies missing from the calendar (each request asks for re-use under the Open Government Licence). More categories follow on the same pipeline; each is a separate small product.

## Results
None yet.

## Next decision
Owner: approve or amend the request in `OWNER_ACTIONS.md`.
