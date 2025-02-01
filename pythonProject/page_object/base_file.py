from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from Utilities.generate_logs import LogGen

class Basepage:


    logs = LogGen.loggenerates()

    def __init__(self, driver):
        self.driver = driver

    def do_click(self, by_locator):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).click()
            self.logs.info(f"user click on this locator {by_locator}")
        except Exception as E:
            self.logs.error(f"Failed to click on locator {by_locator}",f"{E}")
            raise


    def send_keys(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
            self.logs.info(f"user click on this locator {by_locator} and user pass this in text box {text}")
        except Exception as E:
            self.logs.error(f"Failed to click on locator {by_locator}")
            raise


    def get_title(self):
        return self.driver.title

    def get_text(self, by_locator):
        return WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).text

    def take_screenshot(self, image_name):
        self.driver.save_screenshot(f"../screenshot/{image_name}.png")

    def is_display(self, by_locator):
        WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator)).is_displayed()

    def assertion(self,actual, expected):
        try:
            assert actual == expected , "Failed"
            self.logs.info(f"assertion pass:- {actual} == {expected}")
        except Exception as E:
            self.logs.error(f"assertion failed:- {actual} == {expected}")
            raise

    def drop_down(self,by_locator,value):
        try:
            element = WebDriverWait(self.driver,20).until(EC.presence_of_element_located(by_locator))
            select = Select(element)
            select.select_by_value(value)
            self.logs.info(f"drop down field is working with this locator:- {by_locator} and this value:- {value}")
        except Exception as E:
            self.logs.error(f"drop down field is not working with this locator:- {by_locator} and this value:- {value}")
            raise

    def java_script_click(self,by_locator):
        try:
            self.element = WebDriverWait(self.driver,20).until(EC.presence_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].click();",self.element)
        except Exception as E:
            self.logs.error(f"javascript click not working with this locator {by_locator}")
            raise