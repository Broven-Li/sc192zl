import json
from django.test import TestCase, Client
from django.urls import reverse
from .models import PayerLink

class PayerLinkViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_list(self):
        PayerLink.objects.create(link='http://example.com/link1', name='Link 1', username='user1')
        PayerLink.objects.create(link='http://example.com/link2', name='Link 2', username='user2')

        url = reverse('list')
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        data = response.json()['data']
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['link'], 'http://example.com/link1')
        self.assertEqual(data[0]['name'], 'Link 1')
        self.assertEqual(data[0]['username'], 'user1')
        self.assertEqual(data[1]['link'], 'http://example.com/link2')
        self.assertEqual(data[1]['name'], 'Link 2')
        self.assertEqual(data[1]['username'], 'user2')

    def test_info(self):
        payer_link = PayerLink.objects.create(link='http://example.com/link1', name='Link 1', username='user1')

        url = reverse('info')
        response = self.client.get(url, {'id': payer_link.id})

        self.assertEqual(response.status_code, 200)
        data = response.json()['data']
        self.assertEqual(data['link'], 'http://example.com/link1')
        self.assertEqual(data['name'], 'Link 1')
        self.assertEqual(data['username'], 'user1')

    def test_delete(self):
        payer_link = PayerLink.objects.create(link='http://example.com/link1', name='Link 1', username='user1')

        url = reverse('delete')
        response = self.client.get(url, {'id': payer_link.id})

        self.assertEqual(response.status_code, 200)
        self.assertEqual(PayerLink.objects.filter(id=payer_link.id).count(), 0)

    def test_save(self):
        url = reverse('save')
        data = {
            'link': 'http://example.com/link1',
            'name': 'Link 1',
            'username': 'user1'
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        saved_link = PayerLink.objects.last()
        self.assertEqual(saved_link.link, 'http://example.com/link1')
        self.assertEqual(saved_link.name, 'Link 1')
        self.assertEqual(saved_link.username, 'user1')

    def test_update(self):
        payer_link = PayerLink.objects.create(link='http://example.com/link1', name='Link 1', username='user1')

        url = reverse('update')
        data = {
            'id': payer_link.id,
            'link': 'http://example.com/link2',
            'name': 'Link 2',
            'username': 'user2'
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        updated_link = PayerLink.objects.get(id=payer_link.id)
        self.assertEqual(updated_link.link, 'http://example.com/link2')
        self.assertEqual(updated_link.name, 'Link 2')
        self.assertEqual(updated_link.username, 'user2')

    def test_page(self):
        PayerLink.objects.create(link='http://example.com/link1', name='Link 1', username='user1')
        PayerLink.objects.create(link='http://example.com/link2', name='Link 2', username='user2')
        PayerLink.objects.create(link='http://example.com/link3', name='Link 3', username='user3')
        PayerLink.objects.create(link='http://example.com/link4', name='Link 4', username='user4')

        url = reverse('page')
        data = {
            'pageNum': 1,
            'pageSize': 2,
            'search': 'Link'
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        data = response.json()['data']
        self.assertEqual(len(data), 2)
        self.assertEqual(data[0]['link'], 'http://example.com/link1')
        self.assertEqual(data[0]['name'], 'Link 1')
        self.assertEqual(data[0]['username'], 'user1')
        self.assertEqual(data[1]['link'], 'http://example.com/link2')
        self.assertEqual(data[1]['name'], 'Link 2')
        self.assertEqual(data[1]['username'], 'user2')

        total = response.json()['total']
        self.assertEqual(total, 4)

    def test_pay(self):
        payer_link = PayerLink.objects.create(link='http://example.com/link1', name='Link 1', username='user1')

        url = reverse('pay')
        data = {
            'name': 'John',
            'reserve2': 'user1',
            'payNum': 100
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)
        # Perform additional assertions based on the expected response from the pay API

    def test_exitMoney(self):
        payer_link = PayerLink.objects.create(link='http://example.com/link1', name='Link 1', username='user1')

        url = reverse('exitMoney')
        data = {
            'name': 'John',
            'reserve2': 'user1',
            'payNum': 100
        }
        response = self.client.post(url, data=json.dumps(data), content_type='application/json')

        self.assertEqual(response.status_code, 200)