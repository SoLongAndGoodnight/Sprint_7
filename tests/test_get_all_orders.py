import requests
import allure
from conftest import ORDERS_URL


class TestGetAllOrders:
    @allure.title("Тест на получение списка заказов")
    def test_all_orders(self):
        response = requests.get(ORDERS_URL)
        response_data = response.json()

        with allure.step("Проверяем, что код ответа 200"):
            assert response.status_code == 200

        with allure.step("Проверяем, что в ответе есть ключ 'orders'"):
            assert "orders" in response_data

        with allure.step("Проверяем, что 'orders' является списком"):
            assert isinstance(response_data["orders"], list)