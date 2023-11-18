from rest_framework import serializers
from .models import Pet


class PetListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pet
        fields = ('id', 'owner', 'name', 'breed', 'gender', 'age', 'size', 'description', 'location', 'status', 'pic')


class PetCreateSerializer(serializers.ModelSerializer):
    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)
    class Meta:
        model = Pet
        exclude = ('owner', 'status')


class PetEditSerializer(serializers.ModelSerializer):
    STATUS_CHOICES = [('available', 'Available'), ('adopted', 'Adopted'), ('pending', 'Pending'), ('withdrawn', 'Withdrawn')]
    GENDER_CHOICES = [('male', 'Male'), ('female', 'Female')]
    status = serializers.ChoiceField(choices=STATUS_CHOICES)
    gender = serializers.ChoiceField(choices=GENDER_CHOICES)
    class Meta:
        model = Pet
        exclude = ('owner',)
