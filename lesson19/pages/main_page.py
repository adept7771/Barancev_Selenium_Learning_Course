from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        if self.driver.current_url != "http://barancev.i-adept.ru/":
            self.driver.get("http://barancev.i-adept.ru/")
            self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, '#box-account-login > div > form > table >\
                 tbody > tr:nth-child(4) > td > span > button:nth-child(1)')))
        return self

    def goto_first_item_page(self):
        self.driver.find_element_by_css_selector('#box-most-popular > div > ul > li:nth-child(1) > a.link').click()
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#box-similar-products > h3")))
        return self

    def add_item_to_cart(self, a):
        ''' проверяем обязательное поле селект, если оно есть '''
        if len(self.driver.find_elements_by_css_selector('#box-product >\
                 div.content > div.information > div.buy_now > form > table >\
                  tbody > tr:nth-child(1) > td > select')) > 0:
            self.driver.find_element_by_css_selector(
                '#box-product > div.content > div.information > div.buy_now > form > table > tbody > tr:nth-child(1) > td > select').click()
            self.driver.find_element_by_css_selector(
                '#box-product > div.content > div.information > div.buy_now > form > table > tbody > tr:nth-child(1) > td > select > option:nth-child(2)').click()
        ''' добавляем в корзину '''
        self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "#box-product > div.content >\
                             div.information > div.buy_now > form > table > tbody > tr > td > button")))
        self.driver.find_element_by_css_selector('#box-product > div.content > div.information > div.buy_now\
                             > form > table > tbody > tr > td > button').click()
        ''' ждем обновления '''
        self.wait.until(
            EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#cart > a.content > span.quantity'), str(a+1)))
        return self



