from datetime import datetime
from sqlalchemy import Column, String, DateTime, Text, Integer
from smart_logger.models.base import Base

class LogMetadata(Base):
    """
    SQLAlchemy model to store metadata for each log entry with full caller info.
    """

    __tablename__ = "smart_logger_metadata"

    uuid = Column(String, primary_key=True, index=True)
    datetime = Column(DateTime, nullable=False)
    parent_folder = Column(String, nullable=False)
    filename = Column(String, nullable=False)
    full_path = Column(String, nullable=False)
    log_type = Column(String, nullable=False)
    ip_address = Column(String(45), nullable=False)
    module = Column(String)


    def __repr__(self):
        return (
            f"<LogMetadata(uuid={self.uuid}, datetime={self.datetime}, "
            f"folder={self.parent_folder}, filename={self.filename}, "
            f"log_type={self.log_type}, module={self.module}"
        )


class ActiveClient(Base):
    __tablename__ = "active_clients"
    sid = Column(String(64), primary_key=True)
    namespace = Column(String(64))
    connected_at = Column(DateTime, default=datetime.utcnow)