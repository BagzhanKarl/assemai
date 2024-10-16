from sqlalchemy.orm import Session
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException
from app.db.models import Service

def create_demo_service(db: Session, company: int):
    db_service = Service(
        company=company,
        public_name='Стрижка (Демо)',
        public_price=5000,
        public_description='Демо демо демо',
        service_name='Стрижка (Демо)',
        duration=60,
        cost_price=2000,
        category=0
    )
    db.add(db_service)
    db.commit()
    db_service = Service(
        company=company,
        public_name='Стрижка + укладка (Демо)',
        public_price=8000,
        public_description='Демо демо демо',
        service_name='Стрижка + укладка (Демо)',
        duration=60,
        cost_price=2000,
        category=0
    )
    db.add(db_service)
    db.commit()
    return "True"