from django.core.cache import cache
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.response import Response
from .models import Person
from .serializers import PersonSerializer


class PersonViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = PersonSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("name", "age",)
    CACHE_KEY = 'persons'
    
    def get_queryset(self):
        """
        Used for caching and querying the database if it isn't in the cache
        """
        result = cache.get(self.CACHE_KEY, None)
        if not result:
            print('Fetching persons from database and setting cache') # This is for development purposes only
            result = Person.objects.all().order_by("name")
            cache.set(self.CACHE_KEY, result, 60)
        return result
    
    def perform_create(self, serializer):
        """
        After a new Person is created, clear the cache
        """
        serializer.save()
        print('Deleting persons from cache') # This is for development purposes only
        cache.delete(self.CACHE_KEY)