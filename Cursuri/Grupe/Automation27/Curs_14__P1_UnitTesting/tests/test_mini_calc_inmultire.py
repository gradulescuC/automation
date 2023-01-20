from app.mini_calc import Mini_Calc


class TestMiniCalcAdunare():
		def setup_method(self):
				print("Instructiuni executate la inceput")
				self.calc = Mini_Calc()

		def teardown_method(self):
				print("Instructiuni executate la final")

		def test_inmultire(self): # toate metodele de test trebuie sa inceapa cu test_
				assert self.calc.inmultire(8,4) == 32


"""
Se da nr (1234) si trebuie sa definim metoda care sa inverseze numarul

def metoda_calcul(input1)
	set instructiuni

def test_metoda_calcul(string)
				metoda_calcul(val1, val2) == input.reverse

a = 1234
reverse = string(reverse) + a%10

digit = a%10
reverse = reverse * 10 + digit
"""