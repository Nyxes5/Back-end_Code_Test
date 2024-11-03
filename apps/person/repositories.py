from .models import Person

def get_persons():
    """
    Get all persons
    """
    return Person.objects.all().order_by("name")

def get_person_by_name(name):
    """
    Get person by case insensitive name
    """
    try:
        return Person.objects.get(name__iexact=name)
    except Person.DoesNotExist:
        return None