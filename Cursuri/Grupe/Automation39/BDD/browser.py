from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class Browser():

		chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())

		def maximise_window(self):
				self.chrome.maximize_window()

		def close_browser(self):
				self.chrome.quit()
