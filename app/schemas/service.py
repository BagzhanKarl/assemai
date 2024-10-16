from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class ServiceBase(BaseModel):
    company: int
    service_name: str
    public_name: str
    public_price: float
    cost_price: float
    duration: int
    public_description: Optional[str] = None
    category: Optional[str] = None

class ServiceCreate(ServiceBase):
    pass

class ServiceUpdate(BaseModel):
    public_price: Optional[float] = None
    cost_price: Optional[float] = None
    duration: Optional[int] = None
    public_description: Optional[str] = None

class ServiceRead(ServiceBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)