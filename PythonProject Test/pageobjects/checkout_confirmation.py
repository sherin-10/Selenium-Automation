from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from util.browserutils import BrowserUtils


class Checkout_Confirmation(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver =driver
        self.checkout_button =(By.XPATH, "//button[@class='btn btn-success']")
        self.country_input = (By.ID, "country")
        self.country_option = (By.LINK_TEXT, "India")
        self.checkbox =(By.XPATH, "//div[@class='checkbox checkbox-primary']")
        self.submit_button = (By.XPATH, "//input[@type='submit']")
        self.success_msg =(By.CLASS_NAME, "alert.alert-success.alert-dismissible")


    def checkout(self):
        self.driver.find_element(*self.checkout_button).click()

    def enter_delivery_address(self,country_name):
        self.driver.find_element(*self.country_input).send_keys(country_name)
        wait = WebDriverWait(self.driver, 10)
        wait.until(expected_conditions.presence_of_element_located(self.country_option))
        self.driver.find_element(*self.country_option).click()
        self.driver.find_element(*self.checkbox).click()
        self.driver.find_element(*self.submit_button).click()

    def validate_order(self):
        success_msg = self.driver.find_element(*self.success_msg).text
        assert "Success! Thank you!" in success_msg  # partial text assert using in



