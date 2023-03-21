"""
String index = In general un sir de caractere este ordonat, in sensul in care orice caracter din acel sir
								are o pozitie specifica numita index
								In orice string indexul porneste de la pozitia 0

String length	= Daca vrem sa aflam cate caractere are un string, putem sa ne folosim de functia length

String slicing = O modalitate prin care putem sa extragem doar o parte dintr-un string
									Se poate face prin intermediul indecsilor, si putem sa extragem atat intregul sir
									cat si de la inceput pana la o anumita pozitie, de la o anumita pozitie pana la final
									sau un set de caractere din interior
									Atentie! la range-ul pentru slicing, ultimul index mentionat in range nu este luat in
														considerare
								  Elemente slicing:
								  1. pozitia de inceput a slicing ului
								  2. pozitia de finish (atentie, nu e luata in considerare la calcul)
								  3. pasul de parcurs (fiecare al catalea caracter este luat in considerare)
								  4. separator de elemente, caracterul ":"
								  In mod implicit pozitia de inceput este 0, pozitia de finish e ultimul caracter din string
								  	si pasul este 1


str_exemplu = "Ana are mere"
print(str_exemplu[0:3])
print(str_exemplu[-1])
print(str_exemplu[-3:])

poezie = "Ana are mere si este vesela pentru ca este marti si e la curs"
#  Ex 1: Extrageti toate caracterele de la inceput pana la sfarsitul string-ului cu mentionarea pozitiei si a pasului
print(poezie[0:len(poezie):1])
#  Ex 2: Extrageti toate caracterele de la inceput pana la sfarsitul string-ului folosind pozitia de inceput si de final implicita
print(poezie[:])
#  Ex 3: Extrageti toate caracterele de la inceput pana la sfarsitul string-ului afisand caracterele din 2 in 2
print(poezie[::2])
#  Ex 4: Extrageti toate caracterele de la pozitia 5 pana la pozitia 13 inclusiv
print(poezie[5:14])
#  Ex 5: Extrageti ultimele trei caractere din string
print(poezie[len(poezie)-3:len(poezie)]) # se afiseaza elementele de la indexul 56, 57, 58
print(poezie[-3:])
#  Ex 6: Printati stringul in ordine inversa
print(poezie[::-1])

Metode string = metode care pot fi folosite pentru interactiunea cu stringurile si procesarea stringurilor
								pentru a accesa metodele unui string scriem numele stringului
											urmat de caracterul punct care va deschide un meniu
											cu toate functiile care pot fi folosite cu acel string

poezie = "Ana are mere si este vesela pentru ca este marti si e la curs"
print(poezie.islower())
print(poezie.lower())
print(poezie.upper())

Exemplu de situatie in care se poate folosi:
		vrem sa extragem un text din browser dar nu stim exact sub ce format va veni:
			uppercase sau lowercase, si nici nu este relevant pentru testare.
			Si atunci folosim functia uppercase sau lowercase (in cazul asta specific la alegere)
			pentru a trata toate caracterele din string ul extras la fel si pentru a putea
			controla assertul si a avea o predictibilitate a rezultatelor

islower() -> evalueaza daca toate caracterele dintr-un string sunt de tip lowercase
					returneaza valoare boolean
lower() -> transforma toate caracterele dintr-un string in lowercase

isNumeric() vs isDigit() vs isDecimal(): https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-pyth

operatori de atribuire: =, +=, -=, *=, /=

Exemplu:
varsta = 5
varsta = varsta + 5 <=> varsta +=5

operatori aritmetici: +, -, *, /, %(returneaza restul impartirii deimpartitului la impartitor), **, // (floor division)
print(10%3) -> printeaza 1
print(10**3) -> ridicare la putere
print(10//3) -> returneaza numarul intreg prin taierea de zecimale de la rezultat
print(10//6) -> returneaza 1 pentru ca taie zecimalele
print(round(10/6)) -> returneaza 2 pentru ca aproximeaza

op. de comparare: <,>, <=,>=,==,!= (not egal)

op. logici: and, or, not
			ordinea de prioritate a operatorilor: not > and > or

print(2>3 and 5>1) # 2>3 = False, 5>1 = True => False and True = False
print(2>3 or 5>1) # 2>3 = False, 5>1 = True => False or True = True
print(not 2>3 and 5>1) # 2>3 = False, # not 2>3 = Not False = True, 5>1 = True => True and True = True
print(not (2>3 and 5>1)) # 2>3 = False, 5>1 = True => False and True = False => Not False = True


if	if else	if elif else

Decision coverage: https://www.tutorialspoint.com/software_testing_dictionary/decision_coverage_testing.htm

if = o structura alternativa care ne ajuta sa bifurcam codul in functie de o conditie
Componentele unui if (decizie)
- inceputul deciziei (if)
- conditia de evaluat in functie de care se va executa un cod sau un altul
- ramura din dreapta care reprezinta codul pe care sa il executam in cazul in care conditia este evaluata ca fiind adevarata
- ramura din stanga care reprezinta codul pe care sa il executam in cazul in care conditia este evaluata ca fiind falsa
- elif (optional) -> conditie alternativa de evaluat in cazul in care conditia initiala nu este indeplinita. Nu exista limita de cate elif-uri putem folosi
- else (optional) -> cod care sa fie executat in mod implicit daca conditia din if nu este indeplinita
											sau, in cazul in care avem si elif, daca niciuna din conditii nu este indeplinita
										  Pe else nu se mai pun conditii
Corpul if-ului(adica instructiunile care trebuie executate) sunt separate de conditie
				prin caracterul ":"
Corpul este marcat prin indentare fata de marginea fisierului
In momentul in care se strica indentarea se considera ca s-a iesit din if

Un if in interiorul altui if se numeste if imbricat (embedded if)
"""
"""
# Exercitiu if:

If a client has over 65 years, then it will be offered to him a discount of 15%.
Otherwise if the customer does not have over 65 years, if the person travels with 
at least one child they will have a discount of 10%
For both seniors and non seniors it will be applied an additional discount of 10% 
if they will travel during winter.
Also, for both seniors and non seniors it will be applied a 3% luxury fee if they 
will travel in the first class (in any season) or 1% handling fee otherwise.
"""

varsta = int(input("Va rugam sa introduceti varsta "))
sezon = input("Va rugam sa introduceti sezonul calatoriei ")
clasa = int(input("Va rugam sa introduceti clasa "))
pret_calatorie = int(input("Va rugam sa introduceti pretul calatoriei "))
discount = 0
tax = 0

if varsta>=65:
		discount = 0.15
else:
		nr_child = int(input("Va rugam sa introduceti numarul de copii "))
		if nr_child>=1:
				discount = 0.1

if sezon=="iarna":
		discount+=0.1

if clasa == 1:
		tax = 0.03
else:
		tax = 0.01

pret_calatorie = pret_calatorie - pret_calatorie*discount + pret_calatorie*tax
print(pret_calatorie)

