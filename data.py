class EndPoints:
    TEST_URL = 'https://qa-scooter.praktikum-services.ru'
    LOGIN_COURIER = TEST_URL + '/api/v1/courier/login'  # post
    CREATE_COURIER = TEST_URL + '/api/v1/courier'  # post
    GET_ORDERS = TEST_URL + '/api/v1/orders'  # get
    ACCEPT_ORDER = TEST_URL + '/api/v1/orders/accept/:id'  # put
    CREATE_ORDERS = TEST_URL + '/api/v1/orders'  # post


class OrderData:
    data = {
        "firstName": "Тест",
        "lastName": "Тестовая",
        "address": "Тестовая, 3",
        "metroStation": 3,
        "phone": "+78003553535",
        "rentTime": 5,
        "deliveryDate": "2025-01-01",
        "comment": "Тестовая ракета",
    }


class StatusCodes:
    courier_created = {"status_code": 201,
                       "response_text": '{"ok":true}'}
    login_is_busy = {"status_code": 409,
                     "response_text": '{"code":409,"message":"Этот логин уже используется. Попробуйте другой."}'}
    empty_value = {"status_code": 400,
                   "response_text": '{"code":400,"message":"Недостаточно данных для создания учетной записи"}'}

    courier_login_successful = {"status_code": 200,
                                "response_text": ''}
    courier_login_one_param_empty = {"status_code": 400,
                                     "response_text": '{"code":400,"message":"Недостаточно данных для входа"}'}

    courier_login_incorrect_creds = {"status_code": 404,
                                     "response_text": '{"code":404,"message":"Учетная запись не найдена"}'}

    order_create = {"status_code": 201,
                    "response_text": '{"code":201,track: }'}
    order_get_list = {"status_code": 200,
                      "response_text": ''}