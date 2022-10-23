# TEMA 8 - SELECTORS

# Exercitii OBLIGATORII

# Importarea librariilor necesare pentru a controla Chrome
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

"""
Exercitiul 1.
Alege câte 3 elemente din fiecare tip de selector din următoarele categorii:
    ● Id
    ● Link text
    ● Parțial link text
    ● Name
    ● Tag*
    ● Class name*
    ● Css (1 după id, 1 după clasă, 1 după atribut=valoare_partiala)
Observație:
    - Probabil nu vei găsi un singur website care să cuprindă toate variantele
    de mai sus, astfel că îți recomandăm să folosești mai multe site-uri
    - Opțional: La tag și class name vei folosi find elementS! - salvează în listă.
    Interactionează cu un element la alegere din listă.
Pentru xpath identifică elemente după criteriile de mai jos:
    ● 3 după atribut valoare
    ● 3 după textul de pe element
    ● 1 după parțial text
    ● 1 cu SAU, folosind pipe |
    ● 1 cu *
    ● 1 în care le iei ca pe o listă de xpath și în python ajunge 1 element, deci   
      cu (xpath)[1]
    ● 1 în care să folosești parent::
    ● 1 în care să folosești fratele anterior sau de după (la alegere)
    ● 1 funcție ca și cea de la clasă prin care să pot alege eu prin parametru cu
      ce element vreau să interacționez.
"""
# initializare chrome
s = Service(ChromeDriverManager().install()) # Stocam serviciul de chrome
chrome = webdriver.Chrome(service=s) # definirea unei variabile care va stoca driverul de chrome

# maximizare fereastra
chrome.maximize_window() # este o metoda folosita pentru maximizarea browserului

"""
SITE: http://automationpractice.com/index.php
"""
# navigare catre un url
chrome.get('http://automationpractice.com/index.php?controller=contact')
# metoda get este o metoda prin care se poate naviga la un anumit link


"""
Selector by ID
"""
# Primul element
# <input class="form-control grey validate" type="text" id="email" name="from" data-validate="isEmail" value="" pwa2-uuid="EDITOR/input-7DD-0C5-14F79-094" pwa-fake-editor="">

chrome.find_element(By.ID,"email").send_keys('domutandreea@yahoo.com')
sleep(3)  # sleep este o metoda prin care putem sa punem pauza codului
          # cu alte cuvinte instruim sistemul sa astepte 3 secunde inainte sa execute urmatoarea instructiune

# Al doilea element
# <input class="form-control grey" type="text" name="id_order" id="id_order" value="" pwa2-uuid="EDITOR/input-38D-142-882D8-B84" pwa-fake-editor="">chrome.find_element(By.ID,"autocomplete2").send_keys('Franta')

chrome.find_element(By.ID,"id_order").send_keys('1234')
sleep(3)

# Al treilea element
#<textarea class="form-control" id="message" name="message" pwa2-uuid="EDITOR-128-F87-8FA9F-DE5" pwa-fake-editor="" spellcheck="false" style="position: relative; background: none !important; line-height: 18.5714px;"></textarea>

chrome.find_element(By.ID,"message").send_keys('Buna! Am o problema.')
sleep(3)

"""
Selector by LINK TEXT
"""
# Primul element
# <a href="http://automationpractice.com/index.php?id_category=3&amp;controller=category" title="Women" class="sf-with-ul">Women</a>

chrome.find_element(By.LINK_TEXT, "Women").click()
sleep(3)

# Al doilea element
# <a href="http://automationpractice.com/index.php?id_category=8&amp;controller=category" title="Find your favorites dresses from our wide choice of evening, casual or summer dresses!
#  We offer dresses for every day, every style and every occasion.">
# 		Dresses
# 	</a>

chrome.find_element(By.LINK_TEXT, "Dresses").click()
sleep(3)

# Al treilea element
# <a href="http://automationpractice.com/index.php?id_category=9&amp;controller=category" title="You are looking for a dress for every day? Take a look at
#  our selection of dresses to find one that suits you.">
# 		Casual Dresses
# 	</a>

chrome.find_element(By.LINK_TEXT, "Casual Dresses").click()
sleep(3)

""" 
Selector by PARTIAL LINK TEXT
"""
# Primul element
#<a href="http://automationpractice.com/index.php?id_category=9&amp;controller=category#styles-girly">Cotton<span> (1)</span></a>

chrome.find_element(By.PARTIAL_LINK_TEXT, "Cott").click()
sleep(3)

# Al doilea element
# <a href="http://automationpractice.com/index.php?id_category=9&amp;controller=category#properties-colorful_dress">Colorful Dress<span> (1)</span></a>

chrome.find_element(By.PARTIAL_LINK_TEXT, "Colorful").click()
sleep(3)

""" 
Selector by NAME
"""
# Primul element
# <input class="search_query form-control ac_input" type="text" id="search_query_top" name="search_query" placeholder="Search" value="" autocomplete="off" pwa2-uuid="EDITOR/input-98D-F26-67F46-4F4" pwa-fake-editor="">

chrome.find_element(By.NAME, "search_query").send_keys("evening dresses")
sleep(3)

# Al doilea element
# <button type="submit" name="submit_search" class="btn btn-default button-search">
# 			<span>Search</span>
# 		</button>

chrome.find_element(By.NAME, "submit_search").click()
sleep(3)

# Al treilea element
#<input class="inputNew form-control grey newsletter-input" id="newsletter-input" type="text" name="email" size="18" value="Enter your e-mail" pwa2-uuid="EDITOR/input-377-99B-0899D-1E7" pwa-fake-editor="">

chrome.find_element(By.NAME, "email").send_keys("domutandreea@yahoo.com")
sleep(3)
# <button type="submit" name="submitNewsletter" class="btn btn-default button button-small">
#                     <span>Ok</span>
#                 </button>

chrome.find_element(By.NAME, "submitNewsletter").click()
sleep(3)

chrome.quit() # quit este o metoda care este folosita pentru a inchide browserul

