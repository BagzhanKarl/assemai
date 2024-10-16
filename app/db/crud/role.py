from sqlalchemy.orm import Session
from app.db.models import Roles, Permissions
from app.schemas import CreateRole, CreatePermission

def create_roles_crud(db: Session, role: CreateRole):
    db_roles = Roles(
        name=role.name
    )
    db.add(db_roles)
    db.commit()
    db.refresh(db_roles)
    return db_roles

def create_permission_crud(db: Session, permission: CreatePermission):
    new_permission = Permissions(
        function=permission.function,
        role=permission.role

    )
    db.add(new_permission)
    db.commit()
    db.refresh(new_permission)
    return new_permission