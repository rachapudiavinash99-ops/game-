from datetime import date, datetime
from typing import List, Optional
from pydantic import ConfigDict, BaseModel
from app.schemas.task import TaskResponse


class DailyChallengeResponse(BaseModel):
    id: int
    challenge_date: date
    title: str
    description: str
    topic_id: Optional[int]
    topic_name: Optional[str] = None
    bonus_xp: int
    bonus_score: int
    is_completed: bool = False
    tasks: List[TaskResponse] = []

    model_config = ConfigDict(from_attributes=True)


class CompleteChallengeRequest(BaseModel):
    challenge_id: int
    score: int
