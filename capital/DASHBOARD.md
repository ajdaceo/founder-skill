# CAPITAL dashboard

Updated 2026-11-28 18:40 UTC by the operator (no change since 02:50 UTC; blocked on owner step A). This is the one place to see CAPITAL's position; it is revised at the end of every run.
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
| Finding and qualifying prospects | Operational [V] | 213 for E3, 28 for E4 and 22 for E6, each checked against Companies House and the firm's own site |
| Customer acquisition (outreach) | Untested [U] | No message has ever been sent. Needs the mailbox and your approval of the text |
| Sales conversation and replies | Untested [U] | Reply templates written for E6; none used |
| Payment | Not set up [U] | Needs your Stripe account |
| Fulfilment | Part built | E6 list file builds with release checks passing [V], never delivered [U]. Carbon-plan generator tested on test data [V]. Report builder works on published data [V]; collecting replies from public bodies is untested [U] |
| Customer support | Untested [U] | Rules drafted only |
| Accounting | Minimal [V] | `ledger.csv` exists and is empty; reconciliation with the processor untested [U] |
| Profit measurement | Operational [V] | This dashboard; nothing to measure yet |
| Reinvestment | Policy only [U] | Allocation policy written, never exercised |

**Needs a person, by law or by design:** accounts and identity checks, approving access and secrets, the named requester on statutory requests, refunds, tax, and approval of outward messages until a standing authorisation exists.

## Opportunities
| | Item | State | Next step |
|---|---|---|---|
| Short cycle | **E6** checked list of 213 NHS suppliers with no current Carbon Reduction Plan, sold to firms that sell such plans (£195, 22 prospects, product exists) | Approved in principle 2026-11-28, subject to four conditions; two are met | Private repository; pre-sale re-check; infrastructure test |
| Longer lead | **E4** unpublished renewals report for suppliers (£295, 28 prospects) | Outreach approved in principle 2026-11-28, subject to the same conditions. Statutory requests (P3) not approved: pending demand | Infrastructure test; figures hand-checked on send day |
| Fallback | **E3** carbon plans for NHS suppliers | Suspended, launch-ready. Selling its list in E6 means a restart needs a fresh list | None unless reactivated |
| Candidate | **E5** fixing a measured weakness for hand-picked firms | Sketch only | Choose one weakness from the 564 sites already checked |
| Candidate | Referring the 213 companies to an established plan seller for a fee | Idea; one seller advertises £1,000 per referred client | Follow-on to E6 if buyers prefer paying on results |
| Simulated | S1 trend rule on five funds; S2 crypto trend rule; S3 asset watch | Running on paper | Weekly and monthly updates |

Rejected, with the deciding reason: open bounties (payers closing programmes; measured trial earned $0) · contingency recovery (needs account access and trust; platforms automate it) · freelance marketplaces (not autonomous) · marketplace listings (new listings get a median of one user [V]) · inbound lead capture (no traffic for new sites) · deal origination (needs a track record; about 20 months to a deal) · buying assets at £200 to £5,000 (earn too little; unverifiable) · goods arbitrage (no evidence of net return; hands-on) · published-data renewals calendar (free at Stotles [V]).

## Assets built [V]
- Prospecting pipeline: award notices to company to verified website to detected signal (`ops/`). Measured on 35 hand-checked sites.
- Carbon Reduction Plan generator with 428 official factors, 63 tests, independent recalculation matched on 48 of 48 lines.
- Contract data: 723 occupational health and 486 learning-system contracts since 2020; 7,160 technology award rows.
- E3 prospect list (213) and restart pack. E4 prospect list (28) with individual samples. E6 product file builder and prospect list (22).
- Trading backtests and paper ledger. Research library of 13 mechanism files.

