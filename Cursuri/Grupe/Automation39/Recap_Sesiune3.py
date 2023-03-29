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
print("\t\t\t\t\t\t\t\t\t\t--------------------LISTE-------------------\n\n")
print("Initializare lista goala - se face prin numele listei urmat de egal si doua paranteze patrate\n")
lista_test = []

# declarare = rezervarea unei adrese de memorie reprezentata de un nume
# initializare =  salvarea unei (unor) valori in acea adresa de memorie
# in python declararea si intializarea se fac concomitent pentru ca tipul de date al adreselor de memorie este dat
					# de valoarea care este salvata la acea adresa de memorie
					# daca nu specificam valoarea care se salveaza sistemul nu stie ce fel de memorie sa aloce pentru acea variabila
					# int varsta; -> in java
					# varsta = 5 -> in python

print("Initializare lista populata ")
cursanti_incantati_ca_marti_seara_sunt_la_curs = ["Daniela","Petre","Cosmin","Lidia","Vlad"]
print(cursanti_incantati_ca_marti_seara_sunt_la_curs)

print("Functii care pot fi folosite cu listele"
			"trebuie sa le accesam prin numele listei urmat de punct "
			"acest lucru ne va afisa toate functiile care pot fi folosite cu acea lista ")

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
print(f"\t\t\tLista dupa eliminarea Danielei prin functia remove: {cursanti_incantati_ca_marti_seara_sunt_la_curs}")
print(f"\t\t\tLista inainte de eliminare prin pop este: {cursanti_incantati_ca_marti_seara_sunt_la_curs}")
element_scos = cursanti_incantati_ca_marti_seara_sunt_la_curs.pop(3)
print(f"\t\t\tLista dupa folosirea functiei pop este: {cursanti_incantati_ca_marti_seara_sunt_la_curs}")
print(f"\t\t\tElementul pe care l-am scos este: {element_scos} \n")

print(f"Sortarea listei in ordine ascendenta: ")
cursanti_incantati_ca_marti_seara_sunt_la_curs.sort()
print(f"Lista dupa folosiera functiei sort: {cursanti_incantati_ca_marti_seara_sunt_la_curs}\n")

"https://www.ascii-code.com/ -> pentru interpretarea caracterelor de la tastatura"

print("Adaugarea unui element la finalul listei (in ultima pozitie) -> practic se creste lungimea listei cu un si se adauga un nou index")
cursanti_incantati_ca_marti_seara_sunt_la_curs.append("Daniela")
print(f"Lista dupa folosirea functiei append: {cursanti_incantati_ca_marti_seara_sunt_la_curs} \n")

print("Adaugarea unui element in interiorul listei (pe baza de index) -> toate elementele incepand de la indexul respectiv se vor decala spre dreapta")
cursanti_incantati_ca_marti_seara_sunt_la_curs.insert(3,"Vlad")
print(f"Lista dupa folosirea functiei insert: {cursanti_incantati_ca_marti_seara_sunt_la_curs} \n")

print("Extragerea pozitiei unui anumit element specific ")
print(f"Lidia se afla la indexul: {cursanti_incantati_ca_marti_seara_sunt_la_curs.index('Lidia')}\n")

print("Extragerea elementelor din lista - se face pe baza de index. ")
print(f"La pozitia 0 se afla {cursanti_incantati_ca_marti_seara_sunt_la_curs[0]} " )
print(f"Vlad se afla in pozitia {cursanti_incantati_ca_marti_seara_sunt_la_curs.index('Vlad')} \n")

print("Actualizarea unui element din lista")
cursanti_incantati_ca_marti_seara_sunt_la_curs[2]="Maria"
print(f"Cursanti dupa prima modificare: {cursanti_incantati_ca_marti_seara_sunt_la_curs}")
# cursanti_incantati_ca_marti_seara_sunt_la_curs[5] = "Anton" # returneaza eroare pentru ca nu exista element in pozitia respectiva
print(f"Cursanti a doua modificare: {cursanti_incantati_ca_marti_seara_sunt_la_curs} \n")

print("\n\n \t\t\t\t\t\t\t\t\t\t--------------------SETURI-------------------\n\n")

