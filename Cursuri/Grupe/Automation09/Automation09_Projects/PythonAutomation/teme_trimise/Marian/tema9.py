import unittest
from time import sleep

from bs4 import element
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Implementati o clasa Login care sa mosteneasca unittest.TestCase
class Login(unittest.TestCase):
# Gasiti elementele in partea de sus folosind ce selectors doriti voi
#
    h1 = (By.XPATH,'//*[@id="content"]/h1')
    h2= (By.XPATH, '//*[@id="content"]/h2')
    login_button= (By.XPATH,'/html/body/div[2]/div/div/form/button/i')
    element_selenium= (By.XPATH,'//*[@id="page-footer"]/div/div/a')
    error_login = (By.XPATH,'//*[@id="flash"]')


# setUp()
#  Driver
# https://the-internet.herokuapp.com/
    def setUp(self):
        self.s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=self.s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        #self.chrome.find_element(By.CLASS_NAME,'heading')

    def tearDown(self):
        self.chrome.quite

#
# Click pe Form Authentication
    def test_clic(self):
        self.chrome.find_element(By.XPATH,'//*[@id="content"]/ul/li[3]/a').click()

# tearDown()
# # Quit browser
    def tearDown(self):
        self.chrome.quit()

# Test1
#
# Verificati ca noul url e corect
#     def test_URL(self):
#         actual = self.chrome.current_url
#         expect = 'https://the-internet.herokuapp.com/'
#         self.assertEqual(expect, actual, 'URL is incorect')
#
#
# # Test2
# # Verificati ca page title e corect
#     def test_page_title(self):
#         actual= self.chrome.title                                     ####Nu merge...cred ca nu stiu eu de unde sa iau denumirea de titulu
#         print(f'Title is {actual}')                                      # am gasit in html ca titlu este 'the internet' dar nu trebuie sa apara si pe pagina?
#         expect = 'Welcome to the-internet'
#         self.assertEqual(expect,actual,'Page title is incorect')


# Test3
# Verificati textul de pe elementul xpath=//h2 e corect
#     def test_h2(self):
#         actual = self.chrome.find_element(*self.h2).text
#         expect = 'Available Examples'
#         self.assertEqual(actual,expect, 'Text is incorect')
#
# # Test4
# # Verificati ca butonul de login este displayed
#     def test_login_button(self):
#         self.chrome.get('https://the-internet.herokuapp.com/login')
#         button = self.chrome.find_element(*self.login_button)                        #### daca nu ii spun sa caute pe site la sectiunea Login atunci
#         self.assertTrue(button.is_displayed(),'Button is not displayed')             ###       nu gaseste butonul
#
# # Test5
# # Verificati ca atributul href al linkului ‘Elemental Selenium’ e corect
#     def test_atribut_href(self):
#         actual = self.chrome.find_element(*self.element_selenium).get_attribute('href')
#         expected = 'http://elementalselenium.com/'
#         self.assertEqual(actual,expected,'Href attribute is wrong ')
#
# # Test6
# # Lasati goale user si pass
# # Click login
# # Verifica ca eroarea e displayed
#
#     def test_clik_login(self):
#         self.chrome.get('https://the-internet.herokuapp.com/login')
#         self.chrome.find_element(By.XPATH,'//*[@id="login"]/button/i').click()
#         error = self.chrome.find_element(*self.error_login)
#         self.assertTrue(error.is_displayed(), 'Error is not displayed')
#
# #
# # Test7
# # Completeaza cu user si pass invalide
#     def test_user_pass(self):
#         self.chrome.get('https://the-internet.herokuapp.com/login')
#         self.chrome.find_element(By.XPATH,'//*[@id="username"]').send_keys('Marian')
#         self.chrome.find_element(By.XPATH,'//*[@id="password"]').send_keys('mypassword')
# # Click login
#         self.chrome.find_element(By.XPATH,'//*[@id="login"]/button/i').click()
#         sleep(1)
# # Verifica ca mesajul de pe eroare e corect
# # Este si un x pus acolo extra asa ca vom folosi solutia de mai jos
#         expected = 'Your username is invalid!'
#         actual = self.chrome.find_element(*self.error_login).text
#         self.assertTrue(expected in actual, 'Error message text is incorrect')
#
# # Test8
# # Lasati goale user si pass
# # Click login
#     def test_click_error(self):
#         self.chrome.get('https://the-internet.herokuapp.com/login')
#         self.chrome.find_element(By.XPATH,'//*[@id="login"]/button/i').click()
# # Apasa x la eroare
#         self.chrome.find_element(By.XPATH,'//*[@id="flash"]/a').click()
# # Verifica ca eroarea a disparut
#         error = self.chrome.find_element(*self.error_login)
#         self.assertTrue(error.is_displayed(),'Erros is not displayed')
#
#
# # Test9
# # Aici e ok sa avem 2 asserturi
#
# # Ia ca o lista toate //label
#     def test_user_pass_txt(self):
#         self.chrome.get('https://the-internet.herokuapp.com/login')
#         list = self.chrome.find_elements(By.XPATH,'//label')
#      # Verifica textul ca textul de pe ele sa fie cel asteptat (Username si Password)
#         user = 'Username'
#         pas = 'Passowrd'
#         self.assertTrue(list,user)
#         self.assertTrue(list,pas)

# Test10
# Completeaza cu user si pass valide
    def test_user_pass_v1(self):
        self.chrome.get('https://the-internet.herokuapp.com/login')
        self.chrome.find_element(By.XPATH,'//*[@id="username"]').send_keys('tomsmith')
        self.chrome.find_element(By.XPATH,'//*[@id="password"]').send_keys('SuperSecretPassword!')
# Click login
        self.chrome.find_element(By.XPATH,'//*[@id="login"]/button/i').click()

# Verifica ca noul url CONTINE /secure
        new_url = self.chrome.current_url
        self.assertTrue('/secure'in new_url)
# Foloseste un explicit wait pentru elementul cu clasa ’flash succes’
# Verifica ca elementul cu clasa=’flash succes’ este displayed
        element = WebDriverWait(self.chrome, 8).until(EC.presence_of_element_located((By.CLASS_NAME,'flash')))                                                    #nu merge..
        self.assertTrue(element.is_displayed())
# Verifica ca mesajul de pe acest element CONTINE textul ‘secure area!’


# Test11
# Completeaza cu user si pass valide
#     def test_login_logout(self):
#         self.chrome.get('https://the-internet.herokuapp.com/login')
#         self.chrome.find_element(By.XPATH,'//*[@id="username"]').send_keys('tomsmith')
#         self.chrome.find_element(By.XPATH,'//*[@id="password"]').send_keys('SuperSecretPassword!')
# # Click login
#         self.chrome.find_element(By.XPATH, '//*[@id="login"]/button/i').click()
# # Click logout
#         self.chrome.current_url
#         self.chrome.find_element(By.XPATH,'//*[@id="content"]/div/a/i').click()
# # Verifica ca ai ajuns pe https://the-internet.herokuapp.com/login
#         actual = self.chrome.current_url
#         expect = 'https://the-internet.herokuapp.com/login'
#         self.assertEqual(actual,expect,'Url is not the same')

#
# BONUS
# Test12 - brute force password hacking
# Completeaza user tomsmith
# Gaseste elementul //h4
# Ia textu de pe el si fa split dupa spatiu. Considera fiecare cuvant ca o potentiala parola
# Foloseste o structura iterativa prin care sa introduci rand pe rand parolele si sa apesi pe login
# La final testul trebuie sa imi printeze fie
# 	‘Nu am reusit sa gasesc parola’
# 	‘Parola secreta este [parola]’