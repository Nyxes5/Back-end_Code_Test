from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from .serializers import PersonSerializer
from .services import get_or_cache_persons, clear_persons_cache


class PersonViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = PersonSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("name", "age",)
    CACHE_KEY = 'person'
    
    def get_queryset(self):
        return get_or_cache_persons()
    
    def perform_create(self, serializer):
        """
        After a new Person is created, clear the cache
        """
        serializer.save()
        clear_persons_cache()