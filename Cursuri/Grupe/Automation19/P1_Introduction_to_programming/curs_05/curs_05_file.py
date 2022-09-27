"""
O functie este o modalitate prin care putem sa economisim cod.
O functie putem sa o definim o singura data si apoi sa facem ceea ce se numeste
    apelare a functiei
Apelarea functiei inseamna trimiterea sistemului catre adresa de memorie care poarta
    numele functiei si la care este stocat codul pe care vrem sa il executam
Definirea unei functii se poate face pe baza keyword-ului def
O functie POATE sa aiba parametri, dar nu este obligatoriu sa aiba
Chiar daca functia NU are parametri, parantezele de dupa numele functiei sunt
    obligatorii atat la definire cat si la apelare
Un parametru reprezinta o informatie de care functia are nevoie din exterior
    pentru a putea executa toate instructiunile
Putem alege sa parametrizam o functie atunci cand vrem ca functia noastra
    sa poata sa fie rulata pentru o plaja mai mare de valori
    ex: suma intre doua numere, putem avea alte doua numere la fiecare rulara
O functie POATE sa aiba optiune de return, dar nu este obligatoriu sa aiba
Vom alege sa punem optiune de return pe functie atunci cand vrem sa salvam rezultatul
    acelei functii intr-o variabila sau sa trimitem acel rezultat catre un sistem extern
"""

# 1. Definirea unei functii simple, fara parametri si fara return - Se face cu keyword-ul def
from curs_05 import helper_05


# def say_hi():
#     print('Hi')
#     afisare = "Acest test se va afisa prin intermediul optiunii return"
#     return afisare

"""
def - keyword ul care anunta inceputul definirii unei functii
say_hi - numele functiei, care este dat de catre user si care poate sa fie orice  (free text)
            in general, numele functiei trebuie sa fie sugestiv pentru actiunea pe care o face
() - reprezentant al zonei in care PUTEM sa specificam parametri. In cazul functiei say_hi
            nu avem parametri, motiv pentru care parantezele sunt goale
: - reprezentant al inceputului corpului functiei, adica locul in care vom incepe sa descriem
            actiunea pe care trebuie sa o faca functia
print('Hi') - actiunea pe care trebuie sa o faca functia       
Corpul unei functii va fi definit la fel ca la structurile alternative (if) si repetitive  (while, for)
            prin intermediul indentarii (adica spatiul lasat liber de la marginea fisierul python
            pana la inceputul liniei de cod)     
"""

# say_hi() #  daca nu punem parantezele, nu se va executa corpul functiei, pentru ca nu va fi vazuta
              # ca o functie

""" 
Apelarea functiei simple, fara parametri se va face specificand numele functiei 
        urmat de doua paranteze.
Daca nu avem parametri in functie, atunci vom lasa parantezele goale
In momentul in care codul va fi executat, sistemul va cauta adresa de memorie care poarta numele
        de say_hi, va citi codul stocat la acea adresa de memorie si il va executa
"""

# x = say_hi()  #  aici se va executa metoda say_hi chiar daca se va salva in variabila x
#                     # drept urmare, se printa 'Hi' de doua ori: o data de la linia 36
#                         # si inca o data de la linia 47
# print(x) #  se va printa pe ecran keyword-ul None, pentru ca functia nu are setata posibilitatea
#                 # de a trimite spre exterior valorile
# print(say_hi())

""" 
Apelarea functiei cu return se va face specificand numele functiei 
        urmat de doua paranteze iar in corpului functiei se va specific un keyword numit "return".
In momentul in care codul va fi executat, sistemul va cauta adresa de memorie care poarta numele
        de say_hi, va citi codul stocat la acea adresa de memorie si il va executa
Prin intermediul keyword-ului return, noi putem aloca rezultatul functiei unei variabile, sau trimite
        rezultatul catre un sistem extern
Daca o functie nu are return si totusi incercam sa printam rezultatul functiei, sa il alocam unei
        varibile sau sa il trimitem catre un sistem extern, alocarea/printarea/trimiterea va fi facuta
        cu keyword-ul None
"""

def say_hi_v1():
    message = 'Hi'
    return message

# x = say_hi_v1()         # nu va mai printa pe ecran 'Hi' pentru ca functia say_hi_v1 nu mai are o instructiune                    #  in interiorul ei
# print(x)                 # se va printa de data asta cuvantul Hi in loc de cuvantul None, pentru ca am instructiune de return in functie

# def say_hi_v2():
#     return 'Hi'
#
# x = say_hi_v2()
# print(x)                              # se va printa tot cuvantul Hi

""" 
Apelarea functiei cu parametri se va face specificand numele functiei 
        urmat de doua paranteze iar intre paranteze se va specifica numele informatiei care se doreste
        a fi parametrizata
Parametrizarea inseamna oferirea posibilitatii de a executa functia de mai multe ori cu valori diferite

Daca nu folosim parametri, si folosim valori efective in corpul functiilor (sau in cod in general)
        atunci vorbim despre o actiune care se numeste "hardcodare" (hardcoding)

"""

