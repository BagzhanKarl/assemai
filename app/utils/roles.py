from sqlalchemy.orm import Session
from app.db.models import Permissions, Staff  # Зависит от того, как у вас называются модели


def check_permission(function_name: str, user_id: int, db: Session) -> bool:
    # Получаем пользователя и его роль
    staff = db.query(Staff).filter(Staff.user == user_id).first()

    if not staff:
        return False

    permissions = db.query(Permissions).filter(
        Permissions.role == staff.role,
        Permissions.function == function_name
    ).first()

    if permissions:
        return True
    else:
        return False
