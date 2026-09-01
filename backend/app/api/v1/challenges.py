from typing import Optional, List, Dict, Any
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.challenge import DailyChallengeResponse, CompleteChallengeRequest
from app.services.challenge_service import ChallengeService
from app.repositories.task_repo import TaskRepository
from app.api.deps import get_current_user, get_optional_user
from app.models.user import User
from app.models.challenge import UserChallenge

router = APIRouter(prefix="/challenges", tags=["Daily Challenges"])


@router.get("/daily", response_model=DailyChallengeResponse)
def get_daily_challenge(
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_user)
):
    challenge = ChallengeService.get_or_create_daily_challenge(db)
    is_completed = False
    if current_user:
        uc = db.query(UserChallenge).filter(
            UserChallenge.user_id == current_user.id,
            UserChallenge.challenge_id == challenge.id,
            UserChallenge.is_completed == True
        ).first()
        is_completed = bool(uc)

    # Fetch corresponding task objects
    task_id_list = [int(i.strip()) for i in challenge.task_ids.split(",") if i.strip().isdigit()]
    tasks = [TaskRepository.get_by_id(db, tid) for tid in task_id_list if TaskRepository.get_by_id(db, tid)]

    return {
        "id": challenge.id,
        "challenge_date": challenge.challenge_date,
        "title": challenge.title,
        "description": challenge.description,
        "topic_id": challenge.topic_id,
        "topic_name": challenge.topic.name if challenge.topic else "Mixed Topics",
        "bonus_xp": challenge.bonus_xp,
        "bonus_score": challenge.bonus_score,
        "is_completed": is_completed,
        "tasks": tasks
    }


@router.post("/daily/complete")
def complete_daily(
    data: CompleteChallengeRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return ChallengeService.complete_daily_challenge(db, current_user.id, data.challenge_id, data.score)
