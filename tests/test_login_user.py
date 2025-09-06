
import requests as r 
import allure
from urls import URLs
from helpers import GenerateUserData
from data import TestDataLoginUser


class TestLoginUser:

    @allure.title('Тест успешной авторизации пользователя')
    def test_login_user_success(self, create_and_delete_user):

        access_token, response, payload = create_and_delete_user
        
        with allure.step('Вызов метода авторизации пользователя с валидными данными'):
            response = r.post(URLs.LOGIN_USER_URL, data=payload)  
        
        with allure.step('Проверка статус кода ответа'):
            assert response.status_code == 200
        
        with allure.step('Проверка наличия в ответе всех ожидаемых ключей'):
            for key in TestDataLoginUser.RETURN_STATUS_CODE_200:
                assert key in response.text

        


    @allure.title('Тест попытка авторизации несуществующего пользователя')
    def test_login_unknow_user(self):
        
        with allure.step('Вызов метода авторизации пользователя с неизвестными даннымми'):
            response = r.post(URLs.LOGIN_USER_URL, data=GenerateUserData.generate_test_data())
        
        with allure.step('Проверка статус кода и тела ответа'):
            assert response.status_code == 401 and response.json() == TestDataLoginUser.RETURN_STATUS_CODE_401
