import argparse
import sys
import os
import json
import csv

from .parser import parse_email
from . import pro_features as pro


def export_json(data, output_file=None):
    """Export parsed email data to JSON (stdout or file)."""
    output = json.dumps(data, indent=2)
    if output_file:
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(output)
    else:
        print(output, flush=True)


def export_csv(data, output_file=None):
    """Export parsed email data to CSV (stdout or file)."""
    if isinstance(data, dict):
        rows = [data]
    else:
        rows = data

    if not rows:
        headers = ["subject", "from", "to", "date", "body"]
    else:
        headers = list(rows[0].keys())

    if output_file:
        with open(output_file, "w", newline="", encoding="utf-8") as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            for row in rows:
                writer.writerow(row)
    else:
        writer = csv.DictWriter(sys.stdout, fieldnames=headers)
        writer.writeheader()
        for row in rows:
            writer.writerow(row)
        sys.stdout.flush()

def main(argv=None):
    parser = argparse.ArgumentParser(
        description="Email Parser CLI (Gumroad Edition)",
        prog="emailparser"
    )
    subparsers = parser.add_subparsers(dest="command")

    # --- parse subcommand ---
    parse_cmd = subparsers.add_parser("parse", help="Parse .eml file(s)")
    # allow zero or more, then check manually
    parse_cmd.add_argument("input_files", nargs="*", help="Path(s) to .eml file(s) to parse")
    parse_cmd.add_argument(
        "--export", choices=["json", "csv"], default="json", help="Export format (default: json)"
    )
    parse_cmd.add_argument(
        "--output", help="Optional output file (writes to stdout if not provided)"
    )

    # --- extract subcommand ---
    extract_cmd = subparsers.add_parser("extract", help="Run pro feature extraction")
    extract_cmd.add_argument("input_files", nargs="*", help="Path(s) to .eml file(s)")
    extract_cmd.add_argument("--text", help="Raw text instead of .eml file(s)")
    extract_cmd.add_argument("--urls", action="store_true", help="Extract URLs")
    extract_cmd.add_argument("--phones", action="store_true", help="Extract phone numbers")
    extract_cmd.add_argument("--dates", action="store_true", help="Extract dates")
    extract_cmd.add_argument("--amounts", action="store_true", help="Extract amounts")
    extract_cmd.add_argument("--language", action="store_true", help="Detect language")

    args = parser.parse_args(argv)

    # No subcommand provided
    if not args.command:
        parser.print_help(sys.stderr)
        return 1

    # --- handle parse ---
    if args.command == "parse":
        if not args.input_files:
            print("No input provided", file=sys.stderr, flush=True)
            return 1   # ensure tests see non-zero exit

        results = []
        for path in args.input_files:
            if not os.path.exists(path):
                print(f"File not found: {path}", file=sys.stderr, flush=True)
                return 1   # ensure non-zero exit
            try:
                parsed = parse_email(path)
                results.append(parsed)
            except Exception as e:
                print(f"Error parsing {path}: {e}", file=sys.stderr, flush=True)
                return 1   # ensure non-zero exit

        data = results[0] if len(results) == 1 else results

        if args.export == "json":
            export_json(data, args.output)
        else:
            export_csv(data, args.output)
        return 0

    # --- handle extract ---
    if args.command == "extract":
        if not args.text and not args.input_files:
            print("No input provided", file=sys.stderr, flush=True)
            return 1   # match test expectation

        if args.text:
            body_text = args.text
        else:
            bodies = []
            for path in args.input_files:
                if not os.path.exists(path):
                    print(f"File not found: {path}", file=sys.stderr, flush=True)
                    return 1
                try:
                    parsed = parse_email(path)
                    bodies.append(parsed.get("body", ""))
                except Exception as e:
                    print(f"Error parsing {path}: {e}", file=sys.stderr, flush=True)
                    return 1
            body_text = " ".join(bodies)

        extracted = {}
        if args.urls:
            extracted["urls"] = pro.extract_urls(body_text)
        if args.phones:
            extracted["phones"] = pro.extract_phone_numbers(body_text)
        if args.dates:
            extracted["dates"] = pro.extract_dates(body_text)
        if args.amounts:
            extracted["amounts"] = pro.extract_amounts(body_text)
        if args.language:
            extracted["language"] = pro.detect_language(body_text)

        export_json(extracted, None)
        return 0

    return 1

if __name__ == "__main__":
    sys.exit(main())
