# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# setam implicit wait in secunde
# selenium va cauta toate elementele timp de x secunde inainte sa dea eroare

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

first_name = WebDriverWait(chrome, 5).until(EC.presence_of_element_located((By.ID, "first-name")))
# first_name = chrome.find_element(By.ID,"first-names")
first_name.send_keys("test")
sleep(3)

"""

Diferenta intre explicit wait (WebDriverWait) si sleep este ca instructiunea de sleep va fi executata indiferent daca elementul
este gasit sau nu. Deci cu alte cuvinte, sistemul va astepta numarul de secunde definit in sleep in orice situatie

La explicit wait se va astepta numarul specificat de secunde doar daca elementul nu a fost gasit.
In caz contrar, instructiunea va fi executata instant. 

Exemplu:

Vrem sa cautam un element cu id-ul: last_name pe site-ul herrokuapp.com
sistemul va cauta acel element, si daca il va gasi, va trece instant la instructiunea urmatoare

Daca nu il gaseste, sistemul va continua sa il caute pe toata durata stabilita in implicit wait, dupa care va returna eroare
Daca nu am avea acel implicit wait, ar returna eroare instant.

-------------------------
Daca avem sleep inainte sau dupa element si elementul este gasit, atunci va astepta numarul de secunde definit in sleep 
            fie inainte de a cauta elementul fie dupa, depinzand unde este pozitionata instructiunea de sleep (rulare secventiala)
-------------------------        
Daca avem implicit wait si elementul este gasit, se va actiona asupra lui instant
Daca avem implicit wait si elementul nu este gasit, va returna eroare dupa numarul de secunde definit in implicit wait,
                atata timp cat instructiunea de implicit wait a fost pusa inaintea elementului in cauza
-------------------------                
Daca avem explicit wait pe elementul cautat si acesta este gasit, va fi actionat instant
Daca avem explicit wait pe elementul cautat si acesta nu este gasit va returna eroare dupa numarul de secunde definit in explicit wait
Daca avem explicit wait pe un alt element/elemente decat elementul cautat si acesta este gasit, va fi actionat instant
Daca avem explicit wait pe un alt element/elemente decat elementul cautat si acesta nu este gasit, va returna eroare instant


"""
chrome.implicitly_wait(2)

first_name = WebDriverWait(chrome, 20).until(EC.presence_of_element_located((By.ID, "first-name")))
first_name.send_keys("test")

# elem gasit
chrome.find_element(By.ID, 'first-name').send_keys('Gabriela')

# cauta elementul timp de 10 secunde
# last_name = chrome.find_element(By.ID,"last-names").send_keys("test_last_name")
last_name = WebDriverWait(chrome, 20).until(EC.presence_of_element_located((By.ID, "last-names")))
last_name.send_keys('S')


# https://www.geeksforgeeks.org/explicit-waits-in-selenium-python/