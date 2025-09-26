import json
from pathlib import Path
import typer

DEFAULT_CONFIG = {
    "db_engine": None,
    "db_host": None,
    "db_port": None,
    "db_user": None,
    "db_password": None,
    "db_name": None,
    "log_path": "./logs",
    "log_level": "INFO",
    "log_retention_days": 30,
    "log_rotate_size_mb": 100,
    "log_backup_count": 5,
    "encrypt_logs": 0,
    "storage_backend": "local",
    "storage_bucket": None,
    "notify_email": None,
    "notify_webhook": None
}

def make_smart_logger__default_conf():
    """
    Create a default smart-logger.conf file in the current project directory.
    """
    project_dir = Path.cwd()
    config_file = project_dir / "smart-logger.conf"

    if config_file.exists():
        typer.echo(f"Config file already exists at {config_file}")
        raise typer.Exit(code=1)

    with config_file.open("w") as f:
        json.dump(DEFAULT_CONFIG, f, indent=4)
    
    typer.echo(f"Default smart-logger.conf created at {config_file}")