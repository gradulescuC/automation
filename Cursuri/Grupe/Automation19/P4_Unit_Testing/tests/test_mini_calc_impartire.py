from app.mini_calc import MiniCalc

class TestMiniCalcImpartire():
		calc = MiniCalc(6, 7)
		def test_impartire(self):
				assert self.calc.impartire() == 0.8571428571428571