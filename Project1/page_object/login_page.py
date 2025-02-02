import time
from tkinter import Scale

from pycparser.c_ast import Break

from page_object.base_file import Basepage
from selenium import webdriver
from selenium.webdriver.common.by import By

class Login(Basepage):

    username_id = (By.ID, "user-name")
    password_id = (By.ID, "password")
    login_btn_id = (By.ID, "login-button")
    add_cart_id = (By.ID, "add-to-cart-sauce-labs-backpack")
    click_on_cart_css = (By.CSS_SELECTOR, "[class='shopping_cart_badge']")
    select_product_name = "Sauce Labs Bike Light"
    select_product_name2 = "Sauce Labs Backpack"
    #checkout process
    click_checkout_id = (By.ID, "checkout")
    enter_name_id = (By.ID,"first-name")
    enter_lastn_id = (By.ID, "last-name")
    zip_code_id  = (By.ID, "postal-code")
    click_continue_id = (By.ID, "continue")
    click_finish_id = (By.ID, "finish")
    HUMBERGER_MENU_ID = (By.ID, "react-burger-menu-btn")
    CLICK_LOGOUT_ID = (By.ID ,"logout_sidebar_link")
    filter_drop_down_css = (By.CSS_SELECTOR, "[class='product_sort_container']")
    REMOVE_TEXT_ID = (By.ID, "remove-sauce-labs-bike-light")
    ADD_TO_CART_BUTTON_ID = (By.ID, "add-to-cart-sauce-labs-backpack")
    CONTINUE_SHOPPING = (By.ID ,"continue-shopping")



    def click_on_login(self,username, password):
        self.send_keys(self.username_id,username)
        self.send_keys(self.password_id, password)
        self.do_click(self.login_btn_id)

    def product_add_cart(self):
        self.product_names = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_description']")
        for product in self.product_names:
            product_title = product.find_element(By.XPATH, ".//a").text
            # print(product_title)  # Debugging step to ensure the text is correct
            if product_title == self.select_product_name:
                add_button = product.find_element(By.XPATH, ".//button")
                add_button.click()
                time.sleep(3)# Clicking via JavaScript in case of issues
                break

        self.do_click(self.click_on_cart_css)

    def checkout_process(self,fname,lname,zip_code):
        self.do_click(self.click_checkout_id)
        self.send_keys(self.enter_name_id, fname)
        self.send_keys(self.enter_lastn_id, lname)
        self.send_keys(self.zip_code_id, zip_code)
        self.do_click(self.click_continue_id)
        self.do_click(self.click_finish_id)

    def logout_functionality(self):
        self.do_click(self.HUMBERGER_MENU_ID)
        self.do_click(self.CLICK_LOGOUT_ID)

    def select_filter(self,select_value):
        self.do_click(self.filter_drop_down_css)
        time.sleep(2)
        self.drop_down(self.filter_drop_down_css,select_value)
        time.sleep(2)
        products_price = self.driver.find_elements(By.CSS_SELECTOR, "[class='inventory_item_price']")
        products_prices_list = []
        for price in products_price:
            # print(price.text)
            products_prices_list.append(float(price.text[1:]))

        self.products_prices_list = products_prices_list  # Storing the list for access in the test
        self.sorted_prices = sorted(products_prices_list)

    def mutiple_product_add_cart(self):
        self.product_names = self.driver.find_elements(By.XPATH, "//div[@class='inventory_item_description']")
        for product in self.product_names:
            product_title = product.find_element(By.XPATH, ".//a").text
            # print(product_title)  # Debugging step to ensure the text is correct
            if product_title in [self.select_product_name, self.select_product_name2] :
                add_button = product.find_element(By.XPATH, ".//button")
                add_button.click()
                time.sleep(3)  # Clicking via JavaScript in case of issues
        self.do_click(self.click_on_cart_css)
        self.selected_products = [self.select_product_name2, self.select_product_name]

        carts_products = self.driver.find_elements(By.CSS_SELECTOR, "[class='inventory_item_name']")
        self.carts_product_list = []
        for carts in carts_products:
            # print(carts.text)
            self.carts_product_list.append(carts.text)

    def remove_item_from_cart(self):
        self.product_add_cart()
        self.remove_text = self.get_text(self.REMOVE_TEXT_ID)
        self.do_click(self.click_on_cart_css)
        # self.do_click(self.REMOVE_TEXT_ID)
        self.java_script_click(self.REMOVE_TEXT_ID)
        self.do_click(self.CONTINUE_SHOPPING)
        self.add_cart_button = self.get_text(self.ADD_TO_CART_BUTTON_ID)





















