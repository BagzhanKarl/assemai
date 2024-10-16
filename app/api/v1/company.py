from fastapi import APIRouter, Depends, Header, HTTPException, Response, Body
from sqlalchemy.orm import Session

from app.db import get_db, get_info
from app.schemas import CompanyCreate, BranchCreate
from app.utils import verify_access_token, check_permission
from app.db.crud import create_company, create_branch, create_staff, create_demo_service, delete_branch_by_ui, get_all_branch, create_branch_by_ui

company = APIRouter(prefix='/api/public/company', tags=['Company'])

@company.post('/create')
async def create_new_company(schemcompany: CompanyCreate, Authorization: str = Header(), db: Session = Depends(get_db)):
    if Authorization is None:
        raise HTTPException(
            status_code=404,
            detail="Token not found",
        )
    token = Authorization.split(" ")[1]
    try:
        payload = verify_access_token(token)
        user = payload.get("user")
        new_company = create_company(db, schemcompany, user)
        new_branch = create_branch(db, new_company)
        new_staff = create_staff(db, user, new_company.id, 0, 1)
        service = create_demo_service(db, new_company.id)
    except Exception as e:
        raise HTTPException(
            status_code=405,
            detail="Невалидный или истекший токен",
        )
    return {"status": True, "message": "Доступ разрешен", "comp": new_company.id, "branch": new_branch.id}

@company.get('/branches')
async def get_all_branch_handler(Authorization: str = Header(), db: Session = Depends(get_db)):
    if Authorization is None:
        raise HTTPException(status_code=404, detail='Нету токена')

    token = Authorization.split(" ")[1]

    try:
        payload = verify_access_token(token)
        user = payload.get("user")
        branches = get_all_branch(db, user)
    except Exception as e:
        raise HTTPException(
            status_code=405,
            detail="Невалидный или истекший токен",
        )
    return {"status": True, "message": "Доступ разрешен", "data": branches}

@company.post('/branches/create')
async def create_new_branch_by_user(branch: BranchCreate, Authorization: str = Header(), db: Session = Depends(get_db)):
    if Authorization is None:
        raise HTTPException(
            status_code=404,
            detail="Token not found",
        )
    token = Authorization.split(" ")[1]
    try:
        payload = verify_access_token(token)
        user = payload.get("user")
        new_branch = create_branch_by_ui(db, user, branch)
    except Exception as e:
        raise HTTPException(
            status_code=405,
            detail="Невалидный или истекший токен",
        )
    return {"status": True, "message": "Доступ разрешен", "new_branch": new_branch}

@company.delete('/branches/delete')
async def delete_branch_by_id(branch: dict = Body(...), Authorization: str = Header(), db: Session = Depends(get_db)):
    if Authorization is None:
        raise HTTPException(
            status_code=404,
            detail="Token not found",
        )
    token = Authorization.split(" ")[1]
    try:
        payload = verify_access_token(token)
        user = payload.get("user")
        branch_id = branch.get("branch")  # Получаем ID ветки из тела запроса
        boolChek = check_permission("delete_branch_by_id", user, db)
        if not boolChek:
            raise HTTPException(status_code=403, detail="Access denied")
        branch_del = delete_branch_by_ui(db, branch_id)
    except Exception as e:
        raise HTTPException(
            status_code=4050,
            detail="Невалидный или истекший токен",
        )
    return {"status": True, "message": "Доступ разрешен", "data": "Успешно удалено"}

@company.get('/branches/{branch_id}')
async def get_branch_data_by_id(branch_id: int, db: Session = Depends(get_db)):
    response = get_info(db, branch_id)

    return {'status': True, "data": response}