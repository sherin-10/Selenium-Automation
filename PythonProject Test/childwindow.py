import time
from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element(By.LINK_TEXT,"Click Here").click()
windowsopened = driver.window_handles # list returning windows opened
driver.switch_to.window(windowsopened[1]) # child window is stored at 1 index in the list, switches to child
time.sleep(3)
# new way to identify element using tag name
print(driver.find_element(By.XPATH,"//div/h3").text) # prints text in new window
driver.close() # closes current window. here it is child window
driver.switch_to.window(windowsopened[0]) # switches back to parent window
time.sleep(3)
assert "Opening a new window" == driver.find_element(By.TAG_NAME,"h3").text


#---------------Firefox -----------
#wait = WebDriverWait(driver,10)
#wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
