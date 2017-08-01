from time import sleep
import pytest
from nose.tools import assert_equal
from nose.tools import assert_true
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


def test_lesson_10(driver):
    driver.get("http://barancev.i-adept.ru/")

    ''' проверка совпадений названий и цен, часть а и б'''

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
    print('Названия и цены совпадают')

    ''' проверка цвета (в) '''

    driver.get("http://barancev.i-adept.ru/")

    ordinar_price = driver.find_element_by_css_selector(
        '#box-campaigns > div > ul > li > a.link > div.price-wrapper > s')
    ordinar_price_color_rgba = ordinar_price.value_of_css_property("color")
    ordinar_price_color_rgba = ordinar_price_color_rgba[5:]
    ordinar_price_color_list = ordinar_price_color_rgba.split(',')
    ordinar_price_color_list.pop()

    if len(ordinar_price_color_list) == 3:

        if int(ordinar_price_color_list[0]) == int(ordinar_price_color_list[1]) and \
                        int(ordinar_price_color_list[0]) == \
                        int(ordinar_price_color_list[2]):
            print('RGB совпадают!')
            assert_true(True)
        else:
            print('RGB не совпадают!')
            assert_true(False)
    else:
        assert_true(False)
        print('Ошибка в алгоритме')

    ''' проверка зачеркивания (в) '''

    ordinar_price_text_style = driver.find_element_by_css_selector(
        '#box-campaigns > div > ul > li > a.link > div.price-wrapper > s')

    assert_equal(ordinar_price_text_style.tag_name, 's')
    print('Обычная цена зачеркнута')
    ''' s - указывает на тег зачеркивания в HTML '''

    ''' проверка акционного цвета цены на главной странице (г) '''

    sale_price = driver.find_element_by_css_selector(
        '#box-campaigns > div > ul > li > a.link > div.price-wrapper > strong')
    sale_price_color_rgba = sale_price.value_of_css_property("color")
    sale_price_color_rgba = sale_price_color_rgba[5:]
    sale_price_color_list = sale_price_color_rgba.split(',')
    sale_price_color_list.pop()

    if len(sale_price_color_list) == 3:

        if int(sale_price_color_list[1]) == 0 and int(sale_price_color_list[2]) == 0:
            print('G и B акционного цвета цены на главной странице имеют нулевые значения')
            assert_true(True)
        else:
            print('G и B акционного цвета цены на главной странице НЕ имеют нулевые значения')
            assert_true(False)
    else:
        assert_true(False)
        print('Ошибка в алгоритме')

    ''' проверка акционного цвета цены на странице товара (г) '''

    driver.get('http://barancev.i-adept.ru/index.php/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1')
    sale_price = driver.find_element_by_css_selector(
        '#box-product > div.content > div.information > div.price-wrapper > strong')
    sale_price_color_rgba = sale_price.value_of_css_property("color")
    sale_price_color_rgba = sale_price_color_rgba[5:]
    sale_price_color_list = sale_price_color_rgba.split(',')
    sale_price_color_list.pop()

    if len(sale_price_color_list) == 3:

        if int(sale_price_color_list[1]) == 0 and int(sale_price_color_list[2]) == 0:
            print('G и B акционного цвета цены на странице товара имеют нулевые значения')
            assert_true(True)
        else:
            print('G и B акционного цвета цены на странице товара НЕ имеют нулевые значения')
            assert_true(False)
    else:
        assert_true(False)
        print('Ошибка в алгоритме')
    driver.get('http://barancev.i-adept.ru/')

    ''' проверка акционного шрифта цены на главной странице (г) '''

    sale_price_text_style = driver.find_element_by_css_selector(
        '#box-campaigns > div > ul > li > a.link > div.price-wrapper > strong')

    assert_equal(sale_price_text_style.tag_name, 'strong')
    print('Акционная цена жирная')
    ''' strong - указывает на тег зачеркивания в HTML '''

    ''' проверка акционного шрифта цены на странице товара (г) '''
    driver.get('http://barancev.i-adept.ru/index.php/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1')
    sale_price_text_style = driver.find_element_by_css_selector(
        '#box-product > div.content > div.information > div.price-wrapper > strong')

    assert_equal(sale_price_text_style.tag_name, 'strong')
    print('Акционная цена на странице товара жирная')
    ''' strong - указывает на тег зачеркивания в HTML '''
    driver.get('http://barancev.i-adept.ru/')

    ''' Акционная цена крупнее - на главной странице (г) '''

    ordinar_price_text_style = driver.find_element_by_css_selector(
        '#box-campaigns > div > ul > li > a.link > div.price-wrapper > s')
    sale_price_text_style = driver.find_element_by_css_selector(
        '#box-campaigns > div > ul > li > a.link > div.price-wrapper > strong')

    assert_true(ordinar_price_text_style.size['height'] < sale_price_text_style.size['height'])
    assert_true(ordinar_price_text_style.size['width'] < sale_price_text_style.size['width'])
    print('На главной странице размеры шрифта у распродаж больше, чем у обычной цены.')

    ''' Акционная цена крупнее - на странице товара (г) '''
    driver.get('http://barancev.i-adept.ru/index.php/en/rubber-ducks-c-1/subcategory-c-2/yellow-duck-p-1')
    ordinar_price_text_style = driver.find_element_by_css_selector(
        '#box-product > div.content > div.information > div.price-wrapper > s')
    sale_price_text_style = driver.find_element_by_css_selector(
        '#box-product > div.content > div.information > div.price-wrapper > strong')

    assert_true(ordinar_price_text_style.size['height'] < sale_price_text_style.size['height'])
    assert_true(ordinar_price_text_style.size['width'] < sale_price_text_style.size['width'])
    print('На странице товара размеры шрифта у распродаж больше, чем у обычной цены.')

    driver.quit()
