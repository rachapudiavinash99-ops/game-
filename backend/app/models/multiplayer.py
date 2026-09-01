import enum
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import TimestampMixin


class RoomStatus(str, enum.Enum):
    WAITING = "WAITING"
    IN_PROGRESS = "IN_PROGRESS"
    FINISHED = "FINISHED"
    CANCELLED = "CANCELLED"


class GameRoom(Base, TimestampMixin):
    __tablename__ = "game_rooms"

    id = Column(Integer, primary_key=True, index=True)
    room_code = Column(String(10), unique=True, index=True, nullable=False)
    name = Column(String(100), nullable=False)
    host_user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="SET NULL"), nullable=True)
    difficulty = Column(String(20), default="MEDIUM", nullable=False)
    max_players = Column(Integer, default=4, nullable=False)
    question_count = Column(Integer, default=5, nullable=False)
    time_per_question = Column(Integer, default=15, nullable=False)
    status = Column(String(20), default=RoomStatus.WAITING.value, nullable=False)
    current_question_index = Column(Integer, default=0, nullable=False)
    winner_user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    players = relationship("RoomPlayer", back_populates="room", cascade="all, delete-orphan")


class RoomPlayer(Base):
    __tablename__ = "room_players"

    id = Column(Integer, primary_key=True, index=True)
    room_id = Column(Integer, ForeignKey("game_rooms.id", ondelete="CASCADE"), nullable=False, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    username = Column(String(50), nullable=False)
    is_host = Column(Boolean, default=False, nullable=False)
    is_ready = Column(Boolean, default=False, nullable=False)
    score = Column(Integer, default=0, nullable=False)
    streak = Column(Integer, default=0, nullable=False)
    correct_answers = Column(Integer, default=0, nullable=False)
    is_connected = Column(Boolean, default=True, nullable=False)
    joined_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    room = relationship("GameRoom", back_populates="players")
