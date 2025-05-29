from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
driver = webdriver.Chrome()
driver.implicitly_wait(5)
fruit_name='Mango'
driver.get("https://rahulshettyacademy.com/upload-download-test/index.html")
driver.find_element(By.ID,"downloadButton").click()
# edit excel with updated values
# upload file back after editing
file_input = driver.find_element(By.XPATH,"//input[@type='file']") # type should be file to upload file
# send keys is used to upload file specified in the path
file_input.send_keys("C:\\Users\\sheri\\Downloads\\download.xlsx")

wait= WebDriverWait(driver,5)
locator = (By.CSS_SELECTOR,".Toastify__toast-body div:nth-child(2)")
wait.until(expected_conditions.visibility_of_element_located(locator))
# find element requires 2 arguments: By and value.
# Since we have combined both in locator, we put * to make it like 2 arguments and avoid syntax error
print(driver.find_element(*locator).text)

#generic step to get fruit apple price and column number
#price = driver.find_element(By.XPATH,"//div[text()='Apple']/parent::div/parent::div/div[@id='cell-4-undefined']").text
# Next we write how to dynamically get fruit name and column id
# to get the column id of price dynamically and stored in variable
price_column_id = driver.find_element(By.XPATH,"//div[text()='Price']").get_attribute("data-column-id")
# dynamically passing fruit name and position of column
price = driver.find_element(By.XPATH,"//div[text()='"+fruit_name+"']/parent::div/parent::div/div[@id='cell-"+price_column_id+"-undefined']").text
print(price)