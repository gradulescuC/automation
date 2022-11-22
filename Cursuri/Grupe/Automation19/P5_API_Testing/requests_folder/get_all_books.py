import requests

def get_all_books(type=""):
		if type=="":
				response = requests.get("https://simple-books-api.glitch.me/books")
		else:
				response = requests.get(f"https://simple-books-api.glitch.me/books?type={type}")
		return response