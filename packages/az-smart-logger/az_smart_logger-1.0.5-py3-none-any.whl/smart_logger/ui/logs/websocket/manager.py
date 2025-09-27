class WebsocketConnectionManager:
    def __init__(self, sio_server):
        self.sio = sio_server

    async def emit_to_all(self, event: str, data: dict, namespace: str):
        await self.sio.emit(event, data, namespace=namespace)

    async def emit_to_sid(self, event: str, data: dict, namespace: str, sid: str):
        await self.sio.emit(event, data, room=sid, namespace=namespace)

    async def emit_to_room(self, event: str, data: dict, namespace: str, room: str):
        await self.sio.emit(event, data, room=room, namespace=namespace)
