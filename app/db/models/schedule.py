from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from app.db import Base
from sqlalchemy.sql import func

# Schedule Model
class Schedule(Base):
    __tablename__ = 'schedule'

    id = Column(Integer, primary_key=True, index=True)
    user = Column(Integer, nullable=False)
    date = Column(String(20), nullable=False)
    start = Column(String(20), nullable=False)
    end = Column(String(20), nullable=False)
    start_break = Column(String(20), nullable=True)
    end_break = Column(String(20), nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
