from selenium.webdriver.common.by import By

from pageobjects.shop import ShopPage
from util.browserutils import BrowserUtils


class LoginPage(BrowserUtils):
    def __init__(self, driver):
        super().__init__(driver) # constructor initialisation for parent class using super().init
        self.driver = driver
        self. username_input = (By.ID, "username")
        self.password= (By.ID, "password")
        self.sign_button = (By.ID, "signInBtn")


    def login(self,username,password):
        self.driver.find_element(*self.username_input).send_keys(username)
        #find_element requires 2 arguments, so we put *self.username to split it into 2
        self.driver.find_element(*self.password).send_keys(password)
        self.driver.find_element(*self.sign_button).click()
        shop_page = ShopPage(self.driver) # here next page object is created and returned
        return shop_page
    #def signUp(self):
