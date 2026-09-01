from typing import List, Optional
import random
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.task import Task, Answer, DifficultyLevel


class TaskRepository:
    @staticmethod
    def get_by_id(db: Session, task_id: int) -> Optional[Task]:
        return db.query(Task).filter(Task.id == task_id).first()

    @staticmethod
    def list_tasks(
        db: Session,
        topic_id: Optional[int] = None,
        difficulty: Optional[str] = None,
        tag: Optional[str] = None,
        search: Optional[str] = None,
        skip: int = 0,
        limit: int = 50,
        active_only: bool = True
    ) -> List[Task]:
        query = db.query(Task)
        if active_only:
            query = query.filter(Task.is_active == True)
        if topic_id:
            query = query.filter(Task.topic_id == topic_id)
        if difficulty:
            query = query.filter(Task.difficulty == difficulty.upper())
        if tag:
            query = query.filter(Task.tags.ilike(f"%{tag}%"))
        if search:
            query = query.filter((Task.title.ilike(f"%{search}%")) | (Task.question.ilike(f"%{search}%")))
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def get_random_tasks(
        db: Session,
        topic_id: Optional[int] = None,
        difficulty: Optional[str] = None,
        count: int = 5
    ) -> List[Task]:
        query = db.query(Task).filter(Task.is_active == True)
        if topic_id:
            query = query.filter(Task.topic_id == topic_id)
        if difficulty:
            query = query.filter(Task.difficulty == difficulty.upper())
        
        all_matching = query.all()
        if not all_matching:
            # Fallback if no matching topic/difficulty: return any active tasks
            all_matching = db.query(Task).filter(Task.is_active == True).all()
        
        return random.sample(all_matching, min(count, len(all_matching)))

    @staticmethod
    def create(
        db: Session,
        topic_id: int,
        title: str,
        question: str,
        answers_data: list,
        category_id: Optional[int] = None,
        task_type: str = "MULTIPLE_CHOICE",
        difficulty: str = DifficultyLevel.EASY.value,
        points: int = 10,
        time_limit_seconds: int = 20,
        explanation: Optional[str] = None,
        tags: str = "",
        created_by_user_id: Optional[int] = None
    ) -> Task:
        task = Task(
            topic_id=topic_id,
            category_id=category_id,
            title=title,
            question=question,
            task_type=task_type,
            difficulty=difficulty.upper(),
            points=points,
            time_limit_seconds=time_limit_seconds,
            explanation=explanation,
            tags=tags,
            is_active=True,
            created_by_user_id=created_by_user_id
        )
        db.add(task)
        db.flush()

        for idx, ans in enumerate(answers_data):
            answer = Answer(
                task_id=task.id,
                text=ans["text"] if isinstance(ans, dict) else ans.text,
                is_correct=ans.get("is_correct", False) if isinstance(ans, dict) else ans.is_correct,
                order=idx
            )
            db.add(answer)
        
        db.commit()
        db.refresh(task)
        return task

    @staticmethod
    def delete(db: Session, task_id: int) -> bool:
        task = db.query(Task).filter(Task.id == task_id).first()
        if not task:
            return False
        db.delete(task)
        db.commit()
        return True
