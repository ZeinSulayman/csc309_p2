from rest_framework import generics
from .models import Pet
from .serializers import PetSerializer
from .filters import PetFilter
from rest_framework.pagination import PageNumberPagination


class PetPagination(PageNumberPagination):
    page_size = 10  # Number of items per page
    page_size_query_param = 'page_size'
    max_page_size = 100


class PetListCreateView(generics.ListCreateAPIView):
    queryset = Pet.objects.filter(status='available')
    serializer_class = PetSerializer
    filter_class = PetFilter

    def get_queryset(self):
        queryset = super().get_queryset()
        ordering = self.request.query_params.get('ordering', 'name')
        return queryset.order_by(ordering)


class PetRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pet.objects.all()
    serializer_class = PetSerializer
