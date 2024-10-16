import bcrypt

def hash_password(password: str) -> str:
    # Генерация соли и хеширование пароля
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    return hashed_password.decode('utf-8')

def verify_password(plain_password: str, hashed_password: str) -> bool:
    # Сравниваем хешированный пароль с введенным паролем
    return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
