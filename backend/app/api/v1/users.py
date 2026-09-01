from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.user import UserResponse, ProfileResponse, ProfileUpdate
from app.repositories.user_repo import UserRepository
from app.api.deps import get_current_user
from app.models.user import User

router = APIRouter(prefix="/users", tags=["Users"])


@router.get("/profile", response_model=ProfileResponse)
def get_profile(current_user: User = Depends(get_current_user)):
    return current_user.profile


@router.put("/profile", response_model=ProfileResponse)
def update_profile(
    data: ProfileUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    profile = UserRepository.update_profile(
        db=db,
        user_id=current_user.id,
        display_name=data.display_name,
        avatar_url=data.avatar_url,
        bio=data.bio
    )
    return profile
