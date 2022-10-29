"""

IDE = Integrated Development Environment -> un loc in care putem sa scriem si sa rulam cod
        - pycharm
        - intellij
        - eclipse
        - visual studio

Terminal = locul din care putem sa instalam pachete sau sa rulam framework-uri
Consola = locul in care putem sa vizualizam rezultatele rularii de cod. In pycharm se gaseste sub numele de Run
Venv = Virtual environment -> locul in care putem sa izolam anumite aplicatii

"""

"""

1. Hello World + Comentarii

- comentariile sunt linii de cod pe care le putem scrie sub forma de explicatii si care sunt ignorate de compilator
- intructiunile pe care le scriem sunt ca un fel de reguli de gramatica care trebuie sa fie respectate
- daca textul pe care il scriem nu respecta regulile gramaticale ale sistemului, ele trebuie sa fie puse sub forma de comentarii pentru ca sistemul sa le ignore


Exista doua tipuri de comentarii:
1. comentarii multi-line -> comentarii care se pot scrie pe mai multe linii. Sunt reprezentate de un text scris intre doua perechi de trei ghilimele sau apostroafe
2. comentarii single-line -> comentarii care se pot scrie pe o singura linie. Sunt reprezentate de un text precedat de semnul #

Acum suntem in interiorul unui comentariu multi line

Ca sa putem sa comentam mai multe linii in acelasi timp sau sa comentam automat o linie cu comentariu single line
        ne putem folosi de scurtatura CTRL + "/" (pe windows) sau COMMAND + "/" (pe mac)

"""

# comentariu single line
# daca vreau sa mai scriu inca un rand necomentat o sa imi dea eroare
# comentariu marcat cu scurtatura

"""
2. Variabile

Variabilele sunt adrese de memorie la care noi putem stocam informatii
Numele variabilei este de fapt numele adresei de memorie la care sunt stocate informatiile
Numele variabilelor trebuie sa respecte anumite reguli
- trebuie sa inceapa cu litera mica (conventie)
- nu trebuie sa inceapa cu cifra sau caractere speciale (obligatoriu)
- nu trebuie sa contina spatii (obligatoriu)
- numele trebuie sa urmeze formatul camelCase sau snake_case
- numele variabilelor este case-senstive (adica numele pisica nu este egal cu numele Pisica)
- numele variabilelor este unic. Daca vom incerca sa facem o redefinire, 
            de fapt sistemul nu va aloca o alta adresa de memorie ci va schimba informatia de la adresa de memorie deja alocata

"""

marca = "BMW"
"""
aici s-au intamplat doua actiuni:
    1. S-a facut declararea unei variabile marca, adica s-a alocat un spatiu de memorie numit "marca"
    2. S-a facut initializarea variabilei, adica s-a salvat informatia "BMW" la adresa de memorie alocata

BMW trebuie sa fie scris intre ghilimele pentru ca vrem sa fie considerat text dat de la tastatura si nu numele unei variabile
    Daca nu era scris intre ghilimele, sistemul ar fi cautat adresa de memorie numita "BMW". Nu ar fi gasit-o si ar fi returnat eroare
"""

# daca nu folosesc variabila marca, ea va fi marcata cu galben ca si atentionare ca nu am folosit continutul anterior
marca = "Volkswagen" # momentul in care dau o alta valoare pentru o variabila se numeste suprascriere

producator,model = "BMW","X5" # am facut o dubla declarare si initializare, care este posibil in python
                            #  am anuntat sistemul ca vrem sa declaram doua variabile, marca si model
                                    # si in dreapta egalului am specificat valorile cu care vrem sa initializam cele doua variabile

"""
3. Tipuri de date

tipurile de date sunt proprietati ale variabilelor, functiilor sau metodelor 
        care instruiesc sistemul cu privire la valoarea stocata (pentru variabile) sau rezultatul returnat (pentru functii si metode)

exista patru tipuri de date in python:
- string -> putem stoca valori de tip text
- int -> putem stoca valori numerice intregi (pozitive sau negative)
- boolean -> putem stoca doar doua valori: True sau False
- float -> putem stoca numere zecimale (adica numere cu virgula)

Tipul de data in python nu este specificat in mod explicit ca in java, ci este rezultat din valoarea stocata in variabila
Asta este motivul pentru care putem sa facem schimbare de tip de data

"""

variabilaString = "orice text" # am declarat si initializat o variabila cu tipul de date string
variabilaInt = 34
# variabilaInt = "34" # ATENTIE! aici este string si nu int
variabilaBooleanTrue = True
variabilaBooleanFalse = False
# variabilaBooleanFalse = false   -> instructiune ava da eroare pentru ca va cauta o variabila numita false
# variabilaBooleanFalse = "False"   -> ATENTIE! aici este string si nu boolean
variabilaFloat = 3.14 #am declarat si initializat o variabila float
# variabilaFloatRedeclarata = 3,14 -> instructiunea asta nu va stoca o valoare, ci va stoca un tuplu


"""
4. Funcția type() și type casting

Functia type este o functie care returneaza tipul de date al variabilei date ca parametru
Type casting reprezinta fortarea unui tip de data pentru o variabila
Type casting-ul este temporar
Atentie! conversia de la int la float se poate face cu potentiale pierderi de date
"""

