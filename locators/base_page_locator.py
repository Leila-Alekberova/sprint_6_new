from selenium.webdriver.common.by import By


class BasePageLocators:
    YANDEX_LOGO = (By.XPATH, '//a[@class="Header_LogoYandex__3TSOI"]') #лого Яндекс
    SCOOTER_LOGO = (By.XPATH, '//a[@class="Header_LogoScooter__3lsAR"]') #лого Самокат
    ACCEPT_COOKIE = (By.XPATH, "//*[contains(@class,'App_CookieButton__3cvqF')]") #принятие куки "Да все привыкли"
    UPPER_ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g']") #кнопка "Заказать" в хедере страницы
    ORDER_BUTTON = (By.XPATH, "//button[@class='Button_Button__ra12g Button_Middle__1CSJM' and text()='Заказать']") #кнопка "Заказать" в теле страницы