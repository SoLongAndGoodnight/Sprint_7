import requests
import allure
from conftest import COURIER_URL


class TestCourierCreateEmptyLogin:
    @allure.title("Тест на регистрацию с пустым логином. Проверка статус кода и текста в ответе.")
    def test_create_courier_with_empty_login(self):
        payload = {
            "login": "",
            "password": "qwerty123",
            "firstName": "Herson"
        }
        with allure.step("Отправляем запрос на регистрацию с пустым логином"):
            response = requests.post(COURIER_URL, data=payload)
            response_data = response.json()


        with allure.step("Проверяем что статус код 400 и текст в ответе"):
            assert response_data == {'code': 400, "message": "Недостаточно данных для создания учетной записи"}