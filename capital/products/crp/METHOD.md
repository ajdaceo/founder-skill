# Carbon Reduction Plan generator: method

What `build_crp.py` produces is the standard Carbon Reduction Plan defined by Procurement Policy Note 006 (the "2024 CRP" in NHS England's wording). It is self-certified: the client supplies the activity data, and its director approves, signs and publishes the plan. No audit or accreditation is required by the standard.

## What the standard requires, and how the generator meets it
Sources: PPN 006 Technical Standard (updated February 2025), the April 2025 template, the selection-stage guidance, and the UK Government conversion factors (introduction and tab notes). Links are in `VALIDATION.md`.

| Requirement | Generator |
|---|---|
| Net Zero commitment by 2050 at the latest | Blocks a plan with a later year |
| All Scope 1 and Scope 2 emissions, UK operations | Client confirms completeness on the intake form; warnings if either scope is zero |
| Five Scope 3 categories: 4 upstream transport, 5 waste, 6 business travel, 7 commuting, 9 downstream transport | Blocks unless each has data or a stated reason it does not apply |
| Tonnes CO2e, Kyoto gases, UK Government conversion factors | Only the published total kg CO2e rows are used; every figure is quantity x factor / 1000 |
| Factors for the year of the activity data | Year holding the greater part of the period; July to June takes the later year ("majority" approach in the factors' introduction). The plan states the approach |
| Location-based electricity | Grid-average factor; market-based is not substituted |
| Consolidation approach stated | Operational control by default; stated in the plan |
| Same reporting period throughout | Warning if baseline and reporting year-ends differ |
| Reporting period no more than 18 months old | Blocks unless an explanation is supplied, which is printed in the plan |
| Updated within 6 months of year-end | Warning if later |
| Five-year reduction target and carbon reduction measures | Blocks if missing |
| Board approval with date; named signatory and job title | Blocks if missing; declaration uses the template's wording |

## Deliberate choices
- Transport the company pays for, inbound or outbound, is category 4. Category 9 is only transport and storage of sold goods the company does not pay for (prefix the activity with `downstream:`).
- Company-owned or leased vehicles are Scope 1 (fuel litres preferred, distance as a fallback). Employees' own cars on business are Scope 3 category 6. The intake form warns against counting the same journeys twice.
- Flights include radiative forcing. Hotel nights are included when supplied. Well-to-tank emissions and electricity transmission losses sit in category 3, outside the required five, and are left out; the plan says so.
- Refrigerant top-ups use the "Kyoto products only" factors.
- Where no factor is published for an activity in a given year (for example mixed commercial recycling in 2022 to 2025), the generator refuses and lists the alternatives. It never substitutes another year's factor.

## Not covered
- The **2027 NHS CRP** (required from 1 April 2027 for NHS frameworks and contracts of £5m a year or more): global boundary and all relevant Scope 3 categories, including purchased goods and services. Spend-based estimates are allowed there but are not built. The generator covers the standard plan, which is what sub-£5m NHS contracts need from that date.
- Market-based electricity, biogenic "outside of scopes" figures, well-to-tank, homeworking.
- Verification. Activity quantities are the client's and are not audited.

## Files
- `factors.csv`: 428 factors, 48 activities, 2018 to 2026, each with its source row. Rebuilt by `build_factors.py` from the files listed in `factor_sources.csv`.
- `build_crp.py`: plan, calculation record and QA result. `--export` adds Word and PDF copies.
- `test_build_crp.py`: 63 checks with hand-worked figures.
