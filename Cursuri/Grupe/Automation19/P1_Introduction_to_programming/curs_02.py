"""
Atribuire = proces prin care salvam informatii la adresa de memorie identifica cu un nume al unei variabile,
indiferent de tipul de date al acesteia

Operatorii de asignare sunt: = , += , -= , *= , /=
"""

# A. ASSIGNMENT OPERATORS

x = 3       # declarare si initializare a unei variabile prin intermediul operatorului de atribuire - valoare initiala: 3
print(x)

x = x+3    # marirea valorii lui x cu 3 prin intermediul operatorului de atribuire = . valoare curenta: 6
print("-------------------------------------")
print(x)

x += 3  # marirea valorii lui x cu 3 prin intermediul operatorului de atribuire +=. valoare curenta: 9
print(x)
print("-------------------------------------")

x = x - 3 # micsorarea valorii lui x cu 3 prin intermediul operatorului de atribuire =. valoare curenta: 6
print(x)

x -= 3
print(x)

print("-------------------------------------")
x = x*3
print(x)
x *= 3
print(x)
print("-------------------------------------")
x = x/3  # rezultatul impartirii va fi float deoarece putem efectua impartirea intre doua numere care returneaza rest
print(x)
x /= 3
print(x)
print("-------------------------------------")

# B. ARITHMETICAL OPERATORS