print("Definirea si intializarea unui set gol")
set_gol = set()
dict_gol = {}
print(f"Setul initializat gol este: {set_gol}")
print(f"Tipul structurii de date de tip set este: {type(set_gol)}")
print(f"Tipul structurii de date de tip dictionar este: {type(dict_gol)} \n")

print("Definirea unui set populat")
set_populat = {3, 'maria', 5, 'r', "test", "ana"}
print(f"Setul initializat cu date este: {set_populat} \n")


print("Eliminarea unui element random din set "
			"se poate face cu functia pop si "
			"returneaza elementul pe care l-a scos. "
			"daca elementul nu exista returneaza eroare")
set_populat.pop()
print(f"Setul rezultat dupa pop este: {set_populat} \n")

print("Eliminarea unui element specific din set")
set_populat.remove("maria")
print(f"Setul rezultat dupa remove este: {set_populat} \n")

print("Adaugarea elementelor duplicate in set. "
			"Daca elementul deja exista in set, nu ne va da eroare, dar nici nu il va adauga")
set_populat.add('ana')
print(f"Setul rezultat dupa add este: {set_populat} \n")

print("Adaugarea elementelor noi in set")
set_populat.add("antonia")
print(f"Setul rezultat dupa add fara duplicate este: {set_populat} \n")

print("Metoda union returneaza toate elementele din doua seturi unite. "
			"Daca exista duplicate, pastreaza un singur element. "
			"metoda nu actualizeaza setul existent, ci returneaza un nou set "
			"care contine elementele din ambele seturi procesate")
set_suplimentar_pentru_actualizare = {"mere","pere","nuci","covrigi"}
rez = set_populat.union(set_suplimentar_pentru_actualizare)
print(f"Rezultatul functiei union este: {rez}")
print(f"Setul initial a ramas neschibat: {set_populat}\n")

print("Metoda update uneste doua seturi distincte. "
			"Daca exista duplicate, pastreaza un singur element. "
			"metoda actualizeaza setul la care se face update prin adaugarea elementelor "
			"din setul cu care se face update ")
set_populat.update(set_suplimentar_pentru_actualizare)
print(f"Setul initial dupa update: {set_populat} \n")

set_suplimentar_pentru_actualizare = {"test"}
print("Intersectia a doua seturi se face prin intermediul metodei intersection")
rez1 = set_populat.intersection(set_suplimentar_pentru_actualizare)
print(f"Setul initial dupa intersection a ramas neschimbat: {set_populat}")
print(f"Rezultatul a fost returnat si salvat intr-un nou set: {rez1} \n")

print(f"Valoarea curenta a setului 1 este: {set_populat}")
print(f"Valoarea curenta a setului 2 este: {set_suplimentar_pentru_actualizare}")

print("Folosirea metodei isSubset: "
			"Un set se poate numi un subset al unui alt set "
			"atunci cand toate elementele din primul set se regasesc in al doilea set")
print(f"Este setul 1 un subset al setului 2? {set_populat.issubset(set_suplimentar_pentru_actualizare)}")
print(f"Este setul 2 un subset al setului 1? {set_suplimentar_pentru_actualizare.issubset(set_populat)} \n")

# Am adaugat-o pe georgiana pentru a observa ca atunci cand cel putin un element dintr-un set
# 			nu se afla in alt set, atunci setul initial nu se paote considera subset al celui de-al doilea set
set_suplimentar_pentru_actualizare.add("georgiana")
print(f"Dupa adaugarea Georgianei este setul 2 un subset al setului 1? {set_suplimentar_pentru_actualizare.issubset(set_populat)} \n")

print("Folosirea metodei isSuperset: "
			"Un set se poate numi un superset al unui alt set "
			"atunci cand toate elementele din al doilea set se regasesc in primul set")

# am scos-o pe georgiana ca sa putem sa simulam din nou functiilem issuperset si issubset
set_suplimentar_pentru_actualizare.remove("georgiana")

print(f"Este setul 1 un superset al setului 2? {set_populat.issuperset(set_suplimentar_pentru_actualizare)}")
print(f"Este setul 2 un superset al setului 1? {set_suplimentar_pentru_actualizare.issuperset(set_populat)} \n")

