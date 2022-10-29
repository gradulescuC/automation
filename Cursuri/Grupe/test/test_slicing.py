import time
from functools import wraps


def timp_executie(functie_originala):
		@wraps(functie_originala)
		def wrapper(*args,**kargs):
				t1 = time.time()
				result = functie_originala(*args,**kargs)
				t2 = time.time()-t1
				print(f"{functie_originala.__name__} a fost executata in {t2} secunde")
				return result
		return wrapper

@timp_executie
def afisare_informatii(nume, varsta):
		time.sleep(1)
		print(f"Afisare informatii a rulat cu parametrii {nume}, {varsta}")

afisare_informatii("ionel",25)