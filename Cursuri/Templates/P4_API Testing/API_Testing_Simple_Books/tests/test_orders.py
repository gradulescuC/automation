from requests_folder.request_orders import submit_order, update_an_order


class TestOrders:
    def test_update_order(self):
        order_id = submit_order().json()['orderId']
        expected_customerName = "John"
        update_order = update_an_order(order_id)
        assert update_order.json()['customerName'] == expected_customerName, 'first order is not ok'