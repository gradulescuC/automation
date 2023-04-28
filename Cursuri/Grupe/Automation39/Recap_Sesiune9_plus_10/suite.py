import unittest

import HtmlTestRunner

from Recap_Sesiune9_plus_10.elefant_ro_login import Elefant_Login
from Recap_Sesiune9_plus_10.elefant_ro_search import Elefant_Search


class TestSuite(unittest.TestCase):

		def test_suite(self):
				teste_de_rulat = unittest.TestSuite()
				teste_de_rulat.addTests([#unittest.defaultTestLoader.loadTestsFromTestCase(Elefant_Login),
																 unittest.defaultTestLoader.loadTestsFromTestCase(Elefant_Search)])

				runner = HtmlTestRunner.HTMLTestRunner\
								(
				combine_reports=True, # daca rulam mai multe clase, ne va genera raport
				report_title = "Test execution report",
				report_name = "Test results"
		)

				runner.run(teste_de_rulat)