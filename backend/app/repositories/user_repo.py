from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import func
from app.models.user import User, Profile, RefreshToken, UserRole


class UserRepository:
    @staticmethod
    def get_by_id(db: Session, user_id: int) -> Optional[User]:
        return db.query(User).filter(User.id == user_id).first()

    @staticmethod
    def get_by_username(db: Session, username: str) -> Optional[User]:
        return db.query(User).filter(func.lower(User.username) == username.lower()).first()

    @staticmethod
    def get_by_email(db: Session, email: str) -> Optional[User]:
        return db.query(User).filter(func.lower(User.email) == email.lower()).first()

    @staticmethod
    def create(db: Session, username: str, email: str, hashed_password: str, role: str = UserRole.USER.value, display_name: Optional[str] = None) -> User:
        user = User(
            username=username,
            email=email,
            hashed_password=hashed_password,
            role=role,
            is_active=True
        )
        db.add(user)
        db.flush()

        profile = Profile(
            user_id=user.id,
            display_name=display_name or username,
            avatar_url=f"https://api.dicebear.com/7.x/bottts/svg?seed={username}",
            level=1,
            current_xp=0,
            next_level_xp=100
        )
        db.add(profile)
        db.commit()
        db.refresh(user)
        return user

    @staticmethod
    def list_users(db: Session, skip: int = 0, limit: int = 50, search: Optional[str] = None) -> List[User]:
        query = db.query(User)
        if search:
            query = query.filter(
                (User.username.ilike(f"%{search}%")) | (User.email.ilike(f"%{search}%"))
            )
        return query.offset(skip).limit(limit).all()

    @staticmethod
    def update_profile(db: Session, user_id: int, display_name: Optional[str] = None, avatar_url: Optional[str] = None, bio: Optional[str] = None) -> Optional[Profile]:
        profile = db.query(Profile).filter(Profile.user_id == user_id).first()
        if not profile:
            return None
        if display_name is not None:
            profile.display_name = display_name
        if avatar_url is not None:
            profile.avatar_url = avatar_url
        if bio is not None:
            profile.bio = bio
        db.commit()
        db.refresh(profile)
        return profile
