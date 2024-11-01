from django.test import TestCase
from app.serializers import PersonSerializer

class PersonSerializerTest(TestCase):
    def test_serializer_valid_age(self):
        data = {'name': 'Jef', 'age': '18'}
        serializer = PersonSerializer(data=data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalid_age(self):
        data = {'name': 'Jef', 'age': '17'}
        serializer = PersonSerializer(data=data)
        self.assertFalse(serializer.is_valid())