class Competitii_sportive():
		tip_competitie = None
		categorie_varsta = None
		numar_participanti = None
		obiectiv_distanta = None
		dificultate_competitie = None
		premii = {}
		sponsor_oficial = None

		def __init__(self, tip_competitie,plan_localizare,obiectiv_distanta):
				self.tip_competitie = tip_competitie
				self.plan_localizare = plan_localizare
				self.obiectiv_distanta = obiectiv_distanta

		def premiere_participanti(self,locul_intai,locul_doi,locul_trei):
				self.premii["locul_intai"] = locul_intai
				self.premii["locul_doi"] = locul_doi
				self.premii["locul_trei"] = locul_trei

		def afisare_rezultate(self):
				for key,values in self.premii.items():
						print(f"{key} : {values}")

class Maraton(Competitii_sportive):
		pregatire_competitie = None
		plan_localizare = None
		nr_checkpoint = None

		def checkpoint(self):
				if self.nr_checkpoint <4:
						self.nr_checkpoint+=1

maraton = Maraton("maraton","judetean","42")
maraton.pregatire_competitie = "plan alergare"
maraton.premiere_participanti("Ionut Florescu","Ramona Vascul","Catalin Stefan")
maraton.afisare_rezultate()
