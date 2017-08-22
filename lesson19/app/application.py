from selenium import webdriver
from lesson19.pages.main_page import MainPage
from lesson19.pages.cart_page import CartPage

class Application:

    def __init__(self):
        self.driver = webdriver.Chrome()
        self.main_page = MainPage(self.driver)
        self.cart_page = CartPage(self.driver)


    def quit(self):
        self.driver.quit()

    def add_new_item_to_cart(self, num_of_items=None):
        if num_of_items == None:
            num_of_items = 3
        a = 0
        while a < num_of_items:
            self.main_page.open()
            self.main_page.goto_first_item_page()
            self.main_page.add_item_to_cart(a)
            self.main_page.open()
            a+=1

    def delete_all_items_in_cart(self):
        self.cart_page.open()
        self.cart_page.delete_all_items_in_cart()




