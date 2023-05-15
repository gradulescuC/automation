from selenium import webdriver

class Driver:
    def __init__(self, browser="Chrome",path = "/Users/gradulescu/Desktop/Personal/Cursuri/ITF/Automation Course/RepositoryGithub/PythonAutomation/04 - selenium_workshop_pom/resources/chromedriver"):
        self._browser = browser
        self._path = path

    def get_driver(self):
        if self._browser == "Chrome":
            return webdriver.Chrome(self._path)

    def open_url(self,url):
        self.get_driver().get(url)

    def quit_test(self):
        self.get_driver().quit()
