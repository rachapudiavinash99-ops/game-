from typing import List
from sqlalchemy.orm import Session
from app.models.achievement import Achievement, UserAchievement
from app.models.user import Profile
from app.models.notification import Notification
from app.models.game import GameSession


class AchievementService:
    @staticmethod
    def check_and_unlock(db: Session, user_id: int, session: GameSession) -> List[str]:
        """Evaluate all achievement conditions and unlock newly satisfied achievements."""
        profile = db.query(Profile).filter(Profile.user_id == user_id).first()
        if not profile:
            return []

        all_achievements = db.query(Achievement).all()
        user_ach_ids = {ua.achievement_id for ua in db.query(UserAchievement).filter(UserAchievement.user_id == user_id).all()}

        unlocked_titles = []

        for ach in all_achievements:
            if ach.id in user_ach_ids:
                continue

            satisfied = False
            req_type = ach.requirement_type
            req_val = ach.requirement_value

            if req_type == "games_played" and profile.total_games >= req_val:
                satisfied = True
            elif req_type == "correct_answers" and (profile.total_score // 10) >= req_val:
                satisfied = True
            elif req_type == "streak" and profile.best_streak >= req_val:
                satisfied = True
            elif req_type == "perfect_game" and session.accuracy >= 100.0 and session.total_questions >= 5:
                satisfied = True
            elif req_type == "high_score" and session.score >= req_val:
                satisfied = True
            elif req_type == "win_multiplayer" and profile.wins >= req_val:
                satisfied = True

            if satisfied:
                ua = UserAchievement(user_id=user_id, achievement_id=ach.id)
                db.add(ua)
                profile.current_xp += ach.xp_reward

                notif = Notification(
                    user_id=user_id,
                    title=f"Achievement Unlocked: {ach.title}",
                    message=f"You earned the {ach.title} badge and +{ach.xp_reward} XP!",
                    type="achievement",
                    data=f'{{"code": "{ach.code}", "icon": "{ach.icon}"}}'
                )
                db.add(notif)
                unlocked_titles.append(ach.title)

        if unlocked_titles:
            db.commit()
            db.refresh(profile)

        return unlocked_titles
