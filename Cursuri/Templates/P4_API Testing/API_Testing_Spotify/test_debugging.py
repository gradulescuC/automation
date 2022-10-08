from requests_folder.albums.get_album import get_album_without_market, get_album_with_market
response = get_album_without_market('1mc8M9eR9ZIBxqWA2CA4Wo')
print(response.json())