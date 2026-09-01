import json
import logging
from typing import Dict, List, Set, Any
from fastapi import WebSocket

logger = logging.getLogger("gameverse.websocket")


class ConnectionManager:
    def __init__(self):
        # Maps room_code -> list of active WebSockets
        self.room_connections: Dict[str, List[WebSocket]] = {}
        # Maps websocket -> user info dict
        self.socket_user_map: Dict[WebSocket, Dict[str, Any]] = {}

    async def connect(self, websocket: WebSocket, room_code: str, user_info: Dict[str, Any]):
        await websocket.accept()
        if room_code not in self.room_connections:
            self.room_connections[room_code] = []
        self.room_connections[room_code].append(websocket)
        self.socket_user_map[websocket] = {
            "room_code": room_code,
            "user_id": user_info.get("user_id"),
            "username": user_info.get("username")
        }
        logger.info(f"User {user_info.get('username')} connected to room {room_code}")

    def disconnect(self, websocket: WebSocket):
        user_info = self.socket_user_map.pop(websocket, None)
        if user_info:
            room_code = user_info.get("room_code")
            if room_code in self.room_connections:
                if websocket in self.room_connections[room_code]:
                    self.room_connections[room_code].remove(websocket)
                if not self.room_connections[room_code]:
                    del self.room_connections[room_code]
            logger.info(f"User {user_info.get('username')} disconnected from room {room_code}")
        return user_info

    async def broadcast(self, room_code: str, message: Dict[str, Any]):
        if room_code not in self.room_connections:
            return
        payload = json.dumps(message)
        dead_connections = []
        for connection in self.room_connections[room_code]:
            try:
                await connection.send_text(payload)
            except Exception as e:
                logger.error(f"Error sending message to client: {e}")
                dead_connections.append(connection)
        for dc in dead_connections:
            self.disconnect(dc)

    async def send_personal_message(self, websocket: WebSocket, message: Dict[str, Any]):
        try:
            await websocket.send_text(json.dumps(message))
        except Exception as e:
            logger.error(f"Error sending personal message: {e}")


manager = ConnectionManager()
