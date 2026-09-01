from datetime import datetime
from typing import List, Optional
from pydantic import ConfigDict, BaseModel
from app.schemas.task import TaskResponse


class CreateRoomRequest(BaseModel):
    name: str
    topic_id: Optional[int] = None
    difficulty: str = "MEDIUM"
    max_players: int = 4
    question_count: int = 5
    time_per_question: int = 15


class JoinRoomRequest(BaseModel):
    room_code: str


class PlayerResponse(BaseModel):
    id: int
    user_id: int
    username: str
    is_host: bool
    is_ready: bool
    score: int
    streak: int
    correct_answers: int
    is_connected: bool

    model_config = ConfigDict(from_attributes=True)


class RoomResponse(BaseModel):
    id: int
    room_code: str
    name: str
    host_user_id: Optional[int]
    topic_id: Optional[int]
    difficulty: str
    max_players: int
    question_count: int
    time_per_question: int
    status: str
    current_question_index: int
    winner_user_id: Optional[int]
    players: List[PlayerResponse] = []
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
