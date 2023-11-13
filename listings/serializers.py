from rest_framework import serializers
from .models import Pet


class PetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'owner', 'name', 'breed', 'gender', 'age', 'size', 'description', 'location', 'status')


class PetCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        exclude = ('owner',)

