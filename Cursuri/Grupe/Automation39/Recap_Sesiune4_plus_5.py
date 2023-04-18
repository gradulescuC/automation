"""

In programare exista anumite concepte care se numesc structuri repetitive

Recapitulare structuri:

a) structuri de date: liste, seturi, tupluri, dictionare
b) structuri alternative: if-elif-else
c) structuri repetitive: while, for, for each, do while

Metode de control al structurilor repetitive:
a) break -> incheie executia tuturor iteratiilor curente si viitoare din structura repetitiva
b) continue -> sare peste iteratia curenta, dar executa iteratiile viitoare

While este o structura repetitiva care executa un set de instructiuni atata timp cat o conditie
			este adevarata
			De regula se foloseste atunci cand nu stim exact de cate ori trebuie sa executam setul de instructiuni
			Cu alte cuvinte se foloseste atunci cand nu stim exact momentul in care conditia nu va mai fi adevarata
			Componentele unui while:
			a) o variabila de control al while-ului, de regula declarata inainte de inceperea while-ului (nu e necesara mereu)
			b) inceputul while-ulului marcat de cuvantul cheie WHILE
			c) conditia de evaluare (cea pe baza caruia se va decide daca se mai trece o data prin while sau nu)
			d) separatorul intre conditia de evaluare si corpul while-ului care este caracterul ":"
			e) corpul while-ului care este seria de instructiuni care se vor executa

For este o structura repetitiva care executa un set de instructiuni pe baza unui range si care se foloseste
			atunci cand stim exact de cate ori vrem sa repetam un anumit set de instructiuni.
			El se bazeaza pe o variabila de iteratie care va stoca rand pe rand valoarea din range.
			In cazul in care parcurgem structurile date indexate cu un for, variabila de iteratie va stoca pe rand
			indexul fiecarui element din lista
			Componentele unui for:
			a) inceputul for-ului marcat de cuvantul cheie FOR
		  b) variabila de iteratie care va stoca indexul din range / din structura repetitiva
			c) range-ul sau structura repetitiva care sunt parcurse
		  d) separatorul intre range-ul de parcurs si corpul for-ului care este caracterul ":"
			e) seria de instructiuni care reprezinta corpul for-ului

For each este o structura repetitiva care executa un set de instructiuni pe baza unei structuri de date
			si care se bazeaza pe o variabila de iteratie
			Diferenta intre for si for each este aceea ca in cazul for-ului variabila de iteratie stocheaza
			indexul curent al elementului din lista in timp ce la foreach variabila de iteratie stocheaza
			valoarea curenta a elemenului aflat la un anumit index
		  Componentele unui for each:
			a) inceputul for-ului marcat de cuvantul cheie FOR
		  b) variabila de iteratie care va stoca elementul curent din structura parcursa
			c) range-ul sau structura repetitiva care sunt parcurse
		  d) separatorul intre range-ul de parcurs si corpul for-ului care este caracterul ":"
			e) seria de instructiuni care reprezinta corpul for-ului

"""

# Exercitiu 1: Vreau sa ii printez pe cei 101 dalmatieni:
# Varianta 1: cu while
# numar_dalmatian = 1
# while numar_dalmatian<=101:
# 		print(f"Dalmatianul curent are numarul {numar_dalmatian}")
# 		numar_dalmatian += 1
#
# # Varianta 2: cu for
# print("------------FOR------------")
# for i  in range(1,102): # capatul superior de la range nu este luat in considerare
# 													# drept urmare trebuie sa definim range-ul cu un pas mai sus
# 		print(f"Dalmatianul curent are numarul {i}")

# Exercitiul 2: Vreau sa calculez suma tuturor numerelor de la 1 la 10
# suma = 0
# for i in range(1,11):
# 		suma+=i
#
# print(f"Valoarea curenta a sumei este: {suma}")

# suma = 0
# i = 1 # asta este variabila de iteratie
# 					# i = numarul care se aduna.
# while i>=1 and i<=10:
# 		suma=suma+i # varianta alternativa: suma+=1
# 		print(f"Am adunat numarul {i}")
# 		i+=1

"""
Debugging reprezinta procesul de analiza a codului prin care
putem sa observam cum circula datele si prin intermediul caruia
putem sa identificam potentialele probleme

Pentru a face debugging trebuie sa punem un break point in locul
unde vrem sa vedem cum circula datele
Cate breakpointuri vom pune, de atatea ori se va opri codul
Un breakpoint este un loc unde codul se opreste inainte
sa execute urmatoarea instructiune

Ca sa punem un breakpoint dam click pe marginea din stanga a fisierului
intre cifra indicatoare a randului si marginea fisierului

Dupa ce am pus breakpoint urile de care avem nevoie dam click dreapta pe fisier, dar in loc 
sa alegem run alegem optiunea debug
"""

# Exercitiu 3: Vrem sa parcurgem o lista de masini
# si sa alegem din lista doar daca este mercedes. Daca este mercedes
		# atunci nu vom mai verifica si celelalte masini
		# deoarece clientul este interesat doar de mercedes

# lista_masini = ["Audi","Skoda","Lastun","Ferrari","Porche","Trabant","Alpha Romeo","Dacia","Mustang","Tesla","Mercedes"]

# Varianta 1 cu while
# i = 0
# while i<=len(lista_masini):
# 		if lista_masini[i]=="Mercedes":
# 				print("Asta e masina pe care v-o doriti")
# 				break
# 		i+=1

# Varianta 2 cu for
# for i in range(len(lista_masini)): # la range valoarea de start a range-ului este in mod implicit 0
# 		if lista_masini[i]=="Mercedes":
# 				print("Asta e masina pe care v-o doriti")
# 				break

