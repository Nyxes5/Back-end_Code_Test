from rest_framework import mixins, viewsets
from rest_framework.filters import SearchFilter
from .models import Person
from .serializers import PersonSerializer
from .permissions import AdultPermission

class PersonViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet,
):
    permission_classes = [AdultPermission,]
    queryset = (
        Person.objects.all().order_by("name")
    )
    serializer_class = PersonSerializer
    filter_backends = (SearchFilter,)
    search_fields = ("name", "age",)