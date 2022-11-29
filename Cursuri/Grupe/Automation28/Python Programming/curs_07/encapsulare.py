# """
# Encapsulare = restrictionarea accesului la anumite atribute sau metode
# Encapsularea se face prin intermediul unor elemente care poarta numele de modificatori de acces:
# - private = atributul sau metoda definite intr-o clasa sunt vizibile doar in clasa respectiva
# - protected = atributul sau metoda pot fi utilizate in afara clasei
# 						printr-un obiect instantiat din clasa respectiva,
# 						dar acel atribut sau metoda nu va fi sugerat utilizatorului
# - public = atributul sau metoda pot fi utilizate oriunde in afara clasei, si ca vor fi sugerate
# 						utilizatorului la momentul instantierii obiectului
#
# Note importante:
# 1. In java modificatorii de acces sunt specificati in mod explicit
# 				    prin keyword-urile corespunzatoare: public, private, protected
# 	 In python modificatorii de acces sunt specificati in mod indirect in felul urmator:
# 	 - atributele sau metodele public vor fi definite ca atare fara niciun artificiu
# 	 - atributele sau metodele protected for fi precedate de caracterul "_"
# 	 - atributele sau metodele private for fi precedate de dublu "__"
# 2. In python atributul sau metoda protected pot fi accesate oriunde, dar acel atribut sau metoda nu va fi sugerat utilizatorului
#    In java atributul sau metoda protected vor fi accesate doar in acelasi pachet in care se afla clasa
# """
#
#
class Masina_encapsulare:
		culoare = "Fuchsia"
		model = None
		nivel_dotare = "basic"
		tractiune = "spate"
		forma = None
		propulsia = None
		an_fabricatie = None
		numar_inmatriculare = None
		numar_locuri = None
		consum = None
		schimbator = "manual"
		viteza_maxima = 150
		__viteza_curenta = 0
		faruri = "oprite"
		__cost_productie = None # am definit un atribut private
		_numar_piese_vandute = 13 # am definit un atribut protected

		# def accelereaza_masina(self,valoare_accelerare):
		# 		if  self.__viteza_curenta==self.viteza_maxima or self.__viteza_curenta+valoare_accelerare>self.viteza_maxima or self.__viteza_curenta - valoare_accelerare > 20:
		# 				self.__viteza_curenta = self.viteza_maxima
		# 				print("Ati atins deja viteza maxima, nu mai puteti accelera")
		# 		else:
		# 				self.__viteza_curenta += valoare_accelerare
		# 				print(f"Am accelerat cu {valoare_accelerare} km/h")
		# 		print(f"Viteza curenta dupa accelerare este: {self.__viteza_curenta}")
		#
		# def decelereaza_masina(self,valoare_decelerare):
		# 		if self.__viteza_curenta>0 and self.__viteza_curenta>valoare_decelerare:
		# 				self.__viteza_curenta-=valoare_decelerare
		# 				print(f"Am decelerat cu {valoare_decelerare} km/h")
		# 		else:
		# 				self.__viteza_curenta = 0
		# 				print(f"Viteza curenta dupa decelerare este: {self.__viteza_curenta} ")
		# 				raise Exception("Error, valoarea transmisa este mai mica decat 0, am actualizat viteza curenta la 0")

		# pentru a accesa, modifica si sterge valorile de pe un atribut privat ne folosim de conceptul de getter, setter, deleter

		def get_viteza_curenta(self):
				return self.__viteza_curenta

		def set_viteza_curenta(self,valoare_modificare, tip_modificare):
				if tip_modificare == "accelerare":
						if self.__viteza_curenta == self.viteza_maxima or self.__viteza_curenta + valoare_modificare > self.viteza_maxima or self.__viteza_curenta - valoare_modificare > 20:
								self.__viteza_curenta = self.viteza_maxima
								print("Ati atins deja viteza maxima, nu mai puteti accelera")
						elif valoare_modificare > self.viteza_maxima:
								raise Exception("Valoare de accelerare mai mare decat viteza maxima")
						else:
								self.__viteza_curenta += valoare_modificare
								print(f"Am accelerat cu {valoare_modificare} km/h")
								print(f"Viteza curenta dupa accelerare este: {self.__viteza_curenta}")
				elif tip_modificare == "decelerare":
						if self.__viteza_curenta > 0 and self.__viteza_curenta > valoare_modificare:
								self.__viteza_curenta-=valoare_modificare
								print(f"Am decelerat cu {valoare_modificare} km/h")
						else:
							self.__viteza_curenta = 0
							print(f"Viteza curenta dupa decelerare este: {self.__viteza_curenta} ")
							raise Exception("Error, valoarea transmisa este mai mica decat 0, am actualizat viteza curenta la 0")
				else:
						raise Exception("Error, valoare invalida. Este posibil doar accelarare sau decelare")

		def delete_viteza_curenta(self):
				self.__viteza_curenta = None


