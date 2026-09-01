from datetime import datetime, timezone, timedelta
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.score import Score
from app.models.user import User, Profile


class ScoreRepository:
    @staticmethod
    def add_score(
        db: Session,
        user_id: int,
        session_id: int,
        mode: str,
        score: int,
        accuracy: float,
        time_seconds: float,
        topic_id: Optional[int] = None
    ) -> Score:
        score_record = Score(
            user_id=user_id,
            session_id=session_id,
            mode=mode,
            topic_id=topic_id,
            score=score,
            accuracy=accuracy,
            time_seconds=time_seconds,
            created_at=datetime.now(timezone.utc)
        )
        db.add(score_record)
        db.commit()
        db.refresh(score_record)
        return score_record

    @staticmethod
    def get_top_scores(
        db: Session,
        mode: Optional[str] = None,
        topic_id: Optional[int] = None,
        timeframe: str = "all_time",
        limit: int = 20
    ) -> List[Score]:
        query = db.query(Score)
        if mode:
            query = query.filter(Score.mode == mode)
        if topic_id:
            query = query.filter(Score.topic_id == topic_id)
        
        now = datetime.now(timezone.utc)
        if timeframe == "weekly":
            query = query.filter(Score.created_at >= now - timedelta(days=7))
        elif timeframe == "monthly":
            query = query.filter(Score.created_at >= now - timedelta(days=30))
            
        return query.order_by(Score.score.desc(), Score.time_seconds.asc()).limit(limit).all()
