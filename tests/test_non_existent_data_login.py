import requests
import allure
from conftest import LOGIN_URL


class TestCourierLoginExistentData:
    @allure.title("Тест логина с несуществующими данными")
    def test_non_existent_data_login(self):
        payload = {
            "login": "Belyrussky",
            "password": "coctail123"
        }

        response = requests.post(LOGIN_URL, data=payload)
        response_data = response.json()

        print(response.status_code)

        with allure.step("Проверяем, что приходит код 404 и нужное сообщение"):
            assert response.status_code == 404
            assert response_data == {'code': 404, 'message': 'Учетная запись не найдена'}