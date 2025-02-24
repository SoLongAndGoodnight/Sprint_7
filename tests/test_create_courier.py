import requests
from utils import generate_courier_data
import allure
from conftest import COURIER_URL
from conftest import LOGIN_URL
from conftest import COURIER_DELETE


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

        login_payload = {
            "login": payload["login"],
            "password": payload["password"]
        }
        with allure.step("Логинимся и получаем ID курьера"):
            login_response = requests.post(f"{COURIER_URL}/login", json=login_payload)
            login_data = login_response.json()

            assert login_response.status_code == 200, f"Ошибка входа: {login_data}"
            assert "id" in login_data, f"В ответе отсутствует 'id': {login_data}"
            courier_id = login_data["id"]

        # Удаляем курьера
        with allure.step("Удаляем курьера"):
            delete_response = requests.delete(f"{COURIER_URL}/{courier_id}")
            delete_data = delete_response.json()

            assert delete_response.status_code == 200, f"Ошибка удаления: {delete_data}"
            assert delete_data == {'ok': True}, f"Ошибка удаления: {delete_data}"

            print(f"Курьер {courier_id} удален")