from django.http import JsonResponse, Http404
from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from rest_framework.generics import GenericAPIView
from .serializers import PersonSerializer
from .services import (
    get_or_cache_persons,
    clear_persons_cache,
    get_or_cache_person_by_name,
)


class PersonViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    serializer_class = PersonSerializer
    filter_backends = (SearchFilter,)
    search_fields = (
        "name",
        "age",
    )
    CACHE_KEY = "person"

    def get_queryset(self):
        return get_or_cache_persons()

    def perform_create(self, serializer):
        """
        After a new Person is created, clear the cache
        """
        serializer.save()
        clear_persons_cache()


class PersonByNameView(GenericAPIView):

    serializer_class = PersonSerializer

    def get(self, request, *args, **kwargs):
        """
        Get a person by exact (case insensitive) name or raise 404 Not Found
        """
        name = kwargs.get("name")
        person = get_or_cache_person_by_name(name)
        if person:
            serializer = PersonSerializer(person)
            return JsonResponse(serializer.data)
        raise Http404
