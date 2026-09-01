from datetime import datetime, timezone
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.achievement import Achievement, UserAchievement


class AchievementRepository:
    @staticmethod
    def get_all(db: Session) -> List[Achievement]:
        return db.query(Achievement).all()

    @staticmethod
    def get_user_achievements(db: Session, user_id: int) -> List[UserAchievement]:
        return db.query(UserAchievement).filter(UserAchievement.user_id == user_id).all()

    @staticmethod
    def unlock(db: Session, user_id: int, achievement_id: int) -> UserAchievement:
        existing = db.query(UserAchievement).filter(
            UserAchievement.user_id == user_id,
            UserAchievement.achievement_id == achievement_id
        ).first()
        if existing:
            return existing
        
        ua = UserAchievement(
            user_id=user_id,
            achievement_id=achievement_id,
            unlocked_at=datetime.now(timezone.utc)
        )
        db.add(ua)
        db.commit()
        db.refresh(ua)
        return ua
