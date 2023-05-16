import json
from django.test import TestCase, Client
from django.urls import reverse
from custom.models import Custom

class CustomViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list(self):
        Custom.objects.create(cusAccount='account1', create_time='2022-01-01', status='active')
        Custom.objects.create(cusAccount='account2', create_time='2022-02-01', status='inactive')

        url = reverse('list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        data = response.json()['data']
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['cusAccount'], 'account1')
        self.assertEqual(data[0]['create_time'], '2022-01-01')
        self.assertEqual(data[0]['status'], 'active')
        # Perform additional assertions based on the expected response from the list API

    def test_info(self):
        custom = Custom.objects.create(cusAccount='account1', create_time='2022-01-01', status='active')

        url = reverse('/api/custom/info')
        data = {'id': custom.id}
        response = self.client.get(url, data=data)

        self.assertEqual(response.status_code, 200)
        data = response.json()['data']
        self.assertEqual(data['cusAccount'], 'account1')
        self.assertEqual(data['create_time'], '2022-01-01')
        self.assertEqual(data['status'], 'active')
        # Perform additional assertions based on the expected response from the info API

    def test_delete(self):
        custom = Custom.objects.create(cusAccount='account1', create_time='2022-01-01', status='active')

        url = reverse('delete')
        data = {'id': custom.id}
        response = self.client.get(url, data=data)

        self.assertEqual(response.status_code, 200)
        # Perform additional assertions based on the expected response from the delete API

    def test_save(self):
        url = reverse('save')
        data = {
            'cusAccount': 'account1',
            'create_time': '2022-01-01',
            'status': 'active'
            # Add other required fields
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        # Perform additional assertions based on the expected response from the save API

    def test_update(self):
        custom = Custom.objects.create(cusAccount='account1', create_time='2022-01-01', status='active')

        url = reverse('update')
        data = {
            'id': custom.id,
            'cusAccount': 'updated_account1',
            'create_time': '2022-02-01',
            'status': 'inactive'
            # Add other fields to update
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        # Perform additional assertions based on the expected response from the update API

    def test_page(self):
        Custom.objects.create(cusAccount='account1', create_time='2022-01-01', status='active')
        Custom.objects.create(cusAccount='account2', create_time='2022-02-01', status='inactive')
        # Add more data for pagination testing

        url = reverse('page')
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

    def test_login(self):
        Custom.objects.create(cusAccount='account1', cusPwd='password', cusName='John Doe', reserve1='1234')

        url = reverse('login')
        data = {
            'cusAccount': 'account1',
            'cusPwd': 'password'
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['success'], True)