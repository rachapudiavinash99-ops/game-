from typing import List, Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.achievement import AchievementResponse
from app.repositories.achievement_repo import AchievementRepository
from app.api.deps import get_optional_user
from app.models.user import User

router = APIRouter(prefix="/achievements", tags=["Achievements"])


@router.get("", response_model=List[AchievementResponse])
def list_achievements(
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_user)
):
    achievements = AchievementRepository.get_all(db)
    unlocked_map = {}
    if current_user:
        user_achs = AchievementRepository.get_user_achievements(db, current_user.id)
        unlocked_map = {ua.achievement_id: ua.unlocked_at for ua in user_achs}

    res = []
    for a in achievements:
        res.append({
            "id": a.id,
            "code": a.code,
            "title": a.title,
            "description": a.description,
            "icon": a.icon,
            "category": a.category,
            "requirement_type": a.requirement_type,
            "requirement_value": a.requirement_value,
            "xp_reward": a.xp_reward,
            "badge_color": a.badge_color,
            "unlocked": a.id in unlocked_map,
            "unlocked_at": unlocked_map.get(a.id)
        })
    return res
