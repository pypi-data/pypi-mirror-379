# smart_logger/config/base_config.py
import sys
from datetime import datetime
from smart_logger.configuration.loader import load_active_config


class Config:
    """
    Smart Logger configuration holder.
    Loads values from smart-logger.conf (JSON) once.
    """

    # defaults
    DB_URL: str = None
    BASE_LOG_FOLDER: str = "logs"
    AUTH_REQUIRED = None
    STANDALONE_TOKEN = None

    # extra config fields (from JSON)
    DB_ENGINE: str = None
    DB_HOST: str = None
    DB_PORT: str = None
    DB_USER: str = None
    DB_PASSWORD: str = None
    DB_NAME: str = None

    LOG_LEVEL: str = "INFO"
    LOG_RETENTION_DAYS: int = 30
    LOG_ROTATE_SIZE_MB: int = 100
    LOG_BACKUP_COUNT: int = 5
    ENCRYPT_LOGS: int = 0

    STORAGE_BACKEND: str = "local"
    STORAGE_BUCKET: str = None

    NOTIFY_EMAIL: str = None
    NOTIFY_WEBHOOK: str = None

    _loaded = False

    @classmethod
    def load(cls):
        """Load configuration from active smart-logger.conf"""
        if cls._loaded:
            return

        try:
            conf = load_active_config()

            # DB config
            cls.DB_ENGINE = conf.get("db_engine", "sqlite")
            cls.DB_HOST = conf.get("db_host")
            cls.DB_PORT = conf.get("db_port")
            cls.DB_USER = conf.get("db_user")
            cls.DB_PASSWORD = conf.get("db_password")
            cls.DB_NAME = conf.get("db_name")

            # build DB_URL
            if cls.DB_ENGINE == "sqlite":
                cls.DB_URL = f"sqlite:///{cls.DB_NAME or 'smart_logger.db'}"
            elif cls.DB_ENGINE == "mysql":
                cls.DB_URL = f"mysql+pymysql://{cls.DB_USER}:{cls.DB_PASSWORD}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}"
            elif cls.DB_ENGINE == "postgres":
                cls.DB_URL = f"postgresql://{cls.DB_USER}:{cls.DB_PASSWORD}@{cls.DB_HOST}:{cls.DB_PORT}/{cls.DB_NAME}"
            else:
                raise ValueError(f"Unsupported DB engine: {cls.DB_ENGINE}")

            # Logs
            cls.BASE_LOG_FOLDER = conf.get("log_path", "logs")
            cls.LOG_LEVEL = conf.get("log_level", "INFO")
            cls.LOG_RETENTION_DAYS = conf.get("log_retention_days", 30)
            cls.LOG_ROTATE_SIZE_MB = conf.get("log_rotate_size_mb", 100)
            cls.LOG_BACKUP_COUNT = conf.get("log_backup_count", 5)
            cls.ENCRYPT_LOGS = conf.get("encrypt_logs", 0)

            # External storage
            cls.STORAGE_BACKEND = conf.get("storage_backend", "local")
            cls.STORAGE_BUCKET = conf.get("storage_bucket")

            # Notifications
            cls.NOTIFY_EMAIL = conf.get("notify_email")
            cls.NOTIFY_WEBHOOK = conf.get("notify_webhook")

            cls._loaded = True

        except Exception as e:
            print(f"[SmartLogger] Config load failed: {e}", file=sys.stderr)
            raise

    @classmethod
    def get_log_path(cls, parent_folder, filename):
        """
        Returns full path for log file like:
        logs/YYYY-MM-DD/parent_folder/filename.log
        """
        cls.load()  # ensure config is loaded
        today = datetime.utcnow().strftime("%Y-%m-%d")
        return f"{cls.BASE_LOG_FOLDER}/{today}/{parent_folder}/{filename}"
