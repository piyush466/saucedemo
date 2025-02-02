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
            self.logs.info(f"User clicked on this locator: {by_locator}")
        except Exception as E:
            self.logs.error(f"Failed to click on locator {by_locator}. Error: {E}")
            raise

    def send_keys(self, by_locator, text):
        try:
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).send_keys(text)
            self.logs.info(f"User entered text '{text}' in the locator: {by_locator}")
        except Exception as E:
            self.logs.error(f"Failed to send keys to locator {by_locator}. Error: {E}")
            raise

    def get_title(self):
        return self.driver.title

    def get_text(self, by_locator):
        try:
            text = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).text
            self.logs.info(f"Fetched text '{text}' from the locator: {by_locator}")
            return text
        except Exception as E:
            self.logs.error(f"Failed to get text from locator {by_locator}. Error: {E}")
            raise

    def take_screenshot(self, image_name):
        try:
            self.driver.save_screenshot(f"../screenshot/{image_name}.png")
            self.logs.info(f"Screenshot saved with name: {image_name}.png")
        except Exception as E:
            self.logs.error(f"Failed to take screenshot. Error: {E}")
            raise

    def is_display(self, by_locator):
        try:
            is_displayed = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(by_locator)).is_displayed()
            self.logs.info(f"Element visibility checked for locator {by_locator}: {is_displayed}")
            return is_displayed
        except Exception as E:
            self.logs.error(f"Failed to check visibility of locator {by_locator}. Error: {E}")
            raise

    def assertion(self, actual, expected):
        try:
            assert actual == expected, f"Assertion failed: {actual} != {expected}"
            self.logs.info(f"Assertion passed: {actual} == {expected}")
        except AssertionError as E:
            self.logs.error(f"Assertion failed: {actual} != {expected}. Error: {E}")
            raise

    def drop_down(self, by_locator, value):
        try:
            element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator))
            select = Select(element)
            select.select_by_value(value)
            self.logs.info(f"Drop down selected with locator: {by_locator}, value: {value}")
        except Exception as E:
            self.logs.error(f"Failed to select value from drop-down with locator: {by_locator}, value: {value}. Error: {E}")
            raise

    def java_script_click(self, by_locator):
        try:
            self.element = WebDriverWait(self.driver, 20).until(EC.presence_of_element_located(by_locator))
            self.driver.execute_script("arguments[0].click();", self.element)
            self.logs.info(f"JavaScript click performed on locator: {by_locator}")
        except Exception as E:
            self.logs.error(f"JavaScript click failed on locator: {by_locator}. Error: {E}")
            raise
