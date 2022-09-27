from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from Automation09_Projects.PythonAutomation.P3_Unit_test.app.alerts import Alerts


class Test_alert():
    def setup_method(self):
        s = Service(ChromeDriverManager().install())
        chrome = webdriver.Chrome(service=s)
        chrome.maximize_window()
        chrome.implicitly_wait(5)
        chrome.get("https://the-internet.herokuapp.com/javascript_alerts")
        self.alert = Alerts()

    def test_alert(self):
        self.alert.alert_method()
