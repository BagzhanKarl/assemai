from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app.db.models import Company
from app.schemas import CompanyCreate
from app.utils import platform_id_generate

def create_company(db: Session, company: CompanyCreate, user: int):
    db_company = Company(
        name=company.name,
        country=company.country,
        region=company.region,
        address=company.address,
        created_by=user,
        industry=company.industry,
        platform=platform_id_generate(),
        whatsapp='None',
        branch=1,
    )
    db.add(db_company)
    db.commit()
    db.refresh(db_company)
    return db_company
