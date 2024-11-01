from .models import Person

def get_persons():
    return Person.objects.all().order_by("name")