<!-- Source notes compiled 2026-11-27 by a research agent for CAPITAL (E3). Each claim carries its URL and quote. Decisive points were spot-checked by the operator; see research/2026-11-28-e3-readiness.md. Not legal advice. -->
# Infrastructure research: CRP service on a £25 setup budget

Date-stamped: **27 November 2026**. All pages opened on that date from a cloud container (outbound via proxy, non-UK IP, so geo-priced pages may differ slightly from what a UK browser shows).

Method and status labels:

- **VERIFIED** = I opened the provider's own page and the quote below is text from it.
- **SNIPPET** = the provider page would not open (403/503/JS-only); figure comes from a search-result snippet of the provider's page. Treat as unverified.
- **UNCONFIRMED** = could not open a provider page stating it.
- VAT: a sole trader who is not VAT-registered cannot reclaim VAT, so "inc VAT" figures (ex-VAT price x 1.2) are what actually leaves the bank. Where a page did not say whether VAT is included, that is noted.
- Fee arithmetic on £249 is mine, from the quoted rate.

Constraint recap: agent can only use HTTPS on port 443 (no SMTP/IMAP). Owner does all sign-ups in their own name.

---

## A. Domain (.co.uk)

| Registrar | First year | Renewal | Promo-then-jump? | Status | Source and quote |
|---|---|---|---|---|---|
| **Porkbun** | $5.66 | $5.66 | No (flat) | VERIFIED (price); currency shown only as "$", VAT treatment for UK buyers not stated | https://porkbun.com/tld/co.uk — "$5.66 everyday low price $5.66 renewal $0.00 transfer" |
| **IONOS** | £1 ex VAT (£1.20 inc) | £10 ex VAT (£12 inc) | **Yes, 10x jump** | VERIFIED | https://www.ionos.co.uk/domains/co-uk-domain — "Save 90% £10 £ 1 /year for 1 year excl. VAT"; https://www.ionos.co.uk/domains/domain-name-prices — ".co.uk Special offer £ 4 Domain Bundle Price £ 1 Welcome offer £ 1 Regular Renewal Fee £ 10 Domain Transfer £ 4" |
| **Gandi** | £5.99 inc tax (promo; normal £7.13) | £21.56 inc tax (promo; normal £23.96) | **Yes, about 4x jump** | VERIFIED | https://www.gandi.net/en-GB/domain/tld/co.uk — "Registration From £7.13 £5.99 per year"; "Renewal From £23.96 £21.56 per year"; "Prices for United Kingdom, Taxes included, in £ (GBP)" |
| **123-reg** | £3.99 ex VAT (£4.79 inc), new customers only | UNCONFIRMED (renewal column did not render) | Yes (new-customer offer) | First year VERIFIED | https://www.123-reg.co.uk/domain-names/ — ".co.uk The perfect choice for British brands. 1ST YR. NEW CUSTOMER OFFER* £3.99/yr"; "All prices exclude VAT" |
| **Cloudflare Registrar** | UNCONFIRMED (at cost; price only shown in dashboard/search, which returned 403) | UNCONFIRMED | No (at-cost model) | Policy VERIFIED, price not | https://www.cloudflare.com/products/registrar/ — "Registration, transfer, and renewal prices are always at or below what registries and ICANN charge us."; https://www.cloudflare.com/application-services/products/registrar/buy-uk-domains/ — .uk offered "at wholesale prices, with no additional markups"; https://developers.cloudflare.com/registrar/get-started/register-domain/ — "All domains acquired via Cloudflare Registrar use Cloudflare nameservers." |
| **Namecheap** | $6.98 | $9.98 | Mild | SNIPPET only (page returned 403) | https://www.namecheap.com/domains/registration/cctld/co-uk/ (not opened) |

Notes:

- No registrar here needs a paid plan to register. Cloudflare forces Cloudflare nameservers, which is what this stack wants anyway (Cloudflare Pages on the apex).
- Porkbun bills in USD: sterling cost depends on the card's FX rate (roughly £4.30 to £4.60; **FX not verified**). Porkbun page lists "API & MCP access" among free features.
- Cheapest first year: IONOS (£1.20 inc VAT). Cheapest over two or more years with no jump: Porkbun, or Cloudflare if its at-cost price is confirmed at checkout.

