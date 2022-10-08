from requests_folder.albums.get_album import get_album_without_market, get_album_with_market


class TestAlbums:
    # @functionaltesting    @positivetesting
    def test_get_album_exists(self):
        response=get_album_without_market('1mc8M9eR9ZIBxqWA2CA4Wo')
        assert response.status_code == 200

    # @functionaltesting    @negativetesting
    def test_get_album_does_not_exist(self):
        response=get_album_without_market('1mc8M9eR9ZIBxqWA2CA4WN')
        assert response.status_code == 404

    # @functionaltesting @negativetesting
    def test_get_album_invalid(self):
        response=get_album_without_market('*mc8M9eR9ZIBxqWA2CA4WN&')
        assert response.status_code == 400

    # @functionaltesting
    def test_get_album_check_album_type(self):
        response = get_album_without_market('1mc8M9eR9ZIBxqWA2CA4Wo')
        assert response.json()['album_type'] == 'album'

    def test_get_album_check_artist_name(self):
        response = get_album_without_market('1mc8M9eR9ZIBxqWA2CA4Wo')
        assert response.json()['artists'][0]['name'] == 'ABBA'

    def test_get_album_check_number_of_markets(self):
        response = get_album_without_market('1mc8M9eR9ZIBxqWA2CA4Wo')
        assert len(response.json()['available_markets']) == 183

    def test_get_album_check_copyright(self):
        response = get_album_without_market('1mc8M9eR9ZIBxqWA2CA4Wo')
        assert "2014 Polar Music International AB" in response.json()['copyrights'][0]['text']

    def test_get_album_check_album_name(self):
        response = get_album_without_market('1mc8M9eR9ZIBxqWA2CA4Wo')
        assert response.json()['name'] == 'Live At Wembley Arena'

    # @functional testing # positive testing
    def test_get_album_filter_by_market_song_available_in_market(self):
        response = get_album_with_market('1mc8M9eR9ZIBxqWA2CA4Wo', "BR")
        assert response.status_code == 200

    # @functional testing # negative testing  # BUG: ar trebui sa nu returneze nimic
                                                    # ar trebui confirmat cu dezvoltatorul ce ar trebui sa se intample in cazul asta
    """
    def test_get_album_filter_by_market_song_not_available_in_market(self):
        response = get_album_with_market('1mc8M9eR9ZIBxqWA2CA4Wo', "SO")
        assert response.status_code == 404
    """
    # @functional testing # negative testing
    def test_get_album_filter_by_market_invalid_market(self):
        response = get_album_with_market('1mc8M9eR9ZIBxqWA2CA4Wo',"XY")
        assert response.status_code == 400
        assert response.json()['error']['message']=='Invalid market code'

"""
alte teste recomandate:
- check release date
- check total_tracks
- check number of items
"""




