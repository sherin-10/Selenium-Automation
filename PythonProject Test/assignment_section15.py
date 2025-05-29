from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
actuallist= []
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/offers")
driver.find_element(By.XPATH,"//span[text()= 'Veg/fruit name']").click()
browsersortedlist = driver.find_elements(By.XPATH,"//tbody/tr/td[1]")
for i in browsersortedlist:
    actuallist.append(i.text)
print(actuallist)
actuallist_copy= actuallist.copy()
actuallist.sort()
assert actuallist_copy == actuallist
