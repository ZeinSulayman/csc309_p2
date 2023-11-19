from rest_framework.serializers import ModelSerializer, DateTimeField, ListField, \
    PrimaryKeyRelatedField, HyperlinkedRelatedField
from .models import User
#PetSeeker, PetShelter,

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
        fields = ('shelter_name', 'location', 'description','pic')

class PetSeekerSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetSeeker
        fields = ('location', 'bio','pic','pref','phone_num')

class UserSerializer(serializers.ModelSerializer):
    #pet_shelter = PetShelterSerializer(source='pet_shelter', read_only=True)
    #pet_seeker = PetSeekerSerializer(source='pet_seeker', read_only=True)
    #pet_shelter = PetShelterSerializer(read_only=True)
    #pet_seeker = PetSeekerSerializer(read_only=True)
    """location = models.CharField(max_length=200)
    shelter_name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)"""
    password2 = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = "__all__"

    def validate_password2(self, value):
        # Check if password and password2 match
        if self.initial_data['password'] != value:
            raise serializers.ValidationError("Passwords do not match.")
        return value

    """def validate_password(self, value):
        # Validate the password using Django's password validators
        validate_password(value)
        return value"""

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


    """def create(self, validated_data):
        #role = self.context['request'].data.get('role')
        # Extract pet_shelter or pet_seeker data from request data
        pet_shelter_data = self.context['request'].data.get('pet_shelter', {})
        pet_seeker_data = self.context['request'].data.get('pet_seeker', {})

        user = User.objects.create(**validated_data)

        if user.is_pet_shelter:
            user.is_pet_shelter = True
            p = PetShelter.objects.create(user=user, **pet_shelter_data)
            p.save()
        elif user.is_pet_seeker:
            user.is_pet_seeker = True
            f = PetSeeker.objects.create(user=user, **pet_seeker_data)
            f.save()

        user.save()
        return user
"""



'''
class UserSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email',)  # Add other fields as needed

class PetSeekerSerializer(ModelSerializer):
    #owner = UserSerializer()
    owner = PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = PetSeeker
        fields = '__all__'

class PetShelterSerializer(ModelSerializer):
    #user = UserSerializer()

    class Meta:
        model = PetShelter
        fields = '__all__'
'''
