import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
name = "Rahul"
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.find_element(By.CSS_SELECTOR,"#name").send_keys(name)
time.sleep(2)
driver.find_element(By.CSS_SELECTOR,"#alertbtn").click()
time.sleep(5)
alert= driver.switch_to.alert # switch to alert mode to handle popup
alerttext= alert.text
assert name in alerttext
alert.accept() # to accept popup
#alert.dismiss() # to cancel popup
time.sleep(5)