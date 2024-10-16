from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from app.db import Base
from sqlalchemy.sql import func

# Service Model
class Service(Base):
    __tablename__ = 'service'

    id = Column(Integer, primary_key=True, index=True)
    company = Column(Integer, nullable=False)
    service_name = Column(String(255), nullable=False)
    public_name = Column(String(255), nullable=False)
    public_price = Column(Float, nullable=False)
    cost_price = Column(Float, nullable=True)
    duration = Column(Integer, nullable=False)
    public_description = Column(String(1000), nullable=True)
    category = Column(String(50), nullable=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)

