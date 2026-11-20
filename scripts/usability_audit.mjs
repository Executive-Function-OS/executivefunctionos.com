#!/usr/bin/env node
/**
 * Usability / accessibility regression gate.
 *
 * Two modes:
 *   1. Static files:  node scripts/usability_audit.mjs index.html rescue.html ...
 *      - axe-core accessibility violations (critical/serious -> fatal; moderate -> warning)
 *      - broken internal refs (href/src pointing at files missing from repo root)
 *      - file:// links (private-path leakage -> fatal)
 *      - warnings (non-fatal): images without width/height, pages without <h1>
 *
 *   2. Rendered routes: node scripts/usability_audit.mjs --base http://localhost:3000 --routes /,/engine,...
 *      - waits up to 60s for the server, then runs the axe checks on each route
 *
 * Exits 1 on any fatal finding. Requires jsdom + axe-core (npm install --no-save jsdom axe-core).
 */
import fs from 'fs';
import path from 'path';
import http from 'http';
import { createRequire } from 'module';

const require = createRequire(import.meta.url);
const { JSDOM, VirtualConsole } = require('jsdom');

const args = process.argv.slice(2);
const fail = [];
const warn = [];

function loadAxe(win) {
  const axeSource = fs.readFileSync(
    require.resolve('axe-core/axe.min.js'),
    'utf8'
  );
  win.eval(axeSource);
}

async function auditDom(html, label) {
  const virtualConsole = new VirtualConsole();
  const noise = [];
  virtualConsole.on('jsdomError', (e) => {
    const msg = String((e && e.message) || e);
    if (!/Not implemented|Could not load/.test(msg)) noise.push(msg.slice(0, 140));
  });
  const dom = new JSDOM(html, {
    runScripts: 'dangerously',
    pretendToBeVisual: false,
    virtualConsole,
  });
  loadAxe(dom.window);
  const results = await dom.window.axe.run(dom.window.document, {
    resultTypes: ['violations'],
    rules: { region: { enabled: false } },
  });
  const FATAL = new Set(['critical', 'serious']);
  const doc = dom.window.document;
  const extras = {
    h1: doc.querySelectorAll('h1').length,
    imgsNoDims: [...doc.querySelectorAll('img')].filter(
      (i) => !i.hasAttribute('width') && !/(width|max-width)\s*:/.test(i.getAttribute('style') || '')
    ).length,
  };
  dom.window.close();

  for (const v of results.violations) {
    if (!v.nodes.length) continue;
    const entry = `${label} [axe ${v.impact}] ${v.id} x${v.nodes.length}: ${v.help} @ ${v.nodes
      .slice(0, 3)
      .map((n) => n.target.join(' '))
      .join(' | ')}`;
    if (FATAL.has(v.impact)) fail.push(entry);
    else warn.push(entry);
  }
  if (!extras.h1) warn.push(`${label}: no <h1>`);
  if (extras.imgsNoDims)
    warn.push(`${label}: ${extras.imgsNoDims} img(s) without width/height`);
  for (const n of noise.slice(0, 3)) warn.push(`${label}: jsdom ${n}`);
}

function linkCheck(html, label, fileDir) {
  const rootDir = process.cwd();
  const refRe = /(?:href|src|srcset)="([^"]*)"/g;
  let m;
  while ((m = refRe.exec(html))) {
    const isSrcset = m[0].startsWith('srcset');
    for (const piece of m[1].split(isSrcset ? /\s*,\s*/ : '\u0000')) {
      const candidate = isSrcset ? piece.trim().split(/\s+/)[0] : piece.trim();
      if (!candidate) continue;
      // URLs with query strings (font/CDN URLs) are external; skip path resolution.
      if (/[?&]/.test(candidate)) continue;
      const [rawPath, hash] = candidate.split('#');
      const raw = rawPath || (hash !== undefined && rawPath === '' ? '' : candidate);
      if (!raw) continue;
      if (/^(https?:|mailto:|data:|javascript:)/.test(raw)) continue;
      if (raw.startsWith('file://')) {
        fail.push(`${label}: private filesystem link "${raw}"`);
        continue;
      }
      if (raw.startsWith('/')) {
        const target = path.join(rootDir, decodeURIComponent(raw.slice(1)));
        if (!fs.existsSync(target)) fail.push(`${label}: broken ref "${raw}"`);
      } else {
        const target = path.resolve(fileDir, decodeURIComponent(raw));
        if (!fs.existsSync(target)) fail.push(`${label}: broken ref "${raw}"`);
      }
    }
  }
}

async function fetchHttp(url) {
  return new Promise((resolve, reject) => {
    const req = http.get(url, { path: new URL(url).pathname }, (res) => {
      let data = '';
      res.on('data', (c) => (data += c));
      res.on('end', () => resolve({ status: res.statusCode, body: data }));
    });
    req.on('error', reject);
    req.setTimeout(15000, () => {
      req.destroy();
      reject(new Error(`timeout fetching ${url}`));
    });
  });
}

async function waitFor(base, seconds = 60) {
  const deadline = Date.now() + seconds * 1000;
  while (Date.now() < deadline) {
    try {
      const r = await fetchHttp(base + '/');
      if (r.status < 500) return true;
    } catch {}
    await new Promise((r) => setTimeout(r, 1000));
  }
  return false;
}

const baseIdx = args.indexOf('--base');
const routesIdx = args.indexOf('--routes');

if (baseIdx !== -1) {
  const base = args[baseIdx + 1];
  const routes = (args[routesIdx + 1] || '/').split(',').map((r) => r.trim());
  const up = await waitFor(base);
  if (!up) {
    console.error(`usability-audit: server at ${base} did not come up in 60s`);
    process.exit(2);
  }
  for (const route of routes) {
    let res;
    try {
      res = await fetchHttp(base + route);
    } catch (e) {
      fail.push(`${route}: fetch error ${e.message}`);
      continue;
    }
    if (res.status !== 200) {
      fail.push(`${route}: HTTP ${res.status}`);
      continue;
    }
    if (/file:\/\//.test(res.body))
      fail.push(`${route}: contains file:// link`);
    await auditDom(res.body, route);
  }
} else {
  const files = args.filter((a) => !a.startsWith('-'));
  if (!files.length) {
    console.error('usability-audit: no files given and no --base/--routes');
    process.exit(2);
  }
  for (const f of files) {
    if (!fs.existsSync(f)) {
      fail.push(`${f}: file missing`);
      continue;
    }
    const html = fs.readFileSync(f, 'utf8');
    linkCheck(html, f, path.dirname(f));
    await auditDom(html, f);
  }
}

if (warn.length) {
  console.log('Usability audit warnings:');
  for (const w of warn) console.log(`  ⚠ ${w}`);
}
if (fail.length) {
  console.error(`Usability audit FAILED (${fail.length}):`);
  for (const f of fail) console.error(`  ✗ ${f}`);
  process.exit(1);
}
console.log(`Usability audit passed (${warn.length} warning(s)).`);
