
# What business models work when the operator is an AI: evidence report (27 Nov 2026)

**Bottom line:** I found no documented case of an AI-operated business that is profitable without either human attention-capital or a subsidy. The evidence supports three shapes for our situation, in this order: (1) a compounding niche data/intelligence subscription sold B2B, (2) a contingency or outcome-priced recovery service, (3) a human-fronted productised back-office service. All three rest partly on negative evidence (what fails) rather than verified positive cases.

**Method limits you should weigh before relying on this:**
- I used 25 web searches and could not open pages. Every EVIDENCE item below comes from search-result summaries, not from reading the source in full.
- URLs are as returned by search. Figures marked "secondary" were reported by aggregators or blogs and need checking against the primary before anything is built on them.
- Several searches returned nothing useful (Stripe and Etsy AI policies, niche data-subscription case studies, solo recovery-service revenue). Those gaps are stated, not filled.

---

## A. Documented cases of AI-run or AI-heavy businesses

### Autonomous-agent experiments (best documented, mostly losses)

| Case | What happened | Source quality |
|---|---|---|
| Anthropic Project Vend, phase 1 (2025) | Claude-run office shop; balance fell from about $1,000 to just under $800 in roughly a month | Primary write-up, numbers via secondary summary |
| Project Vend, phase 2 (Dec 2025) | Newer models, more agents (a "CEO" agent, a merch agent), new locations; negative-margin weeks "largely eliminated" | Primary write-up; Andon Labs staff still did physical restocking |
| WSJ newsroom vending machine (Dec 2025) | Reporters manipulated the agent into giving stock away and buying a PlayStation 5; ended in the red | Secondary reports of WSJ piece; loss given as "hundreds" to "more than $1,000" |
| Andon Market, San Francisco (2026) | Agent "Luna" given $100,000 and a $7,500/month lease; still losing money months in | Bloomberg/Entrepreneur via summaries |
| Firmulate (2026) | "13 AI employees" software company; €105,000 monthly burn against about €2,300 recurring revenue | Single source, rewritten by content farms; unverified |

- EVIDENCE: Project Vend phase 1 loss and phase 2 improvement. https://www.anthropic.com/research/project-vend-1 and https://www.anthropic.com/news/project-vend-2
- EVIDENCE: WSJ test. The manipulation used fake documents and long persuasion chains (one reporter used 140+ messages); a supervising agent added in a later version was also talked into making everything free. https://boingboing.net/2025/12/18/ai-vending-machine-lost-1000-to-social-engineering.html and https://www.tovima.com/wsj/we-let-ai-run-our-office-vending-machine-it-lost-hundreds-of-dollars/
- EVIDENCE: Andon Market was about $13,000 in the red in April 2026 and needed around $500/day to break even. https://www.bloomberg.com/news/articles/2026-04-23/an-ai-agent-takes-over-a-store-and-orders-too-many-candles-mobwrfw2
- EVIDENCE (date unconfirmed): a later report put it $62,000 down. https://www.entrepreneur.com/business-news/an-ai-bot-ran-a-san-francisco-store-for-the-first-time
- EVIDENCE: a September 2026 visit found "no one in it and nothing useful to sell"; a co-founder reportedly said the agent lacks a founder's survival instinct. https://slashdot.org/story/26/09/13/0523208/a-visit-to-san-franciscos-ai-run-store-no-customers-nothing-useful-and-losing-money-fast
- EVIDENCE (weak): Firmulate figures. https://cornfordandcross.com/biotech-experimental-art/firmulate-live-company/

### "Zero-human company" revenue claims (self-reported, attention-driven)

- **Felix (Nat Eliason's OpenClaw agent).** EVIDENCE (secondary, traced to the founder's own posts): about $195,000 by early March 2026, of which $100,570 via Stripe and the rest in ETH. https://openclaw.report/use-cases/felix-zero-human-company
  - Critics note it mainly sells products about its own setup, and revenue tracks the founder's personal reach. https://vicelabs.ai/blog/the-real-economics-of-running-a-company-on-ai-agents
  - This is a personal-brand business with an agent as the hook. It does not transfer to an operator with no audience.
- **Polsia (platform that runs "autonomous companies").** EVIDENCE: headline ARR of "approaching $10M" and later $18.71M is company-reported and disputed. Critics say it annualises one-off credits and counts customers' ad spend passed through; the founder reportedly declined to show Stripe. https://preuve.ai/blog/polsia-review and https://aiolum.com/story/polsia/
  - EVIDENCE (secondary): 29,132 active companies out of 484,592 created as of 15 Sep 2026, about 6% survival. https://aiolum.com/story/polsia/
  - The money is in selling the tooling to hopefuls; I found no verified profit for any company it runs.
