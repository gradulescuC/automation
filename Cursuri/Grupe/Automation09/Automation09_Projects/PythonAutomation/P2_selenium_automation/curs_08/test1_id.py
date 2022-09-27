"""

cod pentru exemplificare identificare dupa id

"""

# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install()) # Stocam serviciul de chrome
chrome = webdriver.Chrome(service=s) # definirea unei variabile care va stoca driverul de chrome

# maximizam fereastra
chrome.maximize_window() # este o metoda folosita pentru maximizarea browserului

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form') # metoda get este o metoda prin care putem naviga la un anumit link

# selector by ID
first_name = chrome.find_element(By.ID, 'first-name') # metoda find_element este o metoda prin care putem sa cautam un element in codul de html pe baza de diversi identificatori
first_name.send_keys('Ala Bala Portocala') # metoda send_keys este o metoda care scrie ceva intr-un camp din browser

sleep(3) # folosim metoda sleep ca sa putem sa instruim sistemul sa astepte putin inainte sa inchida sa mearga mai departe

chrome.quit() # quit este o metoda care este folosita pentru a inchide browserul