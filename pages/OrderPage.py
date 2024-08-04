import allure
from locators.order_page_locator import *
from pages.BasePage import *
from pages.MainPage import *
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import datetime


class OrderPage(BasePage):

    @allure.step('Заполняем поле Имя')
    def set_name_input(self, name='Лейла'):
        name_input = self.find_element_with_wait(OrderPageLocators.INPUT_FIRST_NAME)
        name_input.send_keys(name)

    @allure.step('Заполняем поле Фамилия')
    def set_second_name_input(self, second_name='Алекберова'):
        second_name_input = self.find_element_with_wait(OrderPageLocators.INPUT_SECOND_NAME)
        second_name_input.send_keys(second_name)

    @allure.step('Заполняем поле Адрес')
    def set_adress_input(self, adress='Дмитровское шоссе'):
        adress_input = self.find_element_with_wait(OrderPageLocators.INPUT_ADDRESS)
        adress_input.send_keys(adress)

    @allure.step('Находим поле метро')
    def metro_field(self):
        self.find_element_with_wait(OrderPageLocators.INPUT_METRO).click()

    @allure.step('Выбираем станцию метро')
    def choose_station(self):
        self.find_element_with_wait(OrderPageLocators.INPUT_METRO_STATION_EXAMPLE).click()

    @allure.step('Вводим телефон')
    def set_phone_input(self, phone='79999999999'):
        phone_input = self.find_element_with_wait(OrderPageLocators.INPUT_PHONE)
        phone_input.send_keys(phone)

    @allure.step('Нажимаем Далее')
    def press_next(self):
        self.click(OrderPageLocators.NEXT_BUTTON)

    @allure.step('Выбираем дату аренды')
    def pick_date_input(self):

        self.find_element_with_wait(OrderPageLocators.INPUT_DATE_PICKER).click()
        self.find_element_with_wait(OrderPageLocators.ORDER_DATE_PICKER_CHOOSE).click()

    @allure.step('Выбираем период аренды')
    def choose_rent_period(self):
        self.find_element_with_wait(OrderPageLocators.INPUT_TIME).click()
        self.find_element_with_wait(OrderPageLocators.INPUT_PERIOD).click()

    @allure.step('Выбираем цвет')
    def choose_color(self):
        self.click(OrderPageLocators.COLOR)

    @allure.step('Вводим комментарий')
    def add_comment(self, comment):
        self.send_keys(OrderPageLocators.INPUT_COMMENT, comment)

    @allure.step('Нажимаем кнопку Заказать')
    def order_agreement(self):
        self.click(OrderPageLocators.ORDER_BUTTON)

    @allure.step('Подтверждаем заказ')
    def order_confirmation(self):
        self.click(OrderPageLocators.ORDER_YES_BUTTON)

    @allure.step('Проверка подтверждения заказа')
    def order_success(self):
        self.click(OrderPageLocators.ORDER_SUCCESS)



