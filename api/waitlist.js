const {
  isHoneypotTripped,
  isValidEmail,
  sanitizeHeader,
  sanitizeText,
  sendIntakeEmail,
  sendResponse,
} = require("./_intake_mailer");

/**
 * Serverless handler for EFOS waitlist signups (replaces Netlify Forms).
 * Accepts application/x-www-form-urlencoded or application/json POSTs.
 */
module.exports = async function handler(req, res) {
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
    sendResponse(req, res, 405, false, "Method not allowed.", "/");
    return;
  }

  const body = req.body && typeof req.body === "object" ? req.body : {};

  if (isHoneypotTripped(body)) {
    sendResponse(
      req,
      res,
      200,
      true,
      "Thank you. You’re on the list. We’ll email you when early access opens.",
      "/"
    );
    return;
  }

  const email = sanitizeHeader(body.email, 254);
  const hardestPart = sanitizeText(body.hardest_part, 4000);

  if (!isValidEmail(email)) {
    sendResponse(req, res, 400, false, "Please enter a valid email address.", "/#waitlist");
    return;
  }

  const payload = {
    type: "waitlist",
    submitted_at: new Date().toISOString(),
    email,
    hardest_part: hardestPart || null,
    user_agent: sanitizeHeader(req.headers["user-agent"], 250) || null,
  };

  try {
    await sendIntakeEmail({
      subject: `[WAITLIST] EFOS signup: ${email}`,
      replyTo: email,
      summaryLines: [
        "New EFOS Waitlist Signup",
        `Email: ${email}`,
        `Submitted: ${payload.submitted_at}`,
        `Hardest part: ${hardestPart || "(not provided)"}`,
      ],
      payload,
    });

    sendResponse(
      req,
      res,
      200,
      true,
      "Thank you. You’re on the list. We’ll email you when early access opens.",
      "/"
    );
  } catch (err) {
    console.error("Waitlist intake failed:", err && err.message ? err.message : err);
    sendResponse(
      req,
      res,
      500,
      false,
      "Something went wrong sending that. Please try again in a moment.",
      "/#waitlist"
    );
  }
};
