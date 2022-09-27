"""
explicati urmatoarele chestii:
    -Ce este un for, cand se foloseste si cum se foloseste:
Este un mod prin care se programeaza repetarea unei secvente de operatiuni,
    -Ce este un for each, cand se foloseste si cum se foloseste
-Este o soliutie de iterare a unei secvente de operatiuni cu numar finit de executie atribuindu-se unei variabile
temporare o valoare
 in functie de  parametri altei variabile
    -Care e diferenta intre for si foreach
    -Ce este un while, cand se foloseste si cum se foloseste.
Este creearea unei bucle
"""
"""Clasa Cerc
Atribute: raza, culoare
Constructor pt ambele atribute
Metode:
descrie_cerc() - va PRINTA culoarea si raza
aria() - va RETURNA aria 
diametru() 
circumferinta()
"""


class Cerc:  # definim clasa cerc cu litera mare
    # aici trecem atrubutele(fields)
    raza = 0
    culoare = None

    # definim constructorul
    def __init__(self, raza, culoare):
        self.raza = raza
        self.culoare = culoare

    # aici facem metodele
    def descrie_cerc(self):
        culoare = self.culoare
        raza = self.raza
        return f'Cercul nostru are culoarea {culoare} si are o raza de {raza}'

    def aria(self, ):
        aria = (self.raza ** 2) * 3.14
        return aria

    def diametru(self, ):
        diametru = 2 * self.raza
        return diametru

    def circunferinta(self):
        circumferinta = 2 * self.raza * 3.14
        return circumferinta


print('------Cerc2--------')
cerc1 = Cerc(8, 'Galben')
print(cerc1.descrie_cerc())
print(f'Aria cercului este: {cerc1.aria()}')
print(f'Diametrul ceruclui este: {cerc1.diametru()}')
print(f'Circumferinta cerecului este: {cerc1.circunferinta()}')
print(f'Am creat Cercul1 despre care putem spune :\n{cerc1.descrie_cerc()}\n-are culoarea {cerc1.culoare}'
      f'\n-raza sa este de {cerc1.raza} fapt careia ii datoram urmatoarele:'
      f'\nAria: {cerc1.aria()}  Diametrul este: {cerc1.diametru()}  Circumferinta:{cerc1.circunferinta()} ')
print('------Cerc2--------')
cerc2 = Cerc(12, 'Bleumarin')
print(cerc2.descrie_cerc())
cerc2.raza = 8
print(f'Aria cercului este: {cerc2.aria()}')
print(f'Diametrul ceruclui este: {cerc2.diametru()}')
print(f'Circumferinta cerecului este: {cerc2.circunferinta()}')
print(f'Am creat Cercul1 despre care putem spune :\n{cerc2.descrie_cerc()}\n-are culoarea {cerc2.culoare}'
      f'\n-raza sa este de {cerc2.raza} fapt careia ii datoram urmatoarele:'
      f'\nAria: {cerc2.aria()}  Diametrul este: {cerc2.diametru()}  Circumferinta:{cerc2.circunferinta()} ')


"""
2. 
Clasa Dreptunghi
Atribute: lungime, latime, culoare
Constructor pt toate atributele
Metode:
descrie()
aria()
perimetrul()
schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va 
suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().
"""


class Dreptunghi:
    lungime = 0
    latime = 0
    culoare = None

    def __init__(self, lungime, latime, culoare):
        self.lungime = lungime
        self.latime = latime
        self.culoare = culoare

    def descriere_dreptunghi(self):
        return f'Avem un dreptunghi {self.culoare} lung de {self.lungime} si lat de {self.latime}'

    def aria(self):
        aria = self.lungime*self.latime
        return aria

    def perimetru(self):
        perimetru = (self.lungime+self.latime)*2
        return perimetru

    def schimbare_culoare(self, culoare_noua):
        # culoare_noua = input('Schimbati culoarea:') - daca foloseam asta in RUN dupa printul rezultatului
        # imi afisa si un NONE, asta inseamna ca doar cu RETURN nu apare problema asta cu NONE?
        self.culoare = culoare_noua


print('----------Drepunghi1--------------')
dreptunghi1 = Dreptunghi(10, 5, 'Maro')
print(dreptunghi1.descriere_dreptunghi())
print(f'Aria este: {dreptunghi1.aria()}')
print(f'Perimetrul este :{dreptunghi1.perimetru()}')
# print(dreptunghi1.schimbare_culoare()) asa a fost apelata functia
dreptunghi1.schimbare_culoare(input('Schimbam culoarea dreptunghiului in: '))
print(dreptunghi1.descriere_dreptunghi())
print('----------Drepunghi2--------------')
dreptunghi2 = Dreptunghi(9.5, 7.35, 'Bleumarin')
print(dreptunghi2.descriere_dreptunghi())
print(f'Aria este: {dreptunghi2.aria()}')
print(f'Perimetrul este: {dreptunghi2.perimetru()}')
# print(dreptunghi2.schimbare_culoare()) asa a fost apelata functia
dreptunghi2.schimbare_culoare(input('Schimbam culoarea dreptunghiului in: '))
print(dreptunghi2.descriere_dreptunghi())


"""
3.
Clasa Angajat
Atribute: nume, prenume, salariu
Constructor pt toate atributele
Metode:
descrie()
nume_complet()
salariu_lunar()
salariu_anual()
marire_salariu(procent)
"""


class Angjat:
    nume = None
    prenume = None
    salariu = 0

    def __init__(self, nume, prenume, salariu):
        self.nume = nume
        self.prenume = prenume
        self.salariu = salariu

    def descriere_angajat(self):
        return f'Date angajat: \nPrenume: {self.prenume};\nNume: {self.nume}; \nSalar: {self.salariu} Euro.'

    def nume_complet(self,):
        nume_complet = self.prenume + ' ' + self.nume
        return f'Numele complet a angajatului este: {nume_complet}'

    def salariu_lunar(self):
        salar = self.salariu
        return salar

    def salariu_anual(self):
        salar_anual = self.salariu_lunar() * 12
        return salar_anual

    def marire_salariu(self, marire):
        self.salariu = self.salariu_lunar() + (self.salariu_lunar() * (marire / 100))



angajat1 = Angjat('Popovici', 'Maria', 500)
print(angajat1.descriere_angajat())
print(angajat1.nume_complet())
print(f'{angajat1.nume_complet()} are salarul lunar de {angajat1.salariu_lunar()} Euro')
print(f'Angajatul {angajat1.nume_complet()}, anual incaseaza prin salar {angajat1.salariu_anual()} Euro')
angajat1.marire_salariu(int(input('Procentaj de marire acordat angajatului este: ')))
print(angajat1.salariu)