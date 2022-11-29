# from curs_05.curs_05_fisier_initial import accesare_elemente_dictionar, calcul_suma_numere
from curs_05.curs_05_fisier_initial import *
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

print(f"Suma numerelor este: {calcul_suma_numere(2,6)}")
accesare_elemente_dictionar(**apa_plata)
print(f"\nSuma numerelor este: {calcul_suma_numere(7,8)}")
