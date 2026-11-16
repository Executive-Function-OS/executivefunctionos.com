const nodemailer = require("nodemailer");

/**
 * Determine whether the caller prefers a JSON API response over an HTML fallback.
 */
function wantsJson(req) {
  const accept = String((req.headers && req.headers.accept) || "").toLowerCase();
  const xrw = String((req.headers && req.headers["x-requested-with"]) || "").toLowerCase();
  return accept.includes("application/json") || xrw === "xmlhttprequest";
}

function escapeHtml(str) {
  return String(str)
    .replace(/&/g, "&amp;")
    .replace(/</g, "&lt;")
    .replace(/>/g, "&gt;")
    .replace(/"/g, "&quot;")
    .replace(/'/g, "&#39;");
}

/**
 * Send either a JSON response (for fetch progressive enhancement) or a clean HTML page
 * (for no-JS form posts).
 */
function sendResponse(req, res, statusCode, ok, message, backUrl = "/") {
  if (wantsJson(req)) {
    res.status(statusCode).setHeader("Content-Type", "application/json; charset=utf-8");
    res.end(JSON.stringify({ ok, message }));
    return;
  }

  const safeMsg = escapeHtml(message);
  const safeBack = escapeHtml(backUrl);
  const title = ok ? "Received — EFOS" : "Submission Issue — EFOS";

  res.status(statusCode).setHeader("Content-Type", "text/html; charset=utf-8");
  res.end(`<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex">
<title>${title}</title>
<style>
  :root{--bg:#f6f1e7;--surface:#fffdf8;--ink:#1f2a27;--muted:#55625d;--line:#ddd3c0;--accent:#2f5d50;--accent-ink:#fff}
  @media (prefers-color-scheme:dark){:root{--bg:#161c1a;--surface:#202927;--ink:#ece7dc;--muted:#a6b1ab;--line:#33403c;--accent:#8cc5b0;--accent-ink:#10201b}}
  body{margin:0;min-height:100vh;display:grid;place-items:center;padding:1.5rem;background:var(--bg);color:var(--ink);font-family:system-ui,-apple-system,"Segoe UI",Roboto,sans-serif;line-height:1.6}
  main{max-width:32rem;width:100%;background:var(--surface);border:1px solid var(--line);border-radius:20px;padding:2rem}
  h1{font-family:Georgia,serif;font-size:1.6rem;margin:0 0 .75rem}
  p{margin:0 0 1.25rem;color:var(--muted)}
  a.btn{display:inline-block;background:var(--accent);color:var(--accent-ink);text-decoration:none;font-weight:600;padding:.7rem 1.25rem;border-radius:10px}
</style>
</head>
<body>
<main>
  <h1>${ok ? "Thank you." : "Could not submit."}</h1>
  <p>${safeMsg}</p>
  <a class="btn" href="${safeBack}">Back to EFOS</a>
</main>
</body>
</html>`);
}

function sanitizeHeader(value, maxLen = 254) {
  return String(value || "")
    .replace(/[\r\n]+/g, " ")
    .trim()
    .slice(0, maxLen);
}

function sanitizeText(value, maxLen = 4000) {
  return String(value || "").trim().slice(0, maxLen);
}

function isValidEmail(email) {
  if (typeof email !== "string") return false;
  const trimmed = email.trim();
  if (!trimmed || trimmed.length > 254) return false;
  return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(trimmed);
}

function isHoneypotTripped(fields) {
  return Boolean(fields && typeof fields._gotcha === "string" && fields._gotcha.trim().length > 0);
}

/**
 * Dispatch an intake email with an embedded structured JSON block for local archival.
 */
async function sendIntakeEmail({ subject, summaryLines, payload, replyTo, attachments = [] }) {
  const user = process.env.SMTP_USER;
  const pass = process.env.SMTP_PASS;
  const to = process.env.INTAKE_TO_EMAIL || user;
  const host = process.env.SMTP_HOST || "smtp.gmail.com";
  const port = Number(process.env.SMTP_PORT || 465);

  if (!user || !pass) {
    throw new Error("Missing SMTP_USER or SMTP_PASS environment variables");
  }

  const transporter = nodemailer.createTransport({
    host,
    port,
    secure: port === 465,
    auth: { user, pass },
  });

  const body = [
    ...summaryLines,
    "",
    "--- EFOS_INTAKE_JSON_START ---",
    JSON.stringify(payload, null, 2),
    "--- EFOS_INTAKE_JSON_END ---",
  ].join("\n");

  await transporter.sendMail({
    from: `"EFOS Intake" <${user}>`,
    to,
    replyTo: replyTo || undefined,
    subject: sanitizeHeader(subject, 200),
    text: body,
    attachments,
  });
}

module.exports = {
  isHoneypotTripped,
  isValidEmail,
  sanitizeHeader,
  sanitizeText,
  sendIntakeEmail,
  sendResponse,
};
