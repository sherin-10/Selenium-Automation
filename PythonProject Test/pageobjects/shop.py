from selenium.webdriver.common.by import By

from pageobjects.checkout_confirmation import Checkout_Confirmation
from util.browserutils import BrowserUtils


class ShopPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver =driver
        self.shoplink = (By.CSS_SELECTOR, "a[href*='shop']")
        self.productslist = (By.XPATH, "//div[@class= 'card h-100']")

    def add_product_to_cart(self, product_name):
        self.driver.find_element(*self.shoplink).click()
        #required_name = 'Blackberry'
        product_list = self.driver.find_elements(*self.productslist)
        for product in product_list:
            product_Name = product.find_element(By.XPATH, "div[1]/h4/a").text
            if product_Name == product_name:
                product.find_element(By.XPATH, "div/button").click()
                print("Added Blackberry to cart.")
        # alert = driver.switch_to.alert()
        # alert.accept()
    def goto_cart(self):
        self.driver.find_element(By.CSS_SELECTOR, "a[class*='btn-primary']").click()
        checkout_confirmation = Checkout_Confirmation(self.driver)
        return checkout_confirmation


