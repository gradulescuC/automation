class Cinema:
    def __init__(self, nume, adresa, capacitate):
        self.nume = nume
        self.adresa = adresa
        self.capacitate = capacitate
        self.filme = [] # daca nu punem niciun _ in mod implicit accesul la atribut sau metoda este public
        self._bilete_vandute = 0 # atributele protected se pot defini prin caracterul _
        self.__total_incasari = 50000 # atributele private se pot defini prin caracterul __
        self.faliment = False

    def add_film(self, film):
        self.filme.append(film)

    def remove_film(self, film):
        self.filme.remove(film)

    def rulare_filme(self):
        print('Filmele ruleaza la', self.nume, 'cinema:')
        for film in self.filme:
            print('-', film)

    def get_total_incasari(self):
        return self.__total_incasari

    def vinde_bilete(self, numar_bilete_vandute):
        self._bilete_vandute +=numar_bilete_vandute

    def set_total_incasari(self, valoare_modificare_total, operatie):
        if operatie == "remove" and self.__total_incasari >0:
            self.__total_incasari -= valoare_modificare_total
        elif operatie == "remove" and self.__total_incasari ==0:
            self.faliment = True
        else:
            self.__total_incasari += valoare_modificare_total

    def delete_total_incasari(self):
        self.__total_incasari  = 0

cinema_afi = Cinema('Hollywood', 'ParkLake', 150)
print(f"Filmele care ruleaza la cinema afi sunt:  {cinema_afi.filme}") # am accesat un atribut (lista) din clasa Cinema care e public. Atributul va putea fi accesat fara probleme
print(f"La cinema afi s-au vandut: {cinema_afi._bilete_vandute} bilete" ) # am accesat un atribut protected, care nu este returnat ca si sugestii in lista de atribute a obiectului. Cu toate astea el va putea fi accesat fara probleme
# print(cinema_park_lake.__total_incasari) # am accesat un atribut private care nici nu este returnat ca si sugestii si nici nu va putea fi accesat. Vom primi eroare
# print(cinema_park_lake._Cinema__total_incasari) # am accesat un atribut private direct prin intermediul clasei si nu a mai returnat eroare

# print(cinema_afi.__total_incasari)
# cinema_afi.floricele = -50 # aici de fapt am creat un nou atribut specific pentru obiectul asta (nu va fi disponibil pentru alt obiect)
cinema_afi.set_total_incasari(30, "add") # am apelat setterul
# print(cinema_afi.floricele)
print(f"Totalul de incasari inainte de apelarea deleterului este: {cinema_afi.get_total_incasari()}") # am apelat getterul
cinema_afi.delete_total_incasari()
print(f"Totalul de incasari dupa apelarea deleterului este: {cinema_afi.get_total_incasari()}") # am apelat getterul
"""
Atunci cand avem de a face cu atribute private (mai ales) sau protected de regula se definesc
ceea ce se numesc getter (metoda pentru extragerea valorii din atribut), setter (metoda
pentru actualizarea valorii din atribut) si deleter (metoda pentru stergerea valorii din atribut)
"""

# cinema_1 = Cinema('Hollywood', 'ParkLake', 150)
# print(cinema_1.floricele) # obiectul asta nu va avea acces la atributul floricele
