import allure
import requests
import random
import string

from constants.urls import Urls


@allure.step('Регистрация пользователя и получение тестовых данных')
def register_new_user_and_return_test_data():
    email = f'{generate_random_string(7)}@example.com'
    name = f'{generate_random_string(8)}'
    password = f'{generate_random_string(12)}'

    payload = {
        "email": email,
        "name": name,
        "password": password
    }

    response = requests.post(Urls.CREATE_USER, data=payload)

    test_data = {
        "email": email,
        "name": name,
        "password": password,
        "json": response.json()
    }

    return test_data


@allure.step('Генерация случайной строки')
def generate_random_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step('Удаление пользователя')
def delete_user(access_token):
    headers = {'Authorization': access_token}
    requests.delete(Urls.USER, headers=headers)


@allure.step('Авторизация')
def login_user(email, password):
    payload = {
        "email": email,
        "password": password,
    }

    response = requests.post(Urls.LOGIN_API, data=payload)
    return response