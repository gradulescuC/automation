"""

Structuri de date = adrese de memorie care pot sa stocheze mai multe valori
Exista patru tipuri de structuri de date:
- liste
- seturi
- tupluri
- dictionare

Atentie!!! nu incurcati tipurile de date cu structurile de date

tipuri de date = proprietati ale unui spatiu de memorie
structuri de date = adrese de memorie

"""


"""
1. Listele 

Listele reprezinta adrese de memorie neomogene (pot stoca valori avand diverse tipuri de date)
care sunt ordonate pe baza de index si mutabile

mutabilitate = proprietatea unei structuri de date de a putea sa isi schimbe elementele
(exemplu: vreau sa mut elevul popescu in banca langa elevul ionescu)

Actiuni care se pot face asupra unei liste:
- adaugare elemente 
- stergere elemente
- modificare element la un anumit index
- mutare element la un anumit index

Definirea listei se face pe baza unei perechi de paranteze patrate []
Se poate initializa si o lista goala

"""

# 1. Declararea si initializarea unei liste goale
lista_studenti = []

# 2. Declararea si intializarea unei liste populate
lista_studenti_prezenti = ["Ramona","Vali","Laurentiu","George","Ionut","Dorin"]
lista_studenti_absenti = ["Andreea","Rodica","Catalin"]
# Observatie: pot sa initializez o lista plecand de la un string prin apelarea functiei string
string_test = "Ana are mere si e fericita"
lista_split = string_test.split()
print(lista_split)

#3.  Accesarea elementelor dintr-o lista
# 3.a. Accesarea primului element din lista
print(f"Primul element din lista este: {lista_studenti_prezenti[0]}")

# 3.b Accesarea ultimului element din lista
print(f"Ultimul element din lista este: {lista_studenti_prezenti[len(lista_studenti)-1]}")

# 4. Functii care pot sa fie folosite cu listele
# Functiile se pot apela prin intermediul numele listei urmat de punct

# 4.a Functia append -> Adauga un element in lista la finalul listei
lista_studenti_prezenti.append("Gabriela")
print(f"Lista de studenti dupa append este: {lista_studenti_prezenti}")

# 4.b Functia insert -> Adauga un element in lista intr-o anumita pozitie
lista_studenti_prezenti.insert(3,"Andy")
print(f"Lista de studenti dupa adaugarea lui Andy este: {lista_studenti_prezenti}")

# 4.c Functia index -> Returneaza indexul unui anumit element
print(f"Studenta Vali se afla in lista la indexul {lista_studenti_prezenti.index('Vali')}")

# 4.d Functia remove -> Sterge un element pe baza numelui sau
lista_studenti_prezenti.remove("Andy")
print(f"Lista studenti prezenti dupa inlaturarea lui Andy este: {lista_studenti_prezenti}")

# 4.e Functia pop -> Sterge un element pe baza de index
lista_studenti_prezenti.pop(len(lista_studenti_prezenti)-1)
print(f"Lista studenti dupa scoaterea ultimului element este: {lista_studenti_prezenti}")

# 4.f Functia count numara de cate ori apare un element intr-o lista
print(lista_studenti_prezenti.count("George"))

# 4.g. Functia reverse -> inverseaza elementele listei
lista_studenti_prezenti.reverse()
print(f"Lista de studenti inversata este: {lista_studenti_prezenti}")

#4.h Functia extent uneste listele prin comasare
lista_studenti_prezenti.extend(lista_studenti_absenti)
# lista_studenti_prezenti.append(lista_studenti_absenti)
# varianta de la linisa 87 creaza o lista imbricata
# lista imbricata (embedded list) = lista in lista
print(f"Lista de studenti dupa functia extend este: {lista_studenti_prezenti}")

# 4.j Functia clear -> sterge continutul listei
# lista_studenti_prezenti.clear()
# print(f"Lista studenti dupa apelarea metodei clear este: {lista_studenti_prezenti}")

# 4.k Functia sort -> sorteaza lista in ordine alfabetica
# lista_studenti_prezenti.sort()
# print(f"Lista studenti dupa sortare este: {lista_studenti_prezenti}")
lista_studenti_prezenti.append("andy")
lista_studenti_prezenti.sort()
print(f"Lista studenti dupa adaugarea lui andy este: {lista_studenti_prezenti}")
# sortarea se va face in ordine alfabetica in functie de codul ASCII:
# https://infoas.ro/lectie/90/codul-ascii-tabel-complet

# 5. Crearea unei liste neomogene:
lista_neomogena = [12,"Maria",True,15.3]

"""
2. Seturi

Seturile reprezinta structuri de date neordonate, immutabile 
	Operatii care se pot face intr-un set:
- accesare elemente
- adaugare elemente
- stergere elemente

Definirea unui set se face cu o pereche de acolade
"""

#1. Definirea unui set gol
set_gol = set()
print(type(set_gol))

#2. Definirea unui set populat
set_pisici = {"tom","silvester","garfield","puss in boots","felix"}
set_catei = {"spike","bethowen","lassy","pluto"}

#3. Accesarea unui element din set
# Avand in vedere ca setul nu este indexat, NU putem accesa direct elementele din set
# Putem sa facem in schimb doua operatii similare:
# - parcurgerea setului cu for (vom face la cursul urmator)
# - putem sa verificam daca un element se afla in set cu operatorul IN
print("tom" in set_pisici)
assert "tom" in set_pisici,"Error: Tom nu exista in set_pisici"

#4. Functii care pot fi folosite cu seturile
# 4.a functia add care adauga un nou element in set
set_pisici.add("Jinx")
print(f"Set pisici dupa adaugarea lui Jinx: {set_pisici}")

# 4.b Functia pop sterge un element la intamplare
set_pisici.pop()
print(f"Setul dupa stergerea elementului cu pop este: {set_pisici}")

