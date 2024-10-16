from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from app.db import Base
from sqlalchemy.sql import func


# Branch Model
class Branch(Base):
    __tablename__ = 'branch'

    id = Column(Integer, primary_key=True, index=True)
    company = Column(Integer, nullable=False)
    country = Column(Integer, nullable=False)
    region = Column(Integer, nullable=False)
    address = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
