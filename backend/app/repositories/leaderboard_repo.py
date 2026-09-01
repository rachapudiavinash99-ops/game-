from typing import List, Dict, Any
from sqlalchemy.orm import Session
from sqlalchemy import desc
from app.models.user import User, Profile
from app.models.score import Score


class LeaderboardRepository:
    @staticmethod
    def get_global_leaderboard(db: Session, limit: int = 50) -> List[Dict[str, Any]]:
        profiles = db.query(Profile).join(User).filter(
            User.is_active == True
        ).order_by(
            desc(Profile.total_score),
            desc(Profile.current_xp)
        ).limit(limit).all()

        results = []
        for rank, p in enumerate(profiles, start=1):
            results.append({
                "rank": rank,
                "user_id": p.user_id,
                "username": p.user.username if p.user else "Player",
                "display_name": p.display_name or (p.user.username if p.user else "Player"),
                "avatar_url": p.avatar_url,
                "level": p.level,
                "xp": p.current_xp,
                "total_score": p.total_score,
                "total_games": p.total_games,
                "wins": p.wins,
                "win_rate": p.win_rate,
                "best_streak": p.best_streak
            })
        return results
