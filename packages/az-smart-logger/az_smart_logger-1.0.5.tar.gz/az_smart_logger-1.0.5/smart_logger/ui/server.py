import asyncio
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import socketio
import uvicorn
from pathlib import Path
from smart_logger.security.middleware import AuthMiddleware
from smart_logger.ui.logs.websocket.manager import WebsocketConnectionManager
from smart_logger.ui.logs.websocket.sockets.logs_socket import LiveEventLogsNamespace
# Base directories
BASE_DIR = Path(__file__).parent

static_path = BASE_DIR / "static"
# FastAPI app
app = FastAPI(title="Smart Logger Dashboard")

app.add_middleware(AuthMiddleware)

# Mount static files
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

# Templates
templates = Jinja2Templates(directory=BASE_DIR / "templates")

# Import and include routes
from smart_logger.ui.auth.routes import router as auth_router
app.include_router(auth_router)

from .logs import routes
app.include_router(routes.router)

sio_server = socketio.AsyncServer(async_mode="asgi", cors_allowed_origins="*", logger=True, engineio_logger=True)

# from smart_logger.ui.logs.websocket.sockets import sio_server

# Register namespaces
sio_server.register_namespace(LiveEventLogsNamespace("/live_event_logs"))

manager = WebsocketConnectionManager(sio_server)
sio_app = socketio.ASGIApp(sio_server, other_asgi_app=app, socketio_path="/socket.io")

@app.get("/chat_broadcast")
async def chat_broadcast():
    # Ye kaam karega agar client "/chat" namespace pe connected hai
    await manager.emit_to_all("message", {"msg": "llllllll"}, namespace="/live_event_logs")
    return {"status": "sent", "msg": "LLLLLLLLLLLLL"}


def start_ui_server(host="127.0.0.1", port=8000, workers=1, reload=False):
    """
    Launch the FastAPI UI server with Socket.IO.
    """
    # uvicorn.run("smart_logger.ui.server:sio_app", host=host, port=port, workers=workers, reload=reload, loop="asyncio")
    uvicorn.run("smart_logger.ui.server:sio_app", host="127.0.0.1", port=8000, workers=workers, reload=reload)

    

