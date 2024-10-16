from pydantic import BaseModel, Field, ConfigDict
from typing import Optional
from datetime import datetime

class CreateRole(BaseModel):
    name: str

class CreatePermission(BaseModel):
    function: str
    role: int