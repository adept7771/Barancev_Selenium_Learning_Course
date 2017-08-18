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
    driver.get('http://barancev.i-adept.ru/adept/?app=catalog&doc=catalog')
    wait.until(EC.presence_of_element_located((By.NAME, "delete")))

    ''' проведем подсчет всех пунктов в каталоге '''
    catalog_list = driver.find_elements_by_css_selector('#content > form > table\
     > tbody > tr > td:nth-child(3) > a')
    catalog_len = len(catalog_list)
    ''' необходимо пройтись по всем элементам каталога, длина каталога будет меняться
     в зависимости от суммарного количества элементов'''
    i = 3 # порядковый номер элемента для обращения, из-за верстки начинаем с третьего
    b = catalog_len+3 # граница проверок
    catalog_counter = 0 # счетчик каталогов

    while i <= b:
        element = driver.find_element_by_css_selector\
            ('#content > form > table > tbody > tr:nth-child('+str(i)+') > td:nth-child(3) > a')
        '''если элемент это ссылка каталога, просто переходим по ней и расширяем длину списка товаров'''
        if element.get_attribute('href').find('product_id') == -1:
            ''' если элемент - каталог, переходим в него '''
            element.click()
            catalog_counter += 1
            ''' считаем получившееся число элементов каталога'''

            current_cat_len = len(driver.find_elements_by_css_selector('#content > form > table\
             > tbody > tr > td:nth-child(3) > a'))

            '''если при открытии каталога, элементов стало больше или столько же, 
            расширяем список для проверки'''
            if current_cat_len >= catalog_len:
                current_cat_len += catalog_counter
                b += (current_cat_len - catalog_len)
                '''смещаем границу проверок на разницу списков элементов'''
                catalog_len = current_cat_len
                '''присваием новую длину списку элементов'''
                i += 1
            else:



        else:
            'если элемент не каталог - проверяем его и возвращаемся к общему списку'
            element.click()
            driver.find_element_by_css_selector('#content > form > p > span > button:nth-child(2)').click()
            i += 1






    # for element in catalog_list:
    #
    #     if element.get_attribute('href').find('category_id') != -1:
    #         element.click()
    #         catalog_len = len(driver.find_elements_by_css_selector('#content > form > table > tbody\
    #          > tr > td:nth-child(3) > a'))


    i = 0
    # while i <= len(catalog_list):
    #     current_url = driver.current_url
    #     wait.until(EC.presence_of_element_located((By.NAME, "delete")))
    #     sleep(1)
    #     catalog_list[i].click()
    #     if driver.find_element_by_css_selector('#content > h1').get_attribute("innerText") == " Catalog":
    #         tmp_list = driver.find_elements_by_css_selector('#content > form > table > tbody > tr > td:nth-child(3) > a')
    #         i += 1
    #         sleep(1)
    #         if len(tmp_list) != len(catalog_list):
    #             catalog_list = tmp_list
    #             i = 0
    #         sleep(1)
    #     else:
    #         print('я в товаре')
    #         sleep(1)
    #         driver.get(current_url)


    driver.quit()