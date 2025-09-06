
import requests as r
import allure
from urls import URLs
from data import TestDataOrder

class TestGetOrders:

    @allure.title('Тест получения списка заказов авторизированным пользователем')
    def test_get_order_with_authorization(self, create_and_delete_user):

        access_token, response, payload = create_and_delete_user

        with allure.step('Вызов метода создания заказа'):
            r.post(URLs.ORDERS_URL, data=TestDataOrder.INGREDIENTS,
                              headers={"Authorization": access_token})
        
        with allure.step('Вызов метода получения списка заказов пользователя'):
            response = r.get(URLs.ORDERS_URL,
                             headers={"Authorization": access_token})
        
        with allure.step('Проверка статус кода ответа'):
            assert response.status_code == 200
        
        with allure.step('Проверка наличия в ответе всех ожидаемых ключей'):
            for key in TestDataOrder.RETURN_USER_ORDERS:
                assert key in response.text


    
    @allure.title('Тест попытка получения списка заказов без авторизации')
    def test_get_order_without_authorization(self):
        
        with allure.step('Вызов метода получения списка заказов'):
            response = r.get(URLs.ORDERS_URL)
        
        with allure.step('Проверка статус кода и тела ответа'):
            assert response.status_code == 401 and response.json() == TestDataOrder.RETURN_STATUS_CODE_401
            