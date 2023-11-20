from rest_framework import serializers
from .models import Notification


class NotifSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ('content','link')


class NotifEditSerializer(serializers.ModelSerializer):

    class Meta:
        model = Notification
        fields = ('read',)