## Decisions (newest first)
| Date | Decision | Reason |
|---|---|---|
| 2026-11-28 | Scheduled operator moved from Opus to Sonnet; Haiku for routine subagents; Opus or Fable only for listed decisions | Owner instruction; allowance nearly used |
| 2026-11-28 | New private repository to become the single source of truth; public branch to be deleted after the copy is verified | The current repository is a public fork and cannot be made private [V] |
| 2026-11-28 | Owner approved P1 (E6) and P2 (E4) in principle, with four conditions | Conditions tracked in `infrastructure/STANDING-AUTHORISATIONS.md` |
| 2026-11-28 | E6 prepared as the shorter-cycle experiment | Only candidate with a finished product; payment possible within days. Own estimate: a sale is less likely than not [E] |
| 2026-11-28 | E4: 28 vendor emails before any statutory request; requests only on three reservations and your approval | Owner instruction; no waiting on public bodies in December |
| 2026-11-28 | Name Oakmarch kept; never to be used for financial services | No company or .uk domain of that name [V]; no mark found on a third-party index [P]; near name OAKMARK is registered for investment services |
| 2026-11-28 | Scheduled operator to be moved by the owner editing the existing task | Test showed a task I create cannot push to the repository [V] |
| 2026-11-28 | E4's paid product changed to unpublished contracts | Published expiry data is free at Stotles and £155 to £189 a month at BidSkim |
| 2026-11-28 | Mailbox on Microsoft 365, not Google | Google's terms bar unsolicited commercial email outright; Microsoft's bar bulk spam |
| 2026-11-28 | Dedicated environment `capital-ops` created with a twelve-host allowlist; owner approved [V] | Default environment was unrestricted and shared with your other work |
| 2026-11-28 | Owner approved E4 for controlled validation, £25 cap | Cheap test beats more research |
| 2026-11-28 | Owner suspended E3 | Small market, hard acquisition, liability and operating burden |
| 2026-11-28 | Trading kept on paper | Backtest: 5.0% a year with a 12% worst fall; no capital created at this scale |

## Pipeline [V]
| Experiment | Prospects | Contacted | Replies | Reservations | Paid | Conversion |
|---|---|---|---|---|---|---|
| E6 | 22 (16 ready) | 0 | 0 | n/a | 0 | n/a |
| E4 | 28 | 0 | 0 | 0 | 0 | n/a |
| E3 | 213 | 0 | 0 | 0 | 0 | n/a |

## Simulations (paper only) [V]
| Book | Started | Start value | Latest | As of |
|---|---|---|---|---|
| S1 five funds, trend rule | 2026-11-28 | 1,000 | 999.0 | 2026-11-28 |
| S2 Bitcoin and Ether, trend rule | 2026-11-28 | 1,000 | 997.4 | 2026-11-28 |
| S3 asset watch | 2026-11-28 | 8 listings tracked | next check 2026-12-28 | |

## Radar: newest items
1. Checked lists as a product line: the prospecting pipeline's output is itself saleable to firms that sell to those companies (score 8). In E6.
2. Plan sellers pay for results: one advertises £1,000 per referred client (score 7). Follow-on to E6.
3. Tender tools share one gap: contracts that were never published (score 9). In E4.
Full log: `radar/RADAR.md`. Next weekly pass: on or after 2026-11-30.

## Capabilities and blockers
- **Can do now:** research, data collection from allowed public sources, prospect checks, document, list and report generation, paper trading, record keeping.
- **Cannot do yet:** send or read email, take payment, publish a website. All wait on set-up.
- **Public exposure [V]:** records were on a public branch for about a day. GitHub's log shows no views or visitors to 26 November; no secrets or identity details were in it. One file of copied contact addresses has been cleaned. Detail: `infrastructure/EXPOSURE-ASSESSMENT.md`.
- **Operator [V]:** the existing scheduled task pushes correctly and now runs on Sonnet with current instructions. It still needs the owner to change its repository, environment and connectors (step B).
- **E6 checks [V]:** all 213 companies re-confirmed active at Companies House today; Stripe's and Microsoft's terms do not bar the product on their text; non-exclusivity now stated in every E6 text. Website re-check of all 213 is still to run (`ops/E6-RECHECK.md`).
- **Not confirmed:** the official trade mark register for the name (step 0).

## Owner actions
One step at a time. **Current step: A, create the private repository** (`infrastructure/SETUP-GUIDE.md`). Then B (scheduled task), then steps 0 to 7.

## Next actions and milestones
1. Owner completes set-up; operator tests mail and payment end to end on a message and a £1 test invoice to the owner. **Milestone: first verified pass through send, receive, invoice, pay, record.**
2. E6: send to the ready firms, five on day one. **Milestone: first genuine customer interaction.** Judged ten days after the first send. **Milestone M4 if one pays: first independent customer payment.**
3. E4: send the 28 emails alongside E6. Go or no-go on statutory requests 14 days later.
4. Weekly: radar pass, paper books, this dashboard, Friday report.
Programme review: 27 December 2026.
