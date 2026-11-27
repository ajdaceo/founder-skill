"""Turn site_check.js output into prospect statuses: does the supplier publish a Carbon Reduction Plan, and how old is it?

Usage: python3 qualify.py site_check_output.jsonl out.csv [--today YYYY-MM-DD]
Read-only. For every plan link found it downloads the document, reads it (pdftotext, then OCR for scans) and
extracts the publication date. Statuses:
  crp_current     published within the last 12 months
  crp_borderline  12-15 months old (may still be inside the six-months-after-year-end window; not a prospect)
  crp_overdue     more than 15 months old, published 2025
  crp_outdated    published 2024 or earlier
  crp_undated     a plan exists but no date could be read (not a prospect; needs a human look)
  crp_unpublished the link leads to a note such as "contact us for a copy", not a plan
  no_crp          working website, no plan link or plan wording beyond general net-zero statements
  blocked / dead / error   could not be checked (not a prospect)
Also picks a published contact email on the site's own domain (generic addresses first) and Companies House facts
when a company number is known (--ch adds status, type, year-end and SIC from the public register page).
"""
import csv
import datetime as dt
import hashlib
import html
import json
import os
import re
import subprocess
import sys
import tempfile
import time
import urllib.parse

import requests

UA = {"User-Agent": "Mozilla/5.0 (CAPITAL research; read-only)"}
UA2 = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0 Safari/537.36"}
CRP = re.compile(r"carbon[\s\-_]*reduction|\bcrp\b|ppn[\s\-_]*0?0?6|carbon[\s\-_]*plan|net[\s\-_]*zero[\s\-_]*(plan|roadmap|strategy)", re.I)
MONTHS = {m: i for i, m in enumerate("january february march april may june july august september october november december".split(), 1)}
MONTHS.update({m[:3]: i for m, i in list(MONTHS.items())})
MONTHS["sept"] = 9
GENERIC = ("info", "sales", "enquiries", "enquiry", "hello", "office", "admin", "contact", "orders", "accounts", "mail", "customerservices", "customerservice")


def fetch(url, timeout=40):
    for ua in (UA, UA2):
        try:
            r = requests.get(url, headers=ua, timeout=timeout)
            if r.status_code == 200:
                return r
        except requests.RequestException:
            pass
    return None


def pdf_text(content):
    """Text of the first pages of a PDF; OCR if it is a scan. Returns (text, creation_date or None)."""
    with tempfile.TemporaryDirectory() as d:
        p = os.path.join(d, "doc.pdf")
        open(p, "wb").write(content)
        created = None
        try:
            info = subprocess.run(["pdfinfo", "-isodates", p], capture_output=True, timeout=30).stdout.decode("utf-8", "ignore")
            m = re.search(r"(?:ModDate|CreationDate):\s+(\d{4})-(\d{2})-(\d{2})", info)
            dates = [dt.date(int(a), int(b), int(c)) for a, b, c in re.findall(r"(?:ModDate|CreationDate):\s+(\d{4})-(\d{2})-(\d{2})", info)]
            created = min(dates) if dates else None
            text = subprocess.run(["pdftotext", "-layout", "-l", "8", p, "-"], capture_output=True, timeout=60).stdout.decode("utf-8", "ignore")
            if len(text.strip()) < 200:
                subprocess.run(["pdftoppm", "-r", "110", "-f", "1", "-l", "3", "-png", p, os.path.join(d, "pg")], capture_output=True, timeout=120)
                text = ""
                for img in sorted(f for f in os.listdir(d) if f.endswith(".png")):
                    text += subprocess.run(["tesseract", os.path.join(d, img), "-", "--psm", "6"], capture_output=True, timeout=120).stdout.decode("utf-8", "ignore") + "\n"
        except (OSError, subprocess.SubprocessError):
            text = ""
        return text, created


def parse_date(s):
    """First recognisable date in a short string -> (date, precision) where precision is day/month/year."""
    s = s.strip()
    m = re.search(r"\b(\d{1,2})\s*[/.\-_]\s*(\d{1,2})\s*[/.\-_]\s*(\d{4}|\d{2})\b", s)
    if m:
        d, mo, y = int(m.group(1)), int(m.group(2)), int(m.group(3))
        y += 2000 if y < 100 else 0
        if 1 <= mo <= 12 and 1 <= d <= 31 and 2015 <= y <= 2030:
            try:
                return dt.date(y, mo, d), "day"
            except ValueError:
                pass
    m = re.search(r"\b(\d{1,2})(?:st|nd|rd|th)?\s+(?:of\s+)?([A-Za-z]{3,9})\.?,?\s+(\d{4})\b", s)
    if m and m.group(2).lower() in MONTHS and 2015 <= int(m.group(3)) <= 2030:
        try:
            return dt.date(int(m.group(3)), MONTHS[m.group(2).lower()], int(m.group(1))), "day"
        except ValueError:
            pass
    m = re.search(r"\b([A-Za-z]{3,9})\.?,?\s+(\d{1,2})(?:st|nd|rd|th)?,?\s+(\d{4})\b", s)
    if m and m.group(1).lower() in MONTHS and 2015 <= int(m.group(3)) <= 2030:
        try:
            return dt.date(int(m.group(3)), MONTHS[m.group(1).lower()], int(m.group(2))), "day"
        except ValueError:
            pass
    m = re.search(r"\b([A-Za-z]{3,9})\.?,?\s+(\d{4})\b", s)
    if m and m.group(1).lower() in MONTHS and 2015 <= int(m.group(2)) <= 2030:
        return dt.date(int(m.group(2)), MONTHS[m.group(1).lower()], 15), "month"
    m = re.search(r"\b(20(?:1[5-9]|2[0-9]))\b", s)
    if m:
        return dt.date(int(m.group(1)), 7, 1), "year"
    return None, None


