# Simulated validation register

Zero capital. Rules are fixed before results are seen. No real money, leverage or account access without the owner's separate explicit approval.

| ID | What | Rule | Started | Where | Review |
|---|---|---|---|---|---|
| S1 | Five asset-class funds, trend rule | Hold each only above its 10-month average, else cash; 0.1% cost a side | 2026-11-28 | `trading/paper/ledger.csv` (book A) | Quarterly: compare with holding the same assets |
| S2 | Bitcoin and Ether, trend rule | Hold each only above its 50-day average, else cash; 0.26% cost a side | 2026-11-28 | `trading/paper/ledger.csv` (book B) | Quarterly; stays on paper until at least two more years agree with the backtest |
| S3 | Asset watch | Each month record up to ten small assets for sale with stated revenue and price; re-check monthly whether each sold, was repriced or vanished. Judge: would a "buy" call made on listing day have held up? | 2026-11-28 | `simulation/asset-watch.csv` | After three monthly checks |

How to update S1 and S2 (needs network): `python3 trading/fetch_data.py <dir>` then `python3 trading/paper.py <dir>`; commit `trading/paper/`.