- **Base44.** EVIDENCE (verified acquisition price): Wix paid $80M cash for a six-month-old "solo-owned" company, which had eight employees at sale. https://techcrunch.com/2025/06/18/6-month-old-solo-owned-vibe-coder-base44-sells-to-wix-for-80m-cash
  - Its profit figure ($189k in one month) is the founder's own claim. https://analyticsindiamag.com/ai-news-updates/a-single-owner-bootstrapped-ai-startup-gets-acquired-for-80-million
  - This was a human-founder software company in a hot category, not an AI-operated business.

### What the cases show

Failure modes with evidence: social-engineering by customers, discounting and giveaways, poor purchasing, hallucinated commitments, and no urgency when losing money. The only large revenue figures are founder-reported and depend on human fame.

---

## B. Which small-operator models show verified economics

### The base rate for quick-to-build software is poor

- EVIDENCE (the marketplace's own stats page, snapshot date unclear): on TrustMRR, a payment-verified revenue index, 68.5% of listed startups sit at $0–$1k, 16.7% at $1k–$10k, 10.0% at $10k–$100k. https://trustmrr.com/stats
- EVIDENCE (vendor analysis of that dataset): among 3,787 revenue-earning indie software businesses, median monthly recurring revenue was $145; 75th percentile $894; 90th percentile $5,107; 6.1% reached $10k. https://bigideasdb.com/state-of-indie-saas-revenue-2026
- EVIDENCE (same vendor): newer cohorts do worse. Median $259 for the 2024 class, $193 for 2025, $80 for 2026; share reaching $10k was 8.3%, 6.1%, 2.7%. Age explains part of this, but it fits the cloning problem you already hit. https://bigideasdb.com/saas-trends-2027
- EVIDENCE (third-party analysis of 60 startups): the high-growth tier is dominated by B2B outbound and sales tooling. https://dev.to/storeintel/we-analyzed-60-stripe-verified-saas-startups-on-trustmrr-tech-stacks-mrr-vs-one-time-sales--54h7
- Caveat: the dataset is self-selected, has stale entries, and has no solo-founder field. https://crawlora.net/datasets/trustmrr

### Sale multiples

- EVIDENCE (Acquire.com's own report): confirmed 2025 deals closed at 3.7x net income under $100k and 3.9x for $100k–$1M, with a median 90 days on market. https://blog.acquire.com/wp-content/uploads/2026/02/Acquire-Multiples-Report-2025.pdf
- EVIDENCE (Flippa H1 2026): content-site sales fell 39%; ecommerce averaged a 1.55x profit multiple. https://flippa.com/blog/digital-ma-insights-h1-2026/
- So content sites are a shrinking asset class, and recurring-revenue businesses fetch more than twice the ecommerce multiple.

### Newsletters

- EVIDENCE (beehiiv's own reports, via secondary summaries): paid subscription revenue on the platform was $19M in 2025 against $8M in 2024; median time to first dollar for 2025 launches was 66 days; median paid conversion 0.62%. https://www.beehiiv.com/blog/the-state-of-newsletters-2026 and https://www.beehiiv.com/blog/the-state-of-paid-newsletters-2026
- ASSUMPTION: at 0.62% conversion, a £1k/month paid newsletter needs thousands of free subscribers unless it is priced as a B2B tool (£30–£100+/month) for a narrow audience. I found no B2B-specific earnings distribution.

### Where evidence is thin

- **Niche data/intelligence subscriptions, lead-gen sites, directories:** no verified dataset or case study found. The search returned only listicles.
- **Contingency/recovery services:** only pricing norms, no small-operator revenue. EVIDENCE (vendor-adjacent): classic recovery audits charge 15–25% of recovered money. https://cloudsquid.io/blog/recovery-audit-redundant-what-replaces-it/
- **Outcome-priced AI services:** investor playbooks argue for them but advise starting with the market's normal pricing; this is opinion, not data. https://www.emcap.com/thoughts/the-ai-native-services-playbook

---

## C. Channel reality, late 2026

**Search still works for buying-intent queries; it is badly damaged for informational ones.**
- EVIDENCE: Pew (July 2025, 68,879 searches) found users clicked a traditional result 8% of the time with an AI summary present against 15% without. Ahrefs (Feb 2026) found position-one click-through 58% lower with an AI summary. Both via https://driven-metrics.com/blog/ai-overview-click-through-rate/
- EVIDENCE (Seer Interactive via secondary): AI summaries appeared on 36% of informational queries but 5% of transactional ones. https://www.cognizo.ai/blog/google-ai-overviews-statistics
- EVIDENCE (secondary): 68% of US Google searches ended without a click in Jan–Apr 2026, up from 60% in 2024. https://www.omnibound.ai/blog/ai-seo-statistics

**Mass-generated pages are an enforcement target.**
- EVIDENCE: Google ran spam updates in June, August and September 2026 with scaled content abuse in scope; one case study involved a site with 1.5M indexed URLs. https://gsqi.com/marketing-blog/august-2026-google-spam-update-case-studies/
- EVIDENCE (SEO commentary): the common thread is scale with little unique value, and programmatic pages are not banned as such. https://seosherpa.com/programmatic-seo/
- ASSUMPTION: pages built on proprietary data the site itself produces are the defensible version.

**Cold email is legal to UK companies but its yield is falling.**
- EVIDENCE (vendor benchmarks, differing denominators): average reply rate 3.43% in 2026, down from 5.1% in 2024. https://www.lemlist.com/blog/cold-email-benchmarks
- EVIDENCE (Hunter data via secondary): sequences to 21–50 recipients averaged 6.2% replies; 500+ averaged 2.4%. https://www.blazehive.io/statistics/cold-email-statistics/
- EVIDENCE (vendor): Gmail now rejects non-compliant bulk mail outright, with a 0.1% complaint threshold. https://dupple.com/learn/cold-email-deliverability-2026
- EVIDENCE (ICO primary): the email marketing rule does not apply to corporate subscribers (companies, LLPs), so B2B email to them is allowed without consent. Sole traders and ordinary partnerships are treated as individuals and need consent or soft opt-in. https://ico.org.uk/for-organisations/direct-marketing-and-privacy-and-electronic-communications/business-to-business-marketing/
- The ICO guidance is under review after the Data (Use and Access) Act. ASSUMPTION (not confirmed by search): maximum fines for breaching these rules rose to £17.5m or 4% of turnover.
- ASSUMPTION: EU countries are generally stricter than the UK and the US is more permissive; I did not search this.

**LinkedIn automation is prohibited and enforced.**
- EVIDENCE (LinkedIn primary): accounts using prohibited software risk restriction or shutdown. https://www.linkedin.com/help/linkedin/answer/a1341387
- EVIDENCE: LinkedIn is suing scraping providers. https://news.bloomberglaw.com/artificial-intelligence/linkedins-war-against-bot-scrapers-ramps-up-as-ai-gets-smarter
- The claim that about 40% of accounts on non-compliant tools were restricted in Q1 2026 is a marketing-blog figure and unverified.

**Freelance marketplaces bar unattended agents.**
- EVIDENCE (secondary blogs, not the terms themselves): Upwork permits AI-drafted proposals with human review but prohibits fully automated submission. https://getmany.com/blog/upwork-ai-policy

**Not evidenced either way:** communities, partnerships, PR and directories as channels.

**Stopped working:** informational content sites, mass AI page generation, high-volume generic cold email, automated LinkedIn outreach.

---

## D. Structural constraints

**The owner is liable for everything the agent does.**
- EVIDENCE (CMA primary, 9 March 2026): businesses are responsible for their AI agents as they are for employees, even when a third party supplies the agent. They should tell customers when an AI agent is in use, not overstate its abilities, test before deployment and keep human oversight. https://www.gov.uk/government/publications/complying-with-consumer-law-when-using-ai-agents/complying-with-consumer-law-when-using-ai-agents
- EVIDENCE (law-firm summary): fines can reach 10% of global turnover. https://www.taylorwessing.com/en/insights-and-events/insights/2026/03/aq-ai-agents-cma-publishes-guidance-on-complying-with-consumer-law
- EVIDENCE: the UK Jurisdiction Taskforce's July 2026 legal statement says liability attaches to legal persons, not the AI, and a business that holds out a chatbot as speaking for it is generally liable for its statements. https://www.hsfkramer.com/notes/litigation/2026-07/uk-jurisdiction-taskforce-publishes-final-legal-statement-on-liability-for-ai-harms
- ASSUMPTION (general law, not from search): the contracting party must be the owner or a limited company. A limited company caps personal exposure, and B2B-only selling avoids most consumer-law burden.

**Data protection registration.**
- EVIDENCE: the ICO fee is £52 for the smallest tier since 17 Feb 2025, payable by controllers unless exempt. https://ico.org.uk/for-organisations/advice-for-small-organisations/whats-new/blogs/data-protection-fee-what-you-need-to-do/

**Buyers want a human to exist.**
- EVIDENCE (Gartner primary press releases): 87% of customers say companies using generative AI for service must provide access to a human. https://www.gartner.com/en/newsroom/press-releases/2026-08-04-gartner-survey-finds-87-percent-of-customers-say-companies-using-genai-for-customer-service-must-provide-access-to-a-human-agent0
- EVIDENCE: 69% of B2B buyers validate AI-generated insight with a sales rep, although 67% prefer a rep-free purchase. https://www.gartner.com/en/newsroom/press-releases/2026-05-20-gartner-survey-finds-sixty-nine-percent-of-b-two-b-buyers-turn-to-sales-reps-to-validate-ai-generated-insights and https://www.gartner.com/en/newsroom/press-releases/2026-03-09-gartner-sales-survey-finds-67-percent-of-b2b-buyers-prefer-a-rep-free-experience
- Reading: self-serve purchase is acceptable, but there must be a named human escalation path and verifiable output.

**Gaps:** I found nothing on Stripe's or Etsy's rules for agent-operated merchants. The owner should assume identity checks and account liability sit with them personally (ASSUMPTION). I found no documented practice of how successful operators handle disclosure; the CMA guidance is the best available standard.

---

## E. Selection principles and recommended shapes

### Five principles

1. **Never give the agent discretion over price, refunds or commitments in open conversation.** Every documented agent business that let customers negotiate lost money to manipulation. Use fixed prices and rule-based fulfilment.
2. **Sell something that gets harder to copy each day it runs.** Quick software has a median of about $145/month and newer cohorts are worse. A daily-accumulated, cleaned, historical dataset cannot be cloned in a weekend. The link from this to revenue is ASSUMPTION; the base rate is evidence.
3. **Target buying-intent demand and companies, not informational traffic or consumers.** AI summaries hit informational queries about seven times as often as transactional ones, content-site sales fell 39%, and UK rules allow email to companies but not sole traders.
4. **Acquire customers with low-volume, evidence-backed outreach.** Small targeted sequences get roughly 2.5 times the reply rate of large ones, bulk sending is now rejected, and LinkedIn automation risks the account. The agent's edge is research depth per prospect, not volume.
5. **Put a human and a legal entity visibly behind it, disclose AI use, and stay out of regulated advice.** Liability lands on the owner regardless, and most buyers demand a human route.

### Three shapes the evidence most supports

| Shape | Example niche | Why it fits | Main risk |
|---|---|---|---|
| 1. Compounding niche intelligence subscription (B2B alerts plus a historical database from public sources) | Daily monitoring of UK local-authority planning or licensing decisions, or sub-threshold public tenders, for one trade vertical; sold at £30–£150/month to limited companies | Value accumulates daily; fixed price; verifiable output; buying-intent search terms; each record can be a unique page | No verified small-operator case found; incumbents exist in tenders; zero-budget distribution is the bottleneck; scraping terms and data licensing |
| 2. Contingency or outcome-priced recovery/audit service | Auditing small firms' freight or carrier invoices, software subscriptions, or marketplace seller reimbursements for a share of money recovered (norm is 15–25%) | No upfront trust needed; outcome is measurable; document processing at scale is the agent's strength | No small-operator revenue evidence found; needs access to client data and accounts (trust and security); long payment cycles; hallucinated findings create liability; some recovery fields are regulated or crowded |
| 3. Human-fronted productised back-office service at a fixed price | Monthly compliance or document pack for one vertical, for example supplier-certificate and insurance-expiry tracking for small construction subcontractors | Matches buyer preference for self-serve purchase with human validation; fixed scope prevents manipulation | Evidence is thinnest here (investor opinion only); owner time creeps up; easiest of the three to clone unless paired with shape 1's data |

**Not supported by the evidence:** content sites, generic directories, mass programmatic pages, consumer retail, anything on freelance marketplaces, and a paid newsletter without an existing audience.

**The largest unknown:** whether any zero-budget channel can get the first ten B2B customers without a human face. Nothing I found demonstrates it, so that is the first thing to test cheaply before building.
