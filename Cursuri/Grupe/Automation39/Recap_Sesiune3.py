"""

Structurile de date sunt adrese de memorie care pot stoca mai multe valori

Atentie!!! structurile de date nu sunt tipuri de date

Exista patru structuri de date principale in python:
1. liste = structuri de date ordonate si indexate care pot stoca mai multe valori.
						listele accepta valori duplicate
						permit stocarea valorilor care sunt reprezentate de diverse tipuri de date (neomogena)
						permite adaugarea, stergea si modificarea elementelor (mutabila) -> atentie!!! imbutabila si nici imputabila
						permite adaugarea de elemente atat la final (append) cat si in interior (insert)
2. seturi = structuri de date neordonate, neindexate, care permit adaugarea si stergerea elementelor, dar nu si modificarea lor
						seturile nu permit adaugarea de duplicate
set1 = {1,3,5,'r',"test"} ->  {1,3,5,'r',"test"}
															{3,1,5,'r',"test"}
															{1,5,3,'r',"test"}

Vreau sa imi inlocuiesti elementul din pozitia 3 din r in m.

3. tupluri = structuri de date ordonate, indexate care nu permit adaugarea, stergerea sau modificarea de elemente, dar care permit duplicate
4. dictionare = structuri de date ordonate (incepand cu python 3.7) care stocheaza informatii de tip cheie:valoare
								ele sunt mutabile, adica permit adaugarea, stergerea si modificarea de elemente
								cheile din dictionar sunt unice, dar valorile de pe chei pot fi duplicate (adica putem avea doua chei cu aceeasi valoare)


"""
print("--------------------LISTE-------------------")
print("Initializare lista goala - se face prin numele listei urmat de egal si doua paranteze patrate")
lista_test = []

# declarare = rezervarea unei adrese de memorie reprezentata de un nume
# initializare =  salvarea unei (unor) valori in acea adresa de memorie
# in python declararea si intializarea se fac concomitent pentru ca tipul de date al adreselor de memorie este dat
					# de valoarea care este salvata la acea adresa de memorie
					# daca nu specificam valoarea care se salveaza sistemul nu stie ce fel de memorie sa aloce pentru acea variabila
					# int varsta; -> in java
					# varsta = 5 -> in python

print("Initializare lista populata")
cursanti_incantati_ca_marti_seara_sunt_la_curs = ["Daniela","Petre","Cosmin","Lidia","Vlad"]

print("Functii care pot fi folosite cu listele"
			"\ trebuie sa le accesam prin numele listei urmat de punct"
			"acest lucru ne va afisa toate functiile care pot fi folosite cu acea lista")

"""
remove -> se foloseste pentru a elimina un element specific pe baza de valoare.
Cand apelez metoda trebuie sa ii dau valoarea pe care vreau sa o scot din lista
Daca valoarea respectiva nu exista in lista returneaza eroare
Daca nu dam niciun parametru primim eroare

pop -> se foloseste pentru a elimina un element specific pe baza de index
				daca nu dam niciun parametru scoate in mod implicit ultimul element din lista
				returneaza elementul pe care l-am scos
"""
# cursanti_incantati_ca_marti_seara_sunt_la_curs = ["Daniela","Petre","Cosmin","Lidia","Vlad"]
cursanti_incantati_ca_marti_seara_sunt_la_curs.remove("Daniela")
print(cursanti_incantati_ca_marti_seara_sunt_la_curs)
print(f"Lista inainte de eliminare este: {cursanti_incantati_ca_marti_seara_sunt_la_curs}")
element_scos = cursanti_incantati_ca_marti_seara_sunt_la_curs.pop(3)
print(cursanti_incantati_ca_marti_seara_sunt_la_curs)
print(f"Elementul pe care l-am scos este: {element_scos}")

print("Sortarea listei in ordine ascendenta")
cursanti_incantati_ca_marti_seara_sunt_la_curs.sort()
print(cursanti_incantati_ca_marti_seara_sunt_la_curs)

"https://www.ascii-code.com/ -> pentru interpretarea caracterelor de la tastatura"

