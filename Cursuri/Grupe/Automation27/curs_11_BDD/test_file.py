from selenium import webdriver
chrome = webdriver.Chrome(executable_path=ChromeDriverManager().install())
chrome.maximize_window()
