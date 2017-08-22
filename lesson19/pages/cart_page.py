from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CartPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        if self.driver.current_url != 'http://barancev.i-adept.ru/index.php/en/checkout':
            self.driver.get('http://barancev.i-adept.ru/index.php/en/checkout')
            self.wait.until(EC.presence_of_element_located(
                (By.CSS_SELECTOR, "#order_confirmation-wrapper > form > div.comments > textarea")))
        return self

    def delete_all_items_in_cart(self):
        ''' проверка количества элементов '''
        items_in_cart = self.driver.find_elements_by_css_selector('#box-checkout-cart > ul > li > a')
        ''' цикл удаления '''
        current_item_num = 1
        if len(items_in_cart) > 0:
            while current_item_num <= len(items_in_cart):
                if current_item_num < len(items_in_cart):
                    ''' кликаем на товар, если товар не последний оставшийся в корзине'''
                    self.driver.find_element_by_css_selector('#box-checkout-cart > ul > li:nth-child(1) > a').click()

                current_item_title = self.driver.find_element_by_css_selector(
                    '#box-checkout-cart > div > ul > li:nth-child(1) > form > div > p:nth-child(1) > a > strong') \
                    .get_attribute('textContent')

                ''' удаляем '''
                self.driver.find_element_by_name('remove_cart_item').click()

                ''' небольшой велосипед '''
                new_item_title = self.driver.find_element_by_css_selector(
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
                        self.driver.find_element_by_css_selector('#box-checkout-cart > div > ul > li:nth-child(1) > form >\
                                         div > p:nth-child(1) > a > strong').get_attribute('textContent')
                    self.wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#order_confirmation-wrapper > table\
                         > tbody > tr:nth-child(2) > td.item'), current_item_name))
                else:
                    sleep(3)
                ''' для визуальной проверки, что все элементы корзины удалены. Можно закомментить. '''
                current_item_num += 1
        else:
            print('Элементов в корзине нет, или они уже удалены!')

        print('Все элементы корзины успешно удалены!')
        return self