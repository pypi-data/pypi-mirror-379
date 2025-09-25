#!/usr/bin/env python3
"""
Setup script for python-multirunner package.

This script provides backward compatibility with setuptools while using
the modern pyproject.toml configuration.
"""

from setuptools import setup

# Read the README file for long description
try:
    with open("README.md", "r", encoding="utf-8") as fh:
        long_description = fh.read()
except FileNotFoundError:
    long_description = "A high-performance hybrid executor for Python 3.13+ without GIL"

if __name__ == "__main__":
    setup()
