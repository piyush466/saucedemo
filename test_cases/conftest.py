

import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from page_object.about_us_page import About_Us
from page_object.base_file import Basepage
from page_object.login_page import Login


@pytest.fixture
def setup(request):

    option = Options()
    # option.add_argument("--headless")
    option.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=option)
    driver.get("https://www.saucedemo.com/")
    driver.implicitly_wait(20)
    request.cls.driver = driver
    request.cls.basepage = Basepage(driver)
    request.cls.login = Login(driver)
    request.cls.about = About_Us(driver)

    yield driver
    driver.quit()