set_pisici.remove("tom")
print(f"Setul dupa stergerea elementului cu remove este: {set_pisici}")

# set_pisici.discard("bla bla")
# print("am trecut pe aici")
# set_pisici.remove("bla blab bla")

# Diferenta intre remove si discard este ca remove da eroare daca elementul nu exista
# 			si discard executa instructiunea dar nu da eroare daca elementul nu exista

# 4.c Functia update si functia union concateneaza doua seturi
# set_pisici.update(set_catei)
# print(f"Set pisici dupa update: {set_pisici}")
set_rezultat = set_pisici.union(set_catei)
print(f"Set pisici dupa union: {set_rezultat}")

# Diferenta intre update si union este ca update modifica lista de la care se pleaca direct,
# 		in schimb ce union creaza o a treia lista
# 		care reprezinta concatenarea celor doua liste implicate

# 4.c Functia clear sterge continutul setului
# set_pisici.clear()
# print(f"Set pisici dupa clear: {set_pisici}")


"""
Tupluri (tuples)
Tuplurile reprezinta structuri de date ordonate si identificabile 
			pe baza de index care accepta duplicate
			si este imutabil (immutable)
"""
# 1. Definirea unui tuplu gol:
tuplu_gol = ()
print(type(tuplu_gol))

#2. Definirea unui tuplu populat:
tuplu_populat = ("mere","pere","nuci","covrigi","si-o bucata de sorici","mere","si gutui amarui")
greutate = 15,6 # Daca definim o variabila in felul asta, o va identifica automat ca si tuplu
greutate_float= 15.6 # Daca vrem sa definim un float, separatorul trebuie sa fie "."

#3. Functii care se pot folosi cu un tuplu
# 3.a Functia index returneaza indexul primului element dat ca parametru
print(f"Indexul fructului mere este: {tuplu_populat.index('mere')}")
# for i in range(len(tuplu_populat)):
# 		if tuplu_populat[i] == "mere":
# 				print(f"Indexul curent al fructului mere este: {i}")

# 3.b Functia count returneaza de cate ori apare un anumit element in tuplu
print(f"Fructul mar apare de {tuplu_populat.count('mere')} ori")

"""
4. Dictionarele

Un dictionar este o structura de date ordonata care contine mai multe perechi cheie: valoare
Cheile trebuie sa fie unice. Ele servesc drept inlocuitor pentru indexul de la liste

Operatii care se pot face intr-un dictionar:
- adaugare perechi
- stergere perechi
- modificare valoare cheie
- accesare elemente
"""

# 1. Creare dictionar gol:
dict_gol = {}

#2. Creare dictionar populat:
masini = {
		"nume":"bmw",
		"model":"x5",
		"an_fabricatie":2010,
		"tip_tractiune":"spate",
		"norme_euro":"euro4",
		"combustibil":"benzina"
}

#3. Accesarea elementelor dintr-un dictionar
print(f"Numele masinii este: {masini['nume']}")
print(f"Modelul masinii este: {masini.get('model')}")

#4. Adaugarea elementelor in dictionar
masini["numar_locuri"]=5
print(f"Masina are  {masini['numar_locuri']} locuri")

#5.Actualizarea elementelor din dictionar
masini.update({"norme_euro":"euro6"})
print(f"Norma europeana curenta este: {masini['norme_euro']}")
masini["an_fabricatie"]=2012
print(f"Am corectat anul de fabricatie al masinii la valoarea {masini['an_fabricatie']}")

#6.Stergerea elementelor din dictionar
masini.pop("nume")
print(f"Dictionarul curent este {masini}")

#7. Accesarea cheilor din dictionar
print(f"Proprietatile masinii mele sunt: {masini.keys()}")

#8. Accesarea valorilor din dictionar:
print(f"Valorile proprietatilor masinii mele sunt: {masini.values()}")

#9. Accesarea perechilor cheie: valoare
print(f"Dictionarul este format din urmatoarele elemente: {masini.items()}")

#10. Dictionar imbricat
apa_plata = {
		"borsec":{
				"nume":"borsec",
							"producator": "borsec",
							"cantitate_vanzare":"500ml",
							"impachetare":"baxuri"
						},
		"aqua carpatica":{
											"nume":"aqua carpatica",
											"cantitate_vanzare":"2l",
											"impachetare":"sticla"
										 },
		"dorna":
				{
						 "nume":"dorna",
						 "producator":"dorna",
						 "impachetare":"bax",
						 "promovare":{"reclama":"Hai gata cu fotosinteza, la culcare toata lumea"},
						 "televiziune promovare":["tvr1","tvr2","acasa tv","antena1"]
				}
}
print(apa_plata["aqua carpatica"]["impachetare"])
print(apa_plata["dorna"]["promovare"]["reclama"])
print(apa_plata["dorna"]["televiziune promovare"][2])

"""
Testare statica = tehnici de testare fara rulare de cod (analiza statica + review)
Testare dinamica = tehnici de testare cu rulare de cod
a) whitebox (backend - testare de cod)
tehnici de testare
- statement coverage
- decision coverage
b) blackbox (frontend - testare de interfata)
tehnici de testare:
- equivalence partitioning
- boundary value analysis
- state transition testing
- use case testing
- decision table

pip install pylint
cd <calea la care se afla fisierul pe care vreau sa il analizez>
ls (list) -> pentru a vedea toate fisierele din folderul curent
 pylint curs_03.py -> evaluare fisier
 
principiu al testarii care ne avertizeaza sa facem testare cat mai devreme: 
 										Early testing -> testarea timpurie scuteste timp si bani
 										
Verificare  = testare care acopera mai degraba procesul decat produsul
Validare = testare care acopera mai degraba produsul decat procesul
"""