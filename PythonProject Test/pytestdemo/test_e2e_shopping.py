import json
import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pageobjects.login import LoginPage
test_data_path ='../data/test_e2e_shopping.json' # path of json
with open(test_data_path) as f: #open method to open
    test_data =json.load(f) # assign it to an object after loading
    test_list =test_data["data"] # convert object to a python object to access it


@pytest.mark.parametrize("test_list_item",test_list) # first arg takes each value and then runs each time
def test_e2eshopping(browserInstance,test_list_item):
    #driver = webdriver.Chrome()
    #driver.implicitly_wait(5)
    driver = browserInstance
    #driver.get("https://rahulshettyacademy.com/angularpractice/")
    driver.get("https://rahulshettyacademy.com/loginpagePractise/")
    #driver.find_element(By.ID,"username").send_keys("rahulshettyacademy")
    #driver.find_element(By.ID,"password").send_keys("learning")
    #driver.find_element(By.ID,"signInBtn").click()
    loginPage = LoginPage(driver) # creating object for loginclass with driver as argument
    #loginPage.login() #calling login method from loginclass using object
    print(loginPage.getTitle()) # calling parent class browserutil here
    # xpath - > //a[contains(@href,'shop')] // contains id is used with regular expressions
    # css  -> a[href*='shop'] // * is used with regular expressions
    #driver.find_element(By.CSS_SELECTOR, "a[href*='shop']").click()
    #required_name = 'Blackberry'
    #product_list = driver.find_elements(By.XPATH, "//div[@class= 'card h-100']")
    #for product in product_list:
      #  product_name = product.find_element(By.XPATH, "div[1]/h4/a").text
       # if product_name == required_name:
         #   product.find_element(By.XPATH, "div/button").click()
          #  print("Added Blackberry to cart.")
   # alert = driver.switch_to.alert()
    #alert.accept()
    #driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
    shop_page = loginPage.login(test_list_item["username"],test_list_item["password"]) # shop page obj is created inside login class and return the object of shop page
    shop_page.add_product_to_cart(test_list_item["productName"]) # passing product name here
    print(shop_page.getTitle()) # calling parent class browserutil here
    shop_page.goto_cart()
    # check out
    #driver.find_element(By.XPATH, "//button[@class='btn btn-success']").click()
    #driver.find_element(By.ID, "country").send_keys("ind")
    #wait = WebDriverWait(driver, 10)
    #wait.until(expected_conditions.presence_of_element_located((By.LINK_TEXT, "India")))
    #driver.find_element(By.LINK_TEXT, "India").click()
    #driver.find_element(By.XPATH, "//div[@class='checkbox checkbox-primary']").click()
    #driver.find_element(By.XPATH, "//input[@type='submit']").click()
    #success_msg = driver.find_element(By.CLASS_NAME, "alert.alert-success.alert-dismissible").text
    #assert "Success! Thank you!" in success_msg  # partial text assert using in
    checkout_confirmation = shop_page.goto_cart()
    checkout_confirmation.checkout()
    checkout_confirmation.enter_delivery_address("ind")
    checkout_confirmation.validate_order()

