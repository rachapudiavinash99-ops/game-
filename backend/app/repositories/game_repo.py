from datetime import datetime, timezone
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.game import GameSession, GameQuestion, PlayerAnswer, SessionStatus, GameMode
from app.models.task import Task


class GameRepository:
    @staticmethod
    def create_session(
        db: Session,
        user_id: Optional[int],
        mode: str,
        tasks: List[Task],
        topic_id: Optional[int] = None,
        difficulty: Optional[str] = None,
        lives: int = 3
    ) -> GameSession:
        session = GameSession(
            user_id=user_id,
            mode=mode,
            topic_id=topic_id,
            difficulty=difficulty,
            status=SessionStatus.IN_PROGRESS.value,
            score=0,
            xp_earned=0,
            accuracy=0.0,
            lives_remaining=lives,
            total_questions=len(tasks),
            correct_count=0,
            wrong_count=0,
            streak_count=0,
            best_streak=0,
            started_at=datetime.now(timezone.utc)
        )
        db.add(session)
        db.flush()

        for idx, task in enumerate(tasks):
            gq = GameQuestion(
                session_id=session.id,
                task_id=task.id,
                order=idx,
                time_limit_seconds=task.time_limit_seconds
            )
            db.add(gq)

        db.commit()
        db.refresh(session)
        return session

    @staticmethod
    def get_session(db: Session, session_id: int) -> Optional[GameSession]:
        return db.query(GameSession).filter(GameSession.id == session_id).first()

    @staticmethod
    def record_player_answer(
        db: Session,
        session_id: int,
        task_id: int,
        selected_answer_id: Optional[int],
        is_correct: bool,
        time_spent: float,
        points: int,
        current_streak: int
    ) -> PlayerAnswer:
        ans = PlayerAnswer(
            session_id=session_id,
            task_id=task_id,
            selected_answer_id=selected_answer_id,
            is_correct=is_correct,
            time_spent_seconds=time_spent,
            points_earned=points,
            streak_at_time=current_streak
        )
        db.add(ans)
        db.commit()
        db.refresh(ans)
        return ans

    @staticmethod
    def get_user_sessions(db: Session, user_id: int, limit: int = 20) -> List[GameSession]:
        return db.query(GameSession).filter(
            GameSession.user_id == user_id,
            GameSession.status == SessionStatus.COMPLETED.value
        ).order_by(GameSession.completed_at.desc()).limit(limit).all()