# Am definit o functie prin care am parametrizat userul caruia vrem sa ii spunem Hello
# Am vrut sa facem asta pentru ca am vrut sa putem sa salutam mai multe persoane

def print_hi_user(user):
    print(f'Hello {user}')

"""
user specificat intre paranteze rotunde reprezinta un template, sau o variabila care va stoca
        valoarea efectiva a userului caruia vrem sa ii spunem Hello
user specificat intre acolade reprezinta aceeasi variabila care a venit prin parametru si care va fi
        folosita pentru executarea corpului functiei
"""

# print_hi_user('Mihai')
# lista_users = ["Anda","Andreea Domut","Andreea Stoia","Anna","Magdalena","Domnica"]
# print("------FOR-----")
# for i in range(len(lista_users)):
#     print_hi_user(lista_users[i])

# print("------FOR EACH-----")
# for user in lista_users:
#     print_hi_user(user)

"""
Apelarea functiei se va face prin specificarea intre paranteze rotunde a valorii pe care 
        vrem sa o trimitem
Daca o functie a fost definita cu parametri, este obligatoriu sa fie si apelata cu argumente
Daca functia a fost definita cu parametri si apelata fara argumente, atunci sistemul va returna eroare
        in consola: TypeError: print_hi_user() missing 1 required positional argument: '<nume_parametru>'
In momentul apelarii, valoarea sau valorile pe care le scriem intre paranteze se numesc argumente

definire = parametri
apelare = argumente
"""

# Apelarea functiei cu o valoare trimisa prin input

# user = input("Introdu numele utilizatorului pe care vrei sa il saluti: ")
# print_hi_user(user)


# Apelarea functiei intr-un for, pentru parcurgerea unei liste
# lista_nume = ['Bogdan','Mircea','Luci','Raluca','Tavi','Mihai','Andreea']
#
# for nume in lista_nume:
#     print_hi_user(nume)
#
# # Putem sa definim si functii cu mai mult de un parametru
# # O functie poate sa aiba oricat de multi parametri avem nevoie

# def print_hi_user_npr(nume,prenume):
#     # print(f'Hello {nume} {prenume}')
#     return f'Hello {nume} {prenume}'
#
# print_hi_user_npr("Ion","Ion")
# print(print_hi_user_npr("Ion","Ion"))

# Putem sa definim o functie in care parametrii sa fie optionali
# (adica apelarea functiei se poate face fie cu argumente fie fara)

def print_hi_user_valori(nume='sorin',prenume='anton'):
    prenume = prenume.upper()
    print(f'Hello {nume} {prenume}')

print_hi_user_valori("mihai","alexandru")
print_hi_user_valori()              # In cazul in care nu specificam parametri, valorile implicite care se vor folosi
#                                   #  pentru executarea functiei vor fi cele definite ca valori in parametrizare
#                                   # In cazul asta, Sorin Anton

# def multiple_arguments(*args):
#     # print("test")
#     print(*args[1])

# multiple_arguments("Maria")
# multiple_arguments("Anton", "Marian")
# multiple_arguments("1", "2", "3", "4", "5", "6")


# def adder(*num):
#     sum = 0
#     for n in num:
#         sum = sum + n
#     print(f"Suma numerelor care au fost calculate este : {sum}")

# adder(1)
# adder(12,34)
# adder(125678,235,12,1,34,56)

# Vrem sa calculam suma tututor numerelor pare dintr-un anumit interval
# def suma_numere_pare(limita_superioara_range):
#     suma=0
#     for numar in range(limita_superioara_range):
#         if numar%2==0:
#             suma+=numar
#     return suma

# print(suma_numere_pare(9))

# def suma_numere_impare(limita_superioara_range):
#     suma=0
#     for numar in range(limita_superioara_range):
#         if numar%2!=0:
#             suma+=numar
#     return suma
"""
suma_numere_impare
    initialise the sum with the value of 0
    iterate with an iterator called number through the range defined by the input (for number between 0 and superior limit)
        if the number is even:
            add the number to the existing value of the variable suma (suma=suma+numar)
    send the value of the variable suma to the outside
"""
# print(suma_numere_impare(9))
#
# def make_set(n1,n2,n3):
#     r = set()
#     print(type(r))
#     r.add(n1)
#     r.add(n2)
#     r.add(n3)
#     return r

"""
make_set(input n1, input n2, input n3)
    create set r
    print the type of the set r
    add number n1 to the set r
    add number n2 to the set r
    add number r3 to the set r
    
    send outside the populated set
"""
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
# REZERVOR = 50
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

