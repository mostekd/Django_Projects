from rest_framework import serializers
from .models import UserSubmission, City

class CitySerializer(serializers.ModelSerializer):
    voivodeship = serializers.StringRelatedField()

    class Meta:
        model = City
        fields = ['id', 'name', 'voivodeship']

class UserSubmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserSubmission
        fields = ['id', 'name', 'email', 'birthdate', 'city']
