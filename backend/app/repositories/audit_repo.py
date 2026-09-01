import json
from typing import List, Optional, Any
from sqlalchemy.orm import Session
from app.models.audit import AuditLog


class AuditRepository:
    @staticmethod
    def log(
        db: Session,
        action: str,
        resource_type: str,
        user_id: Optional[int] = None,
        resource_id: Optional[str] = None,
        details: Optional[Any] = None,
        ip_address: Optional[str] = None
    ) -> AuditLog:
        details_str = json.dumps(details) if details and not isinstance(details, str) else details
        log_entry = AuditLog(
            user_id=user_id,
            action=action,
            resource_type=resource_type,
            resource_id=str(resource_id) if resource_id is not None else None,
            details=details_str,
            ip_address=ip_address
        )
        db.add(log_entry)
        db.commit()
        db.refresh(log_entry)
        return log_entry

    @staticmethod
    def list_logs(db: Session, skip: int = 0, limit: int = 50) -> List[AuditLog]:
        return db.query(AuditLog).order_by(AuditLog.created_at.desc()).offset(skip).limit(limit).all()
