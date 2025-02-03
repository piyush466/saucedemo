import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

options = Options()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(options=options)
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
practice = driver.title
driver.switch_to.window(windows[1])
qaclick = driver.title

if practice == qaclick:
    print("both pagers are same")
elif practice != qaclick:
    print("pass")


driver.switch_to.window(windows[0])
time.sleep(3)

driver.find_element(By.ID, "name").send_keys("piyush")
driver.find_element(By.ID, "alertbtn").click()

alert = driver.switch_to.alert
print(alert.text)
alert.accept()
# assert  "piyush" in alert.text, "failed"

element = driver.find_element(By.XPATH, "//button[@id='mousehover']")
driver.execute_script("arguments[0].scrollIntoView();", element)
# driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(2)
new_element = driver.find_element(By.CLASS_NAME,"mouse-hover")
action = ActionChains(driver)
action.move_to_element(new_element).perform()
driver.find_element(By.XPATH, "//a[text()='Top']").click()
time.sleep(2)
driver.execute_script("arguments[0].scrollIntoView();", element)
time.sleep(2)

frame = driver.switch_to.frame("courses-iframe")

driver.find_element(By.LINK_TEXT, "Blog").click()

driver.switch_to.default_content()
time.sleep(5)

















