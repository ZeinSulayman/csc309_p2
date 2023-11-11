from rest_framework.serializers import ModelSerializer, DateTimeField, ListField, \
    PrimaryKeyRelatedField, HyperlinkedRelatedField
from .models import Store


class BaseStoreSerializer(ModelSerializer):
    created_date = DateTimeField(read_only=True)

    class Meta:
        model = Store
        fields = '__all__'


class AdminStoreSerializer(BaseStoreSerializer):
    pass

