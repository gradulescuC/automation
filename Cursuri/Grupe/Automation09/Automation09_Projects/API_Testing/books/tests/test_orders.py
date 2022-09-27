from books.requests.orders import *
from books.requests.api_clients import *


class TestOrders:

    def setup_method(self):
        self.token = get_token()

    def test_add_order_book_out_of_stock(self):
        r = add_order(self.token,  2, 'Andy')
        assert r.status_code == 404, 'code not ok'
        assert r.json()['error'] == 'This book is not in stock. Try again later.', 'error not ok'

    def test_add_valid_order(self):
        r = add_order(self.token, 1, 'Marin')
        assert r.status_code == 201, 'code not ok'
        assert r.json()['created'] is True, 'order not created'
        #cleanup
        delete_order(self.token, r.json()['orderId'])

    def test_get_orders(self):
        add1 = add_order(self.token, 1, 'Marin')
        add2 = add_order(self.token, 1, 'Marin')
        r = get_orders(self.token)
        assert r.status_code == 200, 'code not ok'
        assert len(r.json()) == 2, 'get orders not working'
        #cleanup
        delete_order(self.token, add1.json()['orderId'])
        delete_order(self.token, add2.json()['orderId'])

    def test_delete_order(self):
        add = add_order(self.token, 1, 'User1')
        r = delete_order(self.token, add.json()['orderId'])
        assert r.status_code == 204, 'code not ok'
        # extra verif
        get_all = get_orders(self.token)
        assert len(get_all.json()) == 0, 'order was not deleted'

    def test_delete_invalid_order_id(self):
        r = delete_order(self.token, '123abc')
        assert r.status_code == 404, 'code not ok'
        assert r.json()['error'] == 'No order with id 123abc.', 'error no ok'

    def test_get_order(self):
        id = add_order(self.token, 1, 'Andy').json()['orderId']
        r = get_order(self.token, id)
        assert r.status_code == 200, 'code not ok'
        assert r.json()['id'] == id, 'id not ok'
        assert r.json()['bookId'] == 1, 'book id not ok'
        assert r.json()['customerName'] == 'Andy', 'customerName not ok'
        assert r.json()['quantity'] == 1, 'quantity not ok'
        # cleanup
        delete_order(self.token, id)

    def test_get_invalid_order_id(self):
        r = get_order(self.token, '123abc')
        assert r.status_code == 404, 'code not ok'
        assert r.json()['error'] == 'No order with id 123abc.', 'error no ok'

    def test_get_order_invalid_token(self):
        r = get_order('123', '123abc')
        assert r.status_code == 401, 'code not ok'
        assert r.json()['error'] == 'Invalid bearer token.', 'error no ok'

    def test_patch_invalid_order_id(self):
        r = edit_order(self.token, '123abc', 'Andy2')
        assert r.status_code == 404, 'code not ok'
        assert r.json()['error'] == 'No order with id 123abc.', 'error no ok'

    def test_patch_invalid_order_id(self):
        id = add_order(self.token, 1, 'Andy').json()['orderId']
        r = edit_order(self.token, id, 'Andy2')
        assert r.status_code == 204, 'code not ok'
        get = get_order(self.token, id)
        assert get.json()['customerName'] == 'Andy2', 'update name not working'
        # cleanup
        delete_order(self.token, id)