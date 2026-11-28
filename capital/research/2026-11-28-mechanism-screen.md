# Mechanism screen (started 2026-11-28) — WORKING NOTE, evidence still arriving

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

## Round 2 (in progress)
Three further mechanisms with higher ceilings or different payers:
- Deal origination for acquirers of small companies (retainers and success fees).
- Supply-side positions in ecosystems that publish demand data and pay per use (including tools sold to other AI agents).
- Inbound enquiries captured and sold per lead or per call.

## Decision and smallest tests
Pending round 2.
