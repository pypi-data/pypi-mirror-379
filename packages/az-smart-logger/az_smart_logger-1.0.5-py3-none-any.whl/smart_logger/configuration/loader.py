import json
from pathlib import Path

LIBRARY_HOME = Path.home() / ".smart_logger"
CONFIG_POINTER = LIBRARY_HOME / "config_path"


def load_active_config() -> dict:
    """
    Helper function to load active configuration in Python code.
    Reads path from ~/.smart_logger/config_path and loads JSON.
    """
    if not CONFIG_POINTER.exists():
        raise RuntimeError("No config set. Run `smart-logger set-config` first.")

    config_file = Path(CONFIG_POINTER.read_text().strip())
    if not config_file.exists():
        raise RuntimeError("Config file missing. Please re-run `set-config`.")

    with open(config_file, "r") as f:
        return json.load(f)
