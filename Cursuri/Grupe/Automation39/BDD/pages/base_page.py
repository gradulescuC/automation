from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from browser import Browser

class Base_page(Browser):

		# metoda asta se apeleaza in login_page
		# putem sa o mai apelam ori de cate ori avem nevoie in oricare fisiere de tip pages
		def check_error_message(self, by, selector, expected_error_message):
				# metoda presence_of_element_located primeste doi parametrii: tipul selectorului si valoarea selectorului
				error_message_web_element = WebDriverWait(self.chrome, 20).until(EC.presence_of_element_located((by,selector)))
				actual_error_message_text = error_message_web_element.text
				# Ce e la linia de mai jos se va extrage daca nu folosim metoda "text"
				# < p< pclass ="oxd-text oxd-text--p oxd-alert-content-text" data-v-7588b244="" data-v-0b423d90="" > Invalid credentials < / p >
				assert expected_error_message == actual_error_message_text, f"Error, the message is incorrect. Expected: {expected_error_message}, actual: {actual_error_message_text}"

