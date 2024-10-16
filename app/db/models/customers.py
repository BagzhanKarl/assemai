from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from app.db import Base
from sqlalchemy.sql import func

# Customers Model
class Customers(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    company = Column(Integer, nullable=True)
    total_spent = Column(Float, nullable=True)
    average_spent = Column(Float, nullable=True)
    visit_count = Column(Integer, nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    branch = Column(Integer, nullable=True)
