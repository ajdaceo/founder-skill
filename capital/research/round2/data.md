## Headline

Most of the niches named in the brief are already cloned, and I found three candidates that survive, none of them validated. All evidence comes from search-result snippets (page fetching was blocked), so every price below needs confirming on the vendor's own page. I used all 25 searches.

## What this research killed

Each of these showed several cheap, recent entrants in a single search.

| Niche | What is already there (EVIDENCE) |
|---|---|
| UK planning-application leads | 8+ services at £9–£149/mo, e.g. Planning Pipe from £44.95/mo (https://planningpipe.co.uk/products/), PatchList from £9/mo (https://thepatchlist.com/), Tradecue £29.99/mo (https://tradecue.co.uk/) |
| UK tender alerts | Many AI entrants (https://bidskim.com/compare, https://cleantender.co.uk/alternatives/tracker-intelligence, https://jorpex.com/compare/tender-monitoring-tools/); Stotles has a free tier (https://www.capterra.com/p/235578/Stotles/pricing/) |
| HGV operator-licence feeds | HaulierScope at £19–£129/mo (https://www.saasworthy.com/product/haulierscope); Apify scrapers at $5 per 1,000 records (https://apify.com/dthen/uk-fleet-leads-dvsa) |
| New food-business and hospitality leads | FoodLeads at £9/mo (https://www.foodleads.co.uk/); Apify actors at $3–5 per 1,000 (https://apify.com/ukdatakit/uk-food-business-leads) |
| Premises-licence registers | Plota claims 267 councils' registers, free search and alerts (https://plota.co.uk/updates/licensing) |
| Vet price comparison (CMA order 2026) | At least 6 consumer sites live before the December 2026 deadline (https://comparevetpricing.co.uk/, https://clearvet.co.uk/price-index, https://pawlee.uk/); the RCVS will also share data with comparison sites (https://www.gov.uk/government/news/cma-concludes-market-investigation-with-major-reforms-to-veterinary-sector) |
| Council-meeting monitoring | GovChat at £55–£120/mo (https://www.govchat.co.uk/), CivicPulse (https://www.civicpulse.uk/); in Germany, Poliscope (https://poliscope.de/ratsinformationssystem/amberg/093610000) |
| Property-licensing monitoring | Kamma at 30p per property per month, £65 minimum (https://www.kerfuffle.com/suppliers/kamma) |
| Self-storage rate tracking | StorTrack UK at £45/mo (https://optimize.stortrack.co.uk/) |

The pattern: any single public register or API is commoditised within months. The survivors need one of three things:
- **Time:** data that takes months to accumulate (FOI responses, history).
- **Extraction depth:** values buried in documents and matched across languages, not just notice feeds.
- **High-value verticals:** quote-only enterprise incumbents and no SME tier.

---

## Candidate 1: Public-sector install-base and contract-renewal data for one software category at a time

Built from FOI disclosure logs, existing FOI responses and our own FOI requests, for SME govtech and health-tech vendors.

1. **Who pays.** Sales and bid leads at SME software or services vendors selling one category to NHS trusts and councils, plus boutique consultancies. (ASSUMPTION on the exact buyer title.)
2. **Problem.** They need to know which body uses which supplier, at what annual cost, and when the contract ends. Published notices are incomplete.
   - EVIDENCE: one tracker notes 11 award notices in a single category published no end date (https://contractsdue.co.uk/categories/48170000-compliance-software-package).
   - EVIDENCE: public bodies' disclosure logs carry this as one-off FOI answers with supplier, start and end date and extension columns, scattered across hundreds of sites (https://foi.ghc.nhs.uk/responses/technology-contracts/, https://resolution.nhs.uk/wp-content/uploads/2024/12/FOI_6851_Procurement-and-contracts.pdf, https://www.nss.nhs.scot/publications/foi-2026-3237-contract-values-and-startend-dates/foi-2026-3237-contract-values-and-startend-dates-html/).
3. **Current spend.**
   - EVIDENCE (second-hand, from a competitor's page): Tussell is cited at £11,400 per licence per year on G-Cloud 14 (https://bidskim.com/alternatives/tussell).
   - EVIDENCE: Stotles Basic is £50 per user per month and Growth £475/mo, with a free tier (https://www.capterra.com/p/235578/Stotles/pricing/).
   - EVIDENCE: Future Health Intelligence sells NHS supplier profiles with install counts; price not found (https://futurehealthintelligence.com/fhi-supplier-profiles/).
   - EVIDENCE: Tracker is estimated at about £5,100/yr and Tenders Direct from about £1,359/yr (https://frntir.ai/guides/tender-alert-services-uk).
4. **Frequency.** Continuous: contracts expire every month. EVIDENCE: 9,416 published IT contracts end in the 12 months to September 2027 (https://www.servnetuk.com/research/uk-public-sector-it-contract-expiry-2026).
5. **Reach without ads.**
   - Publish a free league table per category ("who supplies X to every English council"), which trade press and LinkedIn can pick up. (ASSUMPTION that they will.)
   - Email named vendors in that category. EVIDENCE: under PECR, limited companies and LLPs can be emailed without consent, but sole traders and ordinary partnerships cannot; keep an opt-out list, and UK GDPR still applies to named employee addresses (https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/).
   - Keep it to UK recipients. (ASSUMPTION: several EU states are stricter on B2B email.)
6. **Price.** £149–£299/mo per category dataset with monthly refresh and renewal alerts, or a £400–£900 one-off snapshot. (ASSUMPTION, set between Stotles and Tussell.)
7. **Automation.**
   - Automated: crawling disclosure logs, parsing PDF, Excel and email responses, resolving supplier and product names, drafting and tracking FOI requests, chasing late replies, internal reviews.
   - Not automated: the owner's legal identity on requests and Pro account; judgement on refusals; any buyer who wants a call.
8. **Why hard to replicate.** Each FOI round takes 20 working days or more per body, so a multi-year, multi-category history with normalised names cannot be scraped in a weekend. Coverage and history compound. (ASSUMPTION, but it follows from the statutory timescale.)
9. **Willingness to pay.** Incumbent prices above. The disclosure logs themselves show a steady stream of contract, system and end-date requests; that these come from suppliers doing this by hand is my ASSUMPTION.
10. **Validation (under £50, two weeks).**
    - Pick one category that Future Health Intelligence does not profile, e.g. a council back-office system.
    - Build a 60-body sample from existing disclosure logs only, with no new FOIs.
    - Email 40 vendors in that category (limited companies) offering the full dataset at £400.
    - Pass: 2 or more paid pre-orders, or 5 or more replies asking for price or a sample. Fail: fewer than 3 replies.
11. **Path (ASSUMPTION throughout).**
    - £100: one snapshot sale.
    - £1,000: 6 subscribers at about £180 across 2 categories.
    - £5,000: 25–30 subscribers across 8–10 categories.
    - £10,000: 50–55 subscribers across about 20 categories, plus one-off reports. Needs low churn, and a category only holds 20–100 vendors.
12. **Human involvement.** About 1–2 hours a week: account identity, the occasional refusal dispute, payment admin.

**Legal and licensing.**
- EVIDENCE: commercial use of WhatDoTheyKnow needs a Pro subscription (https://www.whatdotheyknow.com/pro/pages/legal).
- EVIDENCE: some bodies attach "no commercial re-use without permission" conditions to responses (https://www.whatdotheyknow.com/cy/request/176126/response/438863/attach/html/3/FOI%20Conditions%20of%20Use.pdf.html). Selling extracted facts rather than the documents lowers but does not remove this; it needs a per-body check under the re-use regulations. (ASSUMPTION.)
- EVIDENCE: commercially motivated and round-robin requests are not automatically vexatious, but burden counts (https://ico.org.uk/for-organisations/foi/learning-resources-and-training-videos/refusing-commercially-motivated-requests-as-vexatious/). Requests must stay narrow and infrequent per body.
- GDPR exposure is low, since this is contract data; strip officer names.

**Strongest reason it fails.** Stotles' free and £50 tiers plus Future Health Intelligence may be good enough, and each category's buyer pool is small. There is also a reputational cost to loading public bodies with FOIs.

**Neglected segment.** Vendors with 5–50 staff in unglamorous categories and smaller bodies (district councils, housing associations, fire services, universities) who cannot justify five-figure licences.

---

## Candidate 2: EU hospital tender award and unit-price intelligence for SME medtech, one product family at a time

1. **Who pays.** Export and tender managers at SME medical-device manufacturers and national distributors. (ASSUMPTION.)
2. **Problem.** They price bids blind: award prices sit in national portals, in local languages, inside award PDFs and lot tables. Enterprise tools exist but are sold to large life-science firms. EVIDENCE: Cube RM sells win-price modelling (https://www.cuberm.com/tender-pricing-guidance/); Vamstar sells hospital-level award data going back to 2019 (https://vamstar.io/frequently-asked-questions/).
3. **Current spend.** Both incumbents are quote-only: Vamstar is a modular annual subscription priced by number of markets (same URL), and Cube RM is tiered by users (https://www.gartner.com/reviews/product/cube-rm-tender-central). I found no figures; five figures a year is my ASSUMPTION.
4. **Frequency.** Every bid; weekly to monthly for an active tenderer. (ASSUMPTION.)
5. **Reach.**
   - Free monthly "awarded price index" for one product family, in English plus the local language, posted on LinkedIn and offered to trade associations.
   - Inbound search for "[product] tender prices [country]".
   - Cold email only where lawful; start with UK limited companies under the ICO rule above. (ASSUMPTION: Germany and others need opt-in.)
6. **Price.** £199–£499/mo per product family across 5 or more countries, or £500–£1,500 per bid benchmark report. (ASSUMPTION.)
7. **Automation.** Automated: daily collection, translation, lot and line-item extraction, product matching, price normalisation per unit. Not automated: clinical-equivalence disputes on product matching (needs sampling QA), enterprise-style sales conversations.
8. **Why hard to replicate.**
   - Raw notices are a commodity. EVIDENCE: 8 Apify scrapers exist for Spain's portal alone (https://apify.com/tenderfeed/spain-placsp-tenders).
   - The moat is line-item extraction and a cross-language product ontology with years of price history. (ASSUMPTION that this is deep enough.)
9. **Willingness to pay.** Indirect only: two funded incumbents selling exactly this to large firms. I found no SME-priced competitor, which is not proof of demand.
10. **Validation.** Build one product family across Spain, Italy and Portugal for the last 24 months. Offer the report at £300 to 40 SME makers or distributors. Pass: 2 sales or 6 qualified replies. Fail: under 3 replies, or extraction accuracy below 90% on a 100-row hand check.
11. **Path (ASSUMPTION).** £100: one report. £1,000: 4 subscribers at £250. £5,000: 17–20 subscribers across 5 families. £10,000: 30–35 subscribers plus reports.
12. **Human involvement.** About 2–3 hours a week early on, mostly sales calls and QA sign-off. This is the heaviest human load of the three.

**Legal and licensing.**
- EVIDENCE (vendor-reported): Spanish portal data is reusable commercially with attribution under Law 37/2007 (https://apify.com/icarodata/placsp-licitaciones); the official manual is at https://contrataciondelestado.es/datosabiertos/DGPE_PLACSP_OpenPLACSP_v.1.1.1.pdf.
- Italy's and Portugal's terms were not verified; check each portal's licence and database-right position.
- GDPR exposure is low; exclude sole-trader bidders.

**Strongest reason it fails.** Medtech SMEs buy through relationships and distributors, sales cycles are long, and an AI-run vendor with no domain reputation may not be trusted on price data.

**Neglected segment.** Manufacturers and distributors under roughly €50m revenue bidding in 2–6 countries.

---

## Candidate 3: Asian regulatory-change monitoring for SME cosmetics and food-supplement exporters

1. **Who pays.** Regulatory or export leads at small brands and contract manufacturers selling into China, Korea, Japan and ASEAN. (ASSUMPTION.)
2. **Problem.** Rules change in local-language gazettes; a missed change means blocked shipments or relabelling. (ASSUMPTION on cost.)
3. **Current spend.** EVIDENCE: ChemLinked cosmetics membership is USD 1,799/yr for one user and USD 4,999/yr corporate for up to 20 users, sold per portal, so food is a separate subscription (https://cosmetic.chemlinked.com/membership, https://food.chemlinked.com/qa).
4. **Frequency.** Weekly changes across markets. (ASSUMPTION.)
5. **Reach.** Free weekly digest; searchable pages per ingredient and country; LinkedIn; trade-association newsletters. Opt-in email only for sole traders.
6. **Price.** £39–£99/mo for a personalised watchlist (their ingredients, their markets), against about £120/mo-equivalent at the incumbent. (ASSUMPTION.)
7. **Automation.** Automated: monitoring primary government sources, translation, change detection, mapping changes to each customer's ingredient list. Not automated: accountability for interpretation; it must be framed as monitoring, not legal advice, with source links.
8. **Why hard to replicate.** An ingredient-by-country rule history and customers' own watchlists create switching costs. (ASSUMPTION.) Translation alone is no moat.
9. **Willingness to pay.** The incumbent's published prices and multi-portal business; I found no customer counts.
10. **Validation.** Run four weeks of a free China and Korea cosmetics digest with a £49/mo personalised-watchlist checkout. Pass: 100 sign-ups and 3 paid. Fail: under 30 sign-ups or zero paid.
11. **Path (ASSUMPTION).** £100: 2 subscribers. £1,000: about 17 at £60. £5,000: about 80. £10,000: about 150, or fewer with a £199 team tier.
12. **Human involvement.** About 1 hour a week, plus owning the liability terms.

**Legal and licensing.** Government texts are generally reusable, but do not translate or republish competitors' or news articles (copyright). Carry professional-indemnity-style disclaimers. GDPR exposure is minimal.

**Strongest reason it fails.** The incumbent is backed by a body of free news, and buyers want a named expert to blame; an error here does real harm to a customer.

**Neglected segment.** Indie brands and small exporters needing one or two markets and one seat, for whom USD 1,799 per portal is too much.

---

## Ranking

1. **Candidate 1 is strongest.** Its moat is statutory time delay plus normalisation labour, the raw material is demonstrably public yet scattered, incumbent prices are visible, and the validation costs nothing. Its ceiling is limited by small buyer pools per category, and it carries legal and reputational friction around commercial FOI use.
2. **Candidate 2 has the highest value per customer** and the most real data-engineering moat, but the weakest evidence: no incumbent price and no SME demand signal. It also needs the most human selling, which conflicts with the owner's low-involvement constraint.
3. **Candidate 3 has the cleanest pricing evidence and self-serve model** but the thinnest moat and real liability risk.

None of the three has demonstrated demand at our price point. I would run Candidate 1's test first and treat a fail as a genuine stop, given how saturated everything adjacent proved to be.