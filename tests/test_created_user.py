
import requests as r
import pytest
import allure
from urls import URLs
from helpers import GenerateUserData
from data import TestDataCreateUser

class TestCreateUser:

    @allure.title('Тест успешного сознания пользователя')
    def test_create_user_success(self, create_and_delete_user):

        access_token, response, payload = create_and_delete_user
        
        with allure.step('Проверка возвращения бэком статус кода 200'):
            assert response.status_code == 200 
        
        with allure.step('Проверка наличия в ответе всех ожидаемых ключей'):
            for key in TestDataCreateUser.RETURN_STATUS_CODE_200:
                assert key in response.text 

        

    @allure.title('Тест недопустимости создания пользователя с уже используемыми данными')
    def test_create_user_duplicate(self):

        with allure.step('генерация тестовых данных'):
            user_data = GenerateUserData.user_data
        
        with allure.step('вызов метод создания пользователя'):
            r.post(URLs.CREATE_USER_URL, data=user_data)     
        
        with allure.step('Попытка создания пользователя с теми же данными'):
            response = r.post(URLs.CREATE_USER_URL, data=user_data)
        
        with allure.step('Проверка статус кода и тела ответа'):
            assert response.status_code == 403 and response.json() == TestDataCreateUser.RETURN_EXISTING_USER

    
    @pytest.mark.parametrize('test_data', [GenerateUserData.user_data_without_email,
                                           GenerateUserData.user_data_without_password,
                                           GenerateUserData.user_data_without_name])
    
    @allure.title('Тест создания пользователя без заполнения обязательных полей')
    def test_create_user_without_required_fields(self, test_data):

        with allure.step('Вызов метода создания пользователя без передачи обязательных полей'):
            response = r.post(URLs.CREATE_USER_URL, data=test_data)
        
        with allure.step('Проверка статус кода и тела ответа'):
            assert response.status_code == 403 and response.json() == TestDataCreateUser.RETURN_WITHOUT_REQUIRED_FIELDS



