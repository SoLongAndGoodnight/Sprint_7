import requests
import allure
from conftest import LOGIN_URL


class TestCourierLogin:
    @allure.title("Тест на логин. Проверка статус кода и текста c id в ответе.")
    def test_courier_login_with_all_fields_is_ok(self):
        payload = {
            "login": "Mike666",
            "password": "qwerty123"
        }
        with allure.step("Отправляем POST запрос с заполненными логином и паролем"):
            response = requests.post(LOGIN_URL, data=payload)
            response_data = response.json()

            print(response.status_code)
            print(f"Response body: {response.json()}")

        with allure.step("Проверяем код ответа и id в ответе"):
            assert response.status_code == 200
            assert "id" in response_data, f"В ответе нет ключа 'id'. Ответ: {response_data}"