print("Adaugarea unui element la finalul listei (in ultima pozitie) -> practic se creste lungimea listei cu un si se adauga un nou index")
cursanti_incantati_ca_marti_seara_sunt_la_curs.append("Daniela")
print(cursanti_incantati_ca_marti_seara_sunt_la_curs)

print("Adaugarea unui element in interiorul listei (pe baza de index) -> toate elementele incepand de la indexul respectiv se vor decala spre dreapta")
cursanti_incantati_ca_marti_seara_sunt_la_curs.insert(3,"Vlad")
print(cursanti_incantati_ca_marti_seara_sunt_la_curs)

print("Extragerea pozitiei unui anumit element specific")
print(cursanti_incantati_ca_marti_seara_sunt_la_curs.index("Lidia"))

print("Extragerea elementelor din lista - se face pe baza de index. ")
print(f"La pozitia 0 se afla {cursanti_incantati_ca_marti_seara_sunt_la_curs[0]}" )
print(f"Vlad se afla in pozitia {cursanti_incantati_ca_marti_seara_sunt_la_curs.index('Vlad')}")

print("Actualizarea unui element din lista")
cursanti_incantati_ca_marti_seara_sunt_la_curs[2]="Maria"
print(f"Cursanti dupa prima modificare: {cursanti_incantati_ca_marti_seara_sunt_la_curs}")
# cursanti_incantati_ca_marti_seara_sunt_la_curs[5] = "Anton" # returneaza eroare pentru ca nu exista element in pozitia respectiva
print(f"Cursanti a doua modificare: {cursanti_incantati_ca_marti_seara_sunt_la_curs}")

print("--------------------SETURI-------------------")

print("Definirea si intializarea unui set gol")
set_gol = set()
dict_gol = {}
print(f"Tipul structurii de date este: {type(set_gol)}")
print(f"Tipul structurii de date nr 2 este: {type(dict_gol)}")

print("Definirea unui set populat")
set1 = {3,'maria',5,'r',"test","ana"}

print("Eliminarea unui element random din set"
			"se poate face cu functia pop"
			"returneaza elementul pe care l-a scos"
			"daca elementul nu exista returneaza eroare")
set1.pop()
print(f"Setul rezultat dupa pop este: {set1}")

print("Eliminarea unui element specific din set")
set1.remove("maria")
print(f"Setul rezultat dupa remove este: {set1}")

print("Adaugarea elementelor duplicate in set"
			"Daca elementul deja exista in set, nu ne va da eroare, dar nici nu il va adauga")
set1.add('ana')
print(f"Setul rezultat dupa add este: {set1}")

print("Adaugarea elementelor noi in set")
set1.add("antonia")
print(f"Setul rezultat dupa add fara duplicate este: {set1}")

print("Metoda union returneaza toate elementele din doua seturi unite"
			"Daca exista duplicate, pastreaza un singur element"
			"metoda nu actualizeaza setul existent, ci returneaza un nou set"
			"care contine elementele din ambele seturi procesate")

set2 = {"mere","pere","nuci","covrigi"}
rez = set1.union(set2)
print(rez)
print(set1)

print("Metoda update uneste doua seturi distincte"
			"Daca exista duplicate, pastreaza un singur element"
			"metoda actualizeaza setul la care se face update prin adaugarea elementelo"
			"din setul cu care se face update ")
#
# set1.update(set2)
# print(set1)

set2 = {"test"}
print("Intersectia a doua seturi")
rez1 = set1.intersection(set2)
print(set1)
print(rez1)

print(f"Valoarea curenta a setului 1 este: {set1}")
print(f"Valoarea curenta a setului 2 este: {set2}")

print("Folosirea metodei isSubset"
			"Un set se poate numi un subset al unui alt set"
			"atunci cand toate elementele din primul set se regasesc in al doilea set")
print(f"Este setul 1 un subset al setului 2? {set1.issubset(set2)}")
print(f"Este setul 2 un subset al setului 1? {set2.issubset(set1)}")

set2.add("georgiana")
print(f"Dupa adaugare este setul 2 un subset al setului 1? {set2.issubset(set1)}")

