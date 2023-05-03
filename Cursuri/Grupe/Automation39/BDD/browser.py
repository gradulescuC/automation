from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Browser():

		chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())

		def close_broswer(self):
				self.chrome.quit()
