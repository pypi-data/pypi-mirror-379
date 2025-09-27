import asyncio
from smart_logger.core.db_handler import DBHandler
import socketio
from smart_logger.core.logger import TempLogReader

class LiveEventLogsNamespace(socketio.AsyncNamespace):
    def __init__(self, namespace: str = "/live_event_logs"):
        super().__init__(namespace)
        self.reader = TempLogReader()
        self.db_handler = DBHandler()

    async def on_connect(self, sid, environ):
        print(f"[DEBUG] Client connected: {sid}")
        await self.enter_room(sid, sid, namespace=self.namespace)
        # Global lock use karo
        self.db_handler.add_active_client(sid, self.namespace)
        asyncio.create_task(self._stream_logs_to_client(sid))


    async def on_disconnect(self, sid):
        print(f"[DEBUG] Client disconnected: {sid}")
        await self.leave_room(sid, sid, namespace=self.namespace)
        self.db_handler.remove_active_client(sid)

    async def _stream_logs_to_client(self, sid):
        """
        Stream logs line-by-line from temp file to client.
        Stops automatically if client disconnects.
        """
        while sid in self.db_handler.get_active_clients():
            line = self.reader.get_line()
            if line:
                await self.emit("log_event", {"msg": line}, room=sid)
            else:
                await asyncio.sleep(0.2)  # wait briefly if no logs

    async def on_message(self, sid, data):
        print(f"[DEBUG] Live Event Logs Message from {sid}: {data}")
        await self.emit("log_event", {"msg": f"User: {data}"}, skip_sid=sid)
