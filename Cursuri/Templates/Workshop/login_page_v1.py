# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from selenium import webdriver # program prin intermediul caruia vom avea acces la toate
                                    # functionalitatile de interactiune cu un browser
from selenium.webdriver.chrome.service import Service # program prin intermediul caruia
                                            # putem aduce un utilitar cu care putem lansa browserul
from selenium.webdriver.common.by import By # program care ne ajuta sa identificam
                                                    # elementele web in interfata unui website
from webdriver_manager.chrome import ChromeDriverManager # program ce ne ajuta sa pornim browserul
from time import sleep # program ce ne ajuta sa punem pauza in cod astfel incat
                                # sa putem vedea ce se intampla

# initializam chrome
s = Service(ChromeDriverManager().install()) # o modalitate prin care noi putem sa descarcam
                                                # driverul de browser din online
chrome = webdriver.Chrome(service=s) # o modalitate prin care noi putem sa deschidem browserul
                                            # adica programul pe care il rulam va gasi driver-ul care a fost descarcat
                                                # il va folosi pentru a lansa browserul iar serviciul de browser lansat
                                                # il va salva intr-o cutiuta numita chrome

chrome.maximize_window() # maximize_window() este o functie care are ca si rol
                                # marirea ferestrei browserului la dimensiune maxima
sleep(3)
chrome.get("https://the-internet.herokuapp.com/login")
sleep(3)

chrome.find_element(By.ID,"username").send_keys("tomsmith") #  linie de cod care identifica elementul
                                                                #  si da click pe el
sleep(3)
chrome.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
sleep(3)

chrome.find_element(By.XPATH,"//button[@type='submit']")
chrome.find_element(By.XPATH,"//form[@id='login']/button").click()
sleep(5)

"""
Modalitati de cautare
ID
XPATH = o adresa care identifica un element ca si pozitie fata de inceputul paginii web
ClassName
CSS Selector
Tag
Name
"""

# <input type="text" name="username" id="username"> - elementul pentru user copiat din browser
# id= cheie
# "username" = valoare
# <input type="password" name="password" id="password"> elementul pentru parola copiat din browser
# <button class="radius" type="submit"><i class="fa fa-2x fa-sign-in"> Login</i></button>
# /html/body/div[2]/div/div/form/button - XPATH ABSOLUT
# //button[@type="submit"] - XPATH relativ

# input = un element din browser in care putem sa introducem valori de la utilizator
# type="text" = o modalitate prin care sistemul a fost instruit ca acea casuta de input accepta text
# name="username" este o modalitate de identificare a elementului
# id="username" este o modalitate unica de identificare a elementului si una dintre cele mai folosite metode de identificare
                    # id="usernamea unui element in testarea automata

# 1. Ma voi asigura ca elementul meu este gasit prin modalitatea de identificare aleasa [id="username"]
# 2. Voi scrie linia de cod de identificare a elementului si de interactiune cu acel element

# selenium
# webdriver-manager









