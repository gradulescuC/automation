from functools import wraps

def upper_case_characters(functie_apelata):
		@wraps(functie_apelata)
		def wrapper(text):
				rezultat = functie_apelata(text)
				print(f"Am executat functia in interiorul wrapperului")
				rez = rezultat.upper()
				print(f"Textul meu este: {rez}")
				return rez
		return wrapper

@upper_case_characters
def print_text_upper(text):
		print(f"Am terminat executia")
		return text

print_text_upper("test")
