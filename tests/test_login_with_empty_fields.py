import requests
import pytest
import allure
from conftest import LOGIN_URL


class TestCourierLoginInvalidData:
    @allure.title("Тест на логин с пустыми полями")
    @pytest.mark.parametrize("payload", [
        {'password': 'qwerty123'},  # Без логина
        {'login': 'Mike666', 'password': ''}, # Без пароля
        {'login': '', 'password': ''}  # Пустые логин и пароль
    ])
    def test_courier_login_with_invalid_data(self,payload):
        headers = {"Content-Type": "application/json"}

        with allure.step("Отправляем запросы на логин с комбинациями: без логина; без пароля; пустые логин и пароль"):
            response = requests.post(LOGIN_URL, json=payload, headers=headers)
            response_data = response.json()

        print(f"Response code: {response.status_code}")
        print(f"Response body: {response_data}")

        with allure.step("Проверяем, что приходит код 400 и нужное сообщение"):
            assert response.status_code == 400, f"Ожидался код 400, но получили {response.status_code}"
            assert response_data == {'code': 400, 'message': 'Недостаточно данных для входа'}, \
            f"Ожидали сообщение {'code': 400, 'message': 'Недостаточно данных для входа'}, но получили {response_data}"
