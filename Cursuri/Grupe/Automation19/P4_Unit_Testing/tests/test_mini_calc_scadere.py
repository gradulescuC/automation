from app.mini_calc import MiniCalc


class TestMiniCalcScadere():
		calc = MiniCalc(6, 7)

		def test_scadere(self):
				assert self.calc.scadere() == -1