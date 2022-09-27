# a. Usor (recomandat)
# 1. Revizualizeaza intalnirea 5 si ia notite in caz ca ti-a scapat ceva
# 2. Vizualizeaza video despre Functii din 'Primii pasi in Programare'
# (Daca nu ai facut-o deja)
# 3. Vizualizeaza video 7 despre OOP din 'Primii pasi in Programare'
# Astfel, la intalnirea LIVE deja va fi a 2-a oara cand vei auzi conceptele
# si sigur ti se vor intipari in minte mai bine.
# https://www.itfactory.ro/8174437-intro-in-programare/
#
# Pentru toate exercitiile
# Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
# Daca functia are return, printati raspunsul
#
# b. Dificultate: usor spre mediu
#
# 1. Functie care sa calculeze si sa returneze suma a 2 numere
#
# def suma (x,y):
#        z= x+y
#        return z
# a = int(input("alege numearul1"))
# b = int(input("alege nr2"))
# c=4
# d= 6
# print(suma(c,b))

#rezolvat




#
# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
# def true_false(numere):
#        if numere %2 ==0:
#         return True
#        else:
#               return False
# numere = int(input('alege un nr'))
# print(true_false(numere))

####Rezolvat

#
# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# (nume, prenume, nume_mijlociu)
# def nr_caractere(nume,prenume,nume_mijlociu):
#        total = len(nume)+len(prenume)+len(nume_mijlociu)
#        return total
# nume = 'Negru'
# prenume = 'Marian'
# nume_mijlociu = 'Alexandru'
# print(nr_caractere(nume,prenume,nume_mijlociu))
#
#
# nume = 'megru'
# prenume = 'darius'
# nume_mijlociu = 'ion'
# print(nr_caractere(nume,prenume,nume_mijlociu))


####Rezolvat



# 4. Functie care returneaza aria dreptunghiului
# def aria_dreptunghi(l1,l2,l3,l4):
#        if l1 == l3 and l2 == l4:
#               aria = l1*l2
#               return aria
#        else:
#               print('nu este un dreptunghi')
#
# a = 6
# b = 5
# c = 6
# d = 5
# print(aria_dreptunghi(a,b,c,d))
#
# e=55
# f=78
# g=56
# h=78
# print(aria_dreptunghi(e,f,g,h))



# 5. Functie care returneaza aria cercului
# def aria_cercului(r,pi):
#        aria = pi*(r*r)
#        return aria
# raza = float(input('scrie raza'))
# pi = 3.14
# print(aria_cercului(raza,pi))
# masa = 58
# print(aria_cercului(masa,pi))


#
# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu
# def find_character(string,x):
#        if x in string:
#               return True
#        else:
#               return False
# nume = "cristi"
# character_to_find = 'c'
# print(find_character(nume,character_to_find))
#
# name = 'Theodor'
# find = 'i'
# print(find_character(name,find))



#
# 7. Functie fara return, primeste un string si printeaza pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case exte y
# def low_upper(string):
#        lower, upper =0,0
#        for i in range(len(string)):
#               if string[i].isupper():
#                      upper+=1
#               if string[i].islower():
#                      lower+=1
#        print(f'nr. de caractere upper case este {upper}')
#        print(f'nr. de caractere lower case este {lower}')
# string = 'Ana are Mere'
# low_upper(string)
# ### Rezolvat




#
# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive

# def pozitive(list):
#     for numere in lista:
#         if numere< 0:
#             continue
#         else:
#             numere>0
#         return numere
# lista = [1,5,49,87,-8,-54,-66,89,99,-7]
# print(pozitive(lista))
#
# ##### nu iese...
# def pozitive(lista_input):
#     lista_pozitive = []
#     for numere in lista_input:
#         if numere > 0:
#             lista_pozitive.append(numere)
#     return lista_pozitive
# lista = [1,5,49,87,-8,-54,-66,89,99,-7]
# rez = pozitive(lista)
# print(rez)



#
# 9. Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.
# def comparatie_nr(x,y):
#     if x>y:
#         print(f'primul numar {x} este mai mare decat al doilea nr. {y}')
#     elif x<y:
#         print(f'Al doilea nr.{y} este mai mare decat primul nr. {x}')
#     else:
#         print('Numerele sunt egale')
# a= 5847899587452
# b = 7895433015
# comparatie_nr(a,b)

