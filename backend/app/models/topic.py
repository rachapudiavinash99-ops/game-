from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from app.core.database import Base
from app.models.base import TimestampMixin


class Topic(Base, TimestampMixin):
    __tablename__ = "topics"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), unique=True, index=True, nullable=False)
    slug = Column(String(100), unique=True, index=True, nullable=False)
    description = Column(Text, nullable=True)
    icon = Column(String(50), default="Zap", nullable=False)
    color = Column(String(30), default="#6366f1", nullable=False)
    is_active = Column(Boolean, default=True, nullable=False)
    order = Column(Integer, default=0, nullable=False)

    categories = relationship("Category", back_populates="topic", cascade="all, delete-orphan")
    tasks = relationship("Task", back_populates="topic", cascade="all, delete-orphan")
    game_sessions = relationship("GameSession", back_populates="topic")


class Category(Base, TimestampMixin):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    topic_id = Column(Integer, ForeignKey("topics.id", ondelete="CASCADE"), nullable=False)
    name = Column(String(100), nullable=False)
    slug = Column(String(100), nullable=False)
    description = Column(Text, nullable=True)

    topic = relationship("Topic", back_populates="categories")
    tasks = relationship("Task", back_populates="category")
