import time
from selenium.webdriver.common.by import By
from page_object.base_file import Basepage
from page_object.login_page import Login
from test_cases.baseclass import BaseClass


class Test_login(BaseClass):
    get_text_xpath = (By.XPATH, "//div[text()='Swag Labs']")
    get_text_invalid = (By.XPATH, "//h3")
    invalid_text = "Epic sadface: Username and password do not match any user in this service"
    product_name = (By.CSS_SELECTOR, "[class='inventory_item_name']")
    #after checkout complete
    success_messgae_tagname = (By.TAG_NAME, "h2")

    def test_01_valid_login(self):
        self.login.click_on_login("standard_user", "secret_sauce")
        self.basepage.assertion(self.basepage.get_text(self.get_text_xpath) ,"Swag Labs")

    def test_02_invalid_login(self):
        self.login.click_on_login("standard_user", "se")
        self.basepage.assertion(self.basepage.get_text(self.get_text_invalid), self.invalid_text)

    def test_03_login_with_black_creds(self):
        self.login.click_on_login(" ", "")
        self.basepage.assertion(self.basepage.get_text(self.get_text_invalid), "Epic sadface: Password is required")

    #Verify "Add to Cart" functionality
    def test_04_add_cart_functionality(self):
        self.login.click_on_login("standard_user", "secret_sauce")
        self.login.product_add_cart()
        self.basepage.assertion(self.basepage.get_text(self.product_name), self.login.select_product_name)

    #Verify cart checkout process
    def test_05_cart_checkout_process(self):
        self.login.click_on_login("standard_user", "secret_sauce")
        self.login.product_add_cart()
        self.login.checkout_process("piyush","dravyakr", 444111)
        self.basepage.assertion(self.basepage.get_text(self.success_messgae_tagname), "Thank you for your order!")

    #verify logout functionality
    def test_06_check_logout_functionality(self):
        self.login.click_on_login("standard_user", "secret_sauce")
        self.login.logout_functionality()
        self.basepage.assertion(self.basepage.get_title(), "Swag Labs")

    #verify low to high filter
    def test_07_filter(self):
        self.login.click_on_login("standard_user", "secret_sauce")
        self.login.select_filter("lohi")
        self.basepage.assertion(self.login.products_prices_list, self.login.sorted_prices)

    #verify user can multiple products in cart
    def test_08_user_can_add_mutiple_products_cart(self):
        self.login.click_on_login("standard_user", "secret_sauce")
        self.login.mutiple_product_add_cart()
        self.basepage.assertion(self.login.selected_products, self.login.carts_product_list)

    #verify user can remove hte product from cart
    def test_09_user_can_remove_the_product_from_cart(self):
        self.login.click_on_login("standard_user", "secret_sauce")
        self.login.product_add_cart()
        self.login.remove_item_from_cart()
        self.basepage.assertion(self.login.add_cart_button, "Add to cart")















