from fastapi import APIRouter, Depends, Header, HTTPException, Response, Body
from sqlalchemy.orm import Session

from app.db import get_db, get_info, get_all_by_branch, create_user_for_branch
from app.schemas import UserForStaff
from app.utils import verify_access_token, check_permission

staff = APIRouter(prefix='/api/public/company/staff', tags=['Staff'])

@staff.get('/get/{branch_id}')
async def get_all_staff_handler(branch_id: int,  db: Session = Depends(get_db)):
    staff = get_all_by_branch(db, branch_id)
    return {"status": True, "message": "Доступ разрешен", "data": staff}


@staff.post('/create/{branch_id}')
async def create_user_branch(branch_id: int, userCreate: UserForStaff, Authorization: str = Header(), db: Session = Depends(get_db)):
    if Authorization is None:
        raise HTTPException(status_code=404, detail='Нету токена')

    token = Authorization.split(" ")[1]

    try:
        # Проверка и верификация токена
        payload = verify_access_token(token)
        user = payload.get("user")

        # Проверка прав доступа
        boolcheck = check_permission('create_user_branch', user, db)
        if not boolcheck:
            raise HTTPException(status_code=403, detail="Access denied")

        # Создание нового пользователя
        newuser = create_user_for_branch(db, branch_id, userCreate, user)

        if not newuser:
            raise HTTPException(status_code=400, detail="Пользователь с таким номером уже существует")

    except HTTPException as e:
        # Повторное выбрасывание исключений HTTPException, чтобы не скрывать их
        raise e
    except Exception as e:
        # Вывод подробной информации об исключении для отладки
        print(f"Ошибка: {e}")
        raise HTTPException(
            status_code=405,
            detail=f"Невалидный или истекший токен. Детали: {str(e)}"
        )

    return {'status': True, 'data': 'Пользователь успешно создан'}
