// Browser pass for prospect qualification. Read-only: loads public pages only.
// Usage: node site_check.js sites.json out.jsonl [concurrency]
//   sites.json: [{"id": "...", "url": "https://..."}]
// For each site: homepage, then up to 8 same-site pages that could signpost a Carbon Reduction Plan
// (sustainability, environment, policies, about, accreditations...), plus sitemap and four common paths.
// Records: links and wording about carbon / CRP / net zero / PPN, published email addresses, any company number shown.
const fs = require('fs');
const { chromium } = require('playwright');

const NAV = /carbon|crp|net[\s-]?zero|ppn|sustainab|environment|polic|esg|csr|responsib|green|accredit|download|document|about|quality|ethic|compliance|legal|corporate|governance|our-story|who-we|contact/i;
const STRONG = /carbon|\bcrp\b|net[\s-]?zero|ppn/i;
const PHRASE = /.{0,80}(carbon reduction plan|net[\s-]zero|carbon neutral|carbon footprint|ppn ?0?0?6|scope 1).{0,100}/gi;
const EMAIL = /[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}/g;
const COMPANY_NO = /(?:company|registered|registration|reg\.?|co\.?)\s*(?:no\.?|number|num\.?)?\s*(?:in england(?: and wales)?|in scotland)?\s*(?:no\.?|number)?[:.\s]*((?:SC|NI|OC)?\d{6,8})\b/gi;
const DEAD = /domain (is )?for sale|buy this domain|parked|account suspended|under (construction|maintenance)|coming soon|site not configured|website is no longer/i;
const COMMON = ['carbon-reduction-plan', 'sustainability', 'environment', 'policies'];

async function grab(ctx, u) {
  const page = await ctx.newPage();
  try {
    const resp = await page.goto(u, { waitUntil: 'domcontentloaded', timeout: 30000 });
    await page.waitForTimeout(1500);
    const links = await page.$$eval('a', as => as.map(a => [(a.innerText || a.getAttribute('aria-label') || a.title || '').trim().replace(/\s+/g, ' ').slice(0, 80), a.href]));
    const text = await page.evaluate(() => document.body ? document.body.innerText : '');
    return { status: resp ? resp.status() : 0, final: page.url(), links, text, title: await page.title() };
  } catch (e) {
    return { status: -1, final: u, links: [], text: '', title: '', error: String(e).split('\n')[0].slice(0, 120) };
  } finally { await page.close(); }
}

