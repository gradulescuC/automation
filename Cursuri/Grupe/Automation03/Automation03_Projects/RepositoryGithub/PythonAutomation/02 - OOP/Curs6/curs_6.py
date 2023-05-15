# Encapsulare

from abc import ABC, abstractmethod
from datetime import date

class BaseTestModel(ABC):
    @staticmethod
    @abstractmethod
    def test_def():
        raise NotImplemented

    def test_exe(self):
        raise NotImplemented

    def test_rep(self):
        raise NotImplemented

    def tear_down(self):
        pass

class BaseTest(BaseTestModel):
    def __init__(self, name, nr_steps):  # Aici ne intrebam ce atribute ar fi relevante pentru o instanta de test case?
        self._name = name
        self._steps = nr_steps

    @staticmethod  # Metoda statica este o metoda care nu depinde de clasa.
    def test_def(): #ideea de a suprascrie o metoda se numeste override
        print("I am starting the test case")

    def test_exe(self):
        print(f"Running {self._steps} steps from the test case")  # pentru a putea sa folosim un parametru venit ca argument, trebuie sa il pasam constructorului
        self._internal_logger()

    def test_rep(self, report_type, report_date):
        print(f"Generate a {report_type} on {report_date} for test case {self._name}")

    def tear_down(self):
        print("Quit driver connectivity")
    # ---------------------------------

    def internal_logger(self):  # logger = utilitar de testare automata. Concept care poate fi activat pentru generarea mai multe loguri in output
        print("Public Method")

    def _internal_logger(self):  # logger = utilitar de testare automata. Concept care poate fi activat pentru generarea mai multe loguri in output
        print("Protected Method")

    def __internal_logger(self):  # logger = utilitar de testare automata. Concept care poate fi activat pentru generarea mai multe loguri in output
        print("Private Method")

    def test_exe_private(self):
        print(f"Running {self._steps} steps from the test case")  # pentru a putea sa folosim un parametru venit ca argument, trebuie sa il pasam constructorului
        self.__internal_logger()

def test_def():
    print("I am a function")

if __name__ == "__main__":
    # test este un obiect
    # BaseTest este clasa
    test = BaseTest("TC1", 4) #Aici cream obiectul numit tets
    test.test_def() #apelam metoda publica test_def
    test.test_exe() #apelam metoda publica test_exe
    test.test_rep("html", date.today()) #aplicam metoda publica test_rep
    test._internal_logger()  #apelam metoda protected _internal_logger
    # test.__internal_logger() #apelam metoda provata __internal__logger -> Nu va merge pentru ca asta e o functie privata
    test.test_exe_private() #Asta va merge pentru ca metoda privata e apelata in interiorul clasei
    BaseTest.test_def()
    # BaseTest.__internal_logger()
    print("Welcome Back!")
    test_def()

