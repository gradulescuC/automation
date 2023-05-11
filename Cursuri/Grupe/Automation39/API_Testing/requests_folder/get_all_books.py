import requests

def get_all_books(type="",limit=""):
		# host + extensie = endpoint
		# endpoint = componenta prin intermediul careia se preia informatia de la client si se trimite catre server
		if type=="" and limit == "":
				response = requests.get('https://simple-books-api.glitch.me/books')
		elif type != "" and limit =="":
				response = requests.get(f'https://simple-books-api.glitch.me/books?type={type}')
		elif type == "" and limit != "":
				response = requests.get(f'https://simple-books-api.glitch.me/books?limit={limit}')
		else:
				response = requests.get(f'https://simple-books-api.glitch.me/books?type={type}&limit={limit}')
		return response



# Exemplu apelare functie
# type= fiction sau type = non-fiction
# limit = 1 sau limit = 20
# limit = un parametru de filtrare care defineste conform documentatiei cate rezultate trebuie sa fie returnate
# get_all_books("fiction",1)
# get_all_books("non-fiction",20)

# Apelarea de mai jos ar returna eroare pentru ca functia e definita cu parametri si noi am apelat-o fara parametri
# get_all_books()


