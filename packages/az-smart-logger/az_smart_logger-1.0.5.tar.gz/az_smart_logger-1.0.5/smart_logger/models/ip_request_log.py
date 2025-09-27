from sqlalchemy import Column, Integer, String, DateTime, func
from smart_logger.models.base import Base

class IPRequestLog(Base):
    __tablename__ = "ip_request_log"

    id = Column(Integer, primary_key=True, autoincrement=True)
    ip_address = Column(String(45), nullable=False)
    endpoint = Column(String(255), nullable=False)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())
