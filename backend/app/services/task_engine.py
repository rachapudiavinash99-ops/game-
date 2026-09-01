from typing import List, Optional
from sqlalchemy.orm import Session
from app.repositories.task_repo import TaskRepository
from app.repositories.topic_repo import TopicRepository
from app.models.task import Task
from app.models.topic import Topic


class TaskEngine:
    @staticmethod
    def get_challenge_tasks(
        db: Session,
        topic_id: Optional[int] = None,
        difficulty: Optional[str] = None,
        count: int = 5
    ) -> List[Task]:
        """Fetch dynamically selected tasks for a game session."""
        return TaskRepository.get_random_tasks(db, topic_id=topic_id, difficulty=difficulty, count=count)

    @staticmethod
    def get_all_active_topics(db: Session) -> List[Topic]:
        return TopicRepository.get_all(db, active_only=True)
