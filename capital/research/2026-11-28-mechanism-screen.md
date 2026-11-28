# Mechanism screen (2026-11-28): two rounds complete

Owner brief (2026-11-28): stop gravitating to "build a digital product or compliance document and advertise it". Look for an economic advantage across fundamentally different mechanisms. Not UK-only, not tied to earlier experiments. Smaller opportunities are acceptable if they build capital, infrastructure or a base for expansion.

## The test
A mechanism is worth a practical test only if all six can be answered with evidence:
1. Who already pays whom, and how much?
2. What is the inefficiency?
3. What measurable edge does automation give *us*, as opposed to anyone with the same AI?
4. What stops others copying it once it works?
5. How is the payer reached without the owner's face, an audience, or mass cold email?
6. What does it need from the owner, in capital, and from a regulator?

## What CAPITAL has, and lacks
- **Has:** near-zero cost for reading, coding, classifying and matching at scale, around the clock. A working pipeline from public award notices to company identity, verified website, detected signal and dated evidence (built for E3; accuracy measured on 564 sites).
- **Lacks:** capital, brand, audience, licences, owner time. Runs over HTTPS only, in accounts held in the owner's name.
- **So favour** mechanisms where the buyer already exists and pays on delivery, where few customers are needed, where no capital is at risk, and where regulated exposure is low.

## Map of mechanisms
| # | Mechanism | Who pays, for what | Where an edge could come from | Main obstacle | Status |
|---|---|---|---|---|---|
| 1 | Outcome-paid open work (code bounties, security review of open-source code, audit contests) | A project or platform pays on an accepted deliverable | Labour cost and parallelism; no customer to find | Supply of paid tasks; other AI agents; maintainers' rules on AI submissions | Evidence being gathered |
| 2 | Trigger-event intelligence sold to vendors | Sales-driven vendors pay per lead or by subscription | Daily reading of public registers plus verified enrichment; history accumulates into a dataset | A buyer group that really pays; incumbents | Evidence being gathered |
| 3 | Introducer commissions on triggered events (finance, payments, software) | Provider pays commission on a completed sale | Same information edge; revenue per transaction | Still has to reach the small company; regulation | Evidence being gathered with 2 |
| 4 | Contingency recovery of money owed | Claimant pays a share of what is recovered | Finding or quantifying claims at scale | Authority to act, regulation, trust, slow cycles | Evidence being gathered |
| 5 | AI labour through freelance marketplaces | Buyers already searching | Cost and speed | Everyone has the same AI; ratings start at zero; Fiverr bars automated messaging and has no seller API; Upwork's 2026 agent beta still needs the account holder to confirm each binding action | Rejected as a core mechanism: not autonomous, no edge |
| 6 | Apps or listings inside ecosystems (Shopify, Atlassian, Apify, Etsy, Workspace) | Users, through platform billing | Platform distribution | Assessed earlier; this is the product pattern the owner flagged | Not reopened |
| 7 | Search-intent capture and lead sale (programmatic pages from proprietary data) | Vendors pay per lead | Pages nobody else can generate | 6 to 12 months for search traffic; search-engine policy on scaled AI pages | Possible later add-on to 2 |
| 8 | Audience plus sponsorship | Sponsors | None without an audience | Slow | Rejected for now |
| 9 | Buying small cash-generating assets | n/a | Cheap operation | Purchases not authorised; no capital | Research only, once capital exists |
| 10 | Inventory or price arbitrage (domains, goods, keys, betting, trading) | Resale margin | None we can evidence | Capital at risk; speculative; barred by the mandate without approval | Rejected |
| 11 | Licensing a dataset | Licensees | Needs unique data with history | Long sales cycles | Only as an extension of 2 |
| 12 | Services sold by tender or agency selling (bid writing, development agency) | Clients | Cost | Human selling and accountability | Rejected: owner time |

## Round 1 evidence (2026-11-28; notes in `research/mechanisms/`, mostly secondary sources)

### 1. Outcome-paid open work: REJECTED
- Payers are withdrawing because of AI-generated volume. curl ended its bounty (Jan 2026). HackerOne's Internet Bug Bounty paused new submissions and cut payouts (Mar to May 2026). Google stopped taking open-source vulnerability reports until at least early 2027. huntr left open-source bounties. Code4rena announced a wind-down; Sherlock is replacing contests with its own AI auditor.
- What remains open to anyone (Algora, Opire) is small and crowded: one scan found 30 live bounties worth about $18k in total; bounties draw 5 to 10 competing pull requests within hours; bots watch the feeds.
- The one measured AI-agent trial found: 200+ bounties scanned, 12 genuine, 5 pull requests submitted, 0 merged, $0 earned.
- Edge: none. Every competitor has the same labour cost, and the payers are closing the door.

