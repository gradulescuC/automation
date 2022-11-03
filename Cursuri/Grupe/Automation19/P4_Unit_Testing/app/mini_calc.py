class MiniCalc:
		# constructor explicit
					# se defineste atunci cand vrem sa fortam utilizatorul sa trimita un set de informatii
								# vitale pentru existenta obiectului, fara de care acesta nu ar putea exista

		def __init__(self,a, b):
				self.a = a
				self.b = b

		def adunare(self):
				# am precedat atributele de keyword-ul self pentru ca am vrut sa facem referire la atributele definite in clasa
								# si nu la atribute venite prin parametru in metoa
				return self.a + self.b

		def scadere(self):
				return self.a - self.b

		def inmultire(self):
				return self.a * self.b

		def impartire(self):
				return self.a / self.b