import random
import string


def platform_id_generate():
    part_length = 3
    characters = string.ascii_letters + string.digits  # Строка теперь включает буквы и цифры
    parts = [''.join(random.choices(characters, k=part_length)) for _ in range(3)]
    result = '-'.join(parts)
    return result
