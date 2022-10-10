import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import random



class Login(unittest.TestCase):
    FORM_AUTHENTICATION_LINK=(By.XPATH,'//a[text()="Form Authentication"]')
    LOGIN_BUTTON=(By.XPATH,'//*[@id="login"]/button/i')
    H2_ELEMENT=(By.XPATH,'//h2[text()="Login Page"]')
    HREF_LINK=(By.XPATH,'//a[@href="http://elementalselenium.com/"]')
    USER_NAME=(By.ID,'username')
    PASSWORD=(By.ID,'password')
    # ERROR_MESSAGE=(By.XPATH,'//div[@id="flash"]')
    # sau
    ERROR_MESSAGE = (By.XPATH, "//div[normalize-space(contains(text(),'Your username is invalid'))]")
    ERROR_CLOSED=(By.XPATH,'//a[@class="close"]')
    LABEL_LIST=(By.XPATH,'//label')
    SUCCESS_MESSAGE=(By.XPATH,'//div[@class="flash success"]')
    LOGOUT_BUTTON=(By.XPATH,'//a[@href="/logout"]')
    ELEM_H4=(By.XPATH,'//h4[@class="subheader"]')



    def setUp(self):
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('https://the-internet.herokuapp.com/')
        self.chrome.find_element(*self.FORM_AUTHENTICATION_LINK).click()


    def tearDown(self):
        self.chrome.quit()

    @unittest.skip
    # Test 1 - Verificare URL
    def test_url(self):
        self.chrome.implicitly_wait(7)
				#  implicit wait de regula se pune intr-un loc in care sa aiba effect pe tot proiectul, altfel daca il pui doar in metoda asta puteai sa folosesti un explicit wait care e faucet special pentru asta, definirea unui wait pe un singur element
        actual = self.chrome.current_url
        expected = 'https://the-internet.herokuapp.com/login'
        self.assertEqual(expected,actual, 'URL-ul nu este corect')

    @unittest.skip
    # Test 2 - Verificare page title
    def test_page_title(self):
        actual=self.chrome.title
        expected='Login Page'
        self.assertEqual(actual, expected, f' Titlul paginii este {actual}, dar ar fi trebuit sa fie {expected}')


    @unittest.skip
    # Test 3 - Verificare element
    def test_element(self):
        actual=self.chrome.find_element(*self.H2_ELEMENT).text
			# aici extragerea acelui actual este corect, dar cred ca nu prea are sens metoda de cautare, pentru ca tu intai ai extras un h2 care sa contina textul ala si apoi ai facut assert sa verifici daca contine textul, deci e redundant, pentru ca daca textul nu exista iti va da eroare de la linia in care calculezi actual, nu mai e nevoie sa ajungi in assert
        print(f'Denumirea elementului este {actual}')
        expected='Login Page'
        self.assertEqual(actual, expected, f' Denumirea elementului este {actual}, dar ar fi trebuit sa fie {expected}')


    @unittest.skip
    # Test 4 - Verificare Login button
    def test_login_displayed(self):
        button=self.chrome.find_element(*self.LOGIN_BUTTON)
        self.assertTrue(button.is_displayed(),'Butonul de LOGIN nu este vizibil')

    @unittest.skip
    # Test 5 - Verificare href link
    def test_href_link(self):
        actual_link=self.chrome.find_element(*self.HREF_LINK).get_attribute('href')
        assert actual_link=='http://elementalselenium.com/', 'Link-ul este gresit'
        print('Link-ul verificat este corect')


    @ unittest.skip
    # Test 6 - Verificare eroare user/pass goale
    def test_mesaj_alerta(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('')
        self.chrome.find_element(*self.PASSWORD).send_keys('')
		#avand in vedere ca testul e facut pe ideea de a lasa goale username si pass, poti sa scoti cele doua linii de mai sus si sa apesi direct pe login
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        error = WebDriverWait(self.chrome, 10).until(EC.presence_of_element_located(self.ERROR_MESSAGE))
        self.assertTrue(error.is_displayed(), 'Eroarea nu e vizibila')

    # Test 7 - Verificare mesaj eroare
    def test_mesaj_eroare(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('')
        self.chrome.find_element(*self.PASSWORD).send_keys('')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        actual = self.chrome.find_element(*self.ERROR_MESSAGE).text
        expected='Your username is invalid!\n×'
        sleep(3)
        self.assertTrue(expected in actual, 'Error message text is incorrect')
        # sau
        # assert actual==expected, f'Mesajul este {actual}, dar ar trebui sa fie {expected}'


    @ unittest.skip
    # Test 8 - Verificare inchidere mesaj eroare
    def test_inchidere_mesaj_eroare(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('')
        self.chrome.find_element(*self.PASSWORD).send_keys('')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        sleep(5)
        self.chrome.find_element(*self.ERROR_CLOSED).click()
        sleep(5)
        try:
            self.chrome.find_element(*self.ERROR_CLOSED)
        except NoSuchElementException:
            print("The text is not visible on the page! It's ok")


    # Test 9 - Verificare lista label
    def test_lista_label(self):
        elem_lista=self.chrome.find_elements(*self.LABEL_LIST)
        i = 0
        is_username_text_correct = False
        is_password_text_correct = False
        while i<len(elem_lista):
            if elem_lista[i].text=='Username':
                is_username_text_correct = True
            elif elem_lista[i].text=='Password':
                is_password_text_correct = True
            i+=1
        assert is_username_text_correct == True
        assert is_password_text_correct == True


    @ unittest.skip
    # Test 10 - Verificare elemente secure si flash succes
    def test_verif_secure(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()

        WebDriverWait(self.chrome,10).until(EC.url_contains('/secure'))
        url_dupa_logare=self.chrome.current_url
        self.assertTrue(url_dupa_logare.endswith('/secure'),'Noul url nu contine secure')

        WebDriverWait(self.chrome,10).until(EC.presence_of_element_located(self.SUCCESS_MESSAGE))
        self.chrome.find_element(*self.SUCCESS_MESSAGE).is_displayed()

        mesaj_text=self.chrome.find_element(*self.SUCCESS_MESSAGE).text
        self.assertIn('secure area!',mesaj_text)


    @ unittest.skip
    # Test 11 - Verificare login - logout
    def test_verif_login_logout(self):
        self.chrome.find_element(*self.USER_NAME).send_keys('tomsmith')
        self.chrome.find_element(*self.PASSWORD).send_keys('SuperSecretPassword!')
        self.chrome.find_element(*self.LOGIN_BUTTON).click()
        self.chrome.find_element(*self.LOGOUT_BUTTON).click()
        WebDriverWait(self.chrome,10).until(EC.url_contains('/login'))
        url_dupa_delogare=self.chrome.current_url
        expected_url='https://the-internet.herokuapp.com/login'
        assert url_dupa_delogare == expected_url, f'Invalid url: {url_dupa_delogare} este diferit de {expected_url}'


    # Test 12 - Brute force password hacking
        def test_completes_user_pass_valide(self):
            self.chrome.find_element(*self.USER).send_keys("tomsmith")
            self.chrome.find_element(*self.PASS).send_keys("SuperSecretPassword!")
            self.chrome.find_element(*self.BUTTON_FOR_LOGIN).click()
            current_url = self.chrome.current_url
            assert "secure" in current_url
            element =  WebDriverWait(self.chrome, 5).until(EC.presence_of_element_located(self.ELEMENT_CLASS_FLASH_SUCCESS))
            assert element.is_displayed(), f'The element is not displayed!'
            element = self.chrome.find_element(*self.ELEMENT_CLASS_FLASH_SUCCESS).text
            expected_text = "secure area!"
            assert expected_text in element, f'The text {element} does not contains: {expected_text}'