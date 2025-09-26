# smart_logger/core/db_handler.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from smart_logger.models.logger_user import Base as UserBase, LoggerUser
from smart_logger.core.base_config import DB_URL

class DBHandler:
    def __init__(self, db_url: str = None):
        self.db_url = db_url or DB_URL
        connect_args = {"check_same_thread": False} if "sqlite" in self.db_url else {}
        self.engine = create_engine(self.db_url, connect_args=connect_args)
        self.SessionLocal = sessionmaker(bind=self.engine)

    def create_logger_user(self, first_name, last_name, email, password):
        session = self.SessionLocal()
        user = LoggerUser(first_name=first_name, last_name=last_name, email=email)
        user.set_password(password)
        session.add(user)
        session.commit()
        session.close()
