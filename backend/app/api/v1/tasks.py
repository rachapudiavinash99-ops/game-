from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.task import TaskResponse
from app.repositories.task_repo import TaskRepository

router = APIRouter(prefix="/tasks", tags=["Tasks"])


@router.get("", response_model=List[TaskResponse])
def list_tasks(
    topic_id: Optional[int] = Query(None),
    difficulty: Optional[str] = Query(None),
    tag: Optional[str] = Query(None),
    search: Optional[str] = Query(None),
    skip: int = Query(0, ge=0),
    limit: int = Query(20, ge=1, le=100),
    db: Session = Depends(get_db)
):
    tasks = TaskRepository.list_tasks(
        db=db,
        topic_id=topic_id,
        difficulty=difficulty,
        tag=tag,
        search=search,
        skip=skip,
        limit=limit
    )
    return tasks
