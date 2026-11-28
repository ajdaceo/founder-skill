# CAPITAL dashboard

Updated 2026-11-28 02:19 UTC by the operator. This is the one place to see CAPITAL's position; it is revised at the end of every run.
Key: **[V]** verified result · **[E]** estimate · **[A]** assumption · **[U]** built but untested.

## Money [V]
| Revenue | Expenditure | Net profit | Cash held | Paying customers |
|---|---|---|---|---|
| £0 | £0 | £0 | £0 | 0 |

Capital available: £25 approved for E4 set-up, within the £100 starting budget (up to £250 only on an evidenced request). Monthly commitments: none yet; £7.78 a month from month two if the mailbox is kept [V price].

## The commercial cycle: what works today
| Stage | Status | Basis |
|---|---|---|
| Opportunity discovery | Operational [V] | 13 mechanisms screened; weekly radar running |
| Finding and qualifying prospects | Operational [V] | 213 for E3 and 28 for E4, each checked against Companies House and the firm's own site |
| Customer acquisition (outreach) | Untested [U] | No message has ever been sent. Needs the mailbox and your approval of the text |
| Sales conversation and replies | Untested [U] | Reply templates not yet written |
| Payment | Not set up [U] | Needs your Stripe account |
| Fulfilment | Part built | Carbon-plan generator tested on test data [V], never on a customer [U]. Report builder works on published data [V]; collecting replies from public bodies is untested [U] |
| Customer support | Untested [U] | Rules drafted only |
| Accounting | Minimal [V] | `ledger.csv` exists and is empty; reconciliation with the processor untested [U] |
| Profit measurement | Operational [V] | This dashboard; nothing to measure yet |
| Reinvestment | Policy only [U] | Allocation policy written, never exercised |

**Needs a person, by law or by design:** accounts and identity checks, approving access and secrets, the named requester on statutory requests, refunds, tax, and approval of outward messages until a standing authorisation exists.

## Opportunities
| | Item | State | Next step |
|---|---|---|---|
| Primary | **E4** unpublished renewals report for suppliers (£295, 28 prospects) | Approved for controlled validation; re-scoped after competitor check; waiting on set-up and approval of messages | Owner: set-up guide and approvals |
| Fallback | **E3** carbon plans for NHS suppliers | Suspended, launch-ready | None unless reactivated |
| Candidate | **E5** fixing a measured weakness for hand-picked firms | Sketch only | Choose one weakness from the 564 sites already checked |
| Candidate | Selling unpublished-contract data to the tender-tool companies | Idea, depends on E4 data | Hold |
| Simulated | S1 trend rule on five funds; S2 crypto trend rule; S3 asset watch | Running on paper | Weekly and monthly updates |

Rejected, with the deciding reason: open bounties (payers closing programmes; measured trial earned $0) · contingency recovery (needs account access and trust; platforms automate it) · freelance marketplaces (not autonomous) · marketplace listings (new listings get a median of one user [V]) · inbound lead capture (no traffic for new sites) · deal origination (needs a track record; about 20 months to a deal) · buying assets at £200 to £5,000 (earn too little; unverifiable) · goods arbitrage (no evidence of net return; hands-on) · published-data renewals calendar (free at Stotles [V]).

## Assets built [V]
- Prospecting pipeline: award notices to company to verified website to detected signal (`ops/`). Measured on 35 hand-checked sites.
- Carbon Reduction Plan generator with 428 official factors, 63 tests, independent recalculation matched on 48 of 48 lines.
- Contract data: 723 occupational health and 486 learning-system contracts since 2020; 7,160 technology award rows.
- E3 prospect list (213) and restart pack. E4 prospect list (28) with individual samples.
- Trading backtests and paper ledger. Research library of 13 mechanism files.

## Decisions (newest first)
| Date | Decision | Reason |
|---|---|---|
| 2026-11-28 | E4's paid product changed to unpublished contracts | Published expiry data is free at Stotles and £155 to £189 a month at BidSkim |
| 2026-11-28 | Mailbox on Microsoft 365, not Google | Google's terms bar unsolicited commercial email outright; Microsoft's bar bulk spam |
| 2026-11-28 | Dedicated environment `capital-ops` created with a twelve-host allowlist; owner approved [V] | Default environment was unrestricted and shared with your other work |
| 2026-11-28 | Owner approved E4 for controlled validation, £25 cap | Cheap test beats more research |
| 2026-11-28 | Owner suspended E3 | Small market, hard acquisition, liability and operating burden |
| 2026-11-28 | Trading kept on paper | Backtest: 5.0% a year with a 12% worst fall; no capital created at this scale |

## Pipeline [V]
| Experiment | Prospects | Contacted | Replies | Reservations | Paid | Conversion |
|---|---|---|---|---|---|---|
| E4 | 28 | 0 | 0 | 0 | 0 | n/a |
| E3 | 213 | 0 | 0 | 0 | 0 | n/a |

## Simulations (paper only) [V]
| Book | Started | Start value | Latest | As of |
|---|---|---|---|---|
| S1 five funds, trend rule | 2026-11-28 | 1,000 | 999.0 | 2026-11-28 |
| S2 Bitcoin and Ether, trend rule | 2026-11-28 | 1,000 | 997.4 | 2026-11-28 |
| S3 asset watch | 2026-11-28 | 8 listings tracked | next check 2026-12-28 | |

## Radar: newest items
1. Tender tools share one gap: contracts that were never published (score 9). In E4.
2. The same data could be sold to the tender-tool companies (score 7). Held.
3. Cyber Essentials discount scheme may lift demand for 350+ certification bodies (score 8). Terms not yet read.
Full log: `radar/RADAR.md`. Next weekly pass: on or after 2026-11-30.

## Capabilities and blockers
- **Can do now:** research, data collection from allowed public sources, prospect checks, document and report generation, paper trading, record keeping.
- **Cannot do yet:** send or read email, take payment, publish a website. All wait on the set-up guide.
- **Environment:** `capital-ops` exists and is in use in this session [V]. The scheduled task still has to be pointed at it (set-up guide, step 6.3).

## Owner actions
`OWNER_ACTIONS.md`: (1) set-up guide, about 60 to 75 minutes once; (2) approve the outreach text, terms and statutory request text; (3) enter two secrets in the secure forms when asked (the environment card is already approved).

## Next actions and milestones
1. Owner completes set-up; operator tests mail and payment end to end on a message and a £1 test invoice to the owner. **Milestone: first verified pass through send, receive, invoice, pay, record.**
2. Send 28 approved emails and the first statutory requests. **Milestone: first genuine customer interaction.**
3. Compile and deliver the report in January; invoice reservers. **Milestone M4: first independent customer payment.**
4. Weekly: radar pass, paper books, this dashboard, Friday report.
Programme review: 27 December 2026.
