from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy.sql import func
from app.db import Base

# Company Model
class Company(Base):
    __tablename__ = 'company'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    platform = Column(String(50), nullable=False)
    whatsapp = Column(String(20), nullable=True)
    country = Column(Integer, nullable=False)
    region = Column(Integer, nullable=False)
    address = Column(String(255), nullable=False)
    created_by = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    branch = Column(Integer, nullable=False)
    industry = Column(Integer, nullable=False)
