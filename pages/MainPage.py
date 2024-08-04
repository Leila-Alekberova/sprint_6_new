from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTIONS = By.XPATH, '//*[@id="accordion__heading-{}"]'  #Блок с вопросами
    ANSWERS = By.XPATH, '//*[@id="accordion__panel-{}"]'  #Ответы на вопросы