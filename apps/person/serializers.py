from rest_framework import serializers
from .models  import Person


class PersonSerializer(serializers.ModelSerializer):
    class Meta():
        model = Person
        fields = ('id', 'name', 'age',)
        read_only_fields = ('id',)

    def validate_age(self, value):
        """
        A person has to be 18+ years old
        """
        if value < 18:
            raise serializers.ValidationError("person has to be older than 18.")
        return value
    
    def validate_name(self, value):
        """
        A person can't have the same name in case insensitive
        """
        if Person.objects.filter(name__iexact=value).first():
            raise serializers.ValidationError("person's name has to be unique.")
        return value
