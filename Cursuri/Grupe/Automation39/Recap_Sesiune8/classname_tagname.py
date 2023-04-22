from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())

# cu metoda get putem sa deschidem un site
chrome.get("https://www.elefant.ro/")
chrome.maximize_window()
sleep(3)
try:
		accept_cookies_button = chrome.find_element(By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
		accept_cookies_button.click()
		assert accept_cookies_button.text == "ACCEPT"
except:
		pass

# Vreau sa fac un test prin care evaluez ca pot sa caut produse pe site
# Atunci cand gasim un element cu o clasa care contine spatii de fapt avem de a face cu mai multe clase
# fiecare spatiu nou delimiteaza urmatoarea clasa
# in cazul de mai jos avem de a face cu trei clase diferite
# atunci cand facem cautare dupa clasa trebuie OBLIGATORIU sa folosim doar pe una din ele NU PE TOATE
# chrome.find_element(By.CLASS_NAME,"form-control searchTerm js-has-overlay").send_keys("de veghe in lanul de secara") # instructiunea asta va returna eroare: unable to locate element
# Atentie!!! cautarea in HTML se va face dupa toate clasele sub format cheie valoare: [class="form-control searchTerm js-has-overlay"]

# Numele unei clase NU TREBUIE sa aiba spatii

# metoda send_keys scrie text intr-un textbox
# metoda click da click pe un element(link, buton etc)
# metoda find_element returneaza un singur element. Daca nu il gaseste returneaza eroare
chrome.find_element(By.CLASS_NAME,"form-control").send_keys("de veghe in lanul de secara")
sleep(4)
chrome.find_element(By.CLASS_NAME,"search-result").click()
# metoda find_elements returneaza o lista de elemente. Daca nu gaseste niciunul returneaza o lista goala
lista_carti = chrome.find_elements(By.CLASS_NAME,"product-tile")

# am scos valoarea de pe atributul data-sku si am evaluat ca aceasta valoare este corecta
# assert lista_carti[0].get_attribute("data-sku") == "6330a449-0efc-4897-9df6-12b29828a81f"
sleep(2)

# Cautare dupa tag name

"""
Exemple de tag-uri:
a) <a href="link catre care navigam">text care este pus peste link</a> -> a este prescurtarea de la ancora si este o legatura catre o alta pagina (link)
b) <p></p> -> prescurtarea de la paragraf
c) <span></span> -> de regula e folosit pentru stilizari (gen culoare, font, dimensiune scris, aliniere in pagina)
d) <div></div> -> este folosit pentru blocuri care definesc un singur element
"""

lista_elemente_identificate_prin_tag = chrome.find_elements(By.TAG_NAME,"div")
print(len(lista_elemente_identificate_prin_tag))