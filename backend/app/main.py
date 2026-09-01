
import logging
from contextlib import asynccontextmanager
from fastapi import FastAPI, WebSocket, WebSocketDisconnect, Query, Request, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse

from app.core.config import settings
from app.core.logging import setup_logging, logger
from app.core.database import SessionLocal, Base, engine
from app.core.exceptions import GameVerseException
from app.core.security import decode_token
from app.api.router import api_router
from app.seeds.seed_runner import run_seeds
from app.websocket.connection_manager import manager
from app.websocket.room_manager import MultiplayerRoomEngine


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Setup structured logging
    setup_logging()
    logger.info(f"Starting {settings.PROJECT_NAME} v{settings.VERSION}...")
    
    # Initialize database tables and seed initial topics, tasks, achievements, users
    db = SessionLocal()
    try:
        run_seeds(db)
        logger.info("Database schemas and seed data ready.")
    except Exception as e:
        logger.error(f"Database startup error: {e}")
    finally:
        db.close()

    yield

    logger.info("Shutting down GameVerse backend...")


app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION,
    description=settings.DESCRIPTION,
    openapi_url=f"{settings.API_V1_STR}/openapi.json",
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan
)

# CORS configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5174",
        "http://127.0.0.1:5174",
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:3000",
        "http://127.0.0.1:3000",
        "http://localhost:8008",
        "http://127.0.0.1:8008",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Centralized exception handler
@app.exception_handler(GameVerseException)
async def gameverse_exception_handler(request: Request, exc: GameVerseException):
    return JSONResponse(
        status_code=exc.status_code,
        content={
            "error": True,
            "error_code": exc.error_code,
            "message": exc.detail,
            "extra": exc.extra
        }
    )


# Include all versioned REST API routers
app.include_router(api_router, prefix=settings.API_V1_STR)


# Real-Time WebSocket endpoint for Multiplayer gameplay
@app.websocket("/ws/multiplayer/{room_code}")
async def websocket_multiplayer_endpoint(
    websocket: WebSocket,
    room_code: str,
    token: str = Query(...)
):
    # Authenticate token on handshake
    try:
        payload = decode_token(token)
        user_id = int(payload.get("sub"))
    except Exception:
        await websocket.close(code=status.WS_1008_POLICY_VIOLATION)
        return

    db = SessionLocal()
    try:
        from app.models.user import User
        user = db.query(User).filter(User.id == user_id).first()
        username = user.username if user else f"Player_{user_id}"

        await manager.connect(websocket, room_code, {"user_id": user_id, "username": username})

        # Process incoming game messages
        while True:
            data = await websocket.receive_json()
            action_type = data.get("type")

            if action_type == "PLAYER_READY":
                is_ready = bool(data.get("is_ready", True))
                await MultiplayerRoomEngine.handle_player_ready(db, room_code, user_id, is_ready)

            elif action_type == "START_GAME":
                await MultiplayerRoomEngine.start_game(db, room_code, user_id)

            elif action_type == "SUBMIT_ANSWER":
                task_id = data.get("task_id")
                answer_id = data.get("answer_id")
                time_spent = float(data.get("time_spent", 0.0))
                await MultiplayerRoomEngine.submit_player_answer(db, room_code, user_id, task_id, answer_id, time_spent)

            elif action_type == "NEXT_QUESTION":
                await MultiplayerRoomEngine.next_question(db, room_code)

            elif action_type == "CHAT_MESSAGE":
                text = data.get("message", "")
                await manager.broadcast(room_code, {
                    "type": "CHAT",
                    "user_id": user_id,
                    "username": username,
                    "message": text
                })

    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception as e:
        logger.error(f"WebSocket error in room {room_code}: {e}")
        manager.disconnect(websocket)
    finally:
        db.close()
