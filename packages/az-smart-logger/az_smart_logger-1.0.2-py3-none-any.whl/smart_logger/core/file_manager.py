from pathlib import Path
from .utils import build_log_path

class FileManager:
    """Handles log file creation and directory management."""

    def __init__(self, base_dir: Path):
        self.base_dir = base_dir

    def get_log_file(self, parent_folder: str, filename: str) -> Path:
        return build_log_path(self.base_dir, parent_folder, filename)
