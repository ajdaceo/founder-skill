# E3 supplier scan — final (2026-11-27)

**Verdict: passes the owner's threshold, narrowly on the measure that matters.** Of the first 50 suppliers on the list, 37 (74%) have no current published Carbon Reduction Plan (CRP). Counting only realistic buyers that can be contacted, 22 of 50 (44%) qualify, against a 40% bar. On the most cautious reading (treating any plan dated 2025 as current) it is 17 of 50 (34%), which fails. Recommendation: run the £25 outreach test, with the two risks below written into it.

Row-by-row evidence: `research/e3-scan-verified.csv`. Websites used: `research/e3-prospects-first50-sites.csv`.

## Sample
First 50 rows of `research/e3-prospects-nhs-food-framework.csv` (80 SMEs on the NHS Supply Chain Fresh & Food to Go framework, FTS 026675-2024). All are in scope: NHS Supply Chain has required a published CRP (Evergreen Level 1) for tenders since 6 April 2026.

The first 50 rows are the list's first alphabetical block, mostly fresh-food wholesalers, butchers and dairies. The second block (30 rows, mostly sandwich and food-to-go makers) was not scanned, apart from three checked earlier: Raynor Foods (current plan), Tiffin Sandwiches (none), On a Roll (none).

## Final counts (50 suppliers, each verified by hand)
| Status | Count | Meaning |
|---|---|---|
| Current plan | 13 | Published and covering the latest financial year |
| Overdue plan | 5 | Published in 2025, annual update now late (13–20 months old) |
| Outdated plan | 2 | Dated 2024 (Braces Bakery, County Foods) |
| Plan not published | 1 | Middlesex Meat: website says "contact us for a copy" |
| No plan | 14 | Working website, nothing found in two passes |
| Website down | 5 | Could not be checked (maintenance, suspended, 503/522 from two networks) |
| No website found | 8 | Nowhere to publish a plan, but no email route either |
| Insolvent | 2 | James Burrows (administration, Oct 2025), QMover MFS (notice of intention, Aug 2026) |

"Current" follows the rule already recorded in E3: a plan must be updated within six months of each financial year-end. Year-ends were read from the reporting year in each document, so the five "overdue" calls carry some uncertainty; Clegg's and Hallam Country Fresh are the closest calls at 13–14 months.

## The three ways to count
| Measure | Count | Share of 50 |
|---|---|---|
| No current published plan, any reason | 37 | 74% |
| Realistic buyer: working website, solvent, plan missing, unpublished, outdated or overdue | 22 | 44% |
| Same, but treating the five 2025-dated plans as current | 17 | 34% |

Among the 35 suppliers with a working website and no insolvency, 22 (63%) lack a current plan.

## What changed since the interim scan
The interim figure was 5 of 8 (62%) lacking a current plan. The larger sample is less favourable: more suppliers have plans than the first eight suggested.

## Two risks for the offer
1. **Most suppliers who needed a plan have already made one themselves.** 21 of the 35 working-site suppliers (60%) have produced a plan at some point. Most used the free Cabinet Office template; Clegg's used a Chamber of Commerce programme; only Harlech and Prescott-Thomas show paid outside help (both ClimatePartner). The task is evidently doable in-house at no cost, which weakens a £249 price. The outreach test is what will show whether the remaining suppliers will pay.
2. **The prospect pool is thin.** 22 reachable prospects from 50 scanned implies about 35 from the full 80. The E3 test needs 100 delivered emails, so roughly 230 suppliers would have to be scanned, which means adding other frameworks. Email addresses have not been collected yet, and some of the 22 will only offer a contact form.

A possible second segment: 8 of the 22 already have a plan that is overdue, outdated or unpublished. They have shown they will act, and an update is less work than a first plan.

## The 22 reachable prospects
| Supplier | Status | Detail |
|---|---|---|
| Bio&Me | No plan | Consumer brand |
| Chew Valley Dairy | No plan | Net zero wording only |
| Bentley Foodservice (Cramart) | No plan | |
| Crowndale Food Service | No plan | |
| IMS of Smithfield | No plan | |
| John Sheppard Butchers | No plan | Site content from 2015–16 |
| Moving Mountains Foods | No plan | Consumer brand |
| Ralph Livesey | No plan | No policy pages |
| Ribble Farm Fare | No plan | Sustainability page, no figures |
| Set Produce | No plan | 2020 environmental policy only |
| Sykes House Farm | No plan | |
| The Organic Pantry | No plan | |
| Town Head Farm Products (Dales Dairies) | No plan | |
| VFC Foods | No plan | Consumer brand |
| Middlesex Meat | Not published | "Contact us for a copy" |
| Braces Bakery | Outdated | May 2024, no Scope 3 |
| County Foods | Outdated | April 2024, baseline only |
| School Milk Services | Overdue | March 2025 |
| Tamar Fresh | Overdue | May 2025; own review date March 2026 |
| TPB Foods | Overdue | August 2025 |
| Clegg's Chilled Food Service | Overdue | September 2025 |
| Hallam Country Fresh Foods | Overdue | October 2025 |

Suppliers with a current plan (not prospects): AG Axton, Arthur Brett, Harlech, Freeman Catering Butchers, JR Holland, JR Wholesale Sussex, Johal Dairies, John Palin, Norfolk Catering, Owen Taylor, Prescott-Thomas, Reeves Butchers, W McClure.

## Method
1. `ops/crp_scan.py --limit 50` as written returned 49 `no_site`: its DuckDuckGo lookup was reset from the cloud shell. That run is kept in `research/e3-scan-results-raw-run1.csv` and is not a finding.
2. Websites found by checking likely domains directly and by web search (41 candidates; 35 working).
3. Script pass on the known sites (homepage, common paths, sitemap, up to 12 carbon-related links, PDF text).
4. Browser pass on every site where the script found nothing (navigation, footer, about and policy pages).
5. Every plan document opened and its publication date read, including scanned PDFs.
6. Sites unreachable from the shell retried from a second network; three stayed down.

The script alone matched the hand-verified status on only 29 of 50. It missed five published plans and called five old plans current, so its output should not be used without the browser pass and document check.

## Limits
- "No plan" means none signposted on the website. A plan held privately or buried in an unlinked file would be missed; procurement rules require it to be published and clearly signposted, so the website test is the right one.
- The five down sites and eight no-website suppliers are unverified either way and are excluded from the 22.
- One framework, 50 suppliers. The 44% figure has a wide margin at this sample size.

## Earlier interim check (superseded)
Eight suppliers checked by hand on 2026-11-27: three current (Raynor, Owen Taylor, Johal), one outdated (Braces), four none (Tiffin, Ribble Farm Fare, On a Roll, Set Produce). The five that fall in the first 50 (Owen Taylor, Johal, Braces, Ribble Farm Fare, Set Produce) were re-verified with the same result.
