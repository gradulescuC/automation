"""

Structuri repetitive = modalitati prin care putem executa un cod in mod repetat
					pana cand o anumita conditie nu mai este indeplinita
					sau pana cand nu ne mai incadram intr-un anumit interval

Exista patru tipuri de structuri repetitive:
while
do while (nu e in scopul cursului)
for
for each

Modalitati de control al structurilor repetitive:
- break
- continue

"""

"""

1. While  este o structura repetitiva in care executam o serie de instructiuni atata timp cat o conditie este adevarata
De regula elementul sau variabila de control a while-ului se declara in afara acestuia

"""
# Exercitiu 1: Vreau sa printez pe ecran toate numerele de la 1 la 10
c = 1
while c<=10:
		print(f"Numarul curent este: {c}")
		c+=1
# debugging = proces prin care analizam codul pentru a vedea cum circula datele
# de fiecare data cand vrem sa facem debugging putem sa punem ceea ce se numeste
					# breaking points in cod, ca sa oprim executia la fiecare breaking point

# Exercitiu 2: Vreau sa printez pe ecran pe cei 101 dalmatieni
i = 1
while i <=101:
		print(f"Dalmatiunul curent are numarul: {i}")
		i+=1

# Exercitiu 3: Vreau sa printez suma numerelor de la 1 la 10
j = 0
suma = 0
while j<=10:
		suma += j
		j+=1
print(f"Suma numerelor este: {suma}")

# Exercitiu 4: Vreau sa parcurg o lista de elemente si sa printez fiecare element din lista
lista_studenti_indragostiti_de_while = ["ramona","catalin","laurentiu","george","ionut","dorin"]
i = 0
while i<len(lista_studenti_indragostiti_de_while):
		print(f"Studentul curent este: {lista_studenti_indragostiti_de_while[i]}")
		i+=1

# Exercitiu 5: Vreau sa il inlocuiesc pe Dorin cu Andreea pentru ca lui Dorin nu ii place while
i = 0
while i<len(lista_studenti_indragostiti_de_while):
		if lista_studenti_indragostiti_de_while[i]=="dorin":
				lista_studenti_indragostiti_de_while[i]="andreea"
		i+=1
print(f"Lista finala dupa ce dorin ne-a parasit este: {lista_studenti_indragostiti_de_while}")

# Exercitiu 5: Vreau sa il inlocuiesc pe Laurentiu cu Dorin pentru ca Dorin s-a razgandit si l-a dat pe George afara de entuziasm
while i<len(lista_studenti_indragostiti_de_while):
		if lista_studenti_indragostiti_de_while[i]=="dorin":
				lista_studenti_indragostiti_de_while[i]="andreea"
				break
		i+=1
print(f"Lista finala dupa ce dorin l-a dat afara pe george este: {lista_studenti_indragostiti_de_while}")

# break se foloseste pentru a termina executia restului de iteratii indiferent daca conditia mai este indeplinita sau nu

"""
2. For = structura repetitiva care este utilizata atunci cand vrem sa parcurgem o lista cu scopul de a printa elementele
					sau de a le modifica, si respectiv atunci cand vrem sa executam un set de instructiuni de un numar specific
							de ori (range)
Elementele din care este compus un for:
- inceputul structurii repetitive (for)
- variabila de iteratie
- inceputul range-ului de parcurs (default 0)
- sfarsitul range-ului de parcurs(obligatoriu) - capatul superior nu este luat in considerare
- pasul range-ului (default este 1)
"""

#Exercitiu 1: Vreau sa parcurg numerele de la 0 la 10 si sa printez care sunt pare:
for i in range(11):
		if i%2 == 0:
				print(f'Numarul {i} este par')
		else:
				print(f"Numarul {i} este impar")

# nested list- embedded list - lista imbricata - matrice
lista_elemente = [
		[1,"test"],
		[2,"test1"],
		[3,"test2"]
]
for i in range(len(lista_elemente)):
		for j in range(len(lista_elemente[i])):
				print(f"Valoarea curenta a elementului din lista este: {lista_elemente[i][j]}")

# Vrem sa parcurgem o lista de elemente, sa zicem fructe. Vrem sa printem fiecare fruct pe ecran,
							# si daca sunt caise sa le inlocuim cu gutui