---

## B. Mailbox on own domain with an HTTPS API for sending and reading

### B1. Mailbox providers

| Provider / plan | Price, 1 user | Min term | HTTPS API for send + read | Sending limits | What terms say on unsolicited / cold / automated mail | Verdict |
|---|---|---|---|---|---|---|
| **Microsoft 365 Business Basic** (Graph API) | £5.40/user/month ex VAT (£6.48 inc), "paid yearly". One-month free trial. Monthly-commitment price **UNCONFIRMED** (not on page) | "Annual subscription-auto renews"; monthly commitment exists but price not shown | Yes. `POST https://graph.microsoft.com/v1.0/me/sendMail`, application permission `Mail.Send` | 10,000 recipients/day; 30 messages/minute; tenant external-recipient limit, trial tenants capped at 5,000 external/day | AUP only says "to spam or distribute malware". No explicit clause on unsolicited commercial mail or automation in the text opened | **Least restrictive wording found. Recommended.** |
| **Exchange Online (Plan 1)** (Graph API) | £3.10/user/month ex VAT (£3.72 inc), "paid yearly". No trial button | Annual subscription | Same Graph API | Same | Same Microsoft AUP | Cheapest paid option with acceptable wording; annual commitment |
| **Google Workspace Starter** (Gmail API) | £7/user/month flexible; £5.90 with one-year commitment. VAT treatment not stated on page (assume +20%: £8.40 / £7.08). 14-day trial | None on flexible plan | Yes. `POST https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/send` | 2,000 messages/day; 3,000 external recipients/day; trial: 500 external recipients/day | Workspace AUP bans "unsolicited mass email, promotions, advertisements, or other solicitations ("spam")". Gmail policy: "Don't use Gmail to distribute spam or unsolicited commercial mail." | Works technically; wording is tighter than Microsoft's. Fallback |
| **Fastmail** Individual / Standard (JMAP) | $6/month monthly, $5/month yearly (tax-exclusive). 30-day trial | None stated | Yes. JMAP at `https://api.fastmail.com/jmap/session`, bearer API token | 8,000/day (Individual/Standard); trial 120/day | **Explicit ban**: "use in connection with unsolicited commercial email"; and "It is a violation of these Terms to use the Services to send programmatically generated emails to addresses that are outside your Customer Account." | **Not usable**: bans both cold mail and agent-generated mail |
| **Zoho Mail** Forever Free / Mail Lite | Free (1 domain, 5 users, web-only); Mail Lite £0.80/user/month billed annually (no monthly plan), + local taxes | Mail Lite annual only | REST API exists (OAuth, `https://mail.zoho.eu/api/...`); **whether it works on the free plan is UNCONFIRMED** (docs only say "You need a valid Zoho Mail account") | "dynamic... based on each user's reputation" | **Explicit ban**: "Zoho Mail cannot be used for sending out emails in the following categories: Promotional emails, Bulk or Mass emails, Marketing emails, Newsletters, Automated Emails, Transactional Emails." | **Not usable** on terms (promotional and automated both banned) |
| **AgentMail** (API-first inbox for agents) | Free: $0, 3 inboxes, 100 emails/day; Developer $20/month | None | Yes (REST, webhooks) | Free 100/day | **Explicit ban**: "AgentMail does not support cold outreach: email to people who have not asked to hear from you" | **Not usable** for prospecting. (Pricing page says free tier has "1 custom domain"; rate-limit doc says "None": conflicting) |
| **Forward Email** Enhanced Protection | $3/month | Not checked | Send via REST yes (`POST /v1/emails`); reading messages via API was marked "Coming soon" on the page as fetched: **UNCONFIRMED** | "Unlimited outbound (reputation-based)" | Marketing email "subscribers must be opt-in"; cold mail not named | Not recommended: read API unconfirmed, opt-in rule |
| **Cloudflare Email Routing + Email Sending** | Inbound free; sending to arbitrary recipients needs Workers Paid (3,000 emails/month included) | n/a | Via Workers (would need custom build) | 3,000/month included | AUP not checked | Not evaluated further; a build project, not a mailbox |

Sources and exact quotes (B1):

