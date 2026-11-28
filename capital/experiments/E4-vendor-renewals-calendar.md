# E4: Unpublished renewals report for suppliers in one public-sector market

Status: APPROVED by owner 2026-11-28 for controlled validation (cap £25). LONGER-LEAD experiment. Outreach first; statutory requests only after customer interest is shown and the owner approves them. Not live.

## Hypothesis
A supplier that depends on public-sector contracts in a narrow category will pay for a complete, checked calendar showing when its competitors' contracts end.

## Why a test and not more research
The data exists now, the buyers are identifiable from the same data, and a few dozen individually written emails will show whether anyone wants it. No desk research can answer that.

## Two markets (figures rebuilt from 2020 onward)
| | A. Occupational health and employee assistance | B. Learning management systems and e-learning |
|---|---|---|
| Published contracts since January 2020 | 723 | 486 |
| Still running | 275 | 154 |
| Ending within 18 months | 161, worth £189.5m | 106, worth £16.5m |
| Suppliers | 253 | 211 |
| Buyers | 454 | 310 |
| Median contract value | £150,000 | £75,019 |

Source: Contracts Finder award notices, pulled 2026-11-28 with `ops/cf_report.py` (Open Government Licence v3.0). Two markets so that one result is not mistaken for a verdict on the whole idea: A is a service market with large contracts; B is a software market with smaller ones. 28 prospects in all (12 in A, 16 in B).

## Original design (WITHDRAWN 2026-11-28; kept for the record. The live design is under "Revised test" below)

### Customer
Limited companies that have won two or more published contracts in the category since 2023, or small firms with a live contract. Active on Companies House, with a working website and a published company email address. Twenty per arm, chosen by hand from the verified list.

### Offer and price
- **Renewals calendar:** every published contract in the category since January 2023 with buyer, incumbent, value, start, end, months left, region and a link to the source notice. Spreadsheet. One refresh after six months included.
- **£295, fixed.** Full refund on request within 14 days. No negotiation.
- **Free sample in the email:** five real contracts ending in 4 to 14 months that the recipient does not hold, and a count of the recipient's own contracts on record.
- Stated limits: published notices only; some bodies publish late or never; extensions are not always announced.

### Channel
One individually written email to the company's published address. One follow-up after seven days. Nothing further. Sender identity, AI disclosure and opt-out in every message. Limited companies and LLPs only.

### Cost cap
£25: domain (about £5) and the first month of a mailbox. No advertising.

### Exposure target and deadline
Forty delivered emails within five working days of approval. Judged 21 days after the first send.

### Pass and fail lines
- **Pass:** at least one paid order. **Strong:** three or more.
- **Continue with one change:** no orders but four or more substantive replies (asking about scope, price, sample or coverage). Change one thing (price or format) and send to twenty new prospects.
- **Fail:** anything less. Record whether it failed on reach (bounces, no opens), offer, product or economics.

### What is measured
Per arm: delivered, replies, substantive replies, orders, refunds, and what repliers say they already use.

### Fulfilment
`ops/cf_report.py` rebuilds the calendar on the day of the order. Delivery by email within 24 hours of payment. The paid calendars are kept out of this public repository.

### If it passes
Edition two adds contracts that were never published, obtained by statutory request to the bodies missing from the calendar (each request asks for re-use under the Open Government Licence). More categories follow on the same pipeline; each is a separate small product.

## Competition (checked at source 2026-11-28) and what it changes
| | Stotles | BidSkim | This report |
|---|---|---|---|
| Expiring contracts from published notices | Yes, including on the free plan ("Expiring contracts and awards"); award search is free | Yes: end date, extensions, incumbent, value; 22,900+ contracts ending within 12 months; updated daily | Yes, as a courtesy sample only |
| Price | Free; Basic £99 a month billed yearly (£1,188 + VAT); Growth from £475 a month | Monitor £79 a month; Predict (renewals) £189 a month, or £155 billed yearly | £295 once per market |
| Contracts never published | Not checked: we have no evidence either way | Not checked: we have no evidence either way | The paid product |

**Finding.** A paid calendar built only from published notices is not worth £295: Stotles shows the same facts free and BidSkim adds daily monitoring. That version of E4 is withdrawn.

**What published notices miss.** Both tools describe their data as built from published notices; we have not tested what else they hold, and the emails make no claim about them. In occupational health we find a live published contract for only 69 English councils, 14 NHS bodies and 10 police forces (Contracts Finder, 2020 to 2026, title search; some contracts will sit under other titles or frameworks). The rest are in no notice.

**Re-scope.** The paid product is the unpublished contracts, obtained by one short Freedom of Information request per body, compiled with the published ones. Payment on delivery. The published-data sample in each email shows competence, not the product.

**Still unproven.** Whether suppliers value the unpublished contracts enough to pay; how many bodies answer usefully; whether the tools add this later. The test answers the first two.

## Revised test (supersedes the offer, pass lines and fulfilment above)
- **Offer:** "Unpublished renewals report" for the market, £295 on delivery, reserve by reply, refund within 14 days if not as described. Terms: `E4-assets/terms.md`.
- **Messages:** `E4-assets/outreach-drafts.md` (28 prospects; examples shown). Statutory request text: `E4-assets/foi-request-draft.md` (about 280 bodies in the first batch, 60 a day).
- **Order of work (owner instruction 2026-11-28):** the 28 vendor emails go first. They say plainly that no requests have been sent and that the report goes ahead only if enough suppliers want it. No statutory request is sent before that.
- **Go or no-go on the requests:** three or more reservations within 14 days of the first email. If met, the owner is asked to approve the statutory requests (about 280 bodies, 60 a day); delivery about eight weeks later; invoices on delivery. If not met, no requests are sent and reservers are told.
- **Pass:** go threshold met, then at least one invoice paid within 14 days of delivery. **Fail:** fewer than two reservations and fewer than four serious replies.
- **Evidence timing:** reservations and replies in December; payment evidence about eight weeks after the go decision. E4 does not occupy December: the shorter-cycle experiment E6 runs alongside it.
- **Second use of the data if vendors do not buy:** offer it to the tender-tool companies themselves (radar item).

## Results
None yet.

## Next decision
Owner: complete `infrastructure/SETUP-GUIDE.md`, and approve the messages, terms and statutory request text listed in `OWNER_ACTIONS.md`.
