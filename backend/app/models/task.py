import enum
from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey, Enum
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import TimestampMixin


class DifficultyLevel(str, enum.Enum):
    EASY = "EASY"
    MEDIUM = "MEDIUM"
    HARD = "HARD"
    EXPERT = "EXPERT"


class TaskType(str, enum.Enum):
    MULTIPLE_CHOICE = "MULTIPLE_CHOICE"
    BOOLEAN = "BOOLEAN"
    CODE_SNIPPET = "CODE_SNIPPET"


class Task(Base, TimestampMixin):
    __tablename__ = "tasks"

    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="CASCADE"), nullable=False, index=True)
    category_id = Column(Integer, ForeignKey("categories.id", ondelete="SET NULL"), nullable=True)
    title = Column(String(200), nullable=False)
    question = Column(Text, nullable=False)
    task_type = Column(String(30), default=TaskType.MULTIPLE_CHOICE.value, nullable=False)
    difficulty = Column(String(20), default=DifficultyLevel.EASY.value, nullable=False, index=True)
    points = Column(Integer, default=10, nullable=False)
    time_limit_seconds = Column(Integer, default=20, nullable=False)
    explanation = Column(Text, nullable=True)
    tags = Column(String(255), default="", nullable=False)  # Comma-separated tags
    is_active = Column(Boolean, default=True, nullable=False)
    created_by_user_id = Column(Integer, ForeignKey("users.id", ondelete="SET NULL"), nullable=True)

    topic = relationship("Topic", back_populates="tasks")
    category = relationship("Category", back_populates="tasks")
    answers = relationship("Answer", back_populates="task", cascade="all, delete-orphan")
    game_questions = relationship("GameQuestion", back_populates="task")


class Answer(Base):
    __tablename__ = "answers"

    id = Column(Integer, primary_key=True, index=True)
    task_id = Column(Integer, ForeignKey("tasks.id", ondelete="CASCADE"), nullable=False, index=True)
    text = Column(Text, nullable=False)
    is_correct = Column(Boolean, default=False, nullable=False)
    order = Column(Integer, default=0, nullable=False)

    task = relationship("Task", back_populates="answers")
