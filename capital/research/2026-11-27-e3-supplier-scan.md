# E3 supplier scan — interim (2026-11-27 ~23:00 UTC)

Source list: research/e3-prospects-nhs-food-framework.csv (80 SMEs, NHS Supply Chain Fresh & Food to Go framework, FTS 026675-2024).
In-scope test: all are NHS Supply Chain framework suppliers -> Evergreen Level 1 (published CRP) required for NHS SC tenders since 6 Apr 2026.

## Checked so far (8 SMEs, direct website check)
| Supplier | Result | Evidence |
|---|---|---|
| Raynor Foods | CRP current (2026) | site footer |
| Owen Taylor & Sons | CRP current (May 2026) | /wp-content/uploads/2026/06/Appendix-13-Carbon-Reduction-Plan-Owen-Taylor-May-26-v1.1.pdf |
| Johal Dairies | CRP current (reporting year 2025, Jul 2026) | /wp-content/uploads/2026/07/Reporting-Year-2025-July-2026.pdf |
| Braces Bakery | CRP OUTDATED (2024) | /wp-content/uploads/Carbon-reduction-plan-2024.pdf |
| Tiffin Sandwiches | No compliant CRP (Scope 2 target only + certificate) | site |
| Ribble Farm Fare | No CRP found | site |
| On a Roll Sandwich Co | No CRP found | homepage |
| Set Produce | No CRP found (2020 environmental policy only) | homepage |
Not SME / excluded: Freshways (no CRP found), Creamline & PFD (have CRPs).
Unreachable by fetch tool: Cleggs, Sandwich King (robots unreachable).

## Interim counts
- 5 of 8 (62%) lack a current CRP (4 none + 1 outdated). Above the 40% threshold, but n=8 — NOT yet decision-grade.
- 3 of 8 already have consultant-grade CRPs: incumbents exist; outdated plans (annual update rule) are a repeat-revenue angle.

## Feasibility (confirmed)
Self-certified Annex A template, director sign-off, no accreditation/verification. Client supplies data (energy bills, fuel, mileage); we compute with DESNZ factors. Liability: accuracy of calculation only; client signs declaration. Needs a clear engagement letter + PI-style disclaimer.

## Blocker
Web fetch to new domains needs per-URL approval in this session; shell network still 403 (proxy allowlist). Remaining 42 checks: ops/crp_scan.py once network allows, or approve fetches.
