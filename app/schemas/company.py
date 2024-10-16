from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class CompanyBase(BaseModel):
    name: str
    platform: str
    country: int
    region: int
    address: str
    created_by: int
    branch: str
    industry: int
    whatsapp: Optional[str] = None

class CompanyCreate(BaseModel):
    name: str
    country: int = 1
    region: int = 0
    address: str
    created_by: int
    industry: int

class CompanyUpdate(BaseModel):
    address: Optional[str] = None
    whatsapp: Optional[str] = None

class CompanyRead(CompanyBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)