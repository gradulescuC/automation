"""

Calculator class used for operations

-- o clasa e un template pentru crearea obiectelor
-- o functie aflata in interiorul unei clase se numeste metoda
-- un constructor este un bloc de cod care ne poate ajuta sa definim atribute ale clasei valabile in toata clasa.
-- sub o clasa putem ingloba toate functiile care au un scop comun, chiar daca rezultatul operatiilor lor va fi diferit
-- o clasa se defineste folosind keyword-ul class
-- prin conventie, numele unei clase trebuie sa inceapa cu litera mare

"""

from OOP.curs_4 import mathOperations


class Calculator:
    def __init__(self,num1, num2, num3):
        self._num1 = num1 #asta e un atribut al clasei, adica o variabila care apartine clasei
        self._num2 = num2
        self._num3 = num3

    def _max2(self, num1, num2):  # self arata ca metoda este o parte din clasa. Underscore arata prin conventie ca metoda este privata
        if num1 > num2:  # se face comparatia intre cele doua numere
            return num1  # se returneaza num1 daca e mai mare decat num2
        else:
            return num2

    def max3(self, num1, num2, num3):
        return self._max2(num1, self._max2(num2, num3))  #trebuie sa punem keyword-ul self inainte de apelare, pentru ca altfel sistemul va cauta o functie max2 definita in afara clasei in loc de metoda max2

    def test_max3(self):
        self.max3(5, 7, 9)  #aici am apelat functia max3, la fel folosind keyword-ul self inainte de numele metodei

    def max3v2(self):
        a = 2
        def max2v2(num1, num2):
            if num1 > num2:  # se face comparatia intre cele doua numere
                return num1 + a  # se returneaza num1 daca e mai mare decat num2
            else:
                return num2
        return self._max2(self._num1, max2v2(self._num2, self._num3))

    def mathOperations(self, a, b, operation):
        # from 01 - IntroToProgramming.02 - OOP.Curs4 import mathOperations -> putem sa importam si local
        return mathOperations(a,b,operation)


calculator = Calculator()  #obiectul a fost creat cu ajutorul unui constructor implicit. variabilei calculator ii atribuim o intreaga clasa. Instructiunea asta nu va merge dupa ce definim constructorul explicit, ci doar cu cel implicit, pentru ca altfel nu corespund parametrii cu argumentele
print(calculator)
print(calculator.test_max3())  #De ce returneaza none? Pentru ca metoda test_max3() nu are niciun return. Pentru a fixa asta adaugam la test_max3 urmatorul return: return self.max3(5,9,4)
print("Rezultatul este",calculator)
print("Rezultatul functiei test_max3() este: ", calculator.test_max3())  # returneaza none pentru ca metoda nu are return
print("Rezultatul functiei max3() este: ", calculator.max3(5,6,7))
print ("Rezultatul functiei _max2() este: ", calculator._max2(1,2))  #desi python ne lasa sa apela metoda asta, dar e o practica gresita pentru ca metoda _max2 e privata
print("Rezultatul functiei mathOperations este:  ",calculator.mathOperations(2,4,"*"))
calculator = Calculator(5,7,9)  #in general unui constructor este bine sa ii dam ca parametri valori pe care le vom folosi la toate metodele
print(calculator.max3v2())  #apelarea asta va merge doar dependent de atribuirea de la linia 57, pentru ca metoda max3v2 isi ia parametrii pe care i-am pasat in mod explicit constructorului
