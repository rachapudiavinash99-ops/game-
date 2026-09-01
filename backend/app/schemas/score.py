from datetime import datetime
from typing import Optional
from pydantic import ConfigDict, BaseModel


class ScoreResponse(BaseModel):
    id: int
    user_id: int
    username: Optional[str] = None
    display_name: Optional[str] = None
    avatar_url: Optional[str] = None
    mode: str
    topic_id: Optional[int]
    topic_name: Optional[str] = None
    score: int
    accuracy: float
    time_seconds: float
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
