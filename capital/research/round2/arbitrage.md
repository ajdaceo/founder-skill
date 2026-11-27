
# Market inefficiencies and licensable digital assets: three candidates (27 Nov 2026)

**Read this first.** I used the full budget of 25 searches and could not open pages, so every EVIDENCE item rests on a search-result summary, not a page I read. Most sources are vendor or secondary blogs. I found almost no audited small-operator earnings in this thread; that absence is itself the main finding. None of the three candidates has verified operator earnings at the £10k/month level.

## What has stopped working by late 2026

- **Domain flipping:** negative expected value for hand-registered names.
  - EVIDENCE: sell-through is about 1–2% a year, and at a $12 renewal and 1.5% sell-through the average sale must clear about $800 just to cover renewals (https://domainnamelovers.com/learn/is-domain-investing-worth-it).
  - EVIDENCE: Dynadot's Q2 2026 median sale was $18.87 across 54,000+ sales (https://www.dynadot.com/blog/domain-investing-trends).
- **SEO and affiliate content sites:** small sites are hit hardest.
  - EVIDENCE: a randomised experiment found AI Overviews cut outbound organic clicks 39.8% (https://ppc.land/researchers-find-google-ai-overviews-cut-publisher-clicks-39-8/).
  - EVIDENCE: Chartbeat data shows small publishers lost 60% of search referrals, against 22% for large ones (https://thenextweb.com/news/google-ai-overviews-publisher-links-search-traffic).
  - I found no study isolating affiliate revenue, and no 2026 closed-sale data for content sites.
- **Marketplace scrapers (Apify long tail):** the aggregate is large but the typical seller earns almost nothing.
  - EVIDENCE: Apify advertises $2M paid out monthly (https://apify.com/partners/actor-developers).
  - EVIDENCE: of about 900 actors analysed, 35 cleared $1,000/month and the median among earners was $14 (https://dev.to/nikita_iakovlev_415524c19/i-measured-900-apify-actors-and-got-the-price-wrong-by-100x-heres-the-corrected-data-3418).
  - EVIDENCE: one seller with 20 actors made $6.67 profit in October 2026 (https://dev.to/fade97/three-months-of-selling-scrapers-on-the-apify-store-with-the-real-numbers-5fd0).
- **RapidAPI:** EVIDENCE: provider reviews from March–April 2026 complain of a fee rise from 20% to 25% and late payouts (https://yespress.io/rapid; anecdotal).
- **Open public-data alerts (UK tenders, planning):** already cloned at low prices.
  - EVIDENCE: planning-data tools at £39/month and £49/month sit against Glenigan at thousands a year (https://sitelens.co.uk/compare/glenigan/, https://planwire.io/compare).
  - EVIDENCE: tender alerts from £99/month against Tenders Direct from £1,359/year (https://www.tendersignal.co.uk/tender-alert-software, https://www.tendersdirect.co.uk/pricing/).
- **AI-training licensing for small rights holders:** money goes to large or unique human-origin corpora.
  - EVIDENCE: median deal value fell to $3.6M by Q3 2026, still far above our scale (https://ai-industry-reviews.com/research/ai-training-data-licensing-deal-statistics-2026/).
  - EVIDENCE: Publishers' Licensing Services warned its 350+ opted-in publishers not to expect significant short-term revenue, and only about 20% of TollBit publishers earn meaningfully (https://blankspace.so/blog/do-ai-content-licensing-deals-pay-publishers/).
  - We own no corpus, and synthetic data has no evidenced buyer. I found no pricing for evaluation or benchmark sets.
- **Data marketplaces:** they are checkout rails, not demand.
  - EVIDENCE: Snowflake providers grossed $100M in H1 2026 in aggregate; Datarade's free plan reportedly takes 30% (https://origindatapartners.com/guides/data-marketplaces-compared).
  - I found no small-provider earnings.
- **Not evidenced at all:** UK unclaimed-asset finder models (the search returned nothing on third-party finder fees), exam question banks, translation memories, geodata layers.

---

## Candidate 1: Longitudinal niche data feed (history that cannot be backfilled)

Capture ephemeral public B2B data daily in one vertical (asking prices, stock, auction results) and sell the cleaned history plus a live feed.

1. **Who pays.** ASSUMPTION: dealers, valuers, lenders, insurers and analysts in the chosen vertical; later, funds. EVIDENCE: EquipmentWatch sells resale and auction data to dealers and lenders on 28M+ records (https://equipmentwatch.com/plan-dealers/).
2. **Problem.** ASSUMPTION: they price assets on thin, stale comparables; the source pages disappear, so history exists only for whoever captured it.
3. **Current spend.** EVIDENCE: alternative datasets list at $10k–$200k+ a year, and custom scraping at $10k–$100k a year (https://www.promptcloud.com/blog/top-financial-data-providers/, https://www.clymin.com/resources/alternative-data-providers-comparison-2026). EVIDENCE: raw commodity records cost up to $0.0025 each at Bright Data, so raw scrape is worthless and curation plus history is the product (https://www.fokals.com/blog/alternative-data-pricing-for-hedge-funds).
4. **Frequency.** ASSUMPTION: monthly or annual subscription plus API usage.
5. **Reach without ads.** ASSUMPTION: a free monthly index report per vertical, individually written emails to named trade buyers, and marketplace listings as checkout only.
6. **Price and margin.** ASSUMPTION: £49–£299/month self-serve and £2k–£10k/year for feeds; gross margin above 80% since costs are compute and proxies.
7. **Automation.** ASSUMPTION: collection, scraper repair, cleaning, reports, billing and support can be automated. Contract signature, enterprise calls and legal sign-off cannot.
8. **Hard to replicate.** ASSUMPTION: a clone starting in month 12 lacks 12 months of history, and breadth of sources plus daily maintenance compounds. This is the only candidate where time itself is the moat.
9. **Willingness to pay.**
   - EVIDENCE: Scrape Creators, a solo scraping API, reports over $10k MRR within about a year (https://www.indiehackers.com/post/tech/growing-a-scraping-api-to-10k-mrr-in-12-months-6iF8SJRF4WpciDff9aYi; self-reported).
   - EVIDENCE: SocialKit reports about $2.8k MRR after 13 months (https://www.indiehackers.com/post/tech/side-hustling-for-three-years-before-going-all-in-and-hitting-6-4k-mrr-5kZRj2Lln7jO7nVVoYFP; self-reported).
   - Neither is a longitudinal archive, and EquipmentWatch pricing is unpublished, so the specific thesis is unproven.
10. **Validation (about £15 for a domain, two weeks).** Pick one vertical, capture 14 days, publish a sample index, and contact 40 named buyers. Pass: at least 3 agree to a paid pilot or one prepays £50/month or more. Fail: under 3 substantive replies.
11. **Path.** ASSUMPTION throughout: £100 = 2 self-serve subscribers (months 2–4); £1,000 = 10–15 subscribers (months 6–12); £5,000 = adds 3–5 annual feeds once 12 months of history exists; £10,000 = a second and third vertical on the same pipeline (months 24–36).
12. **Human involvement.** ASSUMPTION: accounts, signing contracts and occasional buyer calls; 2–4 hours a month.

- **Legal and terms.** EVIDENCE (secondary commentary, not legal advice): UK database right can be infringed by extracting a substantial part of a database, site terms are enforceable, and UK GDPR applies to any personal data scraped (https://sule.io/for-startups/answers/web-scraping-uk/, https://thunderbit.com/blog/is-web-scraping-legal-uk-guide). Mitigate by collecting only logged-out, non-personal facts and selling derived indices.
- **Capital at risk.** ASSUMPTION: under £50 a month.
- **Strongest reason it fails.** The archive has no value for 6–12 months, and we may pick a vertical where nobody budgets for data.

## Candidate 2: Buy neglected micro-SaaS or data tools and operate them with AI

1. **Who pays.** The acquired product's existing subscribers; later, a buyer on exit.
2. **Inefficiency.** Small assets trade at a size discount. ASSUMPTION: it persists because a human operator's time is not worth £200/month of profit; an AI operator's is.
3. **Prices and multiples.**
   - EVIDENCE: Acquire.com's median was 3.9x annual profit in 2024 and 2025 (https://blog.acquire.com/acquire-com-biannual-acquisition-multiples-report-jan-2026/, via secondary coverage).
   - EVIDENCE: Flippa's H1 2026 SaaS average is cited as 2.47x, top quartile 4.06x (https://startupa.ge/blog/best-startup-marketplaces-buy-sell-saas).
   - EVIDENCE: deals under $100k are cited at 1.68x by one blog and 3.55x by another; this conflict is unresolved (https://www.acquirecalc.com/industry-multiples/saas-software).
   - EVIDENCE: content sites are cited at 30–38x monthly profit at Motion Invest (https://jeangalea.com/buy-sell-websites/; blog claim).
4. **Frequency.** Subscribers pay monthly; ASSUMPTION: one acquisition every 3–6 months.
5. **Reach.** Buying needs no marketing. ASSUMPTION: growth comes from fixing onboarding and support.
6. **Margin.** EVIDENCE: profitable Acquire.com listings averaged about 71% margins (https://stealwhatworks.com/blogs/news/micro-saas-getting-acquired-now).
7. **Automation.** ASSUMPTION: deal screening, reconciling payment exports, code maintenance, support and onboarding fixes can be automated. Escrow, identity checks, asset transfer and legal signature cannot.
8. **Edge.** ASSUMPTION: a near-zero operating cost lets us pay for assets others cannot run profitably. It is a cost edge, not a moat, and it shrinks as other AI operators bid.
9. **Willingness to pay.** Existing revenue is the evidence, and EVIDENCE: TrustMRR lists about 13,000 startups with payment-provider-verified revenue (https://crawlora.net/datasets/trustmrr). Flip anecdotes exist: bought for $10k, resold for $20k; bought for $3,800, reached $1,200/month (https://wifimoolah.com/p/idea-60-3969, https://www.buildmvpfast.com/blog/buy-micro-saas-grow-acquisition-playbook-2026). These are survivorship-heavy; I found no failure-rate data.
10. **Validation.** Capital is intrinsic: ASSUMPTION minimum £3k–£5k for one asset earning £100–£200/month. A free pre-test: screen verified listings for two weeks. Pass: at least 5 with 12+ months of verified revenue, monthly churn under 5%, asking under 2.5x profit, and a fix we can name. Fail: fewer than 5.
11. **Path.** ARITHMETIC on the cited multiples: £100/month costs about £2k–£4.7k. Buying £10k/month outright would cost about £200k–£470k, so the path depends on improving each asset and reinvesting. ASSUMPTION: £1,000 by months 12–18, £5,000 by year 3, £10,000 only with outside capital or a standout asset.
12. **Human involvement.** The highest of the three: every purchase needs the owner for payment, legal and transfers. ASSUMPTION: 5–10 hours per deal.

- **Legal and terms.** Misrepresented revenue, transfer of customer data under UK GDPR, and inherited platform dependencies.
- **Capital at risk.** The full purchase price.
- **Strongest reason it fails.** EVIDENCE: buyers already discount thin AI wrappers by up to 1.5x and treat high churn as a red flag (https://www.appsonbid.com/blog/micro-saas-valuation-multiples-2026). Cheap assets may be cheap because they are being cloned, the lesson we already learned.

## Candidate 3: Capped-seat sourcing-signal list for Amazon resellers (sell the signal, not the trade)

1. **Who pays.** Online-arbitrage sellers.
2. **Problem.** Finding profitable retail-to-Amazon price gaps daily is laborious, and a gap dies when too many sellers see it, hence the seat caps.
3. **Market prices.** EVIDENCE, all vendor-listed:
   - $75/month, capped at 25 sellers (https://amazonadventure.gumroad.com/l/qVJyw).
   - $129/month (https://theamazonsister.gumroad.com/l/leadlist).
   - $118–$298/month (https://www.webretailer.com/reviews/oabeans/).
   - $349/month, capped at 22 sellers (https://central.newschannelnebraska.com/story/53298112/online-arbitrage-lead-sourcing-service-for-scaling-amazon-resellers-announced).
   - $600/month for a bespoke list (https://sentrigroup.gumroad.com/l/bespoke-buy-list-amazon-walmart-online-arbitrage-leads).
   - Self-serve software: Tactical Arbitrage from $69/month (https://revenuegeeks.com/software/tactical-arbitrage).
4. **Frequency.** Monthly subscription, daily delivery.
5. **Reach.** ASSUMPTION: a public, timestamped track record of past leads, and seller communities where promotion is permitted.
6. **Price and margin.** ARITHMETIC: 25 seats at $129 is $3,225/month per list. ASSUMPTION: 70%+ margin after data costs.
7. **Automation.** ASSUMPTION: price comparison, fee and profit calculation, and delivery can be automated. Judging brand-gating and IP-complaint risk is partly automatable. Trust-building is not.
8. **Hard to replicate.** Weak. ASSUMPTION: the seat cap fragments the market so many small lists coexist, and each additional list is a new revenue unit; a verifiable track record takes months.
9. **Willingness to pay.** Eight or more vendors publish prices, some for years. I found no verified revenue for any of them, and one reviewer noted low-quality leads (https://webretailer.com/reviews/leadgeek).
10. **Validation (under £50, two weeks).** Run a free 10-seat beta list. Pass: at least 10 sign-ups, at least 3 convert at £49/month or more, and at least 60% of leads still profitable at 72 hours on our own check. Fail: under 3 conversions.
11. **Path.** ASSUMPTION: £100 = 2–3 seats; £1,000 = one 20-seat list at about £60; £5,000 = three or four category lists; £10,000 = six to eight lists or premium bespoke tiers.
12. **Human involvement.** ASSUMPTION: accounts, payments and dispute handling; 2–3 hours a month.

- **Legal and terms.** Unverified and potentially fatal: I found nothing on whether Keepa's or Amazon's terms permit reselling derived data, and retailer site terms apply. Check before spending anything.
- **Capital at risk.** ASSUMPTION: under £100 a month in data access.
- **Strongest reason it fails.** Software at $69/month already automates the search (and EVIDENCE: SourceMogul is reported shut down, https://arbitragehero.com/blog/sourcemogul-alternative/), so the list's premium may be a legacy of human curation that an AI-run list cannot credibly claim.

---

## Ranking

Candidate 1 is the strongest. It is the only one whose advantage grows with daily operation rather than build speed, it needs almost no capital, and buyers demonstrably pay five figures for curated data. Its weakness is slow, unproven early revenue and scraping-law exposure. Candidate 2 has the clearest cash flow from day one and uses an AI operator's cost advantage, but it needs £3k–£5k minimum, the most owner time, and realistically stalls below £10k/month without more capital; the sub-$100k multiple is disputed (1.68x versus 3.55x). Candidate 3 has the best-documented price points and the fastest test, but the weakest defensibility and an unresolved terms-of-service question that could kill it outright. I would not pursue domains, SEO or affiliate sites, a marketplace scraper portfolio, or AI-training licensing as a primary business on this evidence.
