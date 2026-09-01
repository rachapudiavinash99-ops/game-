from typing import Optional
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.schemas.game import StartGameRequest, SubmitAnswerRequest, SubmitAnswerResponse, GameSessionResponse, GameResultResponse
from app.game_engine.session_manager import GameSessionManager
from app.api.deps import get_optional_user, get_current_user
from app.models.user import User

router = APIRouter(prefix="/games", tags=["Game Engine"])


@router.post("/start", response_model=GameSessionResponse)
def start_game(
    data: StartGameRequest,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_user)
):
    user_id = current_user.id if current_user else None
    session = GameSessionManager.start_session(
        db=db,
        user_id=user_id,
        mode=data.mode,
        topic_id=data.topic_id,
        difficulty=data.difficulty,
        question_count=data.question_count
    )
    return session


@router.post("/submit-answer", response_model=SubmitAnswerResponse)
def submit_answer(
    data: SubmitAnswerRequest,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_user)
):
    user_id = current_user.id if current_user else None
    result = GameSessionManager.submit_answer(
        db=db,
        session_id=data.session_id,
        task_id=data.task_id,
        selected_answer_id=data.selected_answer_id,
        time_spent_seconds=data.time_spent_seconds,
        user_id=user_id
    )
    return result


@router.post("/finish/{session_id}", response_model=GameResultResponse)
def finish_game(
    session_id: int,
    db: Session = Depends(get_db),
    current_user: Optional[User] = Depends(get_optional_user)
):
    user_id = current_user.id if current_user else None
    result = GameSessionManager.finalize_session(db=db, session_id=session_id, user_id=user_id)
    return result
