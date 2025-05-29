import time

from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
#checking Checkboxes
checkboxes = driver.find_elements(By.XPATH,"//input[@type='checkbox']")
print(len(checkboxes))
for checkbox in checkboxes:
    if checkbox.get_attribute("value")=='option2':
        checkbox.click()
        assert checkbox.is_selected()
        break

#checking Radiobuttons
radiobuttons = driver.find_elements(By.XPATH,"//input[@type='radio']")
# if you know which index is the desired button
radiobuttons[2].click()
# if index is dynamic and changes
print(len(radiobuttons))
for radiobutton in radiobuttons:
    if radiobutton.get_attribute("value")=='radio1':
        radiobutton.click()
        assert radiobutton.is_selected()
        break

# is displayed fn - to check if a text is displayed on screen
assert driver.find_element(By.ID,"displayed-text").is_displayed()
driver.find_element(By.ID,"hide-textbox").click()
#assert not is opposite of assert. it passes when condition given is false
assert not driver.find_element(By.ID,"displayed-text").is_displayed()
time.sleep(3)