#!/usr/bin/env python3
import os
import re
import json
import html

MD_PATH = '/home/annika/Documents/Federal_Complaint/TIMELINE_OF_ALL_COMMUNICATIONS_WITH_CITY_OFFICIALS.md'
OUT_HTML = '/home/annika/ExecutiveFunctionOS_Web/timeline.html'

def parse_timeline(md_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        text = f.read()

    phase_matches = list(re.finditer(r'^## (\d+\.\s+Phase\s+[IVXLCDM]+:[^\n]+)', text, re.MULTILINE))
    phases = []

    for i, pm in enumerate(phase_matches):
        p_title = pm.group(1).strip()
        p_num = int(re.match(r'^(\d+)\.', p_title).group(1))
        start_pos = pm.end()
        end_pos = phase_matches[i+1].start() if i+1 < len(phase_matches) else len(text)
        phase_content = text[start_pos:end_pos]
        
        entry_chunks = re.split(r'\n(?=### \d+\.\d+ )', phase_content)
        entries = []
        for chunk in entry_chunks:
            chunk = chunk.strip()
            if not chunk.startswith('### '):
                continue
            first_line = chunk.split('\n')[0]
            m = re.match(r'^###\s+(\d+\.\d+)\s+(.+?)\s+—\s+(.+)$', first_line)
            if not m:
                m = re.match(r'^###\s+(\d+\.\d+)\s+(.+)$', first_line)
                item_num = m.group(1) if m else '0'
                date_time = m.group(2) if m else ''
                title = date_time
            else:
                item_num = m.group(1)
                date_time = m.group(2).strip()
                title = m.group(3).strip()
                
            medium = ''
            from_actor = ''
            to_actor = ''
            subject = ''
            summary = ''
            record_source = ''
            
            med_m = re.search(r'\*\s+\*\*Medium:\*\*\s*(.+)', chunk)
            if med_m: medium = med_m.group(1).strip()
            
            from_m = re.search(r'\*\s+\*\*From:\*\*\s*(.+)', chunk)
            if from_m: from_actor = from_m.group(1).strip()
            
            to_m = re.search(r'\*\s+\*\*To:\*\*\s*(.+)', chunk)
            if to_m: to_actor = to_m.group(1).strip()
            
            subj_m = re.search(r'\*\s+\*\*Subject:\*\*\s*(.+)', chunk)
            if subj_m: subject = subj_m.group(1).strip()
            
            summ_m = re.search(r'\*\s+\*\*Summary:\*\*\s*(.+?)(?=\n\*\s+\*\*Record Source:\*\*|\n### |\Z)', chunk, re.DOTALL)
            if summ_m: summary = summ_m.group(1).strip()
            
            rec_m = re.search(r'\*\s+\*\*Record Source:\*\*\s*(.+?)(?=\n### |\Z)', chunk, re.DOTALL)
            if rec_m: record_source = rec_m.group(1).strip()

            # Classify actor category
            all_actors_str = f"{from_actor} {to_actor}".lower()
            actor_cat = "Other / General"
            if any(k in all_actors_str for k in ['konkol', 'troutman', 'rains', 'mcgriff', 'commission', 'marl', 'mitchell', 'o\'donnell', 'smith']):
                actor_cat = "City Leadership"
            elif any(k in all_actors_str for k in ['kennedy', 'wilson', 'kersey', 'code enforcement', 'police', 'band']):
                actor_cat = "Code Enforcement"
            elif any(k in all_actors_str for k in ['oreskovich', 'fraijo', 'berreth', 'utility', 'billing', 'walker', 'wheeler', 'public works', 'sayers']):
                actor_cat = "Public Works & Utilities"
            elif any(k in all_actors_str for k in ['lindgren', 'simpson', 'baseler', 'municipal court', 'clerk']):
                actor_cat = "Municipal Court"
            elif any(k in all_actors_str for k in ['henderson', 'johnson', 'street', 'hodgkinson', 'stouffer', 'cis']):
                actor_cat = "Defense Counsel & CIS"
            elif any(k in all_actors_str for k in ['eriksson', 'buckhout']):
                actor_cat = "Plaintiffs"

            # Classify medium category
            med_lower = medium.lower()
            med_cat = "Other"
            if 'email' in med_lower:
                med_cat = "Email"
            elif any(k in med_lower for k in ['letter', 'notice', 'placard', 'mail', 'written']):
                med_cat = "Notice / Letter"
            elif any(k in med_lower for k in ['phone', 'audio', 'ivr', 'call', 'voicemail']):
                med_cat = "Phone / Audio"
            elif any(k in med_lower for k in ['court', 'filing', 'order', 'pleading', 'subpoena', 'motion']):
                med_cat = "Court Filing / Order"
            elif any(k in med_lower for k in ['in-person', 'inspection', 'standoff', 'visit', 'appeared']):
                med_cat = "In-Person / Inspection"
            elif any(k in med_lower for k in ['records', 'foia', 'pra']):
                med_cat = "Records Request"
            
            entries.append({
                'id': f'comm-{item_num.replace(".", "-")}',
                'item_num': item_num,
                'phase_num': p_num,
                'date_time': date_time,
                'title': title,
                'medium': medium,
                'medium_cat': med_cat,
                'from': from_actor,
                'to': to_actor,
                'actor_cat': actor_cat,
                'subject': subject,
                'summary': summary,
                'record_source': record_source
            })
        phases.append({
            'phase_num': p_num,
            'phase_title': p_title,
            'entries': entries
        })
    return phases

def format_inline_md(text):
    if not text:
        return ""
    t = html.escape(text)
    t = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', t)
    t = re.sub(r'\*(.+?)\*', r'<em>\1</em>', t)
    t = re.sub(r'`(.+?)`', r'<code>\1</code>', t)
    t = re.sub(r'\[(.+?)\]\((file:///[^)]+)\)', r'<span class="file-source-tag">\1</span>', t)
    t = re.sub(r'\[(.+?)\]\((https?://[^)]+)\)', r'<a href="\2" target="_blank" rel="noopener">\1</a>', t)
    paragraphs = t.split('\n\n')
    formatted_p = []
    for p in paragraphs:
        p = p.strip()
        if p.startswith('&gt; '):
            quote_lines = [line.replace('&gt; ', '', 1) for line in p.split('\n')]
            formatted_p.append(f'<blockquote>{"<br>".join(quote_lines)}</blockquote>')
        else:
            p_lines = p.split('\n')
            formatted_p.append(f'<p>{"<br>".join(p_lines)}</p>')
    return ''.join(formatted_p)

def generate_html(phases):
    total_entries = sum(len(p['entries']) for p in phases)
    
    all_entries = []
    for p in phases:
        for e in p['entries']:
            all_entries.append({
                'id': e['id'],
                'item_num': e['item_num'],
                'phase_num': e['phase_num'],
                'phase_title': p['phase_title'],
                'date_time': e['date_time'],
                'title': e['title'],
                'medium': e['medium'],
                'medium_cat': e['medium_cat'],
                'from': e['from'],
                'to': e['to'],
                'actor_cat': e['actor_cat'],
                'subject': e['subject'],
                'summary': e['summary'],
                'summary_html': format_inline_md(e['summary']),
                'record_source': e['record_source'],
                'record_source_html': format_inline_md(e['record_source'])
            })

    entries_json = json.dumps(all_entries)

    # Build options for phases
    phase_options_html = ""
    for p in phases:
        short_title = html.escape(p['phase_title'][:60] + ('...' if len(p['phase_title']) > 60 else ''))
        phase_options_html += f'<option value="{p["phase_num"]}">{short_title}</option>\n'

    # Build timeline stream
    stream_html = ""
    for p in phases:
        stream_html += f"""
        <section class="phase-block" data-phase-num="{p['phase_num']}">
          <div class="phase-header">
            <h2 class="phase-title">{html.escape(p['phase_title'])}</h2>
            <span class="phase-count">{len(p['entries'])} events</span>
          </div>
          <div class="phase-entries">
        """
        for e in p['entries']:
            from_clean = e['from'].replace('`', '')
            to_clean = e['to'].replace('`', '')
            summary_snippet = html.escape(e['summary'][:220] + ('...' if len(e['summary']) > 220 else ''))

            stream_html += f"""
            <article class="event-card" id="{e['id']}" 
                     data-id="{e['id']}"
                     data-phase="{e['phase_num']}"
                     data-actor-cat="{e['actor_cat']}"
                     data-medium-cat="{e['medium_cat']}"
                     onclick="openEventDrawer('{e['id']}')">
              <div class="card-meta-line">
                <span class="badge-item">Item {e['item_num']}</span>
                <span class="badge-date">{html.escape(e['date_time'])}</span>
                <span class="badge-medium">{html.escape(e['medium'])}</span>
                <span class="badge-actor">{html.escape(e['actor_cat'])}</span>
              </div>
              <h3 class="card-title">{html.escape(e['title'])}</h3>
              <div class="card-participants">
                <strong>From:</strong> {html.escape(from_clean)} &bull; <strong>To:</strong> {html.escape(to_clean)}
              </div>
              <div class="card-summary-snippet">{summary_snippet}</div>
              <div class="card-footer">
                <span class="view-record-trigger">View full record &rarr;</span>
                <button type="button" class="copy-link-btn" onclick="copyCardLink(event, '{e['id']}')" title="Copy permanent link to this entry">
                  &sect; Copy Anchor
                </button>
              </div>
            </article>
            """
        stream_html += """
          </div>
        </section>
        """

    template = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Municipal Communications Timeline &bull; Evidentiary Record (2023–2026)</title>
  <meta name="description" content="Searchable, point-and-click chronological index and verbatim evidentiary record of 98 communications between Annika Eriksson, Donald Buckhout, and Oregon City officials.">
  <link rel="icon" type="image/svg+xml" href="favicon-paladin.svg">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Charter:ital,wght@0,400;0,700;1,400&family=Fira+Code:wght@400;500;600&family=Inter:wght@400;500;600;700;800&family=JetBrains+Mono:wght@400;500;600;700&family=Space+Grotesk:wght@500;600;700;800&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="tokens.css">
  <link rel="stylesheet" href="kinetic_clarity_buttons.css">

  <style>
    :root {
      --paladin-paper: #F3EADC;
      --paladin-paper-subtle: #FAF6EE;
      --paladin-ink: #1C1710;
      --paladin-ink-muted: #574F44;
      --paladin-teal: #1F5F58;
      --paladin-teal-light: #EBF4F3;
      --paladin-terracotta: #C45C3E;
      --paladin-terracotta-light: #FBF0ED;
      --paladin-rule: rgba(28, 23, 16, 0.16);
      --paladin-rule-strong: rgba(31, 95, 88, 0.35);
      --paladin-amber: #D97706;
      --paladin-slate: #0F172A;
    }

    * { box-sizing: border-box; margin: 0; padding: 0; }

    html {
      scroll-behavior: smooth;
      background-color: var(--paladin-paper);
    }

    body {
      background-color: var(--paladin-paper);
      color: var(--paladin-ink);
      font-family: var(--font-editorial, 'Charter', Georgia, serif);
      line-height: 1.6;
      font-size: 1.05rem;
      position: relative;
    }

    body::before {
      content: "";
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background-image: 
        linear-gradient(to right, rgba(31, 95, 88, 0.03) 1px, transparent 1px),
        linear-gradient(to bottom, rgba(28, 23, 16, 0.035) 1px, transparent 1px);
      background-size: 24px 24px;
      pointer-events: none;
      z-index: 0;
    }

    .container {
      max-width: 1240px;
      margin: 0 auto;
      padding: 0 1.25rem;
      position: relative;
      z-index: 1;
    }

    /* Header & Navigation */
    header {
      position: sticky;
      top: 0;
      background: rgba(243, 234, 220, 0.96);
      backdrop-filter: blur(10px);
      border-bottom: 2px solid var(--paladin-teal);
      z-index: 100;
      box-shadow: 0 2px 10px rgba(28, 23, 16, 0.06);
    }

    .nav-container {
      max-width: 1240px;
      margin: 0 auto;
      padding: 0.85rem 1.25rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 1rem;
    }

    .brand-link {
      display: flex;
      align-items: center;
      gap: 0.75rem;
      text-decoration: none;
      color: var(--paladin-ink);
    }

    .brand-logo-img {
      width: 40px;
      height: 40px;
      border-radius: 8px;
      box-shadow: 0 2px 5px rgba(28, 23, 16, 0.2);
    }

    .brand-title {
      font-family: var(--font-display, 'Space Grotesk', sans-serif);
      font-size: 1.25rem;
      font-weight: 800;
      letter-spacing: 0.08em;
      color: var(--paladin-ink);
      line-height: 1;
    }

    .brand-sub {
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.65rem;
      color: var(--paladin-teal);
      letter-spacing: 0.06em;
      margin-top: 0.2rem;
      text-transform: uppercase;
      font-weight: 600;
    }

    .paladin-nav-links {
      display: flex;
      gap: 1.1rem;
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.82rem;
      font-weight: 600;
      letter-spacing: 0.04em;
    }

    .paladin-nav-links a {
      color: var(--paladin-ink);
      text-decoration: none;
      transition: color 0.15s ease;
      padding: 0.25rem 0.2rem;
    }

    .paladin-nav-links a.active {
      color: var(--paladin-teal);
      border-bottom: 2px solid var(--paladin-teal);
      font-weight: 700;
    }

    .paladin-nav-links a:hover {
      color: var(--paladin-terracotta);
    }

    /* Hero */
    .timeline-hero {
      padding: 2.5rem 0 1.5rem;
      border-bottom: 1px solid var(--paladin-rule);
    }

    .case-banner {
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem 1.2rem;
      margin-bottom: 1rem;
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.78rem;
    }

    .case-chip {
      display: inline-flex;
      align-items: center;
      gap: 0.4rem;
      background: rgba(31, 95, 88, 0.08);
      border: 1px solid var(--paladin-rule-strong);
      padding: 0.25rem 0.65rem;
      border-radius: 4px;
      color: var(--paladin-ink);
    }

    .case-chip strong {
      color: var(--paladin-teal);
      font-weight: 700;
    }

    .hero-title {
      font-family: var(--font-display, 'Space Grotesk', sans-serif);
      font-size: clamp(1.8rem, 4vw, 2.5rem);
      font-weight: 800;
      letter-spacing: -0.02em;
      line-height: 1.15;
      color: var(--paladin-ink);
      margin-bottom: 0.6rem;
    }

    .hero-subtitle {
      font-size: 1.1rem;
      color: var(--paladin-ink-muted);
      max-width: 880px;
      line-height: 1.5;
      margin-bottom: 1.5rem;
    }

    /* Stat bar */
    .stats-strip {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(140px, 1fr));
      gap: 0.85rem;
      margin-top: 1rem;
    }

    .stat-box {
      background: var(--paladin-paper-subtle);
      border: 1px solid var(--paladin-rule);
      border-left: 3px solid var(--paladin-teal);
      padding: 0.65rem 0.85rem;
      border-radius: 4px;
    }

    .stat-number {
      font-family: var(--font-display, 'Space Grotesk', sans-serif);
      font-size: 1.45rem;
      font-weight: 800;
      color: var(--paladin-teal);
      line-height: 1;
    }

    .stat-label {
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.72rem;
      color: var(--paladin-ink-muted);
      text-transform: uppercase;
      letter-spacing: 0.04em;
      margin-top: 0.35rem;
    }

    /* Filter & Control Bar (Sticky) */
    .controls-wrapper {
      position: sticky;
      top: 61px;
      z-index: 90;
      background: rgba(243, 234, 220, 0.98);
      backdrop-filter: blur(8px);
      border-bottom: 1.5px solid var(--paladin-teal);
      padding: 0.85rem 0;
      box-shadow: 0 4px 12px rgba(28, 23, 16, 0.05);
      margin-bottom: 2rem;
    }

    .controls-grid {
      display: flex;
      flex-wrap: wrap;
      gap: 0.6rem 0.85rem;
      align-items: center;
    }

    .search-input-box {
      flex: 1 1 240px;
      position: relative;
    }

    .search-input-box input {
      width: 100%;
      padding: 0.6rem 2.2rem 0.6rem 0.85rem;
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.85rem;
      background: #FFFFFF;
      border: 1px solid var(--paladin-rule-strong);
      border-radius: 4px;
      color: var(--paladin-ink);
      outline: none;
      transition: border-color 0.15s ease, box-shadow 0.15s ease;
    }

    .search-input-box input:focus {
      border-color: var(--paladin-teal);
      box-shadow: 0 0 0 3px rgba(31, 95, 88, 0.15);
    }

    .search-clear-btn {
      position: absolute;
      right: 0.65rem;
      top: 50%;
      transform: translateY(-50%);
      background: none;
      border: none;
      font-size: 1.1rem;
      color: var(--paladin-ink-muted);
      cursor: pointer;
      display: none;
    }

    .filter-select {
      padding: 0.58rem 0.75rem;
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.8rem;
      background: #FFFFFF;
      border: 1px solid var(--paladin-rule-strong);
      border-radius: 4px;
      color: var(--paladin-ink);
      outline: none;
      cursor: pointer;
    }

    .filter-select:focus {
      border-color: var(--paladin-teal);
    }

    .reset-filters-btn {
      padding: 0.55rem 0.9rem;
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.78rem;
      font-weight: 600;
      background: transparent;
      border: 1px solid var(--paladin-terracotta);
      color: var(--paladin-terracotta);
      border-radius: 4px;
      cursor: pointer;
      transition: background 0.15s, color 0.15s;
    }

    .reset-filters-btn:hover {
      background: var(--paladin-terracotta);
      color: #FFFFFF;
    }

    .counter-badge {
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.75rem;
      color: var(--paladin-teal);
      font-weight: 700;
      margin-left: auto;
      white-space: nowrap;
    }

    /* Timeline Stream & Phase Blocks */
    .timeline-stream {
      display: flex;
      flex-direction: column;
      gap: 2.5rem;
      padding-bottom: 5rem;
    }

    .phase-block {
      position: relative;
    }

    .phase-header {
      background: #1C1710;
      color: #F8FAFC;
      padding: 0.85rem 1.25rem;
      border-radius: 6px 6px 0 0;
      border-left: 6px solid var(--paladin-terracotta);
      display: flex;
      flex-wrap: wrap;
      justify-content: space-between;
      align-items: center;
      gap: 0.5rem;
    }

    .phase-title {
      font-family: var(--font-display, 'Space Grotesk', sans-serif);
      font-size: 1.15rem;
      font-weight: 700;
      letter-spacing: 0.02em;
    }

    .phase-count {
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.75rem;
      color: rgba(248, 250, 252, 0.75);
      background: rgba(255, 255, 255, 0.12);
      padding: 0.2rem 0.5rem;
      border-radius: 4px;
    }

    .phase-entries {
      display: flex;
      flex-direction: column;
      gap: 0.85rem;
      padding: 1rem 0;
      border-left: 2px solid rgba(31, 95, 88, 0.25);
      margin-left: 1.25rem;
      padding-left: 1.25rem;
    }

    /* Event Card */
    .event-card {
      background: #FFFFFF;
      border: 1px solid var(--paladin-rule);
      border-radius: 6px;
      padding: 1.15rem;
      position: relative;
      transition: transform 0.15s ease, box-shadow 0.15s ease, border-color 0.15s ease;
      cursor: pointer;
    }

    .event-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 5px 15px rgba(28, 23, 16, 0.08);
      border-color: var(--paladin-teal);
    }

    .event-card.active-target {
      border-color: var(--paladin-terracotta);
      box-shadow: 0 0 0 3px rgba(196, 92, 62, 0.2);
    }

    .event-card::before {
      content: "";
      position: absolute;
      left: -1.75rem;
      top: 1.4rem;
      width: 12px;
      height: 12px;
      border-radius: 50%;
      background: #FFFFFF;
      border: 3px solid var(--paladin-teal);
      transition: background 0.15s ease, transform 0.15s ease;
    }

    .event-card:hover::before {
      background: var(--paladin-teal);
      transform: scale(1.2);
    }

    .card-meta-line {
      display: flex;
      flex-wrap: wrap;
      align-items: center;
      gap: 0.45rem 0.75rem;
      margin-bottom: 0.5rem;
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.75rem;
    }

    .badge-item {
      background: var(--paladin-slate);
      color: #F8FAFC;
      font-weight: 700;
      padding: 0.2rem 0.5rem;
      border-radius: 3px;
    }

    .badge-date {
      color: var(--paladin-terracotta);
      font-weight: 700;
    }

    .badge-medium {
      background: rgba(31, 95, 88, 0.1);
      color: var(--paladin-teal);
      border: 1px solid rgba(31, 95, 88, 0.25);
      padding: 0.15rem 0.45rem;
      border-radius: 3px;
    }

    .badge-actor {
      background: rgba(217, 119, 6, 0.1);
      color: #B45309;
      border: 1px solid rgba(217, 119, 6, 0.25);
      padding: 0.15rem 0.45rem;
      border-radius: 3px;
    }

    .card-title {
      font-family: var(--font-display, 'Space Grotesk', sans-serif);
      font-size: 1.15rem;
      font-weight: 700;
      line-height: 1.3;
      color: var(--paladin-ink);
      margin-bottom: 0.5rem;
    }

    .card-participants {
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.78rem;
      color: var(--paladin-ink-muted);
      margin-bottom: 0.65rem;
      line-height: 1.4;
    }

    .card-participants strong {
      color: var(--paladin-ink);
    }

    .card-summary-snippet {
      font-size: 0.95rem;
      color: #334155;
      line-height: 1.55;
      margin-bottom: 0.85rem;
      display: -webkit-box;
      -webkit-line-clamp: 3;
      -webkit-box-orient: vertical;
      overflow: hidden;
    }

    .card-footer {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding-top: 0.65rem;
      border-top: 1px solid rgba(28, 23, 16, 0.08);
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.75rem;
    }

    .view-record-trigger {
      color: var(--paladin-teal);
      font-weight: 700;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      transition: color 0.15s;
    }

    .event-card:hover .view-record-trigger {
      color: var(--paladin-terracotta);
    }

    .copy-link-btn {
      background: none;
      border: none;
      color: var(--paladin-ink-muted);
      cursor: pointer;
      padding: 0.2rem 0.4rem;
      border-radius: 3px;
      font-size: 0.72rem;
      transition: background 0.15s, color 0.15s;
    }

    .copy-link-btn:hover {
      background: rgba(31, 95, 88, 0.1);
      color: var(--paladin-teal);
    }

    /* Slide-Over Drawer */
    .drawer-backdrop {
      position: fixed;
      top: 0; left: 0; width: 100%; height: 100%;
      background: rgba(15, 23, 42, 0.55);
      backdrop-filter: blur(4px);
      z-index: 200;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.25s ease;
    }

    .drawer-backdrop.open {
      opacity: 1;
      pointer-events: auto;
    }

    .slide-drawer {
      position: fixed;
      top: 0; right: 0;
      width: min(720px, 92vw);
      height: 100%;
      background: #FFFFFF;
      box-shadow: -8px 0 25px rgba(15, 23, 42, 0.2);
      z-index: 210;
      display: flex;
      flex-direction: column;
      transform: translateX(100%);
      transition: transform 0.28s cubic-bezier(0.16, 1, 0.3, 1);
    }

    .slide-drawer.open {
      transform: translateX(0);
    }

    .drawer-header {
      background: #1C1710;
      color: #F8FAFC;
      padding: 1.25rem 1.5rem;
      border-bottom: 2px solid var(--paladin-teal);
      display: flex;
      justify-content: space-between;
      align-items: flex-start;
      gap: 1rem;
    }

    .drawer-title-area h3 {
      font-family: var(--font-display, 'Space Grotesk', sans-serif);
      font-size: 1.25rem;
      font-weight: 700;
      line-height: 1.25;
      margin-bottom: 0.35rem;
    }

    .drawer-meta-badges {
      display: flex;
      flex-wrap: wrap;
      gap: 0.4rem;
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.72rem;
    }

    .drawer-close-btn {
      background: rgba(255, 255, 255, 0.1);
      border: none;
      color: #F8FAFC;
      width: 32px;
      height: 32px;
      border-radius: 50%;
      display: flex;
      align-items: center;
      justify-content: center;
      font-size: 1.3rem;
      cursor: pointer;
      transition: background 0.15s, transform 0.15s;
    }

    .drawer-close-btn:hover {
      background: var(--paladin-terracotta);
      transform: rotate(90deg);
    }

    .drawer-body {
      flex: 1;
      overflow-y: auto;
      padding: 1.5rem;
      background: var(--paladin-paper-subtle);
    }

    .drawer-meta-table {
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 1.5rem;
      background: #FFFFFF;
      border: 1px solid var(--paladin-rule);
      border-radius: 6px;
      overflow: hidden;
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.8rem;
    }

    .drawer-meta-table td {
      padding: 0.55rem 0.85rem;
      border-bottom: 1px solid rgba(28, 23, 16, 0.08);
      vertical-align: top;
    }

    .drawer-meta-table td:first-child {
      width: 110px;
      font-weight: 700;
      color: var(--paladin-teal);
      background: rgba(31, 95, 88, 0.04);
      border-right: 1px solid rgba(28, 23, 16, 0.08);
    }

    .drawer-section-heading {
      font-family: var(--font-display, 'Space Grotesk', sans-serif);
      font-size: 0.95rem;
      font-weight: 800;
      text-transform: uppercase;
      letter-spacing: 0.06em;
      color: var(--paladin-ink);
      margin: 1.5rem 0 0.65rem;
      display: flex;
      align-items: center;
      gap: 0.5rem;
    }

    .drawer-section-heading::after {
      content: "";
      flex: 1;
      height: 1px;
      background: var(--paladin-rule);
    }

    .drawer-summary-box {
      background: #FFFFFF;
      border: 1px solid var(--paladin-rule);
      border-left: 3px solid var(--paladin-teal);
      padding: 1.15rem;
      border-radius: 4px;
      font-size: 1rem;
      line-height: 1.65;
      color: #1E293B;
    }

    .drawer-summary-box p {
      margin-bottom: 0.85rem;
    }

    .drawer-summary-box p:last-child {
      margin-bottom: 0;
    }

    .drawer-summary-box blockquote {
      border-left: 3px solid var(--paladin-terracotta);
      background: rgba(196, 92, 62, 0.05);
      padding: 0.65rem 0.85rem;
      margin: 0.85rem 0;
      font-style: italic;
      color: var(--paladin-ink);
    }

    .drawer-summary-box code {
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.85em;
      background: rgba(15, 23, 42, 0.06);
      padding: 0.1rem 0.35rem;
      border-radius: 3px;
    }

    .drawer-source-box {
      background: #FFFFFF;
      border: 1px solid var(--paladin-rule);
      border-left: 3px solid var(--paladin-amber);
      padding: 0.85rem 1.15rem;
      border-radius: 4px;
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.78rem;
      color: #475569;
      line-height: 1.5;
    }

    .file-source-tag {
      display: inline-block;
      background: rgba(31, 95, 88, 0.08);
      border: 1px solid rgba(31, 95, 88, 0.25);
      color: var(--paladin-teal);
      padding: 0.1rem 0.4rem;
      border-radius: 3px;
      margin: 0.15rem 0;
      word-break: break-all;
    }

    .drawer-footer {
      background: #FFFFFF;
      border-top: 1px solid var(--paladin-rule);
      padding: 0.85rem 1.5rem;
      display: flex;
      justify-content: space-between;
      align-items: center;
      gap: 0.75rem;
    }

    .drawer-nav-btns {
      display: flex;
      gap: 0.5rem;
    }

    .drawer-btn {
      padding: 0.55rem 0.85rem;
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.78rem;
      font-weight: 600;
      border-radius: 4px;
      cursor: pointer;
      transition: all 0.15s ease;
      display: inline-flex;
      align-items: center;
      gap: 0.35rem;
      text-decoration: none;
    }

    .drawer-btn-secondary {
      background: var(--paladin-paper-subtle);
      border: 1px solid var(--paladin-rule);
      color: var(--paladin-ink);
    }

    .drawer-btn-secondary:hover {
      border-color: var(--paladin-teal);
      color: var(--paladin-teal);
    }

    .drawer-btn-primary {
      background: var(--paladin-teal);
      border: 1px solid var(--paladin-teal);
      color: #FFFFFF;
    }

    .drawer-btn-primary:hover {
      background: #164843;
    }

    /* Empty state */
    .empty-search-state {
      text-align: center;
      padding: 4rem 1rem;
      background: #FFFFFF;
      border: 1px dashed var(--paladin-rule-strong);
      border-radius: 6px;
      margin: 2rem 0;
      display: none;
    }

    .empty-search-state h4 {
      font-family: var(--font-display, 'Space Grotesk', sans-serif);
      font-size: 1.25rem;
      color: var(--paladin-ink);
      margin-bottom: 0.5rem;
    }

    .empty-search-state p {
      color: var(--paladin-ink-muted);
      font-size: 0.95rem;
    }

    /* Toast notification */
    .toast-msg {
      position: fixed;
      bottom: 24px;
      left: 50%;
      transform: translateX(-50%) translateY(100px);
      background: #1C1710;
      color: #FFFFFF;
      padding: 0.65rem 1.25rem;
      border-radius: 6px;
      font-family: var(--font-technical, 'JetBrains Mono', monospace);
      font-size: 0.82rem;
      border-left: 4px solid var(--paladin-teal);
      box-shadow: 0 5px 20px rgba(0, 0, 0, 0.25);
      z-index: 300;
      opacity: 0;
      transition: transform 0.25s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.25s ease;
      pointer-events: none;
    }

    .toast-msg.show {
      transform: translateX(-50%) translateY(0);
      opacity: 1;
    }

    /* Footer */
    footer {
      background: #0F172A;
      color: #F8FAFC;
      padding: 3rem 0 2rem;
      margin-top: 5rem;
      border-top: 3px solid var(--paladin-teal);
    }

    .footer-grid {
      display: grid;
      grid-template-columns: 2fr 1fr 1fr;
      gap: 2.5rem;
      margin-bottom: 2rem;
    }

    @media (max-width: 860px) {
      .footer-grid {
        grid-template-columns: 1fr;
        gap: 1.5rem;
      }
      .controls-grid {
        flex-direction: column;
        align-items: stretch;
      }
      .counter-badge {
        margin-left: 0;
        text-align: right;
      }
      .slide-drawer {
        width: 100vw;
      }
    }
  </style>
