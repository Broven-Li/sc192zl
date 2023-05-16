from django.test import TestCase, RequestFactory
from django.urls import reverse
from datetime import datetime
from book.models import Book
from bookuser.models import BookUser
from . import views

class BookTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.book = Book.objects.create(booAAddress='Address 1', create_time=datetime.now())

    def test_list(self):
        url = reverse('list')
        request = self.factory.get(url)
        response = views.list(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.json())
        self.assertIn('data', response.json())

    def test_info(self):
        url = reverse('info')
        request = self.factory.get(url, {'id': self.book.id})
        response = views.info(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.json())
        self.assertIn('data', response.json())

    def test_delete(self):
        url = reverse('delete')
        request = self.factory.get(url, {'id': self.book.id})
        response = views.delete(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.json())
        self.assertEqual(response.json()['success'], True)

    def test_save(self):
        url = reverse('save')
        request_data = {
            'booAAddress': 'New Address',
            'status': 'Active',
            'reserve1': 'Reserve 1',
            # Include other required fields
            'persions': []
        }
        request = self.factory.post(url, data=request_data, content_type='application/json')
        response = views.save(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.json())
        self.assertEqual(response.json()['success'], True)

    def test_update(self):
        url = reverse('update')
        request_data = {
            'id': self.book.id,
            'booAAddress': 'Updated Address',
            # Include other fields to update
        }
        request = self.factory.post(url, data=request_data, content_type='application/json')
        response = views.update(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.json())
        self.assertEqual(response.json()['success'], True)

    def test_page(self):
        url = reverse('page')
        request_data = {
            'pageNum': 1,
            'pageSize': 10,
            'search': '',
            'air': '',
        }
        request = self.factory.post(url, data=request_data, content_type='application/json')
        response = views.page(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn('success', response.json())
        self.assertIn('data', response.json())
        self.assertIn('total', response.json())