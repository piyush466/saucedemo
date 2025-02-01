import pytest
from selenium import webdriver

from page_object.base_file import Basepage
from page_object.login_page import Login


@pytest.fixture
def setup(request):
    driver = webdriver.Chrome()
    driver.get("https://www.saucedemo.com/")
    driver.maximize_window()
    driver.implicitly_wait(20)
    request.cls.driver = driver
    request.cls.basepage = Basepage(driver)
    request.cls.login = Login(driver)

    yield driver
    driver.quit()




