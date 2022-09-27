# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()

# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/form')

# selector by Class - ia primul tot tp. - e ok doar daca avem clasa unica
chrome.find_element(By.CLASS_NAME, 'form-control').send_keys('Test')
# Pentru a putea face cautare de tip atribut = valoare in html, trebuie sa punem metoda de cautare intre paranteze patrate. Exemplu: [class="form-control"]

# ATENTIE: Daca un elementnt are clasa compusa (adica doua clase consecutive separate prin spatiu) cautarea se va face doar dupa una dintre ele
# Exemplu: daca avem un element de tip div cu proprietatea class="col-sm-8 col-sm-offset-2",
#             atunci cautarea se va face in felul urmator: chrome.find_element(By.CLASS_NAME, 'col-sm-8')
#                                                           chrome.find_element(By.CLASS_NAME, 'col-sm-offset-2')
#                                                           chrome.find_element(By.CLASS_NAME, 'col-sm-8 col-sm-offset-2') -> metoda asta de cautare ar fi returnat eroare pentru ca nu gaseste elementul

years_of_experience = Select(chrome.find_element(By.ID,"select-menu"))
sleep(2)
years_of_experience.select_by_visible_text("2-4")
sleep(3)

# # gasim mai multe si punem in lista
lista_elemente = chrome.find_elements(By.CLASS_NAME, 'form-control')
print(len(lista_elemente))
lista_elemente[4].send_keys("09/22/2022")
# lista_elemente[1].send_keys("test1")
# lista_elemente_clasa = chrome.find_elements(By.CLASS_NAME, 'form-control') -> Acelasi lucru, varianta mai lunga
# lista_elemente_clasa[1].send_keys('Test1')
# <a class="btn btn-lg btn-primary" role="button" href="/thanks">Submit</a>

chrome.find_element(By.CLASS_NAME,"btn").click()
sleep(3)


chrome.quit()