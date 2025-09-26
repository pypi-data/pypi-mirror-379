from datetime import datetime
from sqlalchemy import Column, String, Integer, DateTime
from smart_logger.models.base import Base
from passlib.hash import argon2


class LoggerUser(Base):
    __tablename__ = "logger_user"

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    password_hash = Column(String, nullable=False)

    def set_password(self, password: str):
        self.password_hash = argon2.hash(password)

    def verify_password(self, password: str) -> bool:
        return argon2.verify(password, self.password_hash)


class TokenBlacklist(Base):
    __tablename__ = "smart_logger_token_blacklist"

    jti = Column(String, primary_key=True, index=True)
    token = Column(String, nullable=False)  # <-- pura JWT token bhi rakhenge
    created_at = Column(DateTime, default=datetime.utcnow)