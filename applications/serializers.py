from rest_framework import serializers
from .models import PetApplication


class PetApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetApplication
        fields = '__all__'


class PetApplicationUpdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = PetApplication
        fields = ['status']
        #fields = ['first_name']

    def validate_status(self, value):
        # Validate the allowed status transitions based on user type
        #user_is_shelter = self.context['request'].user.is_pet_shelter
        user_is_shelter = self.instance.applicant.is_pet_shelter
        current_status = self.instance.status if self.instance else None

        if user_is_shelter:
            if current_status == PetApplication.PENDING and value not in [PetApplication.ACCEPTED, PetApplication.DENIED]:
                raise serializers.ValidationError('Invalid status transition for shelter')
        else:
            if current_status in [PetApplication.PENDING, PetApplication.ACCEPTED] and value != PetApplication.WITHDRAWN:
                raise serializers.ValidationError('Invalid status transition for seeker')

        return value
