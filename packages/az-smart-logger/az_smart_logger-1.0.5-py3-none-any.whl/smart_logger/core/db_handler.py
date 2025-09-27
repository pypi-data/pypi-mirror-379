from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
from smart_logger.models.log_metadata import ActiveClient, Base, LogMetadata
from smart_logger.core.base_config import DB_URL
from datetime import datetime
from threading import Lock

class DBHandler:
    """Thread-safe DB handler for SmartLogger metadata."""

    _lock = Lock()

    def __init__(self, db_url: str = None):
        self.db_url = db_url or DB_URL
        connect_args = {"check_same_thread": False} if "sqlite" in self.db_url else {}
        self.engine = create_engine(self.db_url, connect_args=connect_args, future=True)
        self.SessionLocal = sessionmaker(bind=self.engine)

    def create_tables(self):
        Base.metadata.create_all(bind=self.engine)

    def insert_log_metadata(self, **kwargs):
        """Thread-safe insert for metadata with full log info."""
        with self._lock:
            session = self.SessionLocal()
            try:
                if "datetime" not in kwargs or not kwargs["datetime"]:
                    kwargs["datetime"] = datetime.utcnow()
                log_entry = LogMetadata(**kwargs)
                session.add(log_entry)
                session.commit()
            except SQLAlchemyError as e:
                session.rollback()
                print(f"[SmartLogger][DB ERROR]: {e}")
            finally:
                session.close()

    def add_active_client(self, sid, namespace):
        session = self.SessionLocal()
        try:
            client = ActiveClient(sid=sid, namespace=namespace)
            session.merge(client)  # merge to avoid duplicates
            session.commit()
        finally:
            session.close()

    def remove_active_client(self, sid):
        session = self.SessionLocal()
        try:
            session.query(ActiveClient).filter(ActiveClient.sid==sid).delete()
            session.commit()
        finally:
            session.close()

    def get_active_clients(self):
        session = self.SessionLocal()
        try:
            return [c.sid for c in session.query(ActiveClient).all()]
        finally:
            session.close()