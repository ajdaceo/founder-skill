# CAPITAL business infrastructure: one-time set-up guide

Written 2026-11-28. Built once and reused by every experiment and service. Prices and policies below were read from the providers' own pages on 2026-11-28 unless marked "not verified".

**Your time:** about 60 to 75 minutes, once. **Cost now:** about £5. **Cost from month two:** £7.78 a month if the mailbox is kept. Inside the £25 cap.

## What only you can do, and why
| Action | Why it must be you |
|---|---|
| Accounts in your name: registrar, Cloudflare, Microsoft, Stripe | Legal ownership, identity checks, bank details |
| Approving the environment and credential cards I raise | The system requires the account owner to approve access and enter secrets |
| ICO self-assessment | A legal declaration by the person responsible for the data |
| Being the named requester on Freedom of Information requests | The Act requires the applicant's real name |
| Approving external messages, until you grant a standing authorisation | Your existing rule |
| Tax reporting | Your legal responsibility |

Everything else is mine.

## Step 0. Identity (decide first; 5 minutes)
- **Recommended trading name: Oakmarch.** Neutral, not tied to any one service. On 2026-11-28 `oakmarch.co.uk` was unregistered at the .uk registry and no company on Companies House began with that name.
- Reserves, also free on both checks: Holmward, Tessard, Kestrel Row.
- Not checked: the trade mark register. Two-minute search: https://www.gov.uk/search-for-trademark
- As a sole trader you trade as "[your name] trading as Oakmarch". Your name and an address where documents can be served must appear on business emails, the website and invoices. Decide which address and phone number to use. A home address is lawful; a paid service address is optional and its cost is not verified.

## Step 1. Domain (10 minutes, about £5 a year)
1. Go to https://porkbun.com/tld/co.uk and register `oakmarch.co.uk`. Verified price: $5.66 to register and $5.66 to renew. The sterling amount and any VAT are shown at checkout and are not verified.
2. Turn on auto-renew and registrar lock. Skip paid add-ons.

## Step 2. DNS and website hosting (10 minutes, free)
1. Create a Cloudflare account at https://dash.cloudflare.com/sign-up and add the site `oakmarch.co.uk` on the Free plan.
2. Cloudflare shows two nameservers. In Porkbun, replace the domain's nameservers with those two.
3. Website: after step 5, in Cloudflare open Workers & Pages, create a Pages project, and connect it to the private GitHub repository (folder `site/`). Add the custom domain `oakmarch.co.uk`. From then on the site updates whenever I commit; no Cloudflare key is needed.

## Step 3. Mailbox (20 minutes, free for a month, then £7.78 a month)
**Provider check, as you asked.** I read the providers' own terms:
- **Microsoft 365** forbids using the service "to spam or distribute malware". Its consumer agreement defines spam as "unwanted or unsolicited bulk email", and the Exchange Online limits page says its sending limits exist "to discourage the delivery of unsolicited bulk messages" and that bulk commercial email belongs with specialist providers. Nothing forbids individually written business emails in small numbers.
- **Google** is stricter and is not suitable: Gmail's policy says "Don't use Gmail to distribute spam or unsolicited commercial mail", and the Workspace policy bars "unsolicited mass email, promotions, advertisements, or other solicitations".
- **Verdict:** Microsoft's terms do not prohibit our intended use: 28 individual emails to companies' published addresses, then statutory requests to public bodies. They do not expressly permit it either; no mainstream provider does. Microsoft can still suspend an account that draws complaints, with notice unless urgent. Low volume, true and specific content and an opt-out are the protection.

1. Open https://www.microsoft.com/en-gb/microsoft-365/business/microsoft-365-business-basic and choose **Try for free** (Business Basic). Verified prices, excluding VAT: £5.40 per user a month on an annual subscription, or £6.48 on a monthly subscription. **Choose monthly** (£7.78 with VAT) so it can be cancelled. The trial's length and conversion terms are on Microsoft's "See trial terms" link and are not verified here; set a reminder for day 25.
2. When asked, use your own domain `oakmarch.co.uk` and follow the wizard: it gives DNS records (MX, SPF, DKIM, autodiscover) to add in Cloudflare.
3. Create one user and mailbox: `hello@oakmarch.co.uk`. Turn on multi-factor authentication for it.
4. In Cloudflare DNS add a DMARC record: name `_dmarc`, type TXT, value `v=DMARC1; p=none; rua=mailto:hello@oakmarch.co.uk`.
5. Let me use the mailbox without knowing your password. In https://entra.microsoft.com go to Applications, App registrations, New registration:
   - Name `capital-operator`; "Accounts in this organizational directory only".
   - API permissions, Add, Microsoft Graph, **Application permissions**: `Mail.Send` and `Mail.ReadWrite`. Then **Grant admin consent**.
   - Certificates & secrets, New client secret, 24 months. Copy the secret **Value** somewhere safe for step 6. Do not paste it into chat.
   - From the Overview page note the **Application (client) ID** and **Directory (tenant) ID**. These are not secrets; give them to me in chat.
   - With one mailbox in the tenant, the app can reach only that mailbox. If you ever add a second mailbox, restrict the app first: https://learn.microsoft.com/en-us/graph/auth-limit-mailbox-access (not re-verified today).

