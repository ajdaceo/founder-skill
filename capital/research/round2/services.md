REPORT: Automated B2B / outcome-based services (27 Nov 2026)

Method and limits: about 25 web searches and no page fetching, so every EVIDENCE item is a search-result summary of the cited page, not a full read. Most pricing evidence comes from vendor marketing pages. Anything not sourced is labelled ASSUMPTION.

## What I examined and dropped

Most of the obvious outcome-paid niches already have AI entrants pricing at near-zero margin.

- **Amazon FBA reimbursement:** commissions run 10-25%, with 25% most common among managed providers and Helium 10 at 15-18%. Since 31 March 2025 Amazon reimburses lost units at manufacturing cost rather than sale price, which shrinks the pool. EVIDENCE: https://www.refunzo.com/blog/amazon-fba-reimbursement-commission-rates/ , https://groweventure.com/amazon-fba-reimbursement-services/
- **Chargeback representment:** Chargeflow charges 25% of recovered amounts and flat-fee competitors are attacking it. It is also a marketplace app, which we already rejected. EVIDENCE: https://www.chargeflow.io/pricing , https://apps.shopify.com/chargepay
- **Parcel audit:** contingency is 25-50% in the US, but most European carriers give no delivery guarantee on standard parcels, so the UK pool is thin. EVIDENCE: https://rocketfuelrecharge.com/blog/parcel-audit-companies , https://dispatch.ly/blog/parcel-audit-software
- **UK tender bid writing:** humans charge £1,750-£8,000 per bid, but AI services already sell at £149/£349/£749 per bid (SwiftBid), about £600 plus a 5% success fee (BidFinder), and £99-£149/month unlimited (CleanTender, AI Tender Writer). EVIDENCE: https://aitenderwriter.com/resources/comparisons/tender-writing-services , https://swiftbid.co.uk/ , https://bidfinder.uk/ , https://cleantender.co.uk/resources/comparisons/ai-tender-software
- **PDF accessibility remediation:** humans charge $4-$18 per page, but AI vendors already sell at $0.30-$3.50. The US ADA Title II deadlines were pushed to April 2027 and April 2028. EVIDENCE: https://harboraccessibility.com/blog/pdf-remediation-cost-per-page/ , https://casocomply.com/services/pdf-remediation , https://www.federalregister.gov/documents/2026/04/20/2026-07663/extension-of-compliance-dates-for-nondiscrimination-on-the-basis-of-disability-accessibility-of-web
- **Innovate UK grant writing:** success fees of 5-15% exist, but Smart grants have been paused since January 2025 and success rates are very low. EVIDENCE: https://echogrant.com/resources/grant-writing-cost , https://ukgrantfunding.co.uk/
- **Business rates:** the VOA has formally documented a cold-call, upfront-fee, lock-in pattern among agents, and the work needs valuation judgement. EVIDENCE: https://www.businessrateseligibility.co.uk/business-rates-revaluation-explained
- **Upwork product data entry:** median fixed-price budget was $33 across 2,829 postings. EVIDENCE: https://gigradar.io/blog/how-to-get-a-data-entry-job-on-upwork-as-a-freelancer
- **Packaging EPR data service:** I found no price evidence, so I am not proposing it.

The three below survive because payment is on results and the work is messy, document-heavy and client-specific, not a tool.

---

## CANDIDATE 1: Customs duty overpayment audit and reclaim for small UK importers (contingency)

**1. Who pays.** UK importers of record, mainly SMEs paying roughly £5k-£200k a year in duty (ASSUMPTION on the band). Accountants and freight forwarders are referrers.

**2. The problem.** Duty is overpaid through wrong commodity codes, unclaimed tariff preference, valuation errors and unclaimed reliefs. The declaration was made by an agent and the importer never checks it.
- EVIDENCE: preference utilisation on UK imports from the EU is about 90%, so some eligible imports still pay duty; ONS reports £118.7bn EU imports of which £107.4bn preferential. https://www.ons.gov.uk/businessindustryandtrade/internationaltrade/articles/useofpreferentialtariffsbyukbusinessesforimportsofgoods/2012to2023/pdf , https://www.uktpo.org/wp-content/uploads/Publications/Briefing-Papers/UKTPO-2024-BP-72.pdf
- EVIDENCE (vendor claims, unverified): "1 in 7 EU-UK shipments overpaying" and one manufacturer recovering £221K in missed preference. https://falsum.co.uk/insights/isnt-uk-eu-trade-duty-free , https://www.borderaudit.io/resources/case-studies
- EVIDENCE: the importer of record can claim even if the agent caused the error, within 3 years, via C285 in CDS. https://www.gov.uk/guidance/apply-for-a-repayment-of-import-duty-and-vat-in-the-customs-declaration-service , https://plutos.org.uk/c285-reclaim-overpaid-duty-uk/

