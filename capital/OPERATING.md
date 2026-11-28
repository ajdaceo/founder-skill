# How CAPITAL runs (from 2026-11-28, MANDATE-AMENDMENT-3.md)

One operator, one schedule (the existing "CAPITAL operator" task and owner chat sessions), one lock. No extra schedules or standing agents. Every run does the three functions in this order and stops when its usage is spent.

## 1. Active commercial experiments (first, every run)
- Records: `experiments/`. One file per experiment with hypothesis, customer, offer and price, channel, cost cap, exposure target, deadline, pass and fail lines, results, next decision.
- Order of work: customer obligations and replies; then the live experiment's next step; then preparing the next experiment.
- Default design: tens of hand-picked prospects, each message true and specific to that prospect, a real offer with a price, a result within 30 days. A cheap controlled test beats more desk research.
- Nothing is sent, published or spent outside an approved envelope. Approval requests are grouped in `OWNER_ACTIONS.md`.

## 2. Opportunity radar (weekly, capped)
- Record: `radar/RADAR.md` (watchlist and dated log).
- Once a week (first run on or after Monday), at most about ten lookups or one capped research agent. Add what changed, score it, and promote an item to an experiment only when a cheap test exists.
- Sources are not limited to earlier ideas: regulation and deadlines, procurement data, marketplace data, asset listings, platform rule changes, new technical capabilities, price gaps.

## 3. Simulated validation (background, one command when network allows)
- Record: `simulation/REGISTER.md`. Paper books and other zero-capital trials with fixed rules set in advance.
- No real money, leverage or financial account without the owner's separate explicit approval.

## Dashboard (last step of every run)
- `DASHBOARD.md` is the one place to see CAPITAL's position. Update it before releasing the lock, even if nothing changed: money from `ledger.csv` and processor records, pipeline counts from the experiment records, simulations from `simulation/`, new radar items, blockers, owner actions, next actions.
- Mark every figure as verified, estimate, assumption or untested. Keep it to one screen per section. Edit the file by hand; do not build tooling for it.
- If a file named `STOP` exists in this folder, take no outward action and say so on the dashboard.

## Capital
- Policy: `research/2026-11-28-capital-allocation-screen.md`. Validation tests are small and capped; scale follows a measured conversion number.
- The owner may fund an exceptional opportunity, including an asset purchase, on evidence and separate approval. Do not assume purchases must wait for retained profit; do not assume funding either.

## Limits that do not change
Fixed prices, no negotiation or discretionary refunds; limited companies and LLPs only for unsolicited email, with sender identity, opt-out and AI disclosure; revenue recorded only from processor records; no customer data in this public repository.

## Model allocation (owner instruction 2026-11-28)
The aim is to spend the expensive models only where judgement decides the outcome.

| Work | Model | Set by |
|---|---|---|
| The scheduled operator: every routine run | Sonnet | The scheduled task's model setting (changed to Sonnet on 2026-11-28) |
| Subagents that fetch, extract, check, classify or reformat | Haiku | The operator, per subagent |
| Subagents that research across several sources or draft customer text | Sonnet | The operator, per subagent |
| One Opus subagent, at most once per run, for the decisions listed below | Opus | The operator, per subagent |
| Sessions the owner opens | The owner's choice in the model picker: Sonnet for check-ins and set-up; Opus or Fable for the decisions listed below | The owner |

Decisions that justify Opus or Fable: a first external message pack or new commercial terms; a legal, regulatory or provider-terms judgement with real downside; a complaint, dispute or other incident; a go or no-go on an experiment; the monthly review. Everything else stays on Sonnet or Haiku. Never start a Fable subagent. Every subagent brief carries a cap on tool calls.

## Two environments, two jobs
- `capital-ops`: holds the mailbox and payment credentials and reaches twelve named hosts only. Customer-facing work runs here.
- Default: open web, no credentials. Jobs that must read arbitrary websites (for example `ops/E6-RECHECK.md`) run here. A session that browses the open web never holds credentials.
