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
    driver.get("http://barancev.i-adept.ru/")
    wait.until(EC.presence_of_element_located((By.NAME, "email")))
    list_of_most_popular = driver.find_elements_by_css_selector(
        '#box-most-popular > div > ul > li > a.link > div.image-wrapper > div')
    list_of_campaigns = driver.find_elements_by_css_selector(
        '#box-campaigns > div > ul > li > a.link > div.image-wrapper > div')
    list_of_latest_prod = driver.find_elements_by_css_selector(
        '#box-latest-products > div > ul > li > a.link > div.image-wrapper > div')

    check(list_of_most_popular, '#box-most-popular', driver)
    check(list_of_campaigns, '#box-campaigns', driver)
    check(list_of_latest_prod, '#box-latest-products', driver)
    driver.quit()


def check(list_of_items, boxname, driver):
    if len(list_of_items) > 0:
        i = 1
        for item in list_of_items:
            label_count = driver.find_elements_by_css_selector(
                boxname + ' > div > ul > li:nth-child('+str(i)+') > a.link > \
                div.image-wrapper > div[class *=sticker]')

            count = len(label_count)

            if len(label_count) > 1:
                print('Товар: №' + str(i) + ' - стикер есть и он не один!')
            if len(label_count) == 0:
                print('Товар: №' + str(i) + ' - стикеров у товара нет')
            else:
                print('Товар: №' + str(i) + ' - имеет один стикер')
            i += 1

    else:
        print('Запрашиваемые элементы не найдены.')