</head>
<body>

  <!-- Top Global Header -->
  <header>
    <div class="nav-container">
      <a href="paladin.html" class="brand-link">
        <img src="paladin-knight-mark.svg" alt="Paladin Mark" class="brand-logo-img">
        <div>
          <div class="brand-title">P.A.L.A.D.I.N.</div>
          <div class="brand-sub">EVIDENTIARY RECORD SYSTEM</div>
        </div>
      </a>

      <nav class="paladin-nav-links">
        <a href="paladin.html">PALADIN</a>
        <a href="why-paladin.html">Manifesto</a>
        <a href="timeline.html" class="active">Timeline (98)</a>
        <a href="library.html">Library</a>
        <a href="index.html">EFOS Hub</a>
      </nav>
    </div>
  </header>

  <!-- Hero Section -->
  <section class="timeline-hero">
    <div class="container">
      <div class="case-banner">
        <div class="case-chip">
          <strong>Federal Action:</strong> <em>Eriksson v. City of Oregon City</em> (D. Or. Case No. <code>3:26-cv-01885-IM</code>)
        </div>
        <div class="case-chip">
          <strong>Municipal / Appellate:</strong> <em>City v. Eriksson</em> (Case No. <code>CE-014675-26</code> / <code>A183495</code>)
        </div>
        <div class="case-chip">
          <strong>Evidentiary Standard:</strong> Verified Primary Sources &bull; No Prohibited Hallucinations
        </div>
      </div>

      <h1 class="hero-title">Master Chronological Evidentiary Timeline</h1>
      <p class="hero-subtitle">
        Point-and-click repository indexing 98 documented communications, utility billing records, municipal citations, code enforcement actions, and court filings spanning June 2023 through September 2026.
      </p>

      <div class="stats-strip">
        <div class="stat-box">
          <div class="stat-number">__TOTAL_ENTRIES__</div>
          <div class="stat-label">Total Audited Events</div>
        </div>
        <div class="stat-box">
          <div class="stat-number">__TOTAL_PHASES__</div>
          <div class="stat-label">Procedural Phases</div>
        </div>
        <div class="stat-box">
          <div class="stat-number">2023–2026</div>
          <div class="stat-label">Verified Date Range</div>
        </div>
        <div class="stat-box">
          <div class="stat-number">100%</div>
          <div class="stat-label">Source-Referenced</div>
        </div>
      </div>
    </div>
  </section>

  <!-- Filter & Control Bar -->
  <div class="controls-wrapper">
    <div class="container">
      <div class="controls-grid">
        <div class="search-input-box">
          <input type="text" id="timelineSearch" placeholder="Search 98 records (person, date, topic, exhibit)..." autocomplete="off">
          <button type="button" id="searchClearBtn" class="search-clear-btn" title="Clear search">&times;</button>
        </div>

        <select id="phaseFilter" class="filter-select" aria-label="Filter by Phase">
          <option value="all">All Phases (1–8)</option>
          __PHASE_OPTIONS__
        </select>

        <select id="actorFilter" class="filter-select" aria-label="Filter by Counterparty">
          <option value="all">All Actors / Counterparties</option>
          <option value="City Leadership">City Leadership (Manager, Mayor, Commission)</option>
          <option value="Code Enforcement">Code Enforcement &amp; Police</option>
          <option value="Public Works & Utilities">Public Works &amp; Utility Billing</option>
          <option value="Municipal Court">Municipal Court (Judge Lindgren, Clerk)</option>
          <option value="Defense Counsel & CIS">City Defense Counsel &amp; CIS</option>
          <option value="Plaintiffs">Plaintiffs (Eriksson, Buckhout)</option>
        </select>

        <select id="mediumFilter" class="filter-select" aria-label="Filter by Medium">
          <option value="all">All Communication Mediums</option>
          <option value="Email">Email</option>
          <option value="Notice / Letter">Notice / Letter / Placard</option>
          <option value="Phone / Audio">Phone / Audio / IVR</option>
          <option value="Court Filing / Order">Court Filing / Order</option>
          <option value="In-Person / Inspection">In-Person / Inspection</option>
          <option value="Records Request">Records Request / FOIA</option>
        </select>

        <button type="button" id="resetFiltersBtn" class="reset-filters-btn">Reset Filters</button>

        <div id="resultsCounter" class="counter-badge">Showing __TOTAL_ENTRIES__ of __TOTAL_ENTRIES__ communications</div>
      </div>
    </div>
  </div>

  <!-- Timeline Content Stream -->
  <main class="container">
    <div id="emptySearchState" class="empty-search-state">
      <h4>No communications matched your query</h4>
      <p>Try searching for a different name, date, topic, or resetting your filters.</p>
      <button type="button" onclick="resetAllFilters()" class="reset-filters-btn" style="margin-top:1rem;">Clear All Filters</button>
    </div>

    <div class="timeline-stream" id="timelineStream">
      __STREAM_CONTENT__
    </div>
  </main>

  <!-- Slide-Over Detail Drawer -->
  <div id="drawerBackdrop" class="drawer-backdrop" onclick="closeEventDrawer()"></div>
  <aside id="slideDrawer" class="slide-drawer" aria-label="Communication Detail View">
    <div class="drawer-header">
      <div class="drawer-title-area">
        <div class="drawer-meta-badges">
          <span id="drawerItemBadge" class="badge-item">Item 1.1</span>
          <span id="drawerPhaseBadge" class="badge-actor">Phase I</span>
          <span id="drawerMediumBadge" class="badge-medium">Email</span>
        </div>
        <h3 id="drawerTitle">Initial Sidewalk Grant Program Inquiry</h3>
      </div>
      <button type="button" class="drawer-close-btn" onclick="closeEventDrawer()" title="Close details (Esc)">&times;</button>
    </div>

    <div class="drawer-body">
      <table class="drawer-meta-table">
        <tbody>
          <tr>
            <td>Date / Time</td>
            <td id="drawerDateTime">—</td>
          </tr>
          <tr>
            <td>Medium</td>
            <td id="drawerMedium">—</td>
          </tr>
          <tr>
            <td>From</td>
            <td id="drawerFrom">—</td>
          </tr>
          <tr>
            <td>To</td>
            <td id="drawerTo">—</td>
          </tr>
          <tr>
            <td>Subject</td>
            <td id="drawerSubject">—</td>
          </tr>
          <tr>
            <td>Phase Context</td>
            <td id="drawerPhaseTitle">—</td>
          </tr>
        </tbody>
      </table>

      <div class="drawer-section-heading">Detailed Factual Summary &amp; Narrative</div>
      <div id="drawerSummary" class="drawer-summary-box"></div>

      <div class="drawer-section-heading">Evidentiary Source &amp; Exhibits</div>
      <div id="drawerSource" class="drawer-source-box"></div>
    </div>

    <div class="drawer-footer">
      <div class="drawer-nav-btns">
        <button type="button" id="prevEventBtn" class="drawer-btn drawer-btn-secondary" onclick="stepEvent(-1)">
          &larr; Previous
        </button>
        <button type="button" id="nextEventBtn" class="drawer-btn drawer-btn-secondary" onclick="stepEvent(1)">
          Next &rarr;
        </button>
      </div>

      <div style="display:flex; gap:0.5rem;">
        <button type="button" class="drawer-btn drawer-btn-secondary" onclick="copyCurrentCitation()">
          Copy Citation
        </button>
        <button type="button" class="drawer-btn drawer-btn-primary" onclick="copyCurrentDirectLink()">
          &sect; Copy Direct Link
        </button>
      </div>
    </div>
  </aside>

  <!-- Floating Toast -->
  <div id="toastMsg" class="toast-msg">Link copied to clipboard</div>

  <!-- Footer -->
  <footer>
    <div class="container">
      <div class="footer-grid">
        <div>
          <div style="display:flex; align-items:center; gap:0.5rem; margin-bottom:0.75rem;">
            <img src="paladin-knight-mark.svg" alt="Paladin Mark" style="width:28px; height:28px; border-radius:4px;">
            <div style="font-family:var(--font-display); font-size:1.1rem; font-weight:800; letter-spacing:0.06em;">P.A.L.A.D.I.N.</div>
          </div>
          <p style="font-size:0.85rem; line-height:1.6; color:rgba(248, 250, 252, 0.75); margin-bottom:1rem;">
            Forensic Case Timeline &bull; Eriksson v. City of Oregon City &bull; Public Record &amp; Evidentiary Index.
          </p>
          <div style="font-family:var(--font-technical); font-size:0.75rem; color:var(--paladin-teal);">
            JUDGESMOKE JURIDICAL SUB-THEME &bull; EXECUTIVE FUNCTION OS
          </div>
        </div>

        <div>
          <div style="font-family:var(--font-technical); font-size:0.8rem; font-weight:700; color:var(--paladin-teal); text-transform:uppercase; margin-bottom:0.8rem;">
            Case Navigation
          </div>
          <ul style="list-style:none; font-family:var(--font-technical); font-size:0.8rem; line-height:2;">
            <li><a href="paladin.html" style="color:#F8FAFC; text-decoration:none;">PALADIN Suite</a></li>
            <li><a href="why-paladin.html" style="color:#F8FAFC; text-decoration:none;">Manifesto &amp; Rules</a></li>
            <li><a href="timeline.html" style="color:#F8FAFC; text-decoration:none;">Timeline (98 Events)</a></li>
            <li><a href="library.html" style="color:#F8FAFC; text-decoration:none;">Library &amp; Evidence</a></li>
          </ul>
        </div>

        <div>
          <div style="font-family:var(--font-technical); font-size:0.8rem; font-weight:700; color:var(--paladin-teal); text-transform:uppercase; margin-bottom:0.8rem;">
            Evidentiary Notice
          </div>
          <p style="font-size:0.75rem; color:rgba(248, 250, 252, 0.65); line-height:1.5;">
            Compiled from public records, verified pleadings, authenticated email headers, and official dockets in Case No. 3:26-cv-01885-IM and CE-014675-26.
          </p>
        </div>
      </div>

      <div style="border-top:1px solid rgba(255,255,255,0.1); padding-top:1.2rem; font-family:var(--font-technical); font-size:0.72rem; color:rgba(248, 250, 252, 0.5); text-align:center;">
        &copy; 2026 Precedent Systems &bull; Access to Justice Initiative. All rights reserved.
      </div>
    </div>
  </footer>

  <!-- Application Logic -->
  <script>
    const ENTRIES_DATA = __ENTRIES_JSON__;
    const entriesMap = new Map();
    ENTRIES_DATA.forEach((e, idx) => {
      e.index = idx;
      entriesMap.set(e.id, e);
    });

    let currentEntryId = null;

    // Elements
    const searchInput = document.getElementById('timelineSearch');
    const searchClearBtn = document.getElementById('searchClearBtn');
    const phaseFilter = document.getElementById('phaseFilter');
    const actorFilter = document.getElementById('actorFilter');
    const mediumFilter = document.getElementById('mediumFilter');
    const resetFiltersBtn = document.getElementById('resetFiltersBtn');
    const resultsCounter = document.getElementById('resultsCounter');
    const emptySearchState = document.getElementById('emptySearchState');
    const timelineStream = document.getElementById('timelineStream');

    const drawerBackdrop = document.getElementById('drawerBackdrop');
    const slideDrawer = document.getElementById('slideDrawer');
    const drawerItemBadge = document.getElementById('drawerItemBadge');
    const drawerPhaseBadge = document.getElementById('drawerPhaseBadge');
    const drawerMediumBadge = document.getElementById('drawerMediumBadge');
    const drawerTitle = document.getElementById('drawerTitle');
    const drawerDateTime = document.getElementById('drawerDateTime');
    const drawerMedium = document.getElementById('drawerMedium');
    const drawerFrom = document.getElementById('drawerFrom');
    const drawerTo = document.getElementById('drawerTo');
    const drawerSubject = document.getElementById('drawerSubject');
    const drawerPhaseTitle = document.getElementById('drawerPhaseTitle');
    const drawerSummary = document.getElementById('drawerSummary');
    const drawerSource = document.getElementById('drawerSource');
    const prevEventBtn = document.getElementById('prevEventBtn');
    const nextEventBtn = document.getElementById('nextEventBtn');
    const toastMsg = document.getElementById('toastMsg');

    // Filter Logic
    function applyFilters() {
      const query = searchInput.value.trim().toLowerCase();
      const phaseVal = phaseFilter.value;
      const actorVal = actorFilter.value;
      const mediumVal = mediumFilter.value;

      searchClearBtn.style.display = query.length > 0 ? 'block' : 'none';

      let visibleCount = 0;
      const cards = document.querySelectorAll('.event-card');
      const phasesElements = document.querySelectorAll('.phase-block');

      cards.forEach(card => {
        const id = card.dataset.id;
        const entry = entriesMap.get(id);
        if (!entry) return;

        let matchesSearch = true;
        if (query) {
          const searchable = (
            entry.item_num + ' ' +
            entry.date_time + ' ' +
            entry.title + ' ' +
            entry.from + ' ' +
            entry.to + ' ' +
            entry.subject + ' ' +
            entry.summary + ' ' +
            entry.record_source
          ).toLowerCase();
          matchesSearch = searchable.includes(query);
        }

        let matchesPhase = (phaseVal === 'all' || entry.phase_num.toString() === phaseVal);
        let matchesActor = (actorVal === 'all' || entry.actor_cat === actorVal);
        let matchesMedium = (mediumVal === 'all' || entry.medium_cat === mediumVal);

        if (matchesSearch && matchesPhase && matchesActor && matchesMedium) {
          card.style.display = 'block';
          visibleCount++;
        } else {
          card.style.display = 'none';
        }
      });

      // Show/hide empty phases
      phasesElements.forEach(phaseEl => {
        let hasVisible = false;
        phaseEl.querySelectorAll('.event-card').forEach(c => {
          if (c.style.display !== 'none') hasVisible = true;
        });
        phaseEl.style.display = hasVisible ? 'block' : 'none';
      });

      resultsCounter.textContent = 'Showing ' + visibleCount + ' of ' + ENTRIES_DATA.length + ' communications';
      emptySearchState.style.display = visibleCount === 0 ? 'block' : 'none';
      timelineStream.style.display = visibleCount === 0 ? 'none' : 'flex';
    }

    function resetAllFilters() {
      searchInput.value = '';
      phaseFilter.value = 'all';
      actorFilter.value = 'all';
      mediumFilter.value = 'all';
      applyFilters();
    }

    // Drawer Open / Close
    function openEventDrawer(id) {
      const entry = entriesMap.get(id);
      if (!entry) return;

      currentEntryId = id;

      // Fill Drawer
      drawerItemBadge.textContent = 'Item ' + entry.item_num;
      drawerPhaseBadge.textContent = 'Phase ' + entry.phase_num;
      drawerMediumBadge.textContent = entry.medium;
      drawerTitle.textContent = entry.title;
      drawerDateTime.textContent = entry.date_time || '—';
      drawerMedium.textContent = entry.medium || '—';
      drawerFrom.textContent = entry.from.replace(/`/g, '') || '—';
      drawerTo.textContent = entry.to.replace(/`/g, '') || '—';
      drawerSubject.textContent = entry.subject.replace(/`/g, '') || 'None specified';
      drawerPhaseTitle.textContent = entry.phase_title || '—';
      drawerSummary.innerHTML = entry.summary_html || '<p>No summary provided.</p>';
      drawerSource.innerHTML = entry.record_source_html || '<p>No primary record reference provided.</p>';

      // Update Nav Buttons
      prevEventBtn.disabled = entry.index === 0;
      nextEventBtn.disabled = entry.index === ENTRIES_DATA.length - 1;

      // Active card highlight
      document.querySelectorAll('.event-card').forEach(c => c.classList.remove('active-target'));
      const activeCard = document.getElementById(id);
      if (activeCard) {
        activeCard.classList.add('active-target');
      }

      // Show drawer
      drawerBackdrop.classList.add('open');
      slideDrawer.classList.add('open');
      document.body.style.overflow = 'hidden';

      // Update URL hash without scroll jump
      history.replaceState(null, null, '#' + id);
    }

    function closeEventDrawer() {
      drawerBackdrop.classList.remove('open');
      slideDrawer.classList.remove('open');
      document.body.style.overflow = '';
      currentEntryId = null;
      history.replaceState(null, null, window.location.pathname + window.location.search);
    }

    function stepEvent(offset) {
      if (!currentEntryId) return;
      const current = entriesMap.get(currentEntryId);
      if (!current) return;
      const nextIndex = current.index + offset;
      if (nextIndex >= 0 && nextIndex < ENTRIES_DATA.length) {
        openEventDrawer(ENTRIES_DATA[nextIndex].id);
      }
    }

    // Clipboard helpers
    function showToast(text) {
      toastMsg.textContent = text;
      toastMsg.classList.add('show');
      setTimeout(() => toastMsg.classList.remove('show'), 2400);
    }

    function copyCardLink(event, id) {
      event.stopPropagation();
      const url = window.location.origin + window.location.pathname + '#' + id;
      navigator.clipboard.writeText(url).then(() => {
        showToast('Direct permanent link copied to clipboard');
      }).catch(() => {
        showToast('URL: ' + url);
      });
    }

    function copyCurrentDirectLink() {
      if (!currentEntryId) return;
      const url = window.location.origin + window.location.pathname + '#' + currentEntryId;
      navigator.clipboard.writeText(url).then(() => {
        showToast('Direct permanent link copied');
      });
    }

    function copyCurrentCitation() {
      if (!currentEntryId) return;
      const entry = entriesMap.get(currentEntryId);
      if (!entry) return;
      const cite = 'Eriksson v. Oregon City, Comm. ' + entry.item_num + ' (' + entry.date_time + '), Medium: ' + entry.medium + ', Title: "' + entry.title + '". Source: ' + entry.record_source;
      navigator.clipboard.writeText(cite).then(() => {
        showToast('Formal citation copied');
      });
    }

    // Event Listeners
    searchInput.addEventListener('input', applyFilters);
    searchClearBtn.addEventListener('click', () => {
      searchInput.value = '';
      applyFilters();
      searchInput.focus();
    });
    phaseFilter.addEventListener('change', applyFilters);
    actorFilter.addEventListener('change', applyFilters);
    mediumFilter.addEventListener('change', applyFilters);
    resetFiltersBtn.addEventListener('click', resetAllFilters);

    // Keyboard Shortcuts
    window.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        closeEventDrawer();
      } else if (slideDrawer.classList.contains('open')) {
        if (e.key === 'ArrowLeft' || e.key === 'k') {
          stepEvent(-1);
        } else if (e.key === 'ArrowRight' || e.key === 'j') {
          stepEvent(1);
        }
      } else if (e.key === '/' && document.activeElement !== searchInput) {
        e.preventDefault();
        searchInput.focus();
      }
    });

    // Hash change & initial load
    window.addEventListener('load', () => {
      const hash = window.location.hash.replace('#', '');
      if (hash && entriesMap.has(hash)) {
        openEventDrawer(hash);
        setTimeout(() => {
          const el = document.getElementById(hash);
          if (el) el.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }, 300);
      }
    });
  </script>
</body>
</html>"""

    final_html = template.replace('__TOTAL_ENTRIES__', str(total_entries))
    final_html = final_html.replace('__TOTAL_PHASES__', str(len(phases)))
    final_html = final_html.replace('__PHASE_OPTIONS__', phase_options_html)
    final_html = final_html.replace('__STREAM_CONTENT__', stream_html)
    final_html = final_html.replace('__ENTRIES_JSON__', entries_json)

    with open(OUT_HTML, 'w', encoding='utf-8') as f:
        f.write(final_html)

    print(f"Generated {OUT_HTML} with {total_entries} entries successfully!")

if __name__ == '__main__':
    phases = parse_timeline(MD_PATH)
    generate_html(phases)
