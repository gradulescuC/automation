from app.mini_calc import Mini_Calc


class TestMiniCalcAdunare():
		def setup_method(self):
				print("Instructiuni executate la inceput")
				self.calc = Mini_Calc()

		def teardown_method(self):
				print("Instructiuni executate la final")

		def test_scadere(self): # toate metodele de test trebuie sa inceapa cu test_
				assert self.calc.scadere(8,4) == 4