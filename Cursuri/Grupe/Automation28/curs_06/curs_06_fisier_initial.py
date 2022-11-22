"""
POO = Programare orientata pe obiecte
OOP = Object Oriented Programming

Clasa = O structura de tip tipar / blueprint / reteta care serveste drept ghid pentru un element care ar PUTEA exista
				Componentele unei clase:
				- atribute = proprietatile cu care se vor identifica obiectele
										 - pentru a accesa un atribut dintr-o clasa in interiorul acelei clase se foloseste keyword-ul self
										 							in caz contrar se va considera ca se face referinta catre parametrii metodei
								     - pentru a accesa un atribut dintr-o clasa in afara clasei se folosesc urmatoarele:
								      					a) un obiect instantiat din acea clasa
								      					b) decoratorul @staticmethod pentru a accesa atributele si metodele clasei
								      					c) prin conceptul de mostenire a unei clase (vom discuta la cursul 7)
								     - atributele pot avea valori implicite daca exista niste valori general valabile
								     - daca nu exista valori general valabile atunci atributele vor avea valoarea initiala None
				- metode = actiunile pe care le poate face un obiect
										ATENTIE!!! Metodele sunt de fapt niste functii create in interiorul clasei
										 In afara clasei = functii
										 In interiorul clasei = metode

Obiect = instanta a clasei, reprezentare reala a tiparului reprezentat de clasa
					pot sa instantiez oricate obiecte dintr-o anumita clasa

Constructor = Element care va fi folosit pentru instantierea obiectelor dintr-o clasa
							Scopul unui constructor este de a ajuta sistemul sa instantieze obiectul dintr-o clasa
							Exista doua tipuri de constructori:
							a) constructor explicit care obliga utilizatorul sa populeze anumite atribute la instantierea	obiectului
														si daca este cazul sa defineasca o regula de populare a atributelor
						  b) constructor implicit care este apelat automat atunci cand nu exista un constructor explicit definit

						  Pot sa definesc mai multi constructori in aceeasi clasa atata timp cat vor avea un numar diferit de parametri
						  						(method overloading) - polimorfism -> In python nu e posibila definirea mai multor constructori
"""

class Masina:
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
		faruri = "oprite"
		viteza_curenta = 0


		# def __init__(self,culoare,model,nivel_dotare,forma, propulsie,consum,numar_locuri,viteza_maxima):
		# 		if culoare == "orange":
		# 				self.culoare = 'portocaliu'
		# 		else:
		# 				self.culoare = culoare
		# 		self.model = model
		# 		self.nivel_dotare = nivel_dotare
		# 		self.forma = forma
		# 		self.propulsia = propulsie
		# 		self.consum = consum
		# 		self.numar_locuri = numar_locuri
		# 		self.viteza_maxima = viteza_maxima

		"""
		Actiuni:
		- pornire
		- accelerare
		- decelerare
		- oprire
		- drift
		- claxon
		"""

		def porneste_masina(self):
				self.faruri = "pornite"
				print("Am pornit masina")

		def accelereaza_masina(self,valoare_accelerare):
				if self.viteza_curenta==self.viteza_maxima \
								or self.viteza_curenta+valoare_accelerare>self.viteza_maxima \
								or self.viteza_curenta - valoare_accelerare > 20:
						self.viteza_curenta = self.viteza_maxima
						print("Ati atins deja viteza maxima, nu mai puteti accelera")
				else:
						self.viteza_curenta += valoare_accelerare
						print(f"Am accelerat cu {valoare_accelerare} km/h")

		def decelereaza_masina(self,valoare_decelerare):
				if self.viteza_curenta>0 and self.viteza_curenta>valoare_decelerare:
						self.viteza_curenta-=valoare_decelerare
						print(f"Am decelerat cu {valoare_decelerare} km/h")
				else:
						self.viteza_curenta = 0

		def opreste_masina(self):
				if self.viteza_curenta==0:
						self.faruri = "oprite"
						print("Am oprit masina")

		def drift_masina(self,viteza_drift):
				if self.viteza_curenta - viteza_drift >20:
						self.viteza_curenta +=viteza_drift
						print("Masina face derapaj controlat")

		def claxoneaza_masina(self):
				print("tit tit")

print("Instructiune in afara if-ului")

if __name__ == "__main__":
		print("Instructiune in interiorul if-ului")
		# culoare,model,nivel_dotare,forma, propulsie,consum,numar_locuri,viteza_maxima
		# bmw = Masina("rosu","X5","confort","suv","benzina","a1",4,150)
		bmw = Masina()
		print(f"Masina bmw are culoarea {bmw.culoare}")
		bmw.tractiune = "fata"
		print(f"Masina bmw are tractiunea {bmw.tractiune}")
		print(f"Culoarea implicita din clasa Masina este {Masina.culoare}")
		print(f"Tractiunea implicita din clasa Masina este {Masina.tractiune}")

		# skoda = Masina("albastru","fabia","premium","break","hybrid","a1",4,180)
		skoda = Masina()
		skoda.an_fabricatie = 2021
		print(f"Masina skoda a fost fabricata in anul {skoda.an_fabricatie}")
		bmw.an_fabricatie = 2020
		print(f"Masina bmw a fost fabricata in anul {bmw.an_fabricatie}")

		bmw.porneste_masina()
		print(f"Momentan farurile masinii bmw sunt {bmw.faruri}")
		bmw.accelereaza_masina(10)
		print(f"Viteza curenta a masinii bmw este {bmw.viteza_curenta}")
		bmw.decelereaza_masina(5)
		print(f"Viteza curenta a masinii bmw este {bmw.viteza_curenta}")
		bmw.accelereaza_masina(180)
		print(f"Viteza curenta a masinii bmw este {bmw.viteza_curenta}")

		volkswagen = Masina()
		print(volkswagen.viteza_curenta, volkswagen.viteza_maxima, volkswagen.culoare, volkswagen.model)

print("Instructiune dupa if")