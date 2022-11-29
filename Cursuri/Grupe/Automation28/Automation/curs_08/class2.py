from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("http://www.seleniumframework.com/Practiceform/")
driver.find_element(By.CLASS_NAME,"validate[required]").send_keys("Andreea Antonescu")
driver.find_element(By.CLASS_NAME,"validate[required,custom[email]]").send_keys("andreea.antonescu@gmail.com")
driver.find_element(By.CLASS_NAME,"validate[required,custom[phone]]").send_keys("0768935401")
driver.find_element(By.NAME,"country").send_keys("Romania")
driver.find_element(By.NAME,"company").send_keys("It Factory")
driver.find_element(By.CLASS_NAME,"dt-btn-submit").click()

"""
atentie!!!
Daca in HTML vedeti o clasa care contine spatii, atunci aveti de a face cu mai multe clase separate prin spatiu
				caz in care cautarea in selenium se va face doar cu una din ele care va asigura unicitatea
"""
