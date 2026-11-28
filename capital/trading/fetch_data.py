"""Fetch daily history for backtests. ETFs: Yahoo chart API (adjusted close). Crypto: Binance public data API (daily klines)."""
import csv, json, sys, time, datetime as dt, requests
out = sys.argv[1]
UA = {"User-Agent": "Mozilla/5.0 (research; read-only)"}
def yahoo(sym):
    r = requests.get(f"https://query1.finance.yahoo.com/v8/finance/chart/{sym}", params={"period1": 0, "period2": 9999999999, "interval": "1d", "events": "div,splits"}, headers=UA, timeout=60)
    r.raise_for_status()
    res = r.json()["chart"]["result"][0]
    ts, adj, close = res["timestamp"], res["indicators"]["adjclose"][0]["adjclose"], res["indicators"]["quote"][0]["close"]
    rows = [(dt.datetime.utcfromtimestamp(t).date().isoformat(), a, c) for t, a, c in zip(ts, adj, close) if a is not None]
    with open(f"{out}/{sym}.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["date", "adjclose", "close"]); w.writerows(rows)
    return len(rows), rows[0][0], rows[-1][0]
def binance(sym):
    rows, start = [], 1500000000000
    while True:
        r = requests.get("https://data-api.binance.vision/api/v3/klines", params={"symbol": sym, "interval": "1d", "limit": 1000, "startTime": start}, headers=UA, timeout=60)
        r.raise_for_status()
        k = r.json()
        if not k: break
        rows += [(dt.datetime.utcfromtimestamp(x[0] / 1000).date().isoformat(), float(x[4]), float(x[5])) for x in k]
        if len(k) < 1000: break
        start = k[-1][0] + 86400000
        time.sleep(0.3)
    with open(f"{out}/{sym}.csv", "w", newline="") as f:
        w = csv.writer(f); w.writerow(["date", "close", "volume"]); w.writerows(rows)
    return len(rows), rows[0][0], rows[-1][0]
for sym in ("SPY", "EFA", "EEM", "IEF", "TLT", "GLD", "VNQ", "DBC", "SHV", "VT", "BND"):
    try: print(sym, yahoo(sym))
    except Exception as e: print(sym, "ERR", type(e).__name__, str(e)[:80])
    time.sleep(0.6)
for sym in ("BTCUSDT", "ETHUSDT"):
    try: print(sym, binance(sym))
    except Exception as e: print(sym, "ERR", type(e).__name__, str(e)[:80])
