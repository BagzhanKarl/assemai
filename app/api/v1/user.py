from fastapi import APIRouter, Depends, Cookie, HTTPException, Response, Header
from sqlalchemy.orm import Session

from app.db import get_db, Staff, Roles
from app.schemas import UsersCreate, UserLogin
from app.utils import create_access_token, verify_password, verify_access_token
from app.db.models import Users
from app.db.crud import create_user

user = APIRouter(prefix='/api/public/user', tags=['User '])

@user.post('/login')
async def login(user: UserLogin, response: Response, db: Session = Depends(get_db)):
    exist_user = db.query(Users).filter(Users.phone == user.phone).first()
    if not exist_user:
        raise HTTPException(status_code=403, detail='Пользователь с таким номером уже зарегистрирован')

    is_valid = verify_password(user.password, exist_user.password)
    if is_valid:
        data = {"user": exist_user.id}
        token = create_access_token(data)
    return {'status': True, 'data': 'Успешно', "token": token}

@user.post('/logout')
async def logout(response: Response):
    response.delete_cookie(key='token')
    return True

@user.post('/signup')
async def register(user: UsersCreate, response: Response, db: Session = Depends(get_db)):
    exict_user = db.query(Users).filter(Users.phone == user.phone).first()

    if exict_user:
        raise HTTPException(
            status_code=400,
            detail='Пользователь с таким номером уже зарегистрирован'
        )
    new_user = create_user(db, user)
    dict = {'user': new_user.id}
    token = create_access_token(dict)
    return {'status': True, 'data': 'Успешно!', "token": token}

@user.get("/protected-route")
def protected_route(token: str = Cookie(None)):
    print(token)
    if token is None:
        raise HTTPException(
            status_code=404,
            detail="Token not found",
        )

    try:
        payload = verify_access_token(token)
        user_id = payload.get("user")

        # Дополнительная логика для использования user_id
    except Exception as e:
        raise HTTPException(
            status_code=405,
            detail="Невалидный или истекший токен",
        )

    return {"message": "Доступ разрешен", "user": user_id}

@user.get('/my')
async def get_my_info(Authorization: str = Header(), db: Session = Depends(get_db)):
    if Authorization is None:
        raise HTTPException(status_code=404, detail='Нету токена')
    token = Authorization.split(" ")[1]
    try:
        payload = verify_access_token(token)
        user_id = payload.get("user")
        userdb = db.query(Users).filter(Users.id == user_id).first()
        staff = db.query(Staff).filter(Staff.user == userdb.id).first()
        role = db.query(Roles).filter(Roles.id == staff.role).first()
    except Exception as e:
        raise HTTPException(
            status_code=405,
            detail="Невалидный или истекший токен",
        )
    return {"status": True, "message": "Доступ разрешен", "first_name": userdb.first_name, "last_name": userdb.last_name, "role": role.name}