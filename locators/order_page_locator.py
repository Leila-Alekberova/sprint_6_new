from selenium.webdriver.common.by import By
from locators.base_page_locator import BasePageLocators

class OrderPageLocators:
    INPUT_FIRST_NAME = (By.XPATH, '//input[@placeholder="* Имя"]')  # поле ввода имени
    INPUT_SECOND_NAME = (By.XPATH, '//input[@placeholder="* Фамилия"]')  # поле ввода фамилии
    INPUT_ADDRESS = (By.XPATH, '//input[contains(@placeholder,"Адрес")]')  # поле ввода адреса
    INPUT_METRO = (By.CLASS_NAME, 'select-search__input')  # раскрытие списка станции метро
    INPUT_METRO_STATION_EXAMPLE = (By.XPATH, '//div[text()="Черкизовская"]') # выбор станции Сокольники
    INPUT_PHONE = (By.XPATH, '//input[contains(@placeholder,"Телефон")]')  # поле ввода телефона
    INPUT_DATE_PICKER = (By.XPATH, "//input[@placeholder='* Когда привезти самокат']") # поле когда привезти самокат
    ORDER_DATE_PICKER_CHOOSE = (By.XPATH, "//div[@aria-label='Choose пятница, 2-е августа 2024 г.']") # выбираем дату
    INPUT_TIME = (By.XPATH, '//div[text()="* Срок аренды"]')  # поле выбора Срок аренда
    INPUT_PERIOD = (By.XPATH, '//div[text()="сутки"]')  # срок аренды сутки
    COLOR = (By.ID, 'grey')  # цвет самоката серая безысходность
    INPUT_COMMENT = (By.XPATH, '//input[contains(@placeholder,"Комментарий для курьера")]')  # поле ввода комментария
    BACK_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM']") # кнопка назад
    ORDER_BUTTON = (By.XPATH, '//div[@class = "Order_Buttons__1xGrp"]/button[text()="Заказать"]') # кнопка Заказать на форме заказа
    ORDER_WINDOW = (By.XPATH, '//div[text()="Хотите оформить заказ?"]') # окно подтверждение заказа
    ORDER_YES_BUTTON = (By.XPATH, '//button[text()="Да"]')  # кнопка подтверждения заказа
    ORDER_SUCCESS = (By.XPATH, '//div[contains(@class,"Order_ModalHeader") and text()="Заказ оформлен"]')  # успех
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')  # кнопка Далее