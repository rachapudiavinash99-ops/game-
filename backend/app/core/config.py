import os
from typing import List, Union
from pydantic import AnyHttpUrl, field_validator
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    PROJECT_NAME: str = "Test Your Knowledge - Full-Stack Gaming Platform"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Topic-based challenge and competitive gaming platform"
    API_V1_STR: str = "/api/v1"
    ENVIRONMENT: str = "development"
    DEBUG: bool = True

    # Database
    DATABASE_URL: str = "sqlite:///./gameverse.db"

    # Redis (Optional PubSub / Caching)
    REDIS_URL: str = "redis://localhost:6379/0"

    # Security
    JWT_SECRET: str = "gameverse_super_secret_jwt_key_development_2026_x99a"
    JWT_ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24  # 24 hours
    REFRESH_TOKEN_EXPIRE_DAYS: int = 7

    # CORS
    CORS_ORIGINS: List[str] = [
        "http://localhost:5173",
        "http://localhost:3000",
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
        "*"
    ]

    # Game Config
    XP_BASE: int = 100
    XP_GROWTH_FACTOR: float = 1.5
    DEFAULT_QUESTION_TIMER: int = 20
    TIME_ATTACK_TOTAL_SECONDS: int = 60
    SURVIVAL_MAX_LIVES: int = 3

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=True,
        extra="allow"
    )


settings = Settings()
