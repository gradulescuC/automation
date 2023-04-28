import time
from time import sleep

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
chrome.maximize_window()

# Navigam catre url
chrome.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
sleep(3)

""" 
    ------------- Ne logam in aplicatie (liniile 21 (insert username), 22 (insert password), 23 (click login button))----------------
    ------------- Dam click pe optiunea Time din meniul din stanga (linia 28) --------------------
    --- a se comenta liniile 24-31 dupa ce ati analizat codul si rezultatele) ----------------

"""
# chrome.find_element(By.CLASS_NAME, "oxd-input").send_keys("Admin")
# chrome.find_elements(By.CLASS_NAME, "oxd-input")[1].send_keys("admin123")
# chrome.find_element(By.CLASS_NAME, "oxd-button").click()


# Inspect: 'Time'
# sleep(5)
# chrome.find_element(By.LINK_TEXT, 'Time').click()


""" ---------------- Dam click pe linkul 'Forgot password' (a se comenta urmatoarul rand dupa ce ati analizat codul si rezultatele)----------------"""
# chrome.find_element(By.XPATH,'//div[@class="orangehrm-login-forgot"]').click()
# sleep(5)


""" 
    ----  Am deschis un link intr-un tab nou si ne-am mutat pe tab-ul nou deschis  ----------------


Pentru a putea naviga printre tab-urile deschise ne folosim de metoda window_handles
prima data vom defini o variabila care sa stocheze toate tab-urile deschise:

taburi_deschise = chrome.window_handles

prin intermediul metodei window_handles vom putea accesa toate tab-urile deschise
            unde window_handles[0] este primul tab din fereastra, iar pe masura ce navigam prin restul
            de tab-uri vom mari indexul corespunzator

"""

# print(chrome.title)  # am printat titlul paginii curente - va printa pe ecran "OrangeHRM", care e titlul paginii https://opensource-demo.orangehrmlive.com/web/index.php/auth/login
chrome.find_element(By.PARTIAL_LINK_TEXT, "OrangeHRM").click() # - dam click pe linkul "OrangeHRM, Inc" din partea de jos a ecranului
chrome.switch_to.window(chrome.window_handles[1])  # mutam focusul pe tab-ul care s-a deschis
# print(chrome.title) # printam din nou titlul paginii curente.
                            # De data asta va printa pe ecram "OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM"
                            # care este linkul paginii pe care ne-am mutat
                            # titlul paginii se poate gasi in HTML cu XPATH-ul: //title


""" ---------- Exercitiu: navigheaza prin tab-urile active, si atunci cand gasim primul tab 
                    care e diferit de cel initial, o sa ii extragem titlul si verificam daca
                    este cel asteptat
Pentru asta am stocat toate tab-urile din fereastra deschisa intr-o lista numita chwd: chwd = chrome.window_handles

"""
# am parcurs lista chwd cu un for in care range-ul este dat de lungimea listei de tab-uri
chwd = chrome.window_handles
current_window = chrome.current_window_handle # am stocat in variabila current_window tab-ul in care avem focusul
for window_index in range(len(chwd)): # range-ul for-ului este dat de lungimea listei de tab-uri.
                                        # in variabila de iteratie stocam indexul tab-ului curent
    chrome.switch_to.window(chwd[window_index]) # facem switch catre urmatorul tab din lista
    if chwd[window_index] != current_window: # daca tab-ul din iteratia curenta nu este egal cu tab-ul de la care am plecat
                                                # inseamna ca switch-ul s-a facut cu succes
        actual_title = chrome.title # extragem titlul curent al paginii
        assert 'OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM'  == actual_title , f"Expected title: 'OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM', actual title: {actual_title}"
        # la assertul de mai sus verificam daca titlul paginii curente este corect

"""

-------- Ce se intampla atunci cand avem mai mult de doua tab-uri deschise si nu stim exact
            al catalea e cel de care avem nevoie?
         In cazul asta putem sa facem evaluare dupa titlul paginii ---------------
         
         
"""


