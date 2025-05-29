
from selenium import webdriver
#driver = webdriver.Chrome()
#driver.get("https://google.com")
#time.sleep(3)

import time
from selenium import webdriver
driver = webdriver.Chrome()
from selenium.webdriver.chrome.service import Service  # importing service class
#driver = webdriver.Firefox()
#driver = webdriver.Edge()
# service class is downloaded in the path specified below from chrome service class downloaded from google
#This is done when Chrome version is old and selenium couldn't find the chrome driver by itself.
#otherwise selenium itself finds the chrome driver and chrome driver acts as a middleman between chrome and selenium
#service_obj= Service("path")
#driver = webdriver.Chrome(service= service_obj)

driver.get("https://rahulshettyacademy.com")
driver.maximize_window()
print(driver.title)
print(driver.current_url)
time.sleep(3)