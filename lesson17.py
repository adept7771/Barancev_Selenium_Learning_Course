from time import sleep
import pytest
from nose.tools import assert_true
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains


@pytest.fixture
def driver(request):
    web_driver = webdriver.Chrome()
    web_driver.maximize_window()
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
    list_of_item_links = []
    catalog_entities_list = driver.find_elements_by_css_selector(
        '#content > form > table > tbody > tr > td:nth-child(3) > a')
    repeat = True

    while repeat:
        'формируем первоначальный список ссылок'
        for element in catalog_entities_list:
            if element.get_attribute('href') not in list_of_item_links:
                list_of_item_links.append(str(element.get_attribute('href')))
        repeat = False

    repeat = True
    while repeat:
        'проходим по списку и ищем категории. Прощелкиваем их и добавляем новые ссылки - если таковые есть'
        for element in list_of_item_links:
            'если ссылка в списке каталог - переходим в него'
            if element.find('product_id') == -1:
                driver.get(element)
                'получаем новый список элементов каталога'
                catalog_entities_list = driver.find_elements_by_css_selector(
                    '#content > form > table > tbody > tr > td:nth-child(3) > a')
                'сравниваем ссылки полученных элементов, с уже имеющимися и добавляем отсутствующие ссылки'
                for item in catalog_entities_list:
                    if item.get_attribute('href') not in list_of_item_links:
                        list_of_item_links.append(str(item.get_attribute('href')))

        'если больше ссылок нет на каталоги, поиск прекращаем'
        repeat = False

    'вычищаем список получившихся ссылок от ссылок на каталоги'
    for a in list_of_item_links:
        if a.find('product_id') == -1:
            list_of_item_links.remove(a)
    list_of_item_links.pop(0)  # по неведомой причине файнд не обрабатывает всегда правильно 1й эл-т

    'список ссылок на товары готов. Проверяем каждый товар на ошибки'
    for element in list_of_item_links:
        driver.get(element)
        wait.until(EC.presence_of_element_located((By.NAME, "delete")))
        logs = driver.get_log("browser")
        url = driver.current_url
        'Если логи не пусты - выводим их'
        if logs is not None:
            for log in logs:
                print('')
                print('Current page: ' + url)
                print('Level: ' + log['level'])
                print('Message ' + log['message'])
    print('!')