expected_title = 'OrangeHRM HR Software | Free & Open Source HR Software | HRMS | HRIS | OrangeHRM' # definim titlul care ne intereseaza
for window_index in range(len(chwd)): # am parcurs lista chwd cu un for la fel ca mai sus. range-ul for-ului este dat de lungimea listei de tab-uri
    if chrome.title == expected_title: # daca am gasit tab-ul care ne intereseaza
        print(f"Titlul s-a extras cu succes si este {chrome.title}") # printam titlul acestia pe ecran
        break # si iesim din for
    chrome.switch_to.window(chwd[window_index])  # atata timp cat nu am iesit din for facem switch catre urmatorul tab din lista

""" ------------Fiind pe noul tab deschis, inchidem bannerul de cookies ca sa nu ne acopere elementele -----------"""
try:
    sleep(10)
    accept_cookies_button = chrome.find_element(By.XPATH,'//a[@title="Accept Cookies"]')
    accept_cookies_button.click()
except:
    pass

""" ---------------
                Elementul identificat dupa link textul cautat este plasat foarte jos
                in pagina si drept urmare nu este accesibil pentru click chiar daca e gasit,
                asa ca o sa trebuiasca sa ne mutam pe acel element in mod explicit
                
                ------------
                
                """
i = 0
while i < 10: # vom face 10 iteratii de scroll
        # ne mutam in jos 500 pixeli
        chrome.execute_script("window.scrollBy(0, 500)", "")
        # incercam sa gasim elementul cu link textul "Our Offices"
        # am asteptat pana cand a devenit clickable
        # am pus intr-un try pentru ca vreau ca daca nu il gaseste sa mearga mai departe sa mai faca scroll inca o data
        try:
            element = WebDriverWait(chrome, 20).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "Our Offices")))
            element.click()
            break
        except:
            pass
        # asteptam 0.5 milisecunde inainte sa mergem mai departe
        time.sleep(0.5)
        i += 1

# chiar daca am mai definit o data lista chwd la linia 70, va trebui sa o redefinim ca sa recalculam
        # numarul de tab-uri deschise in urma deschiderii celui de-al treilea tab dupa instructiunea de la
                # linia 123
        # inainte de instructiunea de la linia 123 numarul de tab-uri deschise este de 2, drept urmare
                # lista noastra are tot doua elemente
        # in urma urmatoarei instructiuni suprascriem lista astfel incat sa ia in considerare si al treilea tab

chwd = chrome.window_handles

"""  
    ---------   
        While-ul de mai jos e facut strict in scopul de a putea sa analizati cum functioneaza window_hanles
        Va recomand sa puneti breakpointuri la fiecare linie si sa rulati cu debug, uitandu-va in acelasi timp 
        si in browser, mai ales dupa instructiunea cu switch. 
        
        While-ul nu se va termina niciodata decat daca il opriti voi (l-am pus asa intentionat
        ca sa vedeti ce se intampla la switch)
        
"""
i = 0 # am initializat o variabila de iteratie cu valoarea 0
while True: # am pus o conditie care se va indeplini mereu ca sa nu iasa in mod automat din while, sa aveti ocazia sa vedeti ce se intampla
    chrome.switch_to.window(chwd[i]) # am facut switch la fereastra din iteratia curenta. Prima data la fereastra de la indexul 0 asa cum a fost initializata variabila de iteratie
    i += 1 # marim valoarea indexului cu 1 ca sa se faca evaluarea lui inainte de a intra in if, ca sa nu ne dea index out of range exception (sa incerce sa acceseze un tab care nu exista)
    if i >=len(chwd): # daca am ajuns cu indexul la valoarea lungimii listei (tineti minte ca ultimul element din lista se afla la pozitia len(chwd)-1, si accesarea elementului din pozitia len(chwd) va returna list index out of range)
        i = 0 # vom reseta contorul la 0 si o vom lua de la capat. Observati cum la urmatoarea iteratie dupa instructiunea asta se va muta din nou pe primul tab cu pagina de login

