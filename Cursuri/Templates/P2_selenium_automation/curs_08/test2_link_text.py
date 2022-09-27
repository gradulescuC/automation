# avem nevoie sa importam cateva librarii gratuite care ne ajuta sa controlam chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

# initializam chrome
s = Service(ChromeDriverManager().install())
chrome = webdriver.Chrome(service=s)

# maximizam fereastra
chrome.maximize_window()
# navigam catre un url
chrome.get('https://formy-project.herokuapp.com/')

sleep(3)

# selector by Link Text
chrome.find_element(By.LINK_TEXT,"Autocomplete").click()

 #cu metoda click apasam pe un buton, sau pe un link sau pe orice alt element pe care se poate apasa sa faca ceva

'''
<a class="btn btn-lg" href="/autocomplete">Autocomplete</a>
a = tag-ului de inceput al unui element de tip ancora
class = "btn btn-lg" -> o modalitate de a adauga ancora intr-o anumita categorie (de ex:categorie de formatare unde toate elementele din acea categorie vor urma acelasi aspect)
href="/autocomplete -> extensia care se va adauga la host
        https://formy-project.herokuapp.com/ -> host
        /autocomplete -> extensia adaugata la host
        https://formy-project.herokuapp.com/autocomplete -> linkul rezultat
Autocomplete -> textul care s-a afisat peste linkul nostru (link text)
/a -> tag-ul de final al elementului de tip ancora
'''
sleep(3)
chrome.quit() 
"""folosim metoda quit atunci cand vrem sa inchidem browserul complet - adica toate taburile deschise
                    daca vrem sa inchidem doar un anumit tab ne vom folosi de metoda close"""
