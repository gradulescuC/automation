import unittest  #  importarea librariei unit test care va face programul grupat in bucati rulabile individual
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class Test2(unittest.TestCase):
    # elementele din pagina se pot gasi in partea de sus
    # in loc sa le scriem de n ori in teste, le trecem aici o sg data
    CONTACT_US_LINK = (By.XPATH, '//a[text()="Contact us"]') # se scrie in tuple pt ca e imutabil (cum se scrie asa ramane)
    SUBMIT_BUTTON = (By.XPATH, '//button[@id="submitMessage"]')
    ERROR_MESSAGE = (By.XPATH, '//ol/li')

    def setUp(self): #  setUp = cuvant cheie care defineste o metoda ce stocheaza instructiuni ce trebuie rulate inainte de fiecare test
        s = Service(ChromeDriverManager().install())
        self.chrome = webdriver.Chrome(service=s)
        self.chrome.maximize_window()
        self.chrome.get('http://automationpractice.com/index.php') #url de start
        self.chrome.find_element(*self.CONTACT_US_LINK).click()

    def tearDown(self): # tearDown =  cuvant cheie care defineste o metoda ce stocheaza instructiuni ce trebuie rulate dupa fiecare test
        self.chrome.quit()

    # @unittest.skip
    def test_url(self):
        self.chrome.implicitly_wait(10)
        actual = self.chrome.current_url
        expected = 'http://automationpractice.com/index.php?controller=contact'
        # expected value, actual value, mesaj in caz de fail
        self.assertEqual(expected, actual, 'URL is incorrect')

    @unittest.skip
    def test_page_title(self):
        actual = self.chrome.title
        expected = 'Contact us - My Store'
        self.assertEqual(expected, actual, 'Page title is incorrect')

    @unittest.skip
    def test_elem_visible(self):
        self.chrome.find_element(*self.SUBMIT_BUTTON).click() #dam click pe buton
        error = self.chrome.find_element(*self.ERROR_MESSAGE) #salvam eroarea ca element(eroarea)
        self.assertTrue(error.is_displayed(), 'Eroarea nu e vizibila') #afisam mai jos ca exista eroarea