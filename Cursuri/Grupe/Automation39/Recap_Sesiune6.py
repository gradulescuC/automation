"""

Programarea orientata pe obiecte este o modalitate prin care putem sa structuram proprietatile si
	comportamentul unei entitati din viata reala intr-o structura logica ce functioneaza ca un template / schita
Acel template va servi drept model pentru crearea unor entitati care sa reprezinte un exemplu concret din viata reala

Structura logica ce defineste entitatea se numeste clasa si reprezinta un tipar care descrie
atributele pe care ar trebui sa le aiba entitatea si respectiv actiunile pe care poate sa le faca entitatea

Atunci cand cream o entitate propriu-zisa pe baza acelei clase (scheme logice) spunem ca am creat un obiect
	modelat dupa acea schema.
Crearea obiectului pe baza unei clase se numeste instantiere, iar obiectul este o instanta a unei clase

Atunci cand se creeaza obiectul de fapt se rezerva o adresa de memorie care are acces la toate atributele
si functiile din clasa care sta la baza obiectului.

In momentul in care noi vom popula atributele obiectului, de fapt noi vom da valori efective pentru acele atribute
care valori vor fi salvate la adresa de memorie rezervata pentru obiectul instantiat.

Exista posibilitatea sa avem valori ale atributelor definite direct in clasa
care vor fi valabile pentru toate obiectele pana in momentul in care acele valori vor fi suprascrise la nivelul
fiecarui obiect (asta inseamna ca fiecare obiect poate sa aiba propriile valori pentru atributele definite
in clasa)


Orice obiect este creat prin intermediul unei structuri numit constructor care se apeleaza de fiecare
data cand un obiect este creat.
Exista doua tipuri de constructori:
- constructor implicit -> este constructorul care este incorporat in limbajul python si el este apelat
			automat atunci cand nu exista un constructor explicit
- constructor explicit -> este constructorul care este definit de catre utilizator cu scopul de a
			controla felul in care acel obiect este instantiat

Functiile reprezinta o modalitate prin care putem sa scriem una sau mai multe linii de cod care vor fi
		refolosite de cate ori avem nevoie.
Scopul unei functii este de a ne ajuta sa economisim cod, astfel incat sa nu trebuiasca sa scriem aceleasi
		linii de mai multe ori

O functie este definita prin cuvantul cheie def
Componentele unei functii:
1. inceputul functiei definit prin cuvantul cheie def
2. numele functiei care trebuie sa nu fie cuvinte rezervate si care in python de regula urmeaza formatul snake_case
3. parantezele care POT stoca parametri
4. separatorul intre lista de parametri si corpul functiei reprezentat de caracterul ":"
5. corpul functiei - setul de instructiuni care se vor executa la apelarea functiei
6. instructiunea return (optionala)

Atunci cand vrem sa folosim instructiunile salvate intr-o functie trebuie
		sa facem ceea ce se numeste apelarea functiei. Instructiunile dintr-o functie
		se vor executa DOAR DACA APELAM FUNCTIA

Apelarea se face prin scrierea numelui functiei urmat de doua paranteze rotunde
		in interiorul carora vom pune (daca este cazul) argumente

Exista patru tipuri de functii
1. Functii simple
2. Functii cu parametri
3. Functii cu return
4. Functii cu parametri si return

Un parametru este o adresa de memorie reprezentata de un nume
care este specificata intre parantezele rotunde la definirea functiei
si care au rolul de a stoca informatii venite din exterior, informatii care vor fi utilizate
si procesate in momentul executarii instructiunilor

La apelare acele variabile fi inlocuite de valori efective care vor fi salvate
		la adresa de memorie reprezentata de acele variabile.

La definire, numele variabilelor se numesc parametri
La apelare, numele valorilor efective care sunt transmise functiilor se numesc argumente

Returnul este o modalitate prin care putem sa transmitem rezultatul functiei in exterior
Spre exemplu, daca vrem sa calculam suma a doua numere si sa o printam pe ecran
		in momentul apelarii functiei, va trebui sa avem instructiune de return,
		in caz contrar suma va ramane incuiata in interiorul functiei

ATENTIE!!! In interiorul unei clase functiile poarta numele de METODE


Formate de denumire a functiilor, claselor si variabilelor
1. camelCase
2. snake_case
3. kebab-case
"""

