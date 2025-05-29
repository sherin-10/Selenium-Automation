import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.switch_to.frame("courses-iframe")
print(driver.find_element(By.CSS_SELECTOR,"div[class='pull-left']").text)
driver.switch_to.default_content()
text = driver.find_element(By.ID, "openwindow").text
print(text)
time.sleep(3)