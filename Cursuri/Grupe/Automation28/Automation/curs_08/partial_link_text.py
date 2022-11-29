import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://the-internet.herokuapp.com/")
driver.find_element(By.PARTIAL_LINK_TEXT,"onload").click()
time.sleep(3)
driver.close()