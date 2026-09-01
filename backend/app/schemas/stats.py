from typing import Dict, List, Optional
from pydantic import BaseModel


class UserStatsResponse(BaseModel):
    user_id: int
    username: str
    level: int
    current_xp: int
    next_level_xp: int
    total_score: int
    total_games: int
    wins: int
    win_rate: float
    current_streak: int
    best_streak: int
    accuracy_rate: float
    mode_distribution: Dict[str, int]
    topic_performances: List[Dict[str, object]]
    recent_scores: List[int]


class SystemOverviewResponse(BaseModel):
    total_users: int
    total_games_played: int
    total_topics: int
    total_tasks: int
    total_rooms_created: int
    active_players_today: int
