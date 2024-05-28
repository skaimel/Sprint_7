import allure
import requests
import random
import string
from data import EndPoints, OrderData
import json


# метод генерирует строку, состоящую только из букв нижнего регистра, в качестве параметра передаём длину строки
@allure.step("Генерация строки случайных букв")
def generate_random_string(length):
    random_string = ''.join(random.choices(string.ascii_lowercase, k=length))
    return random_string


@allure.step("Регистрация нового курьера и возврат логина и пароля")
def register_new_courier_and_return_login_password():

    # создаём список, чтобы метод мог его вернуть
    login_pass = []

    # генерируем логин, пароль и имя курьера
    login = generate_random_string(10)
    password = generate_random_string(10)
    first_name = generate_random_string(10)

    # собираем тело запроса
    payload = {
        "login": login,
        "password": password,
        "firstName": first_name
    }

    # отправляем запрос на регистрацию курьера и сохраняем ответ в переменную response
    response = requests.post(EndPoints.CREATE_COURIER, data=payload)

    # если регистрация прошла успешно (код ответа 201), добавляем в список логин и пароль курьера
    if response.status_code == 201:
        login_pass.append(login)
        login_pass.append(password)
        login_pass.append(first_name)

    # возвращаем список
    return login_pass


@allure.step("Генерация данных для незарегистрированного курьера")
def generate_unregistered_courier():
    courier_data = []
    while len(courier_data) != 3:
        courier_data.append(generate_random_string(8))
    return courier_data


@allure.step("Отправка запроса на создание курьера")
def send_create_courier_request(payload):
    response = requests.post(EndPoints.CREATE_COURIER, data=payload)
    return response


@allure.step("Отправка запроса на вход курьера")
def send_login_request(payload):
    response = requests.post(EndPoints.LOGIN_COURIER, data=payload)
    return response


class Order:
    @staticmethod
    @allure.step("Создание заказа")
    def create_order(color):
        headers = {"Content-type": "application/json"}
        data = OrderData.data
        data.update(color)
        json_data = json.dumps(data)
        response = requests.post(EndPoints.CREATE_ORDERS, headers=headers, data=json_data)
        return response
