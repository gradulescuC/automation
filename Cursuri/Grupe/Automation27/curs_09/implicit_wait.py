from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
chrome = webdriver.Chrome(executable_path= ChromeDriverManager().install())
chrome.implicitly_wait(10)
"""
sleep = metoda prin care punem pauza in cod timp de o perioada bine definita care va fi respectata ad-literam de catre sistem
implicitly_wait() = metoda prin care sistemul va cauta un element timp de o perioada determinata
										daca elementul este gasit mai devreme, atunci va executa urmatoarea instructiune fara sa mai astepte
										daca elementul nu este gasit pana cand tipul alocat expira, atunci sistemul va returna eroare
										Este util in conceptul de RANDARE a paginii - uneori paginile web se pot incarca mai greu
														ceea ce inseamna ca unele elemente nu vor fi vizibile imediat
										Implicit wait este global si va acoperi orice element scris in fisierul curent
"""
chrome.get("https://the-internet.herokuapp.com/login")
chrome.find_element(By.ID,"username").send_keys("tomsmith")
# time.sleep(10)
chrome.find_element(By.ID,"passwords").send_keys("SuperSecretPassword!")
# chrome.find_element(By.CLASS_NAME,'radius').click()
chrome.find_element(By.XPATH,'//button[@class="radius" and @type="submit"]').click()
chrome.quit()