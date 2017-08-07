from time import sleep
import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture
def driver(request):
    web_driver = webdriver.Chrome()
    request.addfinalizer(web_driver.quit)
    return web_driver


def test_lesson_12(driver):
    wait = WebDriverWait(driver, 20)
    driver.get("http://barancev.i-adept.ru/")
    wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#box-account-login > div > form > table >\
     tbody > tr:nth-child(4) > td > span > button:nth-child(1)')))
    ''' число товаров для добавления в корзину '''
    number_of_target_items = 3
    i = 1
    while i <= number_of_target_items:
        ''' переходим на страничку товара '''
        driver.find_element_by_css_selector('#box-most-popular > div > ul > li:nth-child(1) > a.link').click()
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#box-similar-products > h3")))
        ''' проверяем обязательное поле селект, если оно есть '''
        if len(driver.find_elements_by_css_selector('#box-product >\
         div.content > div.information > div.buy_now > form > table >\
          tbody > tr:nth-child(1) > td > select')) > 0:
            driver.find_element_by_css_selector('#box-product > div.content > div.information > div.buy_now > form > table > tbody > tr:nth-child(1) > td > select').click()
            driver.find_element_by_css_selector('#box-product > div.content > div.information > div.buy_now > form > table > tbody > tr:nth-child(1) > td > select > option:nth-child(2)').click()
        ''' добавляем в корзину '''
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#box-product > div.content >\
                     div.information > div.buy_now > form > table > tbody > tr > td > button")))
        driver.find_element_by_css_selector('#box-product > div.content > div.information > div.buy_now\
                     > form > table > tbody > tr > td > button').click()
        ''' ждем обновления '''
        wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#cart > a.content > span.quantity'), str(i)))
        ''' возвращаемся на главную '''
        driver.get("http://barancev.i-adept.ru/")
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#box-account-login > div > form > table >\
                 tbody > tr:nth-child(4) > td > span > button:nth-child(1)')))
        i += 1

    ''' переходим в корзину '''
    driver.get('http://barancev.i-adept.ru/index.php/en/checkout')
    wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "#order_confirmation-wrapper > form > div.comments > textarea")))
    ''' проверка количества элементов '''
    items_in_cart = driver.find_elements_by_css_selector('#box-checkout-cart > ul > li > a')
    ''' цикл удаления '''
    current_item_num = 1
    if len(items_in_cart) > 0:
        while current_item_num <= len(items_in_cart):
            if current_item_num < len(items_in_cart):
                ''' кликаем на товар, если товар не последний оставшийся в корзине'''
                driver.find_element_by_css_selector('#box-checkout-cart > ul > li:nth-child(1) > a').click()

            current_item_title = driver.find_element_by_css_selector(
                '#box-checkout-cart > div > ul > li:nth-child(1) > form > div > p:nth-child(1) > a > strong') \
                .get_attribute('textContent')

            ''' удаляем '''
            driver.find_element_by_name('remove_cart_item').click()

            ''' небольшой велосипед '''
            new_item_title = driver.find_element_by_css_selector(
                '#box-checkout-cart > div > ul > li:nth-child(1) > form > div > p:nth-child(1) > a > strong') \
                .get_attribute('textContent')
            ''' если заголовок не поменялся, ждем '''
            if current_item_title == new_item_title:
                sleep(1)
            ''' к сожалению, не один другой способ определения доступности элементов не смог
             победить прелоудер, который вызывает ошибки '''

            ''' ждем обновления таблицы товаров, если элемент корзины не последний '''
            if current_item_num < len(items_in_cart):
                current_item_name = \
                    driver.find_element_by_css_selector('#box-checkout-cart > div > ul > li:nth-child(1) > form >\
                                 div > p:nth-child(1) > a > strong').get_attribute('textContent')
                wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#order_confirmation-wrapper > table\
                 > tbody > tr:nth-child(2) > td.item'), current_item_name))
            else:
                sleep(3)
            ''' для визуальной проверки, что все элементы корзины удалены. Можно закомментить. '''
            current_item_num += 1
    else:
        print('Элементов в корзине нет, или они уже удалены!')

    print('Все элементы корзины успешно удалены!')
    driver.quit()

