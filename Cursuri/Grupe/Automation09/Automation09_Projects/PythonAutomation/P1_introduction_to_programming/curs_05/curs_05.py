# # Definirea unei functii
#
# def say_hi():
#     print('Hi')
#
# say_hi()
# x = say_hi()
# print(x) # printeaza pe ecran none
#
# def say_hi_v1():
#     message ='Hi'
#     return message
#
# x = say_hi_v1()
# print(x)
#
# def print_hi_user(user):
#     print(f'Hello {user}')
#
# print_hi_user('Mihai')
#
# def print_hi_user_npr(nume,prenume):
#     print(f'Hello {nume, prenume}')
#
#
# def print_hi_user_valori(nume='sorin',prenume='anton'):
#     prenume.upper()
#     print(f'Hello {nume, prenume}')
#
# # input 5 numere
# # output ne dorim un set
#
# def make_set(n1,n2,n3):
#     r = set()
#     print(type(r))
#     r.add(n1)
#     r.add(n2)
#     r.add(n3)
#     return r
#
# print(make_set(1,2,3))
# set1 = make_set(1,2,2)
# set2 = make_set(1,2,3)
# print(set1.intersection(set2))
# make_set(1,2,2).intersection(make_set(1,2,3))
#
# def pi_value():
#     return 3.14
#
# x = pi_value()+4
# print(x)
#
# # from introduction_to_programming.helper_05 import *
# from introduction_to_programming.helper_05 import suma
# print(suma(3,5))
#
# # Calcul impozit in functie de centimetri cubi
# cc = input("Alege centimetri cubi: ")
# impozit = 0
# hybrid = False
# def calculImpozit(cc_input, hybrid_input):
#     if hybrid_input == False:
#         return 10
#     else:
#         if cc_input<1000:
#             return 70
#         elif cc_input<2000:
#             return 160
#         else:
#             return 900
#
# impozit = calculImpozit(cc,False)
# print(impozit)
# impozit=calculImpozit(2400,False)
# print(impozit)
# impozit=calculImpozit(2400,True)
# print(impozit)
#
#
REZERVOR = 50
# def abc(parametruFunctie):
#     REZERVOR
#
# '''
#
# procentul de benzina ramasa daca scadem sub 15%, afisam un warning
# nume de baiat sau fata
# sa imbunatatim f de add din set
# 2 liste? care sunt elementele lor comune?
# f de replace pe lista


benzina = input("Benzina ramasa")
benz_ramasa = 0

def benzina_ramasa(benzina_input):
    if benzina_input>REZERVOR:
        print("Nu poti avea mai multa bezina decat capacitatea rezervorului")
        return 'N/A'
    if benzina_input<0:
        print("Nu poti avea valori negative")
        return 'N/A'
    procentaj_benzina = benzina_input/REZERVOR*100
    print(procentaj_benzina)
    if procentaj_benzina<=15:
        print("Warning")
    return procentaj_benzina

benz_ramasa = benzina_ramasa(benzina)


# nume = input('Introdu numele')
# exceptii_fete = ['Carmen','Damaris','Beatrice']
# exceptii_baieti = ['Mihnea','Mircea','Horia','Horea']
# def gen(nume):
#     if nume[len(nume)-1] !='a' or nume in exceptii_baieti:
#         print('Este baiat')

from helper_05 import pret_bilet
# import helper_05

pret_bilet(5,6)

valoare_totala = pret_bilet - pret_bilet*0.3