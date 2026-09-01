from typing import Optional
from fastapi import Depends, Header
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.core.database import get_db
from app.core.security import decode_token
from app.core.exceptions import AuthenticationError, PermissionDeniedError
from app.repositories.user_repo import UserRepository
from app.models.user import User, UserRole

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/api/v1/auth/login", auto_error=False)


def get_current_user(
    db: Session = Depends(get_db),
    token: Optional[str] = Depends(oauth2_scheme)
) -> User:
    if not token:
        raise AuthenticationError("Authorization token required")
    try:
        payload = decode_token(token)
        user_id = int(payload.get("sub"))
    except Exception:
        raise AuthenticationError("Invalid or expired authorization token")

    user = UserRepository.get_by_id(db, user_id)
    if not user or not user.is_active:
        raise AuthenticationError("User not found or disabled")
    return user


def get_optional_user(
    db: Session = Depends(get_db),
    token: Optional[str] = Depends(oauth2_scheme)
) -> Optional[User]:
    if not token:
        return None
    try:
        payload = decode_token(token)
        user_id = int(payload.get("sub"))
        user = UserRepository.get_by_id(db, user_id)
        if user and user.is_active:
            return user
    except Exception:
        pass
    return None


def get_current_admin(
    current_user: User = Depends(get_current_user)
) -> User:
    if current_user.role != UserRole.ADMIN.value:
        raise PermissionDeniedError("Administrator access required")
    return current_user
