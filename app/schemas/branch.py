from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class BranchBase(BaseModel):
    platform: str
    company: int
    country: int
    region: int
    address: str
    phone: str

class BranchCreate(BaseModel):
    address: str
    phone: str

class BranchUpdate(BaseModel):
    address: Optional[str] = None
    phone: Optional[str] = None

class BranchRead(BranchBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)