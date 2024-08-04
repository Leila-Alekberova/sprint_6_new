import pytest
from selenium import webdriver
from data import Urls


@pytest.fixture(scope='function')
def driver():
    firefox_driver = webdriver.Firefox()
    firefox_driver.get(Urls.url_main)
    firefox_driver.maximize_window()

    yield firefox_driver

    firefox_driver.quit()