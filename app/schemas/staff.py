from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class StaffBase(BaseModel):
    user: int
    company: int
    role: int
    branch: int
    role_text: Optional[str] = None
    desc: Optional[str] = None

class StaffCreate(StaffBase):
    pass

class StaffUpdate(BaseModel):
    role: Optional[int] = None
    role_text: Optional[str] = None
    desc: Optional[str] = None

class StaffRead(StaffBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)
