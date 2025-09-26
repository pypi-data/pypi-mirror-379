# smart_logger/core/base.py
from smart_logger.core.config import Config
import os
from pathlib import Path

# Ensure config is loaded once
Config.load()

BASE_DIR = Path(os.getcwd())
LOG_DIR = BASE_DIR / Config.BASE_LOG_FOLDER
LOG_DIR.mkdir(parents=True, exist_ok=True)

# Database URL (fallback sqlite agar conf me na ho)
DB_URL = Config.DB_URL or f"sqlite:///{BASE_DIR / 'smart_logger.db'}"

# Dual-mode authentication
AUTH_REQUIRED = Config.AUTH_REQUIRED
STANDALONE_TOKEN = Config.STANDALONE_TOKEN

# Log levels
LOG_LEVELS = ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]
DEFAULT_LOG_LEVEL = Config.LOG_LEVEL or "INFO"

# Rotation / retention
LOG_RETENTION_DAYS = Config.LOG_RETENTION_DAYS
LOG_ROTATE_SIZE_MB = Config.LOG_ROTATE_SIZE_MB
LOG_BACKUP_COUNT = Config.LOG_BACKUP_COUNT
ENCRYPT_LOGS = bool(Config.ENCRYPT_LOGS)

# Storage backend
STORAGE_BACKEND = Config.STORAGE_BACKEND
STORAGE_BUCKET = Config.STORAGE_BUCKET

# Notifications
NOTIFY_EMAIL = Config.NOTIFY_EMAIL
NOTIFY_WEBHOOK = Config.NOTIFY_WEBHOOK
