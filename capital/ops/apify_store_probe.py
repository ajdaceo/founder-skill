"""Query Apify's public store API for listings matching keywords and print demand figures."""
import json, sys, time, requests
out = {}
for kw in sys.argv[1:]:
    try:
        r = requests.get("https://api.apify.com/v2/store", params={"search": kw, "limit": 40, "sortBy": "popularity"}, timeout=40)
        items = r.json().get("data", {}).get("items", [])
    except Exception as e:
        print(kw, "ERR", type(e).__name__); continue
    rows = []
    for a in items:
        st = a.get("stats") or {}
        pi = a.get("currentPricingInfo") or {}
        rows.append({"kw": kw, "name": f"{a.get('username')}/{a.get('name')}", "title": (a.get("title") or "")[:60], "users30": st.get("totalUsers30Days"),
                     "users_all": st.get("totalUsers"), "runs30": (st.get("publicActorRunStats30Days") or {}).get("TOTAL"),
                     "rating": a.get("actorReviewRating"), "reviews": a.get("actorReviewCount"), "pricing": pi.get("pricingModel"), "modified": (st.get("lastRunStartedAt") or "")[:10]})
    out[kw] = rows
    tot = sum((x["users30"] or 0) for x in rows)
    print(f"\n== {kw}: {len(rows)} listings, users in last 30 days (sum) {tot}")
    for x in sorted(rows, key=lambda x: -(x["users30"] or 0))[:6]:
        print(f"   {x['users30'] or 0:>6} u30 | {x['users_all'] or 0:>7} all | {str(x['rating'])[:4]:>4}* ({x['reviews']}) | {str(x['pricing'])[:16]:16} | {x['name'][:42]:42} | {x['title']}")
    time.sleep(0.5)
json.dump(out, open("apify/store_probe.json", "w"))
