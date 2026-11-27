# Reassessment after owner challenge on anchoring (2026-11-27 22:00 UK)

## Verdict on E2 (Etsy spreadsheets)
- Would it have been chosen without knowledge of the owner's interests? No.
  - Vehicle tracker: anchored on owner interests (operator wrote "where owner knowledge helps").
  - Etsy: chosen mainly because it was easy to reach and has traffic; marketplace traffic is not product demand.
  - Reseller tracker: one real demand signal (HMRC platform reporting), but crowded and low value (£9).
- Status: E2 demoted to "preserved asset". Not the selected experiment. Etsy setup requests are on hold.

## Screening rules from now on
- Rank by: evidenced spend by identifiable buyers; value per sale (prefer ≥£150); recurrence; an advantage we can actually hold (not "AI is cheap": competitors have AI too); accessible channel without the owner as public face; liability we can manage.
- Owner interests carry zero weight unless independent evidence shows an advantage.
- Familiar, easy-to-build or already-built carries zero weight.

## Candidates examined in this pass
### Carbon Reduction Plans (PPN 006 / NHS Evergreen)
- EVIDENCE demand: NHS Supply Chain requires Evergreen Level 1 for all tenders since 6 Apr 2026 (published PPN 006-compliant CRP); NHS extended CRPs to all new procurements from Apr 2024; enhanced global Scope 1–3 CRPs from 1 Apr 2027 for ≥£5m contracts and new frameworks; CRPs must be updated within 6 months of each financial year-end (recurring).
- EVIDENCE spend: Go Positive £449/yr (Scope 1–2 + partial 3) and £739/yr (full); CarbonPass software £199/yr (AI, ~20 minutes, DEFRA 2026 factors); BringAbout used by 500+ businesses (part subsidised); ClimatePartner, Plan A, Greenly, Gopher Zero also active.
- Weakness: crowded, including cheap AI software at £199/yr. Product alone is not an advantage. Any edge would have to be distribution (finding public-sector suppliers without a compliant CRP) or a niche (e.g. 2027 global-scope upgrade for SMEs). Liability: emissions figures and board sign-off are the client's, but errors damage trust.
- Status: strongest evidence of spend so far; competition is the main risk. Needs a channel test, not a build.

### Packaging EPR data for small producers
- EVIDENCE: small producers (≥£1m turnover, ≥25t packaging) must register and report annually by 1 April; 2026 is the first year many face it; compliance schemes and data services already sell this.
- Weakness: next deadline 1 Apr 2027 (demand peaks Jan–Mar, after this programme); compliance schemes dominate.
- Status: candidate for a Q1 2027 test.

### Renters' Rights Act compliance
- EVIDENCE: Act in force 1 May 2026; information-sheet deadline passed 31 May 2026; PRS database due late 2026.
- Weakness: main deadline passed; NRLA and agents already serve landlords; legal-advice risk.
- Status: low priority unless the PRS database creates a clear paid task.

### Cyber Essentials (PPN 014)
- EVIDENCE: mandatory for many government contracts; IASME fee from ~£300; typical SME first-year spend £1,500–£3,500 incl. consultancy (Connection Technologies, Apr 2026); government launched a £9.4m SME support package on 3 Nov 2026.
- Weakness: certification only via licensed Certification Bodies; readiness work is hands-on IT remediation, not automatable; subsidised free help now competes. Rejected.

### Paid MCP / agent tools (x402, MCP marketplaces)
- EVIDENCE: platforms exist (80–90% revenue share), but write-ups report ~95% of MCP developers earn nothing; demand from paying agents unproven. Rejected for the first revenue; watch.

### European Accessibility Act (UK sellers into EU)
- EVIDENCE: applies to UK businesses selling in-scope products/services to EU consumers since 28 Jun 2025; specialist services (AbilityNet) and automated tools exist.
- Weakness: audits need expertise; remediation is hands-on; liability. Low priority.

## Emerging view (ASSUMPTION until tested)
- The strongest pattern is mandated documents for public-sector suppliers, led by Carbon Reduction Plans: mandatory (NHS Evergreen Level 1 for all NHS Supply Chain tenders since Apr 2026), recurring yearly, priced £199–£739/yr by incumbents.
- Product is commoditised; a possible edge is targeting: find public-sector suppliers whose website shows no CRP and make a specific, checkable offer.
- Draft E3 (not yet selected): prospect list from Contracts Finder award notices (OGL) → check supplier site for a published CRP → email limited companies without one (PECR corporate rule, identify sender, opt-out) offering a done-for-you PPN 006 CRP at a fixed price (e.g. £249) in 5 working days → deterministic calculation with DESNZ factors + template + client sign-off. Pass: ≥1 paid order from 100 delivered emails in 14 days.
- Blocker found: fetching Contracts Finder from this session needs approval, which went unanswered (owner away). The shell blocks the host. Needed: owner approval for contractsfinder.service.gov.uk fetches or network allowlisting.
- Opportunity-agnostic capability every B2B test needs: business domain + mailbox with an API so the operator can send and read email itself (not the owner's personal Gmail).

## Next (time-boxed: finish by 2026-11-29)
1. Widen the screen to at least 8 unrelated categories using the rules above (e.g. B2B data/compliance, agent/API marketplaces, outsourced back-office tasks with published prices, acquisition of small profitable assets).
2. For the top 2: define the cheapest test of paid demand that doesn't depend on the owner's identity or labour (e.g. a priced offer to a list built from open data, with replies handled from a business mailbox).
3. Pick one, write experiments/E3-*.md, and only then ask the owner for setup.
