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


    def vinde_bilete(self, numar_bilete_vandute):
        self._bilete_vandute +=numar_bilete_vandute

    # am folosit un decorator pentru a defini o proprietate custom.
    # prin intermediul careia vom avea acces la atributele getter, setter si deleter

    # un decorator este o modalitate prin care putem sa modificam comportamentul unei metode fara sa ii modificam logica

    @property
    def total_incasari(self):
        pass

    @total_incasari.getter
    def total_incasari(self):
        return self.__total_incasari

    @total_incasari.setter
    def total_incasari(self, valoare_modificare_total): # la setterul definit prin property trebuie sa avem un singur parametru care e valoarea cu care se modifica
            self.__total_incasari += valoare_modificare_total

    @total_incasari.deleter
    def total_incasari(self):
        self.__total_incasari = 0

cinema_afi = Cinema('Hollywood', 'ParkLake', 150)
print(f"Filmele care ruleaza la cinema afi sunt:  {cinema_afi.filme}") # am accesat un atribut (lista) din clasa Cinema care e public. Atributul va putea fi accesat fara probleme
print(f"La cinema afi s-au vandut: {cinema_afi._bilete_vandute} bilete" ) # am accesat un atribut protected, care nu este returnat ca si sugestii in lista de atribute a obiectului. Cu toate astea el va putea fi accesat fara probleme
# print(cinema_park_lake.__total_incasari) # am accesat un atribut private care nici nu este returnat ca si sugestii si nici nu va putea fi accesat. Vom primi eroare
# print(cinema_park_lake._Cinema__total_incasari) # am accesat un atribut private direct prin intermediul clasei si nu a mai returnat eroare

# print(cinema_afi.__total_incasari)
# cinema_afi.floricele = -50 # aici de fapt am creat un nou atribut specific pentru obiectul asta (nu va fi disponibil pentru alt obiect)
# print(cinema_afi.floricele)

"""
Atunci cand avem de a face cu atribute private (mai ales) sau protected de regula se definesc
ceea ce se numesc getter (metoda pentru extragerea valorii din atribut), setter (metoda
pentru actualizarea valorii din atribut) si deleter (metoda pentru stergerea valorii din atribut)
"""

# cinema_1 = Cinema('Hollywood', 'ParkLake', 150)
# print(cinema_1.floricele) # obiectul asta nu va avea acces la atributul floricele

# Apelarea getterului:
print(f"Incasarile accesate prin getter: {cinema_afi.total_incasari}") # atentie!!! nu se mai pun cele doua paranteze rotunde

# Apelarea setterului:
cinema_afi.total_incasari = 60

print(f"Incasarile accesate prin getter dupa apelarea setterului: {cinema_afi.total_incasari}") # atentie!!! nu se mai pun cele doua paranteze rotunde

# Apelarea deleterului
del cinema_afi.total_incasari

print(f"Incasarile accesate prin getter dupa apelarea deleterului: {cinema_afi.total_incasari}") # atentie!!! nu se mai pun cele doua paranteze rotunde

