from typing import List, Optional
from fastapi import APIRouter, Depends, status, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserResponse
from app.schemas.task import TaskCreate, TaskAdminResponse, TaskUpdate
from app.schemas.topic import TopicCreate, TopicResponse, TopicUpdate
from app.schemas.admin import AuditLogResponse, AdminUserUpdate
from app.repositories.user_repo import UserRepository
from app.repositories.task_repo import TaskRepository
from app.repositories.topic_repo import TopicRepository
from app.repositories.audit_repo import AuditRepository
from app.api.deps import get_current_admin
from app.models.user import User
from app.models.topic import Topic
from app.models.task import Task

router = APIRouter(prefix="/admin", tags=["Admin Portal"])


@router.get("/users", response_model=List[UserResponse])
def admin_list_users(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin)
):
    return UserRepository.list_users(db, skip=skip, limit=limit, search=search)


@router.put("/users/{user_id}/status")
def admin_update_user_status(
    user_id: int,
    data: AdminUserUpdate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin)
):
    user = UserRepository.get_by_id(db, user_id)
    if not user:
        return {"error": "User not found"}
    if data.is_active is not None:
        user.is_active = data.is_active
    if data.role is not None:
        user.role = data.role
    if data.level is not None and user.profile:
        user.profile.level = data.level
    db.commit()

    AuditRepository.log(
        db=db,
        action="UPDATE_USER_STATUS",
        resource_type="USER",
        user_id=admin.id,
        resource_id=str(user_id),
        details={"is_active": user.is_active, "role": user.role}
    )
    return {"status": "success", "user_id": user.id, "is_active": user.is_active}


@router.post("/topics", response_model=TopicResponse)
def admin_create_topic(
    data: TopicCreate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin)
):
    topic = TopicRepository.create(
        db=db,
        name=data.name,
        slug=data.slug,
        description=data.description,
        icon=data.icon,
        color=data.color,
        order=data.order
    )
    AuditRepository.log(db, "CREATE_TOPIC", "TOPIC", user_id=admin.id, resource_id=str(topic.id))
    return topic


@router.post("/tasks", response_model=TaskAdminResponse)
def admin_create_task(
    data: TaskCreate,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin)
):
    task = TaskRepository.create(
        db=db,
        topic_id=data.topic_id,
        category_id=data.category_id,
        title=data.title,
        question=data.question,
        answers_data=data.answers,
        task_type=data.task_type,
        difficulty=data.difficulty,
        points=data.points,
        time_limit_seconds=data.time_limit_seconds,
        explanation=data.explanation,
        tags=data.tags,
        created_by_user_id=admin.id
    )
    AuditRepository.log(db, "CREATE_TASK", "TASK", user_id=admin.id, resource_id=str(task.id))
    return task


@router.delete("/tasks/{task_id}")
def admin_delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin)
):
    success = TaskRepository.delete(db, task_id)
    AuditRepository.log(db, "DELETE_TASK", "TASK", user_id=admin.id, resource_id=str(task_id))
    return {"status": "deleted" if success else "not_found"}


@router.get("/audit-logs", response_model=List[AuditLogResponse])
def admin_get_audit_logs(
    skip: int = Query(0, ge=0),
    limit: int = Query(50, ge=1, le=100),
    db: Session = Depends(get_db),
    admin: User = Depends(get_current_admin)
):
    return AuditRepository.list_logs(db, skip=skip, limit=limit)
