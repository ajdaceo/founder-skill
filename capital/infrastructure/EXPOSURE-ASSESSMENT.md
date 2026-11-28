# What the public repository exposed (assessed 2026-11-28)

**Summary: no sign that anyone looked, and no secrets or identity details were in it. The commercial material and one file of contact addresses were publicly reachable for about a day. The fix is a private repository and then removing the public branch.**

## Facts [verified today unless marked]
- The CAPITAL records sit in `ajdaceo/founder-skill`, which is public and is a **fork** of another person's public repository. GitHub does not allow a fork to be made private.
- They are on the branch `claude/wizardly-noether-26a3n7` only, not on the default branch `main`. First pushed 27 November 2026.
- GitHub's own traffic log: **0 views and 0 visitors** in the 14 days to 26 November. Two clones by one client on 21 November, before the folder existed. Stars 0, forks 0, watchers 0. GitHub's log runs a day or two behind, so 27 and 28 November are not reported yet; I will re-read it after the move.
- Our own scheduled sessions clone the repository, so future clone counts will include them.
- GitHub's code search covers default branches only (general knowledge, not re-checked today), so the branch was not searchable there. Whether a web search engine has crawled it was not tested.

## What was reachable
| Kind | Detail | Sensitivity |
|---|---|---|
| Commercial | Mandate and your instructions as written, experiment designs, prices, draft messages, competitor notes, three prospect lists (213, 28, 22 companies) and the E6 product list itself | Moderate. It would let a competitor copy the approach and undermines "sold to five firms" for E6 |
| Contact addresses | One research file held 115 addresses copied from official award notices, about 30 naming a person. All are already published in those notices | Low, but unnecessary. **Removed from the current files today**; still in the branch history |
| Identifiers | A scheduled-task ID and an environment ID in notes | Low. They are not credentials |
| Not present | Secrets, keys, passwords, bank or identity details, your name, address or email, customer data | n/a |

## Assessment
- Likelihood that someone saw it: low. Impact if they did: moderate for E6, low otherwise.
- Data protection, on my reading and not as legal advice: the addresses were already public and no harm to anyone is likely, so this is a matter to record, not to report. It is recorded here.

## Actions
1. Done: addresses removed from the current files; E6 is blocked until the list is in a private repository; operator instructions now forbid writing personal or customer data to the repository.
2. You: create a private repository (set-up guide, step A). I copy the records across as a clean first commit, without the history.
3. You, after I confirm the copy is complete and pushing works: delete the public branch `claude/wizardly-noether-26a3n7` (GitHub, Branches, bin icon), or tell me to. This is irreversible, so I will not do it unasked.
4. Optional: old commits in a fork can stay reachable by their exact ID for a time after deletion. A request to GitHub Support clears them. I judge this unnecessary unless the traffic log later shows visitors.
