from rest_framework import mixins, viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from .models import Person
from .serializers import PersonSerializer

class PersonViewSet(
    mixins.RetrieveModelMixin,
    mixins.CreateModelMixin,
    viewsets.GenericViewSet,
):
    queryset = (
        Person.objects.all().order_by("name")
    )
    serializer_class = PersonSerializer
    filter_backends = (
        OrderingFilter,
        SearchFilter,
    )
    filter_fields = ("name",)
    search_fields = ("name",)
    ordering_fields = ("name",)