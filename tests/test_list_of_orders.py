import allure
import requests

from data import EndPoints, StatusCodes


@allure.suite('Список заказов')
class TestListOfOrders:
    @allure.title('Проверка списка заказов')
    @allure.description('Тест успешного возврата списка заказов в тело ответа')
    def test_oder_list(self):
        response = requests.get(EndPoints.GET_ORDERS)
        assert response.status_code == StatusCodes.order_get_list["status_code"]
        assert "track" in response.text