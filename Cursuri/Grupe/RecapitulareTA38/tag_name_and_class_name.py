import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
chrome.get("https://the-internet.herokuapp.com/")
# print(chrome.find_element(By.LINK_TEXT,"Form Authentication"))
chrome.find_element(By.LINK_TEXT,"Form Authentication").click()
lista_inputuri = chrome.find_elements(By.TAG_NAME,"input")

"""
Exista doua metode de cautare a elementelor in interfata:
1. find_element -> cauta un singur element
										daca il gaseste il returneaza.
										daca gaseste mai multe elemente care respecta criteriul il returneaza pe primul
										daca nu gaseste niciun element care respecta criteriul returneaza eroare
2. find_elements -> cauta toate elementele care respecta criteriul 
										daca gaseste un singur element returneaza o lista cu un singur element
										daca gaseste mai multe elemente care respecta criteriul returneaza o lista in care fiecare element 
														ocupa o pozitie specifica in lista in functie de ordinea in care au fost identificate
										daca nu gaseste niciun element care respecta criteriul returneaza eroare returneaza o lista goala (NU RETURNEAZA EROARE)
"""

# lista_inputuri[0].send_keys("tomsmith")
# lista_inputuri[1].send_keys("SuperSecretPassword!")
for i in range(len(lista_inputuri)):
		if lista_inputuri[i].get_attribute("name")=="username":
				lista_inputuri[i].send_keys("tomsmith")
				print("username")
		else:
				lista_inputuri[i].send_keys("SuperSecretPassword!")
				print("password")

"""
In elementele de tip HTML putem sa avem mai multe proprietati
		sub forma atribut=valoare
		Daca vrem sa extragem pentru filtrare valoarea de pe un anumit
			atribut putem sa folosim metoda get_attribute
		exemplu: avem doua input-uri cu type = "text" si un intput cu type = "checkbox"
						daca vrem sa extragem doar inputurile cu type= "text"
						atunci o sa extragem atributul type de pe toate elementele de tip input
						si o sa verificam daca au typul text (type = "text")
						Daca da, atunci o sa se returneze elementul, in caz contrar elementul nu va fi gasit
						
Headerele reprezinta niste sectiuni de scris care pot avea diverse dimensiuni in functie de necesitati
					in felul urmator:
					h1 -> scrisul cel mai mare
					h2 -> urmatorul ca dimensiune dupa h1
					h3 -> urmatorul ca dimensiune dupa h2
					h4 -> urmatorul ca dimensiune dupa h3
					h5 -> urmatorul ca dimensiune dupa h4
					h6 -> scrisul cel mai mic de tip header
					
Title reprezinta titlul paginii si este cel care este reflectat in numele tab-ului

debug = o activitate facuta in general de catre echipa de dezvoltare pentru a a identifica
				sursa unui defect in cod si pentru a putea gasi o solutie
				debug-ul in general se face pentru a pune pauza in cod, astfel incat sa putem vedea
					cum circula informatiile si pentru a putea intelege mai bine felul in care acestea sunt procesate
"""

print(chrome.title)
chrome.find_element(By.CLASS_NAME,"radius").click()
chrome.find_element(By.LINK_TEXT,"Logout").click()
# chrome.find_element(By.XPATH,'//a[@href="/logout"]') -> alta metoda de cautare pe baza de XPATH
current_url = chrome.current_url
expected_url = "https://the-internet.herokuapp.com"
assert expected_url == current_url, f"Error, the URL is not correct. Logout was not successful! Current url is: {current_url}"
time.sleep(3)
chrome.quit()

"""
Daca avem o clasa care contine spatiu, de fapt avem doua clase.
Cand facem cautare dupa class name, vom face cautare ori dupa una ori dupa cealalta, niciodata dupa ambele
chrome.find_element(By.CLASS_NAME,"class='large-12'"
chrome.find_element(By.CLASS_NAME,"class='columns'"
"""