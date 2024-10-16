from fastapi import APIRouter, Depends, Cookie, HTTPException, Response
from sqlalchemy.orm import Session

from app.db import get_db
from app.schemas import CreateRole, CreatePermission
from app.db.crud import create_roles_crud, create_permission_crud

settings = APIRouter(prefix='/api/private/roles', tags=['Settings'])

@settings.post('/roles')
async def create_roles(role: CreateRole, db: Session = Depends(get_db)):
    new = create_roles_crud(db, role)
    return new

@settings.post('/permission')
async def create_roles(permission: CreatePermission, db: Session = Depends(get_db)):
    new = create_permission_crud(db, permission)
    return new