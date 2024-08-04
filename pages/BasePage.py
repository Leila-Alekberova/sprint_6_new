import allure
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators.base_page_locator import *
from locators.main_page_locator import *
from data import *

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Перейти на страницу')
    def go_to_site(self, url='https://qa-scooter.praktikum-services.ru/'):
        return self.driver.get(url)

    @allure.step('Запрос URL страницы')
    def get_current_url(self):
        return self.driver.current_url

    @allure.step('Нахождение и ожидание элемента')
    def find_element_with_wait(self, locator):
        WebDriverWait(self.driver, 5).until(expected_conditions.visibility_of_element_located(locator))
        return self.driver.find_element(*locator)

    @allure.step('Клик на элемент')
    def click(self, locator):
        button = self.driver.find_element(*locator)
        button.click()

    @allure.step('Ожидание отображения элемента')
    def wait_until_element_visibility(self, time, locator):
        WebDriverWait(self.driver, time).until(expected_conditions.visibility_of_element_located(locator))

    @allure.step('Скролл страницы')
    def scroll(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    allure.step('Скроллим страницу и ожидаем отображение элемента')
    def appears_from_element(self):
        self.find_element_with_wait(MainPageLocators.QUESTIONS_ACCORDION[1])

    @allure.step('Принятие куки')
    def cookie_click(self):
        self.click(BasePageLocators.ACCEPT_COOKIE)

    @allure.step('Нажатие на кнопку "Заказать в хедере')
    def order_upper_button_click(self):
        self.click(BasePageLocators.UPPER_ORDER_BUTTON)

    @allure.step('Нажатие на кнопку "Заказать в теле страницы')
    def order_bottom_button_click(self):
        self.click(BasePageLocators.ORDER_BUTTON)

    @allure.step('Отображение текста элемента')
    def get_element_text(self, locator):
        element = self.driver.find_element(*locator)
        WebDriverWait(self.driver, 10).until(expected_conditions.visibility_of_element_located(locator))
        return element.text

    @allure.step('Отправка заполненного поля')
    def send_keys(self, locator, value):
        self.driver.find_element(*locator).send_keys(value)

    @allure.step('Отображение локатора вопроса')
    def answer_locator(number):
        return MainPageLocators.ANSWERS[number]

    @allure.step('Нахождение вопроса по его номеру')
    def question_locator(number):
        return MainPageLocators.QUESTIONS[number]

    @allure.step('Найти вопросы и возврат их ответа')
    def click_and_get_answer(self, number):
        self.find_element_with_wait((number)).click()
        return self.find_element_with_wait(Answers(number))

    @allure.step('Ожидание, чтобы кнопка стала доступна для клика')
    def wait_for_element_to_be_clickable(self, locator):
        WebDriverWait(self.driver, 10).until(expected_conditions.element_to_be_clickable(locator))

    @allure.step('Смена URL страницы')
    def url_changes(self, url):
        WebDriverWait(self.driver, 10).until(expected_conditions.url_changes(url))

    @allure.step('Переключение драйвера')
    def driver_changes(self):
        self.driver.switch_to.window(self.driver.window_handles[-1])

    @allure.step('Ожидание  заголовка')
    def wait_title(self, title):
        WebDriverWait(self.driver, 10).until(expected_conditions.title_is(title))

    @allure.step('Нажатие на кнопку сервиса Самокат в хедере')
    def scooter_logo_button_click(self):
        self.click(BasePageLocators.SCOOTER_LOGO)


