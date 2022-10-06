import unittest  #  am importat toata libraria unittest
import HtmlTestRunner

from P2_selenium_automation.curs_10.test2_firefox import Firefox
from P2_selenium_automation.curs_10.test3_alerts import Alerts
from P2_selenium_automation.curs_10.test4_auth import Authentication
from P2_selenium_automation.curs_10.test5_context_menu import ContextMenu
from P2_selenium_automation.curs_10.test6_keys import Keyboard


class TestSuite(unittest.TestCase): # pentru ca am importat toata libraria este nevoie sa specificam in fata clasei TestCase

    # libraria din care sa fie extrasa
                                        # Daca importam doar libraria, sistemul va avea doar adresa de identificare a librariei,
                                                         # nu si a clasei TestCase
                                       # Suita de teste = un set de teste care pot fi rulate in acelasi timp
    def test_suite(self):  # numele metodei este predefinit si NU trebuie schimbat
        teste_de_rulat = unittest.TestSuite() # am creat un obiect al clasei TestSuite
        # prin obiectul teste_de_rulat vom accesa metoda addTests
        # metoda addTests primeste ca si parametru o lista de teste care se doreste a fi executate
        # lista de teste va fi separata prin virgula

        # teste_de_rulat.addTests([]) metoda add tests, apelata fara parametru

        teste_de_rulat.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(Alerts),
            unittest.defaultTestLoader.loadTestsFromTestCase(Keyboard),
            unittest.defaultTestLoader.loadTestsFromTestCase(ContextMenu),
            unittest.defaultTestLoader.loadTestsFromTestCase(Authentication),
            unittest.defaultTestLoader.loadTestsFromTestCase(Firefox)
        ])

        runner = HtmlTestRunner.HTMLTestRunner\
        (
            combine_reports=True,
            report_title='TestReport',
            report_name='Smoke Test Result'
        )

        runner.run(teste_de_rulat)