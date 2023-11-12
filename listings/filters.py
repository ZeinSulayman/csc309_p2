import django_filters
from .models import Pet

class PetFilter(django_filters.FilterSet):
    class Meta:
        model = Pet
        fields = {
            'owner': ['exact'],
            'status': ['exact'],
            'breed': ['exact', 'icontains'],
            'age': ['exact', 'lt', 'gt'],
            'size': ['exact'],
            'gender': ['exact'],
        }
