

import requests as r 
import allure
from urls import URLs
from helpers import GenerateUserData
from data import TestDataChangeUser

class TestChangeUserData:

    @allure.title('Тест изменения данных пользователя')
    def test_change_user_data_success(self, create_and_delete_user):

        access_token, response, payload = create_and_delete_user

        with allure.step('Вызов метода изменения данных пользователя'):
            response = r.patch(URLs.CHANGE_USER_URL, data=GenerateUserData.user_data,
                               headers={"Authorization": access_token})
        
        with allure.step('Проверка статус кода ответа'):
            assert response.status_code == 200
        
        with allure.step('Проверка наличия в ответе всех ожидаемых ключей'):
            for key in TestDataChangeUser.CHANGE_USER_SUCCESS:
                assert key in response.text

    
    @allure.title('Тест попытки изменения пользовательских данных без авторизации')
    def test_change_user_data_without_authorization(self):
        
        with allure.step('Вызов метода изменения данных пользователя без токена'):
            response = r.patch(URLs.CHANGE_USER_URL, data=GenerateUserData.user_data)
        
        with allure.step('Проверка статус кода и тела ответа'):
            assert response.status_code == 401 and response.json() == TestDataChangeUser.RETURN_STATUS_CODE_401
 
