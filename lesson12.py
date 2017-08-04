import random
from os import getcwd
from time import sleep
import pytest
from nose.tools import assert_equal
from nose.tools import assert_true
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains


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
    ''' ^ переходим в каталог '''
    num_of_products = len(driver.find_elements_by_css_selector('table > tbody > tr > td:nth-child(3) > a'))
    ''' ^ считываем число продуктов (оно нам пригодится) '''
    driver.find_element_by_css_selector('#content > div:nth-child(2) > a:nth-child(2)').click()
    sleep(1)
    ''' name '''
    driver.find_element_by_css_selector(
        '#tab-general > table > tbody > tr:nth-child(2) > td > span > input[type="text"]').click()
    driver.find_element_by_css_selector(
        '#tab-general > table > tbody > tr:nth-child(2) > td > span > input[type="text"]') \
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
    local_path = getcwd()
    local_path += '\screen.png'
    driver.find_element_by_css_selector('#tab-general > table > tbody > tr:nth-child(9) > \
     td > table > tbody > tr:nth-child(1) > td > input[type="file"]').send_keys(local_path)
    ''' date valid forms '''
    valid_from_form = driver.find_element_by_css_selector('#tab-general > table > tbody > \
    tr:nth-child(10) > td > input[type="date"]')
    valid_from_form.click()

    valid_from_form.send_keys('10')
    sleep(1)
    valid_from_form.send_keys('10')
    sleep(1)
    valid_from_form.send_keys('2012')

    valid_to_form = driver.find_element_by_css_selector('#tab-general > table > tbody \
    > tr:nth-child(11) > td > input[type="date"]')
    valid_to_form.click()
    valid_to_form.send_keys('10')
    sleep(1)
    valid_to_form.send_keys('10')
    sleep(1)
    valid_to_form.send_keys('2018')

    ''' switch to information panel '''
    driver.find_element_by_css_selector('#content > form > div > ul > li:nth-child(2) > a').click()
    sleep(1)
    driver.find_element_by_xpath('//*[@id="tab-information"]/table/tbody/tr[1]/td/select/option[2]').click()

    driver.find_element_by_css_selector(
        '#tab-information > table > tbody > tr:nth-child(3) > td > input[type="text"]').click()
    driver.find_element_by_css_selector(
        '#tab-information > table > tbody > tr:nth-child(3) > td > input[type="text"]').send_keys('some_keyword')
    driver.find_element_by_css_selector(
        '#tab-information > table > tbody > tr:nth-child(4) > td > span > input[type="text"]').click()
    driver.find_element_by_css_selector(
        '#tab-information > table > tbody > tr:nth-child(4) > td > span > input[type="text"]').send_keys(
        'short description')
    driver.find_element_by_css_selector(
        '#tab-information > table > tbody > tr:nth-child(5) > td > span > div > div.trumbowyg-editor').click()
    driver.find_element_by_css_selector(
        '#tab-information > table > tbody > tr:nth-child(5) > td > span > div > div.trumbowyg-editor').send_keys(
        'loooooooooong long description')
    driver.find_element_by_css_selector(
        '#tab-information > table > tbody > tr:nth-child(6) > td > span > input[type="text"]').click()
    driver.find_element_by_css_selector(
        '#tab-information > table > tbody > tr:nth-child(6) > td > span > input[type="text"]').send_keys('head title')
    driver.find_element_by_css_selector(
        '#tab-information > table > tbody > tr:nth-child(7) > td > span > input[type="text"]').click()
    driver.find_element_by_css_selector(
        '#tab-information > table > tbody > tr:nth-child(7) > td > span > input[type="text"]').send_keys(
        'meta description')

    ''' switch to prices '''

    driver.find_element_by_css_selector('#content > form > div > ul > li:nth-child(4) > a').click()

    driver.find_element_by_css_selector('#tab-prices > table:nth-child(2) > tbody > tr \
    > td > input[type="number"]').click()
    driver.find_element_by_css_selector(
        '#tab-prices > table:nth-child(2) > tbody > tr > td > input[type="number"]').send_keys('10')
    driver.find_element_by_css_selector('#tab-prices > table:nth-child(2) > tbody > tr > td > select').click()
    sleep(1)
    driver.find_element_by_css_selector('#tab-prices > table:nth-child(2) > tbody > tr > td > \
    select > option:nth-child(3)').click()
    driver.find_element_by_css_selector('#tab-prices > table:nth-child(4) > tbody > tr:nth-child(2) \
    > td:nth-child(1) > span > input[type="text"]').click()
    driver.find_element_by_css_selector(
        '#tab-prices > table:nth-child(4) > tbody > tr:nth-child(2) > td:nth-child(1) > span > \
        input[type="text"]').send_keys('10')
    driver.find_element_by_css_selector('#tab-prices > table:nth-child(4) > tbody > tr:nth-child(3) \
    > td:nth-child(1) > span > input[type="text"]').click()
    driver.find_element_by_css_selector(
        '#tab-prices > table:nth-child(4) > tbody > tr:nth-child(3) > td:nth-child(1) > span > \
        input[type="text"]').send_keys('30')

    driver.find_element_by_css_selector('#content > form > p > span > button:nth-child(1)').click()
    sleep(2)
    ''' активируем созданный элемент '''
    driver.find_element_by_css_selector('#content > form > table > tbody > tr.row.semi-transparent > td:nth-child(1)').click()
    driver.find_element_by_css_selector('#content > form > ul > li:nth-child(2) > span > button:nth-child(1)').click()
    sleep(1)

    ''' проверка, что элемент создан '''

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
