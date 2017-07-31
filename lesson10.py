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
    driver.get("http://barancev.i-adept.ru/")

    main_page_name = driver.find_element_by_css_selector('#box-campaigns > div > ul > li > a.link > div.name').text
    main_page_price = driver.find_element_by_css_selector(
        '#box-campaigns > div > ul > li > a.link > div.price-wrapper > s').text
    main_page_sale = driver.find_element_by_css_selector(
        '#box-campaigns > div > ul > li > a.link > div.price-wrapper > strong').text
    driver.find_element_by_css_selector('#box-campaigns > div > ul > li > a.link > div.name').click()
    product_page_name = driver.find_element_by_css_selector('#box-product > div:nth-child(1) > h1').text
    product_page_price = driver.find_element_by_css_selector(
        '#box-product > div.content > div.information > div.price-wrapper > s').text
    product_page_sale = driver.find_element_by_css_selector(
        '#box-product > div.content > div.information > div.price-wrapper > strong').text

    assert_equal(main_page_name, product_page_name)
    assert_equal(main_page_price, product_page_price)
    assert_equal(main_page_sale, product_page_sale)

    driver.get("http://barancev.i-adept.ru/")


    print('!')
    driver.quit()
