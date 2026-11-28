# CAPITAL business infrastructure: set-up guide (final, 2026-11-28)

Built once, reused by every experiment and service. Work through the steps in order; each says what to do, what it costs, and what to tell me afterwards.

**Your time:** about 60 minutes, once. **Cost in the first 30 days:** about £5 (the domain). **From day 31:** £7.78 a month if the mailbox is kept. Inside the £25 cap for roughly the first three months.

Marks used: **[V]** read at the provider's own page or tested on 2026-11-28 · **[P]** partly checked, detail given · **[N]** not verified.

## What was checked before asking you to spend anything

| Check you asked for | Result |
|---|---|
| Name: company register | **[V]** No company name at Companies House contains "Oakmarch". |
| Name: domain | **[V]** `oakmarch.co.uk` and `oakmarch.uk` are both unregistered at the .uk registry (registry lookup returned "not found" for each). |
| Name: trade marks | **[P]** A third-party index of the UK register shows no mark for OAKMARCH. The official register refuses automated access, so that is not yet confirmed at source: step 0 asks you for a two-minute look. One near name exists: **OAKMARK**, registered in the UK by Harris Associates L.P. for investment management (class 36), as shown by the same index. It is a different word in a different field from data and business services, so I still recommend Oakmarch, with one rule: the name is never used for anything financial. |
| Mailbox provider terms | **[V]** Microsoft forbids using the service "to spam or distribute malware" and defines spam as "unwanted or unsolicited bulk email". Individually written business emails in small numbers are not prohibited. They are not expressly permitted either; no mainstream provider does that. Google's terms bar "unsolicited commercial mail" outright, so Google is not used. |
| Mailbox permission restriction | **[V]** Confirmed at Microsoft's page. Permissions granted in Entra reach every mailbox in the organisation. Limiting an app to one mailbox is done in Exchange Online ("RBAC for Applications", which "replaces Application Access Policies"), and the Entra grant must then be removed or the limit has no effect. With a single mailbox in the organisation the two give the same result, so step 3 uses the simple route and fixes a rule: no second mailbox without scoping first. The scoping commands are in the appendix. |
| Mailbox sending limits | **[V]** 10,000 recipients a day per mailbox; a trial organisation is capped at 5,000 external recipients a day; mail sent from the default `onmicrosoft.com` address is limited to 100 external recipients a day. Our ceiling is 20 a day, sent only from `oakmarch.co.uk`. |
| Actual costs | **[V]** Domain $5.66 a year at Porkbun, same on renewal; sterling amount and any VAT appear at checkout **[N]**. Mailbox £6.48 a user a month on a monthly term, £5.40 on an annual term, both before VAT. Free trial: 30 days. **At the end of the trial it "renews to an annual term subscription by default, unless you turn off recurring billing"**, so step 3 turns that off on day one. Whether a card is asked for at sign-up **[N]**. Stripe: no fixed fee; 1.5% + 20p on standard UK cards, 2.8% + 20p premium UK, 2.5% + 20p European, 3.15% + 20p international; 0.4% per paid invoice. Cloudflare DNS and hosting: free plan. |
| Scheduled-session connectivity | **[V]** Two unattended test sessions were run in the `capital-ops` environment on 2026-11-28. The first reached every allowed host (Microsoft Graph and sign-in, Stripe, Contracts Finder, Find a Tender, Companies House, gov.uk, WhatDoTheyKnow, Yahoo, Binance, Apify) and was refused a host that is not on the list, as intended. The second tested the repository: a scheduled session that I create can read this repository but cannot push to it, so step 8 is an edit you make to the existing task, not something I can do for you. |
| ICO fee | Analysis in step 7: on the regulations' wording no fee is due for the planned activities. The ICO's own five-minute self-assessment is the authoritative answer and only you can make that declaration. |

