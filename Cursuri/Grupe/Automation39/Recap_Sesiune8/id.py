
# daca va merge fara acest executable_path puteti sa nu il folositi. Dupa python 4.6 ar trebui sa nu mai fie necesar
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# cu metoda get putem sa deschidem un site
chrome.get("https://www.elefant.ro/")
sleep(3)

# Atunci cand vrem sa interactionam cu un element, primul pas este sa dam click dreapta
# pe el si sa apasam pe butonul de inspect
# automat codul care a definit acel element va fi colorat diferit fata de restul codului (de regula cu albastru)

# Varianta 1 de interctiune cu elementul
# chrome.find_element(By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()

# Varianta 2 de interctiune cu elementul prin definirea unei variabile in care sa stochez elementul
# Am pus instructiunile de gasire a elementului si click pentru situatia in care butonul de cookies nu apare mereu pe pagina

try:
		accept_cookies_button = chrome.find_element(By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
		accept_cookies_button.click()
		assert accept_cookies_button.text == "ACCEPT"
except:
		pass

# eroarea pentru instructiunea de mai jos apare pentru ca variabila accept_cookies_button e vizibila doar in blocul de cod try except
# print(accept_cookies_button.text)

# metoda quit inchide instanta de browser
chrome.quit()

# metoda close inchide doar tab-ul activ din browser
# chrome.close()