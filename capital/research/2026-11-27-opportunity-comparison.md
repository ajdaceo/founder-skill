# Opportunity comparison, 2026-11-27

Six parallel research threads (about 120 leads between them) plus a second round on the Atlassian direction.
Limits: web search summaries only. Page fetches are blocked in this environment, so marketplace install counts, prices, review text and vote totals were mostly not readable. No thread found search-volume data. Treat "not found" as "not verified", not as "absent".

## The main finding
Quick-to-build niches are no longer open. Across every thread, a dated event or new need drew several small tools within weeks, usually free or under $10:
- Microsoft To Do retirement (announced 18 Nov 2026): a $6.99 mover and five open-source exporters within nine days.
- EU withdrawal button (19 Jun 2026): about 10 Shopify apps, one with 582 reviews.
- EU AI Act labelling: six or more free WordPress plugins.
- AI-faked refund photos: seven or more Shopify apps.
- Lemon Squeezy wind-down: a free drop-in replacement plus four paid vendors.
Consequence: speed of build is not an advantage. An edge has to come from something slower to copy: a channel with a barrier to entry, engineering depth, correctness that needs sustained maintenance, or buyers who pay for trust.

## Scorecard (gates from STATE.md; Y = evidenced, ? = unverified, N = fails)

| Candidate | Growing demand | Repeated frustration | Weak incumbents | Active search | Our edge | Zero-ad channel | Cost justified | Verdict |
|---|---|---|---|---|---|---|---|---|
| QuarterReady (MTD workbook) | Y | ? | N | ? | N | ? | Y | Suspended by owner |
| Atlassian Cloud apps for Data Center migration gaps | Y | Y (general) | ? per gap | Y | ? per gap | Y | Y | Lead direction; specific gap not yet proven |
| MCP app for Jira/Confluence Data Center | Y | Y | Y | Y | Y | N | N | Rejected: platform closed to new customers Mar 2026, read-only Mar 2029 |
| Bitbucket Cloud Forge replacements | Y | ? | ? | ? | ? | Y | N | Parked: no Atlassian billing for Bitbucket apps |
| Trello approvals Power-Up | ? | Y (one thread) | Y | ? | ? | Y | Y | Parked: thin evidence, $9.99 bundle competitor |
| Stripe app: German e-invoices | Y | ? | N (3 rivals, one endorsed) | ? | N | Y | ? | Rejected |
| UK DMCC subscription-rule add-on | ? date disputed | N | ? | ? | N | Y | ? | Rejected: host apps will absorb it |
| Live-capture refund evidence (Shopify) | Y | Y | N (7+ apps) | Y | N | Y | Y | Rejected: crowded |
| ChatGPT product-feed validator (WooCommerce) | ? (AI traffic under 0.1%) | Y (one thread) | N | ? | N | Y | ? | Rejected |
| Zendesk Sell / Quip full-history export | Y | ? | ? | ? | ? | ? | ? | Rejected: unknown population, enterprise trust barrier, free migrations |
| Minecraft 26.x plugin scanner | Y | Y | Y | ? | N (clone in days) | Y | N (hundreds/month) | Rejected as a business |
| Hytale / Rust / Blender add-ons | ? | ? | N | ? | N | Y | N (sales in tens) | Rejected |
| CAM reconciliation, small US landlords | ? | Y (one thread) | ? | ? | ? | ? | ? | Parked: one thread of evidence |
| Fiduciary court accountings (US states) | ? | ? | N in California | ? | ? | ? | ? | Parked: liability, per-state formats |
| Companies House filing 2028 | Y | ? | N (6+ entrants, ~£20/yr) | Y | N | Y | N until 2028 | Rejected |
| CPSC eFiling prep / EU CRA kit for indie vendors | Y | ? | ? | ? | ? | ? | ? | Not investigated enough; second-tier |

## Why Atlassian Cloud is the lead direction
EVIDENCE
- Forced migration: Data Center closed to new customers 30 Mar 2026, no expansions after 30 Mar 2028, read-only 28 Mar 2029 (Atlassian "Ascend" announcement and partner summaries).
- Parity gaps are real and documented by the vendors themselves: Confluence Cloud has no user macros; ScriptRunner Cloud lacks features such as custom REST endpoints; Jira Workflow Toolbox reportedly carried about a third of its Data Center functions to Cloud; JSM migration drops canned responses, mail handlers, custom notifications; "Request Access" and "Rename SLAs" have no Cloud equivalent.
- Channel: buyers search the Marketplace from inside the product; Atlassian bills the customer; revenue is recurring per user.
- Economics: 0% revenue share on the first $1M of lifetime Forge revenue from 1 Jan 2026; Forge hosting provided by Atlassian; Silver partner tier has no sales minimum.
- Money is being made: over $6bn lifetime Marketplace sales, 2,000+ partners (secondary source). Earnings concentrate in test management, time tracking, portfolio, advanced administration and workflow tools.
- Incumbents are distracted: Connect end of support is Q4 2026 to Jan 2027, so established vendors are spending this year rewriting existing apps for Forge.
ASSUMPTION / NOT VERIFIED
- That a specific gap exists with meaningful demand and no adequate Cloud app. Simple gaps are taken: default field values (2,799 votes) already has four apps including a free one.
- Small-vendor earnings. No first-hand revenue report from a solo vendor was found. Earnings may concentrate in large vendors.
- Costs at £0: the partner programme lists a bug bounty requirement at all tiers; whether that costs a new vendor money is unverified.
- App review takes 10 to 15 business days, and support obligations apply.

## What would prove or kill it
Data that exists publicly but cannot be read from this environment:
1. Marketplace REST API: per-app install counts, hosting (Connect vs Forge), last release date, rating, price. Query: Data Center apps with high installs and no Cloud version; Cloud apps with high installs still on Connect or not updated in 12 months; categories where the top app is rated under 3.5.
2. Public tracker (jira.atlassian.com): open Cloud suggestions sorted by votes, cross-checked against Marketplace search results.
3. Community forums: threads asking for an app, with no accepted answer.
Kill conditions: no gap with at least 500 votes or 1,000 legacy installs and fewer than two adequate Cloud apps; or a mandatory vendor cost that breaks the £0 allowance.

## Decision
No product is selected. Atlassian Cloud migration-gap apps are the only direction that clears the channel, payment and demand gates; the specific product is unproven and will not be built until the data above confirms a gap.

## Addendum, 12:45 UTC cycle (search only)
- Atlassian vendor costs: bug bounty participation is mandatory for Silver tier and above and for trust badges; a community post reads the programme as Atlassian-funded. Whether a brand-new vendor below Silver must join, and at what cost, is NOT verified. Forge pricing and free allowance: not found.
- The "Runs on Atlassian" badge is reported as being retired on 31 Dec 2026 (Atlassian trust page via search summary), so it is not a durable differentiator.
- CPSC eFiling: CPSC's own registry is free and optional; no seller-forum complaints, tools or broker fees surfaced. No evidence of an unserved paid need. Rejected unless forum evidence appears.
- EU Cyber Resilience Act kit for one-person vendors: 11 Dec 2027 date stands in the sources found; micro and small firms get a simplified technical-documentation form that the Commission has still to publish. An official free form would undercut a paid generator. Parked until that form's status is known.
- marketplace.atlassian.com is still unreachable from this environment.
