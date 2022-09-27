from application.calc import MiniCalc

class TestMiniCalc:
    def setup_method(self):
        print('Se executa la inceput')
        self.calc = MiniCalc(5, 5)

    def teardown_method(self):
        print('Se executa la final')

    def test_init(self):
        assert self.calc.a == 5     #  a este incorect
        assert self.calc.b == 5    #  b este incorect

    def test_adunare(self):
        assert self.calc.adunare() == 9, 'Adunarea nu functioneaza corect'

    def test_scadere(self):
        assert self.calc.scadere() == 0, 'Scaderea nu functioneaza corect'

    def test_inmultire(self):
        assert self.calc.inmultire() == 25, 'Inmultirea nu functioneaza corect'

    def test_impartire(self):
        assert self.calc.impartire()==1,"Impartirea nu functioneaza corect"