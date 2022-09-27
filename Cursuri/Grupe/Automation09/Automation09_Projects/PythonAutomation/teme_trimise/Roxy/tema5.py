import math
import pytz as pytz
from datetime import datetime

# Apelati functia de cel putin 2 ori cu valori diferite pentru a testa
# Daca functia are return, printati raspunsul

# 1. Functie care sa calculeze si sa returneze suma a 2 numere
print('-----------1---------')

# def suma(a,b) :
#     s =  a + b
#     print(s)
# suma(2,3)
# suma(5,-4)

# 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
print('-----------2---------')
# def paritate(a):
#     if a % 2 == 0 :
#         print('TRUE')
#     else :
#         print('FALSE')
# paritate(4)
# paritate(10)
# paritate(55)

# 3. Functie care returneaza numarul total de caractere din numele tau complet. (nume, prenume, nume_mijlociu)
print('-----------3---------')
# def numaratoare(n, p, n_m):
#     s = n + p + n_m
#     return(len(s))
# nume = input('Scrieti numele : ')
# prenume = input('Scrieti prenumele : ')
# nume_mijlociu = input('Scrieti numele mijlociu : ')
# print(f'Intregul nume are {numaratoare(nume, prenume, nume_mijlociu)} caractere')

# alta varianta fara return, cu parametrii pusi la apelarea functiei
# def numaratoare1(n, p, n_m):
#     s = n + p + n_m
#     print(f'Numele complet este : {s}')
#     print(f'Intregul nume are {len(s)} caractere')
# numaratoare1('Crisan','Roxana','Sabina')
# numaratoare1('Pop','Razvan','Ionut')

# 4. Functie care returneaza aria dreptunghiului
print('-----------4---------')
# def aria_dr(L, l):
#     aria = L * l
#     return(aria)
# lungime = int(input('Dati lungimea dreptunghiului : '))
# latime = int(input('Dati latimea dreptunghiului : '))
# print(f'Aria dreptunghiului estes : {aria_dr(lungime, latime)} ')

# alta varianta fara return, cu parametrii pusi la apelarea functiei
# def aria_dr1(L, l):
#     aria = L * l
#     print(f'Aria dreptunghiului este : {aria}')
# aria_dr1(5,3)
# aria_dr1(10,5)

# 5. Functie care returneaza aria cercului
print('-----------5---------')
# def aria_cerc(r):
#     aria_cerc = 3.14 * r * r
#     return(aria_cerc)
# raza = int(input('Dati raza cercului : '))
# print(f'Aria cercului este : {aria_cerc(raza)}')

# # alta varianta fara return, cu parametrii pusi la apelarea functiei
# def aria_cerc1(r):
#     aria_cerc = 3.14 * r * r
#     print(f'Aria cercului este : {aria_cerc}')
# aria_cerc1(1)
# aria_cerc1(5)

# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. False daca nu
print('-----------6---------')
# def finder(cuvant, caracter):
#     if caracter in cuvant :
#         x = True
#     else :
#         x = False
#     return(x)
# cuvant = input('Dati un cuvant : ')
# caract = input('Dati caracterul cautat : ')
# print(finder(cuvant,caract))

# alta varianta fara return, cu parametrii pusi la apelarea functiei
def finder(cuvant, caracter):
        if caracter in cuvant:
            print('True')
        else:
            print('False')
finder('casa', 'm')
finder('casa','a')

# 7. Functie fara return, primeste un string si printeaza pe ecran:
# Nr de caractere lower case este x
# Nr de caractere upper case exte y
print('-----------7---------')
def lower_upper(string) :
    x = 0
    y = 0
    for i in string :
        if i.islower() :
            x = x + 1
        else :
            y = y + 1
    print(f'Nr de caract lower case este : {x}')
    print(f'Nr de caract upper case este : {y}')
lower_upper('MamaLigA')
lower_upper('CaSa')

# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
print('-----------8---------')
# def pozitiv1(lista) :
#      lista_poz = []
#      for numar in lista :
#          if numar > 0 :
#              lista_poz.append(numar)
#      print(f'Lista cu numere pozitive este : {lista_poz}')
# pozitiv1([1, 4, -3, 2, -9])
# pozitiv1([1, 4, -3, 2, -9, 10, 99])

# 9. Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA
# Primul numar x este mai mare decat al doilea nr y
# Al doilea nr y este mai mare decat primul nr x
# Numerele sunt egale.
print('-----------8---------')
def marime(x, y):
    if x > y :
        print(f'Primul numar {x} este mai mare decat al doilea numar {y}')
    elif y > x :
        print(f'Al doilea numar {y} este mai mare decat primul numar {x}')
    else :
        print(f'Numerele sunt egale')
marime(2, 6)
marime(3, 3)
marime(5, -3)

# 10. Functie care primeste un numar si un set de numere.
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
print('-----------9---------NU MERGE BINE---------')
# def adaugare_nr(set_numere, numar):
#     if numar in set_numere:
#         print('Nu am adaugat numarul in set. acesta exista deja')
#         print('False')
#     else:
#         print('Am adaugat numarul nou in set')
#         print('True')
#         set_numere.append(numar)
#         print(f'Noul set de numere este : {set_numere}')
# adaugare_nr([1, 3, 6, 8], 9)
# adaugare_nr([1, 3, 6, 8], 3)

