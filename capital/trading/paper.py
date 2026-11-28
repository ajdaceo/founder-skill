"""Paper trading only. No orders are placed and no account is touched. Records what the validated rules would hold.

Usage: python3 paper.py DATA_DIR        (after: python3 fetch_data.py DATA_DIR)
Keeps paper/state.json (positions) and appends to paper/ledger.csv on every run.

Books (notional, in the instruments' own currency, treated as 1,000 units each at the start):
  A  five asset-class funds, each held only when above its 10-month average (checked at each month-end), else cash fund SHV.
  B  Bitcoin and Ether, each held only when above its 50-day average (the length chosen on 2018-2021 data), else cash at 0%.
Costs charged on every switch: A 0.1% a side (two sides per switch), B 0.26% a side.
"""
import csv
import datetime as dt
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
PAPER = os.path.join(HERE, "paper")
A_ASSETS, B_ASSETS = ("SPY", "EFA", "IEF", "VNQ", "DBC"), ("BTCUSDT", "ETHUSDT")
A_COST, B_COST, B_N, START = 0.001, 0.0026, 50, 1000.0


def read(path, col):
    return [(r["date"], float(r[col])) for r in csv.DictReader(open(path)) if r.get(col) not in (None, "")]


def a_signal(series):
    """(signal, month label, price, average) from the last completed month."""
    me = {}
    for d, v in series:
        me[d[:7]] = (d, v)
    months = sorted(me)[:-1]  # ignore the current, incomplete month
    last10 = [me[m][1] for m in months[-10:]]
    d, v = me[months[-1]]
    return v > sum(last10) / 10, months[-1], v, sum(last10) / 10


def b_signal(series):
    closes = [v for _, v in series[:-1]]  # ignore today's incomplete bar
    d = series[-2][0]
    avg = sum(closes[-B_N:]) / B_N
    return closes[-1] > avg, d, closes[-1], avg


def main(data_dir):
    os.makedirs(PAPER, exist_ok=True)
    sp = os.path.join(PAPER, "state.json")
    state = json.load(open(sp)) if os.path.exists(sp) else {"started": dt.date.today().isoformat(), "slots": {}}
    rows = []
    latest = {a: read(os.path.join(data_dir, f"{a}.csv"), "adjclose") for a in A_ASSETS + ("SHV",)}
    latest.update({a: read(os.path.join(data_dir, f"{a}.csv"), "close") for a in B_ASSETS})
    cash_px = latest["SHV"][-1][1]
    for book, assets, cost, sides in (("A", A_ASSETS, A_COST, 2), ("B", B_ASSETS, B_COST, 1)):
        for a in assets:
            sig, asof, px_sig, avg = a_signal(latest[a]) if book == "A" else b_signal(latest[a])
            px_now = latest[a][-1][1]
            key = f"{book}:{a}"
            slot = state["slots"].get(key)
            if slot is None:  # first run: start each slot with an equal share of the book
                slot = {"value": START / len(assets), "in_market": None, "ref_px": px_now, "ref_cash": cash_px, "last_signal_asof": ""}
            # mark to market since the last run
            if slot["in_market"]:
                slot["value"] *= px_now / slot["ref_px"]
            elif slot["in_market"] is False and book == "A":
                slot["value"] *= cash_px / slot["ref_cash"]
            # act on a new signal (book A only once per completed month)
            action = "hold"
            if slot["in_market"] is None or (sig != slot["in_market"] and asof != slot["last_signal_asof"]):
                first = slot["in_market"] is None
                slot["value"] *= 1 - cost * (1 if first and not sig and book == "B" else sides if not first else (1 if sig or book == "A" else 0))
                slot["in_market"] = sig
                action = "enter" if sig else "exit to cash"
            slot["last_signal_asof"] = asof
            slot["ref_px"], slot["ref_cash"] = px_now, cash_px
            state["slots"][key] = slot
            rows.append({"run_date": dt.date.today().isoformat(), "book": book, "instrument": a, "signal_as_of": asof, "price_at_signal": round(px_sig, 4),
                         "average": round(avg, 4), "signal": "in" if sig else "out", "action": action, "last_price_date": latest[a][-1][0],
                         "last_price": round(px_now, 4), "paper_value": round(slot["value"], 2)})
    for book in ("A", "B"):
        total = sum(s["value"] for k, s in state["slots"].items() if k.startswith(book))
        rows.append({"run_date": dt.date.today().isoformat(), "book": book, "instrument": "TOTAL", "paper_value": round(total, 2)})
    json.dump(state, open(sp, "w"), indent=1)
    lp = os.path.join(PAPER, "ledger.csv")
    new = not os.path.exists(lp)
    fields = ["run_date", "book", "instrument", "signal_as_of", "price_at_signal", "average", "signal", "action", "last_price_date", "last_price", "paper_value"]
    with open(lp, "a", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        if new:
            w.writeheader()
        w.writerows(rows)
    for r in rows:
        print(r["book"], f"{r['instrument']:8}", r.get("signal", ""), r.get("action", ""), r["paper_value"])


if __name__ == "__main__":
    main(sys.argv[1])
