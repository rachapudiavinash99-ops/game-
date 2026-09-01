from datetime import datetime
from typing import Optional
from pydantic import ConfigDict, BaseModel


class NotificationResponse(BaseModel):
    id: int
    title: str
    message: str
    type: str
    is_read: bool
    data: Optional[str] = None
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)
