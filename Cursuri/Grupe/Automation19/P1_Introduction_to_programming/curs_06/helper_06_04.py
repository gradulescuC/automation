class Rochii:
    lungime = None
    culoare = None
    material = None
    marime = None
    model = None
    temperatura_spalare = 40
    brand  = None
    pret_vanzare_rochie = None
    lista_magazine =[]

    def __init__(self,lungime,culoare,material,marime,model,brand, pret_vanzare):
        self.lungime = lungime
        self.culoare = culoare
        self.material = material
        self.marime = marime
        self.model = model
        self.brand = brand
        self.pret_vanzare_rochie = pret_vanzare

    def scurteaza_rochia(self,lungime_scurtare):
        self.lungime -=lungime_scurtare

    def calca_rochia(self):
        if self.material == 'bumbac':
            temperatura_calcare = 40
        elif self.material == 'poliester':
            temperatura_calcare = 50
        else:
            temperatura_calcare = 60
        return temperatura_calcare

    def schimba_pret_vanzare_rochie(self, pret_vanzare):
        self.pret_vanzare_rochie=pret_vanzare

    def adauga_magazin_vanzare(self, nume_magazin):
        self.lista_magazine.append(nume_magazin)


prima_rochie = Rochii(50,"rosie","bumbac","L","Clos","Dolce&Gabana",150)
prima_rochie.scurteaza_rochia(5)
print(f"Lungimea curenta a rochiei 'prima rochie' este {prima_rochie.lungime}")
print(f"Temperatura de calcare pentru 'prima rochie' este {prima_rochie.calca_rochia()}")
prima_rochie.schimba_pret_vanzare_rochie(200)
print(f"Rochia are acum pretul de {prima_rochie.pret_vanzare_rochie}")
prima_rochie.adauga_magazin_vanzare("Zara")
prima_rochie.adauga_magazin_vanzare("H&M")
print(prima_rochie.adauga_magazin_vanzare("New Yorker"))
print(f"Lista magazinelor in care se gaseste rochia este: {prima_rochie.lista_magazine}")
print(f"Lista magazinelor in care se gaseste rochia este:")
for magazin in prima_rochie.lista_magazine:
    print(magazin, end=" ")

