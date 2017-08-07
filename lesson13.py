import random
import pytest
from nose.tools import assert_equal
from nose.tools import assert_false
from nose.tools import assert_true
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    web_driver = webdriver.Chrome()
    # web_driver.maximize_window()
    request.addfinalizer(web_driver.quit)
    return web_driver

def test_lesson_12(driver):
    wait = WebDriverWait(driver, 10)
    driver.get("http://barancev.i-adept.ru/")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#box-account-login > div > form > table >\
     tbody > tr:nth-child(4) > td > span > button:nth-child(1)')))
    first_item_adding(driver, wait)
    first_item_adding(driver, wait)
    first_item_adding(driver, wait)



    print('Сработало!')

    driver.quit()


def first_item_adding(driver, wait):
    current_cart_items_num = driver.find_element_by_css_selector('#cart > a.content > span.quantity') \
        .get_attribute('textContent')
    ''' переходим на страничку товара '''
    driver.find_element_by_css_selector('#box-most-popular > div > ul > li:nth-child(1) > a.link').click()
    ''' добавляем в корзину '''
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#box-product > div.content >\
     div.information > div.buy_now > form > table > tbody > tr > td > button")))
    driver.find_element_by_css_selector('#box-product > div.content > div.information > div.buy_now\
     > form > table > tbody > tr > td > button').click()
    ''' ждем обновления '''
    locator1 = driver.find_element_by_css_selector('#cart > a.content > span.quantity')
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#cart > a.content > span.quantity'), '1'))
    ''' возвращаемся на главную '''
    driver.get("http://barancev.i-adept.ru/")

