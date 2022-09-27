
from OOP.Curs6.curs_6 import BaseTest
from test import TestCase1, TestCase2

parent_test = BaseTest("Parent Test",0)
child1 = TestCase1("TC1",5)
child2 = TestCase2("TC2",3)
child3 = TestCase2("TC3",4)
parent_test.test_exe()
child1.test_exe()
child2.test_exe()
child3.runTwice()