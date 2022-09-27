from books.requests.books import get_books, get_book


class TestBooks:

    # test initial - smoke testing (tip de testare facut la inceput pentru a verifica ca sistemul este suficient de stabil sa suporte procesul de testare)

    # Test 1: Check the status of the get book method
    def test_get_books_200(self):
        response = get_books()
        assert response.status_code == 200, 'status code is not ok'

    # 1. testare functionala = tip de testare facut pentru a verifica faptul ca aplicatia isi indeplineste functiile

    # 1.a. testare pozitiva (positive testing) = tip de testare in care verificam ca sistemul accepta inputurile pe care ar trebui sa le accepte

    # Test 2: Verifica requestul de get books fara niciun fel de filtrare
    def test_get_all_books(self):
        r = get_books()
        assert len(r.json()) >0, 'book total is wrong'

    # Test 3: Verifica requestul de get books cu filtrare pe limita - equivalence partitioning - clasa de echivalenta valida
    def test_get_all_books_limit(self):
        r = get_books(limit=3)
        assert len(r.json()) == 3, 'limit is not working'

    # Test 3.1: Verifica requestul de get books cu filtrare pe limita - boundary value analysis - limita inferioara

    def test_get_all_books_limit_limita_inferioara_boundary(self):
        r = get_books(limit=0)
        assert len(r.json()) == 0, 'limit is not working'

    # Test 3.2: Verifica requestul de get books cu filtrare pe limita - boundary value analysis - limita superioara

    def test_get_all_books_limit_limita_superioara_boundary(self):
        # preconditions: pentru testul asta trebuie sa avem cel putin 20 de carti in sistem
        r = get_books(limit=20)
        assert len(r.json()) == 20, 'limit is not working'

    # Test 3.3: Verifica requestul de get books cu filtrare pe limita - equivalence partitioning - clasa de echivalenta invalida

    def test_get_all_books_limit_invalid_superior(self):
        r = get_books(limit=30)
        assert r.json()["error"] == "Invalid value for query parameter 'limit'. Cannot be greater than 20.", 'limit is not working'

    # Test 3.4: Verifica requestul de get books cu filtrare pe limita - equivalence partitioning - clasa de echivalenta invalida
    def test_get_all_books_limit_invalid_inferior(self):
        r = get_books(limit=-30)
        assert r.json()["error"] == "Invalid value for query parameter 'limit'. Must be greater than 0."

    # Test 4: Verifica requestul de get books cu filtrare pe type fiction
    def test_get_all_books_type_fiction(self):
        r = get_books(book_type='fiction')
        # assert 1 < len(r.json()) <= 4, 'type fiction is not working'
        assert len(r.json()) in range(1,5),'type fiction is not working'

    # Test 5: Verifica requestul de get books cu filtrare pe type non-fiction

    def test_get_all_books_type_non_fiction(self):
        r = get_books(book_type='non-fiction')
        assert len(r.json()) == 2, 'type non-fiction is not working'

    # 1.b. testare negativa (negative testing) = tip de testare in care verificam comportamentul sistemului atunci cand primeste inputuri pe care nu ar trebui sa le accepte
                                                 # testam in primul rand ca inputurile sunt respinse si in al doilea rand ca mesajul de eroare si codurile de raspuns sunt cele asteptate

    # Test 6: Verifica requestul de get books atunci cand punem filtrare invalida dupa type
    def test_get_books_invalid_type(self):
        r = get_books(book_type='abc')
        assert r.status_code == 400, 'status code is not ok'
        assert r.json()['error'] == "Invalid value for query parameter 'type'. Must be one of: fiction, non-fiction.", 'Wrong error'

    # Test 7: Verifica requestul de get books atunci cand punem filtrare valida dupa type SI limita

    def test_get_all_books_type_and_limit(self):
        r = get_books(book_type='fiction', limit=2)
        assert len(r.json()) == 2, 'limit is not working'
        assert r.json()[0]['type'] == 'fiction', 'type filter not working'
        assert r.json()[0]['id'] == 1, 'id not ok'
        assert r.json()[0]["name"] == "The Russian", "book name is not ok"
        assert r.json()[1]['type'] == 'fiction', 'type filter not working'
        assert r.json()[1]['id'] == 3, 'id not ok'
        assert r.json()[1]["name"] == "The Vanishing Half", "book name is not ok"

  # Test 8: Verifica requestul de get book
    def test_get_book(self):
        r = get_book(1)
        expected = {
            "id": 1,
            "name": "The Russian",
            "author": "James Patterson and James O. Born",
            "isbn": "1780899475",
            "type": "fiction",
            "price": 12.98,
            "current-stock": 12,
            "available": True
        }
        assert r.status_code == 200, 'status code not ok'
        assert r.json() == expected, 'book data not ok'

    # Test 6: Verifica requestul de get books atunci cand punem filtrare invalida dupa id
    def test_get_book_invalid_id(self):
        r = get_book(202)
        assert r.status_code == 404, 'code not ok'
        assert r.json()['error'] == 'No book with id 202', 'invalid id msg is not ok'