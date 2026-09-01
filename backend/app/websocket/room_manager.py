import asyncio
from typing import Dict, Any, Optional
from sqlalchemy.orm import Session
from app.models.multiplayer import GameRoom, RoomPlayer, RoomStatus
from app.repositories.multiplayer_repo import MultiplayerRepository
from app.repositories.task_repo import TaskRepository
from app.services.scoring_engine import ScoringEngine
from app.websocket.connection_manager import manager


class MultiplayerRoomEngine:
    # Memory cache for active multiplayer match states: room_code -> match_state dict
    active_matches: Dict[str, Dict[str, Any]] = {}

    @classmethod
    async def handle_player_ready(cls, db: Session, room_code: str, user_id: int, is_ready: bool):
        room = db.query(GameRoom).filter(GameRoom.room_code == room_code).first()
        if not room:
            return
        player = db.query(RoomPlayer).filter(RoomPlayer.room_id == room.id, RoomPlayer.user_id == user_id).first()
        if player:
            player.is_ready = is_ready
            db.commit()

        # Broadcast player state update
        players_data = [
            {
                "user_id": p.user_id,
                "username": p.username,
                "is_host": p.is_host,
                "is_ready": p.is_ready,
                "score": p.score,
                "streak": p.streak
            }
            for p in room.players
        ]
        await manager.broadcast(room_code, {
            "type": "ROOM_UPDATE",
            "room_code": room_code,
            "status": room.status,
            "players": players_data
        })

    @classmethod
    async def start_game(cls, db: Session, room_code: str, user_id: int):
        room = db.query(GameRoom).filter(GameRoom.room_code == room_code).first()
        if not room or room.host_user_id != user_id:
            return

        # Fetch questions for the multiplayer game
        tasks = TaskRepository.get_random_tasks(db, topic_id=room.topic_id, difficulty=room.difficulty, count=room.question_count)
        if not tasks:
            tasks = TaskRepository.get_random_tasks(db, count=room.question_count)

        room.status = RoomStatus.IN_PROGRESS.value
        room.current_question_index = 0
        db.commit()

        questions_payload = []
        for t in tasks:
            questions_payload.append({
                "id": t.id,
                "title": t.title,
                "question": t.question,
                "difficulty": t.difficulty,
                "points": t.points,
                "time_limit": room.time_per_question,
                "explanation": t.explanation,
                "answers": [{"id": a.id, "text": a.text, "order": a.order} for a in t.answers],
                "correct_answer_id": next((a.id for a in t.answers if a.is_correct), 0)
            })

        cls.active_matches[room_code] = {
            "room_id": room.id,
            "questions": questions_payload,
            "current_index": 0,
            "scores": {p.user_id: 0 for p in room.players},
            "streaks": {p.user_id: 0 for p in room.players},
            "answers_submitted": set(),
            "time_per_question": room.time_per_question
        }

        # Broadcast game start countdown
        await manager.broadcast(room_code, {
            "type": "GAME_STARTING",
            "countdown": 3,
            "total_questions": len(tasks),
            "time_per_question": room.time_per_question
        })

        # Send first question after countdown
        await asyncio.sleep(3)
        await cls.broadcast_current_question(room_code)

    @classmethod
    async def broadcast_current_question(cls, room_code: str):
        match = cls.active_matches.get(room_code)
        if not match:
            return
        
        idx = match["current_index"]
        if idx >= len(match["questions"]):
            await cls.finalize_match(room_code)
            return

        q = match["questions"][idx]
        match["answers_submitted"] = set()

        await manager.broadcast(room_code, {
            "type": "NEW_QUESTION",
            "question_index": idx + 1,
            "total_questions": len(match["questions"]),
            "question": {
                "id": q["id"],
                "title": q["title"],
                "question": q["question"],
                "difficulty": q["difficulty"],
                "points": q["points"],
                "time_limit": match["time_per_question"],
                "answers": q["answers"]
            }
        })

    @classmethod
    async def submit_player_answer(cls, db: Session, room_code: str, user_id: int, task_id: int, answer_id: Optional[int], time_spent: float):
        match = cls.active_matches.get(room_code)
        if not match:
            return

        idx = match["current_index"]
        if idx >= len(match["questions"]):
            return
        
        q = match["questions"][idx]
        is_correct = (answer_id == q["correct_answer_id"])

        # Update streak and score
        current_streak = match["streaks"].get(user_id, 0)
        if is_correct:
            current_streak += 1
            match["streaks"][user_id] = current_streak
        else:
            match["streaks"][user_id] = 0

        score_res = ScoringEngine.calculate_question_score(
            difficulty=q["difficulty"],
            is_correct=is_correct,
            time_spent_seconds=time_spent,
            time_limit_seconds=float(match["time_per_question"]),
            current_streak=current_streak
        )

        match["scores"][user_id] = match["scores"].get(user_id, 0) + score_res["points"]
        match["answers_submitted"].add(user_id)

        # Update in database
        room = db.query(GameRoom).filter(GameRoom.room_code == room_code).first()
        if room:
            p = db.query(RoomPlayer).filter(RoomPlayer.room_id == room.id, RoomPlayer.user_id == user_id).first()
            if p:
                p.score = match["scores"][user_id]
                p.streak = match["streaks"][user_id]
                if is_correct:
                    p.correct_answers += 1
                db.commit()

        # Broadcast live score update
        leaderboard_data = []
        if room:
            for pl in sorted(room.players, key=lambda x: x.score, reverse=True):
                leaderboard_data.append({
                    "user_id": pl.user_id,
                    "username": pl.username,
                    "score": pl.score,
                    "streak": pl.streak,
                    "correct": pl.correct_answers
                })

        await manager.broadcast(room_code, {
            "type": "PLAYER_ANSWERED",
            "user_id": user_id,
            "is_correct": is_correct,
            "correct_answer_id": q["correct_answer_id"],
            "explanation": q.get("explanation"),
            "points": score_res["points"],
            "leaderboard": leaderboard_data
        })

    @classmethod
    async def next_question(cls, db: Session, room_code: str):
        match = cls.active_matches.get(room_code)
        if not match:
            return
        match["current_index"] += 1
        await cls.broadcast_current_question(room_code)

    @classmethod
    async def finalize_match(cls, room_code: str):
        match = cls.active_matches.pop(room_code, None)
        if not match:
            return

        from app.core.database import SessionLocal
        db = SessionLocal()
        try:
            room = db.query(GameRoom).filter(GameRoom.room_code == room_code).first()
            if not room:
                return

            room.status = RoomStatus.FINISHED.value

            # Determine winner
            players_sorted = sorted(room.players, key=lambda p: p.score, reverse=True)
            winner = players_sorted[0] if players_sorted else None
            if winner:
                room.winner_user_id = winner.user_id

            db.commit()

            results = [
                {
                    "rank": i + 1,
                    "user_id": p.user_id,
                    "username": p.username,
                    "score": p.score,
                    "correct_answers": p.correct_answers,
                    "is_winner": (winner and p.user_id == winner.user_id)
                }
                for i, p in enumerate(players_sorted)
            ]

            await manager.broadcast(room_code, {
                "type": "MATCH_OVER",
                "winner": {
                    "user_id": winner.user_id if winner else None,
                    "username": winner.username if winner else "No winner",
                    "score": winner.score if winner else 0
                } if winner else None,
                "results": results
            })
        finally:
            db.close()
