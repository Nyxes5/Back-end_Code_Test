from rest_framework.test import APITestCase
from rest_framework import status
from apps.person.models import Person


class PersonAPITest(APITestCase):
    @classmethod
    def setUpTestData(cls):
        """
        Creating test data
        """
        cls.person1 = Person.objects.create(name="Jef", age=18)
        cls.person2 = Person.objects.create(name="Bert", age=19)
        cls.person3 = Person.objects.create(name="Charlie", age=19)
        cls.person4 = Person.objects.create(name="Jack", age=20)

    def test_get_list(self):
        """
        Test GET Request
        """
        response = self.client.get("/api/person")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 4)

    def test_get_search(self):
        """
        Test GET Search Request on name
        """
        response = self.client.get("/api/person?search=jef")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]["name"], self.person1.name)
        self.assertEqual(response.data[0]["age"], self.person1.age)

    def test_get_search_age(self):
        """
        Test GET Search Request on age
        """
        response = self.client.get("/api/person?search=19")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_get_search_partial_age(self):
        """
        Test GET Search Request on a number that's included in age
        """
        response = self.client.get("/api/person?search=1")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_get_search_partial_name(self):
        """
        Test GET Search Request on a letter that's included in name
        """
        response = self.client.get("/api/person?search=r")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)

    def test_post(self):
        """
        Test POST Request
        """
        payload = {"name": "Andy", "age": 20}
        response = self.client.post("/api/person", data=payload)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data["name"], payload["name"])
        self.assertEqual(response.data["age"], payload["age"])

        # Check if it created
        response = self.client.get("/api/person")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_post_duplicate_name(self):
        """
        Test POST Request fail on duplicate name
        """
        payload = {"name": "Charlie", "age": 21}
        response = self.client.post("/api/person", data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check if it didn't create
        response = self.client.get("/api/person")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)

    def test_post_below_18(self):
        """
        Test POST Request fail on below 18 years old
        """
        payload = {"name": "Oscar", "age": 15}
        response = self.client.post("/api/person", data=payload)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        # Check if it didn't create
        response = self.client.get("/api/person")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)