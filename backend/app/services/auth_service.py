from datetime import datetime, timezone
from typing import Optional
from sqlalchemy.orm import Session
from app.core.security import verify_password, get_password_hash, create_access_token, create_refresh_token, decode_token
from app.core.exceptions import AuthenticationError, GameVerseException
from app.repositories.user_repo import UserRepository
from app.models.user import User, RefreshToken, UserRole


class AuthService:
    @staticmethod
    def register_user(db: Session, username: str, email: str, password: str, display_name: Optional[str] = None, role: str = UserRole.USER.value) -> User:
        if UserRepository.get_by_username(db, username):
            raise GameVerseException(status_code=400, detail="Username is already registered", error_code="USERNAME_TAKEN")
        if UserRepository.get_by_email(db, email):
            raise GameVerseException(status_code=400, detail="Email is already registered", error_code="EMAIL_TAKEN")

        hashed_pwd = get_password_hash(password)
        user = UserRepository.create(db, username=username, email=email, hashed_password=hashed_pwd, role=role, display_name=display_name)
        return user

    @staticmethod
    def authenticate_user(db: Session, username: str, password: str) -> dict:
        user = UserRepository.get_by_username(db, username)
        if not user:
            # Fallback search by email
            user = UserRepository.get_by_email(db, username)
            
        if not user or not verify_password(password, user.hashed_password):
            raise AuthenticationError("Invalid username or password")

        if not user.is_active:
            raise AuthenticationError("Account has been disabled by administrator")

        access_token = create_access_token(subject=user.id, role=user.role)
        refresh_token = create_refresh_token(subject=user.id)

        # Store refresh token record
        rt = RefreshToken(
            user_id=user.id,
            token=refresh_token,
            expires_at=datetime.now(timezone.utc)
        )
        db.add(rt)
        db.commit()

        return {
            "access_token": access_token,
            "refresh_token": refresh_token,
            "token_type": "bearer",
            "user_id": user.id,
            "username": user.username,
            "role": user.role
        }

    @staticmethod
    def refresh_access_token(db: Session, refresh_token_str: str) -> dict:
        try:
            payload = decode_token(refresh_token_str)
            if payload.get("type") != "refresh":
                raise AuthenticationError("Token is not a refresh token")
            user_id = int(payload.get("sub"))
        except Exception:
            raise AuthenticationError("Invalid or expired refresh token")

        user = UserRepository.get_by_id(db, user_id)
        if not user or not user.is_active:
            raise AuthenticationError("User not found or inactive")

        new_access_token = create_access_token(subject=user.id, role=user.role)
        return {
            "access_token": new_access_token,
            "refresh_token": refresh_token_str,
            "token_type": "bearer",
            "user_id": user.id,
            "username": user.username,
            "role": user.role
        }