"""
operatorii aritmetici sunt operatori care permit operatii matematice
Exemple de operatori aritmetici: +, -, *, /, % (operatorul modulo), ** (operatorul putere), // (floor division)
"""
print(2+3)
print(6-4)
print(3*2)
print(5/3)
print(5%3)
print(2**3) # operatorul putere, care ridica baza la putere -> 2 este ridicat la puterea a 3-a si rezultatul va fi 8
print(7/2.5)
print(7//2.5) # operatorul floor division rotunjeste rezultatul la cel mai apropiat numar intreg inferior
print(10%3) # operatorul modulo returneaza restul impartirii deimpartitului la impartitor -> 3 incape in 10 de 3 ori (3*3 = 9) -> ne ramane 1 unitate
print(456%253)

x = 1256789235
y = 234589
print(x/y)

# # C. COMPARISON OPERATORS
#
# """
# Operatori prin intermediul carora putem compara doua valori distincte (vor fi foarte utili in cadrul assert urilor)
# """
y = 3
x = 2
print(x==2)  # ATENTIE!! Nu confundati operatorul de atribuire (=) cu operatorul de comparatie (==)
print(x==y)
print(x!=2)  # != este un operator de comparatie care verifica faptul ca operatorul din stanga este diferit de cel din dreapta.
                    # daca cele doua valori sunt diferite, rezultatul evaluarii va fi TRUE
                    # putem sa spunem ca valideaza un fals
print(x!=y)

print(x>2) # > este un operator care evalueaza daca valoarea din stanga este mai mare decat valoarea din dreapta

print(x>y)

print(x<2) # < este un operator care evalueaza daca valoarea din stanga este mai mica decat valoarea din dreapta
print(x<y)

print(x>=2) # >= este un operator care evalueaza daca valoarea din stanga este mai mare sau egala cu valoarea din dreapta
print(x>=y)

print(x<=2) # <= este un operator care evalueaza daca valoarea din stanga este mai mica sau egala cu valoarea din dreapta
print(x<=y)


# D. LOGICAL OPERATORS
# Operatorii logici sunt operatori care sunt folositi pentru a defini evaluari mai complexe
# formate din mai multe conditii de evaluare

# Operatorii logici sunt:  AND OR NOT

# NOT > AND > OR

print(x<2 and x<y or x==y)
print(x<2 or x<y and x==y)
print(not (x<2 or x<y) and x==y)
print( x<2 or not (x<y and x==y))


# """

x = 3
y = 5

print(x<2 and x<y) # x<2 and x<y este o conditie compusa care instruieste sistemul sa o evalueze
#                         #ca fiind adevarata, doar daca ambele conditii simple pe care le contine
#                             #sunt evaluate ca fiind adevarate
#                                 # conditia compusa de mai sus va returna false
print(x==2 and x<y) # Conditia compusa va returna true pentru ca ambele conditii simple sunt evaluate ca si TRUE

print(x==2 and x==y) # Conditia compusa va returna FALSE pentru ca continutul variabilei x nu este identic cu continutul variabilei y

print(x==2 or x<y) # Conditia compusa x==2 or x<y instruieste sistemul sa o evalueze ca fiind adevarata
                         # atata timp cat oricare din conditiile simple sunt evaluate ca fiind adevarate

print(not(x==2 or x<y)) # operatorul NOT este folosit pentru a NEGA rezultatul evaluarii unei expresii

print(x<2 or y>x and x==y) # se va evalua mai intai y>x and x==y care va returna FALSE
                                # apoi se va evalua x<2 si va returna FALSE
                                # apoi se va evalua rezultatul celor doua: FALSE OR FALSE  = FALSE

print((x<2 or y>x) and x==y) # se va evalua mai intai x<2 or y>x care va returna TRUE (FALSE OR TRUE = TRUE)
                                # apoi se va evalua x==y si va returna FALSE
                                # apoi se va evalua rezultatul celor doua: TRUE AND FALSE  =  FALSE

print(not x<2 or y>x and x==y) # se va evalua mai intai not x<2 care va returna TRUE (NOT FALSE  = TRUE)
                                # apoi se va evalua y>x and x==y si va returna FALSE
                                # apoi se va evalua rezultatul celor doua: TRUE OR FALSE  =  TRUE
# x = 3
# y = 5

print(not(x<2 or y>x) and x==y) # se va evalua mai intai x<2 or y>x care va returna TRUE
                                 # apoi se va evalua not TRUE si va returna FALSE
                                 # apoi se va evalua x==y si va returna FALSE
                                 # apoi se va evalua rezultatul celor doua: FALSE AND FALSE  =  FALSE


# """
# if(not(isDisplayed()))
#         =
# if(isDisplayed()==False)
# """
# # y = 3
# # x = 2
#
# """
#
# In general operatorul NOT are prioritate in fata operatorilor OR si AND
# Operatorul AND are prioritate in fata operatorului OR
#
#
# Ordinea prioritatii: NOT > AND > OR
#
# Exemple de evaluari:
#
# FALSE or FALSE = FALSE
# FALSE or TRUE = TRUE
# TRUE or TRUE = TRUE
#
# FALSE and FALSE = FALSE
# FALSE and TRUE = FALSE
# TRUE anf TRUE = TRUE
#
# not FALSE = TRUE
# not TRUE = FALSE
#
# Exemple de conditii evaluate:
#
# print(not x==2 or y>5 and x<y)
#     - Ordinea evaluarii va fi:
#             not x==2 (FALSE)
#             y>5 and x<y (FALSE)
#             FALSE OR FALSE
#
# print(not (x==2 or y>5 and x<y))
#     - Ordinea evaluarii va fi:
#             x==2 (TRUE)
#             y>5 (doar daca x==2 va fi evaluata ca FALSE)
#             x<y (TRUE)
#             TRUE or TRUE => TRUE
#             not TRUE => FALSE
#
# print(not ((x==2 or y>5) and x<y))
#     - Ordinea evaluarii va fi:
#             x==2 (TRUE)
#             y>5 (doar daca x==2 va fi evaluata ca si FALSE)
#             x<y (TRUE)
#             TRUE and TRUE => TRUE
#             not TRUE = >FALSE
#
# print(not x==2 or (y>5 and x<y))
#     - Ordinea evaluarii va fi:
#             not x==2 (FALSE)
#             y>5 (FALSE1)
#             x<y (doar daca y>5 va fi evaluata ca si TRUE) => TRUE
#             FALSE1 and TRUE => FALSE3
#             FALSE or FALSE3 => FALSE
#
# not x==2  = A (FALSE)
# y>5 and x<y = B (FALSE)
# A or B (FALSE or FALSE = FALSE)
#
#
# """
#
# print(not(x==2 or x<y))
# print(x<y and x>y and x == y)
# print(x<y or x>y and x <= y)
#
#
# # D. FLOW CONTROL
#
# """
# Un flow control este o modalitate prin care putem sa instruim programul sa execute un set de instructiuni
# sau un alt set de instructiuni in functie de rezultatul evaluarii unei conditii
#
# Daca conditia este adevarata, atunci se va executa un set de instructiuni
# Daca conditia este falsa, atunci se va executa un alt set de instructiuni
#
# Componente ale unei decizii (flow control)
# - inceputul deciziei = IF
# - ramura din dreapta a deciziei, care se va executa doar atunci cand conditia este evaluata ca fiind adevarata (THEN)
# - ramura din stanga a deciziei, care se va executa doar atunci cand conditia este evaluata ca fiind falsa (ELSE)
#             ELSE - ul tine loc unui set de instructiuni implicite
# - conditie aditionala separata, ca sa sa fie evaluata in cazul in care conditia principala este evaluata ca si falsa (ELIF)



# Nota: Noi putem sa adaugam o decizie in interiorul unei alte decizii, caz in care putem sa vorbim despre decizii IMBRICATE
#         (Decizii imbricate = Embedded decisions)
#
# - Conditia decizionala este separata de prima instructiune de pe ramura de THEN prin semnul ":"
# - Putem sa includem o instructiune in interiorul unei decizii prin indentarea sa fata de marginea din stanga programului
# - Sfarsitul if-ului va fi considerat acolo unde este intalnita prima instructiune neindentata
#         ATENTIE!!! exceptie va face keyword-ul ELSE
#
# - Ordinea keyword-urilor o sa fie: IF, ELIF, ELSE
#
# """
#
# """
#
# Constanta este o adresa de memorie care nu trebuie sa isi schimbe valoarea
# In python conceptul de constanta NU exista din punct de vedere tehnic
#         - eu nu pot sa implementez o modalitate de a restrictiona schimbarea unei valori la o adresa de memorie
# In python, ca sa putem implementa conceptul de constanta, s-a decis prin conventie ca toate adresele de memorie care nu vrem
#             sa isi schimbe continutul sa fie scrise in intregime cu majuscule
#
# """


# cerinta: verificati daca abonamentul clientului este activ inainte sa ii oferiti accesul in sala

# isActivated = input("introduceti statusul abonamentului ") # in mod implicit tipul de data al valorilor introduse de la tastatura este string
# if int(isActivated)==1:
#     print("Permiteti accesul")
# else:
#     print("Nu permiteti accesul")


# cerinta: verificati daca abonamentul clientului este activ, iar daca nu este i se va trimite un mail cu o oferta de reinnoire
#
# isActivated = input("introduceti statusul abonamentului ") # in mod implicit tipul de data al valorilor introduse de la tastatura este string
# if int(isActivated)==0:
#     print("Reinnoiti abonamentul")
#
# if not(int(isActivated)):
#     print("Reinnoiti abonamentul")


# cerinta: verificati daca abonamentul clientului este activ inainte sa ii oferiti accesul in sala.
# Optiunile valide de la tastatura sunt 1 sau 0. Daca se introduce altceva vrem sa printam un mesaj de eroare

# isActivated = input("introduceti statusul abonamentului ") # in mod implicit tipul de data al valorilor introduse de la tastatura este string
# if int(isActivated)==1:
#     print("Permiteti accesul")
# elif int(isActivated==0):
#     print("Nu permiteti accesul")
# else:
#     print("Eroare, introduceti doar valorile 1 sau 0")

# if imbricat = if in if (in engleza se mai numeste embedded if)



# if int(isActivated)==1 or isActivated==0: # am verificat mai intai valorile introduse de la tastatura.
#     if int(isActivated)==1: #  abia daca valorile sunt ok merg mai departe cu prima verificare. Aici am aplicat un if in if (if imbricat sau embedded if)
#         print("Permiteti accesul")
#     else:
#         print("Nu permiteti accesul")
# else: #  instructiunile de pe ramura de else se vor executa doar daca conditia evaluata nu va fi adevarata
#     print("Eroare, introduceti doar valorile 1 sau 0")


"""
Cerinta: 
vrem sa implementam un nou sistem de tip bilete de avion. 
copiii sub 10 ani vor avea gratuitate la cumpararea biletului
adolescentii intre 10 si 18 ani vor avea 50% reducere
adultii vor plati pret intreg
seniorii peste 65 de ani vor avea reducere 30%
"""

# varsta = int(input("Va rugam sa introduceti varsta pasagerului "))
# if varsta<10:
#     discount = 1
# elif varsta<=18:
#     discount = 0.5
# elif varsta<=65:
#     discount = 0
# else:
#     discount = 0.3
#
# pret = 30
# pret = pret - pret*discount
# print(pret)



"""
Company X sells merchandise to wholesale and retail outlets.Wholesale customers receive a two percent discount on all orders. 
The company also encourages both wholesale and retail customers to pay cash on delivery by offering a two percent discount for this method of payment. 
Another two percent discount is given on orders of 50 or more units. Each column represents a certain type of order.



If a client has over 65 years, then it will be offered to him a discount of 15%.
Otherwise if the customer does not have over 65 years, if the person travels with at least one child they will have a discount of 10%
For both seniors and non seniors it will be applied an additional discount of 10% if they will travel during winter.
Also, for both seniors and non seniors it will be applied a 3% luxury fee if they will travel in the first class (in any season) or 1% handling fee otherwise.

"""

varsta = int(input("Va rugam sa introduceti varsta pasagerului "))
anotimp = input("Va rugam sa introduceti anotimpul calatoriei ")
clasa = int(input("Va rugam sa introduceti clasa calatoriei "))
pret = int(input("Va rugam sa introduceti pretul biletului "))

discount = 0
if varsta>65:
    discount = 0.15
else:
    nrCopii = int(input("Va rugam sa introduceti numarul de copii "))
    if nrCopii>=1:
        discount = 0.1
if anotimp == "iarna":
    discount+=0.1
if clasa == 1:
    taxa = 0.03
else:
    taxa= 0.01

pret = pret - pret * discount + pret * taxa
# senior care calatoreste iarna la clasa a 2-a -> 30 - 30*0.25 + 30*0.01 = 30 - 7.5 + 0.3 = 22.8
# persoana sub 65 de ani fara copii care calatoreste primavara la clasa 1 -> 30 + 0.9 = 30.9
print(pret)



# NOTA_DE_TRECERE = 5 # constant that we do not want to change it's value
# NOTA_DE_TRECERE_PURTARE = 7
#
# nota_examen = int(input("Introduceti nota de la examen "))
# nota_purtare = int(input("Introduceti nota la purtare "))
#
# if nota_examen >= NOTA_DE_TRECERE and nota_purtare >= NOTA_DE_TRECERE_PURTARE:
#     print("Am trecut")
#     if nota_examen==10 and nota_purtare==10:
#         print("felicitari,esti premiant")
# else: # Else does not have a condition because it means the instructions to be executed in case the previous condition is evaluated as false
#     print("Nu am trecut")
#     if(nota_purtare >= NOTA_DE_TRECERE_PURTARE):
#         print("Mai invata")
#     elif(nota_examen >= NOTA_DE_TRECERE):
#         print("Fii cuminte, ca altfel nu vine mosul!")
#     else:
#         print("Trebuie sa fii mai serios")



# optiune = int(input("Alegeti limba, pentru romana apasati 1, pentru engleza apasati 2"))
# if optiune == 1:
#     print("Ati ales limba romana")
#     optiune1 = input("pentru persoane fizice apasati 1, pentru persoane juridice apasati 2")
#     if(optiune1 == 1):
#         print("Ati ales persoana fizica")
#     elif(optiune1 == 2):
#         print("Ati ales persoana juridica")
#     else:
#         print("Optiune invalida, va rugam sa incercati din nou")
# elif optiune==2:
#     print("You chose english")
#     optiune1 = input("For individual persons press one, for companies press 2")
#     if (optiune1 == 1):
#         print("You chose individual person")
#     elif (optiune1 == 2):
#         print("You chose a company")
#     else:
#         print("Invalid option, please try again")
# elif optiune == 3:
#     print("return to main menu")
#
# else:
#     print("Invalid option, please choose another option")
#
#
# pasaport = input("Aveti pasaport? ")
# varsta = input("va rugam sa introduceti varsta persoanei")
#
# if pasaport == 'Da':
#     if varsta>=18:
#         print("Puteti trece")
#     else:
#         ambiiParinti = input("Sunt ambii parinti prezenti? Da/NU ")
#         if ambiiParinti == 'Da':
#             print("Puteti trece")
#         else:
#             permisiuneParinteLipsa = input("exista permisiune de la parintele lipsa? Da/NU")
#             if permisiuneParinteLipsa=='Da':
#                 print("Puteti trece")
#             else:
#                 print("Nu puteti trece")



# pasaport = input("Aveti pasaport? ")
# varsta = input("va rugam sa introduceti varsta persoanei")
# ambiiParinti = input("Sunt ambii parinti prezent? Da/NU")
# permisiuneParinteLipsa = input("exista permisiune de la parintele lipsa? Da/NU")
#
#
# if pasaport == 'Da' and (ambiiParinti == 'Da' or permisiuneParinteLipsa == 'Da'):
#     print("permite calatoria")
# else:
#     print("nu permite calatoria")
