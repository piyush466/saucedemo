from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(10)

labels = driver.find_elements(By.XPATH, "//label")
for label in labels:
    print(label.text)
    if label.text == "Option3":
        label.find_element(By.XPATH, "./input").click()

driver.find_element(By.ID, "opentab").click()

windows = driver.window_handles
print(windows)




