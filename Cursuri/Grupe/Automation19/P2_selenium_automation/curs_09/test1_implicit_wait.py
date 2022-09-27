from time import sleep
from selenium import webdriver  # pachet care contine toate functiile si variabilele utile pentru interactiunea cu browserul
from selenium.webdriver.chrome.service import Service # clasa care contine instanta de driver, elemente care sunt utile la instantierea driverului
from webdriver_manager.chrome import ChromeDriverManager # clasa care contine toate functiile si atributele utile pentru lansarea driverului
from selenium.webdriver.common.by import By # librarie ce contine toate actiunile care se pot face in raport cu cautarea unui element

# initializam chrome
s = Service(ChromeDriverManager().install())  # momentul in care noi instalam toate pachetele necesare la run-time pentru rularea driver ului
chrome = webdriver.Chrome(service=s) # lansam broser ul de chrome si il salvam intr-o variabila al carei nume este optional

# maximizam fereastra
chrome.maximize_window() # am maximizat fereastra pentru a ne asigura ca toate elementele sunt vizibile pe site

# setam implicit wait in secunde - o modalitate prin care putem defini un timp global de asteptare
                    # pana cand sa dea eroare in momentul in care un element nu este gasit
                    # se va instantia in momentul in care va fi executata instructiunea
                            # si va fi distrus in momentul in care executia se incheie si browserul este inchis

# selenium va cauta toate elementele timp de x secunde inainte sa dea eroare

# Diferenta intre implicit wait si sleep este ca instructiunea de sleep va fi executata intotdeauna, deci sistemul va
        # astepta numarul de secunde  definit in sleep de fiecare data cand va gasi o instructiune de sleep
        # noi va trebui sa punem o instructiune de sleep de fiecare data cand vrem ca sistemul sa astepte o anumita
        # perioada de timp. Drept urmare, va trebui scris mai multe linii de cod, facand programul mai greu de citit
#  Pe de alta parte, timpul definit intr-un implicit wait va fi asteptat doar daca elementul nu este gasit
        #  si va functiona in felul urmator:
        # daca avem un implicit wait de 6 secunde, si elementul este gasit dupa 3 secunde, atunci se va merge mai
        # departe dupa 3 secunde
        # daca elementul nu este gasit deloc, se va astepta 6 secunde si apoi se va returna eroare
        # implicit wait va fi scris o singura data, si va fi valabil pe toata durata executiei, drept urmare va presupune
                #mai putin cod scris, si drept urmare un program mai usor de citit


"""
Exemplu:

Vrem sa cautam un element cu id-ul: last_name pe site-ul herrokuapp.com
sistemul va cauta acel element, si daca il va gasi, va trece instant la instructiunea urmatoare

Daca nu il gaseste, sistemul va continua sa il caute pe toata durata stabilita in implicit wait, dupa care va returna eroare
Daca nu am avea acel implicit wait, ar returna eroare instant

"""

chrome.implicitly_wait(6)

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# elem gasit
chrome.find_element(By.ID, 'first-names').send_keys('Gabriela')

# id e invalid => NoSuchElementException
chrome.find_element(By.ID, 'last-name').send_keys('Radulescu')

sleep(3)
# de citit
# https://www.geeksforgeeks.org/implicit-waits-in-selenium-python/