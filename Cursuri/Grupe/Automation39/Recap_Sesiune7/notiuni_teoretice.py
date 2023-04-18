"""

PILONII PROGRAMARII

Exista patru piloni ai programarii:
1. Mostenire  = posibilitatea de a transmite atributele si metodele definite
								intr-o clasa catre o alta clasa
								avantajul de a folosi mostenirea este acela ca economisim cod prin a reutiliza
								informatii care deja au fost definite si de asemenea acela de a crea anumite
								legaturi intre clase astfel incat sa construim o logica bine definita

								Cate clase poate sa mosteneasca o alta clasa? Un numar nelimitat

2. Encapsulare = posiblitatea de a restrictiona accesul la anumite atribute si metode dintr-o clasa astfel incat
								sa protejam datele si sa aratam utilizatorului doar informatiile de care are nevoie
								Encapsularea se poate obtine pe baza a ceea ce se numeste modificatori de acces
								Exista trei modificatori de acces principali:
								- public - atributul sau metoda sunt accesibile oriunde
								- private - atributul sau metoda sunt accesibile doar in interiorul clasei in care au fost definite prin intermediul self
								- protected - atributul sau metoda sunt vizibile oriunde dar nu sunt returnate ca sugestii
											ATENTIE!!! In java (si posibil alte limbaje de programare) protected inseamna ca atributul
																	sau metoda sunt accesibile doar in pachetul in care au fost definite
3. Polimorfism = posibilitatea de a crea o functie care sa poata sa fie apelata sub mai multe forme
									Se poate implementa si prin crearea unor functii cu un numar indefinit de parametri
									prin functii cu parametrii ce au valori implicite sau prin crearea
									a doua functii cu acelasi nume, dar create in clase diferite

									ATENIE!!! In java (si posibil si alte limbaje de programare)
									polimorfismul se poate implementa si prin definirea a doua functii cu acelasi nume
									dar cu numar diferit de parametri / cu parametri care au tip de date diferit.

									De asemenea, in java se pot defini mai multi constructori, fiecare cu propria
									definitie, la fel ca si la functii.

									Atunci cand definim doua functii cu nume identic sau doi constructori in aceeasi clasa
									vorbim de conceptul de overloading (method overloading / constructor overloading)

4. Abstractizare = un proces prin care ascundem din fata utilizatorului unele date ale unei functii
									si respectiv o modalitate prin care putem sa fortam clasele copil
									sa implementeze un comportament specific pentru o anumita metoda
"""

