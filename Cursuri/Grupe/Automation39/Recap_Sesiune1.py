"""
Comentarii = Linii de cod care sunt ignorate de catre sistem din punctul de vedere
							al limbajului si care ne ajuta la documentarea codului

							Exista doua tipuri de comentari:
							- comentarii single line marcate cu caracterul #
							- comentarii multiple-line marcate cu triple quotes

Variabile = Adrese de memorie care pot sa stocheze diverse valori care pot sa difere de-a lungul executiei programului
						Initializarea variabilelor in python se face prin folosirea operatorului de atribuire
						Initializarea variabilelor in python este obligatorie, deoarece continutul acesteia defineste
										tipul de data al acelei variabile - Python este un limbaj loosely-typed, adica
													nu restrictioneaza o variabila la un anumit tip de data pe tot parcursul executiei

Constante = Adrese de memorie care pot sa stocheze diverse valori care nu pot sa difere de-a lungul executiei programului
				    In Python termenul de constanta exista doar ca si conventie, prin scrierea lor cu majuscule,
				    dar ele sunt tratate tot ca si variabile

Tipuri de date = Proprietati ale adreselor de memorieale adreselor de memorie care definesc ce fel de informatii pot fi stocate
								la acea adresa de memorie. Tipul de date poate varia in functie de valoarea salvata la acea adresa de memorie
								si se poate schimba pe parcursul executiei programului

								Exemplu:
								varsta = 3 # am initializat o variabila cu valoarea 3 reprezentata de tipul de date int
								varsta = 5 # am schimbat valoarea, dar tipul de date a ramas neschimbat
								varsta = "cinci" # am schimbat valoarea si implicit si tipul de date

Type casting = Modalitate prin care putem sa fortam un anumit tip de date unei valori.
               Exemplu de utilitate:
               Vrem sa extragem dintr-un site web numarul de produse returnate in urma cautarii si vrem sa evaluam
               daca acel numar este mai mare sau egal cu un numar specific (gen ne intereseaza sa vedem ca avem cel putin
               10 rezultate in urma cautarii). Valoarea extrasa din browser va fi string, iar pentru a putea
               sa o evaluam trebuie sa ii facem casting la int

               Exemplu 2:
               Aceeasi valoare din browser este extrasa direct ca si float, si vrem sa avem o comparatie mai precisa
               intre doua elemente de acelasi tip ca sa tratam doar valori intregi. Si atunci facem conversie la int

5.999 99 Lei
valoare_produs = chrome.find_element(By.ID,"valoare_id").text.replace(" ","").replace("Lei","").replace(".","")
int(valoare_produs) == 5999

               Exemplu 3:
               Vrem sa introducem varsta unui utilizator de la tastatura, si in functie de ea sa evaluam
               daca acea persoana beneficiaza de discount la cumpararea unui bilet de avion.
               Pentru asta trebuie sa comparam varsta introdusa de la tastatura cu o valoare numerica
               pentru a ne da seama daca persoana respectiva este eligibila pentru discount.
               In mod implicit tipul de date al valorilor introduse de la tastatura este string,
               iar in cazul asta comparatia nu va fi posibila decat prin type casting care sa forteze valoarea la int

               varsta_utilizator = input("Va rugam sa introduceti varsta pasagerului")
               assert int(varsta_utilizator)<=18 or int(varsta_utilizator)>=65,"Pasagerul nu se incadreaza la discount"

Print statement = este o functie care ne ajuta sa afisam informatii in consola

Printare cu formatare = modalitate prin care putem integra variabile in interiorul unui string
												daca nu am folosi printare cu formatare, am fi obligati sa folosim concatenare
												care ar putea duce la erori de incompatibilitate in cazul in care avem doua tipuri de date care
												nu se pot concantena. Solutia alternativa ar fi sa folosim type casting, cu dezavantajul ca
												vom face codul mai putin lizibil

										   Exemplu:

										   print("Ana are" + 12 + "ani") -> va returna eroare pentru ca int si string
										   																	nu sunt compatibile la concatenare deoarece caracerul + este
										   																	interpretat ca si adunare pentru int si ca si concatenare pentru string
										   print("Ana are" + string(12) + "ani") -> va merge dar codul va fi mai putin lizibil
										   print(f"Ana are {12} ani") -> va merge si este cea mai buna varianta

Assert = este un keyword care ne ofera posibilitate de a compara doua valori diferite. Returneaza un rezultat boolean care reprezinta
								caracterul adevarat sau fals al comparatiei
				 assertul are urmatoarele componente:
				 - pe prima pozitie valoarea pe care o comparam
				 - pe a doua pozitie valoarea cu care comparam. cele doua valori sunt separate prin operatorul == (operatorul de comparatie)
				 - optional un mesaj care sa fie returnat in cazul in care cele doua valori nu sunt egale. Mesajul de eroare
				 			este separat de a doua valore, cea cu care comparam, prin caracterul virgula

Exemplu:
varsta_pasager = int(input("va rugam introduceti varsta pasagerului "))

try:
		assert(varsta_pasager<=10 or varsta_pasager>=65 or varsta_pasager == 50)
		print("Calculul discountului a fost facut cu succes. Procedam la emiterea biletului")
except:
		print("Nu am putut sa aplicam discountul pentru ca pasagerul nu are varsta corespunzatoare")

= (operator de atribuire)
== (operator de comparatie)

Input statement = Este o functie prin intermediul careia putem sa cerem informatii de la un utilizator
									In mod implicit, informatiile transmise de la tastatura au tipul de date string
"""


variabila_test = "Andrada"
print(variabila_test)
del variabila_test
# print(variabila_test) # del sterge adresa de memorie rezervata pentru acea variabila