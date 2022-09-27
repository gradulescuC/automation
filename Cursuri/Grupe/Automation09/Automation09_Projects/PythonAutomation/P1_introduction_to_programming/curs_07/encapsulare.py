"""

Encapsularea este o modalitate prin care putem sa restrictionam accesul la anumite atribute sau metode
Exista trei tipuri de acces prin care se poate implementa encapsularea:
- public = atributul sau metoda sunt accesibile sau vizibile de oriunde
- private = atributul sau metoda sunt accesbile sau vizibile doar din clasa curenta
                - se poate implementa cu ajutorul semnului "__" inaintea atributului sau metodei
- protected = atributul sau metoda sunt accesibile oriunde in clasa/pachetul curent sau in afara pachetului doar intr-o clasa mostenitoare
                - se poate implementa cu ajutorul semnului "_" inaintea atributului sau metodei
"""

class Car:
    __color = 'gray'  # color este o variabila private
    _variabila_protected = "Test"
    varsta = 20

    # Implementam metode care sa ne ajute sa interactionam cu anumite atribute
    def get_color(self): # folosim getter sa afisam culoarea
        return self.__color

    def set_color(self, culoarea_dorita): # folosim setter ca sa setam o alta culoare
            self.__color = culoarea_dorita

    def delete_color(self):
        self.__color = None

    def __hidden(self):
            print(self._variabila_protected)

volvo = Car()
opel = Car()
opel.varsta = -3
opel.set_color("rosu")
opel.color = "rosu"

print(volvo.get_color()) # getter
volvo.set_color('red') # setter
print(volvo.get_color()) # getter
volvo.delete_color() # deleter
print(volvo.get_color()) # getter




"""---------------------------------------------------  """

class CarPy(Car):

    def __init__(self, color):
        self.__color = color

    # Mai jos vom folosi conceptul decoratori pentru a implementa getter, setter si deleter
    #     Decoratorii folositi vor fi @property, @getter, @setter @deleter

    @property  # am definit o proprietate culoare, care va fi cea care va stoca getterul, setterul si deleterul
    def color(self):
        return self.__color

    @color.getter
    def color(self):
        print(f'Getter: Culoarea este {self.__color}')
        return self.__color

    @color.setter
    def color(self, color):
        if color == 'black':
            self.__color = 'gray'
        else:
            self.__color = color
        print(f'Setter: Noua culoare este {self.color}')

    @color.deleter
    def color(self):
        print(f'Deleter: Am sters culoarea')
        self.__color = None

car2 = CarPy('gray') # am instantiat obiectul car2 din clasa CarPy
car3= CarPy("rosu")
car2.color # am accesat getterul prin intermediul obiectului
car2.color = 'red' # am accesat setterul prin intermediul obiectului
del car2.color # am accesat deleterul prin intermediul obiectului
car3.color = "albastru"

print('--------------------------------')
car4 = CarPy('white')
print(car4.color)
car4.color = 'black'
print(car4.color)
del car4.color
print(car4.color)
