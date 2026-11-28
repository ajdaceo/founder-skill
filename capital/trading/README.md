# Trading: validation and paper trading only

No real money is traded, no leverage is used and no financial account is accessed. That needs the owner's separate explicit approval (MANDATE-AMENDMENT-2.md).

- `fetch_data.py DATA_DIR`: daily history (funds from Yahoo's chart data, crypto from Binance's public data).
- `backtest.py DATA_DIR`: two published rules with costs and out-of-sample periods. Results of the 2026-11-28 run are in `backtest-results-2026-11-28.json`.
- `paper.py DATA_DIR`: appends to `paper/ledger.csv` what the rules would hold now (notional 1,000 units per book). Run it after `fetch_data.py` whenever network access allows; weekly is enough.

## Results (2026-11-28)
**A. Hold each of five asset classes only when above its 10-month average, else cash** (rule published 2007; everything tested is after publication; February 2007 to October 2026; 0.1% cost a side):

| | Return a year | Worst peak-to-trough fall | Risk-adjusted (Sharpe) |
|---|---|---|---|
| Timing rule | 5.0% | -12% | 0.53 |
| Same assets, always held | 6.0% | -43% | 0.41 |
| 60% US shares, 40% bonds | 8.1% | -29% | 0.70 |
| US shares only | 10.8% | -51% | 0.64 |
| Cash fund | 1.6% | 0% | |

Worst calendar year for the rule: -5.7% (2022). Five losing years in twenty. At 0.5% cost a side the return falls to 3.5% a year. The rule gives up about one point of return a year to cut the worst fall by three quarters.

**B. Hold Bitcoin or Ether only when above its N-day average, else cash** (N chosen on 2018 to 2021; judged on January 2022 to November 2026):

| | Cost a side | Return a year | Worst fall | Always held |
|---|---|---|---|---|
| Bitcoin, N=50 (chosen) | 0.26% | 17.1% | -52% | 5.5% a year, -67% |
| Bitcoin, N=50 | 0.6% | 9.0% | -56% | |
| Ether, N=50 (chosen) | 0.26% | 23.0% | -39% | -14.8% a year, -74% |
| Ether, N=50 | 0.6% | 16.2% | -42% | |
| Ether, N=100 (not chosen) | 0.26% | 1.0% | -53% | |

Fragile: a different averaging length on Ether erases the gain. Under five years of out-of-sample data cannot separate this from luck (the uncertainty on the risk-adjusted figure is about as large as the figure).

## Reading
- Neither rule creates capital at CAPITAL's scale. On 1,000 units, rule A averages about +50 a year with a worst fall of about -116. Rule B might average +90 to +230 with falls of -400 to -560.
- Rule A is a candidate treasury policy for retained profits later: modest return, small drawdowns, a few trades a year.
- Rule B stays on paper until much more evidence exists.
- Practical route if ever approved: a share-dealing account with an API and a practice mode inside an ISA. UK retail customers cannot trade crypto derivatives. See `research/mechanisms/trading.txt`.
