# 1. Polimorfism prin functii cu parametri default
def sir_numere_pare(range_end, range_beginning=0, range_step=1):
		for i in range(range_beginning, range_end + 1, range_step):
				if i % 2 == 0:
						print(f"Numarul {i} este par")
				else:
						print(f"Numarul {i} este impar")

sir_numere_pare(10,0,1)
sir_numere_pare(10,4)
sir_numere_pare(10,range_step=4)

# 2. Polimorfism prin functii cu *args
def calcul_suma_numere(*numbers):
		suma = 0
		for number in numbers:
				suma = suma + number
		return suma


print(calcul_suma_numere(1))
print(calcul_suma_numere(2, 6))
print(calcul_suma_numere(578901256, 789013476, 56))
print(calcul_suma_numere(1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27))


def accesare_elemente_dictionar(**kwargs):
		for key, value in kwargs.items():
				print(f"Detalii despre apa: {key}")
				for key_inner, value_inner in value.items():
						if key_inner == "promovare":
								print(f'Apa {key} are {key_inner}: {value_inner["reclama"]}')
						elif key_inner == "televiziune promovare":
								print(f"Televiziunile pe care se promoveaza sunt:", end=" ")
								for televiziuni in value_inner:
										print(televiziuni, end=" ")
						else:
								print(f"Apa {key} are {key_inner} : {kwargs[key][key_inner]}")

# polimorfism prin definirea a doua clase care contin aceeasi metoda
class America():
		def language(self):
				print("Engleza")


class Romania():
		def language(self):
				print("Romana")

america = America()
romania = Romania()
america.language()
romania.language()

# polimorfism prin reimplementarea metodei din clasa parinte in clasa copil

class Animal():
		def sound(self):
				print("miau")

class Catel(Animal):
		def sound(self):
				print("ham")

catel = Catel()
catel.sound()