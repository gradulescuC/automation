# 1. Clasa Cerc
# Atribute: raza, culoare
# Constructor pt ambele atribute
# Metode:
# descrie_cerc() - va PRINTA culoarea si raza
# aria() - va RETURNA aria
# diametru()
# circumferinta()

# class Cerc:
#     raza = 15
#     culoare = 'rosu'
#
#
#     def __init__(self,culoare,raza):
#         self.raza = raza
#         self.culoare = culoare
#
#     def descriere_cerc(self,culoare, raza):
#         print(f'Culoarea cercului este {culoare} si are raza de {raza}')
#
#     def aria(self,aria):
#         self.aria = aria
#         return aria
#
#     def diametru(self,diametru):
#         self.diametru= diametru
#
#     def circumferinta(self,circumferinta):
#         self.circumferinta = circumferinta
#
# cerc1 = Cerc
# cerc1.culoare = 'Albastru'
# cerc1.raza = 20
# cerc1.aria = 3.14*(cerc1.raza*cerc1.raza)
# cerc1.diametru = 2* cerc1.raza
# cerc1.circumferinta = 3.14*cerc1.diametru
# print(f'Cercul este {cerc1.culoare}, si are raza {cerc1.raza} cm, circumferinta {cerc1.circumferinta}, diametrul {cerc1.diametru} si  aria {cerc1.aria}')

# 2. Clasa Dreptunghi
# Atribute: lungime, latime, culoare
# Constructor pt toate atributele
# Metode:
# descrie()
# aria()
# perimetrul()
# schimba_culoarea(noua_culoare) - aceasta metoda nu returneaza nimic. Ea va lua ca si param o noua culoare si va suprascrie atributul self.culoare. Puteti verifica schimbarea culorii prin apelarea metodei descrie().

# class Dreptunghi:
#     lungime = 12
#     latime = 10
#     culoare = 'negru'
#
#     def __init__(self):
#         return
#          self.lungime = lungime
#          self.latime = latime
#          self.culoare = culoare
#
#     def descriere(self,lungime,latime,culoare):
#         print(f'Lungime = {lungime}, latime ={latime}, culoarea este {culoare}')
#
#     def aria(self,lungime,latime):
#         self.aria =lungime*latime
#         return self.aria
#
#     def perimetru(self,lungime,latime):
#         self.perimetru = 2*(lungime+latime)
#         return self.perimetru
#
# dreptunghi1 = Dreptunghi(20,10,'rosu')
# print(dreptunghi1.aria(20,10))
# print(dreptunghi1.perimetru(20,10))
# print(dreptunghi1.descriere(20,10,'rosu'))


# SAU
#     def descriere(self, lungime, latime, culoare):
#          return (f'Lungime = {lungime}, latime ={latime}, culoarea este {culoare}')
#
#
#     def aria(self,lungime,latime):
#          self.aria =lungime*latime
#          return self.aria
#
#     def perimetru(self,lungime,latime):
#          self.perimetru = 2*(lungime+latime)
#          return self.perimetru
#
#
# dreptunghi2 = Dreptunghi()
# # dreptunghi2.lungime = 12
# # dreptunghi2.latime= 10
# dreptunghi2.culoare = 'maro'
# print(dreptunghi2.aria(12,10))
# print(dreptunghi2.perimetru(12,10))
# print(dreptunghi2.descriere(12,10,'verde'))
# print(dreptunghi2.culoare)






# 3.Clasa Angajat
# Atribute: nume, prenume, salariu
# Constructor pt toate atributele
# Metode:
# descrie()
# nume_complet()
# salariu_lunar()
# salariu_anual()
# marire_salariu(procent)

#
# class Angajat:
#     nume = None
#     prenume = None
#     salariu = 0
#
#     def __init__(self):   #daca adaugam constructor cu atribute atunci nu putem accesa
#        return
#         # self.nume = nume                             # functiile decat daca trecem atributele
#         # self.prenume = prenume
#         # self.salariu = salariu

