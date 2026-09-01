from typing import Optional, List, Dict, Any
from fastapi import APIRouter, Depends, WebSocket, WebSocketDisconnect, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.multiplayer import CreateRoomRequest, JoinRoomRequest, RoomResponse
from app.repositories.multiplayer_repo import MultiplayerRepository
from app.api.deps import get_current_user
from app.models.user import User
from app.websocket.connection_manager import manager
from app.websocket.room_manager import MultiplayerRoomEngine
from app.core.security import decode_token

router = APIRouter(prefix="/multiplayer", tags=["Multiplayer"])


@router.post("/rooms", response_model=RoomResponse)
def create_room(
    data: CreateRoomRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    room = MultiplayerRepository.create_room(
        db=db,
        host_user_id=current_user.id,
        host_username=current_user.username,
        name=data.name,
        topic_id=data.topic_id,
        difficulty=data.difficulty,
        max_players=data.max_players,
        question_count=data.question_count,
        time_per_question=data.time_per_question
    )
    return room


@router.get("/rooms", response_model=List[RoomResponse])
def list_rooms(db: Session = Depends(get_db)):
    return MultiplayerRepository.list_active_rooms(db)


@router.get("/rooms/{room_code}", response_model=RoomResponse)
def get_room(room_code: str, db: Session = Depends(get_db)):
    room = MultiplayerRepository.get_room_by_code(db, room_code)
    return room


@router.post("/rooms/join", response_model=RoomResponse)
def join_room(
    data: JoinRoomRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    room = MultiplayerRepository.get_room_by_code(db, data.room_code)
    if room:
        MultiplayerRepository.add_player(db, room.id, current_user.id, current_user.username)
    return room
