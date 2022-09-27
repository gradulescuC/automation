# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

# initializam chrome
s = Service(ChromeDriverManager().install())  # initializam serviciul de Chrome (browserul este descarcat automat de pe net)
chrome = webdriver.Chrome(service=s) # am deschis browserul si l-am pus intr-o cutiuta numita chrome

# maximizam fereastra
chrome.maximize_window() #  Am maximizat fereastra astfel incat sa putem vedea corect toate elementele

# navigam catre un url
chrome.get('https://the-internet.herokuapp.com/login') # Am deschis site-ul pe care vrem sa il testam
chrome.find_element(By.ID,"username").send_keys("tomsmith")
sleep(2)
chrome.find_element(By.ID,"password").send_keys("SuperSecretPassword!")
sleep(2)
chrome.find_element(By.XPATH,"//*[@id='login']/button").click()

# cu sleep putem pune pauza de cateva secunde sa asteptam sa vedem si noi ceva
sleep(8)


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

# input = uun element din browser in care putem sa introducem valori de la utilizator
# type="text" =  o modalitate prin care sistemul a fost instruit ca acea casuta de input accepta text
# name="username" = este o modalitate de identificare a elementului
# id="username" = id-ul este o modalitate unica de identificare a elementului si una dintre cele mai folosite metode de identificare
#                     a unui element in testarea automata


# /html/body/div[2]/div/div/form/button - XPATH ABSOLUT
# //button[@type="submit"] - XPATH relativ


# Pasi pentru a interactiona cu un element
# 1. Ma voi asigura ca elementul meu este gasit prin modalitatea de identificare aleasa [id="username"]
# 2. Voi scrie linia de cod de identificare a elementului si de interactiune cu acel element

# Programe de instalat (din tab-ul Python Packages din partea de jos a pycharm-ului)
# selenium
# webdriver-manager