### 4. Contingency recovery of money owed: REJECTED for now
- Where no licence is needed (chargebacks at about 25% success fee, parcel audits at 25 to 50%, Amazon reimbursements), the claimant must hand over account access, and funded or platform-native tools already automate it. Amazon now reimburses automatically and has cut claim windows to 60 days.
- Where claimants could be found from public data (unclaimed property, estates), licences, fee caps and identity work apply, and the UK estates list has already been suspended once over fraud.
- UK late payment (about £26bn owed at any time) needs the claimant's own ledger and risks its customer relationships. A Commercial Payments Bill (May 2026) may change this in 2027; worth re-checking then.
- Edge: none over incumbents; the platforms are automating recovery themselves.

### 5. AI labour through freelance marketplaces: REJECTED
- Upwork treats unapproved bots as a violation; its 2026 agent beta lets agents search and draft, but the account holder must confirm each binding action. Fiverr permits AI-assisted work but bars automated mass messaging and bulk AI deliveries. Not autonomous, and no edge over every other seller using the same AI.

### 2. Trigger-event intelligence sold to vendors: SURVIVES, unproven
- Money changes hands for adjacent data: Stotles £99 to £475+ a month for public-contract sales intelligence; planning-application lead feeds £49 to £149 a month; larger players (Tussell, Glenigan, Barbour ABI) quote-only.
- Vendors spend heavily to acquire the customers our signals point to: finance brokers are quoted £50 to £100 per inbound invoice-finance enquiry (one lead seller's figures); an IT-channel source puts outsourced lead generation for managed IT contracts at about £1,500 per lead (unverified).
- Buyer groups are countable: 350+ Cyber Essentials certification bodies (many are managed IT firms using certification as a door-opener); about 1,400 commercial finance broker firms.
- Two searches found nobody selling "recent public-contract winners" or "missing compliance document" lists to third-party vendors. That means no competitor, and also no price benchmark.
- Channels exist that need no sales force: Datarade (30% commission on the free tier), AWS Data Exchange (3%), Apify (20%). No evidence of what small providers earn.
- Edge: the join that the incumbents do not sell (award + company + website + verified gap), accuracy we have measured, and a history that accumulates. It is thin: the source data is free and a funded incumbent could add the same signal.
- Company-level records and generic addresses are not personal data; named contacts are. Sole traders must be excluded.

### 3. Introducer commissions: PARKED behind 2
- Funding Circle's introducer guide (2022-23, may be stale) shows up to 6% commission; typical arrangement fees are 0.5 to 2% of the facility; so roughly £500 to £3,000 on a £50k loan, paid only on funded deals. Card-payment and software referral schemes pay little or nothing.
- Introducing limited companies appears to sit outside FCA credit-broking rules, but sole traders and small partnerships are inside them; not confirmed from the handbook text.
- Problem: it still requires reaching and persuading the small company, which is where E3 struggled.

## Where the advantage actually is (working view)
Nothing tested so far shows a proven, defensible advantage. What the evidence does suggest:
1. **Cost structure, not capability.** Everyone has the same AI. Our difference is that a niche worth £2,000 to £5,000 a month, too small for a funded company or a salaried team, can still be profitable here.
2. **Few customers, each worth a lot.** Mechanisms needing hundreds of small buyers (E3) hit the acquisition wall. Selling to a few dozen sales-driven firms does not.
3. **Accumulating data.** Daily snapshots and verified joins become harder to copy with time.
That points at business-to-business intelligence for buyers with high customer value, run as a portfolio of narrow feeds on one pipeline. It does not yet prove anyone will pay.

## Round 2 evidence (2026-11-28)

### 8. Deal origination for acquirers of small companies: REJECTED for now
- The fees are the largest seen in this screen: retainers quoted at $5,000 to $25,000 a month and success fees of 1 to 5% of the price (vendor-published figures).
- Search itself is commoditised by tools at about $15,000 a year. What buyers pay for is trusted conversations with owners and completed deals.
- Buyers rarely accept success-only terms from an unknown provider and ask for a track record. Median time from search to acquisition is about 20 months. An operator with no record and no capital cannot fund that wait. Unregistered-finder risk in the US; UK position needs legal advice.
- Keep as a later stage: it becomes possible once CAPITAL has a track record and its own company dataset.

### 9. Inbound enquiries captured and sold per lead: REJECTED
- Payouts are real but low: about $30 to $45 a call for US home services; £7 to £75 for a UK solar or heat-pump enquiry.
- A newcomer cannot get the traffic: 2 to 6% of new pages reach the first results page within a year; AI summaries cut clicks to the top result by about 58%; scaled AI-written sites are being removed (one documented case lost over 200,000 queries); AI assistants send 0.1 to 1% of visits.

### 6. Supply-side positions in ecosystems: REJECTED, on first-hand data
- Apify is the only ecosystem found that publishes per-listing demand and pays out real money. Its public store data (top 60,000 of 119,369 listings, pulled 2026-11-28 with `ops/apify_store_probe.py` logic) shows:
  - Paid listings: median 1 monthly user; 90th percentile 10; 99th percentile 183.
  - New listings (every user arrived in the last 90 days): 3,282 of them; median 1 monthly user; 1% reach 10; one reaches 50.
  - 236 authors already run portfolios of 50 or more listings (several run 500 to 1,000). Their median is 360 monthly users in total, 2.6 per listing. The "large portfolio maintained cheaply by AI" idea is already crowded.
  - Public-register listings: 4,059 of them share 8,267 monthly users; 60 have 20 or more. Typical price $4 per 1,000 results.
  - Rough yield: Apify's last published monthly payout ($563k, September 2025) divided by today's 1.27 million user-listing pairs is about $0.44 per user per month. A new listing would earn a few dollars a month.
- Paid tools for AI agents: under 5% of about 16,000 servers earn anything (author estimates); pay-per-call volume is tiny. No evidence of supply shortage anywhere a newcomer can enter.

## What the two rounds show
1. **Anything open to "anyone with an AI agent" is saturated or closing.** Bounty payers are shutting programmes because of AI volume. New marketplace listings get one user. Search no longer feeds new sites. Six of the eight mechanisms tested fail for this one reason.
2. **So the advantage cannot be capability. It has to be a position others lack:** data that is hard to obtain or assemble, a trusted relationship, a licence, capital, or assets the owner already holds. CAPITAL has a start on the first and none of the others.
3. **The few-customers, high-value shape is the one that fits.** UK public bodies published 2,577 software and IT award notices in 23 months, to 1,566 suppliers, from 713 buyers, with median award values of £180,000 to £800,000 by category. Vendors with deals that size already pay £1,200 to £11,000 a year each for procurement intelligence.

## Direction recommended
**Procurement intelligence for vendors, built on data that is not free to copy.** Two sources of edge, in order of strength:
1. **Information obtained by statutory request (FOI) and parsed at scale.** Which body uses which supplier, at what value, ending when: facts award notices mostly do not contain. Sending and chasing 100 to 200 requests and reading as many differently formatted replies is laborious for people and cheap for software. This is experiment E1, already drafted, in sharper form.
2. **Verified joins of public registers** (award, company, website, detected gap), which exist now from the E3 work. Thinner edge: the inputs are free.

What is honest to say about it:
- It is still a data product sold by direct approach, to a few dozen vendors per category. The difference from E3 is who pays and why: a few buyers with large contract values, and an edge in the data, not in the ability to build.
- Willingness to pay for a niche report is unproven. General tools have published prices; a one-category snapshot does not.
- Ceiling per category is plausibly a few thousand pounds a year at first. Scale comes from repeating across categories and refreshing annually, and from the dataset that accumulates. That dataset is also what the higher-fee mechanisms (deal origination, introductions) would later need.
- Replies to statutory requests take 20 working days, so data from requests sent in early December arrives after the 27 December review. Vendor interest in a free sample can be measured before then.

## Next steps
**Now, no spend and no outbound contact:**
1. Classify the 2,577 software and IT notices into product categories and pick one with at least 40 vendors and 100 buyers that existing tools cover poorly.
2. Confirm the re-use terms for information released under FOI and typical response rates for that kind of question.
3. Build the free sample for that category from published data.

First cut done 2026-11-28: see `research/procurement-intel/README.md`. Categories with 40 or more vendors include CCTV and body-worn video (123 vendors, 82 small), HR and payroll (49), Microsoft licensing (52), networks (81) and print and mail (59).

**Needs owner approval before it happens:**
- Sending statutory requests to public bodies (needs a named requester: the owner or a trading name).
- Approaching the category's vendors with the sample.

**Owner-only options that would open other mechanisms** (not requested, noted for completeness): a small budget to buy an asset that already has users; or the owner's own trade knowledge and contacts as the trusted position.
