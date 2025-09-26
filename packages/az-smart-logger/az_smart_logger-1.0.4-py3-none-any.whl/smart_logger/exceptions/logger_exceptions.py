class LoggerError(Exception):
    """Base class for all Smart Logger exceptions."""
    def __init__(self, message: str):
        super().__init__(f"[SmartLogger] {message}")


class DBConnectionError(LoggerError):
    """Raised when database connection fails."""
    pass


class LogWriteError(LoggerError):
    """Raised when writing to log file fails."""
    pass
