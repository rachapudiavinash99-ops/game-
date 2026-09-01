from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.topic import Topic, Category
from app.models.task import Task


class TopicRepository:
    @staticmethod
    def get_all(db: Session, active_only: bool = True) -> List[Topic]:
        query = db.query(Topic)
        if active_only:
            query = query.filter(Topic.is_active == True)
        return query.order_by(Topic.order.asc(), Topic.name.asc()).all()

    @staticmethod
    def get_by_id(db: Session, topic_id: int) -> Optional[Topic]:
        return db.query(Topic).filter(Topic.id == topic_id).first()

    @staticmethod
    def get_by_slug(db: Session, slug: str) -> Optional[Topic]:
        return db.query(Topic).filter(Topic.slug == slug.lower()).first()

    @staticmethod
    def create(db: Session, name: str, slug: str, description: Optional[str] = None, icon: str = "Zap", color: str = "#6366f1", order: int = 0) -> Topic:
        topic = Topic(
            name=name,
            slug=slug.lower(),
            description=description,
            icon=icon,
            color=color,
            order=order,
            is_active=True
        )
        db.add(topic)
        db.commit()
        db.refresh(topic)
        return topic

    @staticmethod
    def update(db: Session, topic_id: int, **kwargs) -> Optional[Topic]:
        topic = db.query(Topic).filter(Topic.id == topic_id).first()
        if not topic:
            return None
        for key, val in kwargs.items():
            if val is not None and hasattr(topic, key):
                setattr(topic, key, val)
        db.commit()
        db.refresh(topic)
        return topic

    @staticmethod
    def delete(db: Session, topic_id: int) -> bool:
        topic = db.query(Topic).filter(Topic.id == topic_id).first()
        if not topic:
            return False
        db.delete(topic)
        db.commit()
        return True

    @staticmethod
    def get_task_count(db: Session, topic_id: int) -> int:
        return db.query(func.count(Task.id)).filter(Task.topic_id == topic_id, Task.is_active == True).scalar() or 0
