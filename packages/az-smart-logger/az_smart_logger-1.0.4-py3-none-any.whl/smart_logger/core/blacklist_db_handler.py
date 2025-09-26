# smart_logger/core/db_handler.py
from typing import Optional
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import logging

from smart_logger.core.base_config import DB_URL
from smart_logger.models.logger_user import TokenBlacklist
from smart_logger.models.base import Base 

logger = logging.getLogger(__name__)

class BlacklistDBHandler:
    """
    DB handler with token blacklist helpers.
    """

    def __init__(self, db_url: Optional[str] = None):
        self.db_url = db_url or DB_URL
        connect_args = {"check_same_thread": False} if self.db_url.startswith("sqlite") else {}
        self.engine = create_engine(self.db_url, connect_args=connect_args, future=True)
        self.SessionLocal = sessionmaker(bind=self.engine, autoflush=False, autocommit=False)

    def create_tables(self) -> None:
        """Create all tables (including blacklist)."""
        Base.metadata.create_all(bind=self.engine)

    # -------------------------
    # Blacklist helpers
    # -------------------------
    def blacklist_token(self, jti: str, token: str) -> bool:
        """
        Insert a token (jti + full token) into blacklist table.
        Returns True on success, False on failure.
        """
        session = self.SessionLocal()
        try:
            # avoid duplicate primary-key insert (jti is PK)
            existing = session.query(TokenBlacklist).filter_by(jti=jti).first()
            if existing:
                # already blacklisted
                return True

            entry = TokenBlacklist(jti=jti, token=token)
            session.add(entry)
            session.commit()
            return True
        except SQLAlchemyError as exc:
            session.rollback()
            logger.exception("DB error while blacklisting token: %s", exc)
            return False
        finally:
            session.close()

    def is_token_blacklisted(self, jti: str) -> bool:
        """
        Check whether given jti exists in blacklist.
        Returns True if blacklisted, False otherwise.
        """
        session = self.SessionLocal()
        try:
            exists = session.query(TokenBlacklist).filter_by(jti=jti).first() is not None
            return exists
        except SQLAlchemyError as exc:
            logger.exception("DB error while checking blacklist: %s", exc)
            # On DB error, safer to treat as blacklisted? Here we return True to be conservative.
            return True
        finally:
            session.close()

    # Optional convenience: remove old tokens (cleanup)
    def purge_blacklisted_older_than(self, days: int) -> int:
        """
        Delete blacklisted tokens older than `days`. Returns number of deleted rows.
        """
        from datetime import datetime, timedelta
        cutoff = datetime.utcnow() - timedelta(days=days)
        session = self.SessionLocal()
        try:
            q = session.query(TokenBlacklist).filter(TokenBlacklist.created_at < cutoff)
            count = q.count()
            q.delete(synchronize_session=False)
            session.commit()
            return count
        except SQLAlchemyError as exc:
            session.rollback()
            logger.exception("DB error while purging blacklist: %s", exc)
            return 0
        finally:
            session.close()
