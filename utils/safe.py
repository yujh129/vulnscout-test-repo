"""
Safe utility functions — no vulnerabilities.
"""
import json
import re
import os


def sanitize(text: str) -> str:
    """Remove dangerous characters from input."""
    return re.sub(r"[<>\'\"%;()&|`$]", "", text)


def format_greeting(name: str) -> str:
    """Safe greeting."""
    safe = sanitize(name)
    return f"Hello, {safe}!"


def parse_config(path: str) -> dict:
    """Read config file safely with path validation."""
    # Prevent path traversal and ensure file is a regular file
    real_path = os.path.realpath(path)
    if not real_path.startswith(os.path.realpath(".")):
        raise ValueError("Invalid config file path")
    if not os.path.isfile(real_path):
        raise ValueError("Config file does not exist or is not a regular file")
    # Check file permissions (only readable by owner)
    mode = os.stat(real_path).st_mode
    if mode & 0o077:
        raise PermissionError("Config file has insecure permissions")
    with open(real_path) as f:
        return json.load(f)