import re
from langdetect import detect, LangDetectException

def extract_urls(text: str):
    """Extract URLs from text."""
    url_pattern = r"https?://[^\s]+"
    return re.findall(url_pattern, text or "")

def extract_phone_numbers(text: str):
    """Extract phone numbers from text."""
    phone_pattern = r"(?:\+?\d{1,2}[-.\s]?)?(?:\(?\d{3}\)?[-.\s]?)\d{3}[-.\s]?\d{4}"
    return re.findall(phone_pattern, text or "")

def detect_language(text: str):
    """Detect language of given text, fallback to 'unknown'."""
    try:
        return detect(text)
    except LangDetectException:
        return "unknown"

def extract_dates(text: str):
    """Extract date-like patterns (YYYY-MM-DD or DD/MM/YYYY)."""
    date_pattern = r"\b\d{4}-\d{2}-\d{2}\b|\b\d{2}/\d{2}/\d{4}\b"
    return re.findall(date_pattern, text or "")

def extract_amounts(text: str):
    """Extract currency amounts like $12.34 or €56."""
    amount_pattern = r"[\$€£]\s?\d+(?:\.\d{2})?"
    return re.findall(amount_pattern, text or "")
