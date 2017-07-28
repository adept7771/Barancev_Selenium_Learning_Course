from time import sleep
import pytest
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


def test_example(driver):
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
    list_of_menus = driver.find_elements_by_css_selector('ul[id=box-apps-menu] > li')
    i = 1
    for element in list_of_menus:
        driver.find_element_by_css_selector('ul[id=box-apps-menu]>li:nth-child(' + str(i) + ')').click()
        list_of_submenus = driver.find_elements_by_css_selector(
            'ul[id=box-apps-menu]>li:nth-child(' + str(i) + ')>ul li')
        i2 = 1
        if len(list_of_menus) > 0:

            for submenu in list_of_submenus:
                try:
                    driver.find_element_by_css_selector('#content > h1 > span')
                    print("H1 is here!")
                except NoSuchElementException:
                    print('H1 is absent')

                driver.find_element_by_css_selector(
                    'ul[id=box-apps-menu]>li:nth-child(' + str(i) + ')>ul li:nth-child(' + str(i2) + ')').click()
                i2 += 1
        i += 1

    driver.quit()
