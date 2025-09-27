from setuptools import setup, find_packages
from pathlib import Path

this_dir = Path(__file__).parent
long_description = (this_dir / "README.md").read_text(encoding="utf-8")

setup(
    name="emailparserandsorting",
    version="0.1.3",
    description="Lightweight Python library and CLI tool for parsing .eml files and exporting structured data.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Royce Reynolds",
    author_email="jj.bird8900@gmail.com",
    url="https://github.com/coderreynolds/emailparser",
    packages=find_packages(exclude=["tests*", "dist*", "build*", "release*"]),
    python_requires=">=3.9",
    install_requires=[],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    entry_points={
        "console_scripts": [
            "emailparser=emailparser.cli:main",
        ],
    },
)
