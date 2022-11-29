import time

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.seleniumframework.com/Practiceform/")
driver.find_element(By.NAME,"name").send_keys("Andreea Antonescu")
# lista_elemente_email = driver.find_elements(By.NAME,"email")
# lista_elemente_email[1].send_keys("andreea.antonescu@gmail.com")
driver.find_elements(By.NAME,"email")[1].send_keys("andreea.antonescu@gmail.com")
driver.find_element(By.NAME,"telephone").send_keys("0768935401")
driver.find_element(By.NAME,"country").send_keys("Romania")
driver.find_element(By.NAME,"company").send_keys("It Factory")
driver.find_element(By.LINK_TEXT,"Submit").click()
