"""Historical validation of two published, rule-based strategies with costs and out-of-sample periods.
No money is traded. Usage: python3 backtest.py DATA_DIR [--json out.json]
DATA_DIR holds daily CSVs made by fetch_data.py: ETF files with date,adjclose,close; crypto files with date,close,volume.

Strategy A: "10-month moving average" timing (Faber 2007, written 2006) on five asset classes held as funds:
  US shares (SPY), other developed shares (EFA), US government bonds (IEF), property (VNQ), commodities (DBC).
  Each month-end: hold an asset next month only if its price is above its 10-month average, else hold cash (SHV).
  Equal weights. Everything after the rule's publication is out of sample: test window February 2007 onward.
Strategy B: price above its N-day average on Bitcoin and Ether (daily), else cash at 0%.
  N is chosen on data to end-2021 only and then judged on 2022 onward.
Rules were fixed before looking at results; every tested variant is reported, not only the best.
"""
import csv
import json
import math
import os
import sys


def read(path, col):
    out = []
    for r in csv.DictReader(open(path)):
        try:
            out.append((r["date"], float(r[col])))
        except (ValueError, KeyError):
            pass
    return out


def stats(returns, periods_per_year, rf=None):
    """returns: list of periodic simple returns; rf: matching list of cash returns or None (0)."""
    if not returns:
        return {}
    eq, peak, mdd = 1.0, 1.0, 0.0
    for r in returns:
        eq *= 1 + r
        peak = max(peak, eq)
        mdd = min(mdd, eq / peak - 1)
    n = len(returns)
    years = n / periods_per_year
    cagr = eq ** (1 / years) - 1
    ex = [r - (rf[i] if rf else 0.0) for i, r in enumerate(returns)]
    mean = sum(ex) / n
    var = sum((x - mean) ** 2 for x in ex) / (n - 1) if n > 1 else 0.0
    vol = math.sqrt(var) * math.sqrt(periods_per_year)
    sharpe = (mean * periods_per_year / vol) if vol else 0.0
    return {"years": round(years, 1), "total_return": round(eq - 1, 3), "cagr": round(cagr, 4), "vol": round(vol, 4), "sharpe": round(sharpe, 2), "max_drawdown": round(mdd, 4)}


# ---------- Strategy A ----------
def month_ends(series):
    out = {}
    for d, v in series:
        out[d[:7]] = v  # last trading day of the month wins
    return out


def strategy_a(data_dir, cost, start="2007-02", assets=("SPY", "EFA", "IEF", "VNQ", "DBC"), window=10):
    px = {a: month_ends(read(os.path.join(data_dir, f"{a}.csv"), "adjclose")) for a in assets}
    cash = month_ends(read(os.path.join(data_dir, "SHV.csv"), "adjclose"))
    months = sorted(set.intersection(*[set(p) for p in px.values()]))
    months = months[:-1]  # drop the current, incomplete month
    w = 1.0 / len(assets)
    strat, hold, cashr, labels, switches, in_market = [], [], [], [], 0, 0
    prev_sig = {a: None for a in assets}
    for i in range(window - 1, len(months) - 1):
        m, nxt = months[i], months[i + 1]
        if nxt < start:
            for a in assets:
                prev_sig[a] = px[a][m] > sum(px[a][months[j]] for j in range(i - window + 1, i + 1)) / window
            continue
        rc = (cash[nxt] / cash[m] - 1) if m in cash and nxt in cash else 0.0
        r_s = r_h = 0.0
        for a in assets:
            sig = px[a][m] > sum(px[a][months[j]] for j in range(i - window + 1, i + 1)) / window
            ra = px[a][nxt] / px[a][m] - 1
            r_h += w * ra
            r_s += w * (ra if sig else rc)
            if prev_sig[a] is not None and sig != prev_sig[a]:
                r_s -= w * cost * 2  # sell one holding and buy the other
                switches += 1
            prev_sig[a] = sig
            in_market += sig
        strat.append(r_s); hold.append(r_h); cashr.append(rc); labels.append(nxt)
    spy = [px["SPY"][labels[i]] / px["SPY"][months[months.index(labels[i]) - 1]] - 1 for i in range(len(labels))]
    ief = [px["IEF"][labels[i]] / px["IEF"][months[months.index(labels[i]) - 1]] - 1 for i in range(len(labels))]
    sixty = [0.6 * a + 0.4 * b for a, b in zip(spy, ief)]
    res = {"window": f"{labels[0]} to {labels[-1]}", "cost_per_side": cost,
           "timing": stats(strat, 12, cashr), "same_assets_buy_and_hold": stats(hold, 12, cashr),
           "us_shares_buy_and_hold": stats(spy, 12, cashr), "sixty_forty": stats(sixty, 12, cashr), "cash": stats(cashr, 12),
           "switches_per_year": round(switches / (len(labels) / 12), 1), "share_of_time_invested": round(in_market / (len(labels) * len(assets)), 2)}
    by_year = {}
    for lab, r in zip(labels, strat):
        by_year[lab[:4]] = (1 + by_year.get(lab[:4], 0.0)) * (1 + r) - 1
    res["timing_worst_year"] = min(by_year.items(), key=lambda kv: kv[1])
    res["timing_best_year"] = max(by_year.items(), key=lambda kv: kv[1])
    res["timing_losing_years"] = sum(1 for v in by_year.values() if v < 0)
    res["timing_by_period"] = {name: stats([r for lab, r in zip(labels, strat) if a <= lab[:4] <= b], 12, [c for lab, c in zip(labels, cashr) if a <= lab[:4] <= b])
                               for name, a, b in (("2007-2012", "2007", "2012"), ("2013-2019", "2013", "2019"), ("2020-2026", "2020", "2026"))}
    res["hold_by_period"] = {name: stats([r for lab, r in zip(labels, hold) if a <= lab[:4] <= b], 12, [c for lab, c in zip(labels, cashr) if a <= lab[:4] <= b])
                             for name, a, b in (("2007-2012", "2007", "2012"), ("2013-2019", "2013", "2019"), ("2020-2026", "2020", "2026"))}
    return res


