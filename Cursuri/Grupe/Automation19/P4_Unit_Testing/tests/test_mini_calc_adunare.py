from app.mini_calc import MiniCalc

class TestMiniCalcAdunare():
		def setup_method(self):
				print("Se executa la inceput")
				self.calc = MiniCalc(6,7)

		def teardown_method(self):
				print("Se executa la final")

		# Daca vrem sa accesam un element al unei clase in interiorul clasei respective, avem nevoie
						# de keyword-ul self
		# Daca vrem sa accesam un element al unei clase in afara acelei clase,
												# avem nevoie fie de conceptul de mostenire
													# fie de un obiect instantiat din clasa respectiva
		# 1 - > in aceeasi clasa - self
		# 2 -> in alta clasa -> mostenire
		# 3 -> in afara clasei -> obiect instantiat

		def test_adunare(self):
				assert self.calc.adunare() == 13