#     def descriere(self,nume,prenume,salariu):
#         return (f'Angajatul cu numele {nume} {prenume} are salariul lunar de {salariu} euro. ')
#
#     def nume_complet(self,nume,prenume):
#         return (f'Numele cpmplet este {nume} {prenume}')
#
#     def salariu_lunar(self,salariu):
#         return (f'Salariul lunar este {salariu}')
#
#     def salariu_anual(self,salariu):
#         salariu_anual = salariu*12
#         return (f'Salariul anual este {salariu_anual}')
#
#     def marire_salariu(self,procent):
#         procent = 2/10
#         salariu_marit = salariu+ salariu*procent
#         return (f'Salariul a fost marit cu {procent} % si dupa marire este {salariu_marit} euro')
#
# angajat1 = Angajat()
# print(angajat1.descriere('Florea','Ion', 5000))
# print(angajat1.salariu_anual(5000))
# angajat2= Angajat()
# nume ='Cretu'
# prenume ='Mihai'
# salariu= 1000
# print(angajat2.nume_complet(nume,prenume))
# print(angajat2.salariu_lunar(salariu))
# print(angajat2.salariu_anual(salariu))
# print(angajat2.marire_salariu(salariu))
# angajat3 =Angajat()
# nume = 'Vlad'
# prenume = 'George'
# salariu = 3000
# print(angajat3.descriere(nume,prenume,salariu))
# print(angajat3.salariu_lunar(salariu))
# print(angajat3.salariu_anual(salariu))
# print(angajat3.marire_salariu(salariu))

### fara constructor

# class Angajati:
#     nume= None
#     prenume =None
#     salariu = 0
#
#     def nume_complet(self,nume,prenume):
#         return f'Numele complet este {nume} {prenume}. '
#
#     def salariu_lunar(self,salariu):
#         return f'Salriul lunar este {salariu} lei.'
#     def salariu_anual(self,salariu):
#         salriu_anual = salariu*12
#         return f'Salariul anual este {salriu_anual} lei.'
#
#     def descriere_angajat(self,nume,prenume,salariu):
#         return  f'Angajatul se numeste {nume} {prenume} si are un salariul lunar de {salariu} lei.'
#
# nume = 'Victor'
# prenume = 'Ion'
# salariu = 1500
# angajat1 = Angajati()
# print(angajat1.descriere_angajat(nume,prenume,salariu))
# print(angajat1.salariu_lunar(salariu))
# print(angajat1.salariu_anual(salariu))
# angajat2 = Angajati()
# nume = 'Misu'
# prenume = 'Cristi'
# salariu = 2500
# print(angajat2.descriere_angajat(nume,prenume,salariu))
# angajat3 = Angajati()
# nume = 'Vlad'
# prenume = 'George'
# salariu = 3000
# print(angajat3.descriere_angajat(nume,prenume,salariu))


#####Rezolvat



# 4.Clasa Factura
# Atribute: seria (va fi constanta, nu trebuie constructor, toate facturile vor avea aceeasi serie), numar, nume_produs, cantitate, pret_buc
# Constructor: toate atributele, fara serie
# Metode:
# schimba_cantitatea(cantitate)
# schimba_pretul(pret)
# schimba_nume_produs(nume)
# genereaza_factura() - va printa tabelar daca reusiti
# Factura seria x numar y
# Data: generati automat data de azi
# Produs | cantitate | pret bucata | Total
# Telefon |      7       |       700       | 49000
# Indiciu pt data: https://www.geeksforgeeks.org/get-current-date-using-python/

class Factura:
    seria = 'ff54321'
    numar_fact = 13082022
    nume_produs = 'bicicleta'
    cantitate = 5
    pret_buc = 500

    def __init__(self,nf,numeP,cant,pret):
        self.numar_fact =nf
        self.nume_produs= numeP
        self.cantitate=cant
        self.pret_buc = pret