**3. What they spend now.**
- AAB runs reclaim projects no-win-no-fee, with the fee payable when the refund arrives. EVIDENCE: https://aab.uk/services/tax/customs-duty/
- Avocet Consulting works "wholly contingent". EVIDENCE: https://avocetconsulting.uk/duty-recovery
- Duty Refunds charges 15% of the refund and serves consumers returning goods. EVIDENCE: https://dutyrefunds.co.uk/blog/reclaim-customs-charges/
- BorderAudit sells flat-fee software with "never a success fee". EVIDENCE: https://www.borderaudit.io/product/duty-reclaim
- International contingency benchmarks are 15-30% of duty recovered, mostly from US sources. EVIDENCE: https://gingercontrol.com/blog/customs-duty-audit-guide , https://customsbrokerindex.com/blog/duty-drawback-specialist-the-complete-guide/
- No UK business-to-business contingency percentage is published.

**4. Frequency.** Every import entry can carry an error. There is a rolling 3-year lookback, so one retrospective job per client plus ongoing monitoring (EVIDENCE for the 3 years above; ASSUMPTION for monitoring demand).

**5. Reaching customers without ads or calls.**
- Publish a free self-serve "upload your CDS export, see estimated overpayment" checker. HMRC's "Get customs data" service is now free; paid reports ended 31 March 2026. EVIDENCE: https://www.customs-declarations.uk/hmrc-launches-free-get-customs-data-service-what-uk-traders-need-to-know/ , https://hc-customs.com/guides/hmrc-get-customs-data/
- Programmatic search pages per commodity code and origin ("duty on X from Y: are you overpaying?").
- Written referral agreements with small accountancy practices and freight forwarders, by email, on a revenue share.
- Answering questions in importer and e-commerce forums. (All channel effectiveness is ASSUMPTION.)

**6. What we could charge.** 20% of duty actually repaid, no fee otherwise; later £49-£199/month for monitoring new entries (ASSUMPTION, placed inside the 15-30% benchmark).

**7. Automatable versus not.**
- Automatable: parsing CDS data, flagging code/description mismatches, unclaimed preference by origin, valuation anomalies, duplicates; drafting the C285 claim pack; requesting origin statements from suppliers by email; tracking claims.
- Needs a human or login: the importer must pull the data with their own Government Gateway organisation ID, because agent IDs cannot be used. EVIDENCE: https://hc-customs.com/guides/hmrc-get-customs-data/
- Needs a human or login: C285 submission needs the client's CDS login or a written direct-representation authorisation, and repayment goes only to a UK bank account. EVIDENCE: https://www.gov.uk/guidance/apply-for-a-repayment-of-import-duty-and-vat-in-the-customs-declaration-service , https://easyclearance.pl/en/articles/pelnomocnictwo-celne-direct-indirect-uk.html
- Retrospective preference claims need a valid origin statement from the supplier, which is an external dependency (ASSUMPTION on how often suppliers cooperate).
- The owner signs engagement terms and buys professional indemnity cover (ASSUMPTION on cost).
- Borderline classifications need a human expert or a binding HMRC ruling; we should only file clear-cut cases.
- No licence today: the UK has no customs broker licence. EVIDENCE: https://www.tevolution.international/post/who-can-classify-your-goods-customs-brokers-and-ai-uk-eu-us

**8. Hard to replicate.** A growing private dataset of real declarations, HMRC outcomes per code and error type, per-agent error patterns and supplier origin documents; referral relationships; a claims track record (ASSUMPTION that this compounds; BorderAudit and cat360 are already building similar).

**9. Willingness to pay.**
- Several firms sustain no-win-no-fee duty practices (AAB, Avocet, above).
- Duty Refunds has about 304 Trustpilot reviews, several calling the 15% fee fair. EVIDENCE: https://uk.trustpilot.com/review/dutyrefunds.co.uk
- BorderAudit publishes "£447K recovered" case studies. EVIDENCE: https://www.borderaudit.io/resources/case-studies

**10. Validation (under £50, two weeks).** Domain plus a landing page with a manual free audit offer (£10-£15). Post in 5 importer communities and email 30 small accountancy or forwarder firms one personalised partnership note each.
- Pass: at least 3 importers upload real CDS data and at least 1 file shows a defensible overpayment of £1,000 or more.
- Fail: fewer than 3 uploads, or no file with a clear recoverable error.

