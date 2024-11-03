from .models import Person

def get_persons():
    return Person.objects.all().order_by("name")

def get_person_by_name(name):
    try:
        return Person.objects.get(name__iexact=name) # Case insensitive match
    except Person.DoesNotExist:
        return None