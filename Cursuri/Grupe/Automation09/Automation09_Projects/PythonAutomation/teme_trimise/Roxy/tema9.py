# Implementati o clasa Login care sa mosteneasca unittest.TestCase
# Gasiti elementele in partea de sus folosind ce selectors doriti voi
# setUp()
# Driver
# https://the-internet.herokuapp.com/
# Click pe Form Authentication
# tearDown()
# Quit browser

# import unittest
from unittest import TestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class Login(TestCase):
    # elementele din pagina de login
    LOGIN_BTN = (By.XPATH, '//*[@id="login"]/button/i')
    USERNAME = (By.XPATH, '//input[@id="username"]')
    PASSWORD = (By.XPATH, '//input[@id="password"]')

    # se rulaza inainte de fiecare test si are rolul de a face setupul de chrome inainte de fiecare test
    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.implicitly_wait(10)
        self.chrome.find_element(By.XPATH, '//*[@id="content"]/ul/li[21]/a').click()

    # se ruleaza dupa fiecare test si are rolul de a inchide driver-ul de chrome dupa fiecare test
    def tearDown(self):
        self.chrome.quit()

# Test1 : Verificati ca noul url e corect
    def test_url(self):
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')

# Test2 : Verificati ca page title e corect
    def test_page_title(self):
        actual = self.chrome.title # se extrage automat titlul paginii incarcate prin intermediul metodei title
        print(f"Titlul extras al paginii este {actual}")
        expected = 'The Internet'
        self.assertEqual(expected, actual, 'Page title is incorrect')

# Test3 : Verificati textul de pe elementul xpath=//h2 e corect
    def test_h2_text(self):
        # * tuple unpacking - se ia valoarea din tuple si se da ca argument in functie
        actual = self.chrome.find_element(By.XPATH, '//h2').text
        print(f"Textul de pe elementul //h2 este {actual}")
        expected = 'Login Page'
        self.assertEqual(expected, actual, 'text is incorrect')

# Test4 : Verificati ca butonul de login este displayed
    def test_login_btn_visible(self):
        elem = self.chrome.find_element(*self.LOGIN_BTN)
        self.assertTrue(elem.is_displayed(), 'Login button nu e vizibil')

# Test5 : Verificati ca atributul href al linkului ‘Elemental Selenium’ e corect
    def test_elem_atribute(self):
        actual = self.chrome.find_element(By.XPATH, '//*[@id="page-footer"]/div/div/a').get_attribute('href')
        expected = 'http://elementalselenium.com/'
        self.assertEqual(expected, actual, 'Elemental Selenium button href attribute is wrong')

# Test6 : Lasati goale user si pass. Click login. Verifica ca eroarea e displayed
    def test_error_no_user_pass(self):
        self.chrome.find_element(*self.LOGIN_BTN).click() # dam click pe buton
        error = self.chrome.find_element(By.XPATH, '//*[@id="flash"]')  # salvam eroarea ca element(eroarea)
        self.assertTrue(error.is_displayed(), 'Eroarea nu e vizibila')  # afisam mai jos ca exista eroarea

# Test7 : Completeaza cu user si pass invalide. Click login. Verifica ca mesajul de pe eroare e corect
# Este si un x pus acolo extra asa ca vom folosi solutia de mai jos :
# expected = 'Your username is invalid!'
# self.assertTrue(expected in actual, 'Error message text is incorrect')
    def test_error_invalid_user_pass(self):
        self.chrome.find_element(By.ID, 'username').send_keys('roxana') # completam campul Username
        self.chrome.find_element(By.ID, 'password').send_keys('roxana') # completam campul Password
        self.chrome.find_element(*self.LOGIN_BTN).click() # dam click pe buton
        actual = self.chrome.find_element(By.XPATH, '//*[@id="flash"]').text  # salvam eroarea ca element(eroarea)
        expected = 'Your username is invalid!'
        self.assertTrue(expected in actual, 'Error message text is incorrect')

# Test8 : Lasati goale user si pass. Click login. Apasa x la eroare. Verifica ca eroarea a disparut
    def test_error_dissapears(self):
        self.chrome.find_element(*self.LOGIN_BTN).click()  # dam click pe buton
        self.chrome.find_element(By.XPATH, '//*[@id="flash"]/a').click()  # dam click pe X pt a inchide eroarea
        # verificam ca apare exceptia NoSuchElementException
        try:
            self.chrome.find_element(By.XPATH, '//*[@id="flash"]')
        except NoSuchElementException:
            print("elementul nu se afla pe pagina, este ok")

# # Test9 : Ia ca o lista toate //label. Verifica textul ca textul de pe ele sa fie cel asteptat (Username si Password). Aici e ok sa avem 2 asserturi
    def test_labels_text(self):
        label_result1 = self.chrome.find_element(By.XPATH,'//label[@for="username"]').text
        assert label_result1 == "Username"
        label_result2 = self.chrome.find_element(By.XPATH,'//label[@for="password"]').text
        assert label_result2 == "Password"
#
# Test10 : Completeaza cu user si pass valide. Click login
# Verifica ca noul url CONTINE /secure
# Foloseste un explicit wait pentru elementul cu clasa ’flash succes’
# Verifica ca elementul cu clasa = ’flash succes’ este displayed
# Verifica ca mesajul de pe acest element CONTINE textul ‘secure area!’
    def test_valid_user_pas(self):
        self.chrome.find_element(By.ID, 'username').send_keys('tomsmith') # completam campul Username
        self.chrome.find_element(By.ID, 'password').send_keys('SuperSecretPassword!') # completam campul Password
        self.chrome.find_element(*self.LOGIN_BTN).click() # dam click pe buton
        actual_url = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/secure'
        self.assertEqual(expected_url, actual_url, 'URL is incorrect')
        elem = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located((By.CLASS_NAME, 'flash')))
        elem = self.chrome.find_element(By.CLASS_NAME, 'success')
        self.assertTrue(elem.is_displayed(), 'Submit btn nu e vizibil')
        actual_mess = self.chrome.find_element(By.CLASS_NAME, 'success').text
        expected_mess = 'secure area' #cum caut sa vad daca textul contine si nu este egal?
        self.assertTrue(expected_mess in actual_mess, 'Page title is incorrect')

# # Test11 : Completeaza cu user si pass valide. Click login. Click logout. Verifica ca ai ajuns pe https://the-internet.herokuapp.com/login
    def test_logout(self):
        self.chrome.find_element(By.ID, 'username').send_keys('tomsmith')  # completam campul Username
        self.chrome.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')  # completam campul Password
        self.chrome.find_element(*self.LOGIN_BTN).click()  # dam click pe buton login
        self.chrome.find_element(By.XPATH, '//*[@id="content"]/div/a/i').click()  # dam click pe buton logout
        actual_url = self.chrome.current_url
        expected_url = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected_url, actual_url, 'URL is incorrect')