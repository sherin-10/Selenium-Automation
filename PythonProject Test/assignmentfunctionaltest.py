import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
#implicit wait is used to wait to load the elements instead of sleep
driver.implicitly_wait(5)
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
expected_list = ['Cucumber - 1 Kg','Raspberry - 1/4 Kg','Strawberry - 1/4 Kg'] # list to compare
actual_list = [] # empty list which gets list dynamically
driver.find_element(By.CSS_SELECTOR,".search-keyword").send_keys('ber')
#here sleep is used even though we have implicit wait because implicit wait will just return the empty list
#without waiting for the elements to load as find elements returns an empty list first at the time of running
#while the elements take some time to load so the actual output is not loaded. so the logic breaks here.
time.sleep(3) # used before the find elements step
results = driver.find_elements(By.XPATH,"//div[@class='products']/div")# returns list
print(len(results))
assert len(results) == 3
for result in results:
    actual_list.append(result.find_element(By.XPATH,"h4").text) # appends name to the actual list
    result.find_element(By.XPATH,"div/button").click()
print(actual_list)
# validation to check if actual list and expected list is matching
assert actual_list == expected_list
driver.find_element(By.XPATH,"//img[@alt='Cart']").click()
driver.find_element(By.XPATH,"//button[text()='PROCEED TO CHECKOUT']").click()

#validation to check if the amount matches total amount
amounts = driver.find_elements(By.XPATH,"//tr/td[5]/p")
sum = 0
for amount in amounts:
    sum = sum + int(amount.text)
print(sum)
assert sum == int(driver.find_element(By.CLASS_NAME,"totAmt").text)

#applying promocode
driver.find_element(By.CSS_SELECTOR,".promoCode").send_keys('rahulshettyacademy')
driver.find_element(By.CSS_SELECTOR,".promoBtn").click()
#explicit wait. waits until expected condition meets
# here it is waiting for the web element to be present on screen
# the timeout is 10 seconds
wait = WebDriverWait(driver,10)
wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR,".promoInfo")))
print(driver.find_element(By.CSS_SELECTOR,".promoInfo").text)


#validation to check if discounted amount is less than actual amount
discounted_amount = float(driver.find_element(By.CLASS_NAME,"discountAmt").text)
total_amount = int(driver.find_element(By.CLASS_NAME,"totAmt").text)
print(discounted_amount)
print(total_amount)
assert discounted_amount <= total_amount
