from time import sleep
import pytest
from nose.tools import assert_true
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    web_driver = webdriver.Chrome()
    request.addfinalizer(web_driver.quit)
    return web_driver

def test_lesson_13(driver):

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

    driver.get("http://barancev.i-adept.ru/adept/?app=countries&doc=edit_country")
    wait.until(EC.presence_of_element_located((By.NAME, "save")))

    elements_to_check = driver.find_elements_by_css_selector\
        ('#content > form > table:nth-child(2) > tbody > tr > td > a > i')

    for element in elements_to_check:
        add_country_window = driver.current_window_handle
        old_windows = driver.window_handles
        add_country_title = driver.title
        element.click()
        wait.until(EC.new_window_is_opened)
        new_windows = driver.window_handles
        for element in new_windows:
            if element != old_windows[0]:
                driver.switch_to_window(element)
                assert_true(driver.title != add_country_title)
        driver.close()
        driver.switch_to_window(add_country_window)

    driver.quit()