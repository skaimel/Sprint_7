import pytest
import requests
from data import EndPoints, StatusCodes
from conftest import unregistered_courier
import helpers
import allure


def send_create_courier_request(payload):
    response = requests.post(EndPoints.CREATE_COURIER, data=payload)
    return response


@allure.suite('Создание курьера')
class TestCreateCourier:

    @allure.title('Создание нового курьера')
    @allure.description('Создаем нового курьера, проверяем статус код и текст ответа')
    def test_create_courier(self, unregistered_courier):
        payload = unregistered_courier
        response = send_create_courier_request(payload)
        assert response.status_code == StatusCodes.courier_created["status_code"]
        assert response.text == StatusCodes.courier_created["response_text"]

    @allure.title('Проверка ошибки при создании одинаковых курьеров')
    @allure.description('Тест ошибки создания одинаковых курьеров')
    def test_create_same_courier(self, unregistered_courier):
        payload = unregistered_courier
        send_create_courier_request(payload)
        response_1 = send_create_courier_request(payload)
        assert response_1.status_code == StatusCodes.login_is_busy["status_code"]
        assert response_1.text == StatusCodes.login_is_busy["response_text"]

    @allure.title('Проверка обязательных полей при создании курьера')
    @allure.description('Тест при отсутствии обязательных полей при создании курьера')
    @pytest.mark.parametrize('missing_field', ['login', 'password'])
    def test_create_courier_with_missing_field(self, missing_field):
        login, password, first_name = helpers.generate_unregistered_courier()
        payload = {
            'login': login,
            'password': password,
            'firstName': first_name
        }
        del payload[missing_field]
        response = send_create_courier_request(payload)
        assert response.status_code == StatusCodes.empty_value["status_code"]
        assert response.text == StatusCodes.empty_value["response_text"]