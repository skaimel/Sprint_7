import pytest
import requests
from data import EndPoints, StatusCodes
from conftest import registered_courier, unregistered_courier
import helpers
import allure


@allure.suite('Логин курьера в системе')
class TestLoginCourier:
    @allure.title('Проверка успешной авторизации курьера в системе')
    @allure.description('Тест успешной авторизации курьера в системе')
    def test_login_courier_successful(self, registered_courier):
        payload = registered_courier
        response = helpers.send_login_request(payload)
        assert response.status_code == StatusCodes.courier_login_successful["status_code"]
        assert "id" in response.text

    @allure.title('Проверка обязательных полей при авторизации')
    @allure.description('Тест авторизации при отсутствии обязательных полей')
    @pytest.mark.parametrize('missing_param', ['login', 'password'])
    def test_login_courier_missing_field(self, registered_courier, missing_param):
        payload = registered_courier.copy()
        payload[missing_param] = ''
        response = helpers.send_login_request(payload)
        assert response.status_code == StatusCodes.courier_login_one_param_empty["status_code"]
        assert response.text == StatusCodes.courier_login_one_param_empty["response_text"]

    @allure.title('Проверка некорректных данных при авторизации')
    @allure.description('Тест авторизации с некорректными данными')
    @pytest.mark.parametrize('invalid_param', ['login', 'password'])
    def test_login_courier_with_invalid_data(self, registered_courier, invalid_param):
        payload = registered_courier.copy()
        payload[invalid_param] += '1'
        response = helpers.send_login_request(payload)
        assert response.status_code == StatusCodes.courier_login_incorrect_creds["status_code"]
        assert response.text == StatusCodes.courier_login_incorrect_creds["response_text"]

    @allure.title('Проверка авторизации незарегистрированного пользователя')
    @allure.description('Тест авторизации для незарегистрированного пользователя')
    def test_login_unregistered_courier(self):
        login, password, first_name = helpers.generate_unregistered_courier()
        payload = {
            'login': login,
            'password': password
        }
        response = helpers.send_login_request(payload)
        assert response.status_code == StatusCodes.courier_login_incorrect_creds["status_code"]
        assert response.text == StatusCodes.courier_login_incorrect_creds["response_text"]