## What only you can do, and why
| Action | Why it must be you |
|---|---|
| Accounts in your name: registrar, Cloudflare, Microsoft, Stripe | Legal ownership, identity checks, bank details |
| Approving the credential forms I raise | The system requires the account owner to enter secrets |
| ICO self-assessment | A legal declaration by the person responsible for the data |
| The named requester on any Freedom of Information request | The Act requires the applicant's real name |
| Approving what is sent to outsiders | Your rule, until a standing authorisation covers it |
| Refunds and tax | Refunds stay with you until authorised; tax is your legal responsibility |

Everything else is mine.

---

## Step 0. Confirm the name (5 minutes, free)
1. Open https://trademarks.ipo.gov.uk/ipo-tmtext/start (the official "Search by keyword, phrase or image"). Search **OAKMARCH**. If nothing in classes 35 or 42 looks the same or nearly the same, the name is clear for our use.
2. If you would rather not use a name one letter from OAKMARK, say so and I will check a reserve (Holmward, Tessard, Kestrel Row) the same way before you buy anything.
3. Decide the address and phone number that will appear on emails, the website and invoices. As a sole trader you trade as "[your name] trading as Oakmarch", and the law requires your name and an address where documents can be served. A home address is lawful. A paid service address is optional; its cost is **[N]**.

**Tell me:** "name confirmed", and the address and phone number to use.

## Step 1. Domain (10 minutes, about £5 a year)
1. Go to https://porkbun.com/tld/co.uk and register `oakmarch.co.uk`.
2. Turn on auto-renew. Skip every paid add-on.

**Tell me:** "domain done".

## Step 2. DNS and website hosting (10 minutes, free)
1. Create an account at https://dash.cloudflare.com/sign-up and add the site `oakmarch.co.uk` on the **Free** plan.
2. Cloudflare shows two nameservers. In Porkbun, open the domain, choose nameservers, and replace them with those two.
3. Leave the website until step 5; it is one more click there.

**Tell me:** "DNS done".

## Step 3. Mailbox (20 minutes, free for 30 days, then £7.78 a month)
1. Open https://www.microsoft.com/en-gb/microsoft-365/business/microsoft-365-business-basic and choose **Try for free**.
2. In the sign-up wizard choose to use a domain you own, enter `oakmarch.co.uk`, and add the DNS records it lists (MX, SPF, DKIM, autodiscover) in Cloudflare. Set each to "DNS only" (grey cloud).
3. **Same day:** in https://admin.microsoft.com open Billing, Your products, and turn **recurring billing off**. The trial then simply ends on day 30 unless you choose to buy. If you keep it, buy the **monthly** term (£6.48 + VAT). I will remind you on day 25 through the dashboard.
4. Make the one licensed user `hello@oakmarch.co.uk` (Users, Active users, your user, Manage username and email, set it as primary). Turn on multi-factor authentication. For any further address, add an **alias** to this mailbox; do not create a second mailbox.
5. In Cloudflare DNS add a TXT record: name `_dmarc`, value `v=DMARC1; p=none; rua=mailto:hello@oakmarch.co.uk`.
6. Let me use the mailbox without your password. In https://entra.microsoft.com go to Applications, App registrations, New registration:
   - Name `capital-operator`; "Accounts in this organizational directory only"; Register.
   - API permissions, Add a permission, Microsoft Graph, **Application permissions**: tick `Mail.Send` and `Mail.ReadWrite`. Then **Grant admin consent**. Nothing else.
   - Certificates & secrets, New client secret, 24 months. Copy the secret **Value** and keep it for step 6. Do not paste it into chat.
   - From Overview, copy the **Application (client) ID** and **Directory (tenant) ID**. These are not secrets.

**Tell me:** "mailbox done", with the client ID and tenant ID.

What the app can and cannot do: send from, read and file mail in the organisation's mailboxes, of which there is one. It cannot read calendars, files, contacts or users, change settings, or sign in as you. Deleting the client secret cuts it off at once.

