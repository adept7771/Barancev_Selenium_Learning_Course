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

    # ''' первая часть задания '''
    #
    # ''' check primary sorting '''
    # countries = driver.find_elements_by_css_selector('form > table > tbody > tr > td:nth-child(5) > a')
    # countries_list = []
    # for item in countries:
    #     countries_list.append(item.text)
    # sorted_countries_list = sorted(countries_list)
    # assert_equal(sorted_countries_list, countries_list)
    #
    # ''' check inner sorting '''
    # zones_to_check = []
    # i = 2
    # for item in countries:
    #     current_zone = driver.find_element_by_css_selector(
    #         'form > table > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(6)')
    #     if int(current_zone.text) > 0:
    #         zones_to_check.append(i)
    #     i += 1
    #
    # current_zones_list = []
    # i = 2
    # for item in zones_to_check:
    #     driver.find_element_by_css_selector(
    #         'form > table > tbody > tr:nth-child(' + str(item) + ') > td:nth-child(7)').click()
    #     current_zones_list = driver.find_elements_by_css_selector(
    #         'tbody > tr:nth-child(' + str(i) + ') > td:nth-child(3)')
    #     sorted_current_zones_list = sorted(current_zones_list)
    #     assert_equal(sorted_current_zones_list, current_zones_list)
    #     ''' << go back to countries '''
    #     driver.find_element_by_css_selector('#content > form > p > span > button:nth-child(2)').click()
    #     i += 1

    ''' 2 часть задания '''

    driver.get("http://barancev.i-adept.ru/adept/?app=geo_zones&doc=geo_zones")

    list_of_countries = driver.find_elements_by_css_selector('form > table > tbody > tr td:nth-child(5)')
    i = 2
    ''' формируем общий список Стран Геозон '''
    for element in list_of_countries:
        ''' проходим по каждой стране '''
        driver.find_element_by_css_selector(
            '#content > form > table > tbody > tr:nth-child(' + str(i) + ') > td:nth-child(5)').click()
        primary_list_of_zones_with_junkdata = driver.find_elements_by_css_selector(
            '#table-zones > tbody > tr > td:nth-child(3) > select')
        ''' создаем список стран из dropdown menu без лишнего мусора'''
        string_with_zones = primary_list_of_zones_with_junkdata[0].text
        list_of_dropdown_zones = string_with_zones.split('\n')
        list_of_dropdown_zones.pop(0)
        ''' формируем список всех всех доступных зон из dropdown menu '''

        actual_zones_with_junk = driver.find_elements_by_css_selector(
            '#table-zones > tbody > tr > td:nth-child(3) > select')
        ''' формируем список текущих зон, для страны с мусорными данными '''

        actual_zones_names = []
        ''' выделяем из списка текущих зон ТОЛЬКО имена зон '''
        a = 2
        ''' перебор каждого элемента '''
        for element in actual_zones_with_junk:
            current_zone_element_index = driver.find_element_by_css_selector(
                '#table-zones > tbody > tr:nth-child(' + str(a) + ') > td:nth-child(3) > select').get_attribute(
                'selectedIndex')
            ''' получаем отмеченный индекс зоны для текущего id и присваиваем ему имя, исходя из списка всех зон '''
            current_zone_element_name = list_of_dropdown_zones[int(current_zone_element_index) - 1]
            actual_zones_names.append(current_zone_element_name)

            #assert_equal(current_zone_element_name, sorted_list_of_dropdown_zones[a-2])
            a += 1

        ''' Сравниваем список отсортированных имен зон от получившегося списка и получившийся список '''
        assert_equal(actual_zones_names, sorted(actual_zones_names))

        ''' возвращаемся в общий список стран'''
        driver.find_element_by_css_selector('#content > form > p > span > button:nth-child(2)').click()

    print("Элементы зон отсортированы верно")

    driver.quit()
