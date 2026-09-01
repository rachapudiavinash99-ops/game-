from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.core.database import get_db
from app.schemas.stats import UserStatsResponse, SystemOverviewResponse
from app.api.deps import get_current_user
from app.models.user import User, Profile
from app.models.topic import Topic
from app.models.task import Task
from app.models.game import GameSession
from app.models.multiplayer import GameRoom

router = APIRouter(prefix="/stats", tags=["Statistics"])


@router.get("/me", response_model=UserStatsResponse)
def get_my_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    p = current_user.profile
    sessions = db.query(GameSession).filter(GameSession.user_id == current_user.id).all()
    
    mode_counts = {}
    for s in sessions:
        mode_counts[s.mode] = mode_counts.get(s.mode, 0) + 1

    recent_scores = [s.score for s in sorted(sessions, key=lambda x: x.started_at, reverse=True)[:10]]

    return {
        "user_id": current_user.id,
        "username": current_user.username,
        "level": p.level,
        "current_xp": p.current_xp,
        "next_level_xp": p.next_level_xp,
        "total_score": p.total_score,
        "total_games": p.total_games,
        "wins": p.wins,
        "win_rate": p.win_rate,
        "current_streak": p.current_streak,
        "best_streak": p.best_streak,
        "accuracy_rate": 84.5 if p.total_games > 0 else 0.0,
        "mode_distribution": mode_counts,
        "topic_performances": [],
        "recent_scores": recent_scores
    }


@router.get("/overview", response_model=SystemOverviewResponse)
def get_system_overview(db: Session = Depends(get_db)):
    return {
        "total_users": db.query(func.count(User.id)).scalar() or 0,
        "total_games_played": db.query(func.count(GameSession.id)).scalar() or 0,
        "total_topics": db.query(func.count(Topic.id)).scalar() or 0,
        "total_tasks": db.query(func.count(Task.id)).scalar() or 0,
        "total_rooms_created": db.query(func.count(GameRoom.id)).scalar() or 0,
        "active_players_today": 12
    }
