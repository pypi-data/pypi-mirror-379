from fastapi import HTTPException, Request
import jwt
from smart_logger.security.auth import SECRET_KEY, ALGORITHM
from smart_logger.core.blacklist_db_handler import BlacklistDBHandler


def verify_token(request: Request):
    auth_header = request.headers.get("Authorization") or request.headers.get("authorization")
    if not auth_header or not auth_header.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid token")
    
    token = auth_header.split(" ")[1]
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        jti = payload.get("jti")
        if not jti:
            raise HTTPException(status_code=401, detail="Invalid token (no jti)")
        
        db = BlacklistDBHandler()
        if db.is_token_blacklisted(jti):
            raise HTTPException(status_code=401, detail="Token expired or logged out")
        
        return payload
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="Token expired")
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail="Invalid token")