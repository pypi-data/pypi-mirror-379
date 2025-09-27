import os
from email import policy
from email.parser import BytesParser


class EmailParserError(Exception):
    """Custom exception for email parsing errors."""


def parse_email(path):
    """
    Parse an email file and return its structured components.
    
    Args:
        path (str | pathlib.Path): Path to the email file.
    
    Returns:
        dict: Parsed email fields (subject, from, to, date, body).
    
    Raises:
        EmailParserError: If the file does not exist, is malformed, or cannot be parsed.
    """
    path = str(path)  # normalize Path -> str
    if not os.path.isfile(path):
        raise EmailParserError(f"Invalid file path: {path}")

    try:
        with open(path, "rb") as f:
            msg = BytesParser(policy=policy.default).parse(f)
    except Exception as e:
        raise EmailParserError(f"Failed to parse email file: {e}")

    # sanity check: if no core headers exist, treat as invalid/malformed
    if not any([msg.get("subject"), msg.get("from"), msg.get("to"), msg.get("date")]):
        raise EmailParserError("Invalid or malformed email file")

    subject = msg.get("subject", "") or ""
    sender = msg.get("from", "") or ""
    recipient = msg.get("to", "") or ""
    date = msg.get("date", "") or ""

    body = ""
    if msg.is_multipart():
        for part in msg.walk():
            ctype = part.get_content_type()
            try:
                if ctype == "text/plain":
                    body = (
                        part.get_payload(decode=True).decode(errors="ignore").strip()
                    )
                    break
                elif ctype == "text/html" and not body:
                    # fallback if no plain text found
                    body = (
                        part.get_payload(decode=True).decode(errors="ignore").strip()
                    )
            except Exception:
                raise EmailParserError("Unable to decode email body")
    else:
        if msg.get_content_type() in ("text/plain", "text/html"):
            try:
                body = msg.get_payload(decode=True).decode(errors="ignore").strip()
            except Exception:
                raise EmailParserError("Unable to decode email body")

    # normalize empty body
    if not body.strip():
        body = ""

    return {
        "subject": subject,
        "from": sender,
        "to": recipient,
        "date": date,
        "body": body,
    }
