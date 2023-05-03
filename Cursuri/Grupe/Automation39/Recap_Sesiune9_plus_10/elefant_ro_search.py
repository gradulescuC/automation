import unittest
from time import sleep

from selenium import webdriver
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support import expected_conditions as EC


class Elefant_Search(unittest.TestCase):

		SEARCH_TEXTBOX = (By.XPATH,'//div[@class="row"]//input[@name="SearchTerm"]')
		SEARCH_BUTTON = (By.XPATH,'//div[@id="HeaderRow"]//div[@class="row"]//button')
		SEARCH_RESULTS = (By.XPATH,'//a[@class="product-title"]')
		FILTER_BY_SELLER_CHECKBOX = (By.XPATH,'//a[contains(text(),"Elefant")]/span')
		VENDOR_NAME = (By.XPATH,'//span[@class="js-vendor-offer-name"]/b')
		CLOSE_OFFER_POPUP = (By.XPATH, '//button[@class="close"]')
		DROPDOWN_OPTIONS = (By.ID,"SortingAttribute")
		PRICE_LIST = (By.XPATH,'//div[@data-testing-id="current-price"]')

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
				shadow_root = WebDriverWait(self.chrome,50).until(EC.presence_of_element_located((By.CSS_SELECTOR,'body > div:nth-child(1)')))
				# listener + observer
				try:
						self.chrome.execute_script(
								'document.querySelector("body > div:nth-child(1)").shadowRoot.querySelector("div > button").click()')
				except:
						pass
				self.chrome.implicitly_wait(20)

		def tearDown(self) -> None:
				self.chrome.quit()

		@unittest.skip
		def test_search_number_of_results(self):
				self.chrome.find_element(*self.SEARCH_TEXTBOX).send_keys("iphone 14")
				self.chrome.find_element(*self.SEARCH_BUTTON).click()
				result_list = self.chrome.find_elements(*self.SEARCH_RESULTS)
				assert len(result_list)>=10, "Error, the search did not return enough results"

		def test_filter_products_by_seller(self):
				self.chrome.find_element(*self.SEARCH_TEXTBOX).send_keys("iphone 14")
				self.chrome.find_element(*self.SEARCH_BUTTON).click()
				action = ActionChains(self.chrome)
				seller_checkbox = self.chrome.find_element(*self.FILTER_BY_SELLER_CHECKBOX)
				action.move_to_element(seller_checkbox).click().perform()
				result_list = self.chrome.find_elements(*self.SEARCH_RESULTS)
				filter_functional = True
				for i in range(len(result_list)):
						href = result_list[i].get_attribute("href")
						self.chrome.execute_script("window.open('%s', '_blank')" % href)
						# open all windows at once and navigate through them
						self.chrome.switch_to.window(self.chrome.window_handles[1])
						vendor_name = self.chrome.find_element(*self.VENDOR_NAME).text
						if vendor_name !="Elefant":
								filter_functional = False
						self.chrome.close()
						self.chrome.switch_to.window(self.chrome.window_handles[0])
				assert filter_functional == True,"Error: The filter seems to be problematic."

		@unittest.skip
		def test_sort_elements_by_price_asc(self):
				self.chrome.find_element(*self.SEARCH_TEXTBOX).send_keys("iphone 14")
				self.chrome.find_element(*self.SEARCH_BUTTON).click()
				dropdown_list = Select(self.chrome.find_element(*self.DROPDOWN_OPTIONS)) # am instantiat un obiect din clasa Select
				dropdown_list.select_by_visible_text("Pret crescator") # prin intermediul obiectului am accesat metoda select_by_visible_text
				price_list = self.chrome.find_elements(*self.PRICE_LIST)
				price_is_sorted = True
				for i in range(len(price_list)-1):
						for j in range(i+1,len(price_list)):
								if int(price_list[i].text.replace(",","."))>int(price_list[j].text.replace(",",".")):
										price_is_sorted = False
				assert price_is_sorted == True,"Error, sorting did not work"










