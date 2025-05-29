import time

from selenium import webdriver
from selenium.webdriver.common.by import By # class for the By operator.
# By operator is used to identify the element

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/client")
#Using link text locator to find the links
driver.find_element(By.LINK_TEXT,"Forgot password?").click()
#Using Xpath locator by traversing from parent to child  and to child and using indexing to find right child
driver.find_element(By.XPATH,"//form/div[1]/input").send_keys("demo@gmail.com")
#Using CSSSelector locator by traversing from parent to child  and to child and using indexing to find right child
driver.find_element(By.CSS_SELECTOR,"form div:nth-child(2) input").send_keys("Hello@1234")
driver.find_element(By.CSS_SELECTOR,"#confirmPassword").send_keys("Hello@1234")
driver.find_element(By.XPATH,"//button[@type='submit']").click()
#Another method using only xpath is to find the text and pass the text as element in the corresponding tag
driver.find_element(By.XPATH, "//button[text()='Save New Password']").click()

time.sleep(15)