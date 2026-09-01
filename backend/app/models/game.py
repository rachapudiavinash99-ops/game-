import enum
from datetime import datetime, timezone
from sqlalchemy import Column, Integer, String, Boolean, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import TimestampMixin


class GameMode(str, enum.Enum):
    QUICK_CHALLENGE = "QUICK_CHALLENGE"
    TOPIC_CHALLENGE = "TOPIC_CHALLENGE"
    TIME_ATTACK = "TIME_ATTACK"
    SURVIVAL = "SURVIVAL"
    MULTIPLAYER = "MULTIPLAYER"


class SessionStatus(str, enum.Enum):
    IN_PROGRESS = "IN_PROGRESS"
    COMPLETED = "COMPLETED"
    ABANDONED = "ABANDONED"
    FAILED = "FAILED"


class GameSession(Base, TimestampMixin):
    __tablename__ = "game_sessions"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=True, index=True)
    mode = Column(String(30), default=GameMode.QUICK_CHALLENGE.value, nullable=False)
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="SET NULL"), nullable=True)
    difficulty = Column(String(20), nullable=True)
    status = Column(String(20), default=SessionStatus.IN_PROGRESS.value, nullable=False)
    
    # Results
    score = Column(Integer, default=0, nullable=False)
    xp_earned = Column(Integer, default=0, nullable=False)
    accuracy = Column(Float, default=0.0, nullable=False)
    time_taken_seconds = Column(Float, default=0.0, nullable=False)
    lives_remaining = Column(Integer, default=3, nullable=False)
    total_questions = Column(Integer, default=0, nullable=False)
    correct_count = Column(Integer, default=0, nullable=False)
    wrong_count = Column(Integer, default=0, nullable=False)
    streak_count = Column(Integer, default=0, nullable=False)
    best_streak = Column(Integer, default=0, nullable=False)
    
    started_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)
    completed_at = Column(DateTime, nullable=True)

    user = relationship("User", back_populates="game_sessions")
    topic = relationship("Topic", back_populates="game_sessions")
    questions = relationship("GameQuestion", back_populates="session", cascade="all, delete-orphan")
    player_answers = relationship("PlayerAnswer", back_populates="session", cascade="all, delete-orphan")
    score_entry = relationship("Score", back_populates="session", uselist=False, cascade="all, delete-orphan")


class GameQuestion(Base):
    __tablename__ = "game_questions"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("game_sessions.id", ondelete="CASCADE"), nullable=False, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False)
    order = Column(Integer, default=0, nullable=False)
    time_limit_seconds = Column(Integer, default=20, nullable=False)

    session = relationship("GameSession", back_populates="questions")
    task = relationship("Task", back_populates="game_questions")


class PlayerAnswer(Base):
    __tablename__ = "player_answers"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("game_sessions.id", ondelete="CASCADE"), nullable=False, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False)
    selected_answer_id = Column(Integer, ForeignKey("answers.id", ondelete="SET NULL"), nullable=True)
    is_correct = Column(Boolean, default=False, nullable=False)
    time_spent_seconds = Column(Float, default=0.0, nullable=False)
    points_earned = Column(Integer, default=0, nullable=False)
    streak_at_time = Column(Integer, default=0, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(timezone.utc), nullable=False)

    session = relationship("GameSession", back_populates="player_answers")
