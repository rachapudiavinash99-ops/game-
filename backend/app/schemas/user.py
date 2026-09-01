from datetime import datetime
from typing import Optional
from pydantic import ConfigDict, BaseModel, EmailStr


class ProfileResponse(BaseModel):
    id: int
    display_name: Optional[str]
    avatar_url: str
    bio: Optional[str]
    level: int
    current_xp: int
    next_level_xp: int
    total_score: int
    total_games: int
    wins: int
    win_rate: float
    current_streak: int
    best_streak: int

    model_config = ConfigDict(from_attributes=True)


class ProfileUpdate(BaseModel):
    display_name: Optional[str] = None
    avatar_url: Optional[str] = None
    bio: Optional[str] = None


class UserResponse(BaseModel):
    id: int
    username: str
    email: EmailStr
    role: str
    is_active: bool
    is_verified: bool
    created_at: datetime
    profile: Optional[ProfileResponse] = None

    model_config = ConfigDict(from_attributes=True)


class UserUpdate(BaseModel):
    email: Optional[EmailStr] = None
    is_active: Optional[bool] = None
    role: Optional[str] = None
