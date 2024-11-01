from rest_framework import serializers
from .models  import Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta():
        model = Person
        fields = ('id', 'name', 'age',)
        read_only_fields = ('id',)

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("person has to be older than 18.")
        return value