import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://formy-project.herokuapp.com/form")
time.sleep(3)
# driver.find_element("id","first-name").send_keys("Test")
driver.find_element(By.ID,"first-name").send_keys("Test 123 abc","test1 parametru separat")
driver.find_element(By.ID,"first-name").send_keys("apelare suplimentara")
driver.find_element(By.ID,"last-name").send_keys("it factory")
time.sleep(3)
driver.quit() # inchide tot browserul si toate taburile active
# driver.close() # inchide doar tab-ul activ din browser
