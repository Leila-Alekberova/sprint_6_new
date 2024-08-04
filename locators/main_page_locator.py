from selenium.webdriver.common.by import By

class MainPageLocators:
    QUESTIONS_ACCORDION = By.XPATH, '//*[@id="accordion__heading-{}"]'  #Блок с вопросами
    ANSWERS_ACCORDION = By.XPATH, '//*[@id="accordion__panel-{}"]'  #Ответы в блоке с вопросами