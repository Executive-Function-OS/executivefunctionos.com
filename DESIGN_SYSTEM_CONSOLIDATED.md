# EFOS Master Design System: Warm Paper & Looking-Glass Architecture

Unified specification for the PALADIN umbrella: one structural system, two divisional voices. Harmonizes the public Work-to-Rhythm landing page (warm paper-and-ink) with the Looking-Glass 2.0 / Canva AI systems-thinking architecture, and assigns each product division a home mode and leading accent.

## 1. Principles & Ethos

* **Core Essence**: Structural Clarity & Dynamic Resonance.
* **Guiding Axiom**: Utility over ornament. Signals must be scannable, clear, and actionable. Carroll's wit lives in structure, naming, and typography, never in competing decoration.
* **Dual Modes** (shared by both divisions):
  * **Daylight Mode (Calm Reading & Onboarding)**: Grounded in tactile, warm paper-and-ink tones that reduce visual fatigue and cognitive overstimulation.
  * **Looking-Glass Mode (Deep Focus & Systems Modeling)**: Grounded in Deep Slate (`#0F172A`) with high-contrast mathematical accents (Cheshire Teal, White Rabbit Gold, Vellum).

## 2. Divisions

The umbrella holds two divisions. They share the skeleton (grid, type stack, hairlines, focus ring, mark system) and differ only in **home mode**, **leading accent**, and **voice**. Same structure, different signal — that is the intended "slight variation."

### 2.1 Precedent Systems — complexity outside

