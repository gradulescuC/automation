from requests_folder.albums.get_album import get_album

class TestAlbums:


    # @functionaltesting    @positivetesting
    def test_get_album_exists(self):
        response=get_album('1mc8M9eR9ZIBxqWA2CA4Wo')
        assert response.status_code == 200

    # @functionaltesting    @negativetesting
    def test_get_album_does_not_exist(self):
        response=get_album('1mc8M9eR9ZIBxqWA2CA4WN')
        assert response.status_code == 404

# @functionaltesting    @negativetesting
    def test_get_album_invalid(self):
        response=get_album('*mc8M9eR9ZIBxqWA2CA4WN&')
        assert response.status_code == 400