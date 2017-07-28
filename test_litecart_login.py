from time import sleep
import pytest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException


@pytest.fixture
def driver(request):
    # web_driver = webdriver.Chrome()
    web_driver = webdriver.Ie()
    # web_driver = webdriver.Firefox()
    web_driver.maximize_window()
    web_driver.implicitly_wait(5)
    request.addfinalizer(web_driver.quit)
    return web_driver


def test_example(driver):
    driver.get("http://barancev.i-adept.ru/adept/login.php")
    # sleep(2)
    # driver.find_element_by_name('username').click
    # driver.find_element_by_name('username').send_keys('adept2')
    # driver.find_element_by_name('password').click
    # driver.find_element_by_name('password').send_keys('zmowv53479353jtzv')
    # driver.find_element_by_name('login').click()
    # sleep(2)
    driver.quit()
