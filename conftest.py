
import pytest
import allure
import requests as r
from urls import URLs
from helpers import GenerateUserData


@pytest.fixture(scope="function")
def create_and_delete_user():

    payload = GenerateUserData.generate_test_data()
    
    with allure.step('Создание пользователя'):
        response = r.post(URLs.CREATE_USER_URL, json=payload)
        access_token = response.json()['accessToken']
    
    yield access_token, response, payload

    with allure.step('Удаление созданного для теста пользователя'):
        r.delete(URLs.CHANGE_USER_URL, headers={'Authorization': access_token})