"""
1. Functie care sa calculeze si sa returneze suma a 2 numere
V1
"""
# def adunare(a,b):
#    return (a + b)
#
# print(adunare(int(input('Numarul A:')),int(input('Numarul B:'))))
"""
v2
"""
# def adunare(a,b):
#    return print(a + b)
#
# adunare(int(input('Numarul A:')),int(input('Numarul B:')))

"""
v3
"""
# def adunare(a,b):
#     print(a + b)
#
# adunare(int(input('Numarul A:')),int(input('Numarul B:')))

"""
2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
"""
# def par_sau_impar(cifra):
#     if cifra%2 == 0:
#        return True
#     elif cifra%2 != 0:
#         return False
#
# print(par_sau_impar(11))


"""
3. Functie care returneaza numarul total de caractere din numele tau complet.
(nume, prenume, nume_mijlociu) 
"""

# def lungime_nume(nume, prenume, nume_mijlociu):
#     return print('Numele tau este alcatuit din : ',len(nume+prenume+nume_mijlociu),' litere')
#
# lungime_nume("Rozsi", 'Norbert', 'Daniel')

"""
4. Functie care returneaza aria dreptunghiului
"""
# def aria_dreptunghi(lungime, latime):
#     return print('Aria dreptunghiului este:', lungime*latime)
#
# aria_dreptunghi(7,5)

"""
5. Functie care returneaza aria cercului
"""

# def aria_cercului(raza):
#     return print(float(3.14*raza**2))
#
# aria_cercului(5)

"""
6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu
"""

# def cautare_litera(text, litera):
#     if litera in text:
#         return print(True)
#     else:
#         return print(False)
#
# cautare_litera('Aici introducem textul, dupa virgula litera', 'f')


"""
7. Functie fara return, primeste un string si printeaza pe ecran:
-	Nr de caractere lower case este x
-	Nr de caractere upper case exte y 
"""

# def case_sensitive_count(text):
#     upper = 0
#     lower = 0
#     for i in range(len(text)):
#         if text[i] >= 'a' and text[i] <= 'z':
#             lower += 1
#         elif text[i] >= 'A' and text[i] <= 'Z':
#             upper += 1
#     print('Nr de caractere lower case este=', lower)
#     print('Nr de caractere upper case este=', upper)
#
# case_sensitive_count(str(input('Introduceti un text sa vedem cate litre mari si mici avem:')))


"""
8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive
"""

# lista_nr = [-5,-10,655,45,13,95,-6,54,98,5,-4568,2,487]
# def nr_pozitiv():
#     lista_poz = [i for i in lista_nr if i>= 0] #Gasit, recunosc, dar pare a fi genial
#     print(lista_poz)
# nr_pozitiv()


"""
9.Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA
-	Primul numar x este mai mare decat al doilea nr y
-	Al doilea nr y este mai mare decat primul nr x
-	Numerele sunt egale

"""

# def comparator_numere(x,y):
#     if x > y:
#         print('Primul numar ',x, 'este mai mare decat al doilea nr', y)
#     elif b > x:
#         print('Al doilea nr',y, 'este mai mare decat primul nr',x)
#     else:
#         print('Numerele sunt egale')
#
#
# print(comparator_numere(int(input('Numarul X:')),int(input('Numarul Y:'))))

"""
10. Functie care primeste un numar si un set de numere.
Printeaza ‘am adaugat numarul nou in set’ + returneaza True
Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False
"""
def fun_adauga_la_set(numar,set_de_numere):
    if not numar in set_de_numere:
        set_de_numere.add(numar)
        print('Am adaugat numarul nou', numar, 'in set ' ,set_de_numere, '!')
        return True
    else:
        print('Nu am adaugat numarul in set, acesta exista deja!')
        return False

set_de_numere = {2,8,5,9,78,3}
print(set_de_numere)
fun_adauga_la_set(int(input('Ce numar doriti sa adaugati in set?: ')), set_de_numere)