##### rezolvat





# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
# def adaugare(x,y):
#     for numere in y:
#         if not x in y:
#             y.add(x)
#             print(f'Am adaugat numarul nou, {x}, in set {y}!')
#             return True
#         else:
#             print('Nu am adaugat numarul in set, acesta exista deja!')
#             return False
# x=7
# y = {2,8,5,9,78,3}
# adaugare(x,y)
#
# a= 2
# b = {2,4,5,6,7,8,9,0,11,}
# adaugare(a,b)

####Rezolvat




#
# c. Optionale (may need google)
#
# 11. Functie care primeste o luna din an si returneaza cate zile are acea luna
# from calendar import monthrange
# def zile_lunar(an,luna):
#     return monthrange(an,luna)[1]
# an = 2022
# luna = int(input("alege luna"))
# print(zile_lunar(an, luna))

#####  SAU
# def zile_luna(an,luni):
#         while x >= 1 and x<=12:
#             if x in luni:
#                 return f'31 zile'
#             elif x ==2:
#                 return f'28 zile'
#             else:
#                 return f'30 zile'
#         else:
#             print('luna invalida')
#
# luni = {1,3,5,7,8,10,12}
# an = 2022
# x= int(input('...'))
# print(zile_luna(an,luni))

#### Rezolvat





#
# 12. Functie calculator care sa returneze 4 valori
# Suma, diferenta, inmultirea, impartirea a 2 numere
#
# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)
#
# def calculator (x,y):
#         a= (x+y)
#         b = (x-y)
#         c = (x*y)
#         d = (x/y)
#         return f'Suma: {a}',\
#                f'Diferenta: {b}',\
#                f'Inmultirea:{c}', \
#                f'Impartirea: {d}'
#
# x=10
# y=2
# print(calculator(x,y))
# #
# a=78
# b=157
# print(calculator(a,b))





# 13. Functie care primeste o lista de cifre (adica doar 0-9)
# Ex: [1, 3, 1, 5, 9, 7, 7, 5, 5]
# Returneaza un DICT care ne spune de cate ori apare fiecare cifra
# => dict {
# 0: 0
# 1 :2
# 2: 0
# 3: 1
# 4: 0
# 5: 3
# 6: 0
# 7: 2
# 8: 0
# 9: 1
# }

from collections import Counter
nr = [1, 3, 1, 5, 9, 7, 7, 5, 5]
print(Counter(nr))


# rezolvat






# 14. Functie care primeste 3 numere
# Returneaza valoarea maxima dintre ele
# def maxima (a,b,c):
#     if a >=b and a>=c:
#         return a
#     elif c>=b and c>=a: #a>b and b<c and a<c or a<b and b<c or a<c:
#         return c
#     else:
#         return b
# a=5
# b=2
# c=3
# print(maxima(a,b,c))

#rezolvat



# 15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3
# Suma va fi 6 (0+1+2+3)
# def suma_numere (a):
#     while a>0:
#         suma = (a*(a+1))/2
#         return suma
# a=3
# print(suma_numere(a))


# BONUS:
#
# 16. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
# ‘Numele este de baiat’ sau ‘Numele este de fata’
# def tip_nume(nume):
#     if nume[-1]== 'a':
#         return 'Numele este de fata!'
#     else:
#         return 'Numele este de baiat!'
#
# nume = input('intro numele:')
# print(tip_nume(nume))

#rezolvat

#
#
# 17. Functie care primesete 2 liste de numere (numerele pot fi dublate)
# Returnati numerele comune
#
# Ex:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Raspuns: {2, 3}
#

# 18. Functie care sa aplice o reducere de pret
# Daca produsul costa 100 lei si aplicam reducere de 10%
# Pretul va fi 90
# Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida
#
# 19. Functie care sa afiseze data si ora curenta din China
#
# 20. Functie care sa afiseze cate zile mai sunt pana la ziua ta / sau pana la craciun daca nu vrei sa ne zici cand e ziua ta :)
