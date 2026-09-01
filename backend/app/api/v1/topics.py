from typing import Optional, List, Dict, Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.topic import TopicResponse
from app.repositories.topic_repo import TopicRepository

router = APIRouter(prefix="/topics", tags=["Topics"])


@router.get("", response_model=List[TopicResponse])
def list_topics(db: Session = Depends(get_db)):
    topics = TopicRepository.get_all(db, active_only=True)
    res = []
    for t in topics:
        res.append({
            "id": t.id,
            "name": t.name,
            "slug": t.slug,
            "description": t.description,
            "icon": t.icon,
            "color": t.color,
            "is_active": t.is_active,
            "order": t.order,
            "task_count": TopicRepository.get_task_count(db, t.id),
            "categories": t.categories
        })
    return res
