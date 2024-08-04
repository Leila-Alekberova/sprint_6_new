import allure
import pytest
import locators
from locators.main_page_locator import MainPageLocators
from locators.base_page_locator import BasePageLocators
from conftest import driver
from pages.MainPage import *
from pages.BasePage import BasePage
from data import *

class TestOrderButtons:

    @allure.title('Клик на кнопку "Заказать" в хедере страницы')
    def test_click_on_header_button(self, driver):
        main_page = BasePage(driver)
        main_page.cookie_click()
        main_page.order_upper_button_click()
        current_url = main_page.get_current_url()
        assert current_url == Urls.url_order


class TestDzen:
    @allure.title('Тест перехода на Дзен')
    @allure.title('Проверка редиректа на страницу Дзена по клику на логотип Яндекса в хедере')
    def test_click_on_yandex_logo(self, driver):
        main_page = BasePage(driver)
        main_page.cookie_click()
        main_page.wait_for_element_to_be_clickable(BasePageLocators.YANDEX_LOGO)
        main_page.click(BasePageLocators.YANDEX_LOGO)
        main_page.driver_changes()
        main_page.wait_title("Дзен")
        assert '/dzen' in main_page.get_current_url()

class TestAnswers:
    @allure.title('Проверка функционирования раскрывающихся вопросов в блоке "Вопросы о важном"')
    @allure.description('Методом параметризации проверяем текст ответов вопроса поочередно')
    @pytest.mark.parametrize('number', range(8))
    def test_click_and_get_answer(self, driver, number):
        main_page = BasePage(driver)
        main_page.cookie_click()
        question = MainPageLocators.QUESTIONS[0]
        question_2 = MainPageLocators.QUESTIONS[1].format(number)
        main_page.click((question, question_2))

        answer = MainPageLocators.ANSWERS[0]
        answer_2 = MainPageLocators.ANSWERS[1].format(number)
        answer_text = main_page.get_element_text((answer, answer_2))

        waiting_text = Answers.answers[number]
        assert answer_text == waiting_text


class TestClickHeaderLogo:
    @allure.title('Проверка перехода по клику на логотип Самоката в хедере страницы')
    def test_click_on_scooter_logo(self, driver):
        order_page = BasePage(driver)
        order_page.order_upper_button_click()
        order_page.scooter_logo_button_click()
        assert order_page.get_current_url() == Urls.url_main



