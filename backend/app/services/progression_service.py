from typing import Dict, Any, Tuple
from sqlalchemy.orm import Session
from app.models.user import Profile
from app.models.notification import Notification
from app.core.config import settings


class ProgressionService:
    @staticmethod
    def get_xp_for_level(level: int) -> int:
        """Calculate total XP needed to reach next level: base * (level ^ growth_factor)"""
        if level <= 1:
            return settings.XP_BASE
        return int(settings.XP_BASE * (level ** settings.XP_GROWTH_FACTOR))

    @classmethod
    def add_xp_and_progress(cls, db: Session, user_id: int, xp_amount: int, score_amount: int, is_win: bool = False) -> Dict[str, Any]:
        profile = db.query(Profile).filter(Profile.user_id == user_id).first()
        if not profile:
            return {"level_up": False, "new_level": 1, "current_xp": 0}

        profile.total_score += score_amount
        profile.total_games += 1
        if is_win:
            profile.wins += 1
        if profile.total_games > 0:
            profile.win_rate = round((profile.wins / profile.total_games) * 100, 1)

        profile.current_xp += xp_amount

        initial_level = profile.level
        level_up = False

        # Level up loop while XP exceeds threshold
        while profile.current_xp >= profile.next_level_xp:
            profile.current_xp -= profile.next_level_xp
            profile.level += 1
            profile.next_level_xp = cls.get_xp_for_level(profile.level)
            level_up = True

        if level_up:
            # Create in-app level up notification
            notif = Notification(
                user_id=user_id,
                title="Level Up!",
                message=f"Congratulations! You reached Level {profile.level}!",
                type="level_up",
                data=f'{{"level": {profile.level}}}'
            )
            db.add(notif)

        db.commit()
        db.refresh(profile)

        return {
            "level_up": level_up,
            "previous_level": initial_level,
            "new_level": profile.level,
            "current_xp": profile.current_xp,
            "next_level_xp": profile.next_level_xp
        }
