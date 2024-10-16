from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class CustomersBase(BaseModel):
    first_name: str
    phone: str
    company: Optional[int] = None
    total_spent: Optional[float] = None
    average_spent: Optional[float] = None
    visit_count: Optional[int] = None
    branch: Optional[int] = None

class CustomersCreate(CustomersBase):
    pass

class CustomersUpdate(BaseModel):
    total_spent: Optional[float] = None
    average_spent: Optional[float] = None
    visit_count: Optional[int] = None

class CustomersRead(CustomersBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)