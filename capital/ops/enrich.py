"""Enrich candidate suppliers with Companies House facts and a verified website.

Usage: python3 enrich.py candidates.csv out.csv [--workers 10]
Input columns used: id, supplier, coh (company number, may be blank), town, postcode, url (may be blank).
Read-only, public pages only.

1. Companies House (public register pages, no API key): find the company (by number, else by exact name match),
   record status, type, incorporation date, last accounts date, SIC and registered postcode.
2. Website: keep a URL given in the source data; otherwise try likely domains built from the company and trading
   names and accept one only if the page itself identifies the company (its company number, or its name together
   with its registered postcode or town). Unverified guesses are discarded, never kept.
"""
import concurrent.futures
import csv
import html
import re
import sys
import time
import urllib.parse

import requests

UA = {"User-Agent": "Mozilla/5.0 (CAPITAL research; read-only)"}
CH = "https://find-and-update.company-information.service.gov.uk"
SUFFIX = re.compile(r"\b(limited|ltd|llp|plc|cic|c\.i\.c|community interest company|uk|u\.k|gb|group|holdings|company|co|inc|the|and|of|trading as|t/a|ta)\b\.?", re.I)
GENERIC_TAIL = {"services", "service", "solutions", "healthcare", "health", "care", "medical", "group", "associates", "consulting",
                "consultancy", "partners", "partnership", "supplies", "systems", "international", "england", "trust", "foundation"}
DEAD = re.compile(r"domain (is )?for sale|buy this domain|parked|account suspended|under (construction|maintenance)|coming soon|site not configured|hugedomains|godaddy", re.I)
POSTCODE = re.compile(r"\b([A-Z]{1,2}\d[A-Z\d]?)\s*(\d[A-Z]{2})\b")


def get(url, timeout=12):
    try:
        r = requests.get(url, headers=UA, timeout=timeout, allow_redirects=True)
        if r.status_code == 200:
            return r
    except requests.RequestException:
        pass
    return None


def text_of(r):
    return re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", r.text))))


def norm_name(s):
    s = re.sub(r"\(.*?\)", " ", s.lower().replace("&", " and "))
    s = re.sub(r"\b(limited|ltd|llp|plc|cic|c\.i\.c)\b\.?", " ", s)
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


def ch_company(number):
    number = number.strip().upper()
    number = number.zfill(8) if number.isdigit() else number
    r = get(f"{CH}/company/{number}", 25)
    if not r:
        return {}
    txt = text_of(r)
    out = {"ch_number": number}
    m = re.search(r"(?is)<title>\s*(.*?)\s+(?:overview|people|filing|more)", r.text)
    out["ch_name"] = html.unescape(m.group(1)).strip() if m else ""
    for key, pat in (("ch_status", r"Company status ([A-Z][\w —\-]{2,60}?) (?:Company type|Dissolved on|Incorporated on)"),
                     ("ch_type", r"Company type ([\w \-,]{5,90}?) (?:Incorporated|Registered) on"),
                     ("ch_incorporated", r"(?:Incorporated|Registered) on (\d+ \w+ \d{4})"),
                     ("ch_last_accounts", r"Last accounts made up to (\d+ \w+ \d{4})"),
                     ("ch_sic", r"Nature of business \(SIC\) (\d{5} - [^$]{3,90}?)(?: \d{5} - | \$| Tell us| Previous company| Is there)"),
                     ("ch_address", r"Registered office address (.{5,160}?) Company status")):
        m = re.search(pat, txt)
        out[key] = m.group(1).strip() if m else ""
    pc = POSTCODE.findall(out.get("ch_address", "").upper())
    out["ch_postcode"] = f"{pc[-1][0]} {pc[-1][1]}" if pc else ""
    return out


def ch_find(name):
    """Company number for an exact (normalised) name match in the register search, else ''."""
    r = get(f"{CH}/search/companies?q={urllib.parse.quote_plus(name)}", 25)
    if not r:
        return ""
    target = norm_name(name)
    for num, nm in re.findall(r'href="/company/([A-Z0-9]{8})"[^>]*>(.*?)</a>', r.text, re.S)[:8]:
        if norm_name(html.unescape(re.sub(r"<[^>]+>", "", nm))) == target:
            return num
    return ""


