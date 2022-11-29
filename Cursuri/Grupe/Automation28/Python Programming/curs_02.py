"""

1. SLICING

Slicing = Modalitate prin care putem sa extragem doar anumite parti dintr-un string

Slicing-ul se poate face pe baza urmatoarelor elemente:
- pozitie de inceput -> implicit va fi 0 - adica de la inceputul stringului
- pozitie de final -> implicit va fi lungimea stringului - adica pana la final
- pas (cate caractere sa se sara) -> implicit va fi 1 - adica se va printa fiecare caracter

In general in range-ul pe baza caruia se extrage bucata din string nu se ia in considerare capatul de interval

Exemplu:
Daca ii spun sistemul sa extraga toate caracterele de la pozitia 0 la pozitia 5, de fapt va extrage pana la pozitia 4

"""

poezie = "Cobori in jos Luceafar bland"

# Exercitiu 1: vrem sa extragem toate caracterele din string specificand explicit start-ul si end-ul si pasul implicit
print(poezie[0:len(poezie)]) # len(poezie) = 28 -> adica cate caractere sunt in string
                                # in programare toate elementele dintr-o structura ordonata incep de la indexul 0
                                    # de aceea indexul ultimului element se va afla in pozitia cu 1 mai mica decat lungimea stringului
                                      # avand in vedere ca ultimul caracter se afla in pozita cu 1 mai mica decat lungimea stringului,
                                            # desi capatul de interval nu se ia in considerare nu pierdem ultimul element datorita diferentei intre index si lungime

# Exercitiu 2: vrem sa extragem toate caracterele din string folosind start si end implicit
print(poezie[:])

# Exercitiu 3: vrem sa extragem toate caracterele din string folosind start si end implicit si pas explicit de 2 (adica printare din 2 in doua caractere)
print(poezie[::2])

# Exercitiu 4: vrem sa extragem toate caracterele din string folosind start si end implicit si pas implicit
print(poezie[::])

# Exercitiu 5: vrem sa extragem caracterele incepand de la pozitia 3 pana la pozitia 10 inclusiv
print(poezie[3:11])

# Exercitiu 6: vrem sa extragem ultimele trei caractere de la final
print(poezie[-3:])
print(poezie[-3:])

# Exercitiu 7: vrem sa printam string-ul in sens invers
print(poezie[::-1])

"""
Metode pe care putem sa le folosim cu string-urile
Pentru a le putea accesa vom scrie numele srting-ului urmat de caracterul "."
"""
# poezie = "Cobori in jos Luceafar bland"
print(poezie.find("a")) # va identifica indexul primului caracter a din string
print(poezie.find("c"))  # va identifica indexul primului caracter c din string
print(f"Caracterul x se afla in pozitia {poezie.find('X')}")

# Referinta cod ASCII: https://www.ascii-code.com/

print(poezie.index("C"))  # va identifica indexul primului caracter C din string
                                # metoda index face exact acelasi lucru ca metoda find
# print(f"Caracterul x se afla in pozitia {poezie.index('Y')}")

# Diferenta intre find si index este ca "find" returneaza -1 in cazul in care caracterul nu e gasit si "index" da eroare

print(poezie.split()) # functie care sparge string-ul in functie de cuvintele componente.
                            # rezultatul este o lista
                             # separatorul implicit este spatiu, dar se poate suprascrie
print(poezie.split(sep="L")) # Am suprascris separatorul

print(poezie.count("a")) # numara de cate ori apare un anumit substring in string-ul de la care plecam
print(poezie.isdigit()) # verifica daca toate caracterele dintr-un string sunt cifre
                            # atentie!!! sunt trei functii care fac asta: isDigit, isNumeric, isDecimal

# Diferenta intre cele trei metode: https://stackoverflow.com/questions/44891070/whats-the-difference-between-str-isdigit-isnumeric-and-isdecimal-in-python

print(poezie.replace("a","M"))

"""
2. Operatori

Operatori sunt elemente prin intermediul carora putem efectua operatii asupra variabilelor
Exista patru tipuri de operatori:
- Operatori aritmetici -> prin intermediul carora putem efectua operatii matematice
- Operatori de comparatie -> prin intermediul carora putem efectua comparatii intre continutul variabilelor
- Operatori de atribuire -> prin intermediul carora putem sa alocam valori variabilelor
- Operatori logici -> prin intermediul carora putem evalua conditii mai complexe

alocare = salvare de informatii la adresa de memorie care este identificata de numele variabilei
"""

