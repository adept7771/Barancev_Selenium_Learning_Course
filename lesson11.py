import random
from time import sleep
import pytest
from nose.tools import assert_equal
from nose.tools import assert_true
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
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
    driver.get('http://barancev.i-adept.ru/index.php/en/create_account')

    ''' Регистрация '''

    ''' tax id '''
    driver.find_element_by_css_selector(
        '#create-account > div > form > table > tbody > tr:nth-child(1) \
        > td:nth-child(1) > input[type="text"]').send_keys('123')
    ''' Company '''
    driver.find_element_by_css_selector(
        '#create-account > div > form > table > tbody > tr:nth-child(1) > \
        td:nth-child(2) > input[type="text"]').send_keys('123')
    ''' First name '''
    driver.find_element_by_css_selector(
        '#create-account > div > form > table > tbody > tr:nth-child(2) > td:nth-child(1) \
         > input[type="text"]').send_keys(generate_random())
    ''' Last Name '''
    driver.find_element_by_css_selector(
        '#create-account > div > form > table > tbody > tr:nth-child(2) > td:nth-child(2) > \
        input[type="text"]').send_keys(generate_random())
    ''' Address 1 * '''
    driver.find_element_by_css_selector(
        '#create-account > div > form > table > tbody > tr:nth-child(3) > td:nth-child(1) > input[type="text"]') \
        .send_keys('addresssss 11111')
    ''' Postcode * '''
    driver.find_element_by_css_selector(
        '#create-account > div > form > table > tbody > tr:nth-child(4) > td:nth-child(1) > input[type="text"]') \
        .send_keys('12345')
    ''' City * '''
    driver.find_element_by_css_selector(
        '#create-account > div > form > table > tbody > tr:nth-child(4) > td:nth-child(2) > input[type="text"]') \
        .send_keys('Vault 777')
    ''' Country  '''
    driver.find_element_by_css_selector(
        '#create-account > div > form > table > tbody > tr:nth-child(5) > td:nth-child(1) > span.select2.select2-container.select2-container--default > span.selection > span > span.select2-selection__arrow').click()
    sleep(1)
    driver.find_element_by_css_selector('body > span > span >\
    span.select2-search.select2-search--dropdown > input').send_keys('United States')
    driver.find_element_by_css_selector('body > span > span >\
        span.select2-search.select2-search--dropdown > input').send_keys(Keys.ENTER)
    sleep(1)

    ''' Email '''
    e_mail = generate_random()+'@blabla.ru'
    driver.find_element_by_css_selector(
        '#create-account > div > form > table > tbody > tr:nth-child(6) > td:nth-child(1) > input[type="email"]') \
        .send_keys(e_mail)
    ''' Phone  '''
    driver.find_element_by_css_selector(
        '#create-account > div > form > table > tbody > tr:nth-child(6) > td:nth-child(2) > input[type="tel"]') \
        .send_keys('+19094444789')
    ''' Desired Password '''
    pass_word = '12345qwerty12345'
    driver.find_element_by_css_selector(
        '#create-account > div > form > table > tbody > tr:nth-child(8) > td:nth-child(1) > input[type="password"]') \
        .send_keys(pass_word)
    ''' Confirm Password  '''
    driver.find_element_by_css_selector(
        '#create-account > div > form > table > tbody > tr:nth-child(8) > td:nth-child(2) > input[type="password"]') \
        .send_keys(pass_word)
    ''' submit '''
    driver.find_element_by_css_selector('#create-account > div > form > table > tbody > tr:nth-child(9)'
                                        ' > td > button').click()
    sleep(2)
    ''' quit '''
    driver.find_element_by_css_selector('#box-account > div > ul > li:nth-child(4) > a').click()
    ''' re-enter '''
    sleep(1)
    driver.find_element_by_css_selector('#box-account-login > div > form > table > tbody\
     > tr:nth-child(1) > td > input[type="text"]').send_keys(e_mail)
    driver.find_element_by_css_selector('#box-account-login > div > form > table > tbody >\
     tr:nth-child(2) > td > input[type="password"]').send_keys(pass_word)
    driver.find_element_by_css_selector('#box-account-login > div > form > table > tbody > tr:nth-child(4) > td > span > button:nth-child(1)').click()
    ''' quit again'''
    driver.find_element_by_css_selector('#box-account > div > ul > li:nth-child(4)').click()

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