class Scoala():
		# Atribute pe care le pot avea scolile
		adresa = None # am pus none pentru ca fiecare obiect poate sa aiba
								# propria adresa si nu are sens sa fortam o adresa
								# specifica pentru toate scolile din oras
		ciclu_invatamant = "primar"
		capacitate_elevi = None
		numar_profesori = None
		profil = "Real"
		clase = {}

		# Am definit un constructor explicit
		def __init__(self,adresa,ciclu_invatamant,profil):
				self.adresa = adresa
				self.ciclu_invatamant = ciclu_invatamant
				while profil.lower() not in ("real","uman"):
						profil = input("Profil invalid. Va rugam sa introduceti una din optiunile: Real, Uman ")
						self.profil = profil

		# Activitati care se pot face intr-o scoala
		def adauga_clasa(self,nume_clasa,profil, ciclu, numar_elevi, numar_profesori):
		# 		# ca sa putem accesa atributele definite intr-o clasa, trebuie sa le precedam
		# 		# de cuvantul cheie self. In caz contrar, sistemul va crede ca incercam
		# 		sa accesam unul dintre parametrii definiti in metoda
		 		self.clase[nume_clasa]={"profil":profil,
																"ciclu":ciclu,
																"numar_elevi":numar_elevi,
																"numar_profesori":numar_profesori
																}

		"""
		
		"""

		def actualizeaza_adresa_scoala(self,adresa_noua):
				self.adresa = adresa_noua
				print(self.adresa)
				return self.adresa


		def extrage_numarul_de_profesori(self):
				return self.numar_profesori

# Facem instantierea unui nou obiect
# Atunci cand instantiem un obiect dintr-o clasa care are constructor
# 		explicit suntem obligati sa dam valori pentru parametrii definiti
# 		in constructorul explicit

# scoala1 = Scoala() -> instructiunea returneaza eroare: TypeError: Scoala.__init__() missing 3 required positional arguments: 'adresa', 'ciclu_invatamant', and 'profil'
# 											eroarea este returnata pentru ca incercam sa instantiem un obiect
# 											fara a da valori parametrilor din constructor

# Am instantiat un obiect din clasa Scoala cu valori pentru parametrii constructorului
scoala1 = Scoala("Strada lalelelor 23","primar","Uman")

# Ca sa putem sa vedem atributele si metodele la care are acces obiectul
# 		trebuie sa scriem numele obiectului urmat de caracterul "."
# print(f"Adresa scolii este: {scoala1.adresa}")
# print(f"Ciclul de invatamant al scolii este: {scoala1.ciclu_invatamant}")
# print(f"Profilul scolii este: {scoala1.profil}")

# scoala1.actualizeaza_adresa_scoala("Strada Micsunelelor numarul 45")
# print(f"Noua adresa scolii este: {scoala1.adresa}")
# # printam doar obiectul -> se printeaza de fapt adresa de memorie care reprezinta obiectul
# print(scoala1)

# Actualizam numarul de profesori din scoala:
# scoala1.numar_profesori = 45
# print(scoala1.extrage_numarul_de_profesori())

# Avand in vedere ca metoda actualizeaza_adresa_scoala nu are return
# 			instructiunea de mai jos va printa None
# print(scoala1.actualizeaza_adresa_scoala("Strada Magnoliei numarul 125"))
# adresa_actualizata = scoala1.actualizeaza_adresa_scoala("Strada cireselor numarul 31")
# print(adresa_actualizata)

# scoala2 = Scoala()
# print(scoala2.adresa)
# print(scoala2.profil)
# print(scoala2.ciclu_invatamant)

print(f"Atributele definite la nivel de clasa sunt: "
			f"{Scoala.adresa, Scoala.profil, Scoala.ciclu_invatamant, Scoala.clase,Scoala.numar_profesori}"
			)
print(f"Atributele definite la nivel de obiect scoala1 sunt: "
			f"{scoala1.adresa, scoala1.profil, scoala1.ciclu_invatamant, scoala1.clase,scoala1.numar_profesori}"
			)

# Atentie!!! ordinea argumentelor date la instantiere trebuie
# sa coincida cu ordinea parametrilor definiti in constructor

scoala3 = Scoala("Strada margelelor numarul 5","Gimnazial","Uman")

print(f"Atributele definite la nivel de obiect scoala3 sunt: "
			f"{scoala3.adresa, scoala3.profil, scoala3.ciclu_invatamant, scoala3.clase,scoala3.numar_profesori}"
			)

"""

Concluzie:

Nu este obligatoriu sa:
- avem constructor explicit
- sa avem return la functie
- sa avem parametrii la functie

Ele vor fi implementate doar atunci cand avem nevoie

"""