# Am definit doua seturi identice, ca sa observam comportamentul functiilor issuperset si issubset
set3 ={"Andrei"}
set4={"Andrei"}
print("Atunci cand cele doua seturi sunt identice, rezultatul metodei issubset este egal cu rezultatul metodei issuperset")
print(f"Este setul 3 un superset al setului 4? {set3.issuperset(set4)}")
print(f"Este setul 3 un subset al setului 4? {set3.issubset(set4)}\n")

print("\n\n\t\t\t\t\t\t\t\t\t\t--------------------TUPLURI-------------------\n\n")
print("Definirea si intializarea unui tuplu gol")
tuplu_gol= ()
print(f"Tuplul gol care a fost initializat este: {tuplu_gol}")

# tuple = tuplu (engleza vs romana)
print("Definirea si intializarea unui tuplu populat")
tuplu_populat = ("Andrei","Marin","Ioana","Andrei")
print(f"Am initializat urmatorul tuplu populat: {tuplu_populat} \n")

print("De cate ori apare un element in tuplu? ")
print(f"Andrei apare de {tuplu_populat.count('Andrei')} ori \n")

print("In ce pozitie gasesc un anumit element? ")
print(f"Marin se afla in pozitia {tuplu_populat.index('Marin')}")
print(f"Andrei se afla in pozitia {tuplu_populat.index('Andrei')}\n")

print(f"Lungimea tuplului este: {len(tuplu_populat)} \n")
tuplu_neomogen = ("Andrei",1,True)
print(f"Putem  sa initializam si un tuplu neomogen: {tuplu_neomogen}")

"""
Functia len se poate folosi pe toate structurile de date
Toate structurile de date sunt neomogene, adica pot sa stocheze valori
reprezentate de tipuri de date diverse concomitent
"""

print("\n\n\t\t\t\t\t\t\t\t\t\t--------------------DICTIONARE-------------------\n\n")

print("Definirea si initializarea unui dictionar gol")
dict_nepopulat = {}
print(f"Am initializat urmatorul dictionar gol: {dict_nepopulat} \n")

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
print(f"Jucatorii existenti in dictionarul populat sunt: {jucatori_de_fotbal} \n")

print("Adaugarea unui element in dictionar se poate face "
			"in doua moduri:")

print("\t- Prin folosirea metodei update")
print("\t- Prin incercarea de actualizare a unei chei care nu exista")
print("\t\t\t\tDaca punem in dictionar o cheie care nu exista, atunci ea se va adauga automat")
jucatori_de_fotbal.update({"gica hagi":63})
jucatori_de_fotbal["ianis hagi"] = 24
print(f"Lista de jucatori dupa adaugarea lui gica si ianis hagi este {jucatori_de_fotbal} \n")

print("Extragerea elementelor din dictionar se face pe baza cheii in doua feluri: ")
print("\t\t - Prin accesarea cu paranteze patrate pe baza de cheie ")
print("\t\t - Prin folosirea metodei get pe baza de cheie")
print(f"Messi are: {jucatori_de_fotbal['Messi']} ani")
print(f"Mutu are: {jucatori_de_fotbal.get('Mutu')} ani \n")

print("Stergerea elementelor din dictionar se face pe baza metodei pop")
jucatori_de_fotbal.pop("Maradona")
print(f"Dictionarul dupa eliminarea lui Maradona este: {jucatori_de_fotbal}\n")

print("extargerea tuturor jucatorilor din dictionar")
print(f"{jucatori_de_fotbal.keys()}\n")

print("extargerea tuturor varstelor jucatorilor din dictionar")
print(f"{jucatori_de_fotbal.values()}\n")

print("stergerea din dictionar a ultimului element din dictionar se poate face cu metoda popitem")
jucatori_de_fotbal.popitem()
print(f"Jucatorii de fotbal dupa functia pop: {jucatori_de_fotbal} \n")

print("extragerea tuturor perechilor de jucatori din dictionar")
print(f"{jucatori_de_fotbal.items()}\n")

print("dictionare imbricate (embedded - 2d - nested ) (dictionare in dictionare)")
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