# 1. OPERATORI ARITMETICI: +, -, *, /, **, %, //
# 1.1. Operatorul + este folosit pentru a aduna doua numere sau pentru a concatena doua string-uri
# Exemple:
nr_1 = 5
nr_2 = 7
print(f"Suma celor doua numere este: {nr_1 + nr_2}")
str_1 = "ana "
str_2 = "are mere"
print(f"String-urile concatenate sunt: {str_1 + str_2}")
print("String-urile concatenate sunt: " + str_1 + " " + str_2)

# 1.2. Operatorul = este folosit pentru a efectua diferenta intre doua numere
print(f"Diferenta intre cele doua numere este: {nr_1 - nr_2}")

# 1.3. Operatorul * este folosit pentru a efectua inmultirea intre doua numere
print(f"Inmultirea celor doua numere a rezultat in numarul: {nr_1*nr_2}")

# 1.4. Operatorul / este folosit pentru a efectua impartirea a doua numere
print(f"Impartirea celor doua numere a rezultat in numarul: {nr_1 / nr_2}")
# ATENTIE!! rezultatul operatiei efectuate cu operatorul division este float

# 1.5. Operatorul // (FLOOR DIVISION) este folosit pentru a efectua impartirea intreaga a doua numere (adica se taie zecimalele de la rezultat)
print(f"Impartirea cu floor division celor doua numere a rezultat in numarul: {nr_1 // nr_2}")
print(f"Impartirea cu celor doua numere a rezultat in urma rotunjirii in numarul: "  + str(round(nr_1 / nr_2)))

# 1.6. Operatorul % (MODULO) este folosit pentru a obtine restul impartirii deimpartitului la impartitor
print(f"Restul impartirii lui {nr_2} la {nr_1} este {nr_2%nr_1}")

# 1.7. Operatorul ** (RIDICARE LA PUTERE) este folosit pentru a ridica un numar la puterea x
print(f"Numarul {nr_2} ridicat la puterea {nr_1} este {nr_2**nr_1}")


# 2. OPERATORI DE COMPARATIE: ==, <=, >=, <, >, !=
# 2.1. OPERATORUL == este folosit pentru a compara valoarile dintre doua variabile
                        # ATENTIE!!! Nu confundati operatorul de comparatie == cu operatorul de atribuire =
                        # Rezultatul comparatiei o sa fie boolean

print(f"Cele doua numere sunt egale? {nr_1==nr_2}")

# 2.2. OPERATORUL <= este folosit pentru a verifica comparatia intre doua numere, daca primul este mai mic sau egal cu al doilea
print(f"Numarul 1 este mai mic sau egal cu numarul 2? {nr_1<=nr_2}")

# 2.2. OPERATORUL >= este folosit pentru a verifica comparatia intre doua numere, daca primul este mai mare sau egal cu al doilea
print(f"Numarul 1 este mai mare sau egal cu numarul 2? {nr_1>=nr_2}")

# 2.3. OPERATORUL < este folosit pentru a verifica comparatia stricta intre doua numere, pentru a vedea daca primul este mai mic decat al doilea
print(f"Numarul 1 este mai mic decat numarul 2? {nr_1<nr_2}")

# 2.4. OPERATORUL > este folosit pentru a verifica comparatia stricta intre doua numere, pentru a vedea daca primul este mai mare decat al doilea
print(f"Numarul 1 este mai mare decat numarul 2? {nr_1>nr_2}")

# 2.5. OPERATORUL != (not egal) este folosit pentru a verifica comparatia stricta intre doua numere, pentru a vedea daca primul este diferit de al doilea
print(f"Numarul 1 este diferit de numarul 2? {nr_1!=nr_2}")

# 3. OPERATORI DE ATRIBUIRE: +=, -=, =, *=, /=

# ATENTIE!!! OPERATORII ++, -- din java NU EXIST in Python

# 3.1. Operatorul = -> Este folosit pentru a salva o informatie intr-o variabila
                    # atribuirea unei valori intiale intr-o variabila se numeste initializare
