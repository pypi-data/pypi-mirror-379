from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware
import jwt
from smart_logger.security.auth import SECRET_KEY, ALGORITHM
from smart_logger.core.blacklist_db_handler import BlacklistDBHandler

class AuthMiddleware(BaseHTTPMiddleware):
    def __init__(self, app, excluded_paths: list[str] = None):
        super().__init__(app)
      
        self.excluded_paths = excluded_paths or [
            "/smart-logger/login",
            "/auth/login",
            "/logs/login",
            "/logs/dashboard",
            "/logs/live-logs",
            "/docs",
            "/redoc",
            "/openapi.json",
            "/static",
            "/.well-known/appspecific/com.chrome.devtools.json",
            "/favicon.ico",
            "/chat_broadcast",
            "/logs/filter_logs"
        ]
        self.blacklist_db = BlacklistDBHandler()

    async def dispatch(self, request: Request, call_next):
        path = request.url.path
        ws_path = request.scope.get("path", "")

        # Ignore OPTIONS requests (CORS preflight)
        if request.method == "OPTIONS":
            return await call_next(request)

        # Skip auth check for excluded paths
        if any(path.startswith(p) for p in self.excluded_paths):
            return await call_next(request)

        if ws_path and (ws_path.startswith("/socket.io") or ws_path.startswith("/ws")):
            return await call_next(request)
            # query_string = request.scope.get("query_string", b"").decode()
            # params = dict(qc.split("=") for qc in query_string.split("&") if "=" in qc)
            # token = params.get("token")
        else:
            # Get Authorization header
            auth_header = request.headers.get("Authorization") or request.headers.get("authorization")
            if not auth_header or not auth_header.startswith("Bearer "):
                raise HTTPException(status_code=401, detail="Missing or invalid token")

            token = auth_header.split(" ")[1]
        try:
            # Decode token
            payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
            jti = payload.get("jti")

            if not jti:
                raise HTTPException(status_code=401, detail="Invalid token (no jti)")

            # Blacklist check
            if self.blacklist_db.is_token_blacklisted(jti):
                raise HTTPException(status_code=401, detail="Token expired or logged out")

            # Store user payload for downstream
            request.state.user = payload

        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail="Token expired")
        except jwt.InvalidTokenError:
            raise HTTPException(status_code=401, detail="Invalid token")
        except Exception as e:
            # fallback for unexpected error
            raise HTTPException(status_code=500, detail=f"Auth middleware error: {str(e)}")

        return await call_next(request)
