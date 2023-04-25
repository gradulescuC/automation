"""

"""
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())

# Intrati pe site-ul https://www.elefant.ro/
chrome.get("https://www.elefant.ro/")
chrome.maximize_window()

# - Test 1: Identificati butonul "accept cookies" si dati click pe el
try:
		accept_cookies = WebDriverWait(chrome,10).until(EC.presence_of_element_located((By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")))
		accept_cookies.click()
except:
		pass

# - Test 2: cautati un produs la alegere (iphone 14) si verificati ca s-au returnat cel putin 10 rezultate ([class="product-title"])
chrome.find_element(By.XPATH,'//input[@name="SearchTerm"]').send_keys("Iphone 14")
time.sleep(5)
button_list = chrome.find_elements(By.XPATH,'//button[@name="search"]')
button_list[0].click()
WebDriverWait(chrome,10).until(EC.presence_of_element_located((By.CLASS_NAME,'product-title')))
returned_elements = chrome.find_elements(By.CLASS_NAME,'product-title')
for i in range(len(returned_elements)):
		print(f"Elementul curent este: {returned_elements[i].text}")
assert len(returned_elements)>=10,"Error, the number of returned elements is not correct"

# - Test 3: Extrageti din lista produsul cu pretul cel mai mic [class="current-price "] -> //img[@class="product-image"]
element_prices = chrome.find_elements(By.CLASS_NAME,"current-price ")
dict_elemente = {}
for i in range(len(returned_elements)):
		dict_elemente[returned_elements[i].text]=element_prices[i].text.replace(".","").replace(",",".").replace(" lei","")[:-3]

min_price = 99999999999999
produs_min = ""
for key, value in dict_elemente.items():
		if int(value)<int(min_price):
				min_price = value
				produs_min = key
print(f"Produsul cu cel mai mic pret este: {produs_min} si are valoarea de {min_price} lei")

# - Test 4: Extrageti titlul paginii si verificati ca este corect
chrome.find_elements(By.XPATH,'//div[@id="HeaderRow"]//a[@rel="home"]')[0].click()
actual_title = chrome.title
expected_title = "elefant.ro - mallul online al familiei tale! • Branduri de top, preturi excelente • Peste 500.000 de produse pentru tine!"
assert actual_title == expected_title,"Error, title is not correct"

# - Test 5: Intrati pe site, accesati butonul cont si click pe conectare.
# Identificati elementele de tip user si parola si inserati valori incorecte
# 			(valori incorecte inseamna oricare valori care nu sunt recunscute drept cont valid)
# - Dati click pe butonul "conectare" si verificati urmatoarele:
#             1. Faptul ca nu s-a facut logarea in cont
#             2. Faptul ca se returneaza eroarea corecta

chrome.find_element(By.XPATH,'//ul[@class="user-links"]/li/a[@href="#account-layer"]').click()
connect_button = chrome.find_element(By.XPATH,'//div[@id="account-layer"]//a[contains(text(),"Conectare")]')
ActionChains(chrome).move_to_element(connect_button).click(connect_button).perform()
username = chrome.find_element(By.ID,"ShopLoginForm_Login")
username.send_keys("invalid_username@gmail.com")
password = chrome.find_element(By.ID,"ShopLoginForm_Password")
password.send_keys("invalid_password")
login_button=chrome.find_element(By.XPATH,'//button[@value="Login"]')
login_button.click()
actual_error = chrome.find_element(By.XPATH,'//div[@role="alert"]').text
expected_error = "Adresa dumneavoastră de email / Parola este incorectă. Vă rugăm să încercați din nou."
assert expected_error == actual_error,"Error, mesajul de eroare este incorect"
login_button=chrome.find_element(By.XPATH,'//button[@value="Login"]')
assert login_button.is_displayed()==True, "Error, logarea a fost facuta desi credentialele sunt incorecte"

# - Test 6: Stergeti valoarea de pe campul email si introduceti o valoare invalida (adica fara caracterul "@") si verificati faptul ca butonul "conectare" este dezactivat
username = chrome.find_element(By.ID,"ShopLoginForm_Login")
username.clear()
username.send_keys('invalid_username')
time.sleep(5)
assert login_button.is_enabled()==False,"Error, login button is enabled"