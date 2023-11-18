from rest_framework import serializers
from .models import PetApplication


class PetApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetApplication
        fields = ['first_name', 'last_name', 'dob', 'email', 'address', 'occupation',
                  'hours_away_weekdays', 'hours_away_weekends', 'medical_history',
                  'criminal_history', 'first_time_pet_owner', 'description']


class PetApplicationDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetApplication
        fields = "__all__"


class PetApplicationShelterUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetApplication
        fields = ['status']
        #fields = ['first_name']

    def validate_status(self, value):
        # Validate the allowed status transitions based on user type

        user_is_shelter = self.instance.applicant.is_pet_shelter
        current_status = self.instance.status if self.instance else None

        if user_is_shelter:
            if current_status != "pending" or value not in ["accepted", "denied"]:
                raise serializers.ValidationError('Invalid status transition for shelter')

        return value


class PetApplicationSeekerUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetApplication
        fields = ['status']

    def validate_status(self, value):
        # Validate the allowed status transitions based on user type
        user_is_seeker = self.instance.applicant.is_pet_seeker
        current_status = self.instance.status if self.instance else None

        if user_is_seeker:
            if value not in ["pending", "accepted"] and value != "withdrawn":
                raise serializers.ValidationError('Invalid status transition for seeker')

        return value
