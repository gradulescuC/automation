from abc import ABC, abstractmethod
class Animal(ABC):

		def run(self):
				print("go go go ale ale ale")

		@abstractmethod # decorator = element care schimba comportamentul unei clase
		def sound(self):
				pass

		@abstractmethod
		def sleep(self):
				raise NotImplementedError

class Cat(Animal):
		numar_vieti = 9

		def sound(self):
				print("miau")

		def sleep(self):
				print("prrrrr")

pisica_galbena = Cat()
pisica_galbena.sound()
pisica_galbena.sleep()