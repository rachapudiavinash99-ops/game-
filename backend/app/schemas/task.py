from typing import List, Optional
from pydantic import ConfigDict, BaseModel, Field


class AnswerBase(BaseModel):
    text: str
    is_correct: bool = False
    order: int = 0


class AnswerCreate(AnswerBase):
    pass


class AnswerResponse(BaseModel):
    id: int
    text: str
    order: int

    model_config = ConfigDict(from_attributes=True)


class AnswerAdminResponse(AnswerResponse):
    is_correct: bool

    model_config = ConfigDict(from_attributes=True)


class TaskBase(BaseModel):
    topic_id: int
    category_id: Optional[int] = None
    title: str = Field(..., max_length=200)
    question: str
    task_type: str = "MULTIPLE_CHOICE"
    difficulty: str = "EASY"
    points: int = 10
    time_limit_seconds: int = 20
    explanation: Optional[str] = None
    tags: str = ""
    is_active: bool = True


class TaskCreate(TaskBase):
    answers: List[AnswerCreate]


class TaskUpdate(BaseModel):
    topic_id: Optional[int] = None
    category_id: Optional[int] = None
    title: Optional[str] = None
    question: Optional[str] = None
    task_type: Optional[str] = None
    difficulty: Optional[str] = None
    points: Optional[int] = None
    time_limit_seconds: Optional[int] = None
    explanation: Optional[str] = None
    tags: Optional[str] = None
    is_active: Optional[bool] = None
    answers: Optional[List[AnswerCreate]] = None


class TaskResponse(BaseModel):
    id: int
    topic_id: int
    category_id: Optional[int]
    title: str
    question: str
    task_type: str
    difficulty: str
    points: int
    time_limit_seconds: int
    explanation: Optional[str]
    tags: str
    is_active: bool
    answers: List[AnswerResponse] = []

    model_config = ConfigDict(from_attributes=True)


class TaskAdminResponse(TaskResponse):
    answers: List[AnswerAdminResponse] = []
    created_by_user_id: Optional[int]

    model_config = ConfigDict(from_attributes=True)


class TaskBulkCreate(BaseModel):
    tasks: List[TaskCreate]
