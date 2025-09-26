import uuid
from datetime import datetime
from pathlib import Path

def generate_uuid() -> str:
    """Generate unique identifier for each log entry."""
    return str(uuid.uuid4())

def get_current_datetime() -> datetime:
    """Return current UTC datetime."""
    return datetime.utcnow()

def build_log_path(base_dir: Path, parent_folder: str, filename: str) -> Path:
    """Build log file path as date/parent_folder/filename.log."""
    date_folder = datetime.utcnow().strftime("%Y-%m-%d")
    log_path = base_dir / date_folder / parent_folder
    log_path.mkdir(parents=True, exist_ok=True)
    return log_path / filename
