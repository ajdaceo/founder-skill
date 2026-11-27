# Owner actions

## 1. Network access (blocks all real research and both tests)
Approval prompts sent from the session have closed unanswered three times, so please set it directly: cloud environment menu in the session title bar, then Edit, then Network access. Either choose a broader access level, or add the hosts needed under Allowed domains (keep "Allow package managers" ticked). Guide: https://code.claude.com/docs/en/cloud-environments#network-access
A broader level is the practical choice: test 1 reads hundreds of NHS and council sites, which cannot be listed one by one.

## 2. Validation costs and approvals (only when you want test 1 to start)
- A domain and a mailbox, about £15. This is a cost; nothing is bought until you say so.
- Approve the outreach email text before anything is sent. Sends go to limited companies only, in small numbers, with an opt-out.
- A payment link for pre-orders (Stripe or similar, in your name).

## Reference: suspended QuarterReady launch steps


---


Only these need you. Total time about 30 minutes. Cost £0.

## 1. Approve going on sale (decision)
Product: QuarterReady MTD workbook, £14 one-off. Reply "approved" or say what to change.

## 2. Open a Payhip account (identity and payout: must be you)
- payhip.com, free plan. Fee is 5% per sale plus card processing. No monthly cost. It collects UK/EU VAT on digital sales for you.
- Connect Stripe or PayPal for payouts.
- Add a product: upload `capital/products/mtd-workbook/dist/QuarterReady-MTD-Workbook.xlsx`, paste the copy from `LISTING.md`, price £14.
- Send me the product link.

## 3. Host the landing page (pick one, both free)
- Cloudflare Pages or Netlify: drag the `capital/site` folder in. Send me the URL.
- Or create a new empty GitHub repo for the business and add it to my access; I will move the workspace there and can then deploy via GitHub Pages myself.

## 4. Optional, later: Etsy listing
Etsy has buyers already searching "MTD spreadsheet". It charges about £0.16 per listing plus fees per sale. This is a cost, so I will not ask for it until Payhip is live.

## Notes
- If self-employment income from this passes £1,000 in a tax year you need to register it with HMRC. That is your obligation as owner.
- This workspace sits in a folder of the founder-skill repo because that is the only repo this session can write to. A dedicated repo (action 3) is cleaner.