**11. Path (all ASSUMPTION; average recovered £4,000 per client, fee £800).**

| Monthly profit | What it takes |
|---|---|
| £100 | 1 paid claim every 8 months; realistically the first payout arrives in month 3-5 because of HMRC processing lag |
| £1,000 | about 1.3 paid claims a month |
| £5,000 | about 5 claims a month plus about 20 monitoring subscribers at £50 |
| £10,000 | about 9 claims a month plus about 60 subscribers, needing roughly 10 active referral partners |

**12. Ongoing human involvement.** The owner signs client and partner agreements, holds the bank account and insurance, and gives occasional sign-off on borderline claims: about 1-3 hours a week (ASSUMPTION). No calls needed if everything runs by email and portal.

**Risks.**
- An audit will also surface underpaid duty, which creates disclosure obligations for the client and deters some.
- Wrong claims risk HMRC penalties for the client and liability for us.
- Mandatory registration of customs intermediaries is under consultation. EVIDENCE: https://www.gov.uk/government/consultations/introduction-of-mandatory-registration-for-customs-intermediaries/customs-intermediaries-introduction-of-mandatory-registration
- This is customs advice, not regulated tax advice by licence, but it sits close to the "no tax advice" boundary and the owner should decide whether it is acceptable.

**Strongest reason it fails.** Small importers will not go through the Government Gateway data pull or trust an unknown firm with their declarations, and supplier origin evidence proves unobtainable, so found money cannot be claimed.

**Neglected segment.** Importers too small for AAB or Avocet-style consultancies and unwilling to buy and operate audit software themselves (ASSUMPTION).

---

## CANDIDATE 2: Statutory late-payment compensation and interest recovery (contingency)

**1. Who pays.** UK small businesses that invoice larger businesses and are routinely paid late, especially on ex-customers or customers they no longer fear losing.

**2. The problem.** They are legally owed money they never claim.
- EVIDENCE: fixed compensation is £40, £70 or £100 per late invoice by invoice size, plus interest at 8% over base (11.75% for July-December 2026). It is claimable for 6 years, including on invoices since paid. https://www.smoothcl.co.uk/site/services/commercial-litigation-solicitors/late-payment-law/ , https://judgelaw.co.uk/debt-recovery/how-to-recover-unpaid-invoices-uk-2026-guide/ , https://lovetts.co.uk/debt-recovery-information/late-payment-law/
- EVIDENCE: the barrier is exactly AI-shaped work. A credit-management body cites "the huge amount of time and effort required to analyse the sales ledger" over 6 years. https://cpa.co.uk/meaningful-financial-compensation-for-being-paid-late/
- EVIDENCE: government puts the cost of late payment at £11bn a year and 38 business closures a day. https://www.gov.uk/government/news/largest-crackdown-on-late-payments-in-over-25-years-as-landmark-bill-enters-parliament

**3. What they spend now.**
- StatClaim charges 10% of compensation and interest recovered, no win no fee. EVIDENCE: https://statutoryclaimonline.uk/late-payment-compensation/
- General commercial debt contingency is 8-25%, and flat demand letters cost £150-£450. EVIDENCE (vendor page): https://www.cosmodca.com/help-article/debt-collection-agency-fees-uk
- Other players: Late Payment Action, Thomas Higgins, latepayclaim.com. EVIDENCE: https://latepaymentaction.com/insights/what-is-a-late-payment-claim/ , https://www.thomashiggins.com/missed-out-on-compensation.html , https://latepayclaim.com/

**4. Frequency.** Continuous. Every late invoice creates a new entitlement, and there is a one-off 6-year backlog per client.

**5. Reaching customers without ads or calls.**
- Build a public "does [company] pay late, and what are you owed?" page for each large payer from the government's payment-practices data, which has an export. EVIDENCE: https://check-payment-practices.service.gov.uk/export/ (cited in https://assets.publishing.service.gov.uk/media/6a50c8a69e9c95844ae64ca1/large-business-payment-practices-statistics-methodology-and-background-quality-report.pdf)
- Offer a free ledger-upload calculator.
- Ride the 2026 legislation news cycle with explanatory content. EVIDENCE that the Bill was introduced 19 May 2026 with mandatory interest, a 60-day cap and fines: https://www.bakermckenzie.com/en/insight/publications/2026/05/united-kingdom-late-payment-bill-impact-for-commercial-contracts
- Email partnerships with bookkeepers.
- The same data improves with every outcome: which debtors pay on a first letter becomes proprietary. (Channel performance is ASSUMPTION.)