lista_fructe  = ["mere","pere","prune","caise","struguri"]
for i in range(len(lista_fructe)):
		if lista_fructe[i]=="caise":
				lista_fructe[i]="gutui"
print(f"Lista de fructe de toamna este: {lista_fructe}")

# Avem o lista de culori. Si vrem sa vindem haine in culorile respective
			# cand vine un cumparator vrem sa ii prezentam haine in culorile alese de el
			# adica, daca cumparatorul ne spune ca nu ii place culoarea x, ii vom exclude de la prezentare hainele in culoarea respectiva


lista_culori_disponibile = ["rosu","galben","albastru","fuchsia","magenta","roz","violet","maro","negru","orange","verde","indigo"]
liste_culori_de_exclus = ["rosu","galben","roz"]
for i in range(len(lista_culori_disponibile)):
		if lista_culori_disponibile[i] in liste_culori_de_exclus:
				continue
		print(f"Va recomandam haine in culoarea: {lista_culori_disponibile[i]}")

# continue este o modalitate prin care putem sa sarim peste iteratia curenta
					# fara sa iesim din structura repetitiva

"""
foreach = structura repetitiva care este utila mai ales atunci cand vrem sa stergem elemente dintr-o lista 

Diferenta intre for si foreach e ca la for stocam indexul in variabila de iteratie
			iar la foreach stocam elementul din lista in variabila de iteratie
"""
lista_animale = ["elefant","maimuta","leu","pantera","cocos"]
# for i in range(len(lista_animale)):
# 		print(f"indexul curent este: {i}")
# 		if lista_animale[i] == "cocos":
# 				lista_animale.pop(i)
# 		print(f"Animalul curent este: {lista_animale[i]}")
# print(f"Lista dupa eliminarea cocosului este: {lista_animale}")

# de recomandat cand vrem sa modificam elemente sa nu folosim for
				# pentru ca dimensiunea listei nu este calculata in mod dinamic
					# si la un moment dar se va incerca sa se acceseze un element de la un index care nu exista

# exemplu de foreach
for animal in lista_animale:
		print(f"indexul curent este: {lista_animale.index(animal)}")
		if animal == "cocos":
				lista_animale.remove(animal)
		print(f"Animalul curent este: {animal}")
print(f"Lista dupa eliminarea cocosului este: {lista_animale}")


""""

Algoritmul de sortare a listelor prin metoda bulelor (bubble sort)
Algoritmul presupune sa evaluam daca un element de la o anumita pozitie este mai mic decat un element de la o alta pozitie
Daca da, ne vom folosi de o variabila swap (bula, pahar) in care vom stoca temporar una dintre valori pentru a face transferul

"""
# bubble sort cu variabila swap
lista_numere = [6,5,4,8,9,3,-1,10]  #  [0][1], [1][2], [1][3], [1][4], [1][5],[1][6]
																		# 6>5, -> [5,6,4,8,9,3,-1,10]
																		# 5>4 -> [4,6,5,8,9,3,-1,10]
																		# 4 > 8
																		# 4 > 9
																		# 4 > 3 -> [3,6,5,8,9,4,-1,10]
																		# [1][2], [1][3], [1][4], [1][5],[1][6]
																    # [2][3], [2][4], [2][5], [2][6]
																	  # [3][4], [3][5], [3][6]
																	  # [4][5], [4],[6]
																	  # [5][6]
for i in range(len(lista_numere)-1):
		schimbare = False
		for j in range(i+1,len(lista_numere)):
				if lista_numere[i]>lista_numere[j]:
						swap = lista_numere[i]
						lista_numere[i] = lista_numere[j]
						lista_numere[j] = swap
						schimbare = True
		if schimbare == False:
				break
