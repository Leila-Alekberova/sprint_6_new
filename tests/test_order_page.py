import allure
import pytest
from selenium import webdriver
from conftest import driver
from pages.OrderPage import *
from pages.MainPage import *
from pages.BasePage import *
from data import Urls

class TestOrder:
    @allure.title('Заполнение формы заказа самоката')
    @allure.description('Заполняем форму заказа самоката, используя две кнопки Заказать как точки входа')
    @pytest.mark.parametrize("name, second_name, address, phone, comment", [
        ("Лейла", "Алекберова", "Дмитровское шоссе", "79999999999", "Комментарий к заказу")])
    def test_order_page(self, driver, name, second_name, address, phone, comment):
        # Переход на страницу заказа
        with allure.step("Переход на страницу заказа"):
            driver.get(Urls.url_order)
        # Создание экземпляра OrderPage
        order_page = OrderPage(driver)
        # Заполнение формы заказа
        with allure.step("Заполнение формы заказа"):
            order_page.set_name_input(name)
            order_page.set_second_name_input(second_name)
            order_page.set_adress_input(address)
            order_page.metro_field()
            order_page.choose_station()
            order_page.set_phone_input(phone)
            order_page.press_next()
            order_page.pick_date_input()
            order_page.choose_rent_period()
            order_page.choose_color()
            order_page.add_comment(comment)
        # Подтверждение заказа
        with allure.step("Подтверждение заказа"):
            order_page.order_agreement()
            order_page.order_confirmation()

        # Проверки после подтверждения заказа
        with allure.step("Проверка успешного оформления заказа"):
            order_page.order_success()