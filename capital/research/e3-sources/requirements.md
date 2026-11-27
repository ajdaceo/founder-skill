<!-- Source notes compiled 2026-11-27 by a research agent for CAPITAL (E3). Each claim carries its URL and quote. Decisive points were spot-checked by the operator; see research/2026-11-27-e3-readiness.md. Not legal advice. -->
# Carbon Reduction Plan (CRP) requirements - sourced research notes

Research date: 27 November 2026. Read-only web research. Every quote below was copied from a source opened on that date unless marked otherwise.

## 0. How sources were accessed (read this before relying on a quote)

- GOV.UK: read through the official GOV.UK Content API (same text as the public page). Full text, exact quotes.
- NHS England (england.nhs.uk): the public HTML pages return an AWS WAF bot challenge and could NOT be opened in a browser-like way. The same pages were read in full through NHS England's own public WordPress REST API on the same host (`/wp-json/wp/v2/...`), which also gives "date" and "modified" stamps. PDFs on england.nhs.uk opened normally. Treated as primary.
- NHS Supply Chain (supplychain.nhs.uk), GCA/CCS (gca.gov.uk), procurementjourney.scot, blogs.gov.scot, finance-ni.gov.uk, belfastcity.gov.uk, lupc.ac.uk: opened directly.
- gov.wales WPPN 006: raw download blocked (403). Read via the fetch tool, which returned only short quoted fragments. Quotes are fragments, not full sentences.
- COULD NOT BE OPENED: gov.scot SPPN 3/2022 page (bot challenge); businessclimatehub.uk (bot challenge); find-tender.service.gov.uk notices (403); thecpc.ac.uk (403); westsussex.gov.uk (403); web.archive.org (blocked). Anything depending on these is marked UNCONFIRMED.

---

## 1. Central government: PPN 006

### 1.1 Current instrument and status
- Current note is "PPN 006: Taking account of Carbon Reduction Plans in the procurement of major government contracts". First published 17 Feb 2025; last public change 10 Jul 2025 (FAQ added). Still listed in the live PPN collection (collection updated 5 Aug 2026, latest note PPN 026 of 28 Oct 2026). No successor or amendment found.
  - URL: https://www.gov.uk/government/publications/ppn-006-taking-account-of-carbon-reduction-plans-in-the-procurement-of-major-government-contracts
  - Quote (publication page): "This PPN has been updated to reflect new terminology introduced by the Procurement Act 2023 and the Procurement Regulations 2024. For procurements commenced and contracts awarded before this date, please refer to PPN 06/21."
  - Change history on that page: "First published." 2025-02-17; "Added the document: Carbon Reduction Plan Template" 2025-04-17; "Added the document: PPN 006: Frequently asked questions" 2025-07-10.
  - Collection list: https://www.gov.uk/government/collections/procurement-policy-notes