print(type(variabilaInt)) # printeaza <class 'int'>
print(type(variabilaString)) # printeaza <class 'str'>
print(type(variabilaBooleanTrue)) # printeaza <class 'bool'>
print(type(variabilaFloat)) # printeaza <class 'float'>

print(type(str(variabilaInt))) # printeaza <class 'str'>
print(type(variabilaInt)) # printeaza <class 'int'>
variabilaInt = str(variabilaInt)
print(type(variabilaInt)) # <class 'str'>

# print(type(int(variabilaString))) # va returna eroare pentru ca nu putem face conversie a unui text la un numar: ValueError: invalid literal for int() with base 10: 'orice text'
variabilaString = "1234"
print(type(int(variabilaString))) # instructiunea asta va merge pentru ca stringul e format doar din numere

print(type(bool(variabilaInt))) #
# variabilaInt = bool(variabilaInt)
print(variabilaInt) #
variabilaBooleanTrue = int(variabilaBooleanTrue)
print(variabilaBooleanTrue)
variabilaBooleanFalse = int(variabilaBooleanFalse)
print(variabilaBooleanFalse)
variabilaFloat = int(variabilaFloat) # instructiunea o sa mearga doar ca taie zecimalele
print(variabilaFloat)

"""
5. Funcția print()

Functia print este o modalitate prin care putem sa afisam informatii in consola

Structura functiei print este urmatoarea:
1. numele functiei (print)
2. valoarea pe care vrem sa o afisam (text, numere, caractere speciale etc)

Daca vrem sa printam text, este foarte important sa fie pus intre ghilimele sau apostroafe. 
        In caz contrar, sistemul va crede ca este o variabila, pe care nu o va gasi si va returna eroare
        
In limbajele de programare in general semnul ghilimele reprezinta delimitator de text
        Orice text este prins intre ghilimele de inceput si ghilimele de final
        Daca incercam sa scriem un al doilea text intre ghilimele in interiorul unui text intre ghilimele, atunci sistemul va considera
                ghilimelele de inceput al celui de-al doilea test ca fiind sfarsitul primului text     
"""

print("Hello world")
print('Hello world') # putem sa specificam textul si intre ghilimele
# print("Hello "Anton" ") -> Sistemul va considera in cazul asta ca textul meu este "Hello", iar Anton este o varibila separata
# Optiuni pentru problema cu limita de text:
#  1. scriem ghilimele in apostroafe
print('Hello "Anton"')
# 2. scriem apostroafe intre ghilimele
print("Hello 'Anton'")
# 3. ne folosim de escape character "\" care instruieste sistemul sa trateze urmatorul caracter nu ca pe un caracter special
                    # ci ca pe un text de afisat pe ecran
print("Hello \"Anton\"")
print('Hello \'Anton\'')

"""
PRINT: Concatenare
Concatenare inseamna lipirea a doua stringuri separate intr-unul singur

"""
# Exemplu:
suntLaCurs = "Sunt la curs "
imiPlace = "Imi place? "
raspuns = "Meh, ma cam plictisesc, vreau la mare sub umbrela."
stringConcatenat = suntLaCurs + imiPlace + raspuns
print(stringConcatenat)
print(suntLaCurs + imiPlace + raspuns)



oraCurenta = 20
# print(stringConcatenat + "Este ora" + oraCurenta)  -> va returna eroare: TypeError: can only concatenate str (not "int") to str
# concatenarea se poate faceƒ doar intre string-uri
#  concatenarea cu alt tip de data este incompatibila
# in cazul asta specific nu va functiona pentru ca semnul "+" are o semnificatie diferita
            # pentru string (concatenare) vs int (adunare)

# Optiuni:
# 1. Pot sa definesc direct valoarea orei intre ghilimele
            # (nu este neaparat o optiune pentru ca nu putem controla tot timpul tipul de data al variabilelor pe care le primim)
# 2. Type casting
print(stringConcatenat + " Este ora " + str(oraCurenta))
# 3. Printare cu formatare
print(f"{stringConcatenat} Este ora {oraCurenta}")

"""
6. Assert

Assert este un cuvant care este tradus ca evaluare
Din punct de vedere tehnic inseamna o comparatie intre doua valori
    Daca comparatia returneaza True, atunci sistemul va merge mai departe cu executarea urmatoarei instructiuni
    Daca comparatia returneaza False, atunci sistemul va opri executia programului curent si va returna eroare: AssertionError
 
Componentele unui assert:
1. keyword-ul assert care anunta sistemul ca urmeaza o evaluare
2. valorea pe care o comparam
3. operatorul de comparare
4. valoarea cu care comparam
5. mesajul de eroare pe care sa il returneze atunci cand comparatia returneaza False (optional)
   
"""

# imiPlaceLaCurs = False
# assert imiPlaceLaCurs == True, "Error, error, studenti plictisiti, fa treaba mai buna"

# user = "abcUser"
# expected_password ="pass123"
# inserted_password = input("Va rugam sa inserati parola: ")
# print(expected_password==inserted_password) # printeaza rezultatul evaluarii
# assert expected_password==inserted_password,"Eroare: parola gresita, mai aveti doua incercari"

# functia input returneaza valori de tip string.
# Ca sa putem sa le procesam ca int trebuie sa facem type casting
a = int(input("Va rugam sa introduceti primul numar: "))
b = int(input("Va rugam sa introduceti al doilea numar: "))
suma = a + b
print(suma)