from rest_framework import serializers
from .models import PetShelter, Pet


class ShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetShelter
        fields = '__all__'


class PetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = '__all__'
