import json
import pytest
from emailparser import cli


def run_cli(args, capsys):
    """
    Run CLI inside this process for coverage.
    Returns (exit_code, stdout, stderr).
    """
    try:
        code = cli.main(args)   # capture return code directly
    except SystemExit as e:
        code = e.code

    out, err = capsys.readouterr()
    return code, out, err


def test_cli_no_args(capsys):
    exit_code = cli.main([])   # Explicitly pass empty argv
    captured = capsys.readouterr()
    assert exit_code == 1
    assert "usage:" in captured.err


def test_parse_json(tmp_path, capsys):
    eml = tmp_path / "sample.eml"
    eml.write_text(
        "From: alice@example.com\nTo: bob@example.com\nSubject: Hi\n\nHello Bob!"
    )

    code, out, err = run_cli(["parse", str(eml), "--export", "json"], capsys)
    assert code == 0
    data = json.loads(out)
    assert data["subject"] == "Hi"
    assert "body" in data


def test_parse_csv(tmp_path, capsys):
    eml = tmp_path / "sample.eml"
    eml.write_text(
        "From: alice@example.com\nTo: bob@example.com\nSubject: Hi\n\nHello Bob!"
    )
    out_file = tmp_path / "out.csv"

    code, out, err = run_cli(
        ["parse", str(eml), "--export", "csv", "--output", str(out_file)], capsys
    )
    assert code == 0
    content = out_file.read_text()
    assert "subject" in content
    assert "Hi" in content


# ---------------- Pro features ----------------

def test_extract_from_text_urls_and_phones(capsys):
    text = "Check this link: https://gumroad.com and call (555) 123-4567."
    code, out, err = run_cli(["extract", "--urls", "--phones", "--text", text], capsys)
    assert code == 0
    data = json.loads(out)
    assert "urls" in data and "https://gumroad.com" in data["urls"]
    assert "phones" in data and any("555" in p for p in data["phones"])


def test_extract_from_email_dates_and_amounts(tmp_path, capsys):
    eml = tmp_path / "invoice.eml"
    eml.write_text(
        "From: shop@example.com\nTo: bob@example.com\nSubject: Invoice\n\n"
        "Invoice date: 2023-10-05\nTotal: $42.50"
    )

    code, out, err = run_cli(
        ["extract", str(eml), "--dates", "--amounts"], capsys
    )
    assert code == 0
    data = json.loads(out)
    assert "dates" in data and any("2023-10-05" in d for d in data["dates"])
    assert "amounts" in data and any("42.50" in a for a in data["amounts"])


# ---------------- Negative tests ----------------

def test_cli_parse_missing_file(capsys):
    """Ensure CLI handles missing input file gracefully."""
    code, out, err = run_cli(["parse", "does_not_exist.eml"], capsys)
    assert code == 1
    assert "File not found" in err

def test_cli_extract_missing_input(capsys):
    """Ensure CLI handles extract with no input gracefully."""
    code, out, err = run_cli(["extract"], capsys)
    assert code == 1
    assert "No input provided" in err

def test_cli_parse_multiple_files(tmp_path, capsys):
    """Parse multiple .eml files and ensure output is a list of results."""
    eml1 = tmp_path / "one.eml"
    eml2 = tmp_path / "two.eml"
    eml1.write_text("From: a@example.com\nTo: b@example.com\nSubject: First\n\nBody1")
    eml2.write_text("From: c@example.com\nTo: d@example.com\nSubject: Second\n\nBody2")

    code, out, err = run_cli(
        ["parse", str(eml1), str(eml2), "--export", "json"], capsys
    )
    assert code == 0
    data = json.loads(out)
    assert isinstance(data, list)
    subjects = [d["subject"] for d in data]
    assert "First" in subjects and "Second" in subjects


def test_cli_parse_invalid_file(tmp_path, capsys):
    """Trigger parse_email exception to test error handling."""
    bad = tmp_path / "bad.eml"
    # Write binary garbage instead of a proper email
    bad.write_bytes(b"\x00\x01\x02 not a valid email")

    code, out, err = run_cli(["parse", str(bad)], capsys)
    assert code == 1
    assert "Error parsing" in err
