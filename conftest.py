import pytest
import helpers


@pytest.fixture
def unregistered_courier():
    login, password, first_name = helpers.generate_unregistered_courier()
    payload = {
        'login': login,
        'password': password,
        'firstName': first_name
    }

    yield payload


@pytest.fixture
def registered_courier():
    login, password, first_name = helpers.register_new_courier_and_return_login_password()
    payload = {
        'login': login,
        'password': password
    }

    yield payload
