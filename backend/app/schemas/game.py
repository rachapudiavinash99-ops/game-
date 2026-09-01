from datetime import datetime
from typing import List, Optional
from pydantic import ConfigDict, BaseModel
from app.schemas.task import TaskResponse


class StartGameRequest(BaseModel):
    mode: str = "QUICK_CHALLENGE"  # QUICK_CHALLENGE, TOPIC_CHALLENGE, TIME_ATTACK, SURVIVAL
    topic_id: Optional[int] = None
    difficulty: Optional[str] = None
    question_count: int = 5


class SubmitAnswerRequest(BaseModel):
    session_id: int
    task_id: int
    selected_answer_id: Optional[int] = None
    time_spent_seconds: float = 0.0


class SubmitAnswerResponse(BaseModel):
    is_correct: bool
    correct_answer_id: int
    points_earned: int
    streak: int
    explanation: Optional[str]
    current_score: int
    lives_remaining: int
    is_game_over: bool


class GameQuestionData(BaseModel):
    order: int
    task: TaskResponse
    time_limit_seconds: int


class GameSessionResponse(BaseModel):
    id: int
    mode: str
    topic_id: Optional[int]
    difficulty: Optional[str]
    status: str
    score: int
    xp_earned: int
    lives_remaining: int
    streak_count: int
    total_questions: int
    questions: List[GameQuestionData] = []
    started_at: datetime

    model_config = ConfigDict(from_attributes=True)


class GameResultResponse(BaseModel):
    session_id: int
    mode: str
    status: str
    score: int
    xp_earned: int
    accuracy: float
    time_taken_seconds: float
    total_questions: int
    correct_count: int
    wrong_count: int
    best_streak: int
    level_up: bool = False
    new_level: int = 1
    unlocked_achievements: List[str] = []