- Microsoft price: https://www.microsoft.com/en-gb/microsoft-365/business/compare-all-microsoft-365-business-products — "Microsoft 365 Business Basic ... £5.40 user/month, paid yearly (Annual subscription-auto renews) Price does not include VAT. Buy now Try for free". Trial: "After your one-month free trial ends, your subscription will automatically convert to a paid subscription and you'll be charged the applicable subscription fee based on the subscription term and billing plan you select. Cancel anytime during your free trial to stop future charges. A credit card is required to sign up." Commitment options: "Monthly commitment with monthly payment: Sign up for a monthly subscription and pay month-to-month and cancel at any time. Annual commitment with monthly payment: Sign up for a one-year subscription and pay monthly. Annual commitment with annual payment: ... pay for the entire year upfront."
- Exchange Online price: https://www.microsoft.com/en-gb/microsoft-365/exchange/compare-microsoft-exchange-online-plans — "Exchange Online (Plan 1) Hosted email service and messaging solution for business users £3.10 user/month, paid yearly (Annual subscription-auto renews) Price does not include VAT. Buy now"
- (Both Microsoft pages returned 503/"blocked" to the default fetcher and opened only with browser-like headers.)
- Graph send: https://learn.microsoft.com/en-us/graph/api/user-sendmail?view=graph-rest-1.0 — "POST /users/{id | userPrincipalName}/sendMail"; permissions table "Application | Mail.Send"; "When using JSON format, you can include a file attachment in the same sendMail action call."
- Exchange limits: https://learn.microsoft.com/en-us/office365/servicedescriptions/exchange-online-service-description/exchange-online-limits — "Recipient rate limit | 10,000 recipients per day"; "Message rate limit | 30 messages per minute"; "The limit for trial tenant is capped at 5,000 external recipients per day."; "Outbound mail from these [onmicrosoft.com] domains is limited to 100 external recipients per organization within a 24-hour rolling window." (so send from the custom domain); "Exchange Online customers who need to send legitimate bulk commercial email (for example, customer newsletters) should use third-party providers that specialize in these services."
- Microsoft AUP: https://www.microsoft.com/licensing/terms/product/ForOnlineServices/all — "Neither Customer, nor those that access an Online Service through Customer, may use an Online Service: ... to spam or distribute malware;"
- Google price: https://workspace.google.com/intl/en_uk/products/gmail/for-work/ — "£5.90" per user per month with one-year commitment, "Or £7 per user/month, when billed monthly."; https://workspace.google.com/pricing?hl=en-GB&region=GB — "Annual (Save 16% with one-year commitment)", "All plans billed monthly, all prices £GBP"; Google help table (https://knowledge.workspace.google.com/admin/billing/ai-features-and-pricing-updates-for-google-workspace-business-editions) lists Business Starter GBP "£7" flexible, "£5.90" annual. A search snippet mentioned a £2.95 new-customer introductory rate; **not seen on the pages opened, UNCONFIRMED**.
- Gmail limits: https://knowledge.workspace.google.com/admin/gmail/gmail-sending-limits-in-google-workspace — daily sending limit per user 2,000 (trial 500); external recipients 3,000/day; "free trial accounts have different limits than paid accounts, and limits aren't increased during the free trial period."
- Gmail API: https://developers.google.com/workspace/gmail/api/reference/rest/v1/users.messages/send — "POST https://gmail.googleapis.com/gmail/v1/users/{userId}/messages/send"
- Google AUP: https://workspace.google.com/terms/use_policy.html — "to generate, distribute, publish or facilitate unsolicited mass email, promotions, advertisements, or other solicitations ("spam");"
- Gmail programme policy: https://support.google.com/mail/answer/16734397 — "Don't use Gmail to distribute spam or unsolicited commercial mail. You are not allowed to use Gmail to send email in violation of the CAN-SPAM Act or other anti-spam laws"; "You are not allowed to automate the Gmail interface, whether to send, delete, or filter emails, in a manner that misleads or deceives users."; "your definition of "unsolicited" or "unwanted" mail may differ from your email recipients' perception." (Page does not say whether it binds Workspace accounts as well as consumer Gmail.)
- Fastmail price: https://www.fastmail.com/pricing/ — Individual "$6/month" monthly, "$5/month" yearly; "All prices are tax-exclusive."; "Try free for up to 30 days". API: https://www.fastmail.com/dev/ — session at "https://api.fastmail.com/jmap/session"; "generate an API token (for JMAP access) in Settings → Privacy & Security → Manage API tokens." Limits: https://www.fastmail.help/hc/en-us/articles/1500000277382-Account-limits — "All trial accounts are limited to sending a maximum of 120 messages per day." Terms: https://www.fastmail.com/policies/terms-of-service/ — "The Services are not designed for sending automated or transactional emails. It is a violation of these Terms to use the Services to send programmatically generated emails to addresses that are outside your Customer Account."; "may not use it in ways not permitted by other clauses of these Terms, including, but not limited to, use in connection with unsolicited commercial email"; "Fastmail will immediately terminate any Customer Account which it believes, in its sole discretion, is transmitting or is otherwise connected with any spam or other unsolicited bulk email."
- Zoho price: https://www.zoho.com/mail/zohomail-pricing.html — Forever Free "Up to 5 users", "IMAP/ POP/ Active Sync not included"; Mail Lite £0.80 per user/month billed annually, "No monthly plan". Free plan is "web-only access" per https://www.zoho.com/mail/help/adminconsole/subscription.html. API: https://www.zoho.com/mail/help/api/getting-started-with-api.html — "You need a valid Zoho Mail account to use the API." Policy: https://www.zoho.com/mail/help/usage-policy.html — quote in table; also "The number of emails you can send is dynamic. It is determined based on each user's reputation." General terms: https://www.zoho.com/terms.html — "You agree not to use the Services for the transmission of "junk mail", "spam", "chain letters", "phishing" or unsolicited mass distribution of email."
- AgentMail: https://www.agentmail.to/pricing — Free "$0/month", "3 inboxes", "100 emails/day"; https://agentmail.to/docs/knowledge-base/cold-outreach.md — "**No.** AgentMail does not support cold outreach: email to people who have not asked to hear from you, such as prospects from a scraped or purchased list, or an automated sales sequence. Writing each message with an LLM does not change that."; terms https://www.agentmail.to/legal/terms s.8(h) — "Send any unsolicited or unauthorized advertising, promotional materials, email, junk mail, spam".
- Forward Email: https://forwardemail.net/en/private-business-email — "Enhanced Protection: $3/month", "Developer API access"; https://forwardemail.net/en/terms — marketing "subscribers must be opt-in".
- Cloudflare email: https://developers.cloudflare.com/email-service/platform/pricing/ — Workers Free sending "Free, to verified destination addresses only."; paid 3,000/month then "$0.35 per 1,000 emails."

