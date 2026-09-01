import statistics
from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session
from app.models.game import GameSession, PlayerAnswer
from app.models.score import Score
from app.models.user import Profile


class AnalyticsEngine:
    """
    Advanced player analytics and performance radar engine.
    Computes dimension scores across Speed, Accuracy, Consistency, Endurance, Versatility, and Mastery.
    """

    @classmethod
    def compute_player_radar_metrics(cls, db: Session, user_id: int) -> Dict[str, float]:
        """
        Compute 6-dimensional gamer capability vector (0 to 100):
        1. Accuracy: Lifetime accuracy percentage
        2. Speed: Ratio of speed bonuses earned vs maximum possible
        3. Consistency: Low variance in score distribution across sessions
        4. Endurance: Long survival runs and time attack perseverance
        5. Versatility: Diversity of topics played
        6. Mastery: Performance on HARD and EXPERT difficulty questions
        """
        sessions = db.query(GameSession).filter(GameSession.user_id == user_id).all()
        if not sessions:
            return {
                "accuracy": 50.0,
                "speed": 50.0,
                "consistency": 50.0,
                "endurance": 50.0,
                "versatility": 50.0,
                "mastery": 50.0
            }

        total_correct = sum(s.correct_count for s in sessions)
        total_questions = sum(s.total_questions for s in sessions)
        accuracy_score = (total_correct / max(1, total_questions)) * 100.0

        # Speed metric
        time_spent_avg = sum(s.time_taken_seconds for s in sessions) / max(1, len(sessions))
        speed_score = max(10.0, min(100.0, 100.0 - (time_spent_avg * 1.5)))

        # Consistency (inverse of score standard deviation coefficient)
        scores = [s.score for s in sessions]
        if len(scores) > 1:
            stdev = statistics.stdev(scores)
            mean_score = statistics.mean(scores)
            cv = stdev / max(1.0, mean_score)
            consistency_score = max(20.0, min(100.0, 100.0 - (cv * 40.0)))
        else:
            consistency_score = 65.0

        # Versatility
        distinct_topics = {s.topic_id for s in sessions if s.topic_id is not None}
        versatility_score = min(100.0, (len(distinct_topics) / 10.0) * 100.0)

        # Endurance
        max_streak = max((s.best_streak for s in sessions), default=0)
        endurance_score = min(100.0, max(20.0, max_streak * 10.0))

        # Mastery
        hard_sessions = [s for s in sessions if s.difficulty in ("HARD", "EXPERT")]
        if hard_sessions:
            hard_correct = sum(s.correct_count for s in hard_sessions)
            hard_total = sum(s.total_questions for s in hard_sessions)
            mastery_score = (hard_correct / max(1, hard_total)) * 100.0
        else:
            mastery_score = 40.0

        return {
            "accuracy": round(accuracy_score, 1),
            "speed": round(speed_score, 1),
            "consistency": round(consistency_score, 1),
            "endurance": round(endurance_score, 1),
            "versatility": round(versatility_score, 1),
            "mastery": round(mastery_score, 1)
        }
