from fastapi import APIRouter, Response, Header, HTTPException
from datetime import datetime

from app.utils import verify_access_token

asdf = APIRouter(prefix='/test/cookie')


@asdf.get("/")
def root(Authorization: str = Header()):
    return {"User-Agent": Authorization}

@asdf.post('/')
def asg(Authorization: str = Header()):
    if Authorization is None:
        raise HTTPException(
            status_code=404,
            detail="Token not found",
        )
    token = Authorization.split(" ")[1]
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