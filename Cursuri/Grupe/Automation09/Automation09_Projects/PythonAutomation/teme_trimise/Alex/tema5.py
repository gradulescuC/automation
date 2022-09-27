#1. Functie care sa calculeze si sa returneze suma a 2 numere

# def calcul_suma(a, b):                                      #definesc o functie cu 2 valori ca argument
#     suma_numere = a + b                                     #definesc o variabila ce prezinta suma a celor 2 valori
#     return suma_numere                                      #folosesc return pentru pentru a returna suma
# Rez = calcul_suma(10, 4)
# print(Rez)                                                  #afisez suma


# #2 Functie care sa returneze TRUE daca un numar este par, FALSE pt impar

# def numar_par(numere):                              #definesc o functie
#     if numere % 2 == 0:                             #conditionez cu if ca numarul sa fie par (%2==0)
#         return True
#     else:                                           #daca nu este par intra pe else si returneaza false
#         return False
#
# rezultat = numar_par(int(input('Introduce un numar: ')))
# print(rezultat)



#3 Functie care returneaza numarul total de caractere din numele tau complet. (nume, prenume, nume_mijlociu)

# def numeComplet(nume, prenume, nume_mijlociu):                               #declar functia
#     return len(nume) + len(prenume) + len(nume_mijlociu)                     #returnez pe aceasi linie de cod numarul total de caractere adunand fiecare nume in parte
#
# print(numeComplet('Patrascoiu', 'Alexandru','Dorin'))                        #afisez nr total de caractere



#4 Functie care returneaza aria dreptunghiului
#
# def calcul_arie(L, l):                                      #am definit functia
#     aria = L * l                                            #am creat o variabila aria ce reprezinta formula ariei dreptunghiului
#     return (f'Aria dreptunghiului este: {aria}')            #am apelat la functia return care se intoarce la variabila si calculeaza
# aria_dreptunghi = calcul_arie(12, 5)                        #am declarat valorile pentru L si l.
# print(aria_dreptunghi)                                      #afisej aria



#5  Functie care returneaza aria cercului
#
# def calcul_arie_cerc(pi, r):                     #am definit functia cu variabilele necesare de calcul
#     arie_cerc = round(pi * r**2)                  #am definit aria cercului rotunjita
#     return (f'Aria cercului este: {arie_cerc}')     #am apelat return pentru a returna valoarea ariei
# x = int(input('Introduceti raza: '))                #am definit o variabila unde pot memora ce valoare doresc pt raza
# aria_cercului = calcul_arie_cerc(3.1415, x)
# print(aria_cercului)                                #afisez aria calculata



#6  Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu

# avem nevoie de un string pe care sa-l declaram
# vom avea nevoie de un input unde comparam ce am introdus de la tastatura cu stringul declarat
# avem nevoie de o functie care sa caute si sa identifice caracterul introdus!
# avem nevoie de return care sa ne returneze true or false

# def find_character(string):
#     if caracter in string:
#         return True
#     else:
#         return False
#
# caracter = str(input('Introdu un caracter: '))
# string = find_character('Hocus Pocus')
# print(string)

#7 Functie fara return, primeste un string si printeaza pe ecran:
#Nr de caractere lower case este x
#Nr de caractere upper case este y
# nu voi folosi return deci oare merge cu if / elif?
#trebuie sa definesc o functie care sa includa un input
#voi itera dupa if cu lower case si voi itera din nou cu upper dupa elif
#trebuie sa numere literele mici si literele mari


# def string(cuvant):
#     lower=0
#     upper=0
#     for i in cuvant:
#         if i.islower() == True:
#             lower+=1
#         else:
#             upper+=1
#     print("Lower case letters:", lower)
#     print("Upper case letters:", upper)
#
#
# cuvant =input('Introdu un cuvant: ')
# string(cuvant)

#8 Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive

# def numere_pozitive(lista):                 #am definit functia
#     listaTest = []
#     for i in range(len(lista)):             #folosesc for pentru a itera intreaga lista
#         if lista[i]>0:                      #conditionez ca valorile din lista sa fie pozitive
#             listaTest.append(lista[i])      #valorile pozitive se vor adauga in lista
#     return(listaTest)                       #returnez valorile pozitive
#
#
# lista = []                                                       #am creat o lista unde se vor afisa numerele pozitive
# for i in range(1,11):
#     lista.append(int(input(f"Introduceti numarul {i} ")))       #voi adauga toate numerele introduse de la tastatura intr-o lista cu append
#
# numere_pozitive(lista)                                          #am apelat functia
# lista_numere_pozitive = numere_pozitive(lista)
# print(f"Numerele pozitive sunt: {lista_numere_pozitive}")       #afisez doar numerele pozitive

#9 . Functie care nu returneaza nimic. Primește 2 numere si PRINTEAZA
#Primul numar x este mai mare decat al doilea nr y
#Al doilea nr y este mai mare decat primul nr x
#Numerele sunt egale.
#am nevoie de o functie cu 2 variabile
#voi folosi if, elif si else pt 3 cazuri de comparatie.
#voi da niste valori pt cele 2 variabile

# def numere_x_y(a,b):
#     if a > b:
#         print('Primul numar este mai mare')
#     elif a < b:
#         print('Al doilea numar este mai mare')
#     else:
#         print('Numerele sunt egale')
# a = 2
# b = 3
# result=numere_x_y(a,b)
# print(result)

#10  Functie care primeste un numar si un set de numere.
#Printeaza ‘am adaugat numarul nou in set’ + returneaza True
#Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
#voi defini o lista cu numere
#voi defini o functie care sa ia un numar de la tastatura si sa-l adauge in lista .add sau cu .append


# def adaugare(numar,lista):
#     for numbers in lista:
#         if not numar in lista:
#             lista.add(numar)
#             print(f'Am adaugat numarul {numar}, in setul {lista}!')
#             return True
#         else:
#             print('Nu am adaugat numarul in set, acesta exista deja!')
#             return False
# numar=int(input('Introdu un numar: '))
# lista = {1,3,12,7,21,33,43,51}
# adaugare(numar,lista)


