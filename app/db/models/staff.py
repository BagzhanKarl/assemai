from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from app.db import Base
from sqlalchemy.sql import func

# Staff Model
class Staff(Base):
    __tablename__ = 'staff'

    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, nullable=False)
    company = Column(Integer, nullable=False)
    role = Column(Integer, nullable=False)
    branch = Column(Integer, nullable=False)
    role_text = Column(String(255), nullable=True)
    desc = Column(String(1000), nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

