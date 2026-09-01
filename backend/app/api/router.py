from fastapi import APIRouter
from app.api.v1 import auth, users, topics, tasks, games, multiplayer, scores, leaderboards, achievements, challenges, notifications, stats, admin, health

api_router = APIRouter()

api_router.include_router(health.router)
api_router.include_router(auth.router)
api_router.include_router(users.router)
api_router.include_router(topics.router)
api_router.include_router(tasks.router)
api_router.include_router(games.router)
api_router.include_router(multiplayer.router)
api_router.include_router(scores.router)
api_router.include_router(leaderboards.router)
api_router.include_router(achievements.router)
api_router.include_router(challenges.router)
api_router.include_router(notifications.router)
api_router.include_router(stats.router)
api_router.include_router(admin.router)
