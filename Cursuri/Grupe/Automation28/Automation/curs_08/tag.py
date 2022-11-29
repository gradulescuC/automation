from selenium.webdriver.support.select import Select

from selenium import webdriver
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.get("https://formy-project.herokuapp.com/form")
lista_labels = driver.find_elements(By.TAG_NAME,"label")
print(len(lista_labels))
for i in range(len(lista_labels)):
		print(lista_labels[i].text)
dropdown_menu = Select(driver.find_element(By.TAG_NAME,"select"))
dropdown_menu.select_by_visible_text("2-4")