bmw = Masina_encapsulare()
print(bmw._numar_piese_vandute)
# bmw.accelereaza_masina(-5)
# bmw.decelereaza_masina(-7)
print(f"Viteza curenta a masinii bmw este: {bmw.get_viteza_curenta()}")
bmw.set_viteza_curenta(8,"accelerare")
print(f"Viteza curenta a masinii bmw este: {bmw.get_viteza_curenta()}")
bmw.set_viteza_curenta(7,"decelerare")
bmw.delete_viteza_curenta()
print(f"Viteza curenta a masinii bmw este: {bmw.get_viteza_curenta()}")

# print(bmw.viteza_curenta)
# print(volvo.__cost_productie) # va returna eroare pentru ca atributul este private si nu va fi recunoscut

print("---------------------------------------")

class Masina_encapsulare_decoratori:
		culoare = "Fuchsia"
		model = None
		nivel_dotare = "basic"
		tractiune = "spate"
		forma = None
		propulsia = None
		an_fabricatie = None
		numar_inmatriculare = None
		numar_locuri = None
		consum = None
		schimbator = "manual"
		viteza_maxima = 150
		__viteza_curenta = 0
		faruri = "oprite"
		__cost_productie = None # am definit un atribut private
		_numar_piese_vandute = 13 # am definit un atribut protected

		# def accelereaza_masina(self,valoare_accelerare):
		# 		if  self.__viteza_curenta==self.viteza_maxima or self.__viteza_curenta+valoare_accelerare>self.viteza_maxima or self.__viteza_curenta - valoare_accelerare > 20:
		# 				self.__viteza_curenta = self.viteza_maxima
		# 				print("Ati atins deja viteza maxima, nu mai puteti accelera")
		# 		else:
		# 				self.__viteza_curenta += valoare_accelerare
		# 				print(f"Am accelerat cu {valoare_accelerare} km/h")
		# 		print(f"Viteza curenta dupa accelerare este: {self.__viteza_curenta}")
		#
		# def decelereaza_masina(self,valoare_decelerare):
		# 		if self.__viteza_curenta>0 and self.__viteza_curenta>valoare_decelerare:
		# 				self.__viteza_curenta-=valoare_decelerare
		# 				print(f"Am decelerat cu {valoare_decelerare} km/h")
		# 		else:
		# 				self.__viteza_curenta = 0
		# 				print(f"Viteza curenta dupa decelerare este: {self.__viteza_curenta} ")
		# 				raise Exception("Error, valoarea transmisa este mai mica decat 0, am actualizat viteza curenta la 0")

		# pentru a accesa, modifica si sterge valorile de pe un atribut privat ne folosim de conceptul de getter, setter, deleter

		# decorator este o proprietate prin intermediul careia putem modifica comportamentul unei functii
		@property
		def viteza_curenta(self):
				pass

		@viteza_curenta.getter
		def viteza_curenta(self):
				return self.__viteza_curenta

		@viteza_curenta.setter
		def viteza_curenta(self,valoare_modificare):
				if valoare_modificare > 0 :
						if self.__viteza_curenta == self.viteza_maxima or self.__viteza_curenta + valoare_modificare > self.viteza_maxima or self.__viteza_curenta - valoare_modificare > 20:
								self.__viteza_curenta = self.viteza_maxima
								print("Ati atins deja viteza maxima, nu mai puteti accelera")
						elif valoare_modificare > self.viteza_maxima:
								raise Exception("Valoare de accelerare mai mare decat viteza maxima")
						else:
								self.__viteza_curenta += valoare_modificare
								print(f"Am accelerat cu {valoare_modificare} km/h")
								print(f"Viteza curenta dupa accelerare este: {self.__viteza_curenta}")
				elif valoare_modificare<0:
						if self.__viteza_curenta > 0 and self.__viteza_curenta > valoare_modificare:
								self.__viteza_curenta-=valoare_modificare
								print(f"Am decelerat cu {abs(valoare_modificare)} km/h")
						else:
							self.__viteza_curenta = 0
							print(f"Viteza curenta dupa decelerare este: {self.__viteza_curenta} ")
							raise Exception("Error, valoarea transmisa este mai mica decat 0, am actualizat viteza curenta la 0")
				else:
						print("Nu s-a facut nicio modificare a vitezei")

		@viteza_curenta.deleter
		def viteza_curenta(self):
				self.__viteza_curenta = None

sedane = Masina_encapsulare_decoratori()
print(sedane.viteza_curenta)
sedane.viteza_curenta = 5
print(f"Viteza curenta a masinii sedane este {sedane.viteza_curenta}")
sedane.viteza_curenta = 7
print(f"Viteza curenta a masinii sedane este {sedane.viteza_curenta}")
sedane.viteza_curenta = -5
print(f"Viteza curenta a masinii sedane este {sedane.viteza_curenta}")
del sedane.viteza_curenta
print(f"Viteza curenta a masinii sedane este {sedane.viteza_curenta}")


"""
valoare modificare este negativa, atunci se considera decelerare
valaore modificare este pozitiva, atunci se considera accelerare
"""

