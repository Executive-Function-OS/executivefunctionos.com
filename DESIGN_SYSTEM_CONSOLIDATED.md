# EFOS Master Design System: Warm Paper & Looking-Glass Architecture

Unified specification harmonizing the public Work-to-Rhythm landing page (warm paper-and-ink) with the Looking-Glass 2.0 / Canva AI systems-thinking architecture.

## 1. Principles & Ethos

* **Core Essence**: Structural Clarity & Dynamic Resonance.
* **Guiding Axiom**: Utility over ornament. Signals must be scannable, clear, and actionable. Carroll's wit lives in structure, naming, and typography, never in competing decoration.
* **Dual Modes**:
  * **Daylight Mode (Calm Reading & Onboarding)**: Grounded in tactile, warm paper-and-ink tones that reduce visual fatigue and cognitive overstimulation.
  * **Looking-Glass Mode (Deep Focus & Systems Modeling)**: Grounded in Deep Slate (`#0F172A`) with high-contrast mathematical accents (Cheshire Teal, White Rabbit Gold, Vellum).

## 2. Color Architecture & Verified WCAG Ratios

### Daylight Mode (Paper & Ink Baseline)
* **Canvas Grounding (`--color-canvas`)**: `#F6F1E7` (Warm light paper)
* **Surface Card (`--color-surface`)**: `#FFFDF8` (Soft cream plate)
* **Alt Surface (`--color-surface-alt`)**: `#EFE8DA`
* **Primary Ink (`--color-ink`)**: `#1F2A27` (Deep slate ink) — **14.2:1 AAA** on `#F6F1E7`
* **Muted Text (`--color-muted`)**: `#55625D` — **4.8:1 AA** on `#F6F1E7`
* **Action Accent (`--color-accent-action`)**: `#2F5D50` (Spruce green) — **5.8:1 AA** on `#F6F1E7`
* **Warm Accent (`--color-warm-accent`)**: `#C47A45` (Terracotta amber)
* **Border Line (`--color-line`)**: `#DDD3C0`

### Looking-Glass Mode (Dark & Focused System)
* **Base Canvas (`--color-canvas`)**: `#0F172A` (Looking-Glass Slate)
* **Board Canvas (`--color-board-slate`)**: `#1B2540` (Alternating cell plate)
* **Surface Card (`--color-surface-card`)**: `#141D30`
* **Primary Text / Vellum (`--color-vellum`)**: `#F5EFE0` — **15.56:1 AAA** on `#0F172A`
* **Signal / Cheshire Teal (`--color-cheshire-teal`)**: `#2DD4BF` — **9.59:1 AAA** on `#0F172A`
* **Focus / White Rabbit Gold (`--color-white-rabbit-gold`)**: `#F59E0B` — **8.31:1 AAA** on `#0F172A`
* **Threshold / Red Queen (`--color-red-queen`)**: `#FDA4AF` — **9.44:1 AAA** on `#0F172A`
* **Structural Line / Brass (`--color-brass-hairline`)**: `#B08D3C` — Decorative/hairlines only.
* *Note on Chalk White*: `#0F172A` against `#F8FAFC` yields **17.06:1 AAA** (corrected from initial 21:1 estimate).

## 3. Typography Stack Hierarchy

* **Editorial / Narrative (`--font-serif`)**:
  `"EB Garamond"`, `"Iowan Old Style"`, `"Palatino Linotype"`, Palatino, Georgia, serif
  * Usage: Hero headlines, narrative explainers, long-form articles, and philosophical axioms.
* **Display & Structural UI (`--font-sans`)**:
  `"Space Grotesk"`, `Inter`, system-ui, -apple-system, sans-serif
  * Usage: Section navigation, interactive buttons, form labels, card headings.
* **Technical & Metrics (`--font-mono`)**:
  `"JetBrains Mono"`, `"Fira Code"`, monospace
  * Usage: AGENTS.md instructions, token definitions, code blocks, tabular data, status tags.

## 4. Portability & Asset Integrity

* All asset imports (CSS, SVGs, favicon, marks) must use strictly relative paths (`./favicon.svg`, `assets/...`) with zero absolute local filesystem references (`file:///home/annika/...`).
* The design system is fully reversible and isolated in git branch `feat/unified-design-system`.
