import uuid
import jwt
from datetime import datetime, timedelta
from passlib.context import CryptContext
from smart_logger.core.blacklist_db_handler import BlacklistDBHandler
from smart_logger.models.logger_user import LoggerUser
from smart_logger.core.db_handler import DBHandler

SECRET_KEY = "AbcdX=1234!@#$Efgh5678Ijklmnop" 
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60

pwd_context = CryptContext(schemes=["argon2"], deprecated="auto")

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def get_password_hash(password: str) -> str:
    return pwd_context.hash(password)

def create_access_token(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    expire = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expire, "jti": str(uuid.uuid4())})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

def authenticate_user(email: str, password: str):
    db = DBHandler()
    session = db.SessionLocal()
    user = session.query(LoggerUser).filter(LoggerUser.email == email).first()
    session.close()
    if not user:
        return None
    if not verify_password(password, user.password_hash):
        return None
    return user

def is_token_blacklisted(token: str) -> bool:
    db = BlacklistDBHandler()
    return db.is_token_blacklisted(token)
