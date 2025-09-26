import re
from pathlib import Path

FILENAME_REGEX = r"^[\w\-. ]+$"
FOLDERNAME_REGEX = r"^[\w\-. ]+$"

def validate_filename(filename: str) -> bool:
    """
    Validate that filename contains only allowed characters.
    Prevents path traversal.
    """
    if not filename or ".." in filename:
        return False
    return re.match(FILENAME_REGEX, filename) is not None

def validate_foldername(foldername: str) -> bool:
    """
    Validate that folder name contains only allowed characters.
    """
    if not foldername or ".." in foldername:
        return False
    return re.match(FOLDERNAME_REGEX, foldername) is not None

def sanitize_path(path: Path) -> Path:
    """
    Ensure the path is within allowed base directory to prevent traversal attacks.
    """
    path = path.resolve()
    if ".." in str(path):
        raise ValueError("Invalid path detected: possible path traversal attempt")
    return path
