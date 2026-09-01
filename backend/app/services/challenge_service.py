from datetime import date, datetime, timezone
from typing import Optional, List
from sqlalchemy.orm import Session
from app.models.challenge import DailyChallenge, UserChallenge
from app.models.task import Task
from app.repositories.task_repo import TaskRepository
from app.services.progression_service import ProgressionService


class ChallengeService:
    @staticmethod
    def get_or_create_daily_challenge(db: Session) -> DailyChallenge:
        today = date.today()
        challenge = db.query(DailyChallenge).filter(DailyChallenge.challenge_date == today).first()
        if challenge:
            return challenge

        # Select 5 random tasks across topics for the daily challenge
        tasks = TaskRepository.get_random_tasks(db, count=5)
        task_ids = ",".join(str(t.id) for t in tasks) if tasks else "1,2,3"

        challenge = DailyChallenge(
            challenge_date=today,
            title=f"Daily Mastery Challenge - {today.strftime('%b %d, %Y')}",
            description="Complete today's handpicked set of mixed-topic questions for bonus XP and leaderboard recognition!",
            task_ids=task_ids,
            bonus_xp=150,
            bonus_score=500,
            is_active=True
        )
        db.add(challenge)
        db.commit()
        db.refresh(challenge)
        return challenge

    @staticmethod
    def complete_daily_challenge(db: Session, user_id: int, challenge_id: int, score: int) -> dict:
        challenge = db.query(DailyChallenge).filter(DailyChallenge.id == challenge_id).first()
        if not challenge:
            return {"error": "Challenge not found"}

        user_ch = db.query(UserChallenge).filter(
            UserChallenge.user_id == user_id,
            UserChallenge.challenge_id == challenge_id
        ).first()

        if user_ch and user_ch.is_completed:
            return {"status": "already_completed", "score": user_ch.score}

        if not user_ch:
            user_ch = UserChallenge(
                user_id=user_id,
                challenge_id=challenge_id,
                is_completed=True,
                score=score + challenge.bonus_score,
                completed_at=datetime.now(timezone.utc)
            )
            db.add(user_ch)
        else:
            user_ch.is_completed = True
            user_ch.score = score + challenge.bonus_score
            user_ch.completed_at = datetime.now(timezone.utc)

        ProgressionService.add_xp_and_progress(db, user_id, challenge.bonus_xp, challenge.bonus_score)
        db.commit()

        return {"status": "completed", "bonus_xp": challenge.bonus_xp, "bonus_score": challenge.bonus_score}
