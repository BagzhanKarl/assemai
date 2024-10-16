from sqlalchemy.orm import Session

from app.db import Staff, Company
from app.db.models import Branch
from app.schemas import CompanyBase, BranchCreate

def create_branch(db: Session, company: CompanyBase):
    db_branch = Branch(
        company=company.id,
        country=company.country,
        region=company.region,
        address=company.address,
        phone='Пока нет',
    )
    db.add(db_branch)
    db.commit()
    db.refresh(db_branch)
    return db_branch

def get_all_branch(db: Session, user: int):
    staff = db.query(Staff).filter(Staff.user == user).first()
    company = db.query(Company).filter(Company.id == staff.company).first()
    branch = db.query(Branch).filter(Branch.company == staff.company).all()
    return {"company": company.name, "branch": branch}

def create_branch_by_ui(db: Session, user: int, branch: BranchCreate):
    staff = db.query(Staff).filter(Staff.user == user).first()
    company = db.query(Company).filter(Company.id == staff.company).first()

    new_branch = Branch(
        company=company.id,
        country=company.country,
        region=company.region,
        address=branch.address,
        phone=branch.phone,
    )
    db.add(new_branch)
    db.commit()
    db.refresh(new_branch)
    return new_branch

def delete_branch_by_ui(db: Session, id: int):
    branch = db.query(Branch).filter(Branch.id == id).first()

    if branch is None:
        return False

    try:
        db.delete(branch)
        db.commit()
        return True
    except Exception as e:
        db.rollback()
        raise e

def get_info(db: Session, id: int):
    branch = db.query(Branch).filter(Branch.id == id).first()
    company = db.query(Company).filter(Company.id == branch.company).first()

    data = {'company': company.name, "branch": branch}
    return data