def read_plan(url):
    """Return dict(kind, pub_date, precision, basis, real) for one candidate plan link."""
    r = fetch(url)
    if not r:
        return {"kind": "unfetched", "pub": None, "precision": None, "basis": "", "real": False}
    ctype = r.headers.get("content-type", "")
    created = None
    if "pdf" in ctype or url.lower().split("?")[0].endswith(".pdf") or r.content[:4] == b"%PDF":
        text, created = pdf_text(r.content)
        kind = "pdf"
    else:
        t = re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>", " ", r.text)
        text = html.unescape(re.sub(r"<[^>]+>", "\n", t))
        kind = "page"
        title = re.search(r"(?is)<title[^>]*>(.*?)</title>", r.text)
        text = (html.unescape(title.group(1)) + "\n" if title else "") + text
    flat = re.sub(r"[ \t]+", " ", text)
    low = flat.lower()
    real = ("scope 1" in low or "scope1" in low) and ("net zero" in low or "net-zero" in low)
    mentions = bool(re.search(r"carbon\s+reduction\s+plan", low))
    pub, precision, basis = None, None, ""
    for pat, label in ((r"publication\s+date\s*[:.…\-_ ]*\s*([^\n]{0,60}(?:\n[^\n]{0,40})?)", "publication date"),
                       (r"(?:date\s+of\s+publication|date\s+published|published(?:\s+on)?)\s*[:.\-]?\s*([^\n]{0,50})", "published"),
                       (r"(?:approved|signed)[^\n]{0,60}?\bdate\s*[:.\-]?\s*([^\n]{0,40})", "sign-off date"),
                       (r"\bdate\s*[:.\-]\s*([^\n]{0,40})", "date line")):
        for m in re.finditer(pat, flat, re.I):
            d, prec = parse_date(m.group(1))
            if d and d <= dt.date.today() + dt.timedelta(days=31):
                pub, precision, basis = d, prec, label
                break
        if pub:
            break
    if not pub and kind == "page":
        d, prec = parse_date(flat[:300])
        if d and re.search(r"carbon\s+reduction\s+plan", flat[:300], re.I):
            pub, precision, basis = d, prec, "page title"
    if not pub and created:
        pub, precision, basis = created, "day", "pdf file date"
    if not pub:
        m = re.search(r"/(20[12]\d)/(0[1-9]|1[0-2])/", url)
        if m:
            pub, precision, basis = dt.date(int(m.group(1)), int(m.group(2)), 15), "month", "upload folder in URL"
    if not pub:
        d, prec = parse_date(urllib.parse.unquote(url.rsplit("/", 1)[-1]).replace("-", " ").replace("_", " "))
        if d:
            pub, precision, basis = d, prec, "file name"
    return {"kind": kind, "pub": pub, "precision": precision, "basis": basis, "real": real, "mentions": mentions, "chars": len(flat.strip())}


def classify(rec, today):
    if rec.get("status") in (403, 401, 429, 503):
        return "blocked", "", "", ""
    if rec.get("status") != 200:
        return "error", "", "", ""
    if rec.get("dead"):
        return "dead", "", "", ""
    links = [s["href"] for s in rec.get("strong", []) if CRP.search(s["text"] + " " + re.sub(r"[-_]+|%20", " ", urllib.parse.unquote(s["href"])))]
    links += [h for h in rec.get("sitemap_hits", []) if CRP.search(re.sub(r"[-_]+", " ", h))]
    links = [h for h in dict.fromkeys(links) if not re.search(r"wp-login|/tag/|/category/|facebook|linkedin|twitter", h)]
    if not links:
        return "no_crp", "", "", ""
    best = None
    for h in sorted(links, key=lambda h: (not h.lower().split("?")[0].endswith(".pdf"), h))[:6]:
        info = read_plan(h)
        time.sleep(0.3)
        info["url"] = h
        if info["kind"] == "unfetched":
            best = best or info
            continue
        if not info["real"] and not info.get("mentions"):
            continue  # link text matched but the target is not about a plan
        if not info["real"] and info["chars"] < 600:
            info["kind"] = "stub"
        if best is None or best["kind"] in ("unfetched", "stub") or (info["pub"] and info["kind"] != "stub" and (not best["pub"] or info["pub"] > best["pub"])):
            best = info
    if best is None:
        return "no_crp", "", "", "plan-like link text only; targets do not contain a plan"
    if best["kind"] == "unfetched":
        return "crp_undated", "", best["url"], "plan link found but could not be downloaded"
    if best["kind"] == "stub":
        return "crp_unpublished", "", best["url"], "link leads to a short note, not a plan"
    if not best["pub"]:
        return "crp_undated", "", best["url"], "no date found"
    pub = best["pub"]
    note = f"{best['basis']} ({best['precision']})"
    if best["precision"] == "year":
        status = "crp_current" if pub.year >= today.year else ("crp_undated" if pub.year == today.year - 1 else "crp_outdated")
        return status, str(pub.year), best["url"], note
    age = (today - pub).days
    status = "crp_current" if age <= 366 else "crp_borderline" if age <= 458 else "crp_overdue" if pub.year >= today.year - 1 else "crp_outdated"
    return status, pub.isoformat() if best["precision"] == "day" else pub.strftime("%Y-%m"), best["url"], note