#
# benzina = input("Benzina ramasa")
# benz_ramasa = 0
#
# def benzina_ramasa(benzina_input):
#     if benzina_input>REZERVOR:
#         print("Nu poti avea mai multa bezina decat capacitatea rezervorului")
#         return 'N/A'
#     if benzina_input<0:
#         print("Nu poti avea valori negative")
#         return 'N/A'
#     procentaj_benzina = benzina_input/REZERVOR*100
#     print(procentaj_benzina)
#     if procentaj_benzina<=15:
#         print("Warning")
#     return procentaj_benzina
#
# benz_ramasa = benzina_ramasa(benzina)

"""
IMPORT
"""

# VARIANTA 1:


# VARIANTA 2

# caracterul "*" inseamna ca importam tot din fisierul specificat


# VARIANTA 3
#
# print(f"Taxele care se aplica la valoarea de {helper_05.pret_bilet} sunt {helper_05.taxe_absolute} lei")
# print(f"Discountul aplicabil pentru {helper_05.pret_bilet} este de {helper_05.discount_absolut}")
# print(f"Valoarea biletului dupa aplicarea taxelor de {helper_05.taxe_absolute} lei"
#       f" si respectiv a discountului {helper_05.discount_absolut} este de "
#       f"{helper_05.pret_total_bilet(helper_05.pret_bilet,helper_05.taxe_aplicabile,helper_05.discount)}")
#
# # VARIANTA 4
# import random
# nume_generat = random.randint(0,9)

"""
If a client has over 65 years, then it will be offered to him a discount of 15%.
Otherwise if the customer does not have over 65 years, if the person travels with at least one child they will have a discount of 10%
For both seniors and non seniors it will be applied an additional discount of 10% if they will travel during winter.
Also, for both seniors and non seniors it will be applied a 3% luxury fee if they will travel in the first class (in any season) or 1% handling fee otherwise.
"""


def calculeaza_pret_bilet(varsta,anotimp,clasa,pret,nrCopii=0):
    discount = 0
    if varsta > 65:
        discount = 0.15
    else:
        if nrCopii >= 1:
            discount = 0.1
    if anotimp == "iarna":
        discount += 0.1
    if clasa == 1:
        taxa = 0.03
    else:
        taxa = 0.01

    pret = pret - pret * discount + pret * taxa
    return pret

# 30 - 30*0.25 + 30*0.03 = 30 - 7.5 + 0.9 = 23.4
# 30 + 30*0.01 = 30 + 0.3 = 30.3
# 30 - 30*0.1 + 30*0.01 = 30 - 3 + 0.3 = 27.3

# varsta = int(input("Va rugam sa introduceti varsta pasagerului "))
# anotimp = input("Va rugam sa introduceti anotimpul calatoriei ")
# clasa = int(input("Va rugam sa introduceti clasa calatoriei "))
# pret = int(input("Va rugam sa introduceti pretul biletului "))
# nrCopii = int(input("Va rugam sa introduceti numarul de copii "))
#
# print(calculeaza_pret_bilet(varsta,anotimp,clasa,pret))
# print(calculeaza_pret_bilet(varsta,anotimp,clasa,pret,nrCopii))


"""
Vrem sa dezvoltam o aplicatie care sa vanda bilete de avion dupa urmatoarele reguli:
- copii sub 10 ani vor avea gratuitate
- adolescentii intre 10 si 18 ani vor avea 50% discount
- adultii vor plati bilet intreg
- seniorii peste 65 de ani vor avea 30% discount

Toate biletele de avion se vor vinde pe baza unui pasaport valid.
Pentru copiii sub 18 ani trebuie aditional fie prezenta ambilor parinti fie permisiune de la parintele lipsa
Adultii incepand cu 18 ani vor plati bilet intreg
"""


def calculare_bilete_avion(varsta,pasaport_valid,pret_bilet,permisiune_parinte_lipsa=0):
    discount = 0
    if pasaport_valid == 1:
        if varsta>65:
            discount = 0.3
        elif varsta<18:
            if permisiune_parinte_lipsa == 1:
                if varsta<10:
                    discount = 1
                else:
                    discount = 0.5
        else:
             discount = 0

    pret_bilet = pret_bilet - pret_bilet * discount
    return pret_bilet

# print(calculare_bilete_avion(5,1,30,1))



def calculeaza_promovare(nota_examen,nota_purtare):
    NOTA_DE_TRECERE = 5
    NOTA_DE_TRECERE_PURTARE = 7
    if nota_examen >= NOTA_DE_TRECERE and nota_purtare >= NOTA_DE_TRECERE_PURTARE:
        print("Am trecut")
        if nota_examen == 10 and nota_purtare == 10:
            print("felicitari,esti premiant")
    else:
        print("Nu am trecut")
        if (nota_purtare >= NOTA_DE_TRECERE_PURTARE):
            print("Mai invata")
        elif (nota_examen >= NOTA_DE_TRECERE):
            print("Fii cuminte, ca altfel nu vine mosul!")
        else:
            print("Trebuie sa fii mai serios")

calculeaza_promovare(7,8)
calculeaza_promovare(6,4)
calculeaza_promovare(4,6)








