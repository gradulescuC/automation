"""

4. Abstractizare = un proces prin care ascundem din fata utilizatorului unele date ale unei functii
									si respectiv o modalitate prin care putem sa fortam clasele copil
									sa implementeze un comportament specific pentru o anumita metoda

Ca sa definim o clasa abstracta, ea trebuie sa mosteneasca clasa ABC (Abstract Base Classs)
"""
from abc import ABC, abstractmethod


class Gradinita(ABC):
		# daca toate metodele din clasa sunt abstracte, atunci clasa se va numi interfata
    # daca cel putin o metoda din acea clasa are comportament implementat, atunci clasa se va numi clasa abstracta
		# daca noi marcam o metoda ca fiind abstracta si nu implementam comportament pentru acea metoda in clasa copil, vom primi o eroare
		# ca sa marcam o metoda ca fiind abstracta trebuie sa punem deasupra ei decoratorul @abstractmethod

		# @abstractmethod
		def joaca(self):
				raise NotImplementedError # i-am spus sistemului sa returneze eroare atunci cand o clasa mostenitoare nu implementeaza comportament pentru metoda asta

		# @abstractmethod
		def somn(self):
				pass # chiar daca noi nu instruim sistemul in mod explicit sa reurneze eroare, el tot o va face daca metoda abstracta nu e implementata in clasa copil
						 # daca nu scriem decoratorul @abstractmethod deasupra metodei sistemul nu va mai returna eroare daca metoda nu este implementata in clasa copil
		#metoda de clasa (classmethod)

		def activitati(self):
				print("Crosetat, desenat si citit")

class Gradinita_privata(Gradinita):
		nr_copii = 0
		adresa = None
		orar = None

		def joaca(self):
				print("Copii sar coarda")

		def somn(self):
				print("Copiii se duc la somn la ora 13:00")

		# daca nu subprascriem o metoda din clasa parinte, ea va fi apelata din clasa parinte.
		# In caz contrar prioritate are metoda cu care s-a facut suprascrierea
		# Reimplementarea metodei activitati in clasa copil este un exemplu de polimorfism

		def activitati(self):
				print("Dansat, cantat si pictat")

# instantierea unui obiect din clasa Gradinita (va fi posibila doar daca metodele din interior nu sunt abstracte)
gradinita = Gradinita()
# instantierea unui obiect din clasa Gradinita_privata
gradinita1 = Gradinita_privata()

# Apelarea metodelor din clasa Gradinita_privara
gradinita1.joaca()
gradinita1.somn()
# Apelam metoda activitati, in primul caz se va apela metoda din clasa Gradinita_privata, iar in al doilea caz cea din clasa Gradinita
gradinita1.activitati()
gradinita.activitati()