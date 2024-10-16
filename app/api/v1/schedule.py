from fastapi import APIRouter, Depends, Header, HTTPException, Response, Body
from sqlalchemy.orm import Session

from app.db import get_db, get_info, get_all_by_branch, create_user_for_branch
from app.schemas import UserForStaff, ScheduleBase
from app.utils import verify_access_token, check_permission

schedule = APIRouter(prefix='/api/public/company/staff/schedule', tags=['Schedule'])

@schedule.post('/create')
async def create_schedule(request: ScheduleBase, db: Session = Depends(get_db)):
    pass