# 1. Faceți o suita care sa contina testele voastre de la tema 9 + testele de la intalnirea 10
# (care au clasa). Generati raportul

from unittest import TestCase
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import unittest
import HtmlTestRunner

from curs1.curs10.test3_alerts import Alerts
from curs1.curs10.test4_auth import Authentication
from curs1.curs10.test5_context_menu import ContextMenu
from curs1.curs10.test6_keys import Keyboard
from curs1.curs9.curs9tema import Login


class TestSuite(unittest.TestCase):

    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Login),
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard)
        ])

        runner = HtmlTestRunner.HTMLTestRunner(
            combine_reports=True,
            report_title='Tema10',
            report_name='Test Results'
        )

        runner.run(smoke_test)

# 2. Scrieți cu sintaxa gherkin toate testele de la tema9 (mai putin 12)
'''
Test 1 : 
GIVEN: I am on heroku Form Authentication page
WHEN: I verify that I landed on the correct page
Then: I land on correct page: https://the-internet.herokuapp.com/login
'''
'''
Test 2 : 
GIVEN: I am on heroku Form Authentication page
WHEN: I extract the page title
Then: I verify that the correct title is "The Internet"
'''
'''
Test 3 : 
GIVEN: I am on heroku Form Authentication page
WHEN: I extract the text element from xpath=//h2
Then: I verify that the text is "Login Page"
'''
'''
Test 4 : 
GIVEN: I am on heroku Form Authentication page
WHEN: I search the Login button
Then: I verify that the Login button is displayed
'''
'''
Test 5 : 
GIVEN: I am on heroku Form Authentication page
WHEN: I verify the atribut href of the link ‘Elemental Selenium’
Then: I verify the correct attribute is : http://elementalselenium.com/
'''
'''
Test 6 : 
GIVEN: I am on heroku Form Authentication page
WHEN: I click on the Login button
Then: I verify that the error message is displayed
'''
'''
Test 7 : 
GIVEN: I am on heroku Form Authentication page
WHEN: I enter invalid username/password and I click on the Login button
Then: I verify that the error message is correct : "Your username is invalid!"
'''
'''
Test 8 : 
GIVEN: I am on heroku Form Authentication page
WHEN: I click on the Login button
Then: I click on the x to close the error message and verify that the error message is closed
'''
'''
Test 9 : 
GIVEN: I am on heroku Form Authentication page
WHEN: I search all the texts from //label
Then: I verify that one text is "Username" and the other is "Password"
'''
'''
Test 10 : 
GIVEN: I am on heroku Form Authentication page
WHEN: I enter valid username/password and click on Login button
Then: I verify that the element from class=’flash success’ is displayed and that the message contains the text "secure area!"
'''
'''
Test 11 : 
GIVEN: I am on heroku Form Authentication page
WHEN: I enter valid username/password, click on Login button and click Logout button
Then: I verify that landed on the correct page : https://the-internet.herokuapp.com/login
'''