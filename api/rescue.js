const path = require("path");
const Busboy = require("busboy");
const {
  isHoneypotTripped,
  isValidEmail,
  sanitizeHeader,
  sanitizeText,
  sendIntakeEmail,
  sendResponse,
} = require("./_intake_mailer");

const MAX_FILE_BYTES = 4 * 1024 * 1024; // Keep safely under Vercel's 4.5 MB request limit
const ALLOWED_EXTENSIONS = new Set([".pdf", ".docx", ".doc", ".txt", ".rtf"]);

function parseMultipart(req) {
  return new Promise((resolve, reject) => {
    const fields = {};
    const files = [];
    let fileTooLarge = false;

    const busboy = Busboy({
      headers: req.headers,
      limits: {
        files: 1,
        fileSize: MAX_FILE_BYTES,
        fields: 20,
        fieldSize: 32 * 1024,
      },
    });

    busboy.on("field", (name, val) => {
      fields[name] = val;
    });

    busboy.on("file", (name, fileStream, info) => {
      const filename = info && info.filename ? path.basename(info.filename) : "";
      const mimeType = (info && info.mimeType) || "application/octet-stream";
      const chunks = [];

      fileStream.on("limit", () => {
        fileTooLarge = true;
      });

      fileStream.on("data", (chunk) => {
        chunks.push(chunk);
      });

      fileStream.on("end", () => {
        if (filename && chunks.length > 0 && !fileTooLarge) {
          files.push({
            fieldname: name,
            filename,
            contentType: mimeType,
            content: Buffer.concat(chunks),
          });
        }
      });
    });

    busboy.on("error", (err) => reject(err));
    busboy.on("finish", () => resolve({ fields, files, fileTooLarge }));

    req.pipe(busboy);
  });
}

/**
 * Serverless handler for $20 Court Document Rescue requests (replaces Netlify Forms).
 * Accepts multipart/form-data POSTs with an optional document attachment up to 4 MB.
 */
async function handler(req, res) {
  if (req.method !== "POST") {
    res.setHeader("Allow", "POST");
    sendResponse(req, res, 405, false, "Method not allowed.", "/rescue.html");
    return;
  }

  let parsed;
  try {
    parsed = await parseMultipart(req);
  } catch (err) {
    console.error("Rescue multipart parse error:", err && err.message ? err.message : err);
    sendResponse(req, res, 400, false, "Could not parse the form upload. Please try again.", "/rescue.html");
    return;
  }

  const { fields, files, fileTooLarge } = parsed;

  if (isHoneypotTripped(fields)) {
    sendResponse(
      req,
      res,
      200,
      true,
      "Thank you! Your document rescue request has been received. We will review your files and email you shortly.",
      "/rescue.html"
    );
    return;
  }

  if (fileTooLarge) {
    sendResponse(
      req,
      res,
      413,
      false,
      "Attachment exceeds the 4 MB upload limit. Please attach a smaller excerpt or submit without the file and we will send an upload link.",
      "/rescue.html"
    );
    return;
  }

  const name = sanitizeHeader(fields.name, 200);
  const email = sanitizeHeader(fields.email, 254);
  const courtType = sanitizeHeader(fields.court_type, 100);
  const serviceNeeded = sanitizeHeader(fields.service_needed, 100);
  const details = sanitizeText(fields.details, 6000);

  if (!name || !isValidEmail(email)) {
    sendResponse(req, res, 400, false, "Please provide your name and a valid email address.", "/rescue.html");
    return;
  }

  const attachments = [];
  if (files.length > 0) {
    const f = files[0];
    const ext = path.extname(f.filename).toLowerCase();
    if (!ALLOWED_EXTENSIONS.has(ext)) {
      sendResponse(
        req,
        res,
        400,
        false,
        "Unsupported file type. Please attach a PDF, DOCX, DOC, TXT, or RTF file.",
        "/rescue.html"
      );
      return;
    }
    attachments.push({
      filename: f.filename,
      content: f.content,
      contentType: f.contentType,
    });
  }

  const payload = {
    type: "court-rescue",
    submitted_at: new Date().toISOString(),
    name,
    email,
    court_type: courtType || null,
    service_needed: serviceNeeded || null,
    details: details || null,
    attachment_filename: attachments.length > 0 ? attachments[0].filename : null,
    attachment_bytes: attachments.length > 0 ? attachments[0].content.length : 0,
  };

  try {
    await sendIntakeEmail({
      subject: `[RESCUE] ${name} (${courtType || "court"})`,
      replyTo: email,
      summaryLines: [
        "New Court Document Rescue Request ($20 Flat)",
        `Name: ${name}`,
        `Email: ${email}`,
        `Court / Jurisdiction: ${courtType || "(not specified)"}`,
        `Primary Need: ${serviceNeeded || "(not specified)"}`,
        `Attachment: ${payload.attachment_filename ? `${payload.attachment_filename} (${payload.attachment_bytes} bytes)` : "(none)"}`,
        `Submitted: ${payload.submitted_at}`,
        "",
        "Details:",
        details || "(not provided)",
      ],
      payload,
      attachments,
    });

    sendResponse(
      req,
      res,
      200,
      true,
      "Thank you! Your document rescue request has been received. We will review your files and email you shortly.",
      "/rescue.html"
    );
  } catch (err) {
    console.error("Rescue intake failed:", err && err.message ? err.message : err);
    sendResponse(
      req,
      res,
      500,
      false,
      "Something went wrong submitting your request. Please try again in a moment.",
      "/rescue.html"
    );
  }
}

handler.config = {
  api: {
    bodyParser: false,
  },
};

module.exports = handler;
