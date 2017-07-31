from time import sleep
import pytest
from nose.tools import assert_equal
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


def test_countries_zones(driver):
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
    driver.get("http://barancev.i-adept.ru/adept/?app=countries&doc=countries")

    ''' check primary sorting '''
    countries = driver.find_elements_by_css_selector('form > table > tbody > tr > td:nth-child(5) > a')
    countries_list = []
    for item in countries:
        countries_list.append(item.text)
    sorted_countries_list = sorted(countries_list)
    assert_equal(sorted_countries_list, countries_list)

    ''' check inner sorting '''
    zones_to_check = []
    i = 2
    for item in countries:
        current_zone = driver.find_element_by_css_selector('form > table > tbody > tr:nth-child('+str(i)+') > td:nth-child(6)')
        if int(current_zone.text) > 0:
            zones_to_check.append(i)
        i += 1

    current_zones_list = []
    i = 2
    for item in zones_to_check:
        driver.find_element_by_css_selector('form > table > tbody > tr:nth-child('+str(item)+') > td:nth-child(7)').click()
        current_zones_list = driver.find_elements_by_css_selector('tbody > tr:nth-child('+str(i)+') > td:nth-child(3)')
        sorted_current_zones_list = sorted(current_zones_list)
        assert_equal(sorted_current_zones_list, current_zones_list)
        ''' << go back to countries '''
        driver.find_element_by_css_selector('#content > form > p > span > button:nth-child(2)').click()
        i += 1

    driver.quit()