## Step 4. Payments (15 minutes, no fixed cost)
1. Register at https://dashboard.stripe.com/register as an individual or sole trader, business name Oakmarch, website `oakmarch.co.uk`. Stripe asks for identity documents and a UK bank account. The exact documents for a sole trader are **[N]**.
2. Developers, API keys, **Create restricted key**, name `capital-operator`. Each resource can be set to None, Read or Write **[V]**:
   - **Write:** Customers, Invoices, Products, Prices, Payment Links.
   - **Read:** Charges (the dashboard may show "Charges and Refunds"), Payment Intents, Checkout Sessions, Balance, Events.
   - **None:** everything else, including Payouts, Disputes, bank details and account settings.
   Read access cannot create a refund, so refunds stay with you. Resource names may differ slightly in the dashboard.
3. Keep the key for step 6. Do not paste it into chat.

**Tell me:** "payments done".

Good to know: Stripe holds a new account's first payout for 7 to 14 days after the first payment **[V]**. A customer can pay within days; the money reaches your bank a week or two later the first time.

## Step 5. Keep working records out of public view (2 minutes, free)
This repository (`ajdaceo/founder-skill`) is **public** **[V]**. It holds prospect lists and, for the shorter experiment, the product itself. No customer data is in it and nothing in it names you. Choose one:
- **Recommended: make this repository private.** GitHub, the repository's Settings, General, scroll to Danger Zone, Change repository visibility, Private. One change covers everything, past and future, and no second repository is needed. It has no forks and no stars today **[V]**.
- **Or keep it public** (for example if you want the skill itself public) and create a private repository `capital-ops`, giving the Claude GitHub app access at https://github.com/apps/claude/installations/select_target. I then move the working data there. The copies already published stay visible in this repository's history.

Then, for the website: in Cloudflare open Workers & Pages, Create, Pages, Connect to Git, pick the private repository, set the build output folder to `capital/site` (or `site` in `capital-ops`), and add the custom domain `oakmarch.co.uk`. From then on the site updates when I commit. No Cloudflare key is needed.

**Tell me:** which option you chose.

## Step 6. Credentials (5 minutes)
When steps 3 and 4 are done, say "ready for credentials". I raise two secure forms; you type the secrets into the forms, never into chat:
- Host `login.microsoftonline.com`, username and password type: username = the Application (client) ID, password = the client secret Value.
- Host `api.stripe.com`, token type: the restricted key.

They are stored on the `capital-ops` environment and added to requests by the network proxy. I never see them. That environment allows only twelve named hosts **[V]**: Microsoft Graph and sign-in; Stripe; Contracts Finder, Find a Tender, Companies House, gov.uk and its file store; WhatDoTheyKnow; Yahoo and Binance price data; Apify.

## Step 7. ICO data protection fee (5 minutes)
- **The rule.** The 2018 fee regulations exempt a business that processes personal data only for its own "advertising, marketing and public relations", for "keeping accounts, or records of purchases, sales or other transactions", and for staff administration.
- **What we will do.** Email companies at their published company addresses and handle replies (own marketing). Keep customer and invoice records (accounts). Sell lists and reports about companies and public contracts that contain no named individuals. Statutory requests carry only your own name.
- **Conclusion.** On that wording no fee is due. It becomes due (£52, or £47 by direct debit) if a service ever holds personal data for another purpose, such as lists of named people or a client's staff data. I keep named individuals out of every product so the position holds.
- **Do this:** take the self-assessment at https://ico.org.uk/for-organisations/data-protection-fee/self-assessment/ and keep a screenshot of the result.

**Tell me:** "ICO: exempt" or "ICO: paid".

