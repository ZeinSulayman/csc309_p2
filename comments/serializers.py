
from rest_framework import serializers
from .models import AppComments, ShelterComments

class AppCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppComments
        fields = ('content',)

class ShelterCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShelterComments
        fields = ('content',)
