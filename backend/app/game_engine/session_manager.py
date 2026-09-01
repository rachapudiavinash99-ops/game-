from datetime import datetime, timezone
from typing import Dict, Any, Optional
from sqlalchemy.orm import Session
from app.repositories.game_repo import GameRepository
from app.repositories.task_repo import TaskRepository
from app.repositories.score_repo import ScoreRepository
from app.services.scoring_engine import ScoringEngine
from app.services.progression_service import ProgressionService
from app.services.achievement_service import AchievementService
from app.models.game import GameSession, SessionStatus, GameMode
from app.models.task import Answer, Task
from app.models.user import Profile
from app.core.exceptions import InvalidGameSessionError, ResourceNotFoundError


class GameSessionManager:
    @classmethod
    def start_session(
        cls,
        db: Session,
        user_id: Optional[int],
        mode: str = "QUICK_CHALLENGE",
        topic_id: Optional[int] = None,
        difficulty: Optional[str] = None,
        question_count: int = 5
    ) -> GameSession:
        """Initialize and persist a new game session with selected task sequence."""
        if mode == GameMode.SURVIVAL.value:
            lives = 3
            # Survival starts with more questions available in buffer
            tasks = TaskRepository.get_random_tasks(db, topic_id=topic_id, count=max(15, question_count))
        elif mode == GameMode.TIME_ATTACK.value:
            lives = 99
            tasks = TaskRepository.get_random_tasks(db, topic_id=topic_id, count=max(20, question_count))
        else:
            lives = 3
            tasks = TaskRepository.get_random_tasks(db, topic_id=topic_id, difficulty=difficulty, count=question_count)

        if not tasks:
            raise ResourceNotFoundError("Tasks", f"topic {topic_id} / difficulty {difficulty}")

        session = GameRepository.create_session(
            db=db,
            user_id=user_id,
            mode=mode,
            tasks=tasks,
            topic_id=topic_id,
            difficulty=difficulty,
            lives=lives
        )
        return session

    @classmethod
    def submit_answer(
        cls,
        db: Session,
        session_id: int,
        task_id: int,
        selected_answer_id: Optional[int],
        time_spent_seconds: float,
        user_id: Optional[int] = None
    ) -> Dict[str, Any]:
        """Process an answer submission, calculate score, update streak/lives, check game over."""
        session = GameRepository.get_session(db, session_id)
        if not session or session.status != SessionStatus.IN_PROGRESS.value:
            raise InvalidGameSessionError("This game session is not active.")

        # Find the task and verify the selected answer
        task = TaskRepository.get_by_id(db, task_id)
        if not task:
            raise ResourceNotFoundError("Task", task_id)

        correct_answer = next((ans for ans in task.answers if ans.is_correct), None)
        is_correct = False
        if selected_answer_id and correct_answer and selected_answer_id == correct_answer.id:
            is_correct = True

        # Update streak
        if is_correct:
            session.correct_count += 1
            session.streak_count += 1
            if session.streak_count > session.best_streak:
                session.best_streak = session.streak_count
        else:
            session.wrong_count += 1
            session.streak_count = 0
            if session.mode == GameMode.SURVIVAL.value:
                session.lives_remaining -= 1

        # Calculate authoritative score
        score_calc = ScoringEngine.calculate_question_score(
            difficulty=task.difficulty,
            is_correct=is_correct,
            time_spent_seconds=time_spent_seconds,
            time_limit_seconds=float(task.time_limit_seconds),
            current_streak=session.streak_count
        )

        points = score_calc["points"]
        session.score += points
        session.time_taken_seconds += time_spent_seconds

        # Record answer log
        GameRepository.record_player_answer(
            db=db,
            session_id=session.id,
            task_id=task.id,
            selected_answer_id=selected_answer_id,
            is_correct=is_correct,
            time_spent=time_spent_seconds,
            points=points,
            current_streak=session.streak_count
        )

        # Check termination condition
        is_game_over = False
        if session.mode == GameMode.SURVIVAL.value and session.lives_remaining <= 0:
            is_game_over = True
            session.status = SessionStatus.FAILED.value
        elif len(session.player_answers) >= session.total_questions:
            is_game_over = True
            session.status = SessionStatus.COMPLETED.value

        db.commit()
        db.refresh(session)

        return {
            "is_correct": is_correct,
            "correct_answer_id": correct_answer.id if correct_answer else 0,
            "points_earned": points,
            "streak": session.streak_count,
            "explanation": task.explanation,
            "current_score": session.score,
            "lives_remaining": session.lives_remaining,
            "is_game_over": is_game_over
        }

    @classmethod
    def finalize_session(cls, db: Session, session_id: int, user_id: Optional[int] = None) -> Dict[str, Any]:
        """Complete the session, compute accuracy, assign XP, update user profile and unlock achievements."""
        session = GameRepository.get_session(db, session_id)
        if not session:
            raise InvalidGameSessionError("Game session not found.")

        if session.status == SessionStatus.IN_PROGRESS.value:
            session.status = SessionStatus.COMPLETED.value
        
        session.completed_at = datetime.now(timezone.utc)

        total_ans = session.correct_count + session.wrong_count
        if total_ans > 0:
            session.accuracy = round((session.correct_count / total_ans) * 100.0, 1)
        else:
            session.accuracy = 0.0

        xp = ScoringEngine.calculate_xp_earned(session.score, session.accuracy, session.mode)
        session.xp_earned = xp

        level_up = False
        new_level = 1
        unlocked = []

        # If logged-in user, persist score record, progress profile and evaluate achievements
        target_uid = user_id or session.user_id
        if target_uid:
            ScoreRepository.add_score(
                db=db,
                user_id=target_uid,
                session_id=session.id,
                mode=session.mode,
                score=session.score,
                accuracy=session.accuracy,
                time_seconds=session.time_taken_seconds,
                topic_id=session.topic_id
            )

            prog = ProgressionService.add_xp_and_progress(
                db=db,
                user_id=target_uid,
                xp_amount=xp,
                score_amount=session.score,
                is_win=(session.status == SessionStatus.COMPLETED.value and session.accuracy >= 50.0)
            )
            level_up = prog.get("level_up", False)
            new_level = prog.get("new_level", 1)

            # Check profile streaks
            profile = db.query(Profile).filter(Profile.user_id == target_uid).first()
            if profile and session.best_streak > profile.best_streak:
                profile.best_streak = session.best_streak
                db.commit()

            unlocked = AchievementService.check_and_unlock(db, target_uid, session)

        db.commit()
        db.refresh(session)

        return {
            "session_id": session.id,
            "mode": session.mode,
            "status": session.status,
            "score": session.score,
            "xp_earned": session.xp_earned,
            "accuracy": session.accuracy,
            "time_taken_seconds": round(session.time_taken_seconds, 2),
            "total_questions": session.total_questions,
            "correct_count": session.correct_count,
            "wrong_count": session.wrong_count,
            "best_streak": session.best_streak,
            "level_up": level_up,
            "new_level": new_level,
            "unlocked_achievements": unlocked
        }
