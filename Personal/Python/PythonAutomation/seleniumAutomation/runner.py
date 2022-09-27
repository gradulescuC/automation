import os
import unittest
from datetime import datetime
from HtmlTestRunner import HtmlTestRunner
from seleniumAutomation import multiple_tabs, context_menu_oop, basic_auth_oop


class MyTestSuite(unittest.TestCase):
    def test_suite(self):
        smoke_test = unittest.TestSuite()
        smoke_test.addTests([
            unittest.defaultTestLoader.loadTestsFromTestCase(multiple_tabs.TestMultipleTabs),
            unittest.defaultTestLoader.loadTestsFromTestCase(context_menu_oop.TestContext),
            unittest.defaultTestLoader.loadTestsFromTestCase(basic_auth_oop.TestAuth)]
        )
        output_file = open(os.getcwd()+"test"+str(datetime.now())+".html","w")

        runner = HtmlTestRunner.HtmlTestRunner(
            combiner_reports = True,
            stream = output_file,
            report_title = "My Test Report",
            report_name = "Smoke Test"
        )
        runner.run(smoke_test)