from typing import Any, Dict, Optional
from fastapi import HTTPException, status


class GameVerseException(HTTPException):
    def __init__(
        self,
        status_code: int,
        detail: str,
        error_code: str = "GENERIC_ERROR",
        extra: Optional[Dict[str, Any]] = None
    ):
        super().__init__(status_code=status_code, detail=detail)
        self.error_code = error_code
        self.extra = extra or {}


class AuthenticationError(GameVerseException):
    def __init__(self, detail: str = "Invalid credentials"):
        super().__init__(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=detail,
            error_code="AUTH_FAILED"
        )


class PermissionDeniedError(GameVerseException):
    def __init__(self, detail: str = "You do not have permission to perform this action"):
        super().__init__(
            status_code=status.HTTP_403_FORBIDDEN,
            detail=detail,
            error_code="PERMISSION_DENIED"
        )


class ResourceNotFoundError(GameVerseException):
    def __init__(self, resource: str, identifier: Any):
        super().__init__(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"{resource} with identifier '{identifier}' was not found.",
            error_code="RESOURCE_NOT_FOUND"
        )


class InvalidGameSessionError(GameVerseException):
    def __init__(self, detail: str = "Game session is invalid or already finished"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
            error_code="INVALID_GAME_SESSION"
        )


class RoomFullError(GameVerseException):
    def __init__(self, detail: str = "Multiplayer room has reached maximum player capacity"):
        super().__init__(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=detail,
            error_code="ROOM_FULL"
        )
