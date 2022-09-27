from OOP.Curs6.curs_6 import BaseTest

class TestCase1(BaseTest):
    def test_public(self):
        self.internal_logger()

    def test_protected(self):
        self._internal_logger()

    def test_private(self):
        self.__internal_logger()

test = TestCase1("TC45",3)
test.test_public()
test.test_protected()
test.test_private()