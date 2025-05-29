import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.service import Service

# define chrome options to open browser as headless, to ignore the certificate errors
chrome_options = webdriver.ChromeOptions() # chrome options object
chrome_options.add_argument("--headless") # browser doesn't open up in UI but executes in backend
chrome_options.add_argument("--ignore-certificate-errors") # to prevent certificate errors
# Chrome browser is invoked along with the chrome options argument
driver = webdriver.Chrome(options = chrome_options)
# invoking chrome options with the service class method
#service_obj = Service("/Users/CDrive etc---------")
#driver = webdriver.Chrome(service = service_obj,options = chrome_options) # pass service class object and chrome options
driver.get("https://rahulshettyacademy.com/AutomationPractice/") # normal chrome driver with chrome options

# javascript executor to scroll down
driver.execute_script("window.scrollBy(0,500);") # scroll 500 in Y axis
driver.execute_script("window.scrollBy(0,document.body.scrollHeight);") # scroll to end of document
# take screenshot and save as png
driver.get_screenshot_as_file("screenshot.png")
