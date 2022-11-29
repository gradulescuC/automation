from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://formy-project.herokuapp.com/form")
driver.find_element(By.CLASS_NAME,"form-control").send_keys("First name is identified by class")
driver.find_elements(By.CLASS_NAME,"form-control")[1].send_keys("Last name is identified by class in list")
driver.find_elements(By.CLASS_NAME,"form-control")[2].send_keys("Job identified by class in list")