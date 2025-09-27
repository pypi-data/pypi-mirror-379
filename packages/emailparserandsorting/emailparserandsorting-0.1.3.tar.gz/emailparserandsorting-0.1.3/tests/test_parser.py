import os
import tempfile
import pytest
from email.message import EmailMessage
from emailparser import parser


def make_eml_file(tmp_path, subject="Test", sender="sender@test.com", recipient="receiver@test.com", body="Hello"):
    """Helper to create a temporary .eml file."""
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = recipient
    msg["Subject"] = subject
    msg.set_content(body)

    file_path = tmp_path / f"{subject}.eml"
    with open(file_path, "wb") as f:
        f.write(msg.as_bytes())
    return str(file_path)


def test_parse_email_basic(tmp_path):
    path = make_eml_file(tmp_path, subject="Basic Test", body="Hello World")
    parsed = parser.parse_email(path)
    assert parsed["subject"] == "Basic Test"
    assert "Hello World" in parsed["body"]
    assert parsed["from"] == "sender@test.com"
    assert parsed["to"] == "receiver@test.com"


def test_parse_email_no_body(tmp_path):
    path = make_eml_file(tmp_path, subject="NoBody", body="")
    parsed = parser.parse_email(path)
    assert parsed["subject"] == "NoBody"
    assert parsed["body"] == ""


def test_parse_email_unusual_content_type(tmp_path):
    # Create message with HTML body instead of plain text
    msg = EmailMessage()
    msg["From"] = "sender@test.com"
    msg["To"] = "receiver@test.com"
    msg["Subject"] = "HTML Email"
    msg.add_alternative("<html><body><p>Hello HTML</p></body></html>", subtype="html")

    file_path = tmp_path / "html_email.eml"
    with open(file_path, "wb") as f:
        f.write(msg.as_bytes())

    parsed = parser.parse_email(str(file_path))
    assert parsed["subject"] == "HTML Email"
    # Fallback: HTML text should still be captured in body
    assert "Hello HTML" in parsed["body"]


def test_parse_email_invalid_file_path():
    # Passing a path that doesn’t exist
    with pytest.raises(parser.EmailParserError):
        parser.parse_email("does_not_exist.eml")


def test_parse_email_invalid_format(tmp_path):
    # Write garbage file instead of real .eml
    bad_file = tmp_path / "bad.eml"
    bad_file.write_text("Not a real email")

    with pytest.raises(parser.EmailParserError):
        parser.parse_email(str(bad_file))


def test_parse_email_decode_failure(monkeypatch, tmp_path):
    """Force a decode failure to ensure EmailParserError is raised."""
    path = make_eml_file(tmp_path, subject="DecodeFail", body="Hello")

    # Monkeypatch BytesParser.parse to return a fake message object
    class FakeMessage:
        def is_multipart(self): return False
        def get_content_type(self): return "text/plain"
        def get_payload(self, decode=False): raise Exception("decode error")
        def get(self, key, default=None): return ""  # no headers

    monkeypatch.setattr("emailparser.parser.BytesParser.parse", lambda self, f: FakeMessage())

    with pytest.raises(parser.EmailParserError):
        parser.parse_email(path)

def test_parse_html_only_email(tmp_path):
    """Ensure parser can handle emails with only HTML body."""
    eml = tmp_path / "html_only.eml"
    eml.write_text(
        "From: alice@example.com\nTo: bob@example.com\nSubject: HTML\n"
        "Content-Type: text/html\n\n"
        "<html><body><p>Hello <b>World</b></p></body></html>"
    )

    from emailparser.parser import parse_email
    parsed = parse_email(str(eml))
    assert parsed["subject"] == "HTML"
    assert "Hello" in parsed["body"]

def test_parse_email_with_no_body(tmp_path):
    """Ensure parser normalizes an empty body to empty string."""
    eml = tmp_path / "nobody.eml"
    eml.write_text(
        "From: alice@example.com\nTo: bob@example.com\nSubject: Empty\n\n"
    )

    from emailparser.parser import parse_email
    parsed = parse_email(str(eml))
    assert parsed["subject"] == "Empty"
    assert parsed["body"] == ""  # body should be normalized to empty string

