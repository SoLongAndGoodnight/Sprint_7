import allure
import requests
import pytest
from conftest import ORDERS_URL


class TestOrder:
    @allure.title("Тест заказа самоката с разным набором данных в color")
    @pytest.mark.parametrize("color", [
        ["BLACK"],
        ["GREY"],
        ["BLACK", "GREY"],
        []
    ])
    def test_order(self, color):
        payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2025-04-06",
        "comment": "Saske, come back to Konoha",
        "color": color
    }
        response = requests.post(ORDERS_URL, json=payload)
        response_data = response.json()

        print(f"Response code: {response.status_code}")
        print(f"Response body: {response_data}")

        with allure.step("Проверяем, что возвращается код 201 и track в ответе"):
            assert response.status_code == 201
            assert "track" in response_data