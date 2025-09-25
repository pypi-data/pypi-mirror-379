# File Organizer

[![CI](https://github.com/recregt/file-organizer/actions/workflows/python-tests.yml/badge.svg)](https://github.com/recregt/file-organizer/actions)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

Small Python utility to organize files in a directory into subfolders by extension.

Usage:

Run the CLI:

    python -m organizer.cli [target] [--dry-run] [--copy] [--overwrite]

Or import the `organize` function from `organizer.core`.

Testing:

    pip install pytest
    pytest