- Changed under the Procurement Act 2023? Terminology only, per the note itself.
  - URL: https://www.gov.uk/government/publications/ppn-006-taking-account-of-carbon-reduction-plans-in-the-procurement-of-major-government-contracts/ppn-006-taking-account-of-carbon-reduction-plans-html
  - Quote (para 8): "This update does not constitute a change in policy or a new call for action but in-scope organisations should continue to apply any ongoing obligations set out in the provisions of this PPN."
  - Quote (para 9): "In-scope organisations must apply the provisions of this PPN to relevant procurements advertised on or after 24 February 2025."
  - FAQ Q6: "The substantive obligation introduced by PPN 06/21, now PPN 006, remains the same under the Act (but as a condition of participation as opposed to selection criteria)."
  - One real change: the £5m threshold now INCLUDES VAT (PPN 06/21 was ex-VAT). NHS England notes: "PPN 006 changed the requirements to include VAT in the threshold for CRPs. This could mean that more activity is captured compared to the application of previous PPN 06/21." (https://www.england.nhs.uk/long-read/carbon-reduction-plan-requirements-for-the-procurement-of-nhs-goods-services-and-works/)

### 1.2 Which buyers and contracts
- Buyers. Quote (para 2): "This Procurement Policy Notice (PPN) applies to all central government departments, their executive agencies and non-departmental public bodies."
- Threshold. Quote (para 3): "with an estimated contract value above £5 million per year[footnote 5] (including VAT) under the Procurement Act 2023 save where it would not be relevant to the contract or proportionate to its nature, complexity and cost"
  - Footnote 5: "Based on advertised contract value, averaged over the life of the contract, e.g. a contract with a four year term with a total contract value of £21 million would be in scope, even if the value in the first year was under £5 million."
- EXCLUDED: "special regime contracts". Para 3 says "other than special regime contracts". Procurement Act 2023 s.10(6) (https://www.legislation.gov.uk/ukpga/2023/54/section/10): "(6)A “special regime contract” means—" "(a)a concession contract," "(b)a defence and security contract," "(c)a light touch contract, or" "(d)a utilities contract,". So PPN 006 does not reach defence and security contracts or light-touch (health, social, education etc. services) contracts.
- Frameworks. Quote (para 4): "This PPN applies to frameworks and dynamic markets but only where it is estimated that the individual value of any contract to be awarded in accordance with the framework or by reference to a dynamic market is greater than £5 million per year (including VAT)."
- Devolved administrations. FAQ Q3: "PPN 006 is not stated to be mandatory for Devolved Administrations."
- Subcontractors exempt. FAQ Q19: "There is no requirement for subcontractors to produce a CRP in compliance with this policy, save for where subcontracted organisations are also bidding on a procurement in their own right."
- Consortia. Guidance para 13: "a CRP should be completed by each consortium member".

### 1.3 What the CRP must contain
- Quote (para 11): "confirming the supplier’s commitment to achieving net zero by 2050 for their UK operations"; "providing the supplier’s current emissions for the sources included in Scope 1 and 2 of the GHG Protocol, and a defined subset of Scope 3 emissions"; "publication of the CRP on the supplier’s website".
- Scope 3 categories (Technical standard, https://www.gov.uk/government/publications/ppn-006-taking-account-of-carbon-reduction-plans-in-the-procurement-of-major-government-contracts/ppn-006-technical-standard-for-completion-of-carbon-reduction-plans-html), para 15: "There are 15 categories of Scope 3 emissions defined by the GHG Protocol. In completing your CRP, suppliers are required to detail their emissions for five of these categories as detailed below." Table lists: "4. Upstream transportation and distribution", "5. Waste generated in operations", "6. Business travel", "7. Employee commuting", "9. Downstream transportation and distribution".
- UK boundary. Technical standard para 16: "a carbon footprint for your organisation’s emissions from sources in the United Kingdom".
- Template sections (PPN 006 section 7): commitment to net zero; baseline emissions footprint; current emissions reporting; emissions reduction targets ("We project that carbon emissions will decrease over the next five years to XX tCO2e by 20XX"); carbon reduction projects; declaration and sign off.
- Minor internal inconsistency in the source: PPN para 11 says "the six greenhouse gases covered by the Kyoto Protocol"; the Technical standard para 19 says "the seven greenhouse gasses named by the Kyoto Protocol".

### 1.4 Publication, update and "current" test
- Publication. Technical standard para 12-13: "suppliers should publish their latest Carbon Reduction Plan on their UK website." "Suppliers should place the link on a prominent place on your homepage." "If you do not have a website, you must provide a copy of the statement in writing to anyone who requests one within 30 days."
- Update frequency. PPN 006 section 6.1: "The CRP should be updated regularly (at least annually) and published and clearly signposted on the supplier’s UK website."
- Six-month point. Technical standard para 11: "To this end your Carbon Reduction Plan should be reviewed and updated within 6 months of your organisation’s financial year-end." (wording is "should", in guidance; it is not the pass/fail test.)
- How "current" is actually tested at conditions-of-participation stage (Guidance, https://www.gov.uk/government/publications/ppn-006-taking-account-of-carbon-reduction-plans-in-the-procurement-of-major-government-contracts/ppn-006-guidance-on-taling-account-of-carbon-redcution-plans-adopting-and-applying-conditions-of-participation-html):
  - Para 8: "the CRP has been published since the publication of the tender notice, or in the preceding 12 month period."
  - Table 1 pass row: "the reporting period falls no more than 18 months prior to the date of the tender notice being published"
  - Table 1 fail row: "Reporting period is more than 18 months from the date of the tender notice being published, without an explanation why."
  - FAQ Q9: "Suppliers will only require one CRP (valid for 12 months), which can be used for all procurements where the measure is applied."

### 1.5 Sign-off and verification
- Technical standard para 24: "Your Carbon Reduction Plan should clearly state that board of directors (or equivalent management body) approval has been given with the date of approval."
- Para 25: "Your Carbon Reduction Plan must be signed off by a director (or equivalent) or designated member (for LLPs). Include their name, job title and the date. You do not need to include a physical signature but you should still clearly state that it has been signed."
- No third-party verification. Para 18: "ISO 14064-3 and ISAE 3410 are widely-used standards for the verification of GHG emissions reports, however it should be noted that there is no requirement to have your carbon footprint audited."
- Self-declared. Guidance para 7: "Questions 1 and 2 should be assessed on a pass/fail basis based on self-declarations by the supplier."
- SBTi / Race to Zero do not substitute. FAQ Q10: "these schemes do not align with the requirements of PPN 006 and a CRP based on/using the template outlined in PPN 006 is required."
- CSR statements do not substitute. FAQ Q9: "No, CSR statements, policies and/or case studies cannot be accepted instead of a CRP."

### 1.6 Pass/fail and consequences
- Guidance para 4: "Under this measure a supplier should only be prevented from being awarded a public contract if they provide a CRP which:fails to make an organisational commitment to reduce their emissions over time to achieve net zero by 2050" (list continues).
- Table 1: "Carbon Reduction Plan not submitted (for new entrants, please refer to paragraph 12)." -> "Fail".
- Not scored. FAQ Q7: "Supplier CRPs should not be scored or compared against each other and assessment takes the form of a check that they meet the requirements of the measure."
- GCA (formerly Crown Commercial Service), 30 Apr 2025 (https://www.gca.gov.uk/news/carbon-reduction-plan-supplier-specifics-gca): "Suppliers who do not have a CRP, or submit an outdated plan, will not meet this requirement and therefore will not be able to continue with their bid."

### 1.7 Built-in relief
- New entrants. Guidance para 12: "Suppliers should not be disadvantaged where they are a new entrant to the market (trading for less than 12 months). In these circumstances the supplier should confirm their commitment to achieving net zero by 2050 and should publish a full CRP as soon as possible."
- Missing data with explanation passes. Table 1: "Emissions in the Carbon Reduction Plan not reported for any Scopes or only for some Scopes, but supplier provides an acceptable explanation why." -> "Pass".
- Parent-company CRP allowed if wholly owned and published on bidder's site (PPN para 10).
- Exceptional circumstances (Guidance para 19): "where the market for a contract of this type is distorted/narrowed/struggling to such a significant extent that delivery of public services is likely put at risk" and "where there is a civil emergency".

### 1.8 Related: PPN 016 (contract schedule)
- https://www.gov.uk/government/publications/ppn-016-carbon-reduction-contract-schedule - "The PPN introduces an optional standard carbon reduction contract schedule that can be included in Government contracts." Para 11: "Use of the carbon reduction schedule is optional".

---

## 2. NHS England

### 2.1 Roadmap as currently published
- Roadmap PDF "Published June 2026": https://www.england.nhs.uk/greenernhs/wp-content/uploads/sites/51/2026/06/nhs-net-zero-supplier-roadmap-june-2026.pdf
  - April 2022: "All NHS procurements include a minimum 10% net zero and social value weighting."
  - April 2023/24: "For all new contracts above £5 million per annum, the NHS requires suppliers to publish a Carbon Reduction Plan for their UK Scope 1 and 2 emissions and a subset of scope 3 emissions as a minimum (aligning with PPN 006)." "From April 2024: This requirement is proportionately extended to cover all new procurements."
  - April 2027: "The NHS will implement new proportionate requirements for suppliers to publicly report targets, emissions and publish a Carbon Reduction Plan for all of their relevant global scope 1, 2 and 3 emissions."
  - April 2028: "New requirements will be introduced overseeing the provision of carbon footprinting for individual products supplied to the NHS. The NHS will work with suppliers and regulators to determine the scope and methodology."
  - The PDF graphic shows four milestones (2022, 2023/24, 2027, 2028). 2030 is not on the graphic.
- 2030 is still on the web page (modified 9 Jun 2026): https://www.england.nhs.uk/greenernhs/get-involved/suppliers/ - "From 2030, suppliers will only be able to qualify for NHS contracts if they can demonstrate their progress through published progress reports and continued carbon emissions reporting."
- April 2027 wording was softened. Earlier roadmap PDF (marked "Published November 2023", https://www.england.nhs.uk/greenernhs/wp-content/uploads/sites/51/2024/04/NHS-Net-Zero-Supplier-Roadmap-2024.pdf) said: "All suppliers will be required to publicly report targets, emissions and publish a Carbon Reduction Plan for global emissions aligned to the NHS net zero target, for all of their Scope 1, 2 and 3 emissions." The June 2026 text says "new proportionate requirements" and "relevant" emissions.

### 2.2 Rules in force NOW (procurements commenced before 1 April 2027)
Source: "Carbon reduction plan and net zero commitment requirements for the procurement of NHS goods, services and works", publication ref PRN00711, first published 14 Feb 2023, last modified 11 Dec 2025. https://www.england.nhs.uk/long-read/carbon-reduction-plan-requirements-for-the-procurement-of-nhs-goods-services-and-works/
- Who: "In-scope organisations are defined as NHS organisations as well as organisations acting on their behalf."
- Tier 1 (full CRP): "a full Carbon Reduction Plan (CRP), as defined in the section “CRP Requirements”, is required for procurements of high value (£5m per annum including VAT and above) and new frameworks operated by in-scope organisations, irrespective of the value of the contract, where relevant and proportionate to the framework."
- Tier 2 (commitment only): "a Net Zero Commitment, as defined in the section “Net Zero Commitment – Requirements”, is required for procurements of lower value (below £5m per annum including VAT and above the relevant published procurement threshold)."
- So BELOW £5m a year a full CRP is NOT required today; only a Net Zero Commitment, and only above the procurement thresholds. Table 1, NZC row from April 2024: "All new contracts below £5m per annum (including VAT since 24 February 2025) and above the published procurement threshold".
- Frameworks: "All new NHS frameworks or open frameworks, irrespective of contract value, are required to apply the full CRP requirements. Where NHS framework owners determine the CRP requirements are not proportionate and relevant to the nature of the framework and out of scope of central government CRP requirements, the owner should apply the NZC requirements." Same for dynamic markets ("as part of the conditions of membership"). Applied "at framework/open framework level, rather than to individual call-offs."
- What a Net Zero Commitment is: "NZC is a public commitment to achieve net zero by 2050 or earlier, and a confirmation that the supplier is taking steps to reduce their GHG emissions over time." Must "clearly signpost and publish the commitment on the supplier’s website." Suggested one-line format (Annex 1): "“[Supplier name] is committed to achieving Net Zero emissions by 20XX for emissions scopes X, X and X. The commitment was made on DD/MM/YY by the [approving board/equivalent management body]”".
- NHS CRP = PPN 006 CRP: "any existing and current CRP developed according to the central government guidelines of PPN 006 will be accepted by the NHS."
- Pass/fail: "Suppliers whose CRP or NZC does not meet the minimum requirements will not be able to proceed to the next stage of the procurement process, except in exceptional circumstances as set out in Annex 5. CRPs and Net Zero Commitments will not be scored or compared against each other."
- Direct awards: "the requirements should be included, where possible, as due diligence, but not assessed as a pass-fail requirement."
- Subcontractors: "Subcontractors are not in scope of the CRP/NZC requirements and do not need to provide evidence of either."

SOURCE CONFLICT on the April 2024 milestone:
- DHSC / NHS England SME guide, 24 Feb 2026 (https://www.gov.uk/government/publications/doing-business-with-the-health-sector-a-guide-for-buyers-and-small-and-medium-sized-enterprises-smes/how-smes-can-work-effectively-with-the-nhs): "From April 2024, all NHS procurements require a carbon reduction plan, regardless of contract value".
- NHS Supply Chain (https://www.supplychain.nhs.uk/programmes/sustainability/net-zero-supply-chain-and-suppliers/): "All suppliers of new contracts for goods, services, and works are required to publish a Carbon Reduction Plan (CRP) (PPN 006)."
- These contradict the detailed NHS England policy guidance quoted above (Net Zero Commitment for sub-£5m). The detailed guidance is the governing document; the one-line summaries are loose. NHS Supply Chain's line is true for its own tenders because they are frameworks.

### 2.3 Rules from 1 April 2027 (CONFIRMED, not delayed, but scaled back)
Source: "2027 NHS carbon reduction plan requirements for the procurement of NHS goods, services and works", ref PRN02316_ii, published 9 Jun 2026, last modified 21 Jul 2026. https://www.england.nhs.uk/long-read/2027-nhs-carbon-reduction-plan-requirements-for-the-procurement-of-nhs-goods-services-and-works/
- Effective date: "From 1 April 2027 this guidance replaces the previous carbon reduction plan guidance and associated requirements." "Procurements commenced prior to 1 April 2027 should continue to apply the requirements set out in the previous CRP and NZC requirements".
- NET ZERO COMMITMENT ABOLISHED for new procurements: "From 1 April 2027, the NHS CRP requirements described in this guidance replace the previous CRP and net zero commitment (NZC) requirements for the procurement of NHS goods, services and works for all in-scope procurements; and therefore, no new procurements will be in scope of the NZC requirements."
- Two tiers:
  - "A 2027 NHS Carbon Reduction Plan (2027 NHS CRP) tier: Applied to procurements of high value (£5 million per annum and above, including VAT) and all new frameworks operated by in-scope organisations, irrespective of the value of the framework contract, where relevant and proportionate to the framework."
  - "A 2024 CRP tier: Applied to procurements of lower value (below £5 million per annum including VAT, and above the relevant published procurement thresholds)."
  - Table 1 lower row: "All new contracts below £5 million per annum (including VAT) and above the relevant published procurement threshold.**" -> "2024 CRP requirement".
- Meaning for small suppliers: from 1 April 2027 a sub-£5m, above-threshold NHS contract needs a full PPN 006-style CRP ("2024 CRP"), where today a one-line commitment suffices.
- Frameworks/dynamic markets: "All new NHS frameworks* or open frameworks, irrespective of contract value, are required to apply the 2027 NHS CRP requirements, unless deemed not proportionate." "Where NHS framework owners determine the 2027 NHS CRP requirements are not proportionate and relevant to the nature of the framework the owner should apply the 2024 CRP requirements." "All new dynamic markets, irrespective of contract value, are required to apply the 2027 NHS CRP requirements as part of the conditions of membership."
- 2027 NHS CRP content: "confirm the supplier’s commitment to achieve net zero by 2050 or earlier for their whole organisation"; "provide the supplier’s baseline and current emissions for the sources included in scope 1 and 2, and all relevant scope 3 emissions in adherence with the GHG Protocol Standard, which identifies 15 emissions categories to be considered"; "be board approved or company director approved if no board is in place"; "be clearly signposted and published on the supplier’s website".
- Global boundary (Annex 1): "For the chosen reporting entity, a global geographical boundary must be applied for the net zero commitment and emissions reporting." Estimation allowed: "estimation methods can be used to calculate scope 3 emissions; for example, through spend-based methods using carbon conversion factors."
- 2024 CRP content (lower tier) is unchanged PPN 006: "commitment to achieve net zero by 2050 or earlier for their UK operations as a minimum geographical boundary" and the same five scope 3 categories.
- Validation/offset disclosure NOT mandatory. Annex 2 Table 4: "Target validation" -> "Not required" for both tiers ("Independently 3rd party validated targets" is only "NHS recommended"). Net zero year minimum "2050"; "2045 or before" is only recommended.
- Pass/fail: "Suppliers whose 2027 NHS CRP or 2024 CRP does not meet the minimum requirements will not be able to proceed to the next stage of the procurement process, except in exceptional circumstances as set out in Annex 5." Annex 5 row 4: "CRP not submitted." -> "Fail".
- First-year leniency (Annex 5 row 14): "Supplier has gaps in first year emissions data for additional scope 3 reporting requirements in NHS FY 2027/28 tenders and provides an acceptable explanation and plan for building capability to report on associated emissions from the following year." -> "Pass".
- Annual update enforced by contract: "relevant authorities should include the requirement for annual updates within the terms and conditions of any contract arranged under PSR."
- Direct awards: "Where it is determined that selection criteria will not be used, suppliers should be encouraged to submit their CRP but these should not be assessed as a pass-fail requirement."
- Scaling back confirmed by NHS England's own findings report (ref PRN02316_i, 9 Jun 2026, https://www.england.nhs.uk/long-read/market-sounding-findings-net-zero-supplier-requirements-from-april-2027/): "3 policy positions were revised: suppliers are encouraged to set a net zero target of 2045, but 2050 is now the minimum requirement"; "validation is encouraged but not mandated"; "the requirement to estimate future offsetting has been removed". Also: "The policy position has been revised to reduce cost burden on suppliers, especially SMEs".
- No later change found. NHS Supply Chain's own CRP dated August 2026 still plans for it: "Prepare suppliers for future NHS Net Zero milestones, including the 2027 requirement for expanded Carbon Reduction Plans covering global Scope 1, 2 and" (https://azuksappnpdsa01.blob.core.windows.net/datashare/NHS-Supply-Chain-Carbon-Reduction-Plan-August-2026.pdf).

### 2.4 April 2028 and 2030
- 2028 is being narrowed. NHS England FAQ, 25 Nov 2026 (https://www.england.nhs.uk/long-read/2028-market-insights-survey-frequently-asked-questions/): "This policy will therefore not apply to all products in the three areas, but only to targeted sub-categories that will maximise impact." "It is likely the requirements will be gradually phased in from April 2028, focusing on priority products with maximum opportunity for impact and key procurement opportunities such as new frameworks or framework renewals." The three areas are "pharmaceuticals, medical technologies, and digital".
- 2030: only the one sentence quoted in 2.1. No implementing guidance found. NHS England says it will "produce the next phase of the NHS Net Zero Supplier Roadmap for 2030 onwards" (https://www.england.nhs.uk/long-read/five-years-greener-nhs-progress-forward-look/). Detail UNCONFIRMED.

### 2.5 Evergreen Sustainable Supplier Assessment
Source: https://www.england.nhs.uk/nhs-commercial/sustainability/evergreen/ (modified 17 Jun 2026)
- What it is: "a self-assessment and reporting tool for suppliers to share sustainability information with the NHS". Hosted on Atamis. "the maturity score will be valid for 12 months."
- Normally not a procurement gate: "The assessment has not been designed to be included as a scored or evaluated requirement in procurement. There are two exceptions". Exception 1: "Suppliers bidding to be on any future NHS Supply Chain Frameworks will be required to submit an Evergreen Assessment and achieve Level 1 as part of the tendering process." Exception 2: NHS England medicines tenders "requiring submission of the Evergreen Assessment from January 2024."
- Levels (criteria "updated in April 2026"):
  - "Level 1 (entry level maturity) Published a Carbon Reduction Plan aligned to PPN requirements, with a UK net zero commitment and emissions reporting."
  - "Level 2 Comprehensive net zero targets and reporting for carbon emissions at a global level aligning to April 2027 Net Zero Supplier Roadmap requirements"
  - "Level 3 2045 net zero targets that are independently validated, and completion of the modern slavery assessment tool."
  - "Level 4 (highest maturity) 2045 net zero targets, independently validated, across the global organisation, while actively taking steps to map supply chain or investigate and mitigate supplier risks of modern slavery."
  - All levels: CRP publication date "Required to be within 12-month period of Assessment submission"; sign-off "Board level"; Level 1 and 2 validation "Not required".

### 2.6 NHS Supply Chain (current requirement)
- News article 26 Feb 2026: https://www.supplychain.nhs.uk/news-article/evergreen-sustainable-supplier-assessment-what-suppliers-need-to-know-for-april-2026/
  - "From 6 April 2026, NHS Supply Chain will introduce an important update to our sustainability requirements for suppliers." "From this date, all suppliers submitting tenders will be required to have achieved Evergreen Level 1 at the point of tender close." "This marks a shift from our previous approach, where any Evergreen submission level was accepted."
  - Level 1 means: "Demonstrate a commitment to achieving net zero by 2050"; "Publish a PPN 006 compliant Carbon Reduction Plan (CRP)"; "Report UK Scope 1, Scope 2, and relevant Scope 3 emissions."
  - "Will tender evaluations score my Evergreen Level? No. Evergreen is required but not evaluated as part of tender scoring."
  - "Level 1 does not require global emissions reporting"
- Pass/fail wording (https://www.supplychain.nhs.uk/suppliers/product-innovation/medical-technology-dynamic-purchasing-system/): "Carbon Reduction Plans are now a selection criterion for any NHS Supply Chain tender meaning that if you haven’t included one in your tender submission, it’s a pass / fail and you won’t progress to the next stage." And: "at tender stage, if you are unable to confirm that you have an Evergreen Level 1 or above Assessment, then it is a pass / fail and you won’t progress further."
- SME softening on the same page: "whilst this is a mandatory requirement, it shouldn’t be a barrier to entry for SMEs or innovators, there are clauses in the guidance above whereby if you haven’t collected the data yet or perhaps there is missing data, you can provide an explanation and commit to doing so."
- Consequence (https://www.supplychain.nhs.uk/programmes/sustainability/): "non-compliance may affect your ability to bid for or retain contracts."
- Individual tender notices reportedly word the test as Level 1 "within 12 months prior to the Tender Close Date". UNCONFIRMED (Find a Tender notices could not be opened; seen only in search snippets).

---

## 3. Other buyers

### 3.1 Wales - WPPN 006 (fragments only; see section 0)
- URL: https://www.gov.wales/wppn-006-decarbonisation-through-procurement-taking-account-of-carbon-reduction-plans-html (first published and last updated 24 Feb 2025 as reported by the fetch tool).
- Who and value: "This WPPN has been published to assist Welsh Government departments, NHS Wales bodies" ... "consider a CRP as a supplier selection criterion in all procurements of £6 million and over".
- Wider Welsh public sector is recommended, not mandated: "This WPPN is recommended as best practice to all Devolved Welsh Authorities (DWAs)."
- Requirement: "Making the inclusion of a Carbon Reduction Plan (CRP) or equivalent" "a requirement at the selection stage of the procurement of public contracts valued at £6 million or more."
- Threshold change: "Amend the threshold figure of £5 million (exc. VAT) to include VAT" "for a new figure of £6 million, to align with other WPPNs."
- Below threshold: "For contracts below £6 million DWAs are strongly advised to take a risk-based assessment" "use their discretion to apply a CRP requirement to contracts in high emission categories." Sectors named: "Manufacturing," "Construction, Transportation and Human Health and Social Work activities."
- "CRPs are only to be used as a supplier qualification pass / fail requirement."
- No SME-specific provision reported. UNCONFIRMED beyond these fragments.

### 3.2 Scotland - different instrument (Bidder Climate Change Plan), not a PPN 006 CRP
- SPPN 3/2022 page itself: COULD NOT BE OPENED. UNCONFIRMED.
- Operative guidance (Procurement Journey): https://www.procurementjourney.scot/additional-resources/climate-emergency/what-do-i-do-on-climate
  - Discretionary: "If you have identified that your procurement exercise is a relevant and/or priority contract, you may ask bidders to provide assurance of their awareness of and response to the climate emergency." "This may be done by asking bidders to provide a completed Bidder Climate Change Plan template in the selection stage at SPD question 4C.7."
  - "Priority contracts are: Contracts with a total value of £4 million or greater or Contracts that focus on commodities identified as climate change priorities by your organisation’"
  - Lighter template for smaller bidders: "the Bidder ‘relevant contract’ Climate Change Plan Template asks bidders to supply information on their organisation’s emissions sources, but does not ask bidders to calculate their carbon emissions."
  - Priority template asks for "their organisation's calculated scope 1 and 2 emissions" (no scope 3 calculation).
  - SME relief: "Where the Organisation wants to reduce barriers to participation in a procurement process, they may wish to use the 'relevant' template for higher value/priority contracts. For example, for frameworks or Dynamic Purchasing System (DPS) exercises, where a number of smaller enterprises may be expected to bid"
  - Pass/fail: "Pass Production and submission of a Bidder Climate Change Plan that has been reviewed and signed off by a person in the business with authority."
- Refreshed 16 Jun 2026 (https://blogs.gov.scot/public-procurement/2026/06/16/refreshed-guidance-for-the-single-procurement-document-and-bidder-climate-change-plans/): "Climate change plans should only be requested for tenders where relevant and proportionate"; "some bidders, including SMEs, require further support, but support needs to be proportionate and manageable"; "removal of previous reference to progression timescales to allow a focus on embedding current best practice".

### 3.3 Northern Ireland
- No carbon-reduction-plan policy note exists on the Department of Finance PPN list. https://www.finance-ni.gov.uk/articles/procurement-policy-notes-ppns lists only: "Procurement Policy Note - 05/21 Human Rights in Public Procurement", "04/21 Procurement Control Limits", "03/21 Supply Chain Resilience", "02/21- Procurement of Social and Other Specific Services (Light Touch Services)", "01/21 - Social Value in Procurement".
- Absence of a requirement elsewhere in NI policy: UNCONFIRMED (only the PPN list was checked).
- Council example: Belfast City Council, tenders over £1 million (https://www.belfastcity.gov.uk/documents/sustainable-procurement-policy-and-strategy/implementing-our-policy): "Within 12 weeks of being awarded a contract, suppliers must upload their greenhouse gas (GHG) emissions data using our carbon reporting tool. They must also publish a carbon reduction plan showing how they will reduce their emissions year by year over the length of the contract." (post-award, not a bid gate). Below £1m: "a supplier can be rewarded as part of the tender process by choosing to implement these requirements in their sustainable offer."

### 3.4 Ministry of Defence
- MOD is a central government department, so PPN 006 applies to its ordinary contracts over £5m a year. But PPN 006 excludes "special regime contracts", which include "(b)a defence and security contract," (see 1.2).
- No MOD-specific CRP policy page found on GOV.UK (site search for MOD/DE&S returned nothing). MOD practice on defence and security contracts: UNCONFIRMED.

### 3.5 Crown Commercial Service (now Government Commercial Agency, GCA)
- crowncommercial.gov.uk redirects to gca.gov.uk.
- GCA annual report 2025-26 (https://www.gov.uk/government/publications/government-commercial-agency-annual-report-and-accounts-2025-to-2026/gca-annual-report-and-accounts-2025-to-2026-accessible-version): "For any contract over £5 million, PPN 006 (PPN 06/21) applies, requiring bidders to provide a Carbon Reduction Plan (CRP)". "CRP compliance process is fully integrated into our supplier management activities to ensure all relevant suppliers maintain compliance throughout the lifetime of their agreements. All compliant CRPs are linked to supplier records on our website for public visibility."
- Not all frameworks. GCA guide (https://www.gca.gov.uk/social-value/carbon-net-zero/how-to-create-a-carbon-reduction-plan-crp): "Before starting, check if you actually need a CRP, as many contracts are exempt from PPN 006"; "check for exceptions: even if a contract is under £5 million, buyers may still need a CRP"; "Always check the specific framework’s terms and tender documents before bidding."
- GCA article (URL in 1.6): "If the contract you are bidding for does not meet the £5 million per year threshold, it will not require a CRP to be submitted. This threshold means plenty of contracts are exempt from CRP requirements."
- Which specific GCA frameworks require a CRP from every supplier: UNCONFIRMED (framework-by-framework).

### 3.6 Local authorities (England)
- Not in scope of PPN 006 (para 2 quoted in 1.2 covers only central departments, executive agencies and NDPBs). Any council requirement is the council's own choice. Only one council policy was opened (Belfast, 3.3). Prevalence across councils: UNCONFIRMED.
- Councils commissioning healthcare under the Provider Selection Regime are named as relevant authorities in the NHS guidance ("Local authorities or combined authorities"), so NHS CRP rules can reach those procurements.

### 3.7 Universities and education consortia
- UK Universities Purchasing Consortia guidance, "Developed by LUPC and adopted by the UKUPC RP Network 2025", "Updated: May 2026": https://www.lupc.ac.uk/media/om2jovit/approach_to_net_zero_with_suppliers.pdf
  - Not mandatory: "While most members are not formally in scope, this framework provides a practical approach to supplier engagement on carbon reduction."
  - Tiering: "Tier 1 — full CRP required"; "Tier 2 — simplified disclosure"; "Tier 3 — commitment only".
  - SMEs: "Tier 3 SMEs / lower-impact Net Zero commitment statement and roadmap in lieu of full emissions disclosure. Signpost to free SME resources (e.g. SME Climate Hub)."
  - "A tiered approach avoids placing disproportionate burden on smaller or lower-impact suppliers".
  - "CRPs should be updated annually, ideally within 6 months of the supplier’s financial year-end."
- TUCO, Crescent Purchasing Consortium, YPO, ESPO: no published blanket CRP rule could be opened. UNCONFIRMED. (A search snippet says a SUPC books framework requires "a carbon reduction plan no later than six months after the framework launches"; not opened, UNCONFIRMED.)

---

## 4. Urgency evidence

### 4.1 Numbers
- Size of NHS supplier base: "over 600,000 products purchased from 80,000 national and global suppliers" (https://www.england.nhs.uk/long-read/five-years-greener-nhs-progress-forward-look/, Sept 2025).
- Evergreen uptake: "Over 2,000 suppliers have signed up to the Evergreen Sustainable Supplier Assessment" (same page). Arithmetic, mine: about 2.5% of 80,000. This is sign-ups, not CRP holders.
- Spend coverage: "under this extended policy, 90% of NHS (non-pay) spend is in scope of Carbon Reduction Plans (CRP) or Net Zero Commitment requirements" (https://www.england.nhs.uk/long-read/progress-report-delivering-a-greener-nhs-five-years-on/, 22 Sep 2025).
- NHS Supply Chain: "Continued strengthening of expectations relating to Carbon Reduction Plans and Evergreen Assessments across procurement activity. 97% of spend now covered by these." (NHS Supply Chain CRP, August 2026, URL in 2.3).
- GCA training demand: "During 2025/26, we have delivered 16 virtual sessions with around 1,000 attendees. Since its inception, the CRP training has been attended by almost 6,300 people across nearly 100 events." (GCA annual report, URL in 3.5).
- NHS 2027 consultation: "We engaged around 10,000 stakeholders and received 219 survey responses"; among suppliers "small and medium‑sized enterprises accounting for 54%"; "Feedback highlighted the specific need for support of smaller suppliers to report on all 15 Scope 3 categories and the need for simple, government-backed tools to support consistency." (findings report, URL in 2.3).
- NOT FOUND: any official count of suppliers lacking a CRP, or of bids rejected for lacking one. UNCONFIRMED / no data published.

### 4.2 Official pass/fail statements
- Cabinet Office: Table 1 "Carbon Reduction Plan not submitted" -> "Fail" (1.6).
- GCA: "will not be able to continue with their bid" (1.6).
- NHS England: "will not be able to proceed to the next stage of the procurement process" (2.2, 2.3).
- NHS Supply Chain: "it’s a pass / fail and you won’t progress to the next stage" (2.6).

### 4.3 Evidence of burden on small suppliers
- CMA, "Public procurement in the national interest", 8 Sep 2026 (https://www.gov.uk/government/publications/procurement-in-the-national-interest/public-procurement-in-the-national-interest-reflections-from-the-cma): "Case study 2: A medical equipment supplier reported that under NHS England requirements, all suppliers must publish a current Carbon Reduction Plan, undertake an Evergreen supplier assessment, complete a Modern Slavery Assessment, and undertake Cyber Essentials certification. The business said it understood the reasons behind these requirements, but the requirements presented a disproportionate burden on SMEs." "Exemptions for SMEs from some of these requirements can themselves be relatively burdensome to complete."

### 4.4 Free official tools and stated effort
- Cabinet Office template: "Carbon Reduction Plan Template ODT, 102 KB" on the PPN 006 page (URL in 1.1). Seven short sections.
- GCA step-by-step guide with worked examples ("a carbon reduction plan example for a small sized technology supplier"), "Interactive CRP training session run monthly by our Sustainability Team", and "UK Government-endorsed carbon footprint calculator on the UK Business Climate Hub page" (https://www.gca.gov.uk/social-value/carbon-net-zero/how-to-create-a-carbon-reduction-plan-crp). Effort hint on that page: "Give yourself enough time: gathering emissions data may require contacting people inside and outside your business". No hours figure given.
- UK Business Climate Hub: GOV.UK press release 14 Aug 2023 (https://www.gov.uk/government/news/one-stop-shop-to-help-businesses-save-money-and-go-green): "includes a free carbon calculator and a suite of new tools to help businesses measure, track and report on their emissions". The hub site itself could not be opened; time-to-complete claim UNCONFIRMED.
- SME Climate Hub (not government): https://smeclimatehub.org/tools/ - "Measure your emissions with our free Carbon Calculators."; Climate Action Planner labelled "60 minutes".
- PPN 006 Technical standard para 17: "Many tools and resources are available for free if you are an SME or VCSE supplier." FAQ Q17: "Some of these services are available for free for SME and VCSE suppliers, others may charge. Suppliers should ensure that CRPs produced by third parties on their behalf still meet the requirements of this policy."
- NHS England: free "Sustainable supplier accelerator" - "a schedule of free webinars, activities and supporting resources" (https://www.england.nhs.uk/nhs-commercial/sustainability/). Current guidance also offers "regular webinars and a CRP checking service" via "england.crp-check@nhs.net" (URL in 2.2). The 2027 guidance mentions webinars only; whether the checking service continues after April 2027 is UNCONFIRMED.
- Scotland: free blank and worked-example templates plus "Supplier’s Guide to Bidder Climate Change Plans" (URL in 3.2).

---

## 5. What weakens the business case

1. Obligation is narrow outside the NHS. Central government only above £5m a year, frameworks only where a call-off exceeds £5m a year (1.2). Home Office SME/VCSE Bid Pack, 6 Oct 2026 (https://www.gov.uk/government/publications/smevcse-public-procurement-bid-pack/smevcse-bid-pack): "For most SMEs and VCSEs, this will only apply when bidding for major contracts."
2. A simple commitment suffices in several places: NHS sub-£5m contracts until 31 March 2027 (2.2); university consortia Tier 3 SMEs (3.7); Scotland's "relevant" template needs no emissions calculation (3.2).
3. Partial data is accepted with an explanation, expressly for SMEs. NHS 2027 guidance: "to reduce barriers for the SMEs and VCSEs to bid for NHS contracts, SMEs or VCSEs with acceptable reasons may use this provision." PPN 006 new-entrant relief (1.7).
4. Whole procurements can be exempted for SME markets. NHS Annex 5: "Where a light touch contract, framework or dynamic market is set up in accordance with PA23 to support SMEs or VCSEs to access public contracts, and the request to implement a CRP could be a barrier to entry."
5. Subcontractors are out of scope everywhere checked (1.2, 2.2).
6. No audit, verification or accreditation is required, and the plan is self-declared (1.5). It is designed to be done in-house on a free template with free training and a free checking service (4.4).
7. Direction of travel is "proportionate": NHS softened 2027 (2.3), is narrowing 2028 (2.4); Scotland removed "progression timescales" (3.2); the CMA has published an SME-burden case study naming the CRP (4.3).
8. Plans to abolish or replace the requirement: none found. PPN 006 unchanged since July 2025; NHS April 2027 date stands. No government-run service that writes the plan for the supplier was found.

---

## 6. Verdict on the four file claims

- (a) NHS Supply Chain requires Evergreen Level 1 (a published CRP) for all tenders since 6 April 2026: CONFIRMED (2.6). Level 1 must be held "at the point of tender close"; it is required but not scored.
- (b) NHS has required CRPs for all new procurements since April 2024: WRONG as stated. Since April 2024 a full CRP is required only at £5m a year and above and for new frameworks/dynamic markets; below £5m (and above procurement thresholds) only a Net Zero Commitment; below thresholds nothing (2.2). One GOV.UK guide and NHS Supply Chain repeat the loose version (conflict noted in 2.2). It becomes close to true from 1 April 2027 (2.3).
- (c) From 1 April 2027 enhanced CRPs covering global Scope 1-3 are required: PARTLY RIGHT. Date confirmed. The enhanced "2027 NHS CRP" applies only at £5m a year and above and to new frameworks/dynamic markets where proportionate; everything else above threshold gets the ordinary "2024 CRP". Scope 3 is "all relevant" categories, estimation allowed, validation not required, 2050 minimum (2.3).
- (d) CRPs must be updated within 6 months of each financial year-end: PARTLY RIGHT. The Technical standard says "should be reviewed and updated within 6 months of your organisation’s financial year-end"; the binding rule is "at least annually", and the bid test is publication within the preceding 12 months and a reporting period no more than 18 months before the tender notice (1.4).
