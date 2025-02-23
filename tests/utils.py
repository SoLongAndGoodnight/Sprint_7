import random
import string


def generate_random_string(length=10):
    #Генерирует случайную строку из букв (по умолчанию 10 символов)
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))


def generate_courier_data():
    #Создает уникальные тестовые данные для курьера.
    return {
        "login": generate_random_string(),
        "password": generate_random_string(),
        "firstName": generate_random_string()
    }


