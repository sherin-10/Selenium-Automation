import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/dropdownsPractise/")
driver.find_element(By.ID,"autosuggest").send_keys("in") # enters the text in dropdown to get suggesions
time.sleep(3)
countries = driver.find_elements(By.CSS_SELECTOR,"li[class='ui-menu-item'] a")
print(len(countries))

for country in countries:
    if country.text == 'India':
        country.click()
        break
time.sleep(3)
print(driver.find_element(By.ID,"autosuggest").text) # this won't work as the value is dynamic
#We use javascript code to get dynamic values entered at runtime
print(driver.find_element(By.ID,"autosuggest").get_attribute("value"))
# Use assertion to check if returned value is same as value entered
assert(driver.find_element(By.ID,"autosuggest").get_attribute("value")) =='India'
