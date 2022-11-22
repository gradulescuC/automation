from app.mini_calc import MiniCalc

class TestMiniCalcInmultire():

		calc = MiniCalc(6, 7)
		def test_inmultire(self):
				assert self.calc.inmultire() == 42