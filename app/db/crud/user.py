from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException

from app.db import Staff
from app.db.models import Users
from app.schemas import UsersCreate, UsersUpdate, UserForStaff
from app.utils import hash_password

# Create User
def create_user(db: Session, user: UsersCreate):
    db_user = Users(
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone,
        password=hash_password(user.password),
        is_active=True,
        is_verify=False
    )
    try:
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
        return db_user
    except IntegrityError:
        db.rollback()
        raise HTTPException(status_code=400, detail="User with this phone already exists.")

def create_user_for_branch(db: Session, branch: int, user: UserForStaff, authuser: int):
    exict_user = db.query(Users).filter(Users.phone == user.phone).first()
    if exict_user:
        print("Пользователь уже есть у нас")
        return False

    staff = db.query(Staff).filter(Staff.user == authuser).first()
    print("Компания")

    db_user = Users(
        first_name=user.first_name,
        last_name=user.last_name,
        phone=user.phone,
        password=hash_password(user.password),
        is_active=True,
        is_verify=False
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    print("Пользователь создано")

    db_staff = Staff(
        user=db_user.id,
        company=staff.company,
        branch=branch,
        role=user.role
    )
    db.add(db_staff)
    db.commit()
    db.refresh(db_staff)
    print("Стафф создано")

    return True

# Get User by ID
def get_user(db: Session, user_id: int):
    pass

# Get User by company ID
def get_all_users_by_company(db: Session, company: int):
    pass

# Get User by branch ID
def get_all_users_by_branch(db: Session, branch: int):
    pass

# Update User
def update_user(db: Session, user_id: int, user_update: UsersUpdate):
    pass

# Delete User
def delete_user(db: Session, user_id: int):
    pass