def name_slugs(supplier, ch_name=""):
    names = []
    for raw in (supplier, ch_name):
        if not raw:
            continue
        parts = re.split(r"\b(?:t/a|trading as|ta)\b", raw, flags=re.I)
        names += [p for p in reversed(parts) if p.strip()]  # trading name first
    slugs = []
    for nm in names:
        nm = re.sub(r"\(.*?\)", " ", nm).replace("&", " and ")
        toks = [t for t in re.sub(r"[^a-z0-9 ]+", "", SUFFIX.sub(" ", nm.lower())).split() if t]
        if not toks:
            continue
        variants = [toks]
        if len(toks) > 1 and toks[-1] in GENERIC_TAIL:
            variants.append(toks[:-1])
        for v in variants:
            for s in ("".join(v), "-".join(v)):
                if 3 < len(s) < 40 and s not in slugs:
                    slugs.append(s)
    return slugs[:5]


def verify(url, supplier, ch):
    """Return (final_url, basis) if the site identifies the company, else None."""
    r = get(url)
    if not r or "html" not in r.headers.get("content-type", ""):
        return None
    body = text_of(r)
    if DEAD.search(body[:3000]) or len(body) < 300:
        return None
    low = body.lower()
    number = ch.get("ch_number", "")
    numbers = {number, number.lstrip("0")} - {""}
    has_no = lambda t: any(re.search(rf"(?<!\d){re.escape(n)}(?!\d)", t) for n in numbers if len(n) >= 6)
    toks = [t for t in norm_name(supplier.split(" t/a ")[-1]).split() if len(t) > 2 and t not in GENERIC_TAIL and t not in ("and", "the")]
    name_ok = bool(toks) and all(t in low for t in toks[:3])
    pc = ch.get("ch_postcode", "")
    pc_ok = bool(pc) and (pc.lower() in low or pc.replace(" ", "").lower() in low.replace(" ", ""))
    if has_no(body):
        return r.url, "company number on homepage"
    if name_ok and pc_ok:
        return r.url, "name and registered postcode on homepage"
    if name_ok:
        for path in ("contact", "contact-us", "privacy-policy", "terms-and-conditions", "about-us"):
            r2 = get(urllib.parse.urljoin(r.url, "/" + path), 10)
            if not r2:
                continue
            b2 = text_of(r2)
            if has_no(b2):
                return r.url, f"company number on /{path}"
            if pc and (pc.lower() in b2.lower() or pc.replace(" ", "").lower() in b2.lower().replace(" ", "")):
                return r.url, f"name on homepage, registered postcode on /{path}"
    return None


def enrich(row):
    out = dict(row)
    number = (row.get("coh") or "").strip() or ch_find(row["supplier"])
    ch = ch_company(number) if number else {}
    out.update({k: ch.get(k, "") for k in ("ch_number", "ch_name", "ch_status", "ch_type", "ch_incorporated", "ch_last_accounts", "ch_sic", "ch_postcode")})
    out["website"], out["website_basis"] = "", ""
    given = (row.get("url") or "").strip()
    if given:
        if not given.startswith("http"):
            given = "https://" + given
        out["website"], out["website_basis"] = given, "given in the award notice"
        return out
    if not ch:
        return out
    for slug in name_slugs(row["supplier"], ch.get("ch_name", "")):
        for tld in (".co.uk", ".com", ".uk", ".org.uk", ".org"):
            hit = verify(f"https://www.{slug}{tld}/", row["supplier"], ch) or verify(f"https://{slug}{tld}/", row["supplier"], ch)
            if hit:
                out["website"], out["website_basis"] = hit
                return out
    return out


def main(src, dst, workers):
    rows = list(csv.DictReader(open(src)))
    done = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=workers) as pool:
        for i, res in enumerate(pool.map(enrich, rows), 1):
            done.append(res)
            if i % 25 == 0:
                print(f"{i}/{len(rows)} websites so far: {sum(1 for d in done if d['website'])}", flush=True)
    with open(dst, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(done[0].keys()))
        w.writeheader()
        w.writerows(done)
    print("DONE", len(done), "with CH record", sum(1 for d in done if d["ch_number"]), "active", sum(1 for d in done if d["ch_status"] == "Active"),
          "with website", sum(1 for d in done if d["website"]), flush=True)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], int(sys.argv[sys.argv.index("--workers") + 1]) if "--workers" in sys.argv else 10)
