from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class ScheduleBase(BaseModel):
    user: int
    date: str
    start: str
    end: str
    start_break: Optional[str] = None
    end_break: Optional[str] = None

class ScheduleCreate(ScheduleBase):
    pass

class ScheduleUpdate(BaseModel):
    start: Optional[str] = None
    end: Optional[str] = None
    start_break: Optional[str] = None
    end_break: Optional[str] = None

class ScheduleRead(ScheduleBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)