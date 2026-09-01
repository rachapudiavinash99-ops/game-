import random
import string
from typing import List, Optional
from sqlalchemy.orm import Session
from app.models.multiplayer import GameRoom, RoomPlayer, RoomStatus


class MultiplayerRepository:
    @staticmethod
    def generate_room_code(length: int = 6) -> str:
        chars = string.ascii_uppercase + string.digits
        return "".join(random.choice(chars) for _ in range(length))

    @staticmethod
    def create_room(
        db: Session,
        host_user_id: int,
        host_username: str,
        name: str,
        topic_id: Optional[int] = None,
        difficulty: str = "MEDIUM",
        max_players: int = 4,
        question_count: int = 5,
        time_per_question: int = 15
    ) -> GameRoom:
        room_code = MultiplayerRepository.generate_room_code()
        while db.query(GameRoom).filter(GameRoom.room_code == room_code).first():
            room_code = MultiplayerRepository.generate_room_code()

        room = GameRoom(
            room_code=room_code,
            name=name,
            host_user_id=host_user_id,
            topic_id=topic_id,
            difficulty=difficulty,
            max_players=max_players,
            question_count=question_count,
            time_per_question=time_per_question,
            status=RoomStatus.WAITING.value
        )
        db.add(room)
        db.flush()

        # Add host as first player
        host_player = RoomPlayer(
            room_id=room.id,
            user_id=host_user_id,
            username=host_username,
            is_host=True,
            is_ready=True
        )
        db.add(host_player)
        db.commit()
        db.refresh(room)
        return room

    @staticmethod
    def get_room_by_code(db: Session, room_code: str) -> Optional[GameRoom]:
        return db.query(GameRoom).filter(GameRoom.room_code == room_code.upper()).first()

    @staticmethod
    def get_room_by_id(db: Session, room_id: int) -> Optional[GameRoom]:
        return db.query(GameRoom).filter(GameRoom.id == room_id).first()

    @staticmethod
    def list_active_rooms(db: Session) -> List[GameRoom]:
        return db.query(GameRoom).filter(GameRoom.status == RoomStatus.WAITING.value).all()

    @staticmethod
    def add_player(db: Session, room_id: int, user_id: int, username: str) -> RoomPlayer:
        player = db.query(RoomPlayer).filter(
            RoomPlayer.room_id == room_id,
            RoomPlayer.user_id == user_id
        ).first()
        if player:
            player.is_connected = True
            db.commit()
            return player

        player = RoomPlayer(
            room_id=room_id,
            user_id=user_id,
            username=username,
            is_host=False,
            is_ready=False
        )
        db.add(player)
        db.commit()
        db.refresh(player)
        return player