# Am pus break in interiorul if-ului, pentru ca altfel se va iesi din iteratie inca de la primul element
			# indiferent daca este ceea ce ne intereseaza sau nu


# lista_masini = ["Skoda","Ferrari","Porche","Audi","Alpha Romeo","Dacia","Mustang","Tesla","Mercedes"]

# for i in range(len(lista_masini)): # la range valoarea de start a range-ului este in mod implicit 0
# 		if lista_masini[i]=="Audi":
# 				raspuns = input("E ok masina?")
# 				break

# Varianta 3 cu foreach

# for masina in lista_masini:
# 		if masina == 'Mercedes':
# 				print("Am gasit masina dumneavoastra")
# 				break
# 		else:
# 				print("Nu am gasit masina, mai cautam")

"""
Diferenta intre for si foreach este ca for-ul salveaza in variabila de iteratie (i)
indexul elementului din lista in timp ce foreach-ul salveaza in variabila de iteratie (masina)
valoarea elementului salvat la un anumit index
"""

# Sa definim o functie care sa parcurga pe rand elementele din lista si sa
# evalueze daca masina curenta este Trabant sau lastun
# acestea fiind masini mai vechi vor fi adaugate intr-o lista noua numita masini_vechi
# si vor fi sterse din lista initiala
# Pentru fiecare masina parcursa vom printa pe ecran urmatoarea propozitie:
		#  va propunem masina x
		# propozitia va fi printata pentru TOATE masinile MAI PUTIN Trabant si Lastun

masini_vechi = []
lista_masini = ["Audi","Skoda","Lastun","Ferrari","Porche","Alpha Romeo","Dacia","Mustang","Tesla","Mercedes","Trabant"]
def functie_parcurgere_lista_cu_while():
		i = 0
		while i<=len(lista_masini):
				if lista_masini[i] == "Lastun" or lista_masini[i]=="Trabant":
						masini_vechi.append(lista_masini[i])
						lista_masini.remove(lista_masini[i])
						continue
				print(f"Va propunem masina {lista_masini[i]}")
				print(f"Masinile vechi curente sunt: {masini_vechi}")
				print(f"Masinile noi curente sunt: {lista_masini}")
				print(f"Lungimea curenta a listei este: {len(lista_masini)}")
				i+=1

# functie_parcurgere_lista_cu_while()


def functie_parcurgere_lista_cu_for():
		for i in range (len(lista_masini)):
				if lista_masini[i] == "Lastun" or lista_masini[i] == "Trabant":
						masini_vechi.append(lista_masini[i])
						lista_masini.remove(lista_masini[i])
						continue
				print(f"Va propunem masina {lista_masini[i]}")
				print(f"Masinile vechi curente sunt: {masini_vechi}")
				print(f"Masinile noi curente sunt: {lista_masini}")
				print(f"Lungimea curenta a listei este: {len(lista_masini)}")
				print(f"Indexul elementului curent este: {i}")

# functie_parcurgere_lista_cu_for()


def functie_parcurgere_lista_cu_foreach():
		for masina in lista_masini:
				if masina == "Lastun" or masina == "Trabant":
						masini_vechi.append(masina)
						lista_masini.remove(masina)
						print(f"Masinile vechi curente sunt: {masini_vechi}")
						print(f"Masinile noi curente sunt: {lista_masini}")
						continue
				print(f"Va propunem masina {masina}")
				print(f"Masinile vechi curente sunt: {masini_vechi}")
				print(f"Masinile noi curente sunt: {lista_masini}")
				print(f"Lungimea curenta a listei este: {len(lista_masini)}")
				print(f"Indexul elementului curent este: {lista_masini.index(masina)}")

functie_parcurgere_lista_cu_foreach()

"""
Exista posibilitatea sa definim functii cu un numar nedefinit de parametri
Asta inseamna ca ramane ca sistemul sa decida la apelarea functiei cati parametri 
trebuie sa defineasca pentru functia respectiva

numarul indefinit de parametri se defineste cu *args

args  = prescurtarea de la arguments. Putem da si alt nume, dar de regula asta este 
				folosit ca si conventie
"""

def suma_numere(*args):
		suma = 0
		for numar in args:
				suma += numar
		return suma

print(suma_numere(1,3))
print(suma_numere(123456,456,123456,23456789,23,1234567,234567))
print(suma_numere())

# Am definit un nested dictionary (nested dictionary = embedeed dictionary = dictionar imbricat = dictionar in dictionar = dictionar 2D)
fotbalisti_pe_echipe = {
		"Barcelona":{
								 "Dica":
										 {"Nume complet":"Nicolae Dica",
												 "Varsta":45,
												 "Numar Tricou":10
											},
								 "Banel":{"Nume complet":"Banel Nicolita",
													"Varsta":47,
													"Numar Tricou":3
													},
								 "Dukadam":{"Nume complet":"Helmut Dukadam",
														"Varsta":65,
														"Numar Tricou":7
														}
								 }
		}

def afiseaza_fotbalisti(**kwargs):
		for key_echipa, value_echipa in kwargs.items():
				for key_jucator, value_jucator in value_echipa.items():
						print(f"La echipa {key_echipa} joaca jucatorul:")
						for key_detalii_jucator, value_detalii_jucator in value_jucator.items():
								print("Detalii jucator", f"{key_detalii_jucator}:{value_detalii_jucator}", sep=" - ", end=",")
						print("\n--------------------------------")

# Atunci cand apelam o functie cu keyargs ca primeste ca argument un dictionar, a
# 	acel dictionar trebuie sa fie precedate de doua caractere "*"
afiseaza_fotbalisti(**fotbalisti_pe_echipe)

# suprascrierea parametrilor functiei print functioneaza doar pana la urmatorul print
print("test test1", end = ",")
print("test2")
print("test3")

