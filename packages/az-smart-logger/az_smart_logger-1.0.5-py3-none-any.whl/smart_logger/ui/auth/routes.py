from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.responses import JSONResponse
import jwt
from pydantic import BaseModel
from smart_logger.security.auth import ALGORITHM, SECRET_KEY, authenticate_user, create_access_token
from smart_logger.core.blacklist_db_handler import BlacklistDBHandler
from smart_logger.ui.auth.services import verify_token

router = APIRouter(prefix="/auth", tags=["auth"])

class LoginRequest(BaseModel):
    email: str
    password: str

@router.post("/login")
def login(req: LoginRequest):
    try:
        user = authenticate_user(req.email, req.password)
        if not user:
            return JSONResponse({"error": "Invalid credentials"}, status_code=401)

        token = create_access_token({"sub": user.email})
        return JSONResponse({"access_token": token, "token_type": "bearer"})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


@router.get("/logout")
def logout_user(request: Request):
    try:
        token = request.headers.get("Authorization") or request.headers.get("authorization")
        if not token:
            return JSONResponse({"error": "Authorization header missing"}, status_code=400)
        
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        jti = payload.get("jti")
        if not jti:
            return JSONResponse({"error": "Token missing jti"}, status_code=400)

        db = BlacklistDBHandler()
        db.blacklist_token(jti, token)  
        return JSONResponse({"status": "success"})
    except jwt.InvalidTokenError:
        return JSONResponse({"error": "Invalid token"}, status_code=401)
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)


@router.get("/protected-check")
async def protected_check(user: dict = Depends(verify_token)):
    try:
        return JSONResponse({"status": "ok", "user": user})
    except Exception as e:
        return JSONResponse({"error": str(e)}, status_code=500)