def pick_email(rec):
    try:
        host = urllib.parse.urlparse(rec.get("final") or rec["url"]).netloc.lower().replace("www.", "")
    except ValueError:
        host = ""
    emails = [e for e in rec.get("emails", []) if re.fullmatch(r"[a-z0-9._%+\-]+@[a-z0-9.\-]+\.[a-z]{2,}", e)]
    own = [e for e in emails if host and (e.split("@")[1] == host or host.endswith("." + e.split("@")[1]) or e.split("@")[1].endswith("." + host))]
    pool = own or [e for e in emails if not re.search(r"gmail|hotmail|outlook|yahoo|btinternet|aol|icloud|live\.co", e)]
    generic = [e for e in pool if e.split("@")[0] in GENERIC]
    chosen = (generic or pool or [""])[0]
    kind = "" if not chosen else ("generic" if chosen.split("@")[0] in GENERIC else "named-or-role")
    return chosen, kind, ("own-domain" if chosen in own else "other-domain" if chosen else "")


def companies_house(number):
    """Public register page -> status, type, incorporation date, last accounts date, SIC. Empty dict on failure."""
    number = number.strip().upper().zfill(8) if number.strip().isdigit() else number.strip().upper()
    r = fetch(f"https://find-and-update.company-information.service.gov.uk/company/{number}", timeout=30)
    if not r:
        return {}
    txt = re.sub(r"\s+", " ", html.unescape(re.sub(r"<[^>]+>", " ", r.text)))
    out = {"ch_number": number}
    name = re.search(r"<title>\s*(.*?)\s+(?:overview|people|filing)", r.text, re.I | re.S)
    out["ch_name"] = html.unescape(name.group(1)).strip() if name else ""
    for key, pat in (("ch_status", r"Company status ([A-Z][\w —\-]{2,60}?) (?:Company type|Dissolved on|Incorporated on)"),
                     ("ch_type", r"Company type ([\w \-]{5,70}?) (?:Incorporated|Registered) on"),
                     ("ch_incorporated", r"(?:Incorporated|Registered) on (\d+ \w+ \d{4})"),
                     ("ch_last_accounts", r"Last accounts made up to (\d+ \w+ \d{4})"),
                     ("ch_sic", r"Nature of business \(SIC\) (\d{5} - [^$]{3,90}?)(?: \d{5} - | \$| Tell us| Previous company| Is there)")):
        m = re.search(pat, txt)
        out[key] = m.group(1).strip() if m else ""
    return out


def main(src, dst, today, with_ch=False, extra=None):
    recs = [json.loads(l) for l in open(src) if l.strip()]
    extra = extra or {}
    rows = []
    for i, rec in enumerate(recs, 1):
        status, plan_date, evidence, note = classify(rec, today)
        email, email_kind, email_domain = pick_email(rec)
        row = {"id": rec["id"], "website": rec.get("final") or rec["url"], "status": status, "plan_date": plan_date, "evidence": evidence,
               "note": note, "email": email, "email_kind": email_kind, "email_domain": email_domain,
               "site_company_nos": " ".join(rec.get("company_nos", [])), "wording": " || ".join(rec.get("phrases", [])[:2])[:300]}
        row.update(extra.get(rec["id"], {}))
        if with_ch and row.get("coh"):
            row.update(companies_house(row["coh"]))
            time.sleep(0.4)
        rows.append(row)
        if i % 20 == 0:
            print(f"{i}/{len(recs)}", flush=True)
    fields = list(dict.fromkeys(k for r in rows for k in r))
    with open(dst, "w", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        w.writerows(rows)
    counts = {}
    for r in rows:
        counts[r["status"]] = counts.get(r["status"], 0) + 1
    print("COUNTS", counts)


if __name__ == "__main__":
    today = dt.date.fromisoformat(sys.argv[sys.argv.index("--today") + 1]) if "--today" in sys.argv else dt.date.today()
    extra = {}
    if "--meta" in sys.argv:  # CSV with an id column; its other columns (e.g. coh, supplier, basis) are carried through
        for r in csv.DictReader(open(sys.argv[sys.argv.index("--meta") + 1])):
            extra[r["id"]] = r
    main(sys.argv[1], sys.argv[2], today, "--ch" in sys.argv, extra)
