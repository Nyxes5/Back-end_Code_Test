from rest_framework.test import APITestCase
from rest_framework import status
from django.test import RequestFactory
from app.models import Person

class PersonAPITest(APITestCase):

    def setUp(self):
        self.factory = RequestFactory()

    @classmethod
    def setUpTestData(cls):
        cls.person1 = Person.objects.create(name='Jef', age=18)
        cls.person2 = Person.objects.create(name='Bert', age=19)
        cls.person3 = Person.objects.create(name='Charlie', age=19)
        cls.person4 = Person.objects.create(name='Jack', age=20)

    def test_get_list(self):
        response = self.client.get('/api/persons')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    
    def test_get_search(self):
        response = self.client.get('/api/persons?search=jef')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], self.person1.name)
        self.assertEqual(response.data[0]['age'], self.person1.age)


    def test_get_search_age(self):
        response = self.client.get('/api/persons?search=19')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    def test_get_search_partial_age(self):
        response = self.client.get('/api/persons?search=1')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)


    def test_get_search_partial_name(self):
        response = self.client.get('/api/persons?search=r')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)


    def test_post(self):
        payload = {
            'name': 'Andy',
            'age': 20
        }
        response = self.client.post('/api/persons', data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['name'], payload['name'])
        self.assertEqual(response.data['age'], payload['age'])

        # Check if it created
        response = self.client.get('/api/persons')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)


    def test_post_duplicate_name(self):
        payload = {
            'name': 'Charlie',
            'age': 21
        }
        response = self.client.post('/api/persons', data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check if it didn't create
        response = self.client.get('/api/persons')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)


    def test_post_below_18(self):
        payload = {
            'name': 'Oscar',
            'age': 15
        }
        response = self.client.post('/api/persons', data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check if it didn't create
        response = self.client.get('/api/persons')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)
