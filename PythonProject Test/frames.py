import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox()
driver.get("https://the-internet.herokuapp.com/iframe")
WebDriverWait(driver, 20).until(EC.frame_to_be_available_and_switch_to_it((By.ID, "mce_0_ifr")))
driver.switch_to.frame("mce_0_ifr") # switches to frame

driver.find_element(By.ID,"tinymce").clear()
driver.find_element(By.ID,"tinymce").send_keys("Automating frames")
driver.switch_to.default_content() # switches to original window
print(driver.find_element(By.TAG_NAME,"h3").text)
time.sleep(3)