variabila_atribuire_initiala = 5 # am salvat valoarea 5 la adresa de memorie numita variabila_atribuire_initiala
                                    # atribuire prin initializare
    # Atentie!!! se poate face suprascriere. Adica daca la aceeasi adresa de memorie facem o noua atribuire,
                # nu se va crea o noua variabila / adresa de memorie
                    # ci se va inlocui valoarea la adresa de memorie curenta
variabila_atribuire_initiala =  7 # atribuire prin suprascriere

# 3.1. Operatorul += -> Este folosit pentru a mari valoarea variabilei din stanga operatorului cu valoarea din dreapta operatorului
                            # rezultatul va suprascrie valoarea curenta din variabila
variabila_atribuire_initiala += 12 # rezultatul operatiei va fi 19

# 3.1. Operatorul -= -> Este folosit pentru a micsora valoarea variabilei din stanga operatorului cu valoarea din dreapta operatorului
variabila_atribuire_initiala -= 12 # rezultatul va suprascrie valoarea curenta din variabila

# 3.1. Operatorul *= -> Este folosit pentru a inmulti valoarea variabilei din stanga operatorului cu valoarea din dreapta operatorului
variabila_atribuire_initiala *= 5 #rezultatul va suprascrie valoarea curenta din variabila

# 3.1. Operatorul /= -> Este folosit pentru a imparti valoarea variabilei din stanga operatorului la valoarea din dreapta operatorului
variabila_atribuire_initiala /= 5 #rezultatul va suprascrie valoarea curenta din variabila


# 3. OPERATORI LOGICI: AND, NOT, OR
# OPERATORUL AND -> Este un operator strict care face ca rezultatul unei conditii compuse sa fie TRUE doar daca fiecare conditie din conditia compusa returneaza TRUE
print(nr_1<nr_2 and nr_1 <=nr_2) # nr_1<nr_2 = TRUE, nr_1 <=nr_2 = TRUE, TRUE AND TRUE = TRUE
print(nr_1<nr_2 and nr_1 >=nr_2) # nr_1<nr_2 = TRUE, nr_1 >=nr_2 = FALSE, TRUE AND FALSE = FALSE

# OPERATORUL OR ->Este un operator mai putin strict care face ca rezultatul unei conditii compuse sa fie TRUE daca oricare din conditiile din conditia compusa returneaza TRUE
print(nr_1<nr_2 and nr_1 <=nr_2) # nr_1<nr_2 = TRUE, nr_1 <=nr_2 = TRUE, TRUE AND TRUE = TRUE
print(nr_1<nr_2 and nr_1 >=nr_2) # nr_1<nr_2 = TRUE, nr_1 >=nr_2 = FALSE, TRUE OR FALSE = TRUE

# OPERATORUL NOT -> Este un operator ce returneaza opusul rezultatului conditiei
print(not nr_1<nr_2)  # nr_1<nr_2 = TRUE, NOT TRUE = FALSE
print(not nr_1<nr_2 and nr_1<=nr_2) # nr_1<nr_2 = TRUE, NOT TRUE = FALSE, nr_1<=nr_2 = TRUE, FALSE AND TRUE = FALSE
print(not nr_1<nr_2 and nr_1<=nr_2 or nr_2 > nr_1) # nr_1<nr_2 = TRUE, NOT TRUE = FALSE, nr_1<=nr_2 = TRUE, FALSE AND TRUE = FALSE, nr_2 > nr_1= TRUE, FALSE OR TRUE = TRUE
print(not nr_1<nr_2 or  nr_1<=nr_2 and nr_2 > nr_1) # nr_1<nr_2 = TRUE, NOT TRUE = FALSE, nr_1<=nr_2 = TRUE, nr_2 > nr_1= TRUE, TRUE AND TRUE = TRUE, FALSE OR TRUE = TRUE
print((not nr_1<nr_2 or  nr_1<=nr_2) and nr_2 > nr_1) # nr_1<nr_2 = TRUE, NOT TRUE = FALSE, nr_1<=nr_2 = TRUE, FALSE OR TRUE = TRUE, nr_2 > nr_1= TRUE, TRUE AND TRUE = TRUE
print(not ((nr_1<nr_2 or  nr_1<=nr_2) and nr_2 > nr_1)) # nr_1<nr_2 = TRUE, nr_1<=nr_2 = TRUE, TRUE OR TRUE = TRUE, nr_2 > nr_1= TRUE, TRUE AND TRUE = TRUE, NOT TRUE = FALSE
# Ordinea prioritatii operatorilor logici: NOT > AND > OR

