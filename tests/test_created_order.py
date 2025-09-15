
import pytest
import requests as r
import allure
from urls import URLs
from data import TestDataOrder


class TestCreateOrder:
    
    

    @allure.title('Тест создания заказа авторизированным пользователем с ингредиентами')
    def test_create_order_with_ingredients_and_authorization(self, create_and_delete_user):

        access_token, response, payload = create_and_delete_user
        

        with allure.step('Вызов метода создания заказа'):
            response = r.post(URLs.ORDERS_URL, data=TestDataOrder.INGREDIENTS,
                              headers={"Authorization": access_token})
        
        with allure.step('Проверка стаутс кода ответа'):
            assert response.status_code == 200 
        
        with allure.step('Проверка наличия в ответе всех ожидаемых ключей'):
            for key in TestDataOrder.STATUS_CODE_200:
                assert key in response.text

        
         

    @allure.title('Тест создания заказа неавторизированным пользователем с ингредиентами')
    def test_create_order_with_ingredients_and_without_authorization(self):

        with allure.step('Вызов метода создания заказа'):
            response = r.post(URLs.ORDERS_URL, data=TestDataOrder.INGREDIENTS)
        
        with allure.step('Проверка статус кода ответа'):
            assert response.status_code == 200 
        
        with allure.step('Проверка наличия в ответе всех ожидаемых ключей'):
            for key in TestDataOrder.STATUS_CODE_200:
                assert key in response.text


    @allure.title('Тест попытки создания заказа авторизированным пользователем без инредиентов')
    def test_create_order_without_ingredients_and_with_auhorization(self, create_and_delete_user):
        
        access_token, response, payload = create_and_delete_user
        
        with allure.step('Вызов метода создания заказа'):
            response = r.post(URLs.ORDERS_URL, data=TestDataOrder.INGREDIENTS_EMPTY_LIST,
                          headers={"Authorization": access_token})
        
        with allure.step('Проверка статус кода и тела ответа'):
            assert response.status_code == 400 and response.json() == TestDataOrder.RETURN_STATUS_CODE_400


    
    
    @allure.title('Тест создания заказа неавторизированным пользователем без ингредиентов')
    def test_create_order_without_ingredients_and_authorization(self):

        with allure.step('Вызов метода создания заказа'):
            response = r.post(URLs.ORDERS_URL, data=TestDataOrder.INGREDIENTS_EMPTY_LIST)
        
        with allure.step('Проверка статус кода и тела ответа'):
            assert response.status_code == 400 and response.json() == TestDataOrder.RETURN_STATUS_CODE_400

    
    
    @allure.title('Тест попытки создания заказа с невалидным хэшем')
    def test_create_order_with_invalid_hash(self, create_and_delete_user):

        access_token, response, payload = create_and_delete_user
        
        with allure.step('Вызов метода создания заказа'):
            response = r.post(URLs.ORDERS_URL, data=TestDataOrder.INGREDIENTS_INVALID_HASH,
                              headers={"Authorization": access_token})
        
        with allure.step('Проверка статус кода ответа'):
            assert response.status_code == 400 and response.json() == TestDataOrder.RETURN_MESSAGE_INVALID_HASH

       