### B2. Transactional services: do they permit unsolicited B2B prospecting?

All five say no. VERIFIED.

| Service | Permits cold B2B? | Quote | URL |
|---|---|---|---|
| Resend | No | "You are prohibited from sending unsolicited messages of any kind, including cold outreach, purchased lists, or scraped contact data"; "All mail must be sent to recipients who have explicitly opted in" | https://resend.com/legal/acceptable-use |
| Postmark | No | "All email lists contained and/or used with respect to the Service must be permission-based subscriptions. Use of a list that has been purchased or rented from a third party is prohibited."; "Emails sent unsolicited will receive abuse complaints that will be reflected on Your account." | https://postmarkapp.com/terms-of-service |
| Mailgun (Sinch) | No | "Acquiring or sending to a third-party mailing list is prohibited."; non-transactional email "can only be sent to recipients who have granted clear, explicit and provable consent" | https://www.mailgun.com/legal/aup/ |
| Amazon SES (AWS AUP) | No for mass mail | "to distribute, publish, send, or facilitate the sending of unsolicited mass email or other messages, promotions, advertising, or solicitations (or "spam")" | https://aws.amazon.com/aup/ |
| Brevo | No | "Lists of Contacts that have been scraped on the internet, acquired or purchased from a third-party ... the use of such lists of Contacts is strictly prohibited"; "You must have the consent of your Contacts, and it must be active" | https://www.brevo.com/legal/antispampolicy/ |