"""
Structura alternativa IF - este o modalitate prin care putem sa acoperim situatiile in care vrem sa
                        executam un set de instructiuni sau un altul in functie de rezultatul evaluarii unei conditii

Structura unei decizii (IF):
- Inceputul deciziei (If) 
- Ramura din dreapta (TRUE) a deciziei -> reprezentata de primul bloc de cod dupa if
- Marcarea instructiunii alternative, cu conditie aditionala, atunci cand avem mai mult de doua situatii posibile (elif)
- Marcarea isntructiunii alternative finale - ultimul set de instructiuni, in cazul in care niciuna dintre conditii nu este indeplinita

Blocul de cod aferent fiecarei ramuri decizionale este marcat de indentare
Ramura decizionala = blocul de cod care se executa in cazul in care conditia este evaluata ca fiind adevarata si respectiv falsa
Indentare = spatiul lasat intre marginea fisierului si linia de cod                  
"""

"""

In testare manuala exista doua categorii de tehnici de testare:
- Testare blackbox -> testare fara acces la cod (frontend)
- Testare whitebox -> testare cu acces la cod (backend)

1. Tehnici de testare whitebox:
- Statement coverage -> Reprezinta numarul de teste necesare pentru a executa CEL PUTIN O DATA fiecare instructiune din cod
- Decision coverage -> Reprezinta numarul de teste necesare pentru a executa CEL PUTIN O DATA fiecare RAMURA DECIZIONALA din cod

In general, decizion coverage este mai acoperitor decat statement coverage

Pentru a calcula statement si decizion coverage  cu usurinta, se recomanda crearea unei scheme care sa contina urmatoarele elemente:
- start / end (optionale) -> marcate printr-un semicerc
- input -> marcat printr-un paralelogram
- statement -> marcat printr-un dreptunghi
- decizie(If) -> marcat printr-un romb 
"""

"""
Exercitiu:

If a client has over 65 years, then it will be offered to him a discount of 15%.
Otherwise if the customer does not have over 65 years, if the person travels with at 
least one child they will have a discount of 10%
For both seniors and non seniors it will be applied an additional discount of 10% if they 
will travel during winter.
Also, for both seniors and non seniors it will be applied a 3% luxury fee if they will travel
in the first class (in any season) or 1% handling fee otherwise.

"""

varsta = int(input("Va rugam sa introduceti varsta: "))
sezon = input("Va rugam sa introduceti sezonul: ")
clasa = int(input("Va rugam sa introduceti clasa la care calatoriti: "))
pret = int(input("Va rugam sa introduceti pretul de baza al biletului: "))
discount = 0
if varsta>65:
		discount = 0.15
else:
		nr_copii = int(input("Va rugam sa introduceti numarul de copii cu care calatoriti: "))
		if nr_copii>0:
				discount = 0.1
if sezon == 'iarna':
		discount += 0.1 # echivalentul instructiunii discount = discount + 0.1
if clasa == 1:
		tax = 0.03
else:
		tax = 0.01
pret = pret - pret*discount + pret * tax
print(pret)

# 30 - 30*0.25 + 30*0.03 = 30-7.5 + 0.9 = 22.5 +  0.9 = 23.4

"""
Scenarii pentru statement coverage:
- Persoana peste 65 de ani care calatoreste iarna la clasa 1
- persoana sub 65 de ani cu un copil care calatoreste iarna la clasa a 2-a

Scenarii pentru decizion coverage:
- Persoana peste 65 de ani care calatoreste iarna la clasa 1
- Persoana sub 65 de ani cu un copil care calatoreste vara la clasa 2
- Persoana sub 65 de ani fara copil care calatoreste vara la clasa 2

Test condition = Ce testam? (Functionalitate pe care vrem sa o verificam)
Test case = Cum testam?

Test case 1
Summary: Verifica faptul ca persoana este 65 de ani care calatoreste iarna la clasa 1 va primi un discount de 25% si va plati taxa de 3%
Pasi de reproducere:
1. Intra in aplicatie
2. Alege destinatia dorita
3. Completeaza informatiile legate de varsta, sezon si clasa
4. Verifica pretul calculat al biletului

Rezultate asteptate: Seniorul va primi un discount de 25% si va plati o taxa de 3%

"""