* **Scope**: Free, open-source, self-hosted, privacy-preserving, auditable public-interest tooling. Funded by grants, never by sales of the tools.
* **Products**: FormGuide → JustiTeX → DocSplit (one workflow). Also PALADIN, hyperRAG, and the Privity Paradox tool (tentative assignment pending confirmation).
* **Home mode**: **Daylight.** Warm paper, ink, cream plates. Should read like a well-set court document and a public ledger — not a SaaS product.
* **Leading accent**: Spruce (`#2F5D50`) for action. White Rabbit Gold (`#92400E`) reserved for warnings and thresholds.
* **Typography**: Serif-forward — EB Garamond (or the property's equivalent editorial serif, e.g. Merriweather in JustiTeX) for narrative. Sans and mono play supporting roles.
* **Voice cues**: Openness worn openly — mono metadata like "runs on your machine", "no central storage", "auditable". Visible structure, visible provenance.

### 2.2 EFOS — complexity inside

* **Scope**: The commercial layer. Sells convenience, integration, analysis, and decision support built around the free tools — never access to the tools themselves.
* **Products**: Percolation Engine (percolation-import), Work-to-Rhythm Loop, the executivefunctionos.com commercial pages and store.
* **Home mode**: **Looking-Glass.** Deep Slate `#0F172A`, Cheshire Teal signals, gold thresholds. Should feel like a decision-grade instrument for one person's mind.
* **Leading accent**: Cheshire Teal (`#2DD4BF` on slate; `#0D9488` Signal Teal on paper) for signals and data. Red Queen (`#FDA4AF`) for over-threshold states in the simulator and battle-map.
* **Typography**: Sans-forward — Space Grotesk (or Geist) for UI, mono for metrics and token metadata. Serif reserved for narrative explainers.
* **Voice cues**: N=1 framing — singular, decision-grade, one real person's workflow. High signal density.

### 2.3 Cross-division bridge

Someone facing a huge litigation record has both problems at once. Cross-links between divisions use one shared card component: same hairline border, same mono label style, re-accented per context (Spruce chip on EFOS pages, Cheshire Teal chip on Precedent pages).

## 3. Color Architecture & Verified WCAG Ratios

### Daylight Mode (Paper & Ink Baseline) — Precedent Systems home
* **Canvas Grounding (`--color-canvas`)**: `#F6F1E7` (Warm light paper)
* **Surface Card (`--color-surface`)**: `#FFFDF8` (Soft cream plate)
* **Alt Surface (`--color-surface-alt`)**: `#EFE8DA`
* **Primary Ink (`--color-ink`)**: `#1F2A27` (Deep slate ink) — **13.15:1 AAA** on `#F6F1E7`
* **Muted Text (`--color-muted`)**: `#55625D` — **5.67:1 AA** on `#F6F1E7`
* **Action Accent (`--color-accent-action`)**: `#2F5D50` (Spruce green) — **6.66:1 AA** on `#F6F1E7`
* **Focus / White Rabbit Gold (`--color-white-rabbit-gold`)**: `#92400E` (Deep amber) — **6.30:1 AA** on `#F6F1E7` (Darkened from `#B45309` to satisfy the >= 4.5:1 WCAG normal-text threshold)
* **Warm Accent (`--color-warm-accent`)**: `#C47A45` (Terracotta amber) — **3.00:1** (Reserved for non-text decoration, cards, borders, and large display; below 4.5:1 normal-text threshold)
* **Keyboard Focus Indicator (`--sc-btn-focus`)**: `#0D9488` (Signal teal 2px solid ring, 3px offset; preserved across all interactive states)
* **Border Line (`--color-line`)**: `#DDD3C0`

### Looking-Glass Mode (Dark & Focused System) — EFOS home
* **Base Canvas (`--color-canvas`)**: `#0F172A` (Looking-Glass Slate)
* **Board Canvas (`--color-board-slate`)**: `#1B2540` (Alternating cell plate)
* **Surface Card (`--color-surface-card`)**: `#141D30`
* **Primary Text / Vellum (`--color-vellum`)**: `#F5EFE0` — **15.56:1 AAA** on `#0F172A`
* **Signal / Cheshire Teal (`--color-cheshire-teal`)**: `#2DD4BF` — **9.59:1 AAA** on `#0F172A`
* **Focus / White Rabbit Gold (`--color-white-rabbit-gold`)**: `#F59E0B` — **8.31:1 AAA** on `#0F172A`
* **Threshold / Red Queen (`--color-red-queen`)**: `#FDA4AF` — **9.44:1 AAA** on `#0F172A`
* **Structural Line / Brass (`--color-brass-hairline`)**: `#B08D3C` — Decorative/hairlines only.
* *Note on Chalk White*: `#0F172A` against `#F8FAFC` yields **17.06:1 AAA** (corrected from initial 21:1 estimate).

## 4. Typography Stack Hierarchy

* **Editorial / Narrative (`--font-serif`)**:
  `"EB Garamond"`, `"Iowan Old Style"`, `"Palatino Linotype"`, Palatino, Georgia, serif
  * Usage: Hero headlines, narrative explainers, long-form articles, and philosophical axioms.
  * Precedent Systems properties may substitute their established editorial serif (e.g. Merriweather) in the same role.
* **Display & Structural UI (`--font-sans`)**:
  `"Space Grotesk"`, `Inter`, system-ui, -apple-system, sans-serif
  * Usage: Section navigation, interactive buttons, form labels, card headings.
  * EFOS product properties may substitute Geist in the same role.
* **Technical & Metrics (`--font-mono`)**:
  `"JetBrains Mono"`, `"Fira Code"`, monospace
  * Usage: AGENTS.md instructions, token definitions, code blocks, tabular data, status tags.

## 5. Token Mapping Table

How the named EFOS tokens land in each property's variable system. Legacy variable names are kept as aliases so components do not need mass edits; values are re-mapped.

| EFOS token | Daylight value | Looking-Glass value | percolation-import (shadcn var) | JustiTeX (CSS var) |
| --- | --- | --- | --- | --- |
| Canvas | `#F6F1E7` | `#0F172A` | `--background` | page background |
| Surface card | `#FFFDF8` | `#141D30` | `--card` | card background |
| Primary ink / Vellum | `#1F2A27` | `#F5EFE0` | `--foreground` | text color |
| Muted text | `#55625D` | slate-400 equivalent | `--muted-foreground` | secondary text |
| Action accent | `#2F5D50` Spruce | `#2DD4BF` Cheshire Teal | `--primary` (alias `--indigo`) | button/link accent |
| Focus ring | `#0D9488` Signal Teal | `#2DD4BF` | `--ring` | focus outline |
| Warning / threshold | `#92400E` | `#F59E0B` White Rabbit Gold | `--warning` (alias `--orange`) | status warning |
| Threshold over-run | `#B91C1C` | `#FDA4AF` Red Queen | `--destructive` (alias `--red`) | status error |
| Border line | `#DDD3C0` | `#1B2540` board slate | `--border` | hairlines |
| Chart palette | Spruce, Signal Teal, Gold, Terracotta, Muted | Cheshire Teal, Gold, Red Queen, Brass, Vellum | `--chart-1` … `--chart-5` | n/a |

Rule: legacy names (`--indigo`, `--emerald`, `--orange`, `--red`) may remain as aliases but must carry EFOS values. New code uses the EFOS names.

## 6. Portability & Asset Integrity

* All asset imports (CSS, SVGs, favicon, marks) must use strictly relative paths (`./favicon.svg`, `assets/...`) with zero absolute local filesystem references (`file:///home/annika/...`).
* The design system is fully reversible and isolated in git branches (spec: `vibe/umbrella-design-spec-fc7cb3`).
* Mark system: Harmonic Lattice is the umbrella mark; the paladin knight-mark is reserved for umbrella/portal level. Division properties use their own marks within the same grid and hairline language.

## 7. Permanent AI-Safe Static HTML Architecture Rule

All public research, governance, forensic, and legal compendia (including `oregon-city-accountability-research.html`, `dlcd-division47-rulemaking.html`, `retrospective-justice-foreclosure-forensics.html`, `citizen-grievance-registry.html`, `privity-paradox.html`, and related public nodes) must be authored as pure static HTML:
* **Initial HTML Body Completeness**: All core content, tables, evidence classifications, quotes, citations, and findings must be directly present in the initial HTML body with zero dependency on client-side JavaScript.
* **Semantic Elements & Real Tables**: Tabular data, evidence registries, and dockets must use real HTML tables (`<table>`, `<thead>`, `<tbody>`, `<tr>`, `<th>`, `<td>`, `<caption>`). Structure must use semantic elements (`<header>`, `<nav>`, `<main>`, `<section>`, `<article>`, `<blockquote>`, `<q>`, `<h1>`–`<h6>`, `<code>`).
* **Zero Client-Rendered Frameworks**: Do not introduce React, Vue, Svelte, Angular, or client-rendered hydration.
* **Simple Fetch Legibility**: The document must be 100% complete and legible to simple fetch tools (`curl`, Python `urllib`, `wget`, `lynx`) and AI crawlers with no JavaScript execution engine.
* **Progressive Enhancement**: Any script must be strictly non-essential progressive enhancement (such as clipboard copy helpers) that degrades completely without obscuring any content.