# ---------- Strategy B ----------
def strategy_b(series, n, cost, start, end):
    dates = [d for d, _ in series]
    px = [v for _, v in series]
    strat, hold, pos, trades, days_in = [], [], 0, 0, 0
    for i in range(n, len(px) - 1):
        d_next = dates[i + 1]
        sig = 1 if px[i] > sum(px[i - n + 1:i + 1]) / n else 0
        if d_next < start or d_next > end:
            pos = sig
            continue
        r = px[i + 1] / px[i] - 1
        rs = r * sig
        if sig != pos:
            rs -= cost
            trades += 1
        pos = sig
        days_in += sig
        strat.append(rs); hold.append(r)
    if not strat:
        return {}
    s = stats(strat, 365)
    s.update({"trades_per_year": round(trades / (len(strat) / 365), 1), "share_of_time_invested": round(days_in / len(strat), 2),
              "buy_and_hold": stats(hold, 365)})
    return s


def run(data_dir):
    out = {"A": {}, "B": {}}
    for cost in (0.001, 0.005):
        out["A"][f"cost_{cost}"] = strategy_a(data_dir, cost)
    for sym in ("BTCUSDT", "ETHUSDT"):
        series = read(os.path.join(data_dir, f"{sym}.csv"), "close")
        block = {}
        for cost in (0.0026, 0.006):
            ins = {n: strategy_b(series, n, cost, "2018-03-05", "2021-12-31") for n in (50, 100, 200)}
            oos = {n: strategy_b(series, n, cost, "2022-01-01", "2099-12-31") for n in (50, 100, 200)}
            chosen = max(ins, key=lambda n: ins[n].get("sharpe", -9))
            block[f"cost_{cost}"] = {"in_sample_2018_2021": ins, "chosen_on_in_sample": chosen, "out_of_sample_2022_on": oos,
                                     "data_through": series[-1][0]}
        out["B"][sym] = block
    return out


if __name__ == "__main__":
    res = run(sys.argv[1])
    if "--json" in sys.argv:
        json.dump(res, open(sys.argv[sys.argv.index("--json") + 1], "w"), indent=1)
    a = res["A"]["cost_0.001"]
    print("A. 10-month timing, five asset classes,", a["window"], "(cost 0.1% a side)")
    for k in ("timing", "same_assets_buy_and_hold", "sixty_forty", "us_shares_buy_and_hold", "cash"):
        print(f"   {k:26} {a[k]}")
    print("   switches/yr", a["switches_per_year"], "| invested", a["share_of_time_invested"], "| worst year", a["timing_worst_year"], "| best", a["timing_best_year"], "| losing years", a["timing_losing_years"])
    for p in a["timing_by_period"]:
        print(f"   {p}: timing {a['timing_by_period'][p]['cagr']:.1%} (dd {a['timing_by_period'][p]['max_drawdown']:.0%}) vs hold {a['hold_by_period'][p]['cagr']:.1%} (dd {a['hold_by_period'][p]['max_drawdown']:.0%})")
    print("   at 0.5% a side: timing", res["A"]["cost_0.005"]["timing"])
    for sym, block in res["B"].items():
        for ck, b in block.items():
            n = b["chosen_on_in_sample"]
            print(f"B. {sym} {ck}: chosen N={n} on 2018-2021 (in-sample Sharpe {b['in_sample_2018_2021'][n]['sharpe']}); data to {b['data_through']}")
            for m in (50, 100, 200):
                o = b["out_of_sample_2022_on"][m]
                print(f"   out of sample N={m}: CAGR {o['cagr']:.1%} vol {o['vol']:.0%} Sharpe {o['sharpe']} maxDD {o['max_drawdown']:.0%} trades/yr {o['trades_per_year']} invested {o['share_of_time_invested']} | hold: CAGR {o['buy_and_hold']['cagr']:.1%} Sharpe {o['buy_and_hold']['sharpe']} maxDD {o['buy_and_hold']['max_drawdown']:.0%}")
