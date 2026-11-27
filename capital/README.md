# CAPITAL: business workspace

Isolated workspace for the digital product business. Everything the operator needs to resume is in this folder.

| File | Purpose |
|---|---|
| `STATE.md` | Current position, backlog in priority order, blockers. Read first, update last, every cycle. |
| `ledger.csv` | Every real expense and every real sale. No estimates, no projections. |
| `OWNER_ACTIONS.md` | The only things that need the owner. |
| `research/` | Dated market evidence with sources. |
| `products/` | One folder per product: build script, tests, packaged output, store listing copy. |
| `site/` | Static marketing site. |

## Operating loop (each scheduled cycle)
1. `git fetch origin claude/wizardly-noether-26a3n7 && git checkout claude/wizardly-noether-26a3n7 && git pull`.
2. Read `STATE.md` and `OWNER_ACTIONS.md`.
3. Take the top backlog item that is not blocked. If everything is blocked on the owner, do research or product-quality work instead.
4. Do it, test it, record evidence.
5. Update `STATE.md` and `ledger.csv`, commit, push.
6. Notify the owner only for: a new owner action, a real sale, a cost decision, or a failure that needs them.

## Rules
- Spending allowance £0. Any cost goes in `OWNER_ACTIONS.md` first and is not incurred until approved.
- No publication, account creation, emails or posts on the owner's behalf without approval.
- Revenue is recorded only from a payment processor record. Demand claims need a source.
- Kill rule: a product with no sale after 60 days live and 300 landing-page visits is dropped or repositioned.

## Architecture
- Execution: Claude Code cloud session, woken by a scheduled task every 6 hours.
- Memory: this folder, on git branch `claude/wizardly-noether-26a3n7`. The container is disposable; the branch is the record.
- Research: web search (page fetches to arbitrary hosts are blocked by the environment's network policy).
- Not available to the operator: payment accounts, hosting accounts, marketplaces. Those belong to the owner.
