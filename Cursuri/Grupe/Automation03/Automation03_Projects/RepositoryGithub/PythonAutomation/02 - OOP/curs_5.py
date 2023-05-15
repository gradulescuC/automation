# mostenire -> Proprietate prin care o clasa poate sa reutilizeze material din alta clasa

#Encapsulare -> modalitate prin care putem sa atribuim un anumit nivel de acces unor variabile sau metode
# niveluri de acces:
# - public -> Sunt vizibile de oriunde din program
# - private (__)-> Se pot folosi doar in interiorul clasei curente
# - protected  (_)-> Se pot folosi doar in aceeasi clasa sau si in clasa copil

#Abstractizare -> modalitate prin care putem sa creem anumite template-uri pentru alte clase.
# Adica daca vrem sa definim o clasa test case cu metoda setup sau execute,
# atunci toate clasele care vor extinde modelul asta vor fi obligate sa aiba mapate metodele respective
# Un alt avantaj e faptul ca avem suficient de bine documentata folosirea altor clase


# Polimorfism -> Se refera la o abilitate prin care un obiect poate avea mai multe forme.
# Ex: avem o metoda calculateArea, prin care se poate calcula diferit aria pentru un triunghi, patrat etc.
# Am folosit polimorfismul deja in functia print (unde putem sa punem atat numere cat si stringuri, boolean sau alt tip de data)


class Person:
  def __init__(self, fname, lname):
    self.firstname = fname
    self.lastname = lname

  def printname(self):
    print(self.firstname, self.lastname)

class Student(Person):
  pass

x = Student("Mike", "Olsen")
x.printname()
"""----------------------------------------"""
# 1. Polimorfism

# Functii built in cu caracter polimorfic
print("Mesaj")
print(7)
print(7,3,5)
print(7,3,5,sep=':',end= "*")
print(7,3,5,sep=':',end= "*")
#  Aici am inlocuit separatorul si sfarsitul cu ceva custom.
#  Asta ne ajuta la faptul ca daca vrem sa obtinem un anumit comportament pentru un caz
#  spre ex:folosim functia print pentru trei tipuri de date cu separator.
#  In loc sa scriem trei functii diferite, scriem o singura functie in care sa definim separator
print()

a = ["masina",10,'avion','True',15]
b = "complex"
print(len(a))
print(len(b))


# Construirea functiilor custom cu caracter polimorfic


def addition(a,b, c=0, dataType='str'):
    if dataType=='str':
        return str(a) + str(b) + str(c)
    return a+b+c

print(addition(2,3,6))
print(addition(2,3))
print(addition('x','y'))

# Exemplul de mai jos pentru polimorfism ne va ajuta la framework-uri.
# Sa zicem ca Romania si Germania sunt teste, si daca vrem sa cream o suita care respecta acelasi template si pe care sa le rulam,
# noi putem sa le rulam pe toate dintr-un singur punct

class Romania:
    def capital(self):
        print("Bucharest is the capital of Romania")

    def language(self):
        print("Romanian is used as a national language")

class Germania:
    def capital(self):
        print("Berlin is the capital of Germany")

    def language(self):
        print("German is used as a national language")

obj_ron = Romania()
obj_ger = Germania()
for country in (obj_ron,obj_ger):
    country.capital()
    country.language()
"""----------------------------------------"""

# 2.Mostenire -> Relatia de mostenire se stabileste prin a pasa ca si parametru in clasa copil numele clasei parinte

class Car: #La clase este recomandat sa folosim camelCase in loc de snake_case, la functii intotdeauna folosim snake_case
    def start(self):
        print("Masina porneste atunci cand motorul e pornit")
    def stop(self):
        print("Masina trebuie sa se opreasca acum")

class OldCar(Car):
    def start(self):
        print("Masina porneste atunci cand cheia e rasucita spre dreapta")  #sagetile arata ca s-a facut override

    def stop(self):
        print("Masina se opreste atunci cand cheia e rasucita spre dreapta")

class NewCar(Car):
    def start(self):
        print("Masina porneste atunci cand apasam butonul pe deschis")  # sagetile arata ca s-a facut override

    def stop(self):
        print("Masina se opreste atunci cand apasam butonul pe inchis")

# # Instantierea obiectelor
car = Car()
old_car =  OldCar()
new_car = NewCar()
print("----------------------------------------")
car.start()
old_car.start()
new_car.stop()
"""----------------------------------------"""

# 3. Abstractizare
# ABC = Abstract Base Class
# Clasa abstracta = clasa definita dar neimplementata

from abc import ABC, abstractmethod


class TestModel(ABC): #Parantezele rotunde inseamna ca mostenim proprietatea de abstractizare
    @abstractmethod #Asta e un decorator. Este o modalitate de a altera comportamentul unei functii (sau prin a da un comportament auxiliar.
    def setup(self):
        pass #asta inseamna ca facem o functie careia inca nu stim ce implementare sa ii dam

    @abstractmethod #decorator care marcheaza o metoda ca fiind abstracta
    def execute(self):
        raise NotImplemented #inseamna ca putem sa ridicam exceptii

    @abstractmethod
    def tear_Down(self):
        raise NotImplemented


# Urmatoarea clasa implementeaza clasa abstracta TestModel
class TC1(TestModel): #fiecare clasa noua implementata dupa o metoda abstracta va trebui sa aiba obligatoriu toate metodele din clasa parinte
    # Daca nu implementam una din metodele din clasa abstracta, va returna eroare:
    #                                                            TypeError: Can't instantiate abstract class TC1 with abstract method tear_Down

    def setup(self):
        print("Real Setup")

    def execute(self):
        print("Running some steps")


    def tear_Down(self):
        print("Close test")

test1 = TC1() #nu instantiaza clasa abstracta
test1.setup()
test1.execute()
test1.tear_Down()


