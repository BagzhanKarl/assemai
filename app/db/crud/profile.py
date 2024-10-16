from sqlalchemy.orm import Session
from app.db.models import Branch, Staff, Company, Roles, Users

def get_all_info_user(db: Session, user: int):
    staff = db.query(Staff).filter(Staff.user == user).first()
    role = db.query(Roles).filter(Roles.id == staff.role).first()
    user = db.query(Users).filter(Users.id == user.id).first()
    company = db.query(Company).filter(Company.id == staff.company).first()
    branch = db.query(Branch).filter(Branch.company == company.id).all()

    return