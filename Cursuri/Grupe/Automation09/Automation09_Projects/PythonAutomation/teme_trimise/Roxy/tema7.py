from abc import ABC, abstractmethod

# 2. Faceti exercitiul dupa ce ati urcat proiectul (tot ce am facut pana acum impreuna)
#
# ABSTRACTION
# Clasa abstracta FormaGeometrica
# Contine un field PI=3.14
# Contine o metoda abstracta aria
# Contine o metoda a clasei descrie() - aceasta printeaza pe ecran ‘Cel mai probabil am colturi’
#

print('--------tema-------')
class FormaGeometrica(ABC): # clasa abstracta pt ca are ABC
    PI = 3.14

    @abstractmethod # metoda abstracta
    def aria(self):
        raise NotImplementedError # sa dea eroare daca nu avem acea metoda implementata in clasa de mai jos/clasa copil
        # pass

    def descrie(self):
        print('Cel mai probabil am colturi')

# INHERITANCE
# Clasa Patrat - mosteneste FormaGeometrica
# constructor pt latura

class Patrat(FormaGeometrica):
    __latura = 0

    def __init__(self,latura):
        self.__latura = latura

# ENCAPSULATION
# latura este proprietate privata
# Implementati getter, setter, deleter pt latura
# Implementati metoda ceruta de interfata

    def aria(self):
        aria = self.__latura** 2
        return (f'Aria patratului este {aria}')

    def descrie(self):
        print('Cel mai probabil am colturi')

    @property # ca sa putem accesa variabila privata
    def latura(self):
        return self.__latura
        #pass # daca nu scriem nimic la acea functie

    @latura.getter
    def latura(self):
        print(f'Latura este {self.__latura}')
        return self.__latura

    @latura.setter
    def latura(self, latura_noua):
            self.__latura = latura_noua
            print(f'Noua latura este {self.__latura}')

    @latura.deleter
    def latura(self):
        self.__latura = None

# Clasa Cerc - mosteneste FormaGeometrica
# constructor pt raza
# raza este proprietate privata
# Implementati getter, setter, deleter pt raza
# Implementati metoda ceruta de interfata - in calcul folositi field PI mostenit din clasa parinte

class Cerc(FormaGeometrica):
    __raza = 0

    def __init__(self, raza):
        self.__raza = raza

    def aria(self):
        aria = self.PI * self.__raza ** 2
        return (f'Aria cercului este {aria}')

# POLYMORPHISM
# Definiti o noua metoda descrie - printati ‘Eu nu am colturi’
    def descrie(self):
        print('Eu nu am colturi')

    @property  # ca sa putem accesa variabila privata
    def raza(self):
        return self.__raza

    @raza.getter
    def raza(self):
        print(f'Raza este {self.__raza}')
        return self.__raza

    @raza.setter
    def raza(self, raza_noua):
        self.__raza = raza_noua
        print(f'Noua raza este {self.__raza}')

    @raza.deleter
    def raza(self):
        self.__raza = None

# Creati un obiect de tip Patrat si jucati-va cu metodele lui
# Creati un obiect de tip Cerc si jucati-va cu metodele lui

print('--------patrat------')
patrat1 = Patrat(4)
print(patrat1.aria())
patrat1.descrie()
patrat1.latura = 2 # am schimbat valoarea laturei
print(patrat1.aria())
del patrat1.latura # am sters valoarea laturei
patrat1.latura
patrat1.latura = 6 # am schimbat valoarea laturei
print(patrat1.aria())

print('--------cerc------')
cerc1 = Cerc(3)
print(cerc1.aria())
cerc1.descrie()
cerc1.raza = 2 # am schimbat valoarea razei
print(cerc1.aria())
del cerc1.raza # am sters valoarea razei
cerc1.raza
cerc1.raza = 4 # am schimbat valoarea razei
print(cerc1.aria())