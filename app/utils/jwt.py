import jwt
from datetime import datetime, timedelta

# Секретный ключ для подписи токенов
SECRET_KEY = "bagzhankarl"
ALGORITHM = "HS256"  # Алгоритм для подписи токена
ACCESS_TOKEN_EXPIRE_MINUTES = 60  # Время жизни токена в минутах

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)

    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def verify_access_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload  # Возвращаем полезные данные из токена
    except jwt.ExpiredSignatureError:
        raise Exception("Токен истек")
    except jwt.JWTError:
        raise Exception("Невалидный токен")
