"""

Exista patru piloni ai programarii:
1. mostenire = o modalitate prin care putem transmite atribute si metode definite intr-o clasa parinte,
								astfel incat ele sa poata fi accesibile si dintr-o clasa copil
								mostenirea se poate implementa prin mentionarea numelui clasei parinte intre paranteze rotunte
								o clasa copil poate sa mosteneasca oricate clase parinte
2. abstractizare = o modalitate prin care putem obliga clasele care mostenesc o clasa abstracta
										sa defineasca un anumit comportament
										exista doua metode de abstractizare:
										a) toate metodele dintr-o clasa sunt abstracte - clasa se va numi interfata
										b) doar o parte din metodele dintr-o clasa sunt abstracte - clasa se va numi clasa abstracta
										Daca definim o clasa copil care mostenste o clasa abstracta / interfata
														si nu implementam metodele abstracte, atunci vom primi o eroare
3. polimorfism = o modalitate prin care putem implementa mai multe functii cu acelasi nume dar comportament diferit
										exista mai multe modalitati de implementare a polimorfismului:
										a) polimorfism prin implementarea aceleiasi metode in doua clase diferite
										b) polimorfism prin reimplementarea metodei din clasa parinte
										c) polimorfism prin definirea unei functii sau metode cu parametri impliciti
										d) polimorfism prin definire unei functii sau metode cu *args
4. encapsulare = o modalitate prin care putem sa restrictionam accesul la anumite atribute sau metode
									exista trei tipuri de acces:
									- public = putem avea acces la atributele si metodele din clasa oriunde in program
									- private = putem avea acces la atributele si metodele clasei doar in interiorul clasei (self)
									- protected = putem avea acces la atributele si metodele clasei doar in acelasi pachet in care se afla clasa
"""