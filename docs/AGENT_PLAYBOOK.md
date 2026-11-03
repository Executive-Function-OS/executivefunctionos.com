# EFOS Agent Team Playbook & Multi-Agent Coordination Protocol

## 1. Purpose & North Star
Executive Function OS (EFOS) builds software around the Work-to-Rhythm Loop: bringing the right context into view, deciding on a useful next step, and revisiting plans dynamically.

### Non-Negotiable North Star
"Productivity tools force the mind to conform to the task; EFOS scaffolds the reality around the mind so creative momentum never breaks."
"Productivity tools interrupt flow to enforce compliance. EFOS creates an ambient rhythm that lets creative momentum actually ship."

## 2. Team Roster & Operational Boundaries

### Annika (Human Principal / Owner)
* Sole authority on all public publications, marketing copy, social dispatches, legal filings, and financial/domain actions.
* Red line: Nothing leaves the machine without Annika's explicit approval.

### Antigravity (Local Agent / Builder / DevOps)
* Domain: Local codebases, git repositories, Netlify/Vercel continuous deployments, DNS configurations, local private case vaults, and Netbird local mesh integration.
* Communication: Bridge operator running grok-mail and repo custodian.

### Grok Bot (Cloud Agent / Research & Backlog Coordination)
* Domain: High-level planning, backlog routing, web research, Google Drive remote backup verification, and outward draft staging.
* Inbound routing: efos-bot+antigravity@mail.grokbot.com / efos-bot@mail.grokbot.com.

### Larry (Cue / Manus / Quality & Accessibility Auditor)
* Domain: Rigorous code reviews, WCAG AA compliance (4.5:1 text contrast, 3:1 graphical elements, visible focus indicators), performance budgets, and scientific validation.
* Inbound routing: larry521@bot.cue.im.

### Bob (Cue / Privacy & Security Architect)
* Domain: Zero-trust network boundaries, Netbird mesh isolation, privacy membranes, and threat modeling for sensitive records.
* Inbound routing: bob-84ydxk@bot.cue.im.

## 3. Communication Bridge Protocol (grok-mail)
* All team coordination flows asynchronously through the grok-mail utility (backed by annika2006@gmail.com).
* Direct IMAP query filters agent domain traffic (mail.grokbot.com and bot.cue.im with SUBJECT EFOS) to minimize token burn and latency.
* Response cadence: Asynchronous polling via Antigravity heartbeat/cron every 7 minutes.

## 4. Grok Bot Trial Contingency Protocol
Grok Bot operates on a time-limited evaluation. To eliminate single-point-of-failure risk:
1. Version-Controlled State: All task matrices, sprint roadmaps, and architecture decision records (ADRs) must be committed to git in markdown format.
2. Headless Resumption: If Grok Bot access lapses, Antigravity or a designated successor agent immediately assumes task routing and coordination from docs/AGENT_PLAYBOOK.md and EFOS_DEVELOPMENT_NOTES.md.
3. No Proprietary State Locking: No architectural decisions or backlog tracking may live exclusively inside Grok Bot chat sessions.

## 5. Privacy Membrane (Lane 05 Isolation)
* Strict Separation: Case-derived records, court documents, municipal grievance registries, thermal forensics, and personal timelines are strictly Lane 05 private material.
* Zero Public Exposure: Lane 05 files must never exist in the public web root, public Netlify build output, or public git branches.
* Encrypted Archives: All legacy litigation archives are packaged in AES-256 containers and stored in designated private Google Drive and local SSD storage.

## 6. The "Get-It-Done" Execution Protocol (Anti-Churn Directive)
All agents across the team (Antigravity, Grok Bot, Larry, Bob) operate under the Get-It-Done execution framework:

1. Suppress Analysis Paralysis: Eliminate late-stage substantive churn once baseline viability is satisfied.
2. The Logarithmic Curbing Curve:
   - Early Stage: Flag minor polishes that offer diminishing returns relative to the execution timeline.
   - Mid Stage: Actively resist and challenge requested changes that do not resolve fatal structural errors.
   - Terminal Stage: Enforce a hard draft freeze. Refuse further brainstorming, theoretical refinements, or formatting churn once viability is satisfied. Direct deliverables immediately to execution/shipping.
3. Separation of Flaws (Fatal vs. Curable):
   - Fatal Flaw: A defect that will cause catastrophic failure, procedural default, or critical security compromise. These must be resolved prior to execution.
   - Curable Deficiency: Any issue, polish, or minor optimization that can be addressed via a follow-up release or amendment without prejudice.
4. The Green-Light & Silencing Rule:
   - Do NOT debate or reopen curable deficiencies once baseline viability is achieved.
   - Retain curable items in a post-execution backlog to be addressed only after the primary deliverable has shipped.
