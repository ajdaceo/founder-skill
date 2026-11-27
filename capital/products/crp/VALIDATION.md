# Independent validation of the calculation (2026-11-27)

**Result: the generator and an independent recalculation agree on every line.**

## How it was checked
A separate agent was given only the official flat files and a plain-English description of 24 activities for a fictitious food wholesaler over two periods. It was barred from reading this repository, chose the factor rows and factor years itself from the official guidance, and calculated in exact decimal arithmetic. Its output is `validation/case1-independent-result.json`; the generator's input is `validation/case1-client.json`.

| | Factor year | Scope 1 | Scope 2 | Scope 3 | Total (tCO2e) |
|---|---|---|---|---|---|
| Baseline, July 2019 to June 2020: generator | 2020 | 203.705 | 72.273 | 110.811 | 386.790 |
| Baseline: independent | 2020 | 203.705 | 72.273 | 110.811 | 386.790 |
| Current, April 2024 to March 2025: generator | 2024 | 169.322 | 61.080 | 106.972 | 337.374 |
| Current: independent | 2024 | 169.322 | 61.080 | 106.972 | 337.374 |

All 48 line items match; the largest difference is 0.0005 t (rounding in the printed record). The checker also confirmed the downloaded factor files are byte-identical to the versions on gov.uk.

## What the check showed about judgement calls
- **July to June years.** The guidance says such years "should apply the newest set of available factors", which both calculations read as the later year. A strict day count would pick the earlier year and move this baseline by about 7 t (mainly electricity and landfill factors). The guidance also permits a day-weighted "blended" approach. The generator uses the majority approach and says so in the plan.
- **Landfill factor.** The commercial waste landfill factor rose from about 100 to 458 kg per tonne between the 2019 and 2020 sets, and to 520 by 2023. A baseline using 2018 or 2019 factors will show much lower waste emissions than later years for the same tonnage.
- **Natural gas.** The standard "Natural gas" row is used, not "100% mineral blend".

## Method review against the official standard
The checker read the PPN 006 Technical Standard, template, guidance and FAQ. Its findings led to these changes, all now in the generator and tests:
1. Declaration text replaced with the template's exact wording.
2. Outbound transport the company pays for moved to category 4; category 9 kept for transport the company does not pay for.
3. A reporting period more than 18 months old now blocks the plan unless an explanation is given.
4. The consolidation approach, location-based electricity, radiative forcing and the exclusion of well-to-tank and transmission losses are stated in the plan.
5. Board approval date is required.
6. Warning when baseline and reporting year-ends differ.
7. Wastewater treatment added as a category 5 activity.

Still to handle on the intake form rather than in code: confirming every UK site is covered, avoiding double counting between fuel-card litres and mileage claims, and whether leased vehicles are inside the boundary.

## Sources
- Technical Standard: https://www.gov.uk/government/publications/ppn-006-taking-account-of-carbon-reduction-plans-in-the-procurement-of-major-government-contracts/ppn-006-technical-standard-for-completion-of-carbon-reduction-plans-html
- Template (April 2025): https://assets.publishing.service.gov.uk/media/6800e3930b24153af1e7c700/2025-04-16_PPN_006_Carbon_Reduction_Plan_Template.odt
- Guidance on selection criteria: https://www.gov.uk/government/publications/ppn-006-taking-account-of-carbon-reduction-plans-in-the-procurement-of-major-government-contracts/ppn-006-guidance-on-taling-account-of-carbon-redcution-plans-adopting-and-applying-conditions-of-participation-html
- FAQ (June 2025): https://www.gov.uk/government/publications/ppn-006-taking-account-of-carbon-reduction-plans-in-the-procurement-of-major-government-contracts/ppn-006-frequently-asked-questions
- Conversion factors and year rule: see `factor_sources.csv`; the rule is in the Introduction sheet of each year's full set.

## Limits of this validation
One worked case with 24 activities and two factor years. It tests factor selection, year selection and arithmetic. It does not test a real client's data quality, which stays the client's responsibility, and the checker was another AI agent, not a qualified carbon accountant.
