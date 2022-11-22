class Gestiune_Liste():
		lungime = None
		sortata = None
		tip_de_date = None
		lista_elemente = None

		def __init__(self,lista_elemente):
				# am definit un atribut direct in constructor
				self.lista_elemente = lista_elemente

		# [3, 5, 9, 7, 1]   [1, 5, 9, 7, 3]
		# sortare elemente prin metoda bulelor
		def bubble_sort(self):
				for i in range(len(self.lista_elemente)):
						schimbare = False
						for j in range(i+1,len(self.lista_elemente)):
								if self.lista_elemente[i]>self.lista_elemente[j]:
										swap = self.lista_elemente[i]
										self.lista_elemente[i] = self.lista_elemente[j]
										# self.lista_elemente[i], self.lista_elemente[j]  = self.lista_elemente[j], self.lista_elemente[i]
										self.lista_elemente[j] = swap
										schimbare = True
						if schimbare == False:
								break
				self.sortata = True

		# actualizare lungime
		def calculeaza_lungimea(self):
				self.lungime = len(self.lista_elemente)

		# identificare tip de date
		# gasire element
		# inlocuire
if __name__ == "__main__":
		lista = [0, 2, 4, 6, 8]
		# Am instantiat un obiect al clasei Gestiune_Liste
		lista_numere_pare = Gestiune_Liste(lista)
		print(lista_numere_pare)  # printeaza obiectul, adica adresa de memorie la care este salvat elementul meu: <__main__.Gestiune_Liste object at 0x103e66800>
		print(f"Lista nesortata este: {lista_numere_pare.lista_elemente}")
		lista_numere_pare.bubble_sort()
		print(f"Lista sortata este: {lista_numere_pare.lista_elemente}")
		print(f"Este lista sortata? {lista_numere_pare.sortata}")