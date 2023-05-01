from time import sleep
import unittest

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC

class Elefant_Login(unittest.TestCase):

		# Am definit o constanta care sa stocheze valoarea de cautare a selectorului elementului
					# pe care il cautam
		# in situatia in care va fi necesara o schimbare a selectorului, putem sa facem schimbarea
					# o singura data si sa se propage peste tot pe unde se face referire la constanta
					# care stocheaza valoarea de cautare a selectorului
		CONNECT_BUTTON = (By.CLASS_NAME,"my-account-link")
		COOKIE_ACCEPT_BUTTON = (By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
		CONNECT_BUTTON_MODAL = (By.XPATH,'//div[@id="account-layer"]//a[contains(text(),"Conectare")]')
		USERNAME = (By.ID,"ShopLoginForm_Login")
		PASSWORD = (By.ID,"ShopLoginForm_Password")
		LOGIN_BUTTON = (By.XPATH,'//button[@value="Login"]')

		def setUp(self) -> None:
				# am pus self in fata obiectului chrome instantiat din clasa Chrome ca sa il marcam
					# ca fiind atribut al clasei si pentru a ii extinde vizibilitatea la toate metodele
				  # definite in acea clasa
				self.chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
				self.chrome.get("https://www.elefant.ro/")
				self.chrome.maximize_window()
				sleep(3)
				accept_cookies_button = self.chrome.find_element(By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
				accept_cookies_button.click()

		def tearDown(self) -> None:
				self.chrome.quit()

		def test_login_to_site_invalid_credentials(self):
				self.chrome.find_element(*self.CONNECT_BUTTON).click()
				sleep(3)
				connect_button = self.chrome.find_element(*self.CONNECT_BUTTON_MODAL)
				# mai jos am folosit clasa ActionChains ca sa putem sa interactionam cu un element de tip context menu
				# cu care nu putem interactiona asa cum o facem cu elementele standard
				ActionChains(self.chrome).move_to_element(connect_button).click(connect_button).perform() # https://www.geeksforgeeks.org/action-chains-in-selenium-python/
				self.chrome.find_element(*self.USERNAME).send_keys("test@gmail.com")
				self.chrome.find_element(*self.PASSWORD).send_keys("testpassword")
				self.chrome.find_element(*self.LOGIN_BUTTON).click()
				# metoda 1 de verificare a faptului ca nu ne-am logat -> prin intermediul url-ului
				expected_url = "https://www.elefant.ro/INTERSHOP/web/WFS/elefant-elefantRO-Site/ro_RO/-/RON/ViewUserAccount-ProcessLogin"
				actual_url = self.chrome.current_url
				assert expected_url == actual_url,"Error: The URL has changed. Maybe you should check the login functionality"

				# metoda 2 de verificare a faptului ca nu ne-am logat -> prin intermediul butonului de logare -> isDisplayed

				# ATENTIE!!! metoda isDisplayed verifica daca elementul este pe pagina, insa nu este vizibil utilizatorului final
										 # daca elementul nu exista pe pagina, metoda NU VA RETURNA FALSE, ci cautarea ca returna eroare: unable to locate element
				assert self.chrome.find_element(*self.LOGIN_BUTTON).is_displayed()

				# Nota: Exista si metoda isEnabled() care verifica daca un element este activ pe pagina

"""
Caracterul * despacheteaza tuplul in care este salvat selectorul

Exemplu:
self.chrome.find_element(*self.COOKIE_ACCEPT_BUTTON) => self.chrome.find_element(By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll") 
self.chrome.find_element(self.COOKIE_ACCEPT_BUTTON) => self.chrome.find_element((By.ID,"CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")) 
"""