# Privacy Quarantine & Netbird Mesh Architecture Specification

## 1. Executive Summary & Objective

The public flagship domain `executivefunctionos.com` is pivoting exclusively to the Work-to-Rhythm software product for executive function, cognitive context management, and developer memory.

Currently, the `ExecutiveFunctionOS_Web` repository and public deployment history contain sensitive case-derived records, municipal grievance registries, thermal forensics, and personal litigation timelines. This document outlines the staged, zero-loss quarantine plan to separate commercial SaaS assets from private legal/forensic assets using an encrypted Netbird overlay mesh network.

## 2. Inventory of Sensitive Case Assets

### High-Sensitivity Litigation & Evidence Pages (in `ExecutiveFunctionOS_Web`)
* `citizen-grievance-registry.html` (116 KB): Municipal complaints and grievance records.
* `dossier.html` (26 KB) and `dossier-washington.html` (1.4 KB): Individual dossiers and case investigations.
* `timeline.html` (716 KB): Exhaustive chronological litigation timeline and incident tracking.
* `chapin-thermal.html` (115 KB) & `forensic-microclimate.html` (115 KB): Forensic thermal evidence and housing habitability measurements.
* `privity.html` & `privity-paradox.html` (39 KB): Legal briefs and contractual liability analyses.
* `paladin.html` & `why-paladin.html`: Public-interest litigation and civic defense tooling narratives.

### Sensitive Internal Artifacts (in `~/projects/paladin/`)
* `projects/paladin/data/`: Structured evidence exports, entity graphs, and case databases.
* `projects/paladin/docs/`: Internal litigation briefs and statutory analyses.
* `projects/paladin/reports/`: Forensic case audit reports.

## 3. The Netbird Quarantine Architecture

Netbird provides an open-source, zero-trust WireGuard mesh network connecting Annika's machines, private staging environments, and trusted local/remote services without opening public firewall ports.

### Network Topology
1. **Public Zone (Internet-Facing)**:
   * **Domain**: `https://executivefunctionos.com`
   * **Host**: Netlify CDN.
   * **Scope**: Commercial Work-to-Rhythm landing page, waitlist form, feature explanations, and public documentation. Zero litigation records or personal evidence.
2. **Private Mesh Zone (Netbird Overlay)**:
   * **Network**: Private 100.x.x.x WireGuard overlay mesh managed by Netbird.
   * **Host**: Local machine or private container serving PALaDIN / Case Intelligence on internal port (e.g., `100.x.x.x:8080`).
   * **Scope**: Complete litigation archive, interactive forensic microclimate analyzers, grievance registry, and court timeline tools.
   * **Access Control**: Strictly restricted to peer-authenticated devices enrolled in Annika's Netbird account.

## 4. Phased Migration & Reversibility Gate

To adhere strictly to Annika's safety rules (reversibility, no unapproved data deletion, no premature route cuts), migration will follow four gated phases:

### Phase 1: Local Segregation & Archive Build
* Clone sensitive HTML pages and paladin assets into a dedicated, private git repository (e.g. `paladin-case-vault`).
* Keep the existing files on a preserved git tag / archive branch (`archive/pre-quarantine-v1`) in `ExecutiveFunctionOS_Web` so nothing is ever lost.

### Phase 2: Netbird Mesh Configuration & Internal Service Standup
* Provision Netbird peer on Annika's workstation.
* Set up a lightweight local static server or Caddy instance listening exclusively on the Netbird interface (`100.x.x.x`).
* Verify that all case pages (`timeline.html`, `dossier.html`, `citizen-grievance-registry.html`) load cleanly with full fidelity across the private mesh.

### Phase 3: Public Web Root Cleanup & Redirect Auditing
* On a clean branch (`feat/commercial-saas-root`), remove the case files from the public build root of `ExecutiveFunctionOS_Web`.
* Configure Netlify `_redirects` to return clean 404s or redirect legacy URLs to an explanatory placeholder, preventing broken links or public search engines from surfacing cached records.
* Deploy to a Netlify deploy preview for Annika's formal approval.

### Phase 4: Production Cutover
* Once Annika signs off on the preview and confirms the Netbird private vault is functioning, merge `feat/commercial-saas-root` to `main`.
* The public site becomes 100% clean, professional, and compliant with commercial privacy standards.

## 5. Security & Verification Guardrails
* **No Exfiltration**: Credentials, tokens, and case records will never be stored or shared via third-party cloud services or public pull requests.
* **Non-Deliverable Test Leads**: All form testing continues using RFC 2606 reserved addresses (`test-lead@example.com`).
* **Audit Trail**: Every branch change is committed with structured git messages, and all team agents (Grok, Larry, Bob) are kept aligned through `grok-mail`.
