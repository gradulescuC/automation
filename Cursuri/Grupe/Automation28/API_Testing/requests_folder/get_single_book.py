import requests

def get_single_book(bookId):
		response = requests.get(f"https://simple-books-api.glitch.me/books/{bookId}")
		return response