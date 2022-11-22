from time import sleep

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)
chrome.maximize_window()

chrome.get("https://www.cel.ro/")
chrome.find_element(By.ID,"keyword").send_keys("laptop i7")
chrome.find_element(By.XPATH,'//button[@type="submit" and @aria-label="Cauta"]').click()
sleep(3)
chrome.find_element(By.XPATH,'//div[@data-mkey="producator"]/div[@class="showMoreWrapper"]/a[@class="btnShowMore"]').click()
lista_furnizori = chrome.find_elements(By.XPATH,'//div[@data-mkey="producator"]/div/a')
produs = "Dell"
# for furnizor in lista_furnizori:
# 		if produs in furnizor.text:
# 				numar_elemente = furnizor.text.replace(produs,"").replace("(","").replace(")","")
# 				print(numar_elemente)

for manufacturer_name in lista_furnizori:
		if produs in manufacturer_name.text:
				results = manufacturer_name.text.replace(produs, "").replace("(", "").replace(")", "").replace(" ","")
				print(results)
				assert int(results)>=2