**6. What we could charge.** 20% of sums recovered, or 15% via bookkeeper partners; optionally £29-£99/month for ongoing automatic claims on new late invoices (ASSUMPTION; above StatClaim's 10%, inside the 8-25% band).

**7. Automatable versus not.**
- Automatable: ingesting Xero, QuickBooks or CSV ledgers; determining due date against paid date per invoice; computing compensation and interest; generating a claim schedule and letters; sending by email and post API; chasing; reconciling payments.
- Needs a human or login: client authorisation, and ledger access through the client's accounting login or an export.
- Contract terms can alter entitlement, so terms need reviewing per client. EVIDENCE: https://www.smoothcl.co.uk/site/services/commercial-litigation-solicitors/late-payment-law/ A debtor in one forum case argued agreed 60-day terms and a course of dealing. EVIDENCE: https://payontime.co.uk/discussions-forums/2-the-late-payment-of-commercial-debts-interest-act/599-retrospective-compensation
- We must not issue or run court claims. Conduct of litigation is reserved to authorised persons; the Mazur ruling (September 2025) said so and its appeal outcome is reported inconsistently. EVIDENCE: https://www.bailii.org/cgi-bin/format.cgi?doc=/ew/cases/EWHC/KB/2025/2341.html , https://cpa.co.uk/high-court-confirms-only-qualified-solicitors-can-conduct-litigation/ If a debtor refuses, the client files the money claim themselves or goes to a partner solicitor.
- Debtors will sometimes phone, so a voicemail-to-email line is needed (ASSUMPTION).

**8. Hard to replicate.** A debtor-behaviour database (who pays statutory claims, after how many letters, which defences they raise), bookkeeper relationships, and a reputation with accounts-payable departments (ASSUMPTION).

**9. Willingness to pay.**
- Several firms sustain no-win-no-fee services (above).
- Suppliers do pursue these: one forum case involved a £3,000 small claim at £40 per invoice over 3 years. EVIDENCE: payontime.co.uk link above.
- I found no incumbent revenue figures or review volumes, so demand evidence is thinner than for Candidate 1.

**10. Validation (under £50, two weeks).** Landing page plus a calculator taking a CSV export of invoice, due and paid dates (£15). Recruit through 5 small-business and bookkeeper communities and 30 personalised emails to bookkeepers.
- Pass: at least 5 real ledgers uploaded, at least 2 clients sign authority for us to send claims to at least one ex-customer, and the median claimable sum per ledger is £1,000 or more.
- Fail: uploads arrive but nobody will authorise a claim.

**11. Path (all ASSUMPTION; average ledger yields £3,000 claimed, 35% collected without court, 20% fee, so about £210 per client backlog).**

| Monthly profit | What it takes |
|---|---|
| £100 | 1 client every 2 months |
| £1,000 | 5 new clients a month, or 2 larger ledgers of £15k claimable |
| £5,000 | about 15 clients a month, skewed to firms with 500+ late invoices, plus 40 subscribers at £40 |
| £10,000 | about 30 clients a month plus 100 subscribers; requires the bookkeeper channel, with each practice bringing several clients |

Unit economics are weaker than Candidate 1 unless ledgers are large.

**12. Ongoing human involvement.** The owner holds the client-money or receiving arrangement (simpler if debtors pay the client directly and we invoice our fee), signs partner terms, and handles the rare complaint: 1-2 hours a week (ASSUMPTION).

**Risks.**
- Straying into reserved legal activity (litigation).
- Giving what is effectively legal advice on contract terms. I did not verify whether this is restricted, so get a one-off solicitor review of the template pack and process (ASSUMPTION that this suffices).
- Reputational harm to clients' trading relationships.
- The pending Bill could change compensation rules. EVIDENCE of pending change: https://kpmg.com/uk/en/insights/advisory/small-business-protections.html
- Commercial debt collection sits outside financial-conduct regulation in my understanding; this is unverified and should be checked (ASSUMPTION).

**Strongest reason it fails.** Large debtors ignore letters that have no litigation threat behind them, and clients will not sue or risk the relationship, so collection rates fall far below my 35% assumption.

**Neglected segment.** Micro-suppliers with hundreds of small invoices to large payers (trades, hauliers, agencies, wholesalers), where manual ledger analysis is uneconomic for human firms (ASSUMPTION, supported by the ledger-effort quote in point 2).

---

## CANDIDATE 3: Patent prior-art bounties (Unified Patents PATROLL), then paid prior-art searches

**1. Who pays.** Unified Patents, funded by its member companies, pays cash prizes to whoever submits the best invalidating prior art for specified patents. Later: patent attorneys and defendants in infringement disputes (ASSUMPTION for that later stage).

**2. The problem.** Companies sued by patent-assertion entities need prior art to invalidate weak patents. Search is skilled, slow, multilingual reading.

**3. What they spend now.** $2,000 per contest is typical, with some announcements totalling $4,000. EVIDENCE: https://www.unifiedpatents.com/insights/2026/11/19/2000-for-techsys-insights-optical-patent-prior-art , https://www.unifiedpatents.com/insights/category/PATROLL . Commercial search prices were not verified in this session.

**4. Frequency.** Multiple new contests a month: I saw two posted on 19 November 2026, three on 19-21 October, and others in May, August and September. EVIDENCE: https://www.unifiedpatents.com/insights/tag/New+Contest . The total open at any time was not found.

**5. Reaching customers.** None needed. Contests are public, which removes the cold-start trust problem entirely. Published wins become the portfolio for later inbound attorney work (ASSUMPTION).

**6. What we could charge.** The prize ($2,000) per win; later a fixed price or a pay-only-if-relevant-art-found fee per search (ASSUMPTION).

**7. Automatable versus not.**
- Automatable: claim parsing, multilingual patent and non-patent literature search, date verification, element-by-element claim charts.
- Needs a human or login: a researcher account in the owner's name, and charts must be generated in Unified's own tool, Pearl, capped at 30 charts per researcher per month, addressing every claim limitation. EVIDENCE: https://www.unifiedpatents.com/insights/category/PATROLL
- Unknown: whether the rules permit AI-prepared submissions. I could not find this; it must be read before entering.
- Prize payment and tax paperwork fall to the owner.

**8. Hard to replicate.** Weak at first, since anyone with a good model can enter. What compounds is an indexed corpus of obscure non-patent literature (manuals, standards drafts, theses, non-English documents) and a public win record (ASSUMPTION).

**9. Willingness to pay.** Unified publicly posts prizes and winner announcements continuously through 2026. EVIDENCE: links above.

**10. Validation (£0, two weeks).** Read the rules; enter 3 open contests (one seen expiring 5 December 2026) with complete Pearl charts.
- Pass: the rules allow AI-assisted work, and for at least 2 of 3 patents the agent finds pre-priority-date art mapping every limitation of the challenged claim, verified by a second independent pass.
- Fail: the rules prohibit it, or no complete mappings. Actual wins will take longer than two weeks to learn.

**11. Path (ASSUMPTION).**

| Monthly profit | What it takes |
|---|---|
| £100 | 1 win a year |
| £1,000 | about 1 win every 6 weeks |
| £5,000 | about 3 wins a month, likely near the ceiling given contest supply and competing researchers |
| £10,000 | not credible on bounties alone; requires converting the track record into about 10 paid searches a month from attorneys, which is unproven |

**12. Ongoing human involvement.** The owner's identity on the account, payout and tax forms, and occasional rule acknowledgements: under 1 hour a week (ASSUMPTION).

**Risks.**
- Platform rule or programme changes: there is a single payer.
- Other entrants using the same models compress win rates.
- No client liability to speak of. A patent attorney, not us, makes any legal judgement.

**Strongest reason it fails.** It is a prize contest with one buyer and a hard supply ceiling, and good easily found art is already known, so win rates may be near zero.

**Neglected segment.** Non-English and non-patent literature, where an agent's breadth is a real edge (ASSUMPTION).

---

## Honest ranking

1. **Customs duty reclaim** is strongest: recurring errors on every import, a statutory 3-year refund route, free machine-readable source data since 2026, several incumbents sustained purely on contingency, a client-specific dataset that compounds, and an email-only referral channel. Its main weaknesses are data-access friction, supplier origin paperwork, liability for wrong claims, and its closeness to the owner's "no tax advice" line.
2. **Late-payment compensation recovery** has the best timing (the 2026 Bill) and the most AI-shaped bottleneck (six-year ledger analysis), plus a free public dataset for search content. But per-client revenue is small, collection without litigation is unproven, and it sits beside reserved legal activity, so I rank it second and would not start without a solicitor reviewing the templates.
3. **Prior-art bounties** are the only option with literally no customer acquisition and a £0 test. They are a capped, single-payer income stream, not a £10k/month business, and are best treated as a cheap proof of capability.

None of the three is clone-proof. The first two win only if the accumulated outcome data and referral relationships are built deliberately from the first client. Running the under-£50 tests for 1 and 2 in parallel is cheap, and the pass thresholds in each section decide which to continue.