# 5. Clasa Cont
# Atribute: iban, titular_cont, sold
# Constructor pentru toate
# Metode:
# afisare_sold() - Titularul x are in contul y suma de n lei
# debitare_cont(suma)
# creditare_cont(suma)




# BONUS: (daca aveti timp si doriti sa lucrati suplimentar)
#
# 6.Clasa Masina
#
# Atribute: marca, model, viteza maxima, viteza_actuala, culoare, culori_disponibile (set), inmatriculata (bool)
# Culoare = gri - toate masinile cand ies din fabrica sunt gri
# Viteza_actuala = 0 - toate masinile stau pe loc cand ies din fabrica
# Culori disponibile = alegeti voi 5-7 culori
# Marca = alegeti voi - fabrica produce o singura marca dar mai multe modele
# Inmatriculata = False
#
# Constructor: model, viteza_maxima
#
# Metode:
# descrie() (se vor printa toate atributele, inafara de culori_disponibile)
# inmatriculare() - va schimba atributul inmatriculata in True
# vopseste(culoare) - se va vopsi masina in noua culoare DOAR daca noua culoare e in optiunea de culori displonibile, altfel afisati o eroare
# accelereaza(viteza) - se va accelera la o anumiota viteza, daca viteza e negativa-eroare, daca viteza e mai mare decat viteza_max - masina va accelera pana la viteza maxima
# franeaza() - masina se va opri si va avea viteza 0


# 7. Clasa TodoList
# Atribute: todo (dict, cheia e numele taskului, valoarea e descrierea)
# La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor
# Metode:
# adauga_task(nume, descriere) - se va adauga in dict
# finalizeaza_task(nume) - se va sterge din dict
# afiseaza_todo_list() - doar cheile
# afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
# daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
# Daca acesta raspunde nu - la revedere
# daca raspunde da - il cerem detalii task si salvam nume+detalii in dict



# 7. Clasa TodoList
class TodoList():
# Atribute: to do (dict, cheia e numele taskului, valoarea e descrierea)
# La inceput nu avem taskuri, dict e gol si nu avem nevoie de constructor
    todo = {}
    detalii = None
# Metode:
# adauga_task(nume, descriere) - se va adauga in dict
    def adauga_task(self,nume,descriere):
        self.nume = nume
        self.descriere = descriere
        todo = {self.nume:self.descriere}
        return todo

# finalizeaza_task(nume) - se va sterge din dict
    def finalizeaza_tasc(self,nume):
        todo = {self.descriere}
        return todo
# afiseaza_todo_list() - doar cheile
    def afiseaza_todo_list(self):
        todo = {self.nume}
        return todo


# afiseaza_detalii_suplimentare(nume_task) - in f de numele taskului, printam detalii suplimentare
    def detalii_suplimentare(self,nume_task):
        self.detalii= nume_task
        if self.nume in TodoList:
            print(self.detalii)
        else:
            if self.nume not in TodoList:
                input('Vrei sa il adaug da/nu')
                if 'da':
                    input('introdu detalii suplimentare')
                    todo = input()
                else:
                    print('la revedere!')

task1 = TodoList()

important1 = task1.adauga_task('contract1', 'negociere pret si perioada')
print(important1)
print(task1.finalizeaza_tasc('contract1'))
print(task1.afiseaza_todo_list())
# task2 =TodoList()
# task2.adauga_task('materiale de constructii', 'livrare la adresa str... nr...')
# print(task2.afiseaza_todo_list())
# print(task2.finalizeaza_tasc('materiale constructii'))
# print(task1.afiseaza_todo_list())




# daca taskul nu e in todo list, intrebam utilizatorul daca vrea sa il adauge.
# Daca acesta raspunde nu - la revedere
# daca raspunde da - il cerem detalii task si salvam nume+detalii in dict























