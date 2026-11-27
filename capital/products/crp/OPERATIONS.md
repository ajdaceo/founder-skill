# Carbon Reduction Plan service: how it runs

Status: design, with the calculation, checks and export built and tested. Nothing here is live. Prices and policies marked "proposed" need the owner's approval.

## Flow
| Step | Who | How |
|---|---|---|
| 1. Order | Client | Pays £249 by payment link or invoice (Stripe). Fixed price, no negotiation |
| 2. Data | Client | One web form (Tally), about 25 fields that map one-to-one to the generator's activities, each with a unit and an "estimate" tick box. Optional bill uploads |
| 3. Intake check | Agent | Reads the submission over the form's API and builds `client.json`. Missing or impossible values produce a templated email listing exactly what is needed |
| 4. Generation | Software | `build_crp.py`: plan, calculation record, QA result. Deterministic; no AI in the numbers |
| 5. Checks | Software, then owner | Four gates below. A plan with any blocking error is never issued |
| 6. Delivery | Agent | Email with PDF and Word plan, the calculation record, and a one-page note on signing, publishing and (optional) the NHS's free plan-checking service |
| 7. Revisions | Agent | One round of data corrections within 30 days included (proposed). Regenerated and rechecked the same way |
| 8. Renewal | Agent | Reminders at 10 and 11 months after publication. Update at a fixed price (proposed £149), last year's data pre-filled, baseline locked |

## The four checks before release
1. **Input rules (automatic, blocking).** Unknown activities, negative values, periods that are not 12 months, a missing factor for the year, Net Zero year after 2050, missing Scope 3 category without a reason, reporting period over 18 months old without an explanation, missing board approval date or signatory. These mirror the buyers' published pass/fail table.
2. **Reasonableness (automatic, needs client confirmation).** No electricity, no Scope 1, change of more than 40% from baseline, different year-ends, late publication. Each becomes a question to the client, not a silent guess.
3. **Release check (automatic, blocking).** `verify_outputs.py` re-adds the calculation record and compares it with the figures printed in the plan.
4. **Owner sign-off (human, logged).** About 10 minutes: read the QA summary and the plan, confirm nothing in the narrative goes beyond what the client supplied, approve. Reason: the owner is personally liable as a sole trader, insurers ask about human supervision, and the AI provider's terms put review on the operator. Proposed to move to sampling (one in five) after 20 clean deliveries.

## What the client is responsible for
The activity data, the completeness of sites covered, the targets and measures, and the director's approval and signature. The service states its method and factors, makes no assurance or verification claim, and never promises that a bid will pass.

## Fixed rules (proposed; no discretion for the agent)
- **Refunds:** full refund before work starts, or if the data supplied cannot produce a plan that passes checks 1 to 3. After delivery, errors of ours are corrected free within 5 working days.
- **Extra revisions:** £49 per further re-issue.
- **Turnaround:** 5 working days from complete data.
- **Escalate to owner:** complaint, refund outside the rule, legal or regulatory contact, suspected data breach, a client disputing a tender outcome.

## Data handling
- Business data only. The form asks for totals (for example total commuting distance), not staff names or addresses, and tells clients not to upload documents containing personal data.
- Client files must live in a private repository or storage, not this public fork. This is an owner setup action before the first order.
- Keep client inputs and outputs for 24 months to support the next renewal, then delete (proposed).
- Contact details of named people at clients and prospects are personal data: privacy notice on the website, opt-out honoured at once, suppression list kept.

## Owner time
- Setup: about 2 to 3 hours once (accounts, identity checks, terms approval).
- Per plan: about 10 minutes sign-off.
- Weekly: the usual report. At five plans a month this is under the 30 minutes a week target; at forty a month it is not, unless sign-off moves to sampling.

## Known gaps
- The enhanced "2027 NHS CRP" (frameworks and £5m+ contracts from 1 April 2027) is not built. It needs spend-based Scope 3 estimates and a global boundary. Until it is, framework suppliers can only be sold the standard plan for tenders that start before that date.
- No client has used the intake form; field wording is untested.
- The offer page, terms, privacy notice and engagement letter are not written. Terms need a solicitor's look at the liability cap.
