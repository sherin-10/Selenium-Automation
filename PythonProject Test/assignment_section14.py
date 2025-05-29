import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/loginpagePractise/")
driver.find_element(By.CLASS_NAME,"blinkingText").click()
windowsopened = driver.window_handles
driver.switch_to.window(windowsopened[1])
message = driver.find_element(By.XPATH,"//div/p[2]").text
print(message)
#var = message.split("at")[1].strip().split(" ")[0]
email = message.split('at ')[1].split(' ')[0]
username = email.split('@')[1].split('.')[0]
print(username)
driver.close()
driver.switch_to.window(windowsopened[0])
driver.find_element(By.ID,"username").send_keys(username)
driver.find_element(By.ID,"password").send_keys(username)
driver.find_element(By.XPATH,"//input[@type='checkbox']").click()
driver.find_element(By.ID,"signInBtn").click()


