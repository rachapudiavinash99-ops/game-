from typing import List, Optional
from pydantic import ConfigDict, BaseModel


class CategoryBase(BaseModel):
    name: str
    slug: str
    description: Optional[str] = None


class CategoryCreate(CategoryBase):
    pass


class CategoryResponse(CategoryBase):
    id: int
    topic_id: int

    model_config = ConfigDict(from_attributes=True)


class TopicBase(BaseModel):
    name: str
    slug: str
    description: Optional[str] = None
    icon: str = "Zap"
    color: str = "#6366f1"
    is_active: bool = True
    order: int = 0


class TopicCreate(TopicBase):
    pass


class TopicUpdate(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    icon: Optional[str] = None
    color: Optional[str] = None
    is_active: Optional[bool] = None
    order: Optional[int] = None


class TopicResponse(TopicBase):
    id: int
    task_count: Optional[int] = 0
    categories: List[CategoryResponse] = []

    model_config = ConfigDict(from_attributes=True)
