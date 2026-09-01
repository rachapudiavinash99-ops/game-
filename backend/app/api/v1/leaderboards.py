from typing import Optional, List, Dict, Any
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.repositories.leaderboard_repo import LeaderboardRepository

router = APIRouter(prefix="/leaderboards", tags=["Leaderboards"])


@router.get("/global")
def get_global_leaderboard(
    limit: int = Query(50, ge=1, le=100),
    db: Session = Depends(get_db)
) -> List[Dict[str, Any]]:
    return LeaderboardRepository.get_global_leaderboard(db, limit=limit)
