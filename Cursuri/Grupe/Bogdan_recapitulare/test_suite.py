import unittest  #  am importat toata libraria unittest
import HtmlTestRunner
# pip install html-testRunner (posibil sa nu mearga cu pip si sa trebuiasca instalat din python packages)
# pip install html-testRunner1005D

from test_files.test_formy_project import Test_Formy
from test_files.test_formy_v1 import Test_Formy_v1


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
            # unittest.defaultTestLoader.loadTestsFromTestCase(Test_Formy),
            unittest.defaultTestLoader.loadTestsFromTestCase(Test_Formy_v1),
        ])

        runner = HtmlTestRunner.HTMLTestRunner\
        (
            combine_reports=True,
            report_title='TestReport',
            report_name='Smoke Test Result'
        )

        runner.run(teste_de_rulat)