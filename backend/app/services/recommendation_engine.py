from typing import List, Dict, Any, Optional
from sqlalchemy.orm import Session
from app.models.topic import Topic
from app.models.game import GameSession
from app.models.task import Task


class RecommendationEngine:
    """
    Personalized training recommendation service.
    Analyzes historical player weaknesses and generates targeted daily drills.
    """

    @classmethod
    def get_recommended_topics(cls, db: Session, user_id: int, limit: int = 3) -> List[Dict[str, Any]]:
        """Identify topics where player accuracy is lowest or least explored."""
        all_topics = db.query(Topic).filter(Topic.is_active == True).all()
        user_sessions = db.query(GameSession).filter(GameSession.user_id == user_id).all()

        topic_stats: Dict[int, Dict[str, Any]] = {}
        for t in all_topics:
            topic_stats[t.id] = {
                "topic": t,
                "played": 0,
                "correct": 0,
                "total": 0,
                "accuracy": 0.0
            }

        for s in user_sessions:
            if s.topic_id and s.topic_id in topic_stats:
                topic_stats[s.topic_id]["played"] += 1
                topic_stats[s.topic_id]["correct"] += s.correct_count
                topic_stats[s.topic_id]["total"] += s.total_questions

        recommendations = []
        for tid, stat in topic_stats.items():
            if stat["total"] > 0:
                stat["accuracy"] = (stat["correct"] / stat["total"]) * 100.0
                priority = 100.0 - stat["accuracy"]  # Lower accuracy = higher recommendation priority
            else:
                priority = 85.0  # Unexplored topic

            recommendations.append({
                "topic_id": stat["topic"].id,
                "topic_name": stat["topic"].name,
                "slug": stat["topic"].slug,
                "icon": stat["topic"].icon,
                "color": stat["topic"].color,
                "priority_score": round(priority, 1),
                "reason": "Targeted accuracy training" if stat["total"] > 0 else "New domain exploration"
            })

        recommendations.sort(key=lambda x: x["priority_score"], reverse=True)
        return recommendations[:limit]
