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


def test_lesson_12(driver):
    wait = WebDriverWait(driver, 10)
    ''' =================== LOGIN =================== '''
    driver.get("http://barancev.i-adept.ru/adept/login.php")
    wait.until(EC.presence_of_element_located((By.NAME, "username")))
    driver.find_element_by_name('username').click()
    driver.find_element_by_name('username').send_keys('adept2')
    driver.find_element_by_name('password').click()
    driver.find_element_by_name('password').send_keys('zmowv53479353jtzv')
    driver.find_element_by_name('login').click()
    ''' ============================================== '''
    driver.find_element_by_css_selector('ul > li:nth-child(2) > a > span.name').click()
    driver.find_element_by_css_selector('#content > div:nth-child(2) > a:nth-child(2)').click()
    ''' name '''
    driver.find_element_by_css_selector('#tab-general > table > tbody > tr:nth-child(2) > td > span > input[type="text"]').click()
    driver.find_element_by_css_selector(
        '#tab-general > table > tbody > tr:nth-child(2) > td > span > input[type="text"]')\
        .send_keys(generate_random())
    ''' code '''
    driver.find_element_by_css_selector(
        '#tab-general > table > tbody > tr:nth-child(3) > td > input[type="text"]').click()
    driver.find_element_by_css_selector(
        '#tab-general > table > tbody > tr:nth-child(3) > td > input[type="text"]').send_keys('12345')
    '''Product Groups'''
    driver.find_element_by_css_selector(
        '#tab-general > table > tbody > tr:nth-child(7) > td > div > table > tbody > tr:nth-child(2) \
        > td:nth-child(1) > input[type="checkbox"]').click()
    ''' Images '''
    #driver.find_element_by_css_selector('')
    ''' date valid forms '''
    valid_from_form = driver.find_element_by_css_selector('#tab-general > table > tbody > \
    tr:nth-child(10) > td > input[type="date"]')
    valid_from_form.click()
    sleep(1)
    valid_from_form.send_keys('10')
    sleep(2)
    valid_from_form.send_keys('10')
    sleep(2)
    valid_from_form.send_keys('2012')

    valid_to_form = driver.find_element_by_css_selector('#tab-general > table > tbody \
    > tr:nth-child(11) > td > input[type="date"]')
    valid_to_form.click()
    valid_to_form.send_keys('10')
    sleep(2)
    valid_to_form.send_keys('10')
    sleep(2)
    valid_to_form.send_keys('2018')
    sleep(2)

    sleep(20)
    #driver.find_element_by_css_selector('')
    #driver.find_element_by_css_selector('')
    #driver.find_element_by_css_selector('')
    #driver.find_element_by_css_selector('')

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
