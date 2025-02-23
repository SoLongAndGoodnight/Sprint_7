import requests
from utils import generate_courier_data
import allure
from conftest import COURIER_URL


class TestCourierCreate:
    @allure.title("Тест на регистрацию. Проверка статус кода и текста в ответе.")
    def test_create_courier(self):
        payload = generate_courier_data()

        with allure.step("Отправляем запрос на регистрацию. Все поля заполнены"):
            response = requests.post(COURIER_URL, data=payload)
            response_data = response.json()

            print(response_data)
            print(response.status_code)

        with allure.step("Проверяем код ответа и текст в ответе"):
            assert response.status_code == 201
            assert response_data == {'ok': True}, f"Ошибка: ожидали {{'ok': True}}, но получили {response_data}"
