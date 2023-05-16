import json
from django.test import TestCase, Client
from bookuser.models import BookUser

class BookUserTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        # Create some BookUser objects for testing
        BookUser.objects.create(cusAccount='account1', create_time='2023-01-01', status='Active', reserve1='1234')
        BookUser.objects.create(cusAccount='account2', create_time='2023-01-02', status='Inactive', reserve1='5678')

    def test_list(self):
        url = '/list/'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        data = response.json()['data']
        self.assertEqual(len(data), 2)
        # Perform additional assertions based on the expected response from the list API

    def test_info(self):
        book_user = BookUser.objects.get(cusAccount='account1')
        url = f'/info/?id={book_user.id}'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        data = response.json()['data']
        self.assertEqual(data['cusAccount'], 'account1')
        # Perform additional assertions based on the expected response from the info API

    def test_delete(self):
        book_user = BookUser.objects.get(cusAccount='account1')
        url = f'/delete/?id={book_user.id}'
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)
        # Perform additional assertions based on the expected response from the delete API

    def test_save(self):
        url = '/save/'
        data = {
            'cusAccount': 'account3',
            'status': 'Active',
            'reserve1': '9012'
            # Add other required fields
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)
        # Perform additional assertions based on the expected response from the save API

    def test_update(self):
        book_user = BookUser.objects.get(cusAccount='account1')
        url = f'/update/'
        data = {
            'id': book_user.id,
            'cusAccount': 'updated_account1',
            # Add other fields to update
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)
        # Perform additional assertions based on the expected response from the update API

    def test_page(self):
        url = '/page/'
        data = {
            'pageNum': 1,
            'pageSize': 10,
            'search': ''  # Add a search query if needed
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = response.json()['data']
        total = response.json()['total']
        self.assertEqual(len(data), 2)
        self.assertEqual(total, 2)
