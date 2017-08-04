import random
from time import sleep
import pytest
from nose.tools import assert_equal
from nose.tools import assert_true
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


@pytest.fixture
def driver(request):
    web_driver = webdriver.Chrome()
    # web_driver.maximize_window()
    request.addfinalizer(web_driver.quit)
    return web_driver


def test_lesson_11(driver):
    driver.get('http://barancev.i-adept.ru/index.php/en/')

    ''' Регистрация '''
    driver.find_element_by_css_selector('#box-account-login > div > form > table > \
    tbody > tr:nth-child(5) > td > a')
    ''' tax id '''
    driver.find_element_by_css_selector('#create-account > div > form > table > tbody > tr:nth-child(1) > td:nth-child(1) > input[type="text"]').click()
    ''' '''
    driver.find_element_by_css_selector('')
    ''' '''
    driver.find_element_by_css_selector('')
    ''' '''
    driver.find_element_by_css_selector('')

    driver.quit()

def generate_random():
    str1 = '123456789'
    str2 = 'qwertyuiopasdfghjklzxcvbnm'
    str3 = str2.upper()
    str4 = str1 + str2 + str3
    ls = list(str4)
    random.shuffle(ls)
    result = ''.join([random.choice(ls) for x in range(12)])
    return str(result)
