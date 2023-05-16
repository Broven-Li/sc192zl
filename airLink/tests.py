import json
from django.test import TestCase, Client
from airLink.models import AirLink
from airLink.views import requestAirApi


class AirLinkTestCase(TestCase):
    def setUp(self):
        # Set up the test database with some initial data
        AirLink.objects.create(link="http://example.com", name="Link 1", username="User1")
        AirLink.objects.create(link="http://example.org", name="Link 2", username="User2")

    def test_list(self):
        # Test the list view
        client = Client()
        response = client.get('/list/')
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], '查询成功')
        self.assertEqual(len(data['data']), 2)

    def test_info(self):
        # Test the info view
        client = Client()
        link_id = 1  # Assuming there is a link with ID 1 in the database
        response = client.get(f'/info/?id={link_id}')
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], '查询成功')
        self.assertEqual(data['data']['id'], link_id)

    def test_delete(self):
        client = Client()
        link_id = 1  # Assuming there is a link with ID 1 in the database
        response = client.get(f'/delete/?id={link_id}')
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], '删除成功')

    def test_save(self):
        # Test the save view
        client = Client()
        data = {
            'link': 'http://example.com',
            'name': 'New Link',
            'username': 'New User'
        }
        response = client.post('/save/', data=json.dumps(data), content_type='application/json')
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], '新增成功')

    def test_update(self):
        # Test the update view
        client = Client()
        link_id = 1  # Assuming there is a link with ID 1 in the database
        data = {
            'id': link_id,
            'link': 'http://example.com',
            'name': 'Updated Link',
            'username': 'Updated User'
        }
        response = client.post('/update/', data=json.dumps(data), content_type='application/json')
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], '修改成功')

    def test_page(self):
        # Test the page view
        client = Client()
        data = {
            'pageNum': 1,
            'pageSize': 10,
            'search': ''
        }
        response = client.post('/page/', data=json.dumps(data), content_type='application/json')
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], '查询成功')
        self.assertEqual(data['total'], 2)
        self.assertEqual(len(data['data']), 2)

    def test_airList(self):
        # Test the airList view
        client = Client()
        data = {
            'pageNum': 1,
            'pageSize': 10
        }
        response = client.post('/airList/', data=json.dumps(data), content_type='application/json')
        data = json.loads(response.content)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['message'], '查询成功')
        self.assertEqual(len(data['data']), 0) # Assuming there are no results for the given parameters

    def test_requestAirApi(self):
        # Test the requestAirApi function
        data = {
            'pageNum': 1,
            'pageSize': 10
        }
        result = requestAirApi('/flight/page1', json.dumps(data))
        self.assertIsInstance(result, list)