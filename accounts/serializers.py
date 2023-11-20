from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework import serializers
from .models import User, PetShelter, PetSeeker
from django.contrib.auth.password_validation import validate_password
from django.db import models

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)

        # Add custom claims if needed
        # token['custom_claim'] = user.custom_claim

        return token

class PetShelterSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetShelter
        fields = ('shelter_name', 'location', 'description','pic','phone_num','website')

class PetSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetSeeker
        fields = ('location', 'bio','pic','pref','phone_num')

class UserSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def validate_password2(self, value):
        # Check if password and password2 match
        if self.initial_data['password'] != value:
            raise serializers.ValidationError("Passwords do not match.")
        return value


    def create(self, validated_data):
        # Remove the password2 field before creating the user
        validated_data.pop('password2', None)
        user = User.objects.create(email=validated_data['email'], username=validated_data['username'],is_pet_shelter=validated_data['is_pet_shelter'], is_pet_seeker=validated_data['is_pet_seeker'])
        user.set_password(validated_data['password'])
        user.save()
        return user

        """ def create(self, validated_data):
        user = User.objects.create(email=validated_data['email'],username=validated_data['username'], is_pet_shelter=True)
        user.set_password(validated_data['password'])
        user.save()
        return user"""
        #fields = ('id', 'username', 'email', 'password', 'is_pet_shelter', 'is_pet_seeker')
        #fields = ('id', 'username', 'email', 'password', 'is_pet_shelter', 'is_pet_seeker', 'pet_shelter', 'pet_seeker')  # Add other fields as needed
