📧 EmailParser


![Tests](https://github.com/coderreynolds/emailparser/actions/workflows/tests.yml/badge.svg)
![PyPI](https://img.shields.io/pypi/v/emailparser)
![Python Versions](https://img.shields.io/pypi/pyversions/emailparser)
![Coverage](https://img.shields.io/codecov/c/github/coderreynolds/emailparser)
![License](https://img.shields.io/github/license/coderreynolds/emailparser)


EmailParser is a lightweight Python library and CLI tool for extracting structured data from emails and exporting it in useful formats.
It’s designed for developers, researchers, and businesses who want quick access to parsed email content without heavy dependencies.
Perfect for automation workflows, or one off email analysis.

## 🚀 Features
- Parse raw email files (`.eml`) into structured objects  
- Export results (CSV, JSON, etc.)  
- Simple CLI for one-line parsing  
- Extendable with custom exporters  
- Includes tests to build trust and ensure reliability  

---

## 📂 Project Structure

emailparser/  
├── emailparser/ 			# Core source code  
│   ├── cli.py 				# CLI entrypoint  
│   ├── parser.py 			# Email parsing logic  
│   ├── exporters.py 			# Export functionality  
│   ├── pro_features.py			# Premium / extra features  
│   └── __init__.py  
│  
├── tests/				# Unit tests  
│   ├── test_cli.py  
│   ├── test_parser.py  
│   └── __init__.py  
│  
├── dist/ 				# Build artifacts (wheel, tar.gz)  
├── release/				# Release-ready builds  
├── build_and_package.py		# Build helper script  
├── pyproject.toml 			# Modern build configuration  
├── setup.py 				# Legacy packaging script  
├── setup.cfg 				# Config for setuptools/pytest/etc.  
├── requirements.txt 			# Dev/test dependencies  
└── README.md 				# Documentation  

---

🔧 Installation
From PyPI (recommended for production)

$ pip install emailparser

From TestPyPI (for testing pre-releases)


$ pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple emailparser


This tells pip to prefer TestPyPI for your package but fall back to the main PyPI index for dependencies.

From source:

```bash
$ git clone https://github.com/yourusername/emailparser.git
$ cd emailparser
$ pip install -e .
```

✅ Verify the Installation

After installing, you can confirm everything works by running the CLI:

$ emailparser --help


You should see the available subcommands (parse, extract) listed.

usage: emailparser [-h] {parse,extract} ...


Or try a quick parse:

$ emailparser parse sample.eml --export json


Python Library Usage

You can also use it directly as a Python library:

from emailparser import parser

# Parse an .eml file
parsed = parser.parse_email("sample.eml")
print(parsed["subject"], parsed["from"])


🚀 Quickstart

You can use emailparser either from the command line (CLI) or directly as a Python library.

⚡ CLI Usage
# Parse a single email file
emailparser parse demo.eml

# Parse multiple files at once
emailparser parse inbox/*.eml

🐍 Library Usage

from emailparser import parser

# Example email content
content = """From: alice@example.com
To: bob@example.com
Subject: Hello

This is a test email body.
"""

# Save to a file
with open("demo.eml", "w", encoding="utf-8") as f:
    f.write(content)

# Parse the .eml file
parsed = parser.parse_email("demo.eml")

print(parsed)


Output:

{
  "subject": "Hello",
  "from": "alice@example.com",
  "to": "bob@example.com",
  "body": "This is a test email body."
}


💻 Usage

CLI

```bash
$ emailparser parse input.eml --export json
```

📘 Python API Example

```python

from emailparser import parser

with open("sample.eml", "r", encoding="utf-8") as f:
    content = f.read()

parsed = parser.parse_email(content)
print(parsed["subject"], parsed["from"])
```

✅ Running Tests
We include tests to ensure stability and trust. Run them with:

```bash
$ pytest -v
```

🔬 Development & Testing

Clone and install dev dependencies:

```bash
$ pip install -r requirements-dev.txt
```

Run tests with coverage:

```bash
$ pytest --cov=emailparser --cov-report=term-missing
```

🧹 Cleaning Up Builds
Sometimes old build artifacts, caches, or temporary files clutter the project.  
We include a helper script `cleanup.py` that resets your workspace to a clean state.

Run:

```bash
python cleanup.py
```

This will remove:

Build artifacts (dist/, release/, .egg-info/)

Cache directories (__pycache__/, .pytest_cache/)

Coverage files (.coverage)

Temporary outputs (out.json, out.txt, etc.)

👉 Use this before creating a new build or publishing to PyPI for a fresh start.


Releasing

This project supports both TestPyPI (for safe testing) and full PyPI releases.

Test Release

$ py release_test.py


Install and verify:

$ py -m pip install --index-url https://test.pypi.org/simple/ --no-deps emailparser
$ py -m emailparser --help

Full Release

$ py release.py


After publishing, users can install with:

$ pip install emailparser


📂 Real-World Workflow: Parse a Folder into JSON + CSV
import os, json, csv
from emailparser import parser

inbox_dir = "inbox"
results = []

for filename in os.listdir(inbox_dir):
    if filename.endswith(".eml"):
        parsed = parser.parse_email(os.path.join(inbox_dir, filename))
        results.append(parsed)

with open("emails.json", "w", encoding="utf-8") as jf:
    json.dump(results, jf, indent=2)

with open("emails.csv", "w", newline="", encoding="utf-8") as cf:
    writer = csv.DictWriter(cf, fieldnames=["subject", "from", "to", "body"])
    writer.writeheader()
    writer.writerows(results)

print(f"✅ Parsed {len(results)} emails into emails.json and emails.csv")

🛠️ Pro Features (Optional SaaS Hooks)

Some functionality (like advanced entity extraction) is reserved for Pro/SaaS usage.

emailparser extract sample.eml

🗺️ Roadmap

 Attachments parsing

 More output formats (Parquet, SQLite)

 Built-in SaaS-ready API server

 GUI desktop version for non-coders

📜 License
This project is licensed under the MIT License – see the LICENSE file for details.

🤝 Contributing  
Contributions are welcome!  

### How to Contribute
1. Fork the repository and create a feature branch.  
2. Install dev dependencies:  
   ```bash
   pip install -r dev-requirements.txt
   ```


3. Run tests locally to ensure nothing breaks:

```bash
pytest -v
```

4. (Optional but recommended) Run the cleanup script to reset the workspace before committing or opening a PR:

```bash
python cleanup.py
```

Guidelines

Please include tests for any new features.

Follow existing code style and structure.

Submit PRs with clear descriptions of changes.

Pull requests with improvements or new exporters are especially encouraged 🚀

We love contributions that add parsers for new email formats or integrations with CRMs.

- 🐛 [Report Bugs](https://github.com/coderreynolds/emailparser/issues)  
- 🌱 [Request Features](https://github.com/coderreynolds/emailparser/issues)  
- 🔀 [Submit Pull Requests](https://github.com/coderreynolds/emailparser/pulls)