print(f"Lista sortata crescator este: {lista_numere}")
"""

ITERATIA 1:
i = 0
	j = 1 -> lista_numere[i]>lista_numere[j]: = 6 > 5
						swap = 6
						lista_numere[i] = 5
						lista_numere[j] = 6 => [5,6,4,8,9,3,-1,10]
	j = 2 -> lista_numere[i]>lista_numere[j]: 5 > 4
						swap = 5
						lista_numere[i] = 4
						lista_numere[j] = 5 => [4,6,5,8,9,3,-1,10]
	j = 3 -> lista_numere[i]>lista_numere[j]: 4 > 8
	j = 4 -> lista_numere[i]>lista_numere[j]: 4 > 9
	j = 5 -> lista_numere[i]>lista_numere[j]: 4 > 3
						swap = 4
						lista_numere[i] = 3
						lista_numere[j] = 4 => [3,6,5,8,9,4,-1,10]
  j = 6 -> lista_numere[i]>lista_numere[j]: 3 > -1
  					swap = 3
						lista_numere[i] = -1
						lista_numere[j] = 3 => [-1,6,5,8,9,4,3,10]
	j = 7 -> lista_numere[i]>lista_numere[j]: -1 > 10	
								
i = 1
	j = 2 -> lista_numere[i]>lista_numere[j]: = 6 > 5
						swap = 6
						lista_numere[i] = 5
						lista_numere[j] = 6 => [-1,5,6,8,9,4,3,10]
	j = 3 -> lista_numere[i]>lista_numere[j]: 5 > 8
	j = 4 -> lista_numere[i]>lista_numere[j]: 5 > 9
	j = 5 -> lista_numere[i]>lista_numere[j]: 5 > 4
						swap = 6
						lista_numere[i] = 5
						lista_numere[j] = 6 => [-1,4,6,8,9,5,3,10]
	j = 6 -> lista_numere[i]>lista_numere[j]: 4 > 3
						swap = 4
						lista_numere[i] = 3
						lista_numere[j] = 4 => [-1,3,6,8,9,5,4,10]
  j = 7 -> lista_numere[i]>lista_numere[j]: 3 > 10

i = 2
	j = 3 -> lista_numere[i]>lista_numere[j]: = 6 > 8
	j = 4 -> lista_numere[i]>lista_numere[j]: 6 > 9
	j = 5 -> lista_numere[i]>lista_numere[j]: 6 > 5
					  swap = 6
						lista_numere[i] = 5
						lista_numere[j] = 6 => [-1,3,5,8,9,6,4,10]
	j = 6 -> lista_numere[i]>lista_numere[j]: 5 > 4
						swap = 5
						lista_numere[i] = 4
						lista_numere[j] = 5 => [-1,3,4,8,9,6,5,10]
	j = 7 -> lista_numere[i]>lista_numere[j]: 4 > 10
	
i = 3
	j = 4 -> lista_numere[i]>lista_numere[j]: = 8 > 9
	j = 5 -> lista_numere[i]>lista_numere[j]: 8 > 6
	 					swap = 8
						lista_numere[i] = 6
						lista_numere[j] = 8 => [-1,3,4,6,9,8,5,10]
	j = 6 -> lista_numere[i]>lista_numere[j]: 6 > 5
					  swap = 6
						lista_numere[i] = 5
						lista_numere[j] = 6 => [-1,3,4,5,9,8,6,10]
	j = 7 -> lista_numere[i]>lista_numere[j]: 5 > 10
"""



# ------------------------------------------
# bubble sort fara variabila swap

lista_numere = [6,5,4,8,9,3,-1,10]
for i in range(len(lista_numere)-1):
		for j in range(i+1,len(lista_numere)):
				if lista_numere[i]<lista_numere[j]:
						swap = lista_numere[i]
						lista_numere[i],lista_numere[j]=lista_numere[j],lista_numere[i]
						lista_numere[j] = swap
print(f"Lista sortata descrescator este: {lista_numere}")

# interschimbarea valorii a doua numere
a = 14
b = 2
if a>b:
		aux = a
		a = b
		b = aux
print(a,b)


lista_text = ["anton","maria","trandafir","teodor","noapte","teofil","marti","curs"]
for i in range(len(lista_text)-1):
		for j in range(i+1,len(lista_text)):
				if lista_text[i]<lista_text[j]:
						swap = lista_text[i]
						lista_text[i],lista_text[j]=lista_text[j],lista_text[i]
						lista_text[j] = swap
print(f"Lista de texte sortata descrescator pe baza codului ASCII este: {lista_text}")