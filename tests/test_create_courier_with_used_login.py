import requests
import allure
from conftest import COURIER_URL


class TestCourierCreateUsedLogin:
    @allure.title("Тест создания курьера с ранее использованными данными")
    def test_create_courier_with_used_login(self):
        payload = {
            "login": "Mike666",
            "password": "qwerty123",
            "firstName": "Herson"
        }
        with allure.step("Отправляем запрос на регистрацию с ранее использованным логином"):
            response = requests.post(COURIER_URL, data=payload)
            response_data = response.json()

        with allure.step("Проверяем что код ответа 409 и текст 'Этот логин уже используется. Попробуйте другой.'"):
            assert response_data == {'code': 409, 'message': 'Этот логин уже используется. Попробуйте другой.'}
