from Recap_Sesiune4_plus_5 import fotbalisti_pe_echipe

"""


3. Polimorfism = posibilitatea de a crea o functie care sa poata sa fie apelata sub mai multe forme
									Se poate implementa si prin crearea unor functii cu un numar indefinit de parametri
									prin functii cu parametrii ce au valori implicite sau prin crearea
									a doua functii cu acelasi nume, dar create in clase diferite
"""

"""polimorfism prin functii cu un numar indefinit de argumente"""

# Exemplu 1:
def suma_numere_indef(*args): # caracterul "*" in fata parametrului inseamna ca functia poate sa ia un numar diferit de parametri la fiecare rulare
		suma = 0
		for numar in args: # in cazul asta args este tratat ca o lista
				suma += numar
		return suma

# Apelare functie polimorfica Ex. 1
print(f"Apelarea functiei fara parametri: {suma_numere_indef()}")
print(suma_numere_indef(2))
print(suma_numere_indef(234,5678,234567,2345678))

# Exemplu 2
def afiseaza_fotbalisti(**kwargs): # atunci cand vrem sa accesam dictionare in functii punem doua stelute in fata parametrului
		for key_echipa, value_echipa in kwargs.items():
				for key_jucator, value_jucator in value_echipa.items():
						print(f"La echipa {key_echipa} joaca jucatorul:")
						for key_detalii_jucator, value_detalii_jucator in value_jucator.items():
								print("Detalii jucator", f"{key_detalii_jucator}:{value_detalii_jucator}", sep=" - ", end=",")
						print("\n--------------------------------")

# Apelare functie polimorfica exemplu2
afiseaza_fotbalisti(**fotbalisti_pe_echipe)

""" polimorfism prin functii cu parametri initializati cu valori implicite (default)"""

"""
If a client has over 65 years, then it will be offered to him a discount of 15%.
Otherwise if the customer does not have over 65 years, if the person travels with at least one child they will have a discount of 10%
For both seniors and non seniors it will be applied an additional discount of 10% if they will travel during winter.
Also, for both seniors and non seniors it will be applied a 3% luxury fee if they will travel in the first class (in any season) or 1% handling fee otherwise.
"""

def calculeaza_pret(varsta,sezon,clasa,pret_calatorie,nr_child=0):
		taxa = 0
		discount = 0
		if varsta >= 65:
				discount = 0.15
		else:
				if nr_child >= 1:
						discount = 0.1
		if sezon == "iarna":
				discount += 0.1
		if clasa == 1:
				taxa = 0.03
		else:
				taxa = 0.01
		pret_calatorie = pret_calatorie - pret_calatorie * discount + pret_calatorie * taxa
		return pret_calatorie

# varsta = int(input("Va rugam sa introduceti varsta "))
# sezon = input("Va rugam sa introduceti sezonul calatoriei ")
# clasa = int(input("Va rugam sa introduceti clasa "))
# pret_calatorie = int(input("Va rugam sa introduceti pretul calatoriei "))
# nr_child = int(input("Va rugam sa introduceti numarul de copii "))

# Apelare functie polimorfica cu numar indefinit de parametri:
print(f"Pretul pentru persoana peste 65 de ani este: {calculeaza_pret(67,'iarna',1,50)}") # nu cere valoare pentru al cincilea parametru pentru ca a fost initializat in mod implicit cu valoarea 0
print(f"Pretul pentru persoan sub 65 de ani este: {calculeaza_pret(32,'iarna',1,50,1)}") # am suprascris valoarea implicita a numarului de copii. Suprascrierea are prioritate

""" polimorfism prin mai multe functii cu acelasi nume definite in clase diferite"""

class America():
		limba = "Engleza"
		drapel ="50 states"

		def printeaza_limba_vorbita_in_tara(self):
				print(f"Limba vorbita in america este: {self.limba}")

class Romania():
		limba = "Romana"
		drapel = "tricolorul mandru"

		def printeaza_limba_vorbita_in_tara(self):
				print(f"Limba vorbita in romania este: {self.limba}")

america = America()
romania = Romania()
america.printeaza_limba_vorbita_in_tara()
romania.printeaza_limba_vorbita_in_tara()



