"""E3 supplier scan: does each prospect publish a Carbon Reduction Plan?

Usage: python3 crp_scan.py research/e3-prospects-nhs-food-framework.csv research/e3-scan-results.csv [--limit 50] [--workers 6]
Needs open outbound network (cloud environment "Full"). Read-only: GET requests only, polite delays.
Method per supplier:
  1. Website: use the input CSV's optional `website` column if filled; otherwise DuckDuckGo HTML search
     "<name> <town>" -> first result whose domain isn't a directory/news site. (DuckDuckGo was unreachable
     from the cloud shell on 2026-11-27, so fill `website` by hand.)
  2. Fetch homepage + common paths + sitemap(s); collect links whose text/href mentions
     carbon/CRP/net zero/PPN/sustainab/environment. Links that mention carbon/CRP/net zero/PPN are checked first.
  3. Fetch up to 12 candidate pages/PDF links (PDF text via pdftotext); classify:
     crp_current  - document/page titled Carbon Reduction Plan (or PPN 06/21 / PPN 006) with a 2025/2026 date
     crp_outdated - CRP found but latest year seen <= 2024
     no_crp       - website found, no CRP found
     no_site      - website not found (manual check needed)
     site_error   - website given but homepage did not return 200 (manual check needed)
Every row records the evidence URL so a human can verify. This is a FIRST PASS: "latest year" can pick up a
footer copyright year, and a blocked or script-rendered site can hide a plan. Verify every row by hand.
Measured 2026-11-27 on 50 suppliers: the first pass matched the hand-verified status on 29 of 50. It missed 5
published plans (footer or script-rendered links, user-agent blocks) and called 5 old plans current.
"""
import concurrent.futures
import csv
import re
import subprocess
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
STRONG = re.compile(r"carbon|crp|net[\s-]?zero|ppn", re.I)
YEAR = re.compile(r"20(1[8-9]|2[0-9])")
MAX_LINKS = 12


def body_text(r):
    """Text of a response; PDFs are converted with pdftotext (first 6 pages)."""
    ctype = r.headers.get("content-type", "")
    if "pdf" in ctype or r.url.lower().split("?")[0].endswith(".pdf"):
        try:
            out = subprocess.run(["pdftotext", "-l", "6", "-", "-"], input=r.content, capture_output=True, timeout=30)
            return out.stdout.decode("utf-8", "ignore")
        except (OSError, subprocess.SubprocessError):
            return ""
    return r.text if "html" in ctype or "xml" in ctype or "text" in ctype else ""


def sitemap_links(base):
    """URLs from sitemap.xml / wp-sitemap.xml (one level of nesting) whose path matches KEY."""
    out, queue, seen = [], [urllib.parse.urljoin(base, p) for p in ("sitemap.xml", "wp-sitemap.xml", "sitemap_index.xml")], set()
    while queue and len(seen) < 12:
        u = queue.pop(0)
        if u in seen:
            continue
        seen.add(u)
        r = get(u)
        time.sleep(0.3)
        if not r or "<loc>" not in r.text:
            continue
        for loc in re.findall(r"<loc>\s*([^<\s]+)\s*</loc>", r.text):
            if loc.lower().split("?")[0].endswith(".xml"):
                queue.append(loc)
            elif KEY.search(urllib.parse.urlparse(loc).path):
                out.append(loc)
    return out


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
    found, seen = [], {}
    for p in PATHS:
        r = get(urllib.parse.urljoin(base, p))
        time.sleep(0.5)
        if not r or "html" not in r.headers.get("content-type", ""):
            continue
        if CRP.search(r.text):
            found.append((r.url, r.text))
        for href, text in re.findall(r'<a[^>]+href=["\']([^"\'#]+)["\'][^>]*>(.*?)</a>', r.text, re.I | re.S):
            if href.lower().startswith(("mailto:", "tel:", "javascript:")):
                continue
            u = urllib.parse.urljoin(r.url, href)
            if u not in seen and (KEY.search(href) or KEY.search(text)):
                seen[u] = bool(STRONG.search(href) or STRONG.search(text))
    for u in sitemap_links(base):
        seen.setdefault(u, bool(STRONG.search(u)))
    ordered = sorted(seen, key=lambda u: (not seen[u], u))  # carbon/CRP/net-zero/PPN links first, then stable order
    return found, ordered[:MAX_LINKS], len(ordered)


def classify(base):
    if not get(base):
        return "site_error", "", "", 0
    found, links, n_links = candidates(base)
    evidence = [u for u, _ in found]
    years = []
    for u in links:
        r = get(u, timeout=25)
        time.sleep(0.5)
        if not r:
            continue
        body = body_text(r)
        if CRP.search(body) or CRP.search(urllib.parse.unquote(u).replace("-", " ").replace("_", " ")):
            evidence.append(u)
            years += [int("20" + y) for y in YEAR.findall(u + " " + body[:20000])]
    for _, text in found:
        years += [int("20" + y) for y in YEAR.findall(text[:20000])]
    evidence = list(dict.fromkeys(evidence))
    if not evidence:
        return "no_crp", "", "", n_links
    latest = max(years) if years else ""
    status = "crp_current" if latest and latest >= 2025 else "crp_outdated" if latest else "crp_undated"
    return status, " ; ".join(evidence[:4]), latest, n_links


def scan_row(row):
    site = (row.get("website") or "").strip()
    if not site:
        site = find_site(row["supplier"], row["town"]) or ""
        time.sleep(1.5)
    if not site:
        res = {"website": "", "status": "no_site", "evidence": "", "latest_year": "", "links_seen": 0}
    else:
        status, ev, yr, n = classify(site)
        res = {"website": site, "status": status, "evidence": ev, "latest_year": yr, "links_seen": n}
    return {**row, **res}


def main(src, dst, limit, workers=1):
    rows = list(csv.DictReader(open(src)))[:limit]
    out = []
    # One supplier = one host, so parallel workers never hit the same site at once.
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        for i, res in enumerate(pool.map(scan_row, rows), 1):
            out.append(res)
            print(i, res["supplier"], res["status"], res["website"], res["evidence"][:90], flush=True)
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
    workers = int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 1
    main(sys.argv[1], sys.argv[2], limit, workers)
