from datetime import datetime
from typing import Optional
from pydantic import ConfigDict, BaseModel


class AchievementResponse(BaseModel):
    id: int
    code: str
    title: str
    description: str
    icon: str
    category: str
    requirement_type: str
    requirement_value: int
    xp_reward: int
    badge_color: str
    unlocked: bool = False
    unlocked_at: Optional[datetime] = None

    model_config = ConfigDict(from_attributes=True)
