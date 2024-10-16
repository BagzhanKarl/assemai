from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

# Booking Schemas
class BookingBase(BaseModel):
    name: str
    phone: str
    branch_id: int
    master_id: int
    date: str
    time: str
    is_canceled: Optional[bool] = False
    is_completed: Optional[bool] = False
    is_active: Optional[bool] = True
    duration: Optional[int] = None

class BookingCreate(BookingBase):
    pass

class BookingUpdate(BaseModel):
    is_canceled: Optional[bool] = None
    is_completed: Optional[bool] = None
    duration: Optional[int] = None

class BookingRead(BookingBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

# BookingService Schemas
class BookingServiceBase(BaseModel):
    booking_id: int
    service_id: int

class BookingServiceCreate(BookingServiceBase):
    pass

class BookingServiceRead(BookingServiceBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)