from contact_list.requests.contacts import *
from contact_list.requests.users import get_token


class TestContacts:

    json = {
        "firstName": "John",
        "lastName": "Doe",
        "birthdate": "1970-01-01",
        "email": "jdoe@fake.com",
        "phone": "8005555555",
        "street1": "1 Main St.",
        "street2": "Apartment A",
        "city": "Anytown",
        "stateProvince": "KS",
        "postalCode": "12345",
        "country": "USA"
    }

    def setup_method(self):
        self.token = get_token()

    def test_get_contacts_200(self):
        r = get_contacts(self.token)
        assert r.status_code == 200, 'status code is not ok'

    def test_get_contact_200(self):
        r = get_contact(self.token, '626d20160c4d140015165721')
        assert r.status_code == 200, 'status code is not ok'

    def test_get_contact(self):
        id = add_contact(self.token, self.json).json()['_id']
        r = get_contact(self.token, id)
        assert r.json()['firstName'] == 'John', 'firstName is not ok'

    def test_add_contact_201(self):
        r = add_contact(self.token, self.json)
        assert r.status_code == 201, 'status code is not ok'

    def test_add_contact(self):
        r = add_contact(self.token, self.json)
        assert r.json()['firstName'] == 'John', 'firstName is not ok'


    def test_update_contact(self):
        json = {
            "firstName": "NewName",
            "country": "NewCountry"
        }
        r = update_contact(self.token, '626d20160c4d140015165721', json)
        assert r.json()['firstName'] == 'NewName', 'firstName is not ok'
        assert r.json()['country'] == 'NewCountry', 'firstName is not ok'

    def test_delete_contact_204(self):
        total_before = len(get_contacts(self.token).json())
        id = add_contact(self.token, self.json).json()['_id']

        r = delete_contact(self.token, id)
        assert r.status_code == 200, 'status code is not ok'
        assert r.text == 'Contact deleted', 'delete msg is not ok'

        total_after = len(get_contacts(self.token).json())
        assert total_before == total_after, 'contact was not deletec'