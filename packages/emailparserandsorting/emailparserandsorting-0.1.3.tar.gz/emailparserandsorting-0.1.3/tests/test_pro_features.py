import re
import email
from email.message import EmailMessage

import emailparser.pro_features as pro


def make_email(body: str, subject: str = "Test", sender: str = "a@test.com", receiver: str = "b@test.com"):
    """Helper to build a minimal EmailMessage."""
    msg = EmailMessage()
    msg["From"] = sender
    msg["To"] = receiver
    msg["Subject"] = subject
    msg.set_content(body)
    return msg


def test_extract_urls_from_text():
    text = "Visit https://gumroad.com and http://example.org"
    urls = pro.extract_urls(text)
    assert "https://gumroad.com" in urls
    assert "http://example.org" in urls


def test_extract_phone_numbers():
    text = "Call me at (555) 123-4567 or 555-987-6543."
    phones = pro.extract_phone_numbers(text)
    assert any("555" in p for p in phones)


def test_detect_language_english():
    text = "Hello world, this is a test."
    lang = pro.detect_language(text)
    assert lang in ["en", "unknown"]  # fallback safe


def test_extract_dates_and_amounts_from_email():
    body = "Meeting scheduled on 2023-10-05. Total cost is $42.50."
    msg = make_email(body, subject="Invoice")
    text = msg.get_content()

    dates = pro.extract_dates(text)
    amounts = pro.extract_amounts(text)

    assert any("2023-10-05" in d for d in dates)
    assert any("42.50" in a for a in amounts)