Purpose-built cold-outreach tools exist (e.g. Instantly: cheapest outreach plan "$47/mo", https://instantly.ai/pricing; API inclusion on that plan not confirmed) but they sit on top of Google/Microsoft mailboxes and cost more than the whole budget.

### B3. Recommendation and risk, stated plainly

**Recommended: Microsoft 365 Business Basic on the one-month free trial, driven through Microsoft Graph.** It is the cheapest option whose published terms, as opened, do not expressly prohibit low-volume individually addressed B2B prospecting or agent-sent mail.

**Risk:** no provider checked *affirmatively permits* unsolicited commercial email. Fastmail, Zoho, AgentMail and all five transactional services forbid it in terms; Google's wording covers "unsolicited ... solicitations" and "unsolicited commercial mail". Microsoft's AUP forbids "spam" without defining it, so Microsoft can decide, at its discretion and typically after recipient complaints, that the prospecting is spam and block or suspend the tenant. The domain's reputation is also at stake on a brand-new domain. Keeping volume to roughly 10 to 20 a day, one recipient per message, corporate addresses only, clear sender identity and an opt-out lowers but does not remove this risk.

**Commitment trap:** the £5.40 price is an annual subscription. If the owner lets the trial convert on an annual term, the liability is about £77.76 inc VAT over the year, well over £25. Choose the monthly-commitment option at checkout (price UNCONFIRMED, not on the page) or cancel inside the trial. Google Workspace flexible (£7/month, cancel any time, 14-day trial) is the no-commitment fallback with tighter policy wording.

---

## C. Payments for a UK sole trader

### C1. Fees on a £249 payment

| Provider / method | Rate (quoted) | Fee on £249 | Net | API readable? | Status |
|---|---|---|---|---|---|
| **Stripe**, standard UK card (Payment Link or Checkout) | "1.5% + 20p for standard UK cards" | £3.94 | £245.06 | Yes | VERIFIED |
| Stripe, premium UK card (business/corporate cards are likely to fall here; definition not checked) | "2.8% + 20p for premium UK cards" | £7.17 | £241.83 | Yes | VERIFIED rate |
| Stripe, EEA card | "2.5% + 20p for European Economic Area cards" | £6.43 | £242.57 | Yes | VERIFIED |
| Stripe Invoicing add-on (Starter) | "0.4% per paid invoice" (on top of payment fee) | + £1.00 | | Yes | VERIFIED |
| Stripe GBP bank transfer (via invoice or Checkout; **not** Payment Links) | "0.5%", "£5.00 cap"; refund "£0.50 per successful refund" | £1.25 (+ £1.00 if by invoice = £2.25) | £247.75 (£246.75 by invoice) | Yes (cash balance transactions API) | VERIFIED |
| Stripe Pay by Bank | "0.5% + 20p per successful charge", "£5.00 cap" | £1.45 | £247.55 | Yes | VERIFIED |
| Stripe Bacs Direct Debit | "1%", "Minimum fee of 20p", "£4.00 cap" | £2.49 | £246.51 | Yes | VERIFIED |
| **GoCardless** Standard | "1% + 20p Per transaction. Prices exclude VAT."; "Capped at £4"; +0.3% over £2,000 | £2.69 ex VAT (£3.23 inc) | about £245.77 | Yes (API product) | VERIFIED; separate Instant Bank Pay price not shown |
| **SumUp Invoices** (Free plan) | "The transaction fee is 2.5%"; "There are no transaction fees for bank transfers or cash payments." | £6.23 card / £0 bank transfer | £242.77 | Not checked | VERIFIED |
| **Square Invoices** (Free plan) | "2.5%" online card payment; "No monthly fees" | £6.23 | £242.77 | Not checked on this page | VERIFIED |
| **PayPal** invoicing / checkout | 2.9% + £0.30 standard domestic (SNIPPET; all PayPal UK fee pages returned 403) | £7.52 | £241.48 | Yes (not verified) | **UNCONFIRMED** |
| Plain bank transfer to a free business account | none | £0 | £249 | See C3 | see C3 |

Sources: https://stripe.com/gb/pricing ; https://stripe.com/gb/invoicing/pricing ("Stripe Invoicing has no fixed fees or setup costs, but Stripe Payments pricing will apply."); https://stripe.com/gb/pricing/local-payment-methods ; https://gocardless.com/pricing/ ; https://www.sumup.com/en-gb/invoices/pricing/ ; https://squareup.com/gb/en/invoices .

### C2. Stripe detail

- No fixed costs: "No setup fees, monthly fees, or hidden fees." (https://stripe.com/gb/pricing)
- Payment Links: no extra fee ("Included at no additional charge for businesses on standard payments pricing"); can be created by API ("Use the API to create and manage payment links", https://docs.stripe.com/payment-links). "Bank transfers don't support Payment Links." (https://docs.stripe.com/payments/bank-transfers)
- Bank transfers: GB accounts can accept GBP; "you provide customers with a virtual bank account number that they can push money to"; works with Invoicing ("Invoices and Subscriptions only support the send_invoice collection method").
- Payout timing (https://docs.stripe.com/payouts): "After you successfully receive your first live payment, Stripe typically schedules your initial payout to complete within 7-14 days"; UK row: "7 calendar days" initial, "3 business days" default thereafter.
- Sole trader without a company: allowed. https://support.stripe.com/questions/selling-on-stripe-without-a-separate-business-entity — "You can use Stripe to sell a product if you have not established a separate business entity to do so." Business type "Sole proprietorship: If you do not have a separate entity and operate by yourself."
- Verification: https://docs.stripe.com/get-started/account/activate — "Verify your business in the Dashboard. Provide information about your business, product, and relationship to the business. As you use more Stripe services, we might request additional information or verification." Public details required: "Business name and website URL; Support email address, phone number, and address; ... Statement descriptor text". The exact UK document list (photo ID, date of birth, bank sort code/account number) is standard KYC but **was not quoted from a page**.
- Restricted businesses (https://stripe.com/gb/legal/restricted-businesses): nothing names consulting, compliance documents or carbon reporting. Clauses worth knowing: "No-value-added services, including the sale or resale of a service without added benefit to the buyer"; "Document falsification services"; "Offering government services without authorisation or value-add". A genuine drafted plan is none of these; do not present the document as government-issued or "approved".
- Agent access: use a restricted API key ("Use restricted API keys instead of secret keys wherever possible").

### C3. Free business bank accounts (for plain bank transfer)

| Bank | Monthly fee | UK transfer fees | Sole trader eligible | API for the agent | Status |
|---|---|---|---|---|---|
| **Starling** business | "With no monthly fees." | "We don't charge transaction fees on payments to or from UK bank accounts, or on UK bank transfers." | Separate sole trader page exists but returned 403 | Personal access token for own account (SNIPPET; developer site is JS-only) | Fees VERIFIED on https://www.starlingbank.com/business-account/ ; sole trader terms and API **UNCONFIRMED** |
| **Monzo Business Lite** | "A free business bank account" | Not stated on page | "Only sole traders and limited company directors in the UK can apply." | API docs: "The Monzo Developer API is not suitable for building public applications."; "You may only connect to your own account"; only `uk_retail` account types listed, business not confirmed | VERIFIED quotes: https://monzo.com/business-banking , https://docs.monzo.com/ |
| **Tide** (Lite) | "No plan fee." | Table shows "Bank transfers 5/month" on the free tier; charge beyond that not shown | "trusted by over 2 million sole traders" | None found | Partly VERIFIED: https://www.tide.co/pricing/ |
| **Wise Business** | **"All in for 50 GBP ... one set-up fee"** | "Receiving domestic payments ... GBP ... Free" | Not checked | Has API (not checked) | VERIFIED: https://wise.com/gb/pricing/business — **£50 setup breaks the budget** |

Practical point: a bank-only route gives the agent no reliable API to see that a client has paid. Stripe does, at £1.25 to £7.17 per sale and no fixed cost.

---

## D. Intake form and file collection

| Tool | Free-tier limits | File upload on free | Read responses over HTTPS API on free | Data location / GDPR | Status |
|---|---|---|---|---|---|
| **Tally** | "unlimited forms and submissions, completely free" (fair use: extensive usage examples start at 50,000 submissions/month) | Yes; 10 MB per file implied by Pro feature "Remove the 10 MB per file size limit when using the File Upload block." | Yes: base "https://api.tally.so", bearer key from Settings > API keys, `GET /forms/{formId}/submissions` "Returns a paginated list of form submissions with their responses."; "limits requests to 100 per minute". Webhooks listed among Free features. No plan restriction stated (not explicitly confirmed as free) | "All Tally form data is encrypted both in transit and at rest, and stored in Europe."; Google Cloud, Belgium; "Tally is based in Belgium (EU) and complies with the GDPR framework."; "We have a DPA available for you." | VERIFIED: https://tally.so/pricing , https://developers.tally.so/api-reference/introduction , https://developers.tally.so/api-reference/endpoint/forms/submissions/list , https://tally.so/help/gdpr , https://tally.so/help/fair-use-policy |
| **Fillout** | "Unlimited forms", "1000 responses/mo" | Yes, max 20 MB per file | Yes: "The Forms API works on every plan."; `https://api.fillout.com/v1/api`; 5 requests/second | Hosted "on Amazon Web Services (AWS), via Render.com"; EU hosting only "on our Team plan and above"; "our standard DPA is available to any customer, on any plan" | VERIFIED: https://www.fillout.com/pricing , https://www.fillout.com/help/fillout-rest-api , https://www.fillout.com/help/gdpr |
| **Jotform** Starter | "Active forms: 5", "Monthly submissions: 100", "Fields per form: 100" | Yes, "Upload space: 100 MB" total | Yes: "1000 requests per day for the starter plan"; `https://api.jotform.com`, EU `https://eu-api.jotform.com` | EU endpoint exists; residency terms not checked | VERIFIED: https://www.jotform.com/pricing/ , https://api.jotform.com/docs/ |
| **Google Forms** | Free with a Google account | Yes, but "To answer this question, responders need to sign in to a Google Account."; files go to owner's Drive | Yes: "GET https://forms.googleapis.com/v1/forms/{formId}/responses" (OAuth) | Google; location not checked | VERIFIED: https://support.google.com/docs/answer/7322334 , https://developers.google.com/workspace/forms/api/reference/rest/v1/forms.responses/list |
| **Cognito Forms** Individual | "1 user", "100 entries / mo.", "100 MB of storage" | Not stated for free plan | Not stated | Not checked | Partly VERIFIED: https://www.cognitoforms.com/pricing |
| **Typeform** Free | "10 responses per month across all your forms combined." | **No** (paid plans unlock "payment and file upload questions") | "API access" listed; webhooks from Basic ($39/month monthly) | Not checked | VERIFIED: https://www.typeform.com/pricing — unsuitable |

Recommendation: **Tally** (free, 25 fields and bill uploads fit, EU-hosted, HTTPS API and webhooks). 10 MB per file is enough for utility-bill PDFs. Delivery of the finished PDF/Word file: attach it to the reply email (Graph sendMail supports file attachments).

---

## E. Free static hosting on a custom domain

| Host | Free limits | Custom domain | Commercial use on free tier | Status |
|---|---|---|---|---|
| **Cloudflare Pages** | "Builds per month" 500; "up to 20,000 files"; "maximum file size for a single Cloudflare Pages site asset is 25 MiB"; 100 custom domains per project; "On both free and paid plans, requests to static assets are free and unlimited." | Yes | No restriction found on the pages opened (not affirmatively stated either) | VERIFIED: https://developers.cloudflare.com/pages/platform/limits/ , https://developers.cloudflare.com/pages/functions/pricing/ |
| **GitHub Pages** | Sites "no larger than 1 GB"; "soft bandwidth limit of 100 GB per month"; public repos only on GitHub Free | Yes | **Not allowed**: "GitHub Pages is not intended for or allowed to be used as a free web-hosting service to run your online business, e-commerce site, or any other website that is primarily directed at either facilitating commercial transactions or providing commercial software as a service (SaaS)." | VERIFIED: https://docs.github.com/en/pages/getting-started-with-github-pages/github-pages-limits |
| **Netlify** Free | "300 credit limit"; bandwidth costs 20 credits per GB (about 15 GB if nothing else uses credits); "Add Custom domains with SSL" | Yes | Page makes no statement | VERIFIED: https://www.netlify.com/pricing/ |

Recommendation: **Cloudflare Pages**. An offer page that links to a payment page is exactly what GitHub's rule excludes.

---

## F. Recommended stack and cost

| Item | Choice | First month | Ongoing | Basis |
|---|---|---|---|---|
| Domain | Porkbun .co.uk (or IONOS if lowest first year matters most) | $5.66, roughly £4.50 (IONOS: £1.20) | $5.66/year, about £0.38/month (IONOS: £12/year from year 2) | VERIFIED prices; FX and Porkbun UK VAT not verified |
| DNS + hosting | Cloudflare free plan + Pages | £0 | £0 | VERIFIED |
| Mailbox + API | Microsoft 365 Business Basic, Graph API | £0 (one-month trial) | £6.48/month inc VAT on annual term; monthly-commitment price UNCONFIRMED. Alternative: Exchange Online Plan 1 £3.72/month inc VAT, annual | VERIFIED annual prices |
| Payments | Stripe Payment Link (card) and/or Stripe invoice with bank transfer | £0 fixed | Per sale: £3.94 to £7.17 card; £2.25 invoice + bank transfer | VERIFIED |
| Intake form | Tally free | £0 | £0 | VERIFIED |
| **Total** | | **about £4.50 (or £1.20 with IONOS)** | **about £6.90/month** (about £4.10 with Exchange Online Plan 1), plus Stripe fees per sale | |

Fits inside £25: **yes** for month one, and for roughly the first three months (about £4.50 + 2 x £6.48 = £17.46), **provided** the mailbox is not locked into an annual term.

Possible extra cost outside the brief: the ICO says "organisations (including sole traders) that use personal information need to pay a data protection fee" unless exempt (https://ico.org.uk/for-organisations/data-protection-fee/). **Fee amount UNCONFIRMED** (page with amounts returned 404); it may on its own exceed the £25 budget. Check the ICO self-assessment before trading.

---

## Owner sign-up actions (the agent cannot do these)

| Service | What the owner does | What it needs |
|---|---|---|
| Registrar (Porkbun/IONOS) | Create account, buy domain, set nameservers to Cloudflare | Name, UK postal address, email, payment card. (.uk registrant identity may be checked: not verified) |
| Cloudflare | Free account, add zone, create Pages project, issue a scoped API token for the agent | Email only |
| Microsoft 365 | Start Business Basic trial, verify domain by DNS TXT, create the mailbox, register an Entra app with `Mail.Send` and mail-read permissions, grant admin consent, hand tenant ID / client ID / secret to the agent | Name, phone, "A credit card is required to sign up" |
| Stripe | Register as sole proprietorship, complete verification, add payout bank account, enable bank transfers, create restricted API key | Legal name, address, phone, website URL, business description, UK bank account; photo ID/date of birth expected (not quoted) |
| Tally | Free account, create API key (Settings > API keys) | Email only |
| Bank (optional) | A free business account if the owner wants business money separate | Photo ID and app-based checks (not verified) |

---

## Items not verified

1. Cloudflare Registrar .co.uk price (not published on a static page).
2. Namecheap .co.uk price (403; snippet only).
3. 123-reg renewal price.
4. Porkbun currency label, UK VAT treatment, and the USD to GBP conversion.
5. Microsoft monthly-commitment prices; cancellation/refund rules on annual terms.
6. Google Workspace VAT treatment and any introductory discount.
7. Zoho Mail API availability on the free plan.
8. Forward Email message-reading API.
9. PayPal UK fees (every PayPal UK fee page returned 403).
10. Starling sole trader page and developer API docs (403 / JS-only); Monzo API for business accounts; Tide charge per transfer beyond the free allowance.
11. GoCardless Instant Bank Pay specific pricing.
12. Stripe: what counts as a "premium" UK card; exact UK sole-trader KYC document list; bank-transfer eligibility for a brand-new account.
13. Tally: API on the free plan is implied (no restriction stated), 10 MB limit is inferred from the Pro feature text.
14. Cognito Forms file upload / API on free; Netlify and Cloudflare Pages commercial-use stance (no statement found).
15. ICO data protection fee amount.
16. UK PECR lawfulness of the prospecting was assumed per the brief and not researched here.

Working files: raw page downloads are in `/tmp/claude-0/-home-user-founder-skill/efd46656-d6f8-5f47-9c2a-308ae1680e0d/scratchpad/infra-dl/`; the fetch helper is `/tmp/claude-0/-home-user-founder-skill/efd46656-d6f8-5f47-9c2a-308ae1680e0d/scratchpad/scripts/fetchtext.py`.
