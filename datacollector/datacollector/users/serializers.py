from rest_framework import serializers
from .models import UserSubmission, City

class CitySerializer(serializers.ModelSerializer):
    voivodeship = serializers.StringRelatedField()

    class Meta:
        model = City
        fields = ['id', 'name', 'voivodeship']

class UserSubmissionSerializer(serializers.ModelSerializer):
    age = serializers.SerializerMethodField()
    city = CitySerializer(read_only=True)
    city_id = serializers.PrimaryKeyRelatedField(
        queryset=City.objects.all(), write_only=True, source='city'
    )

    class Meta:
        model = UserSubmission
        fields = ['id', 'name', 'email', 'birthdate', 'age', 'city', 'city_id']

    def get_age(self, obj):
        return obj.age()