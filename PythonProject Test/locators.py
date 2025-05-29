import time
from selenium import webdriver
from selenium.webdriver.common.by import By # class for the By operator.
# By operator is used to identify the element
from selenium.webdriver.support.select import Select

driver = webdriver.Chrome()
driver.get("https://rahulshettyacademy.com/angularpractice/")

#ID,Xpath,CSSSelector,Class name,name,linkText
driver.find_element(By.NAME,"email").send_keys("hello@gmail.com")
driver.find_element(By.ID,"exampleInputPassword1").send_keys("1234567")
driver.find_element(By.ID,"exampleCheck1").click()
# retrieve element using Xpath
# the syntax is : //tagname[@attribute='value']
#driver.find_element(By.XPATH,"//input[@type='submit']").click()
#driver.find_element(By.XPATH,"//input[@class='btn btn-success']").click()
driver.find_element(By.XPATH,"//input[@value='Submit']").click() # using xpath
#message = driver.find_element(By.CLASS_NAME,"alert").text
#message = driver.find_element(By.CLASS_NAME,"alert-success").text
message = driver.find_element(By.CLASS_NAME,"alert-dismissible").text #using classname
print(message)

# Retrieve element using CSS_SELECTOR
driver.find_element(By.CSS_SELECTOR,"input[name='name']").send_keys("Rahul") # using CSS Selector
# using CSS Selector with #IDName instead of tagname[attribute= value]
driver.find_element(By.CSS_SELECTOR,"#inlineRadio1").click()

assert "Success" in message # assert statement to check if message displayed is correct
#assert "guccess" in message #assert fails here so test case fails

# using index to identify the correct position if we have same locator more than 1
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").send_keys("Completed")
# clears the text entered.here it clears at index 3
driver.find_element(By.XPATH,"(//input[@type='text'])[3]").clear()

# Static Dropdown
dropdown = Select(driver.find_element(By.ID,"exampleFormControlSelect1"))
#dropdown.select_by_value("Male") value can be used only if value is present in inspect
dropdown.select_by_index(0)
dropdown.select_by_visible_text("Female")

time.sleep(15)