## Step 8. Point the scheduled operator at the new environment (3 minutes)
The three-hourly scheduled task "CAPITAL operator (V1.0)" still runs in your Default environment with the Gmail, Calendar and Docs connectors attached. I tested whether I could replace it myself: I cannot. A scheduled session that I create has no repository attached and is refused when it tries to push **[V]**, so it could not save its work. The change has to be made on the existing task, by you:
1. Open the task in the Claude app's scheduled tasks list and edit it.
2. Environment: change to **capital-ops**.
3. Repository: leave `ajdaceo/founder-skill` attached (add `capital-ops` too if you created it in step 5).
4. Connectors: remove Gmail, Google Calendar and Docs. The operator does not use them.
5. Save. Then say **"update the operator's instructions"** and I will replace its prompt with one that reads the current mandate amendments, `OPERATING.md` and `DASHBOARD.md`. I can change the prompt; I cannot change the environment, repository or connectors.

Until this is done the scheduled runs keep working as now, but they cannot reach the mailbox or Stripe, because the credentials live on `capital-ops`.

---

## What I do when you have finished
1. Send one test email to you and read your reply; raise a £1 test invoice to you and confirm it shows as paid; record both. That is the first verified pass through send, receive, invoice, pay and record.
2. Publish the site: who we are, services, terms, privacy notice.
3. Send only what you have approved, at no more than five messages on the first day and twenty a day after that, because a new domain that starts fast gets filtered.

## Appendix: limiting the app to one mailbox (only needed before a second mailbox exists)
From Microsoft's page https://learn.microsoft.com/en-us/exchange/permissions-exo/application-rbac **[V]**. Needs the Exchange Online PowerShell module and an administrator in the Organization Management role group.
1. In Entra, **remove** the admin consent for `Mail.Send` and `Mail.ReadWrite` given in step 3. Microsoft: an organisation-wide grant alongside a scoped one "results in no effective resource scoping".
2. In Entra, Enterprise applications (not App registrations, which "shows different values"), open `capital-operator` and copy its Application ID and Object ID.
3. Run:
   ```
   Connect-ExchangeOnline
   Set-Mailbox hello@oakmarch.co.uk -CustomAttribute1 "capital"
   New-ServicePrincipal -AppId <Application ID> -ObjectId <Object ID> -DisplayName "capital-operator"
   New-ManagementScope -Name "capital mailbox" -RecipientRestrictionFilter "CustomAttribute1 -eq 'capital'"
   New-ManagementRoleAssignment -App <Object ID> -Role "Application Mail.Send" -CustomResourceScope "capital mailbox"
   New-ManagementRoleAssignment -App <Object ID> -Role "Application Mail.ReadWrite" -CustomResourceScope "capital mailbox"
   Test-ServicePrincipalAuthorization -Identity <Object ID> -Resource hello@oakmarch.co.uk | Format-Table
   ```
   The scope filter follows Microsoft's own example. The `Set-Mailbox` line is a standard command that I have not re-read today. Changes take 30 minutes to 2 hours to apply; the test command shows the result at once.

## Still not verified
The official trade mark register (step 0); Porkbun's sterling price and VAT; whether Microsoft asks for a card at trial sign-up; Stripe's exact sole-trader documents; the cost of a service address.

## Scheduled-session test results (2026-11-28)
- **Network, 02:31 UTC [V]:** Graph 200, Microsoft sign-in 302, Stripe 404 (reached; no key yet), Contracts Finder 302, Find a Tender 302, Companies House 200, gov.uk 200, WhatDoTheyKnow 403 (reached; the site refuses that plain request), Yahoo 429 (reached; rate-limited at the root address), Binance 200, Apify 200, and a host outside the list was refused. The repository branch was readable.
- **Repository, 02:36 UTC [V]:** the test session started with no repository checked out. It could clone this (public) repository. A trial push was refused: "not in this session's authorized repository set ... add the repository to the session's sources". Conclusion: the operator must run from a task that has the repository attached, which is what step 8 arranges. If the repository is made private (step 5), reading it will need that attachment too.
- Both test tasks were one-off and have ended.
