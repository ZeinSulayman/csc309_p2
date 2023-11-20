import django_filters
from .models import Pet
from django_filters import rest_framework as filters

class PetFilter(filters.FilterSet):
    status = filters.CharFilter(method='filter_status')

    def filter_status(self, queryset, name, value):
        if value.lower() == 'all':
            return queryset
        else:
            return queryset.filter(status=value)

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
