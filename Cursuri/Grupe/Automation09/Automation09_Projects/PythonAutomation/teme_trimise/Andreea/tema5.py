# # 1. Functie care sa calculeze si sa returneze suma a 2 numere
# x = int(input('introduceti o cifra'))
# def sum (y):
#     return x + y
# print(sum(3))

# # 2. Functie care sa returneze TRUE daca un numar este par, FALSE pt impar
# def is_even(n):
#     if n % 2 == 0:
#         return True
#     else:
#         return False
# n = int(input('Introduceti un numar'))
# print (is_even(n))

# 3. Functie care returneaza numarul total de caractere din numele tau complet.
# nume = (input('introduceti numele complet'))
# def len_nume():
#     return nume
# print(len(nume))

# 4. Functie care returneaza aria dreptunghiului
# a = (input("Lungime: "))
# b = int(input("latime : "))
# aria = a * b
# def aria_dreptunghi():
#      return aria
# print (f'Aria dreptunghiului este de {a*b}')

# 5. Functie care returneaza aria cercului

# 6. Functie care returneaza True daca un caracter x se gaseste intr-un string dat. Fasle daca nu

# def func():
#     mystr = 'Azi e Marti'
#     if ('A' in mystr) or ('M' in mystr):
#          return True
#     else:
#         return False


# 7. Functie fara return, primeste un string si printeaza pe ecran:
# -	Nr de caractere lower case este x
# -	Nr de caractere upper case exte y

# def string_test(s):
#     d={"UPPER_CASE":0, "LOWER_CASE":0}
#     for c in s:
#         if c.isupper():
#            d["UPPER_CASE"]+=1
#         elif c.islower():
#            d["LOWER_CASE"]+=1
#         else:
#            pass
#     print ("Original String : ", s)
#     print ("Nr de caractere upper case exte : ", d["UPPER_CASE"])
#     print ("Nr de caractere lower case este  : ", d["LOWER_CASE"])
#
# string_test("Ala bala portocala")

# string_test('Zilele saptamanii sunt: Luni, Marti, Miercuri, Joi, Vineri, Sambata, Duminica')


# 8. Functie care primeste o LISTA de numere si returneaza o LISTA doar cu numerele pozitive

# def numar_pozitiv(n):
#     sum = 0
#     for x in range (1,n):
#         if n % x == 0:
#             sum +=x
#     return sum == n
# print(numar_pozitiv(6))

# 9. Functie care nu retunraza nimic. Primeste 2 numere si PRINTEAZA -> nu am reusit sa-l fac
# -	Primul numar x este mai mare decat al doilea nr y
# -	Al doilea nr y este mai mare decat primul nr x
# -	Numerele sunt egale.

# def maximum(x,y):
#     if x > y:
#         x = int(input('Introduceti x'))
#         y = int(input('Introduceti y'))
#         print('Primul numar este mai mare decat al doilea nr')
#     elif x < y:
#         print('Al doilea nr este mai mare decat primul nr ')
#     else:
#         print('Numerele sunt egale')


def numar_maxim(x,y):
    while numar_maxim < 0:
        numar_maximint = (input('Varsta incorecta. Va rugam incercati din nou'))
    if x<y:
        print('Primul numar este mai mare decat al doilea nr')
    elif x < y:
        print('Al doilea nr este mai mare decat primul nr ')
    else:
        print('Numerele sunt egale')

x = int(input('Introduceti x'))
y = int(input('Introduceti y'))

# 10. Functie care primeste un numar si un set de numere. -> nu am reusit sa-l fac
# Printeaza ‘am adaugat numarul nou in set’ + returneaza True
# Sau Printeaza ‘nu am adaugat numarul in set. Acesta exista deja’ + returneaza False