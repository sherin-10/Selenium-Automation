import time
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/AutomationPractice/")
driver.implicitly_wait(5)
driver.maximize_window()
action = ActionChains(driver) # here action is the object of ActionChains class
#action.click_and_hold()
#action.context_click() # right click on any item
#action.double_click() # double-click on any item
#action.drag_and_drop(source: driver.find_element(),target: driver.find element) # drags and drops an element
action. move_to_element(driver.find_element(By.ID,"mousehover")).perform()
action.context_click(driver.find_element(By.LINK_TEXT,"Top")).perform()
action.move_to_element(driver.find_element(By.LINK_TEXT,"Reload")).click().perform() # reloads page
#action.move_to_element(driver.find_element(By.LINK_TEXT,"Top")).click().perform() # go to top of page
time.sleep(4)