async function site(browser, item) {
  const ctx = await browser.newContext({ locale: 'en-GB' });
  const out = { id: item.id, url: item.url, status: 0, title: '', dead: false, pages: [], strong: [], phrases: [], emails: [], company_nos: [], sitemap_hits: [] };
  try {
    const home = await grab(ctx, item.url);
    out.status = home.status; out.title = home.title.slice(0, 100); out.final = home.final; out.textlen = home.text.length; out.error = home.error;
    if (home.status !== 200) return out;
    out.dead = DEAD.test(home.title) || (home.text.length < 400 && DEAD.test(home.text));
    const host = new URL(home.final).host.replace(/^www\./, '');
    const strong = new Map(), phrases = new Set(), emails = new Set(), nos = new Set(), queue = new Map();
    const consider = (res, from) => {
      for (const [t, h] of res.links) {
        if (!h) continue;
        if (/^mailto:/i.test(h)) { const m = decodeURIComponent(h.slice(7).split('?')[0]).trim(); if (m.includes('@')) emails.add(m.toLowerCase()); continue; }
        if (/^(tel|javascript):/i.test(h)) continue;
        let dec = h; try { dec = decodeURIComponent(h); } catch (e) {}
        if (STRONG.test(t) || STRONG.test(dec.replace(/[-_]/g, ' '))) strong.set(h, t);
        let same = false; try { same = new URL(h).host.replace(/^www\./, '') === host; } catch (e) {}
        if (same && (NAV.test(t) || NAV.test(h)) && !/\.(pdf|jpe?g|png|docx?|xlsx?|zip)($|\?)/i.test(h)) queue.set(h.split('#')[0], t);
      }
      (res.text.match(PHRASE) || []).slice(0, 3).forEach(s => phrases.add(`${from}: ${s.replace(/\s+/g, ' ')}`));
      (res.text.match(EMAIL) || []).forEach(m => emails.add(m.toLowerCase().replace(/\.$/, '')));
      let m; COMPANY_NO.lastIndex = 0;
      while ((m = COMPANY_NO.exec(res.text)) !== null) nos.add(m[1].toUpperCase());
    };
    consider(home, 'home');
    const homeKey = home.final.replace(/\/$/, '');
    const rank = h => (STRONG.test(h) || STRONG.test(queue.get(h) || '') ? 0 : /sustainab|environment|polic|contact/i.test(h + (queue.get(h) || '')) ? 1 : 2);
    const visit = [...queue.keys()].filter(h => h.replace(/\/$/, '') !== homeKey).sort((a, b) => rank(a) - rank(b)).slice(0, 8);
    for (const h of visit) { const r = await grab(ctx, h); if (r.status === 200) consider(r, new URL(h).pathname.slice(0, 40)); }
    out.pages = visit.map(h => { try { return new URL(h).pathname; } catch (e) { return h; } });
    // Plain HTTP checks through the same browser context: sitemap and common paths
    const base = new URL(home.final).origin + '/';
    for (const sm of ['sitemap.xml', 'wp-sitemap.xml', 'sitemap_index.xml']) {
      try {
        const r = await ctx.request.get(base + sm, { timeout: 15000 });
        if (r.ok()) { const body = await r.text(); (body.match(/<loc>\s*([^<\s]+)\s*<\/loc>/g) || []).map(x => x.replace(/<\/?loc>|\s/g, '')).filter(x => STRONG.test(x.replace(/[-_]/g, ' '))).slice(0, 10).forEach(x => out.sitemap_hits.push(x)); }
      } catch (e) {}
    }
    for (const p of COMMON) {
      if (out.pages.some(x => x.replace(/\//g, '') === p)) continue;
      try {
        const r = await ctx.request.get(base + p, { timeout: 15000, maxRedirects: 3 });
        if (r.ok() && !r.url().replace(/\/$/, '').endsWith(homeKey.replace(/^https?:\/\/(www\.)?/, ''))) {
          const body = await r.text();
          if (/carbon reduction plan|ppn ?0?0?6/i.test(body) && r.url().includes(p.split('-')[0])) strong.set(r.url(), `(direct path /${p})`);
        }
      } catch (e) {}
    }
    out.strong = [...strong].slice(0, 15).map(([h, t]) => ({ text: t, href: h }));
    out.phrases = [...phrases].slice(0, 8);
    out.emails = [...emails].filter(e => !/\.(png|jpe?g|gif|webp|svg)$/i.test(e) && !/sentry|wixpress|example\.|yourname|domain\.com|email\.com/i.test(e)).slice(0, 12);
    out.company_nos = [...nos].slice(0, 5);
  } catch (e) {
    out.error = String(e).split('\n')[0].slice(0, 160);
  } finally { await ctx.close(); }
  return out;
}

(async () => {
  const items = JSON.parse(fs.readFileSync(process.argv[2], 'utf8'));
  const outPath = process.argv[3];
  const conc = parseInt(process.argv[4] || '6', 10);
  fs.writeFileSync(outPath, '');
  const browser = await chromium.launch();
  let i = 0, done = 0;
  const worker = async () => {
    while (i < items.length) {
      const item = items[i++];
      let res;
      try { res = await Promise.race([site(browser, item), new Promise(r => setTimeout(() => r({ id: item.id, url: item.url, status: -2, error: 'site timeout', strong: [], phrases: [], emails: [], company_nos: [], sitemap_hits: [], pages: [] }), 150000))]); }
      catch (e) { res = { id: item.id, url: item.url, status: -3, error: String(e).slice(0, 120), strong: [], phrases: [], emails: [], company_nos: [], sitemap_hits: [], pages: [] }; }
      fs.appendFileSync(outPath, JSON.stringify(res) + '\n');
      if (++done % 10 === 0) console.log(`${done}/${items.length}`);
    }
  };
  await Promise.all(Array.from({ length: conc }, worker));
  await browser.close();
  console.log(`DONE ${done}`);
})();
