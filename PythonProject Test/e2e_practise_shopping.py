import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver= webdriver.Chrome()
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/angularpractice/")
# xpath - > //a[contains(@href,'shop')] // contains id used with regular expressions
# css  -> a[href*='shop'] // * is used with regular expressions
driver.find_element(By.CSS_SELECTOR,"a[href*='shop']").click()
required_name ='Blackberry'
product_list =driver.find_elements(By.XPATH,"//div[@class= 'card h-100']")
for product in product_list:
    product_name = product.find_element(By.XPATH,"div[1]/h4/a").text
    if product_name == required_name:
        product.find_element(By.XPATH,"div/button").click()
        print("Added Blackberry to cart.")
driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
# check out
driver.find_element(By.XPATH,"//button[@class='btn btn-success']").click()
driver.find_element(By.ID,"country").send_keys("ind")
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT,"India")))
driver.find_element(By.LINK_TEXT,"India").click()
driver.find_element(By.XPATH,"//div[@class='checkbox checkbox-primary']").click()
driver.find_element(By.XPATH,"//input[@type='submit']").click()
success_msg = driver.find_element(By.CLASS_NAME,"alert.alert-success.alert-dismissible").text
assert "Success! Thank you!" in success_msg # partial text assert using in
driver.close()
