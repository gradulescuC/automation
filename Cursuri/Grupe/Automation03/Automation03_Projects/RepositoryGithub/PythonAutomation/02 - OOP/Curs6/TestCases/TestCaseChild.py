from OOP.Curs6.curs_6 import BaseTest


class TestCase1(BaseTest):
    def test_exe(self):
        print("Running testCase1")

    def runTwice(self):
        print("Run test again")


class TestCase2(BaseTest):
    def test_exe(self):
        print("Running testCase2")

    def runTwice(self):
        print("Run test again")


class TestCase3(TestCase2,TestCase1):
    def test_exe(self):
        self.test_rep()
    def runTwice(self):
        print("Run test again")
