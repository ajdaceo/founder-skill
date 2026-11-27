"""E3 supplier scan: does each prospect publish a Carbon Reduction Plan?

Usage: python3 crp_scan.py research/e3-prospects-nhs-food-framework.csv research/e3-scan-results.csv [--limit 50]
Needs open outbound network (cloud environment "Full"). Read-only: GET requests only, polite delays.
Method per supplier:
  1. Find website: DuckDuckGo HTML search "<name> <town>" -> first result whose domain isn't a directory/news site.
  2. Fetch homepage + common paths; collect links whose text/href mentions carbon/CRP/net zero/PPN/sustainab.
  3. Fetch up to 6 candidate pages/PDF links; classify:
     crp_current  - document/page titled Carbon Reduction Plan (or PPN 06/21 / PPN 006) with a 2025/2026 date
     crp_outdated - CRP found but latest year seen <= 2024
     no_crp       - website found, no CRP found
     no_site      - website not found (manual check needed)
Every row records the evidence URL so a human can verify.
"""
import csv
import re
import sys
import time
import urllib.parse

import requests

UA = {"User-Agent": "Mozilla/5.0 (CAPITAL research; read-only)"}
SKIP = ("duckduckgo", "linkedin", "facebook", "twitter", "x.com", "instagram", "endole", "companieshouse",
        "company-information", "find-tender", "contractsfinder", "laca.co.uk", "tuco.ac.uk", "yell.com",
        "thecafelife", "sandwich.org.uk", "trustpilot", "wikipedia", "gov.uk", "nhs.uk", "dnb.com",
        "rekki", "bouncewatch", "prospeo", "ditchcarbon", "issuu", "youtube", "google.")
PATHS = ["", "sustainability", "sustainability/", "environment", "environmental-policy", "carbon-reduction-plan",
         "net-zero", "policies", "about", "about-us"]
KEY = re.compile(r"carbon|crp|net[\s-]?zero|ppn|sustainab|environment", re.I)
CRP = re.compile(r"carbon\s+reduction\s+plan|ppn\s*0?6/?21|ppn\s*006", re.I)
YEAR = re.compile(r"20(1[8-9]|2[0-9])")


def get(url, timeout=15):
    try:
        r = requests.get(url, headers=UA, timeout=timeout, allow_redirects=True)
        if r.status_code == 200:
            return r
    except requests.RequestException:
        pass
    return None


def find_site(name, town):
    q = urllib.parse.quote_plus(f"{name} {town}")
    r = get(f"https://html.duckduckgo.com/html/?q={q}")
    if not r:
        return None
    for href in re.findall(r'class="result__a" href="([^"]+)"', r.text):
        if "uddg=" in href:
            href = urllib.parse.unquote(href.split("uddg=")[1].split("&")[0])
        dom = urllib.parse.urlparse(href).netloc.lower()
        if dom and not any(s in dom for s in SKIP):
            return f"{urllib.parse.urlparse(href).scheme}://{dom}/"
    return None


def candidates(base):
    found, seen = [], set()
    for p in PATHS:
        r = get(urllib.parse.urljoin(base, p))
        time.sleep(0.5)
        if not r or "html" not in r.headers.get("content-type", ""):
            continue
        if CRP.search(r.text):
            found.append((r.url, r.text))
        for href, text in re.findall(r'<a[^>]+href="([^"#]+)"[^>]*>(.*?)</a>', r.text, re.I | re.S):
            u = urllib.parse.urljoin(r.url, href)
            if u not in seen and (KEY.search(href) or KEY.search(text)):
                seen.add(u)
        if p == "" and not seen:
            continue
    return found, list(seen)[:6]


def classify(base):
    found, links = candidates(base)
    evidence = [u for u, _ in found]
    years = []
    for u in links:
        r = get(u)
        time.sleep(0.5)
        if not r:
            continue
        body = r.text if "html" in r.headers.get("content-type", "") else u  # PDFs: rely on URL/title
        if CRP.search(body) or CRP.search(u.replace("-", " ")):
            evidence.append(u)
            years += [int("20" + y) for y in YEAR.findall(u + " " + body[:20000])]
    for _, text in found:
        years += [int("20" + y) for y in YEAR.findall(text[:20000])]
    if not evidence:
        return "no_crp", "", ""
    latest = max(years) if years else ""
    status = "crp_current" if latest and latest >= 2025 else "crp_outdated" if latest else "crp_undated"
    return status, evidence[0], latest


def main(src, dst, limit):
    rows = list(csv.DictReader(open(src)))[:limit]
    out = []
    for i, row in enumerate(rows, 1):
        site = find_site(row["supplier"], row["town"])
        time.sleep(1.5)
        if not site:
            out.append({**row, "website": "", "status": "no_site", "evidence": "", "latest_year": ""})
        else:
            status, ev, yr = classify(site)
            out.append({**row, "website": site, "status": status, "evidence": ev, "latest_year": yr})
        print(i, row["supplier"], out[-1]["status"], out[-1]["website"], flush=True)
    with open(dst, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(out[0].keys()))
        w.writeheader()
        w.writerows(out)
    counts = {}
    for r in out:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print("COUNTS", counts)


if __name__ == "__main__":
    limit = int(sys.argv[sys.argv.index("--limit") + 1]) if "--limit" in sys.argv else 50
    main(sys.argv[1], sys.argv[2], limit)
