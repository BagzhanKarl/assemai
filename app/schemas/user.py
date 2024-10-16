from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime


class UserLogin(BaseModel):
    phone: str
    password: str

class UsersBase(BaseModel):
    first_name: str
    last_name: str
    phone: str

class UsersCreate(UsersBase):
    password: str

class UserForStaff(UsersBase):
    password: str
    role: int
class UsersUpdate(BaseModel):
    first_name: Optional[str] = None
    last_name: Optional[str] = None
    is_active: Optional[bool] = None
    is_verify: Optional[bool] = None

class UsersRead(UsersBase):
    id: int
    created_at: datetime
    updated_at: datetime

    model_config = ConfigDict(from_attributes=True)

