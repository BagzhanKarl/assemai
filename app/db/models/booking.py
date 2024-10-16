from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float
from sqlalchemy.sql import func

from app.db import Base

# Booking Model
class Booking(Base):
    __tablename__ = 'booking'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(255), nullable=False)
    phone = Column(String(20), nullable=False)
    branch_id = Column(Integer, nullable=False)
    master_id = Column(Integer, nullable=False)
    date = Column(String(20), nullable=False)
    time = Column(String(20), nullable=False)
    is_canceled = Column(Boolean, default=False)
    is_completed = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)
    duration = Column(Integer, nullable=True)

# BookingService Model
class BookingService(Base):
    __tablename__ = 'bookingservice'

    id = Column(Integer, primary_key=True, index=True)
    booking_id = Column(Integer, nullable=False)
    service_id = Column(Integer, nullable=False)
    created_at = Column(DateTime, server_default=func.now(), nullable=False)
    updated_at = Column(DateTime, server_default=func.now(), onupdate=func.now(), nullable=False)