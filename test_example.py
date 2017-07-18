from time import sleep
import pytest
from selenium import webdriver


@pytest.fixture
def driver(request):
    web_driver = webdriver.Chrome()
    web_driver.maximize_window()
    request.addfinalizer(web_driver.quit)
    return web_driver


def test_example(driver):
    driver.get("http://gs-labs.ru/")
    sleep(5)