print("Folosirea metodei isSuperset"
			"Un set se poate numi un superset al unui alt set"
			"atunci cand toate elementele din al doilea set se regasesc in primul set")

set2.remove("georgiana")

set3 ={"Andrei"}
set4={"Andrei"}

print(f"Este setul 1 un superset al setului 2? {set1.issuperset(set2)}")
print(f"Este setul 2 un superset al setului 1? {set2.issuperset(set1)}")
print(set3.issuperset(set4))
print(set3.issubset(set4))

print("--------------------TUPLURI-------------------")
print("Definirea si intializarea unui tuplu gol")
tuplu_test = ()

# tuple = tuplu (engleza vs romana)
print("Definirea si intializarea unui tuplu populat")
tuplu_populat = ("Andrei","Marin","Ioana","Andrei")

print("De cate ori apare un element in tuplu")
print(f"Andrei apare de {tuplu_populat.count('Andrei')} ori")

print("In ce pozitie gasesc un anumit element?")
print(f"Marin se afla in pozitia {tuplu_populat.index('Marin')}")
print(f"Andrei se afla in pozitia {tuplu_populat.index('Andrei')}")

print(f"Lungimea tuplului este: {len(tuplu_populat)}")

tuplu_neomogen = ("Andrei",1,True)
print(tuplu_neomogen)

"""
Functia len se poate folosi pe toate structurile de date
Toate structurile de date sunt neomogene, adica pot sa stocheze valori
reprezentate de tipuri de date diverse concomitent
"""

print("--------------------DICTIONARE-------------------")

print("Definirea si initializarea unui dictionar gol")
dict_nepopulat = {}

print("Definirea si initializarea unui dictionar populat")
jucatori_de_fotbal = {
		"Ducadam":70,
		"Nicolia":45,
		"Mbape":24,
		"Mutu":45,
		"Benzema":30,
		"Maradona":60,
		"Messi":35,
		"Ronaldo":39
}
print(f"Jucatorii existenti sunt: {jucatori_de_fotbal}")

print("Adaugarea unui element in dictionar se poate face"
			"in doua moduri:")

# Daca punem in dictionar o cheie care nu exista, atunci ea se va adauga automat
jucatori_de_fotbal.update({"gica hagi":63})
jucatori_de_fotbal["ianis hagi"] = 24

# Extragerea elementelor din dictionar se face pe baza cheii:
print(f"Messi are: {jucatori_de_fotbal['Messi']} ani")
print(f"Messi are: {jucatori_de_fotbal.get('Mutu')} ani")

# stergerea elementelor din dictionar se face pe baza metodei pop:
jucatori_de_fotbal.pop("Maradona")
print(f"Dictionarul dupa eliminarea lui Maradona este: {jucatori_de_fotbal}")

# extargerea tuturor jucatorilor din dictionar
print(jucatori_de_fotbal.keys())

# extargerea tuturor varstelor jucatorilor din dictionar
print(jucatori_de_fotbal.values())

# stergerea din dictionar a ultimului element din dictionar se poate face cu metoda popitem
jucatori_de_fotbal.popitem()
print(jucatori_de_fotbal)

# extragerea tuturor perechilor de jucatori din dictionar
print(jucatori_de_fotbal.items())

# dictionare imbricate (embedded - 2d ) (dictionare in dictionare)
jucatori_de_fotbal = {
		"Ducadam":{"varsta":70,"numar_tricou":10,"numar_meciuri":50},
		"Nicolita":{"varsta":45,"numar_tricou":7,
								"titluri_campion":{"balonul_de_aur":2016,
																	 "jucatorul_anului":2010,
																	 "ani_castig":[2016,2010]},
								"numar_meciuri":30}
}

print(f"Nicolita a fost jucatorul anului in: {jucatori_de_fotbal['Nicolita']['titluri_campion']['jucatorul_anului']}")
print(f"Al doilea castig al lui nicolita a fost in anul: {jucatori_de_fotbal['Nicolita']['titluri_campion']['ani_castig'][1]}")