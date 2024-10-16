from sqlalchemy import Column, Integer, String, Boolean, DateTime, Float, ForeignKey
from app.db import Base
from sqlalchemy.sql import func


# Branch Model
class Roles(Base):
    __tablename__ = 'roles'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), index=True, nullable=False)

class Permissions(Base):
    __tablename__ = 'permissions'
    id = Column(Integer, primary_key=True)
    function = Column(String(191), index=True, nullable=False)
    role = Column(Integer, nullable=False)