## Step 4. Payments (15 minutes, no fixed cost)
1. Register at https://dashboard.stripe.com/register as an individual or sole trader, trading name Oakmarch, website `oakmarch.co.uk`. Stripe will ask for identity and a UK bank account.
2. Verified fees: 1.5% + 20p for standard UK cards; 2.8% + 20p for premium UK cards; 2.5% + 20p for European cards; 3.15% + 20p for international cards; 0.4% per paid invoice on the Starter invoicing plan. On a £295 card payment that is £4.63 (standard) or £8.46 (premium).
3. Developers, API keys, **Create restricted key**, name `capital-operator`:
   - Write: Customers, Invoices.
   - Read: Charges, Payment Intents, Payment Links, Checkout Sessions, Products, Prices, Balance, Events.
   - None: everything else, including Refunds and Payouts. Refunds stay with you until you grant a standing authorisation.
   - Keep the key for step 6. Do not paste it into chat.

## Step 5. Private records (5 minutes, free)
1. Create a **private** GitHub repository named `capital-ops` under your account.
2. Give the Claude GitHub app access to it: https://github.com/apps/claude/installations/select_target
3. Tell me its name. Customer records, replies and paid reports go there, never in the public repository.

## Step 6. Operating environment and credentials (10 minutes)
1. **Done 2026-11-28:** you approved the cloud environment **capital-ops** (limited network access) and this session now runs in it. It allows only these hosts:
   `graph.microsoft.com`, `login.microsoftonline.com` (mail); `api.stripe.com` (payments); `www.contractsfinder.service.gov.uk`, `www.find-tender.service.gov.uk`, `find-and-update.company-information.service.gov.uk`, `www.gov.uk`, `assets.publishing.service.gov.uk` (public data); `www.whatdotheyknow.com` (public bodies' request addresses); `query1.finance.yahoo.com`, `data-api.binance.vision`, `api.apify.com` (paper books and radar data). GitHub and package registries are reachable by default. Open-web research then happens only through the search and fetch tools or in a session you start in the Default environment.
2. When steps 3 and 4 are done, I will raise two secure credential forms. Enter:
   - Host `login.microsoftonline.com`, type username and password: username = the Application (client) ID, password = the client secret Value. Microsoft's documentation confirms this sign-in pattern is supported.
   - Host `api.stripe.com`, type token: the restricted key.
   Secrets are stored on the environment and added to requests by the network proxy. I never see them.
3. Scheduled task "CAPITAL operator": edit it once to use the environment `capital-ops`, add the repository `capital-ops`, and remove the Gmail, Calendar and Docs connectors.

## Step 7. ICO data protection fee (5 minutes)
- **The rule.** The 2018 fee regulations exempt a controller that processes personal data only for its own "advertising, marketing and public relations", for "keeping accounts, or records of purchases, sales or other transactions", and for staff administration. The ICO's exemptions page lists the same purposes.
- **Our activities for E4.** Emails to companies' published addresses and handling the replies (our own marketing); customer and invoice records (accounts and records); statutory requests to public bodies (no personal data beyond your own name); a report about contracts between public bodies and companies.
- **Conclusion.** On that wording no fee is due for E4, provided the report holds no personal data. To keep that true, suppliers that are individuals are left out of reports, and no named contacts are stored beyond what repliers send us.
- **When a fee becomes due** (£52, or £47 by direct debit): any service that holds personal data for another purpose, for example data about a client's staff, or lists of named individuals for sale.
- **Do this:** take the ICO's own self-assessment at https://ico.org.uk/for-organisations/data-protection-fee/self-assessment/ and keep a screenshot of the result. It is the authoritative answer and takes five minutes. Exempt or not, the rest of data protection law still applies: a privacy notice on the website, opt-outs honoured, a suppression list.

## What I do once the steps are done
Publish the site (identity, services, terms, privacy notice); test sending and reading mail on a message to yourself; create the Stripe invoice template; run the pre-send checks; then send only what you have approved.

## Not verified today
Porkbun's sterling price and VAT; Microsoft trial length and conversion terms; cost of a service address; the mailbox-restriction procedure; whether the trade mark register is clear for the name.
