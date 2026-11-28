# Procurement intelligence: working data

Source: Find a Tender award notices (Open Government Licence), 1 January 2025 to 27 November 2026, pulled 2026-11-28 with `ops/fts_pull.py`. Above-threshold contracts only; lower-value awards are on Contracts Finder and are not included.

- `tech-awards-2025-01-to-2026-11.csv`: every supplier row on a notice with a software or IT classification, or a technology word in its title.

## First cut by product category (keyword match on notice titles; rough)

| Category | Notices | Vendors | of which SME | Buyers |
|---|---|---|---|---|
| CCTV / body worn video | 63 | 123 | 82 | 54 |
| network / connectivity / WAN | 52 | 81 | 33 | 45 |
| print / mail / hybrid mail | 37 | 59 | 21 | 35 |
| cyber security / SOC / penetration testing | 63 | 54 | 20 | 53 |
| microsoft / software licensing reseller | 134 | 52 | 19 | 104 |
| HR and payroll system | 83 | 49 | 21 | 73 |
| case management system | 56 | 36 | 23 | 41 |
| telephony / contact centre | 52 | 35 | 15 | 48 |
| cloud hosting / data centre | 54 | 35 | 10 | 43 |
| CRM / customer portal | 27 | 25 | 10 | 25 |
| website / CMS | 23 | 23 | 15 | 20 |
| e-procurement / contract management system | 21 | 20 | 12 | 18 |
| finance / ledger system | 29 | 19 | 6 | 28 |
| asset / facilities management (CAFM) | 27 | 18 | 10 | 27 |
| electronic patient record / patient administration | 23 | 17 | 3 | 18 |
| learning management / e-learning | 23 | 17 | 8 | 22 |
| digital dictation / speech recognition / ambient voice | 16 | 17 | 14 | 13 |
| parking / enforcement system | 21 | 17 | 6 | 19 |
| document / records management | 15 | 13 | 3 | 13 |
| data warehouse / BI / analytics | 17 | 13 | 4 | 14 |
| school MIS / education management | 23 | 11 | 4 | 18 |
| managed IT service / service desk | 13 | 11 | 5 | 13 |
| planning / regulatory services system | 15 | 10 | 5 | 14 |
| social care system | 18 | 10 | 5 | 16 |
| e-rostering / workforce rostering | 12 | 8 | 2 | 12 |
| housing management system | 12 | 8 | 5 | 11 |
| library management system | 9 | 6 | 2 | 9 |
| laboratory information (LIMS) | 7 | 5 | 4 | 6 |
| revenues and benefits system | 10 | 3 | 1 | 10 |
| imaging (PACS/RIS) | 4 | 3 | 1 | 4 |

## Reading
- Enough vendors for a category test (40 or more): CCTV and body-worn video, networks, print and mail, cyber security, Microsoft licensing, HR and payroll. Case management is close (36).
- Cyber security is a poor fit for statutory requests: public bodies commonly withhold security details.
- CCTV has the most small vendors (82), which suits a low-priced regional renewal list. HR and payroll has the most buyers per vendor but is dominated by large vendors who already buy intelligence.
- These counts identify vendors (the customers). The buyers to be asked are the whole population of public bodies, not only those with a notice.
- Not yet done: proper classification of titles, a check of what Stotles and Tussell already show for each category, and the re-use terms for released information.
