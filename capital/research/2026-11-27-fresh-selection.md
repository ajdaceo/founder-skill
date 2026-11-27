# Fresh opportunity selection (started 2026-11-27, owner directive: first principles, no preference for earlier research)

Method: rank by evidence of paid demand and an accessible channel first; then economics, operations, legal, owner time.
Preferred shape (not a rule): an existing ecosystem that supplies buyers, billing, payouts and ideally hosting.

## Ecosystems examined so far

### Apify Store (marketplace for scrapers/automations; Apify bills users and pays developers monthly)
- EVIDENCE: Apify keeps 20% commission; payouts monthly, minimum $20 PayPal / $100 other; KYC required (docs.apify.com/platform/actors/publishing/monetize; help.apify.com payouts article).
- EVIDENCE: top independent creators make over $10,000 MRR (Apify help centre). Selection-biased; no median published.
- EVIDENCE (Store API, 2026-11-27): head of store is social/maps scraping (Google Maps 44,951 users/30d; Instagram 58,069). UK niche actors are small: Companies House actors 2–49 users/30d at $0.0015–$0.008 per result; FCA register 5; CQC leads 5.
- ASSUMPTION: at those prices a niche UK actor with ~50 monthly users earns tens of dollars a month. Head categories carry platform-ToS risk (social sites) and heavy competition.
- EVIDENCE (Store API, 2026-11-27 21:45): 'UK' search: most actors 1–49 users/30d at $0.0009–$0.004/result (Autotrader, Zoopla, Gumtree, grocery); planning applications: 15+ competing actors, 0–11 users/30d each.
- Verdict 21:45: oversupplied long tail; rejected for the first experiment (Gate C).
- Verdict so far: good operations fit (hosted, billed, no customer comms); weak economics for a quick first sale unless a niche with high per-run value is found. Keep as candidate; next check: high-price PPE actors with few competitors and legally clean sources.

### Etsy (digital downloads)
- EVIDENCE: UK fees £0.15 listing, 6.5% transaction, 4% + £0.20 processing, 0.32% regulatory; one-time shop setup fee $15–$29 for new shops (Xero, Huskai, Craftybase).
- EVIDENCE: AI-made digital downloads still allowed with disclosure after the 22 Oct 2026 tightening; AI-generated functional instructions (patterns, recipes, manuals) banned.
- EVIDENCE: Open API v3 supports creating digital listings and uploading files; seller apps approved within minutes; no messaging endpoint, so buyer messages need a human in the Etsy app.
- Gap: demand data. etsy.com blocks automated fetching (robots). Need a permitted data source (e.g. owner screenshot of search results, or a paid research tool) before choosing a niche.
- Verdict so far: strongest buyer-intent channel found; owner time is mainly occasional messages.

### Shopify App Store
- EVIDENCE: developers keep 100% of first $1M lifetime revenue, 2.9% processing, $19 one-time registration (shopify.dev revenue-share docs).
- EVIDENCE: first-app review reported at 30+ days and 5–6 weeks in 2026 (community.shopify.dev threads). Earnings follow a power law (adsx, revenuehunt analyses).
- Verdict: review time alone likely pushes a first sale past 27 Dec; merchant support load is high. Deferred.

### Gumroad Discover
- EVIDENCE: 30% fee on Discover sales; sellers report little or no Discover traffic (Indie Hackers post, March 2026, via roo.beehiiv.com). Payout minimum raised to $100.
- Verdict: not a real acquisition channel. Rejected as a channel; usable only as a checkout.

### Google Workspace Marketplace
- EVIDENCE: no marketplace cut (developer write-up); one documented $1.6k MRR Sheets add-on (Indie Hackers); one postmortem of 3k users and $0 revenue (June 2026).
- Verdict: distribution exists, monetisation needs our own billing; Google OAuth verification for sensitive scopes takes time. Candidate for later.

### Fab (Epic)
- EVIDENCE: 88% creator share; Epic reports $24M+ paid to creators in 2025; 420k+ listings and 20k+ publishers (Epic year-in-review); strong demand for RPG frameworks, Blueprint products, procedural systems.
- ASSUMPTION: average ~ $1,200 per publisher per year; power-law distribution.
- Constraint: building/testing Unreal plugins needs Unreal Engine, not available in this cloud environment. Deferred unless owner can run builds.

### Not yet examined
Payhip, Envato/Creative Market, Unity Asset Store, Amazon KDP, Notion/Framer template marketplaces, RapidAPI, Fiverr (owner-identity risk), MCP/agent tool marketplaces.

## Next steps (each operating cycle takes the top unblocked one)
1. Apify: find 3 niches with paid demand (users/30d ≥ 200) and weak incumbents (low rating, stale, few competitors), legally clean sources.
2. Etsy: find a permitted demand-data source; shortlist niches where owner knowledge helps (automotive, clothing design, gaming).
3. Examine 3 more ecosystems from the list above.
4. Pick one experiment by the evidence; write experiments/E2-*.md; ask owner only for the specific setup it needs.
