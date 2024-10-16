from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from app.db import Users, Roles
from app.db.models import Staff
from app.schemas import CompanyCreate
from app.utils import platform_id_generate

def create_staff(db: Session, user: int, company: int, branch: int, role: int):
    db_staff = Staff(
        company=company,
        branch=branch,
        user=user,
        role=role
    )
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    return db_staff

def get_all_by_branch(db: Session, branch: int):
    # Получаем всех сотрудников, привязанных к определенному филиалу
    staff_list = db.query(Staff).filter(Staff.branch == branch).all()

    # Создаем пустой список для хранения сотрудников с данными пользователей
    result = []

    # Проходим по каждому сотруднику и ищем пользователя по user_id
    for staff in staff_list:
        # Ищем пользователя в таблице users по user_id
        user = db.query(Users).filter(Users.id == staff.user).first()
        role = db.query(Roles).filter(Roles.id == staff.role).first()

        # Если пользователь найден, добавляем его к результату вместе с данными сотрудника
        if user:
            result.append({
                'staff': staff.id,
                'first_name': user.first_name,
                'last_name': user.last_name,
                'phone': user.phone,
                'status': user.is_active,
                'role': role.name,
            })

    return result