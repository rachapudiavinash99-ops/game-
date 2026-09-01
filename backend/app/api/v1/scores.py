from typing import List, Optional
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.score import ScoreResponse
from app.repositories.score_repo import ScoreRepository
from app.repositories.game_repo import GameRepository
from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/scores", tags=["Scores & History"])


@router.get("/recent", response_model=List[ScoreResponse])
def get_recent_scores(
    limit: int = Query(20, ge=1, le=50),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    scores = ScoreRepository.get_top_scores(db=db, limit=limit)
    res = []
    for s in scores:
        res.append({
            "id": s.id,
            "user_id": s.user_id,
            "username": s.user.username if s.user else "Anonymous",
            "display_name": s.user.profile.display_name if (s.user and s.user.profile) else "Anonymous",
            "avatar_url": s.user.profile.avatar_url if (s.user and s.user.profile) else "",
            "mode": s.mode,
            "topic_id": s.topic_id,
            "topic_name": "General",
            "score": s.score,
            "accuracy": s.accuracy,
            "time_seconds": s.time_seconds,
            "created_at": s.created_at
        })
    return res


@router.get("/my-history")
def get_my_game_history(
    limit: int = Query(20, ge=1, le=50),
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    sessions = GameRepository.get_user_sessions(db=db, user_id=current_user.id, limit=limit)
    return [
        {
            "id": s.id,
            "mode": s.mode,
            "score": s.score,
            "xp_earned": s.xp_earned,
            "accuracy": s.accuracy,
            "time_taken_seconds": s.time_taken_seconds,
            "total_questions": s.total_questions,
            "correct_count": s.correct_count,
            "wrong_count": s.wrong_count,
            "best_streak": s.best_streak,
            "completed_at": s.completed_at
        }
        for s in sessions
    ]