# 11. Functie care primeste o luna din an si returneaza cate zile are acea luna
print('-----------OPTIONALE---------')
print('-----------11---------')
# def calendar(luna):
#     if luna == 'Ianuarie' or luna == 'Martie' or luna == 'Mai' or luna == 'Iulie' or luna == 'August' or luna == 'Octombrie' or luna == 'Decembrie':
#         print(f'Luna {luna} are 31 de zile')
#     elif luna == 'Aprilie' or luna == ' Iunie' or luna == 'Septembrie' or luna == 'Noiembrie':
#         print(f'Luna {luna} are 30 de zile')
#     elif luna == 'Februarie':
#         print(f'Luna {luna} are 28 sau 29 de zile')
# calendar('Mai')
# calendar('Februarie')
# calendar('Septembrie')

# 12. Functie calculator care sa returneze 4 valori
# Suma, diferenta, inmultirea, impartirea a 2 numere
# In final vei putea face:
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)
print('-----------12---------')
# def calculator(x, y) :
#     a = x + y
#     b = x - y
#     c = x * y
#     d = (x / y)
#     return a,b,c,d
# a, b, c, d = calculator(10, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

# a, b, c, d = calculator(2, 2)
# print("Suma: ", a)
# print("Diferenta: ", b)
# print("Inmultirea: ", c)
# print("Impartirea: ", d)

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
print('-----------13---------')
# def numaratoare_cifre(lista):
#     dict = {}
#     for i in range(0,10) :
#         dict[i] = lista.count(i)
#     for key, value in dict.items():
#         print(key, value)
# lista1 = [1, 3, 1, 5, 9, 7, 7, 5, 5]
# lista2 = [8, 6, 1, 1, 0, 0, 3, 5, 8, 5, 3, 5]
# numaratoare_cifre(lista1)
# numaratoare_cifre(lista2)

# 14. Functie care primeste 3 numere. Returneaza valoarea maxima dintre ele
print('-----------14---------')
# def maxim(a, b, c) :
#     max_nbr = 0
#     for maximul in a,b,c:
#         if maximul > max_nbr:
#             max_nbr = maximul
#     print(f'Valoarea maxima este {max_nbr}')
# maxim(2, 4, 6)
# maxim(-1, 10, 2)

# 15. Functie care sa primeasca un numar si sa retunreze suma tuturor numerelor de la 0 la acel numar
# Ex: daca dam nr 3
# Suma va fi 6 (0+1+2+3)
print('-----------15---------')
# def suma_toate(nr):
#     suma = 0
#     i = 0
#     while i < nr+1:
#         suma = suma + i
#         i = i + 1
#     print(f'Suma este : {suma}')
# suma_toate(3)
# suma_toate(5)

# 16. Functie in care sa dai un nume romanesc si sa iti printeze pe ecran
# ‘Numele este de baiat’ sau ‘Numele este de fata’
print('-----------BONUS---------')
print('-------------16---------')
# def nume(nume_romanesc):
#         if nume_romanesc[-1] == 'a':
#             print(f'Numele {nume_romanesc} este nume de fata')
#         else:
#             print(f'Numele {nume_romanesc} este nume de baiat')
# nume('Andrei')
# nume('Roxana')
# nume('Andreea')

# 17. Functie care primesete 2 liste de numere (numerele pot fi dublate). Returnati numerele comune
# Ex:
# list1 = [1, 1, 2, 3]
# list2 = [2, 2, 3, 4]
# Raspuns: {2, 3}
print('-------------17---------')
# def commun(lista1, lista2):
#     lista_new = []
#     for i in lista1 :
#         if i in lista2:
#             lista_new.append(i)
#     print(lista_new)
# commun([1, 1, 2, 3], [2, 2, 3, 4])


# Pentru 2 seturi nu liste
# def comun(lista1, lista2):
#     print(lista1.intersection(lista2))
# comun({1, 1, 2, 3}, {2, 2, 3, 4})

# 18. Functie care sa aplice o reducere de pret
# Daca produsul costa 100 lei si aplicam reducere de 10%. Pretul va fi 90
# Tratati cazurile in care reducerea e invalida. De ex o reducere de 110% e invalida
print('-------------18---------')
def reducerea(pret, reducere):
    if reducere >=0 and reducere <= 100 :
        pret_nou = pret - pret * reducere/100
        print(f'Produsul este {pret} lei si aplicam o reducere de {reducere}%, deci pretul final va fi {pret_nou} lei')
    else :
        print(f'Reducerea de {reducere}% nu este valida!')
reducerea(100, 10)
reducerea(100, 110)

# 19. Functie care sa afiseze data si ora curenta din China
print('-------------19---------')
today = datetime.now(pytz.timezone('Asia/Hong_Kong'))
print("Today's date:", today) # data si ora actuala din Romania! nu din China!

